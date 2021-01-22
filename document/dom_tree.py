import docs
from config import TreeConfig
from attribute import get_attribute_count
from object import factory as of
from utils.random import Random

import itertools


# We do not merge those nodes from two into one.
merge_blacklist = [
    "SVGAnimateElement",
    "SVGAnimateMotionElement",
    "SVGAnimateTransformElement",
    "SVGSetElement",
]


class DOMTree:
    def __init__(self, max_element_count):
        self.root_svg = None
        self.root_elements = []
        self.element_count = 0
        self.max_element_count = max_element_count

    @property
    def elements(self):
        return list(itertools.chain(*self.root_elements))

    @property
    def full(self):
        return self.element_count >= self.max_element_count

    def add_root_element(self, element):
        index = Random.selector(len(self.root_elements) + 1)
        self.root_elements.insert(index, element)
        element.tree_depth = 0

    def add_root_svg_element(self, context):
        svg = of.create_object("SVGSVGElement")
        self.add_root_element(svg)
        self.init_element(context, svg)
        self.root_svg = svg

    def init_element(self, context, element):
        context.add_object(element)
        element.generate_mandatory_attributes(context)
        self.element_count += 1

    ################################################
    # For dumb fuzz
    ################################################
    def generate_html_elements(self, context, count):
        for _ in range(count):
            element = self.insert_root_element(context)
            element.generate_text()

    def generate_svg_elements(self, context, count):
        self.add_root_svg_element(context)
        for _ in range(count):
            child = self.root_svg.insert_child()
            if child is not None:
                self.init_element(context, child)
                child.generate_text()

    def generate_nodes(self, context):
        if Random.bool():
            self.generate_html_elements(context, TreeConfig.root_element_count)
        else:
            self.generate_html_elements(context, TreeConfig.root_element_count)
            self.generate_svg_elements(context, TreeConfig.root_element_count)
        # else:
        #    self.generate_svg_elements(context, TreeConfig.root_element_count)

        for _ in range(self.max_element_count):
            element = self.insert_element(context)
            if element is not None:
                element.generate_text()

    def generate_attributes(self, context):
        for element in self.elements:
            element.generate_attributes(context)

    ################################################
    # For cov fuzz
    ################################################
    # T1
    def insert_element(self, context):
        if self.full:
            return None

        parents = [e for e in self.elements if e.tree_depth < TreeConfig.max_depth]
        trial = 0
        while trial < len(parents):
            parent = Random.choice(parents)
            child = parent.insert_child()
            if child is not None:
                self.init_element(context, child)
                return child
            trial += 1

        return None

    # T2
    def insert_root_element(self, context):
        if self.full:
            return None

        if Random.selector(5) > 0:
            name = Random.choice(docs.html_general_child_elements)
        else:
            name = Random.choice(docs.html_other_child_elements)
        child = of.create_object(name)
        self.add_root_element(child)

        if child is not None:
            self.init_element(context, child)

        return child

    # T3
    def append_attribute(self, context):
        if self.element_count == 0:
            return False

        elements = self.elements
        trial = 0
        while trial < self.element_count:
            element = Random.choice(elements)
            if get_attribute_count(element.name) > 0 and element.append_attribute(context):
                return True
            trial += 1
        return False

    # T4
    def mutate_attribute(self, context):
        if self.element_count == 0:
            return False

        elements = self.elements
        trial = 0
        while trial < self.element_count:
            element = Random.choice(elements)
            if element.mutate_attribute(context):
                return True
            trial += 1
        return False

    # T5
    def replace_attribute(self, context):
        if self.element_count == 0:
            return False

        elements = self.elements
        trial = 0
        while trial < self.element_count:
            element = Random.choice(elements)
            if element.replace_attribute(context):
                return True
            trial += 1
        return False

    # T6
    def mutate_text(self):
        if self.element_count == 0:
            return False

        elements = self.elements
        trial = 0
        while trial < self.element_count:
            element = Random.choice(elements)
            if element.mutate_text():
                return True
            trial += 1
        return False

    def allow_merge(self):
        return self.element_count <= self.max_element_count

    def do_merge(self, element, context, other_element, merge_map, merge_inserts):
        # 1. merge two roots
        merge_map[other_element] = element
        element.merge_attributes(other_element)

        # 2. try to merge children
        for other_child in other_element.children:
            # 2.1 find the children with the same name
            ok = False
            if other_child.name not in merge_blacklist:
                for child in element.children:
                    if child not in merge_map.values() and child not in merge_inserts and \
                            child.name == other_child.name:
                        self.do_merge(child, context, other_child, merge_map, merge_inserts)
                        ok = True
            if ok:
                continue

            # 2.2 fail to find, directly insert
            element.add_child(other_child)
            for other_offspring in other_child:
                merge_inserts.append(other_offspring)
                other_offspring.id = None
                other_offspring.fix_depth()
                context.add_object(other_offspring)
                self.element_count += 1

    def merge(self, context, other, merge_map):
        merge_inserts = []

        elements = self.elements
        for other_root_element in other.root_elements:
            ok = False
            if other_root_element.name not in merge_blacklist:
                for element in elements:
                    if element not in merge_map.values() and element not in merge_inserts and \
                            element.name == other_root_element.name:
                        self.do_merge(element, context, other_root_element, merge_map, merge_inserts)
                        ok = True
            if ok:
                continue

            # fail to find, directly insert
            self.add_root_element(other_root_element)
            for other_offspring in other_root_element:
                merge_inserts.append(other_offspring)
                other_offspring.id = None
                other_offspring.fix_depth()
                context.add_object(other_offspring)
                self.element_count += 1

        return merge_inserts

    def __str__(self):
        s = ""
        for element in self.root_elements:
            s += str(element) + "\n"
        return s



