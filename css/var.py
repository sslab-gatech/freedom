from value.css import ColorValue
from value.css import LineWidthValue
from value.common import LengthValue, LengthPercentageValue
from utils.random import Random


class CSSVariables:
    def __init__(self):
        self.variables = [
            CSSVariableDeclaration("--css-color", ColorValue()),
            CSSVariableDeclaration("--css-length", LengthValue()),
            CSSVariableDeclaration("--css-length-percent", LengthPercentageValue()),
            CSSVariableDeclaration("--css-line-width", LineWidthValue()),
        ]

    def mutate(self, context) -> bool:
        var = Random.choice(self.variables)
        return var.mutate(context)

    def generate(self, context):
        for var in self.variables:
            var.generate(context)

    def merge_fix(self, merge_map):
        for var in self.variables:
            var.merge_fix(merge_map)

    def __str__(self):
        s = ":root {\n"
        for var in self.variables:
            s += "  {};\n".format(str(var))
        s += "}"
        return s


class CSSVariableDeclaration:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def mutate(self, context) -> bool:
        return self.value.mutate(context)

    def generate(self, context):
        self.value.generate(context)

    def merge_fix(self, merge_map):
        self.value.merge_fix(merge_map)

    def __str__(self):
        return "{}: {}".format(self.name, str(self.value))


