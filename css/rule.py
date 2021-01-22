from config import CSSConfig
from css.selector import create_css_selector
from css.declaration import CSSStyleDeclaration
from utils import dom_value as dv
from utils.random import Random

from abc import abstractmethod, ABCMeta


class CSSStyleRule:
    def __init__(self):
        self.selector = create_css_selector()
        self.declaration = CSSStyleDeclaration()

    def generate(self, context):
        self.selector.generate(context)
        self.declaration.generate(context)

    def append_selector(self, context):
        self.selector.append(context)

    def append_decl(self, context):
        self.declaration.append(context)

    def mutate(self, context) -> bool:
        c = Random.selector(10)
        if c == 0:
            self.selector.append(context)
            return True
        elif c == 1 or c == 2:
            return self.selector.mutate(context)
        else:
            return self.declaration.mutate(context)

    def merge_fix(self, merge_map):
        self.selector.merge_fix(merge_map)
        self.declaration.merge_fix(merge_map)

    def __str__(self):
        return "{} {{ {} }}".format(str(self.selector), str(self.declaration))


class CSSAtRule(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self, context):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class CSSKeyframeRule:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.declaration = CSSStyleDeclaration(animate=True)

    def generate(self, context):
        self.declaration.generate(context)

    def mutate(self, context) -> bool:
        return self.declaration.mutate(context)

    def merge(self, other):
        self.declaration.merge(other.declaration)

    def merge_fix(self, merge_map):
        self.declaration.merge_fix(merge_map)

    def __str__(self):
        return "{} {{ {} }}".format(self.name, str(self.declaration))


class CSSKeyframesRule(CSSAtRule):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.keyframe_rules = {}

    def generate_keyframe_name(self):
        while True:
            name = dv.keyframe_name()
            if name not in self.keyframe_rules:
                break
        return name

    def append_keyframe_rule(self, context):
        keyframe_name = self.generate_keyframe_name()
        keyframe_rule = CSSKeyframeRule(keyframe_name)
        keyframe_rule.generate(context)
        self.keyframe_rules[keyframe_name] = keyframe_rule

    def mutate(self, context) -> bool:
        if len(self.keyframe_rules) < CSSConfig.max_css_keyframe_count \
                    and Random.selector(3) == 0:
            self.append_keyframe_rule(context)
            return True
        else:
            keyframe_name, keyframe_rule = Random.choice(list(self.keyframe_rules.items()))
            if Random.selector(5) == 0:
                del self.keyframe_rules[keyframe_name]
                name = self.generate_keyframe_name()
                self.keyframe_rules[name] = keyframe_rule
                keyframe_rule.name = name
                return True
            else:
                return keyframe_rule.mutate(context)

    def generate(self, context):
        self.append_keyframe_rule(context)

    def merge(self, other):
        for name in other.keyframe_rules:
            if name in self.keyframe_rules:
                self.keyframe_rules[name].merge(other.keyframe_rules[name])
            else:
                self.keyframe_rules[name] = other.keyframe_rules[name]

    def merge_fix(self, merge_map):
        for keyframe_rule in self.keyframe_rules.values():
            keyframe_rule.merge_fix(merge_map)

    def __str__(self):
        s = "@keyframes {} {{\n".format(self.name)
        for keyframe_rule in self.keyframe_rules.values():
            s += "  " + str(keyframe_rule) + "\n"
        s += "}"
        return s


def create_css_style_rule():
    return CSSStyleRule()


def create_css_keyframes_rule(name):
    return CSSKeyframesRule(name)
