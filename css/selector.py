import docs
from config import CSSConfig
from utils import seq
from utils import dom_value as dv
from utils.random import Random

from abc import abstractmethod, ABCMeta
from enum import Enum


# TODO: an+b
def nth():
    if Random.bool():
        return Random.choice(["even", "odd"])
    else:
        return Random.integer()


class CSSSelector(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self, _):
        raise NotImplementedError

    def mutate(self, context) -> bool:
        self.generate(context)
        return True

    def merge_fix(self, merge_map):
        pass

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class CSSAtRuleSelector(CSSSelector):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def generate(self, _):
        pass
    
    def mutate(self, _) -> bool:
        return False

    def __str__(self):
        return "@{}".format(self.value)


# element
# FIXME: we only pick exist element names
class CSSElementSelector(CSSSelector):
    def __init__(self, scope=None):
        super().__init__()
        self.scope = scope
        self.value = None

    def generate(self, context):
        scope = None
        if self.scope is not None:
            scope = context.in_tree_set.intersection(set(self.scope))
        if scope is None or len(scope) == 0:
            scope = context.in_tree_set
        elem = Random.choice(list(scope))
        if elem is not None:
            self.value = docs.tag_from_element(elem)
        else:
            self.value = None

    def __str__(self):
        return self.value or "*"


# .class
class CSSClassSelector(CSSSelector):
    def __init__(self):
        super().__init__()
        self.cla = None

    def generate(self, context):
        self.cla = context.get_token("class")

    def __str__(self):
        if self.cla is None:
            return "*"
        return ".{}".format(self.cla)


# id
class CSSIDSelector(CSSSelector):
    def __init__(self, scope=None):
        super().__init__()
        self.scope = scope
        self.elem = None

    def generate(self, context):
        scope = self.scope
        if self.scope is None:
            scope = docs.elements
        self.elem = context.get_object(scope)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is None:
            return "*"
        return "#{}".format(self.elem.id)


# *
class CSSUniversalSelector(CSSSelector):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        pass

    def mutate(self, _) -> bool:
        return False

    def __str__(self):
        return "*"


def create_css_basic_selector(scope=None):
    c = Random.selector(4)
    if c == 0:
        return CSSUniversalSelector()
    elif c == 1:
        return CSSElementSelector(scope)
    elif c == 2:
        return CSSClassSelector()
    else:
        return CSSIDSelector(scope)


##########################################
# Pseudo class selectors
##########################################
# :x
# TODO: blank, has, local-link, is, nth-col, nth-last-col, target-within, user-invalid, where
class CSSPseudoClassSelector(CSSSelector):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.base = None

    def generate(self, context):
        self.base = create_css_basic_selector()
        self.base.generate(context)

    def __str__(self):
        return "{}:{}".format(str(self.base), self.name)


class CSSActiveSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("active")


class CSSAnyLinkSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("any-link")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_link_elements)
        self.base.generate(context)


class CSSCheckedSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("checked")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLOptionElement"])
        self.base.generate(context)


class CSSDefaultSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("default")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLButtonElement", "HTMLOptionElement"])
        self.base.generate(context)


class CSSDefinedSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("defined")


class CSSDirSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("dir")
        self.arg = None

    def generate(self, context):
        super(CSSDirSelector, self).generate(context)
        self.arg = Random.choice(["ltr", "rtl"])

    def __str__(self):
        s = super(CSSDirSelector, self).__str__()
        return "{}({})".format(s, self.arg)


class CSSDisabledSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("disabled")

    def generate(self, context):
        self.base = create_css_basic_selector([
            "HTMLButtonElement", "HTMLInputElement", "HTMLSelectElement", "HTMLTextAreaElement",
            "HTMLOptGroupElement", "HTMLOptionElement", "HTMLFieldSetElement"
        ])
        self.base.generate(context)


class CSSEmptySelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("empty")


class CSSEnabledSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("enabled")

    def generate(self, context):
        self.base = create_css_basic_selector([
            "HTMLButtonElement", "HTMLInputElement", "HTMLSelectElement", "HTMLTextAreaElement",
            "HTMLOptGroupElement", "HTMLOptionElement", "HTMLFieldSetElement"
        ])
        self.base.generate(context)


class CSSFirstSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("first")

    def generate(self, context):
        self.base = CSSAtRuleSelector("page")
        self.base.generate(context)


class CSSFirstChildSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("first-child")


class CSSFirstOfTypeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("first-of-type")


class CSSFullscreenSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("fullscreen")


class CSSFutureSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("future")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSFocusSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("focus")


class CSSFocusWithinSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("focus-within")


# FIXME: more selectors?; :host(); : host-context()
class CSSHostSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("host")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSHoverSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("hover")


class CSSIndeterminateSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("indeterminate")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLProgressElement"])
        self.base.generate(context)


class CSSInRangeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("in-range")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_submittable_elements)
        self.base.generate(context)


class CSSInvalidSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("invalid")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_submittable_elements)
        self.base.generate(context)


class CSSLangSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("lang")
        self.lang = None

    def generate(self, context):
        super(CSSLangSelector, self).generate(context)
        self.lang = dv.lang()

    def __str__(self):
        s = super(CSSLangSelector, self).__str__()
        return "{}({})".format(s, self.lang)


class CSSLastChildSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("last-child")


class CSSLastOfTypeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("last-of-type")


class CSSLeftSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("left")

    def generate(self, context):
        self.base = CSSAtRuleSelector("page")
        self.base.generate(context)


class CSSLinkSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("link")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_link_elements)
        self.base.generate(context)


class CSSNotSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("not")
        self.selector = None

    def generate(self, context):
        super(CSSNotSelector, self).generate(context)
        self.selector = create_css_basic_selector()
        self.selector.generate(context)

    def __str__(self):
        s = super(CSSNotSelector, self).__str__()
        return "{}({})".format(s, str(self.selector))


class CSSNthChildSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("nth-child")
        self.nth = None

    def generate(self, context):
        super(CSSNthChildSelector, self).generate(context)
        self.nth = nth()

    def __str__(self):
        s = super(CSSNthChildSelector, self).__str__()
        return "{}({})".format(s, self.nth)


class CSSNthLastChildSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("nth-last-child")
        self.nth = None

    def generate(self, context):
        super(CSSNthLastChildSelector, self).generate(context)
        self.nth = nth()

    def __str__(self):
        s = super(CSSNthLastChildSelector, self).__str__()
        return "{}({})".format(s, self.nth)


class CSSNthLastOfTypeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("nth-last-of-type")
        self.nth = None

    def generate(self, context):
        super(CSSNthLastOfTypeSelector, self).generate(context)
        self.nth = nth()

    def __str__(self):
        s = super(CSSNthLastOfTypeSelector, self).__str__()
        return "{}({})".format(s, self.nth)


class CSSNthOfTypeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("nth-of-type")
        self.nth = None

    def generate(self, context):
        super(CSSNthOfTypeSelector, self).generate(context)
        self.nth = nth()

    def __str__(self):
        s = super(CSSNthOfTypeSelector, self).__str__()
        return "{}({})".format(s, self.nth)


class CSSOnlyChildSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("only-child")


class CSSOnlyOfTypeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("only-of-type")


class CSSOptionalSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("optional")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLSelectElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSOutOfRangeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("out-of-range")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_submittable_elements)
        self.base.generate(context)


class CSSPastSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("past")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSPlaceholderShownSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("placeholder-shown")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSReadOnlySelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("read-only")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSReadWriteSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("read-write")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSRequiredSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("required")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLSelectElement", "HTMLInputElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSRightSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("right")

    def generate(self, context):
        self.base = CSSAtRuleSelector("page")
        self.base.generate(context)


class CSSRootSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("root")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSScopeSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("scope")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSTargetSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("target")


class CSSValidSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("valid")

    def generate(self, context):
        self.base = create_css_basic_selector([
            "HTMLButtonElement", "HTMLInputElement", "HTMLObjectElement",
            "HTMLSelectElement", "HTMLTextAreaElement",
            "HTMLFormElement", "HTMLFieldSetElement"
        ])
        self.base.generate(context)


class CSSVisitedSelector(CSSPseudoClassSelector):
    def __init__(self):
        super().__init__("visited")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_link_elements)
        self.base.generate(context)


##########################################
# Pseudo element selectors
##########################################
# TODO: backdrop, cue-region, grammar-error, slotted, spelling-error
class CSSPseudoElementSelector(CSSSelector):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.base = None

    def generate(self, context):
        self.base = create_css_basic_selector()
        self.base.generate(context)

    def __str__(self):
        return "{}::{}".format(str(self.base), self.name)


class CSSAfterSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("after")


class CSSBeforeSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("before")


class CSSCueSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("cue")

    def generate(self, context):
        self.base = CSSUniversalSelector()
        self.base.generate(context)


class CSSFirstLetterSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("first-letter")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_block_elements)
        self.base.generate(context)


class CSSFirstLineSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("first-line")

    def generate(self, context):
        self.base = create_css_basic_selector(docs.html_block_elements)
        self.base.generate(context)


class CSSMarkerSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("marker")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLLIElement", "HTMLSummaryElement"])
        self.base.generate(context)


class CSSPartSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("part")
        self.part = None

    def generate(self, context):
        super(CSSPartSelector, self).generate(context)
        self.part = context.get_token("part")

    def __str__(self):
        s = super(CSSPartSelector, self).__str__()
        return "{}({})".format(s, self.part)


class CSSPlaceholderSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("placeholder")

    def generate(self, context):
        self.base = create_css_basic_selector(["HTMLInputElement", "HTMLTextAreaElement"])
        self.base.generate(context)


class CSSSelectionSelector(CSSPseudoElementSelector):
    def __init__(self):
        super().__init__("selection")


##########################################
# Group
##########################################
class CSSCombinator(CSSSelector):
    def __init__(self, op):
        super().__init__()
        self.op = op
        self.a = None
        self.b = None

    def generate(self, context):
        self.a = create_css_basic_selector()
        self.a.generate(context)
        self.b = create_css_basic_selector()
        self.b.generate(context)

    def mutate(self, context):
        c = Random.selector(4)
        if c == 0:
            return self.a.mutate(context)
        elif c == 1:
            return self.b.mutate(context)
        elif c == 2:
            ok = self.a.mutate(context)
            ok = ok or self.b.mutate(context)
            return ok
        else:
            self.generate(context)
            return True

    def merge_fix(self, merge_map):
        self.a.merge_fix(merge_map)
        self.b.merge_fix(merge_map)

    def __str__(self):
        return "{}{}{}".format(str(self.a), self.op, str(self.b))


class CSSDescendantCombinator(CSSCombinator):
    def __init__(self):
        super().__init__(" ")


class CSSChildCombinator(CSSCombinator):
    def __init__(self):
        super().__init__(">")


class CSSGeneralSiblingCombinator(CSSCombinator):
    def __init__(self):
        super().__init__("~")


class CSSAdjacentSiblingCombinator(CSSCombinator):
    def __init__(self):
        super().__init__("+")


css_basic_selectors = [
    # basic selectors
    CSSElementSelector,
    CSSClassSelector,
    CSSIDSelector
]

css_special_selectors = [
    CSSUniversalSelector,

    # pseudo class selectors
    CSSActiveSelector,
    CSSAnyLinkSelector,
    CSSCheckedSelector,
    CSSDefaultSelector,
    CSSDefinedSelector,
    CSSDirSelector,
    CSSDisabledSelector,
    CSSEmptySelector,
    CSSEnabledSelector,
    # CSSFirstSelector,
    CSSFirstChildSelector,
    CSSFirstOfTypeSelector,
    CSSFullscreenSelector,
    # CSSFutureSelector,
    CSSFocusSelector,
    CSSFocusWithinSelector,
    CSSHostSelector,
    CSSHoverSelector,
    CSSIndeterminateSelector,
    CSSInRangeSelector,
    CSSInvalidSelector,
    # CSSLangSelector,
    CSSLastChildSelector,
    CSSLastOfTypeSelector,
    # CSSLeftSelector,
    CSSLinkSelector,
    CSSNotSelector,
    CSSNthChildSelector,
    CSSNthLastChildSelector,
    CSSNthLastOfTypeSelector,
    CSSNthOfTypeSelector,
    CSSOnlyChildSelector,
    CSSOnlyOfTypeSelector,
    CSSOptionalSelector,
    CSSOutOfRangeSelector,
    # CSSPastSelector,
    CSSPlaceholderShownSelector,
    CSSReadOnlySelector,
    CSSReadWriteSelector,
    CSSRequiredSelector,
    # CSSRightSelector,
    CSSRootSelector,
    CSSScopeSelector,
    CSSTargetSelector,
    CSSValidSelector,
    CSSVisitedSelector,

    # pseudo element selectors
    CSSAfterSelector,
    CSSBeforeSelector,
    CSSCueSelector,
    CSSFirstLetterSelector,
    CSSFirstLineSelector,
    CSSMarkerSelector,
    CSSPartSelector,
    CSSPlaceholderSelector,
    CSSSelectionSelector,

    # Combinators
    CSSDescendantCombinator,
    CSSChildCombinator,
    CSSGeneralSiblingCombinator,
    CSSAdjacentSiblingCombinator
]


# <selector> = <selector>, <selector>
class CSSGroupSelector(CSSSelector):
    def __init__(self):
        super().__init__()
        self.selectors = []

    @property
    def selector_count(self):
        return len(self.selectors)

    def append(self, context):
        if self.selector_count >= CSSConfig.max_css_selector_count:
            return False
        selector = create_css_simple_selector()
        selector.generate(context)
        self.selectors.append(selector)
        return True

    def generate(self, context):
        self.append(context)
    
    def mutate(self, context) -> bool:
        c = Random.selector(3)
        if c == 0:
            # 1. mutate one
            selector = Random.choice(self.selectors)
            return selector.mutate(context)
        elif c == 1:
            # 2. replace one
            if len(self.selectors) == 0:
                return False
            del self.selectors[Random.selector(len(self.selectors))]
            self.append(context)
            return True
        else:
            if len(self.selectors) >= CSSConfig.max_css_selector_count:
                return False
            self.append(context)
            return True

    def merge_fix(self, merge_map):
        for selector in self.selectors:
            selector.merge_fix(merge_map)

    def __str__(self):
        return seq(list(map(str, self.selectors)))


class CSSSelectorType(Enum):
    Basic = 1
    Pseudo = 2


def create_css_simple_selector():
    if Random.bool():
        selector = Random.choice(css_basic_selectors)
    else:
        selector = Random.choice(css_special_selectors)
    return selector()


def create_css_selector():
    return CSSGroupSelector()
