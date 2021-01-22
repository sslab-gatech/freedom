import docs
from config import TreeConfig
from attribute import get_attribute_count, get_attribute_templates, mandatory_attributes
from utils.random import Random

from itertools import chain


def get_object_id(obj):
    return obj.id


class Object:
    def __init__(self, name, _id=None):
        self.id = _id
        self.name = name

    @property
    def is_element(self):
        return False


# Element here only represents the low-level concrete Element instances.
class Element(Object):
    def __init__(self, name):
        super().__init__(name)
        self.tag = None
        self.parent = None
        self.children = []
        self.attributes = {}
        self.tree_depth = None

        self.ahead_text = None
        self.last_text = None

    @property
    def children_count(self):
        return len(self.children)

    @property
    def is_element(self):
        return True

    @property
    def is_in_tree(self):
        return self.tree_depth is not None

    @property
    def is_empty(self):
        return self.children_count == 0

    @property
    def attribute_count(self):
        return len(self.attributes)

    @property
    def additional_label(self):
        return ""

    def has_attribute(self, name):
        return name in self.attributes

    def get_attribute(self, name):
        return self.attributes.get(name)

    def add_attribute(self, attr):
        self.attributes[attr.name] = attr

    def add_child(self, child):
        # always insert into a random location :)
        index = Random.selector(len(self.children) + 1)
        self.children.insert(index, child)
        child.parent = self
        child.tree_depth = self.tree_depth + 1

    def mutate_text(self):
        raise NotImplementedError

    def generate_attribute(self, context, template):
        attr = template.instantiate()
        attr.generate(context)
        return attr

    def generate_mandatory_attributes(self, context):
        if self.name in mandatory_attributes:
            templates = mandatory_attributes[self.name]
            for template in templates:
                attr = self.generate_attribute(context, template)
                assert attr is not None
                attr.mandatory = True
                self.add_attribute(attr)

    ################################################
    # For dumb fuzz
    ################################################
    def generate_attributes(self, context):
        avail_attr_count = get_attribute_count(self.name)
        if avail_attr_count >= 20:
            total_count = TreeConfig.max_attribute_count
        elif avail_attr_count >= 10:
            total_count = Random.range(5, avail_attr_count)
        elif avail_attr_count >= 1:
            total_count = Random.range(1, avail_attr_count)
        else:
            total_count = 0
        for _ in range(total_count):
            self.append_attribute(context)

    ################################################
    # For cov fuzz
    ################################################
    def append_attribute(self, context):
        if self.attribute_count >= TreeConfig.max_attribute_count:
            return False

        templates = get_attribute_templates(self.name)
        assert len(templates) > 0

        trial = 0
        while trial < 10:
            template = Random.choice(templates)
            if not self.has_attribute(template.attr):
                attr = self.generate_attribute(context, template)
                if attr is not None:
                    self.add_attribute(attr)
                    return True
            trial += 1
        return False

    def mutate_attribute(self, context):
        if self.attribute_count == 0:
            return False

        trial = 0
        attribute_names = list(self.attributes.keys())
        while trial < self.attribute_count:
            name = Random.choice(attribute_names)
            attribute = self.attributes[name]
            if not attribute.mandatory:
                attribute.mutate(context)
                return True
            trial += 1
        return False

    def replace_attribute(self, context):
        if self.attribute_count == 0:
            return False

        trial = 0
        attribute_names = list(self.attributes.keys())
        while trial < self.attribute_count:
            name = Random.choice(attribute_names)
            attribute = self.attributes[name]
            if not attribute.mandatory:
                del self.attributes[name]
                return self.append_attribute(context)
            trial += 1
        return False

    def merge_attributes(self, other):
        for name in other.attributes:
            if not self.has_attribute(name):
                self.add_attribute(other.attributes[name])

    def fix_depth(self):
        if self.parent is not None:
            self.tree_depth = self.parent.tree_depth + 1

    def merge_fix(self, merge_map):
        for attr in self.attributes.values():
            attr.merge_fix(merge_map)

    def __iter__(self):
        yield self
        for elem in chain(*map(iter, self.children)):
            yield elem

    def __str__(self):
        s = ""
        if self.ahead_text is not None:
            s += self.ahead_text + "\n"
        s += "<{} id=\"{}\"".format(self.tag, self.id)
        s += self.additional_label
        for name, attr in self.attributes.items():
            s += " {}".format(str(attr))

        if docs.is_html_empty_element(self.name):
            s += ">"
            # assert self.children_count == 0 and self.text is None
            return s

        s += ">\n"
        for child in self.children:
            s += str(child) + "\n"
        if self.last_text:
            s += self.last_text + "\n"
        s += "</{}>".format(self.tag)
        return s
