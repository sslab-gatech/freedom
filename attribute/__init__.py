import docs
from config import TreeConfig
from utils.random import Random

from enum import Enum

regular_attributes = {}
presentation_attributes = {}
global_attributes = {}
aria_attributes = {}
mandatory_attributes = {}

svg_animatable_regular_attributes = {}
svg_animatable_presentation_attributes = {}
svg_animatable_transform_attributes = {}

attributes_count = {}


class AttributeType(Enum):
    REGULAR = 1
    PRESENTATION = 2
    GLOBAL = 3
    ARIA = 4


attribute_types = [
    AttributeType.REGULAR,
    AttributeType.PRESENTATION,
    AttributeType.GLOBAL,
    AttributeType.ARIA
]


def get_attribute_templates(name, include_aria=False):
    selector = Random.choices(attribute_types, [
        TreeConfig.attribute_weight["regular"] * len(regular_attributes[name])
        if name in regular_attributes else 0,
        TreeConfig.attribute_weight["presentation"] * len(presentation_attributes[name])
        if name in presentation_attributes else 0,
        TreeConfig.attribute_weight["global"] * len(global_attributes[name])
        if name in global_attributes else 0,
        TreeConfig.attribute_weight["aria"] * len(aria_attributes[name])
        if include_aria and name in aria_attributes else 0
    ])[0]

    if selector == AttributeType.REGULAR:
        return regular_attributes[name]
    elif selector == AttributeType.PRESENTATION:
        return presentation_attributes[name]
    elif selector == AttributeType.GLOBAL:
        return global_attributes[name]
    else:
        return aria_attributes[name]


class Attribute:
    def __init__(self, elem, name, value):
        self.elem = elem
        self.name = name
        self.value = value
        self.mandatory = False

    def generate(self, context):
        self.value.generate(context)

    def mutate(self, context):
        self.value.mutate(context)

    def merge_fix(self, merge_map):
        self.value.merge_fix(merge_map)

    def __str__(self):
        # assert str(self.value) != ""
        return "{}=\"{}\"".format(self.name, str(self.value))


class AttributeTemplate:
    def __init__(self, elem, attr, value_class):
        self.elem = elem
        self.attr = attr
        self.value_class = value_class

    def instantiate(self):
        if self.value_class is not None:
            value = self.value_class()
        else:
            value = None
        return Attribute(self.elem, self.attr, value)


def get_attribute_count(elem):
    count = attributes_count.get(elem)
    if count is None:
        return 0
    return count


def update_attribute_count(elem):
    if elem not in attributes_count:
        attributes_count[elem] = 0
    attributes_count[elem] += 1


def add_regular_attribute(at):
    elem = at.elem
    if elem not in regular_attributes:
        regular_attributes[elem] = []
    regular_attributes[elem].append(at)
    update_svg_animatable_attribute(at, True)
    update_attribute_count(elem)


def add_presentation_attribute(at):
    elem = at.elem
    if elem not in presentation_attributes:
        presentation_attributes[elem] = []
    presentation_attributes[elem].append(at)
    update_svg_animatable_attribute(at, False)
    update_attribute_count(elem)


def add_global_attribute(at):
    elem = at.elem
    if elem not in global_attributes:
        global_attributes[elem] = []
    global_attributes[elem].append(at)
    update_attribute_count(elem)


def add_aria_attribute(at):
    elem = at.elem
    if elem not in aria_attributes:
        aria_attributes[elem] = []
    aria_attributes[elem].append(at)


def add_mandatory_attribute(at):
    elem = at.elem
    if elem not in mandatory_attributes:
        mandatory_attributes[elem] = []
    mandatory_attributes[elem].append(at)


def update_svg_animatable_attribute(at, is_regular):
    elem = at.elem
    if docs.is_svg_element(elem):
        if at.attr in docs.svg_animatable_attributes:
            if is_regular:
                if elem not in svg_animatable_regular_attributes:
                    svg_animatable_regular_attributes[elem] = []
                svg_animatable_regular_attributes[elem].append(at)
            else:
                if elem not in svg_animatable_presentation_attributes:
                    svg_animatable_presentation_attributes[elem] = []
                svg_animatable_presentation_attributes[elem].append(at)

        if at.attr in docs.svg_animatable_transform_attributes:
            if elem not in svg_animatable_transform_attributes:
                svg_animatable_transform_attributes[elem] = []
            svg_animatable_transform_attributes[elem].append(at)


def get_svg_animatable_attribute(elem):
    has_regular = elem in svg_animatable_regular_attributes
    has_presentation = elem in svg_animatable_presentation_attributes

    if (not has_presentation) or (has_regular and Random.bool()):
        return Random.choice(svg_animatable_regular_attributes[elem])
    else:
        return Random.choice(svg_animatable_presentation_attributes[elem])


def get_svg_animatable_transform_attribute(elem):
    return Random.choice(svg_animatable_transform_attributes[elem])


def print_attribute_count():
    for name, count in attributes_count.items():
        print("{}: {}".format(name, count))
