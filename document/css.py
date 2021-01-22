from config import CSSConfig
from css.var import CSSVariables
from css.rule import create_css_style_rule, create_css_keyframes_rule
from utils.random import Random


class CSS:
    def __init__(self):
        self.css_variables = None
        self.css_style_rules = []
        self.css_keyframes_rules = []

    def init_keyframes(self, context):
        # add @keyframes
        keyframes = context.get_tokens("keyframes")
        for kf in keyframes:
            kf_rule = create_css_keyframes_rule(kf)
            kf_rule.generate(context)
            self.css_keyframes_rules.append(kf_rule)

    def init_css_variables(self, context):
        self.css_variables = CSSVariables()
        self.css_variables.generate(context)

    ############################################
    # For dumb fuzz
    ############################################
    def generate_css_rules(self, context):
        for _ in range(CSSConfig.max_css_count):
            self.append_css_style_rule(context)

        for rule in self.css_style_rules:
            for _ in range(Random.range(0, CSSConfig.max_css_selector_count - 1)):
                rule.append_selector(context)
            for _ in range(CSSConfig.max_css_decl_count - 1):
                rule.append_decl(context)

        for rule in self.css_keyframes_rules:
            for _ in range(Random.range(1, CSSConfig.max_css_keyframe_count)):
                rule.append_keyframe_rule(context)

    ############################################
    # For cov fuzz
    ############################################
    def append_css_style_rule(self, context):
        if len(self.css_style_rules) >= CSSConfig.max_css_count:
            return False
        css_rule = create_css_style_rule()
        css_rule.generate(context)
        self.css_style_rules.append(css_rule)
        return True

    def replace_css_style_rule(self, context):
        count = len(self.css_style_rules)
        if count == 0:
            return False
        del self.css_style_rules[Random.selector(count)]
        return self.append_css_style_rule(context)

    def mutate_css_style_rule(self, context):
        count = len(self.css_style_rules)
        if count == 0:
            return False
        trial = 0
        while trial < count:
            rule = Random.choice(self.css_style_rules)
            if rule.mutate(context):
                return True
            trial += 1
        return False

    def mutate_css_keyframes_rule(self, context):
        count = len(self.css_keyframes_rules)
        if count == 0:
            return False

        trial = 0
        while trial < count:
            rule = Random.choice(self.css_keyframes_rules)
            if rule.mutate(context):
                return True
            trial += 1
        return False

    def mutate_css_variable(self, context):
        return self.css_variables.mutate(context)

    def allow_merge(self):
        return len(self.css_style_rules) <= CSSConfig.max_css_count

    def merge(self, other, merge_map):
        for rule in other.css_style_rules:
            rule.merge_fix(merge_map)
        for rule in other.css_keyframes_rules:
            rule.merge_fix(merge_map)

        self.css_style_rules.extend(other.css_style_rules)
        for i in range(len(self.css_keyframes_rules)):
            self.css_keyframes_rules[i].merge(other.css_keyframes_rules[i])

    def __str__(self):
        s = "<style>\n"
        for rule in self.css_style_rules:
            s += str(rule) + "\n"
        s += "</style>\n\n"
        s += "<style>\n"
        for rule in self.css_keyframes_rules:
            s += str(rule) + "\n"
        s += "</style>\n\n"
        s += "<style>\n"
        s += str(self.css_variables) + "\n"
        s += "</style>\n"
        return s
