from config import CSSConfig
from css import get_css_property
from value import DynamicValue
from utils import semi
from utils.random import Random


class CSSDeclaration:
    def __init__(self, prop, value):
        self.prop = prop
        self.value = value

    def generate(self, context):
        self.value.generate(context)
    
    def mutate(self, context) -> bool:
        return self.value.mutate(context)

    def merge_fix(self, merge_map):
        self.value.merge_fix(merge_map)

    def __str__(self):
        return "{}: {}".format(self.prop, str(self.value))


def create_css_declaration(animatable=False):
    prop, value_class = get_css_property(animatable)
    return CSSDeclaration(prop, value_class())


class CSSStyleDeclaration:
    def __init__(self, animate=False):
        self.animate = animate
        self.declarations = []

    def append(self, context):
        if len(self.declarations) >= CSSConfig.max_css_decl_count:
            return False
        decl = create_css_declaration(self.animate)
        decl.generate(context)
        self.declarations.append(decl)
        return True

    def mutate(self, context) -> bool:
        c = Random.selector(4)
        if c == 0 or len(self.declarations) == 0:
            return self.append(context)
        elif c == 1:
            del self.declarations[Random.selector(len(self.declarations))]
            return self.append(context)
        else:
            decl = Random.choice(self.declarations)
            return decl.mutate(context)

    def generate(self, context):
        self.append(context)

    def merge(self, other):
        self.declarations.extend(other.declarations)

    def merge_fix(self, merge_map):
        for decl in self.declarations:
            decl.merge_fix(merge_map)

    def __str__(self):
        return semi(list(map(str, self.declarations)))


class CSSStyleDeclarationValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.style_declaration = CSSStyleDeclaration()

    def generate(self, context):
        self.style_declaration.generate(context)
        for _ in range(CSSConfig.max_css_internal_decl_count - 1):
            self.style_declaration.append(context)

    def mutate(self, context) -> bool:
        return self.style_declaration.mutate(context)

    def merge_fix(self, merge_map):
        self.style_declaration.merge_fix(merge_map)

    def __str__(self):
        return str(self.style_declaration)
