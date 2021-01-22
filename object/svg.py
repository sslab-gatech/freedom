import docs
from object import Element
from object.html import HTMLElement
from attribute import Attribute
from attribute import svg
from attribute import get_svg_animatable_attribute, get_svg_animatable_transform_attribute
from value import ConstValue
from value.svg import FromValue, AnimationValuesValue, \
    KeySplinesValue, KeyPointsValue, KeyTimesValue
from utils import dom_value as dv
from utils.random import Random


class SVGElement(Element):
    def __init__(self, name):
        super().__init__(name)
        self.tag = docs.svg_tag_from_element(name)

    @staticmethod
    def create(name):
        if name == "SVGAnimateElement" or name == "SVGAnimateMotionElement" \
                or name == "SVGAnimateTransformElement" or name == "SVGSetElement":
            return SVGAnimationElement(name)
        elif name in docs.svg_filter_primitives:
            return SVGFilterPrimitive(name)
        elif name == "SVGForeignObjectElement":
            return SVGForeignObjectElement(name)
        elif name == "SVGGlyphElement":
            return SVGGlyphElement(name)
        else:
            return SVGElement(name)

    def generate_child(self, child_name):
        child = SVGElement.create(child_name)
        self.add_child(child)
        return child

    def generate_text(self):
        if docs.is_svg_text_element(self.name) and Random.selector(5) == 0:
            self.last_text = Random.string()
        if self.parent is None or docs.is_svg_text_element(self.parent.name) and \
                Random.selector(5) == 0:
            self.ahead_text = Random.string()

    def mutate_text(self) -> bool:
        if Random.bool():
            if docs.is_svg_text_element(self.name):
                self.last_text = Random.string()
                return True
            return False
        else:
            if self.parent is None or docs.is_svg_text_element(self.parent.name):
                self.ahead_text = Random.string()
                return True
            return False

    def insert_child(self):
        children = docs.svg_child_elements.get(self.name)

        if len(children) == 0:
            return None

        child = Random.choice(children)
        return self.generate_child(child)


class SVGAnimationElement(SVGElement):
    def __init__(self, name):
        super().__init__(name)
        self.value_class = None
        self.value_count = None
        self.type = None

        if self.name == "SVGAnimateMotionElement":
            self.value_class = svg.CoordinateValue
        if self.name != "SVGSetElement":
            if Random.bool():
                self.value_count = max(1, dv.list_size())

    # SVGSetElement / SVGAnimateElement / SVGAnimateTransformElement
    # FIXME: Now only mutate parent node
    # FIXME: Now do not change mandatory attribute values when generating setAttribute()
    def generate_attribute_name(self, context, template):
        if self.parent is None:
            return None

        if self.has_attribute("attributeName"):
            exist = self.get_attribute("attributeName")
            attr = Attribute(self.name, "attributeName", ConstValue(str(exist.value)))
            return attr

        attr = template.instantiate()
        if self.name == "SVGAnimateTransformElement":
            template = get_svg_animatable_transform_attribute(self.parent.name)
        else:
            template = get_svg_animatable_attribute(self.parent.name)

        # setup value class
        if self.name == "SVGAnimateElement" or self.name == "SVGSetElement":
            self.value_class = template.value_class

        attr.value = ConstValue(template.attr)
        attr.generate(context)
        return attr

    # SVGAnimateTransformElement
    def generate_type(self, context, template):
        if self.has_attribute("type"):
            exist = self.get_attribute("type")
            attr = Attribute(self.name, "type", ConstValue(str(exist.value)))
            return attr

        attr = template.instantiate()
        attr.generate(context)
        _type = str(attr.value)
        if _type == "translate":
            self.value_class = svg.TransformTranslateValue
        elif _type == "scale":
            self.value_class = svg.TransformScaleValue
        elif _type == "rotate":
            self.value_class = svg.TransformRotateValue
        else:
            self.value_class = svg.TransformSkewXValue
        return attr

    def generate_value(self, context, template):
        if self.value_class is None:
            return None
        attr = template.instantiate()
        attr.value = FromValue(self.value_class)
        attr.generate(context)
        return attr

    def generate_values(self, context, template):
        if self.value_class is None or self.value_count is None:
            return None
        attr = template.instantiate()
        attr.value = AnimationValuesValue(self.value_class, self.value_count)
        attr.generate(context)
        return attr

    def generate_key_splines(self, context, template):
        value_count = self.value_count
        if value_count is None:
            value_count = 2
        attr = template.instantiate()
        attr.value = KeySplinesValue(value_count)
        attr.generate(context)
        return attr

    def generate_key_points(self, context, template):
        value_count = self.value_count
        if value_count is None:
            value_count = 2
        attr = template.instantiate()
        attr.value = KeyPointsValue(value_count)
        attr.generate(context)
        return attr

    def generate_key_times(self, context, template):
        value_count = self.value_count
        if value_count is None:
            value_count = 2
        attr = template.instantiate()
        attr.value = KeyTimesValue(value_count)
        attr.generate(context)
        return attr

    def generate_attribute(self, context, template):
        attr_name = template.attr
        if attr_name == "attributeName":
            return self.generate_attribute_name(context, template)
        elif attr_name == "type":
            return self.generate_type(context, template)
        elif attr_name == "from" or attr_name == "to" or attr_name == "by":
            return self.generate_value(context, template)
        elif attr_name == "values":
            return self.generate_values(context, template)
        elif attr_name == "keySplines":
            return self.generate_key_splines(context, template)
        elif attr_name == "keyTimes":
            return self.generate_key_times(context, template)
        elif attr_name == "keyPoints":
            return self.generate_key_points(context, template)
        else:
            return super(SVGAnimationElement, self).generate_attribute(context, template)


class SVGFilterPrimitive(SVGElement):
    @property
    def additional_label(self):
        return " result=\"{}\"".format(self.id)


class SVGForeignObjectElement(SVGElement):
    def __init__(self, name):
        super().__init__(name)

    def generate_child(self, child_name):
        child = HTMLElement.create(child_name)
        self.add_child(child)
        return child

    def insert_child(self):
        if Random.selector(5) > 0:
            child_name = Random.choice(docs.html_general_child_elements)
        else:
            child_name = Random.choice(docs.html_other_child_elements)
        return self.generate_child(child_name)

    def __str__(self):
        s = "<{} id=\"{}\"".format(self.tag, self.id)
        for name, attr in self.attributes.items():
            s += " {}".format(str(attr))

        if self.children_count == 0:
            s += "/>"
        else:
            s += ">\n"
            s += "<body xmlns=\"http://www.w3.org/1999/xhtml\">\n"
            for child in self.children:
                s += str(child) + "\n"
            s += "</body>\n"
            s += "</{}>".format(self.tag)
        return s


class SVGGlyphElement(SVGElement):
    @property
    def additional_label(self):
        return " glyph-name=\"{}\"".format(self.id)
