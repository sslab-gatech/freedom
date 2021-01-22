from js import add_api, is_satiable_arg, API, APITemplate
from js.property import StorePropertyTemplate, LoadPropertyTemplate
from js.arg import StringArg, CharArg, BooleanArg, ClockArg, FloatArg, ColorArg, \
    RandomSelectorArg, ClockInMsArg, IntegerArg, LengthPercentageArg, IndexArg, \
    RegexArg
from js.arg import html as ha
from js.ret import html as hr
from utils.random import Random


#####################################
# var x = y[i % y.length]
#####################################
class ArrayLoadIndex(API):
    def __init__(self, ret, this, selector):
        super().__init__(ret, this)
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.selector.generate(context)
        if self.ret is not None:
            self.ret.generate(context)

    def mutate(self, context):
        if Random.bool():
            self.this.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        lhs = ""
        if self.ret is not None:
            lhs = "var {} = ".format(str(self.ret))
        return lhs + "{0}[{1} % {0}.length]".format(str(self.this), str(self.selector))


class ArrayLoadIndexTemplate(APITemplate):
    def __init__(self, ret_class, this_class):
        super().__init__(ret_class, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        ret = self.ret_class() if self.ret_class is not None else None
        return ArrayLoadIndex(ret, self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


#####################################
# x[i] = y
#####################################
class ArrayStoreIndex(API):
    def __init__(self, value, this, selector):
        super().__init__(None, this)
        self.value = value
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.value.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.value.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.value.merge_fix(merge_map)

    def __str__(self):
        return "{0}[{1} % ({0}.length + 1)] = {2}".format(str(self.this), str(self.selector), str(self.value))


class ArrayStoreIndexTemplate(APITemplate):
    def __init__(self, value_class, this_class):
        super().__init__(None, this_class)
        self.value_class = value_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return ArrayStoreIndex(self.value_class(), self.this_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.value_class, context)


#####################################
# <new DOMString> = <DOMStringMap>[<DOMString>];
# <DOMStringMap>[<DOMString>] = <DOMString>;
#####################################
class DOMStringMapStoreIndex(API):
    def __init__(self, value, this, index):
        super().__init__(None, this)
        self.value = value
        self.index = index

    def generate(self, context):
        self.this.generate(context)
        self.value.generate(context)
        self.index.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.value.mutate(context)
        else:
            self.index.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "{0}[{1}] = {2}".format(str(self.this), str(self.index), str(self.value))


class DOMStringMapStoreIndexTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.index_class = StringArg
        self.value_class = StringArg

    def instantiate(self):
        return DOMStringMapStoreIndex(self.value_class(), self.this_class(), self.index_class())

    def satiable(self, context):
        return True


def initialize_html_properties():
    ######################################################
    # CSS
    ######################################################
    # StyleSheet
    # FIXME: We do not support write .disabled.
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "href"))
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "ownerNode"))
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "parentStyleSheet"))
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "title"))
    add_api(LoadPropertyTemplate(hr.MediaListRet, ha.StyleSheetArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.StyleSheetArg, "disabled"))

    # CSSStyleSheet
    add_api(LoadPropertyTemplate(None, ha.CSSStyleSheetArg, "ownerRule"))
    add_api(LoadPropertyTemplate(hr.CSSStyleRuleListRet, ha.CSSStyleSheetArg, "cssRules"))

    # CSSKeyframesSheet
    add_api(LoadPropertyTemplate(hr.CSSKeyframesRuleListRet, ha.CSSKeyframesSheetArg, "cssRules"))

    # CSSRule
    # WARN: .cssText is implemented in child classes.
    add_api(LoadPropertyTemplate(None, ha.CSSRuleArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.CSSRuleArg, "parentRule"))
    add_api(LoadPropertyTemplate(None, ha.CSSRuleArg, "parentStyleSheet"))

    # CSSStyleRuleList
    add_api(ArrayLoadIndexTemplate(hr.CSSStyleRuleRet, ha.CSSStyleRuleListArg))

    # CSSStyleRule
    add_api(LoadPropertyTemplate(None, ha.CSSStyleRuleArg, "cssText"))
    add_api(StorePropertyTemplate(ha.CSSStyleRuleValueArg, ha.CSSStyleRuleArg, "cssText"))
    add_api(LoadPropertyTemplate(None, ha.CSSStyleRuleArg, "selectorText"))
    add_api(StorePropertyTemplate(ha.CSSSelectorValueArg, ha.CSSStyleRuleArg, "selectorText"))
    add_api(LoadPropertyTemplate(hr.CSSStyleDeclarationRet, ha.CSSStyleRuleArg, "style"))

    # CSSStyleDeclaration
    add_api(LoadPropertyTemplate(None, ha.CSSStyleDeclarationArg, "length"))
    add_api(LoadPropertyTemplate(hr.CSSStyleRuleRet, ha.CSSStyleDeclarationArg, "parentRule"))
    add_api(LoadPropertyTemplate(None, ha.CSSStyleDeclarationArg, "cssFloat"))
    add_api(StorePropertyTemplate(ha.CSSFloatArg, ha.CSSStyleDeclarationArg, "cssFloat"))
    add_api(LoadPropertyTemplate(None, ha.CSSStyleDeclarationArg, "cssText"))
    add_api(StorePropertyTemplate(ha.CSSStyleDeclarationValueArg, ha.CSSStyleDeclarationArg, "cssText"))

    # CSSKeyframesRuleList
    add_api(ArrayLoadIndexTemplate(hr.CSSKeyframesRuleRet, ha.CSSKeyframesRuleListArg))

    # CSSKeyframesRule
    add_api(LoadPropertyTemplate(None, ha.CSSKeyframesRuleArg, "name"))
    add_api(LoadPropertyTemplate(hr.CSSKeyframeRuleListRet, ha.CSSKeyframesRuleArg, "cssRules"))

    # CSSKeyframeRuleList
    add_api(ArrayLoadIndexTemplate(hr.CSSKeyframeRuleRet, ha.CSSKeyframeRuleListArg))

    # CSSKeyframeRule
    add_api(LoadPropertyTemplate(None, ha.CSSKeyframeRuleArg, "keyText"))
    add_api(StorePropertyTemplate(ha.CSSKeyframeNameArg, ha.CSSKeyframeRuleArg, "keyText"))
    add_api(LoadPropertyTemplate(None, ha.CSSKeyframeRuleArg, "cssText"))
    add_api(StorePropertyTemplate(ha.CSSKeyframeRuleValueArg, ha.CSSKeyframeRuleArg, "cssText"))
    add_api(LoadPropertyTemplate(hr.CSSStyleDeclarationRet, ha.CSSKeyframeRuleArg, "style"))

    # MediaQueryList
    add_api(LoadPropertyTemplate(None, ha.MediaQueryListArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.MediaQueryListArg, "matches"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.MediaQueryListArg, "onchange"))

    # MediaList
    add_api(LoadPropertyTemplate(None, ha.MediaListArg, "mediaText"))
    add_api(StorePropertyTemplate(ha.MediaQueryArg, ha.MediaListArg, "mediaText"))
    add_api(LoadPropertyTemplate(None, ha.MediaListArg, "length"))

    # StyleMedia
    add_api(LoadPropertyTemplate(None, ha.StyleMediaArg, "type"))

    # FontFaceSet
    add_api(LoadPropertyTemplate(None, ha.FontFaceSetArg, "size"))
    # add_api(LoadPropertyTemplate(None, ha.FontFaceSetArg, "ready"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceSetArg, "status"))  # FontFaceSetLoadStatus
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.FontFaceSetArg, "onloading"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.FontFaceSetArg, "onloadingdone"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.FontFaceSetArg, "onloadingerror"))

    # FontFace
    # add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "loaded"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "status"))  # FontFaceLoadStatus
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "family"))
    add_api(StorePropertyTemplate(ha.FontArg, ha.FontFaceArg, "family"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "style"))
    add_api(StorePropertyTemplate(ha.CSSStyleDeclarationValueArg, ha.FontFaceArg, "style"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "weight"))
    add_api(StorePropertyTemplate(ha.FontWeightArg, ha.FontFaceArg, "weight"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "stretch"))
    add_api(StorePropertyTemplate(ha.FontStretchArg, ha.FontFaceArg, "stretch"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "unicodeRange"))
    add_api(StorePropertyTemplate(ha.UnicodeRangeArg, ha.FontFaceArg, "unicodeRange"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "variant"))
    add_api(StorePropertyTemplate(ha.FontVariantArg, ha.FontFaceArg, "variant"))
    add_api(LoadPropertyTemplate(None, ha.FontFaceArg, "featureSettings"))
    add_api(StorePropertyTemplate(ha.FontFeatureSettingsArg, ha.FontFaceArg, "featureSettings"))

    ######################################################
    # DOM
    # TODO: HTMLBaseElement, HTMLBodyElement, HTMLScriptElement
    ######################################################
    # DocumentOrShadowRoot
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentOrShadowRootArg, "pointerLockElement"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentOrShadowRootArg, "activeElement"))

    # Window
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "top"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "self"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.WindowArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "event"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "window"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "frames"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "opener"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "closed"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "length"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.WindowArg, "parent"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, ha.WindowArg, "document"))
    add_api(ArrayLoadIndexTemplate(None, ha.WindowArg))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "status"))
    add_api(StorePropertyTemplate(StringArg, ha.WindowArg, "status"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "defaultStatus"))
    add_api(StorePropertyTemplate(StringArg, ha.WindowArg, "defaultStatus"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "locationbar"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "menubar"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "personalbar"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "scrollbars"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "statusbar"))
    add_api(LoadPropertyTemplate(hr.BarPropRet, ha.WindowArg, "toolbar"))
    add_api(LoadPropertyTemplate(hr.ScreenRet, ha.WindowArg, "screen"))
    add_api(LoadPropertyTemplate(hr.VisualViewportRet, ha.WindowArg, "visualViewport"))
    add_api(LoadPropertyTemplate(hr.HistoryRet, ha.WindowArg, "history"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.WindowArg, "frameElement"))
    add_api(LoadPropertyTemplate(hr.NavigatorRet, ha.WindowArg, "navigator"))
    add_api(LoadPropertyTemplate(hr.ApplicationCacheRet, ha.WindowArg, "applicationCache"))
    add_api(LoadPropertyTemplate(hr.CustomElementRegistryRet, ha.WindowArg, "customElements"))
    add_api(LoadPropertyTemplate(hr.NavigatorRet, ha.WindowArg, "clientInformation"))
    add_api(LoadPropertyTemplate(hr.StyleMediaRet, ha.WindowArg, "styleMedia"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "innerWidth"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "innerHeight"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "scrollX"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "pageXOffset"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "scrollY"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "pageYOffset"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "screenX"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "screenY"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "outerWidth"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "outerHeight"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "devicePixelRatio"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "offscreenBuffering"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "screenLeft"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "screenTop"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "orientation"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "isSecureContext"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "webkitURL"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "WebKitTransitionEvent"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "WebKitAnimationEvent"))
    add_api(LoadPropertyTemplate(None, ha.WindowArg, "WebKitMutationObserver"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onanimationend"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onanimationiteration"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onanimationstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onorientationchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onsearch"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "ontransitionend"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onwebkitanimationend"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onwebkitanimationiteration"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onwebkitanimationstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onwebkittransitionend"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.WindowArg, "onwheel"))

    # NodeList
    add_api(LoadPropertyTemplate(None, ha.NodeListArg, "length"))

    # Attr
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "namespaceURI"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "prefix"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "localName"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "specified"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.AttrArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "nodeValue"))
    add_api(StorePropertyTemplate(StringArg, ha.AttrArg, "nodeValue"))
    add_api(LoadPropertyTemplate(None, ha.AttrArg, "textContent"))
    add_api(StorePropertyTemplate(StringArg, ha.AttrArg, "textContent"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.AttrArg, "ownerElement"))

    # NamedNodeMap
    add_api(LoadPropertyTemplate(None, ha.NamedNodeMapArg, "length"))
    add_api(DOMStringMapStoreIndexTemplate(ha.NamedNodeMapArg))

    # Document
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "domain"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "applets"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "scripts"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "referrer"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.DocumentArg, "defaultView"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "currentScript"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "documentElement"))
    # add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "body"))
    # add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "head"))
    add_api(LoadPropertyTemplate(hr.FontFaceSetRet, ha.DocumentArg, "fonts"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "designMode"))
    add_api(StorePropertyTemplate(ha.DesignModeArg, ha.DocumentArg, "designMode"))
    add_api(LoadPropertyTemplate(hr.HTMLAllCollectionRet, ha.DocumentArg, "all"))
    add_api(LoadPropertyTemplate(hr.DocumentTimelineRet, ha.DocumentArg, "timeline"))
    add_api(LoadPropertyTemplate(hr.FontFaceSetRet, ha.DocumentArg, "fonts"))
    # add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "rootScroller"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "scrollingElement"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "images"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "embeds"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "plugins"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "links"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "forms"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "anchors"))
    add_api(LoadPropertyTemplate(hr.DocumentTypeRet, ha.DocumentArg, "doctype"))
    add_api(LoadPropertyTemplate(hr.DOMImplementationRet, ha.DocumentArg, "implementation"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "title"))
    add_api(StorePropertyTemplate(StringArg, ha.DocumentArg, "title"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "dir"))
    add_api(StorePropertyTemplate(ha.DirArg, ha.DocumentArg, "dir"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "fgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.DocumentArg, "fgColor"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "linkColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.DocumentArg, "linkColor"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "vlinkColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.DocumentArg, "vlinkColor"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "alinkColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.DocumentArg, "alinkColor"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "bgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.DocumentArg, "bgColor"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "xmlEncoding"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "xmlVersion"))
    add_api(StorePropertyTemplate(StringArg, ha.DocumentArg, "xmlVersion"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "xmlStandalone"))
    add_api(StorePropertyTemplate(BooleanArg, ha.DocumentArg, "xmlStandalone"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "cookie"))
    add_api(StorePropertyTemplate(StringArg, ha.DocumentArg, "cookie"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "URL"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "documentURI"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "origin"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "suborigin"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "compatMode"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "characterSet"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "charset"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "inputEncoding"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "contentType"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "lastModified"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "readyState"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "hidden"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "webkitHidden"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "visibilityState"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "webkitVisibilityState"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "webkitIsFullScreen"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "fullscreenEnabled"))
    add_api(LoadPropertyTemplate(None, ha.DocumentArg, "webkitFullscreenEnabled"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "fullscreenElement"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "webkitCurrentFullScreenElement"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.DocumentArg, "webkitFullscreenElement"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onreadystatechange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onsearch"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onselectionchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onselectstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onfullscreenchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onfullscreenerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onwebkitfullscreenchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onwebkitfullscreenerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onpointerlockchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onpointerlockerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onsecuritypolicyviolation"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.DocumentArg, "onwheel"))

    # DocumentType
    add_api(LoadPropertyTemplate(None, ha.DocumentTypeArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.DocumentTypeArg, "publicId"))
    add_api(LoadPropertyTemplate(None, ha.DocumentTypeArg, "systemId"))

    # ShadowRoot
    add_api(LoadPropertyTemplate(None, ha.ShadowRootArg, "mode"))
    add_api(LoadPropertyTemplate(None, ha.ShadowRootArg, "delegatesFocus"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ShadowRootArg, "host"))
    add_api(LoadPropertyTemplate(hr.ShadowRootRet, ha.ShadowRootArg, "olderShadowRoot"))
    add_api(LoadPropertyTemplate(hr.HTMLStringRet, ha.ShadowRootArg, "innerHTML"))
    add_api(StorePropertyTemplate(ha.HTMLStringArg, ha.ShadowRootArg, "innerHTML"))

    # ProcessingInstruction
    add_api(LoadPropertyTemplate(None, ha.ProcessingInstructionArg, "target"))

    # Element
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "nodeType"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "nodeName"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "baseURI"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "isConnected"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, ha.ElementArg, "ownerDocument"))
    add_api(LoadPropertyTemplate(hr.NamedNodeMapRet, ha.ElementArg, "attributes"))
    add_api(LoadPropertyTemplate(hr.CSSStyleDeclarationRet, ha.ElementArg, "style"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "parentNode"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "parentElement"))
    add_api(LoadPropertyTemplate(hr.NodeListRet, ha.ElementArg, "childNodes"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "firstChild"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "lastChild"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "previousSibling"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "nextSibling"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "nodeValue"))
    add_api(StorePropertyTemplate(StringArg, ha.ElementArg, "nodeValue"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "textContent"))
    add_api(StorePropertyTemplate(StringArg, ha.ElementArg, "textContent"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.ElementArg, "children"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "firstElementChild"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "lastElementChild"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "childElementCount"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "namespaceURI"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "prefix"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "localName"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "tagName"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "id"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.ElementArg, "classList"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "className"))
    add_api(StorePropertyTemplate(ha.ClassArg, ha.ElementArg, "className"))
    add_api(LoadPropertyTemplate(hr.HTMLStringRet, ha.ElementArg, "innerHTML"))
    add_api(StorePropertyTemplate(StringArg, ha.ElementArg, "innerHTML"))
    add_api(StorePropertyTemplate(ha.HTMLStringArg, ha.ElementArg, "innerHTML"))
    add_api(LoadPropertyTemplate(hr.HTMLStringRet, ha.ElementArg, "outerHTML"))
    add_api(StorePropertyTemplate(StringArg, ha.ElementArg, "outerHTML"))
    add_api(StorePropertyTemplate(ha.HTMLStringArg, ha.ElementArg, "outerHTML"))
    add_api(LoadPropertyTemplate(hr.ShadowRootRet, ha.ElementArg, "shadowRoot"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "slot"))
    add_api(StorePropertyTemplate(ha.SlotArg, ha.ElementArg, "slot"))
    add_api(LoadPropertyTemplate(hr.HTMLSlotElementRet, ha.ElementArg, "assignedSlot"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "scrollTop"))
    add_api(StorePropertyTemplate(FloatArg, ha.ElementArg, "scrollTop"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "scrollLeft"))
    add_api(StorePropertyTemplate(FloatArg, ha.ElementArg, "scrollLeft"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "scrollWidth"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "scrollHeight"))      # https://bugs.chromium.org/p/project-zero/issues/detail?id=1525
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "clientTop"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "clientLeft"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "clientWidth"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "clientHeight"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "computedRole"))
    add_api(LoadPropertyTemplate(None, ha.ElementArg, "computedName"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "previousElementSibling"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.ElementArg, "nextElementSibling"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "onwheel"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "onsearch"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "onbeforeload"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "onselectstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "ongotpointercapture"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ElementArg, "onlostpointercapture"))

    # CharacterData
    add_api(LoadPropertyTemplate(None, ha.CharacterDataArg, "length"))
    add_api(LoadPropertyTemplate(None, ha.CharacterDataArg, "data"))
    add_api(StorePropertyTemplate(StringArg, ha.CharacterDataArg, "data"))

    # NodeIterator
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.NodeIteratorArg, "root"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.NodeIteratorArg, "referenceNode"))
    add_api(LoadPropertyTemplate(None, ha.NodeIteratorArg, "pointerBeforeReferenceNode"))
    add_api(LoadPropertyTemplate(None, ha.NodeIteratorArg, "whatToShow"))
    add_api(LoadPropertyTemplate(hr.NodeFilterRet, ha.NodeIteratorArg, "filter"))

    # TreeWalker
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.TreeWalkerArg, "root"))
    add_api(LoadPropertyTemplate(None, ha.TreeWalkerArg, "whatToShow"))
    add_api(LoadPropertyTemplate(hr.NodeFilterRet, ha.TreeWalkerArg, "filter"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.TreeWalkerArg, "currentNode"))
    add_api(StorePropertyTemplate(ha.ElementArg, ha.TreeWalkerArg, "currentNode"))

    # Text
    add_api(LoadPropertyTemplate(None, ha.TextArg, "wholeText"))
    add_api(LoadPropertyTemplate(hr.HTMLSlotElementRet, ha.TextArg, "assignedSlot"))

    # TimeRanges
    add_api(LoadPropertyTemplate(None, ha.TimeRangesArg, "length"))

    # Selection
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.SelectionArg, "anchorNode"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "anchorOffset"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.SelectionArg, "focusNode"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "focusOffset"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "isCollapsed"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "rangeCount"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "type"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.SelectionArg, "baseNode"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "baseOffset"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.SelectionArg, "extentNode"))
    add_api(LoadPropertyTemplate(None, ha.SelectionArg, "extentOffset"))

    # HTMLAllCollection
    add_api(LoadPropertyTemplate(None, ha.HTMLAllCollectionArg, "length"))

    # HTMLOptionsCollection
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionsCollectionArg, "length"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLOptionsCollectionArg, "length"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionsCollectionArg, "selectedIndex"))
    add_api(StorePropertyTemplate(IndexArg, ha.HTMLOptionsCollectionArg, "selectedIndex"))
    add_api(ArrayLoadIndexTemplate(hr.HTMLOptionElementRet, ha.HTMLOptionsCollectionArg))
    add_api(ArrayStoreIndexTemplate(ha.HTMLOptionElementArg, ha.HTMLOptionsCollectionArg))

    # HTMLElement
    add_api(LoadPropertyTemplate(hr.CSSStyleDeclarationRet, ha.HTMLElementArg, "style"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "accessKey"))
    add_api(StorePropertyTemplate(CharArg, ha.HTMLElementArg, "accessKey"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "autocapitalize"))
    add_api(StorePropertyTemplate(ha.AutoCapitalizeArg, ha.HTMLElementArg, "autocapitalize"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "autocorrect"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLElementArg, "autocorrect"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "contentEditable"))
    add_api(StorePropertyTemplate(ha.ContentEditableArg, ha.HTMLElementArg, "contentEditable"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "dir"))
    add_api(StorePropertyTemplate(ha.DirArg, ha.ElementArg, "dir"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "draggable"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLElementArg, "draggable"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "hidden"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLElementArg, "hidden"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "innerText"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLElementArg, "innerText"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "isContentEditable"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "lang"))
    add_api(StorePropertyTemplate(ha.LangArg, ha.HTMLElementArg, "lang"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "outerText"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLElementArg, "outerText"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "spellcheck"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLElementArg, "spellcheck"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "tabIndex"))
    add_api(StorePropertyTemplate(ha.TabIndexArg, ha.HTMLElementArg, "tabIndex"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "title"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLElementArg, "title"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "translate"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLElementArg, "translate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "webkitdropzone"))
    add_api(StorePropertyTemplate(ha.DropZoneArg, ha.HTMLElementArg, "webkitdropzone"))
    add_api(LoadPropertyTemplate(hr.HTMLMenuElementRet, ha.HTMLElementArg, "contextMenu"))
    add_api(StorePropertyTemplate(ha.HTMLMenuElementArg, ha.HTMLElementArg, "contextMenu"))
    add_api(LoadPropertyTemplate(hr.HTMLElementRet, ha.HTMLElementArg, "offsetParent"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "offsetTop"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "offsetLeft"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "offsetWidth"))
    add_api(LoadPropertyTemplate(None, ha.HTMLElementArg, "offsetHeight"))
    add_api(LoadPropertyTemplate(hr.DOMStringMapRet, ha.HTMLElementArg, "dataset"))

    # HTMLAnchorElement
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MIMETypeArg, ha.HTMLAnchorElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "download"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "referrerPolicy"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "charset"))
    add_api(StorePropertyTemplate(ha.CharsetArg, ha.HTMLAnchorElementArg, "charset"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "coords"))
    add_api(StorePropertyTemplate(ha.CoordsArg, ha.HTMLAnchorElementArg, "coords"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "shape"))
    add_api(StorePropertyTemplate(ha.ShapeArg, ha.HTMLAnchorElementArg, "shape"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "target"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLAnchorElementArg, "target"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "text"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLAnchorElementArg, "text"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "ping"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLAnchorElementArg, "ping"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "rel"))
    add_api(StorePropertyTemplate(ha.RelArg, ha.HTMLAnchorElementArg, "rel"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "href"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLAnchorElementArg, "href"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "hreflang"))
    add_api(StorePropertyTemplate(ha.LangArg, ha.HTMLAnchorElementArg, "hreflang"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAnchorElementArg, "rev"))
    add_api(StorePropertyTemplate(ha.RevArg, ha.HTMLAnchorElementArg, "rev"))

    # HTMLAreaElement
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "alt"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLAreaElementArg, "alt"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "coords"))
    add_api(StorePropertyTemplate(ha.CoordsArg, ha.HTMLAreaElementArg, "coords"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "noHref"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLAreaElementArg, "noHref"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "shape"))
    add_api(StorePropertyTemplate(ha.ShapeArg, ha.HTMLAreaElementArg, "shape"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "target"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLAreaElementArg, "target"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "href"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLAreaElementArg, "href"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "ping"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLAreaElementArg, "ping"))

    # HTMLMediaElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitKeys"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "crossOrigin"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "autoplay"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "autoplay"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "controls"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "controls"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "currentTime"))
    add_api(StorePropertyTemplate(ClockArg, ha.HTMLMediaElementArg, "currentTime"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "defaultPlaybackRate"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMediaElementArg, "defaultPlaybackRate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "loop"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "loop"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "muted"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "muted"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "playbackRate"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMediaElementArg, "playbackRate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "preload"))
    add_api(StorePropertyTemplate(ha.PreloadArg, ha.HTMLMediaElementArg, "preload"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "src"))
    add_api(StorePropertyTemplate(ha.MediaSrcArg, ha.HTMLMediaElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "volume"))
    add_api(StorePropertyTemplate(ha.VolumeArg, ha.HTMLMediaElementArg, "volume"))
    add_api(LoadPropertyTemplate(hr.TimeRangesRet, ha.HTMLMediaElementArg, "buffered"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "currentSrc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "duration"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "ended"))
    add_api(LoadPropertyTemplate(hr.MediaErrorRet, ha.HTMLMediaElementArg, "error"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "networkState"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "paused"))
    add_api(LoadPropertyTemplate(hr.TimeRangesRet, ha.HTMLMediaElementArg, "played"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "readyState"))
    add_api(LoadPropertyTemplate(hr.TimeRangesRet, ha.HTMLMediaElementArg, "seekable"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "seeking"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "startTime"))
    add_api(LoadPropertyTemplate(hr.AudioTrackListRet, ha.HTMLMediaElementArg, "audioTracks"))
    add_api(LoadPropertyTemplate(hr.MediaControllerRet, ha.HTMLMediaElementArg, "controller"))
    add_api(StorePropertyTemplate(ha.MediaControllerArg, ha.HTMLMediaElementArg, "controller"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "defaultMuted"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "defaultMuted"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "kind"))
    add_api(StorePropertyTemplate(ha.TrackKindArg, ha.HTMLMediaElementArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "mediaGroup"))
    add_api(StorePropertyTemplate(ha.MediaGroupArg, ha.HTMLMediaElementArg, "mediaGroup"))
    add_api(LoadPropertyTemplate(hr.MediaSessionRet, ha.HTMLMediaElementArg, "session"))
    add_api(StorePropertyTemplate(ha.MediaSessionArg, ha.HTMLMediaElementArg, "session"))
    add_api(LoadPropertyTemplate(hr.MediaStreamRet, ha.HTMLMediaElementArg, "srcObject"))
    add_api(StorePropertyTemplate(ha.MediaStreamArg, ha.HTMLMediaElementArg, "srcObject"))
    add_api(LoadPropertyTemplate(hr.TextTrackListRet, ha.HTMLMediaElementArg, "textTracks"))
    add_api(LoadPropertyTemplate(hr.VideoTrackListRet, ha.HTMLMediaElementArg, "videoTracks"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitClosedCaptionsVisible"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "webkitClosedCaptionsVisible"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitCurrentPlaybackTargetIsWireless"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitHasClosedCaptions"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitPreservesPitch"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMediaElementArg, "webkitPreservesPitch"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitAudioDecodedByteCount"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMediaElementArg, "webkitVideoDecodedByteCount"))

    # HTMLBRElement
    add_api(LoadPropertyTemplate(None, ha.HTMLBRElementArg, "clear"))
    add_api(StorePropertyTemplate(ha.ClearArg, ha.HTMLBRElementArg, "clear"))

    # HTMLButtonElement
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "formAction"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "autofocus"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLButtonElementArg, "autofocus"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLButtonElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLButtonElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "formEnctype"))
    add_api(StorePropertyTemplate(ha.FormEncTypeArg, ha.HTMLButtonElementArg, "formEnctype"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "formMethod"))
    add_api(StorePropertyTemplate(ha.FormMethodArg, ha.HTMLButtonElementArg, "formMethod"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "formNoValidate"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLButtonElementArg, "formNoValidate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "formTarget"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLButtonElementArg, "formTarget"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLButtonElementArg, "labels"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLButtonElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "type"))
    add_api(StorePropertyTemplate(ha.ButtonTypeArg, ha.HTMLButtonElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLButtonElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLButtonElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLButtonElementArg, "willValidate"))

    # HTMLDListElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDListElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDListElementArg, "compact"))

    # HTMLDataElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDataElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLDataElementArg, "value"))

    # HTMLDetailsElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDetailsElementArg, "open"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDetailsElementArg, "open"))

    # HTMLDirectoryElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDirectoryElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDirectoryElementArg, "compact"))

    # HTMLDivElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDivElementArg, "align"))
    add_api(StorePropertyTemplate(ha.AlignArg, ha.HTMLDivElementArg, "align"))

    # HTMLIFrameElement
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "name"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.HTMLIFrameElementArg, "sandbox"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, ha.HTMLIFrameElementArg, "contentDocument"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.HTMLIFrameElementArg, "contentWindow"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "getSVGDocument"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "referrerPolicy"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.HTMLIFrameElementArg, "permissions"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "csp"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "src"))
    add_api(StorePropertyTemplate(ha.FrameSrcArg, ha.HTMLIFrameElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "srcdoc"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLIFrameElementArg, "srcdoc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "allowFullscreen"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLIFrameElementArg, "allowFullscreen"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLIFrameElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLIFrameElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "align"))
    add_api(StorePropertyTemplate(ha.ObjectAlignArg, ha.HTMLIFrameElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "scrolling"))
    add_api(StorePropertyTemplate(ha.ScrollingArg, ha.HTMLIFrameElementArg, "scrolling"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "frameBorder"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLIFrameElementArg, "frameBorder"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "longDesc"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLIFrameElementArg, "longDesc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "marginHeight"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLIFrameElementArg, "marginHeight"))
    add_api(LoadPropertyTemplate(None, ha.HTMLIFrameElementArg, "marginWidth"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLIFrameElementArg, "marginWidth"))

    # HTMLTableElement
    add_api(LoadPropertyTemplate(hr.HTMLTableCaptionElementRet, ha.HTMLTableElementArg, "caption"))
    add_api(StorePropertyTemplate(ha.HTMLTableCaptionElementArg, ha.HTMLTableElementArg, "caption"))
    add_api(LoadPropertyTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableElementArg, "tHead"))
    add_api(StorePropertyTemplate(ha.HTMLTableSectionElementArg, ha.HTMLTableElementArg, "tHead"))
    add_api(LoadPropertyTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableElementArg, "tFoot"))
    add_api(StorePropertyTemplate(ha.HTMLTableSectionElementArg, ha.HTMLTableElementArg, "tFoot"))
    add_api(LoadPropertyTemplate(hr.HTMLTableSectionsCollectionRet, ha.HTMLTableElementArg, "tBodies"))
    add_api(LoadPropertyTemplate(hr.HTMLTableRowsCollectionRet, ha.HTMLTableElementArg, "rows"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "align"))
    add_api(StorePropertyTemplate(ha.AlignArg, ha.HTMLTableElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "border"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableElementArg, "border"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "frame"))
    add_api(StorePropertyTemplate(ha.TableFrameArg, ha.HTMLTableElementArg, "frame"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "rules"))
    add_api(StorePropertyTemplate(ha.TableRulesArg, ha.HTMLTableElementArg, "rules"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "summary"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTableElementArg, "summary"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "bgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLTableElementArg, "bgColor"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "cellPadding"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableElementArg, "cellPadding"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableElementArg, "cellSpacing"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableElementArg, "cellSpacing"))

    # HTMLFrameElement
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "name"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.HTMLFrameElementArg, "contentWindow"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, ha.HTMLFrameElementArg, "contentDocument"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "longDesc"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLFrameElementArg, "longDesc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "scrolling"))
    add_api(StorePropertyTemplate(ha.ScrollingArg, ha.HTMLFrameElementArg, "scrolling"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "src"))
    add_api(StorePropertyTemplate(ha.FrameSrcArg, ha.HTMLFrameElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "frameBorder"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFrameElementArg, "frameBorder"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "noResize"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLFrameElementArg, "noResize"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "marginHeight"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFrameElementArg, "marginHeight"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameElementArg, "marginWidth"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFrameElementArg, "marginWidth"))

    # HTMLTableColElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "span"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableColElementArg, "span"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "align"))
    add_api(StorePropertyTemplate(ha.TableAlignArg, ha.HTMLTableColElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "ch"))
    add_api(StorePropertyTemplate(CharArg, ha.HTMLTableColElementArg, "ch"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "chOff"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableColElementArg, "chOff"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "vAlign"))
    add_api(StorePropertyTemplate(ha.VAlignArg, ha.HTMLTableColElementArg, "vAlign"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableColElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableColElementArg, "width"))

    # HTMLDialogElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDialogElementArg, "open"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDialogElementArg, "open"))
    add_api(LoadPropertyTemplate(None, ha.HTMLDialogElementArg, "returnValue"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLDialogElementArg, "returnValue"))

    # HTMLTextAreaElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "dirName"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "autofocus"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTextAreaElementArg, "autofocus"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "cols"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "cols"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTextAreaElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLTextAreaElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "inputMode"))
    add_api(StorePropertyTemplate(ha.InputModeArg, ha.HTMLTextAreaElementArg, "inputMode"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "maxLength"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "maxLength"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "minLength"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "minLength"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "placeholder"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTextAreaElementArg, "placeholder"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "readOnly"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTextAreaElementArg, "readOnly"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "required"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTextAreaElementArg, "required"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "rows"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "rows"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "wrap"))
    add_api(StorePropertyTemplate(ha.WrapArg, ha.HTMLTextAreaElementArg, "wrap"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "defaultValue"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTextAreaElementArg, "defaultValue"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTextAreaElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "textLength"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLTextAreaElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLTextAreaElementArg, "labels"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "selectionStart"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "selectionStart"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "selectionEnd"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTextAreaElementArg, "selectionEnd"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "selectionDirection"))
    add_api(StorePropertyTemplate(ha.SelectionDirectionArg, ha.HTMLTextAreaElementArg, "selectionDirection"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTextAreaElementArg, "autocapitalize"))
    add_api(StorePropertyTemplate(ha.AutoCapitalizeArg, ha.HTMLTextAreaElementArg, "autocapitalize"))

    # HTMLOListElement
    add_api(LoadPropertyTemplate(None, ha.HTMLOListElementArg, "reversed"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOListElementArg, "reversed"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOListElementArg, "start"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLOListElementArg, "start"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOListElementArg, "type"))
    add_api(StorePropertyTemplate(ha.NumberingTypeArg, ha.HTMLOListElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOListElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOListElementArg, "compact"))

    # HTMLProgressElement
    add_api(LoadPropertyTemplate(None, ha.HTMLProgressElementArg, "value"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLProgressElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLProgressElementArg, "max"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLProgressElementArg, "max"))
    add_api(LoadPropertyTemplate(None, ha.HTMLProgressElementArg, "position"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLProgressElementArg, "labels"))

    # HTMLQuoteElement
    add_api(LoadPropertyTemplate(None, ha.HTMLQuoteElementArg, "cite"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLQuoteElementArg, "cite"))

    # HTMLFormElement
    # TODO: action
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "encoding"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "acceptCharset"))
    add_api(StorePropertyTemplate(ha.CharsetArg, ha.HTMLFormElementArg, "acceptCharset"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "autocomplete"))
    add_api(StorePropertyTemplate(ha.AutoCompleteArg, ha.HTMLFormElementArg, "autocomplete"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "enctype"))
    add_api(StorePropertyTemplate(ha.FormEncTypeArg, ha.HTMLFormElementArg, "enctype"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "method"))
    add_api(StorePropertyTemplate(ha.FormMethodArg, ha.HTMLFormElementArg, "method"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "noValidate"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLFormElementArg, "noValidate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "target"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLFormElementArg, "target"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.HTMLFormElementArg, "elements"))  # HTMLFormControlsCollection
    add_api(ArrayLoadIndexTemplate(hr.ElementRet, ha.HTMLFormElementArg))
    add_api(LoadPropertyTemplate(None, ha.HTMLFormElementArg, "length"))
    add_api(ArrayLoadIndexTemplate(hr.HTMLElementRet, ha.HTMLFormElementArg))

    # HTMLHeadingElement
    add_api(LoadPropertyTemplate(None, ha.HTMLHeadingElementArg, "align"))
    add_api(StorePropertyTemplate(ha.AlignArg, ha.HTMLHeadingElementArg, "align"))

    # HTMLLegendElement
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLLegendElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLegendElementArg, "align"))
    add_api(StorePropertyTemplate(ha.CaptionAlignArg, ha.HTMLLegendElementArg, "align"))

    # HTMLSlotElement
    add_api(LoadPropertyTemplate(None, ha.HTMLSlotElementArg, "name"))

    # HTMLPreElement
    add_api(LoadPropertyTemplate(None, ha.HTMLPreElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLPreElementArg, "width"))

    # HTMLKeygenElement
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "autofocus"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLKeygenElementArg, "autofocus"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "challenge"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLKeygenElementArg, "challenge"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLKeygenElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLKeygenElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "keytype"))
    add_api(StorePropertyTemplate(ha.KeyTypeArg, ha.HTMLKeygenElementArg, "keytype"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLKeygenElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLKeygenElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLKeygenElementArg, "labels"))

    # HTMLSourceElement
    add_api(LoadPropertyTemplate(None, ha.HTMLSourceElementArg, "sizes"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSourceElementArg, "media"))
    add_api(StorePropertyTemplate(ha.MediaQueryArg, ha.HTMLSourceElementArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSourceElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MediaTypeArg, ha.HTMLSourceElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSourceElementArg, "src"))
    add_api(StorePropertyTemplate(ha.MediaSrcArg, ha.HTMLSourceElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSourceElementArg, "srcset"))
    add_api(StorePropertyTemplate(ha.SrcSetArg, ha.HTMLSourceElementArg, "srcset"))

    # HTMLMetaElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMetaElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMetaElementArg, "httpEquiv"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMetaElementArg, "content"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLMetaElementArg, "content"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMetaElementArg, "scheme"))
    add_api(StorePropertyTemplate(ha.MetaSchemeArg, ha.HTMLMetaElementArg, "scheme"))

    # HTMLTableRowElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "rowIndex"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "sectionRowIndex"))
    add_api(LoadPropertyTemplate(hr.HTMLTableCellsCollectionRet, ha.HTMLTableRowElementArg, "cells"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "align"))
    add_api(StorePropertyTemplate(ha.TableAlignArg, ha.HTMLTableRowElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "ch"))
    add_api(StorePropertyTemplate(CharArg, ha.HTMLTableRowElementArg, "ch"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "chOff"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableRowElementArg, "chOff"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "vAlign"))
    add_api(StorePropertyTemplate(ha.VAlignArg, ha.HTMLTableRowElementArg, "vAlign"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableRowElementArg, "bgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLTableRowElementArg, "bgColor"))

    # HTMLTableCaptionElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCaptionElementArg, "align"))
    add_api(StorePropertyTemplate(ha.CaptionAlignArg, ha.HTMLTableCaptionElementArg, "align"))

    # HTMLFrameSetElement
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameSetElementArg, "cols"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFrameSetElementArg, "cols"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFrameSetElementArg, "rows"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFrameSetElementArg, "rows"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onblur"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onfocus"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onload"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onresize"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onscroll"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLFrameSetElementArg, "onorientationchange"))

    # HTMLModElement
    add_api(LoadPropertyTemplate(None, ha.HTMLModElementArg, "cite"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLModElementArg, "cite"))
    add_api(LoadPropertyTemplate(None, ha.HTMLModElementArg, "dateTime"))
    add_api(StorePropertyTemplate(ha.DateTimeArg, ha.HTMLModElementArg, "dateTime"))

    # HTMLParagraphElement
    add_api(LoadPropertyTemplate(None, ha.HTMLParagraphElementArg, "align"))
    add_api(StorePropertyTemplate(ha.AlignArg, ha.HTMLParagraphElementArg, "align"))

    # HTMLObjectElement
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "code"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "codeBase"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "codeType"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.HTMLObjectElementArg, "contentWindow"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, ha.HTMLObjectElementArg, "contentDocument"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MediaTypeArg, ha.HTMLObjectElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "data"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLObjectElementArg, "data"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "useMap"))
    add_api(StorePropertyTemplate(ha.UseMapArg, ha.HTMLObjectElementArg, "useMap"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLObjectElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLObjectElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "height"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLObjectElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLObjectElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "align"))
    add_api(StorePropertyTemplate(ha.ObjectAlignArg, ha.HTMLObjectElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "archive"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLObjectElementArg, "archive"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "declare"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLObjectElementArg, "declare"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "hspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLObjectElementArg, "hspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "standby"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLObjectElementArg, "standby"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "vspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLObjectElementArg, "vspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLObjectElementArg, "border"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLObjectElementArg, "border"))

    # HTMLSelectElement
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "autofocus"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLSelectElementArg, "autofocus"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLSelectElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLSelectElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "multiple"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLSelectElementArg, "multiple"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "required"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLSelectElementArg, "required"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "size"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLSelectElementArg, "size"))
    add_api(LoadPropertyTemplate(hr.HTMLOptionsCollectionRet, ha.HTMLSelectElementArg, "options"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "length"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLSelectElementArg, "length"))
    add_api(LoadPropertyTemplate(hr.HTMLOptionsCollectionRet, ha.HTMLSelectElementArg, "selectedOptions"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "selectedIndex"))
    add_api(StorePropertyTemplate(IndexArg, ha.HTMLSelectElementArg, "selectedIndex"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLSelectElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLSelectElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLSelectElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLSelectElementArg, "labels"))
    add_api(ArrayLoadIndexTemplate(hr.HTMLOptionElementRet, ha.HTMLSelectElementArg))

    # HTMLDirectoryElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDirectoryElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDirectoryElementArg, "compact"))

    # HTMLParamElement
    add_api(LoadPropertyTemplate(None, ha.HTMLParamElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLParamElementArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLParamElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLParamElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLParamElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLParamElementArg, "valueType"))
    add_api(StorePropertyTemplate(ha.ParamValueTypeArg, ha.HTMLParamElementArg, "valueType"))

    # HTMLDataListElement
    add_api(LoadPropertyTemplate(hr.HTMLOptionsCollectionRet, ha.HTMLDataListElementArg, "options"))

    # HTMLHRElement
    add_api(LoadPropertyTemplate(None, ha.HTMLHRElementArg, "align"))
    add_api(StorePropertyTemplate(ha.AlignArg, ha.HTMLHRElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLHRElementArg, "color"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLHRElementArg, "color"))
    add_api(LoadPropertyTemplate(None, ha.HTMLHRElementArg, "noShade"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLHRElementArg, "noShade"))
    add_api(LoadPropertyTemplate(None, ha.HTMLHRElementArg, "size"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLHRElementArg, "size"))
    add_api(LoadPropertyTemplate(None, ha.HTMLHRElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLHRElementArg, "width"))

    # HTMLLinkElement
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "target"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "integrity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "crossOrigin"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.HTMLLinkElementArg, "sizes"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.HTMLLinkElementArg, "relList"))
    add_api(StorePropertyTemplate(ha.MIMETypeArg, ha.HTMLLinkElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLLinkElementArg, "disabled"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "href"))
    add_api(StorePropertyTemplate(ha.DummyUrlArg, ha.HTMLLinkElementArg, "href"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "rel"))
    add_api(StorePropertyTemplate(ha.RelArg, ha.HTMLLinkElementArg, "rel"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "rev"))
    add_api(StorePropertyTemplate(ha.RevArg, ha.HTMLLinkElementArg, "rev"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "media"))
    add_api(StorePropertyTemplate(ha.MediaQueryArg, ha.HTMLLinkElementArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "hreflang"))
    add_api(StorePropertyTemplate(ha.LangArg, ha.HTMLLinkElementArg, "hreflang"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "as"))
    add_api(StorePropertyTemplate(ha.LinkAsArg, ha.HTMLLinkElementArg, "as"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLinkElementArg, "charset"))
    add_api(StorePropertyTemplate(ha.CharsetArg, ha.HTMLLinkElementArg, "charset"))

    # HTMLScriptElement
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "nonce"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "charset"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "integrity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "crossOrigin"))
    add_api(StorePropertyTemplate(ha.CharsetArg, ha.HTMLScriptElementArg, "charset"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "async"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLScriptElementArg, "async"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "defer"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLScriptElementArg, "defer"))
    add_api(LoadPropertyTemplate(None, ha.HTMLScriptElementArg, "text"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLScriptElementArg, "text"))

    # HTMLStyleElement
    add_api(LoadPropertyTemplate(None, ha.HTMLStyleElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLStyleElementArg, "disabled"))
    add_api(LoadPropertyTemplate(None, ha.HTMLStyleElementArg, "media"))
    add_api(StorePropertyTemplate(ha.MediaQueryArg, ha.HTMLStyleElementArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.HTMLStyleElementArg, "type"))
    add_api(StorePropertyTemplate(ha.CSSTypeArg, ha.HTMLStyleElementArg, "type"))
    add_api(LoadPropertyTemplate(hr.CSSStyleSheetRet, ha.HTMLStyleElementArg, "sheet"))

    # HTMLCanvasElement
    add_api(LoadPropertyTemplate(None, ha.HTMLCanvasElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLCanvasElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLCanvasElementArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLCanvasElementArg, "height"))

    # HTMLDListElement
    add_api(LoadPropertyTemplate(None, ha.HTMLDListElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLDListElementArg, "compact"))

    # HTMLOutputElement
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "name"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, ha.HTMLOutputElementArg, "htmlFor"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLOutputElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOutputElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "defaultValue"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOutputElementArg, "defaultValue"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLOutputElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOutputElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLOutputElementArg, "labels"))

    # HTMLTrackElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "kind"))
    add_api(StorePropertyTemplate(ha.TrackKindArg, ha.HTMLTrackElementArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "src"))
    add_api(StorePropertyTemplate(ha.TrackSrcArg, ha.HTMLTrackElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "srclang"))
    add_api(StorePropertyTemplate(ha.LangArg, ha.HTMLTrackElementArg, "srclang"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "label"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTrackElementArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "default"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTrackElementArg, "default"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTrackElementArg, "readyState"))
    add_api(LoadPropertyTemplate(hr.TextTrackRet, ha.HTMLTrackElementArg, "track"))

    # HTMLUListElement
    add_api(LoadPropertyTemplate(None, ha.HTMLUListElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLUListElementArg, "compact"))
    add_api(LoadPropertyTemplate(None, ha.HTMLUListElementArg, "type"))
    add_api(StorePropertyTemplate(ha.UListTypeArg, ha.HTMLUListElementArg, "type"))

    # HTMLAreaElement
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "ping"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "download"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "referrerPolicy"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "alt"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLAreaElementArg, "alt"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "coords"))
    add_api(StorePropertyTemplate(ha.CoordsArg, ha.HTMLAreaElementArg, "coords"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "shape"))
    add_api(StorePropertyTemplate(ha.ShapeArg, ha.HTMLAreaElementArg, "shape"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "target"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLAreaElementArg, "target"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "rel"))
    add_api(StorePropertyTemplate(ha.RelArg, ha.HTMLAreaElementArg, "rel"))
    add_api(LoadPropertyTemplate(None, ha.HTMLAreaElementArg, "noHref"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLAreaElementArg, "noHref"))

    # HTMLLabelElement
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLLabelElementArg, "form"))
    add_api(LoadPropertyTemplate(hr.HTMLElementRet, ha.HTMLLabelElementArg, "control"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLabelElementArg, "htmlFor"))
    add_api(StorePropertyTemplate(ha.LabelForArg, ha.HTMLLabelElementArg, "htmlFor"))

    # HTMLMapElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMapElementArg, "name"))
    add_api(LoadPropertyTemplate(hr.HTMLAreasCollectionRet, ha.HTMLMapElementArg, "areas"))

    # HTMLVideoElement
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLVideoElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLVideoElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "videoWidth"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "videoHeight"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "poster"))
    add_api(StorePropertyTemplate(ha.ImageSrcArg, ha.HTMLVideoElementArg, "poster"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "webkitSupportsFullscreen"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "webkitDisplayingFullscreen"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "webkitDecodedFrameCount"))
    add_api(LoadPropertyTemplate(None, ha.HTMLVideoElementArg, "webkitDroppedFrameCount"))

    # HTMLTableSectionElement
    add_api(LoadPropertyTemplate(hr.HTMLTableRowsCollectionRet, ha.HTMLTableSectionElementArg, "rows"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableSectionElementArg, "align"))
    add_api(StorePropertyTemplate(ha.TableAlignArg, ha.HTMLTableSectionElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableSectionElementArg, "ch"))
    add_api(StorePropertyTemplate(CharArg, ha.HTMLTableSectionElementArg, "ch"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableSectionElementArg, "chOff"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableSectionElementArg, "chOff"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableSectionElementArg, "vAlign"))
    add_api(StorePropertyTemplate(ha.VAlignArg, ha.HTMLTableSectionElementArg, "vAlign"))

    # HTMLFieldSetElement
    add_api(LoadPropertyTemplate(None, ha.HTMLFieldSetElementArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLFieldSetElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFieldSetElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLFieldSetElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLFieldSetElementArg, "form"))
    add_api(LoadPropertyTemplate(hr.HTMLCollectionRet, ha.HTMLFieldSetElementArg, "elements"))  # HTMLFormControlsCollection
    add_api(LoadPropertyTemplate(None, ha.HTMLFieldSetElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLFieldSetElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFieldSetElementArg, "validationMessage"))

    # HTMLTableCellElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "colSpan"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableCellElementArg, "colSpan"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "rowSpan"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableCellElementArg, "rowSpan"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "headers"))
    add_api(StorePropertyTemplate(ha.TableHeadersArg, ha.HTMLTableCellElementArg, "headers"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "cellIndex"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "align"))
    add_api(StorePropertyTemplate(ha.TableAlignArg, ha.HTMLTableCellElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "axis"))
    add_api(StorePropertyTemplate(ha.TableAxisArg, ha.HTMLTableCellElementArg, "axis"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "height"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableCellElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLTableCellElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "ch"))
    add_api(StorePropertyTemplate(CharArg, ha.HTMLTableCellElementArg, "ch"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "chOff"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLTableCellElementArg, "chOff"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "noWrap"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLTableCellElementArg, "noWrap"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "vAlign"))
    add_api(StorePropertyTemplate(ha.VAlignArg, ha.HTMLTableCellElementArg, "vAlign"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "bgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLTableCellElementArg, "bgColor"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "abbr"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTableCellElementArg, "abbr"))
    add_api(LoadPropertyTemplate(None, ha.HTMLTableCellElementArg, "scope"))
    add_api(StorePropertyTemplate(ha.TableScopeArg, ha.HTMLTableCellElementArg, "scope"))

    # HTMLFontElement
    add_api(LoadPropertyTemplate(None, ha.HTMLFontElementArg, "color"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLFontElementArg, "color"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFontElementArg, "face"))
    add_api(StorePropertyTemplate(ha.FontArg, ha.HTMLFontElementArg, "face"))
    add_api(LoadPropertyTemplate(None, ha.HTMLFontElementArg, "size"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLFontElementArg, "size"))

    # HTMLOptionElement
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOptionElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLOptionElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "label"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOptionElementArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "defaultSelected"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOptionElementArg, "defaultSelected"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "selected"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOptionElementArg, "selected"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOptionElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "text"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOptionElementArg, "text"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptionElementArg, "index"))

    # HTMLMenuElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MenuTypeArg, ha.HTMLMenuElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuElementArg, "label"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLMenuElementArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuElementArg, "compact"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMenuElementArg, "compact"))

    # HTMLMeterElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "value"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "min"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "min"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "max"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "max"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "low"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "low"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "high"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "high"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMeterElementArg, "optimum"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLMeterElementArg, "optimum"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLMeterElementArg, "labels"))

    # HTMLEmbedElement
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MediaTypeArg, ha.HTMLEmbedElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLEmbedElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "src"))
    add_api(StorePropertyTemplate(ha.MediaSrcArg, ha.HTMLEmbedElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "height"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLEmbedElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLEmbedElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLEmbedElementArg, "align"))
    add_api(StorePropertyTemplate(ha.ObjectAlignArg, ha.HTMLEmbedElementArg, "align"))

    # HTMLTitleElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTitleElementArg, "text"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLTitleElementArg, "text"))

    # HTMLInputElement
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "dirName"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "formAction"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "name"))
    add_api(StorePropertyTemplate(ha.AcceptArg, ha.HTMLInputElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "accept"))
    add_api(StorePropertyTemplate(ha.AcceptArg, ha.HTMLInputElementArg, "accept"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "alt"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLInputElementArg, "alt"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "autocomplete"))
    add_api(StorePropertyTemplate(ha.AutoCompleteArg, ha.HTMLInputElementArg, "autocomplete"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "autofocus"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "autofocus"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "defaultChecked"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "defaultChecked"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "checked"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "checked"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "disabled"))
    add_api(LoadPropertyTemplate(hr.HTMLFormElementRet, ha.HTMLInputElementArg, "form"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "formEnctype"))
    add_api(StorePropertyTemplate(ha.FormEncTypeArg, ha.HTMLInputElementArg, "formEnctype"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "formMethod"))
    add_api(StorePropertyTemplate(ha.FormMethodArg, ha.HTMLInputElementArg, "formMethod"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "formNoValidate"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "formNoValidate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "formTarget"))
    add_api(StorePropertyTemplate(ha.TargetArg, ha.HTMLInputElementArg, "formTarget"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "indeterminate"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "indeterminate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "inputMode"))
    add_api(StorePropertyTemplate(ha.InputModeArg, ha.HTMLInputElementArg, "inputMode"))
    add_api(LoadPropertyTemplate(hr.HTMLElementRet, ha.HTMLInputElementArg, "list"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "max"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "max"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "maxLength"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "maxLength"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "min"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "min"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "minLength"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "minLength"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "multiple"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "multiple"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "pattern"))
    add_api(StorePropertyTemplate(RegexArg, ha.HTMLInputElementArg, "pattern"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "placeholder"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLInputElementArg, "placeholder"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "readOnly"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "readOnly"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "required"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "required"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "size"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "size"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "src"))
    add_api(StorePropertyTemplate(ha.ImageSrcArg, ha.HTMLInputElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "step"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "step"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "type"))
    add_api(StorePropertyTemplate(ha.InputTypeArg, ha.HTMLInputElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "defaultValue"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLInputElementArg, "defaultValue"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "value"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLInputElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "valueAsDate"))
    add_api(StorePropertyTemplate(ha.DateTimeArg, ha.HTMLInputElementArg, "valueAsDate"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "valueAsNumber"))
    add_api(StorePropertyTemplate(FloatArg, ha.HTMLInputElementArg, "valueAsNumber"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "willValidate"))
    add_api(LoadPropertyTemplate(hr.ValidityStateRet, ha.HTMLInputElementArg, "validity"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "validationMessage"))
    add_api(LoadPropertyTemplate(hr.HTMLLabelElementListRet, ha.HTMLInputElementArg, "labels"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "selectionStart"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "selectionStart"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "selectionEnd"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLInputElementArg, "selectionEnd"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "selectionDirection"))
    add_api(StorePropertyTemplate(ha.SelectionDirectionArg, ha.HTMLInputElementArg, "selectionDirection"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "align"))
    add_api(StorePropertyTemplate(ha.ObjectAlignArg, ha.HTMLInputElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "useMap"))
    add_api(StorePropertyTemplate(ha.UseMapArg, ha.HTMLInputElementArg, "useMap"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "autocapitalize"))
    add_api(StorePropertyTemplate(ha.AutoCapitalizeArg, ha.HTMLInputElementArg, "autocapitalize"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "capture"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "capture"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "webkitdirectory"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "webkitdirectory"))
    add_api(LoadPropertyTemplate(None, ha.HTMLInputElementArg, "incremental"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLInputElementArg, "incremental"))

    # HTMLMenuItemElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "type"))
    add_api(StorePropertyTemplate(ha.MenuItemTypeArg, ha.HTMLMenuItemElementArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "label"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLMenuItemElementArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "icon"))
    add_api(StorePropertyTemplate(ha.ImageSrcArg, ha.HTMLMenuItemElementArg, "icon"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMenuItemElementArg, "disabled"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "checked"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMenuItemElementArg, "checked"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "radiogroup"))
    add_api(StorePropertyTemplate(ha.RadioGroupArg, ha.HTMLMenuItemElementArg, "radiogroup"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMenuItemElementArg, "default"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMenuItemElementArg, "default"))

    # HTMLTimeElement
    add_api(LoadPropertyTemplate(None, ha.HTMLTimeElementArg, "dateTime"))
    add_api(StorePropertyTemplate(ha.DateTimeArg, ha.HTMLTimeElementArg, "dateTime"))

    # HTMLMarqueeElement
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "behavior"))
    add_api(StorePropertyTemplate(ha.MarqueeBehaviorArg, ha.HTMLMarqueeElementArg, "behavior"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "bgColor"))
    add_api(StorePropertyTemplate(ColorArg, ha.HTMLMarqueeElementArg, "bgColor"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "direction"))
    add_api(StorePropertyTemplate(ha.MarqueeDirectionArg, ha.HTMLMarqueeElementArg, "direction"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "height"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLMarqueeElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "hspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLMarqueeElementArg, "hspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "loop"))
    add_api(StorePropertyTemplate(ha.MarqueeLoopArg, ha.HTMLMarqueeElementArg, "loop"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "scrollAmount"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLMarqueeElementArg, "scrollAmount"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "scrollDelay"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.HTMLMarqueeElementArg, "scrollDelay"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "trueSpeed"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLMarqueeElementArg, "trueSpeed"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "vspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLMarqueeElementArg, "vspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLMarqueeElementArg, "width"))
    add_api(StorePropertyTemplate(LengthPercentageArg, ha.HTMLMarqueeElementArg, "width"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLMarqueeElementArg, "onstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLMarqueeElementArg, "onbounce"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.HTMLMarqueeElementArg, "onfinish"))

    # HTMLTemplateElement
    add_api(LoadPropertyTemplate(hr.DocumentFragmentRet, ha.HTMLTemplateElementArg, "content"))

    # HTMLLIElement
    add_api(LoadPropertyTemplate(None, ha.HTMLLIElementArg, "value"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLLIElementArg, "value"))
    add_api(LoadPropertyTemplate(None, ha.HTMLLIElementArg, "type"))
    add_api(StorePropertyTemplate(ha.NumberingTypeArg, ha.HTMLLIElementArg, "type"))

    # HTMLImageElement
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "sizes"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "crossOrigin"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "referrerPolicy"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "name"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLImageElementArg, "name"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "alt"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLImageElementArg, "alt"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "src"))
    add_api(StorePropertyTemplate(ha.ImageSrcArg, ha.HTMLImageElementArg, "src"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "srcset"))
    add_api(StorePropertyTemplate(ha.SrcSetArg, ha.HTMLImageElementArg, "srcset"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "useMap"))
    add_api(StorePropertyTemplate(ha.UseMapArg, ha.HTMLImageElementArg, "useMap"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "isMap"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLImageElementArg, "isMap"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLImageElementArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLImageElementArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "naturalWidth"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "naturalHeight"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "complete"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "currentSrc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "lowsrc"))
    add_api(StorePropertyTemplate(ha.ImageSrcArg, ha.HTMLImageElementArg, "lowsrc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "align"))
    add_api(StorePropertyTemplate(ha.ObjectAlignArg, ha.HTMLImageElementArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "hspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLImageElementArg, "hspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "vspace"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLImageElementArg, "vspace"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "longDesc"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLImageElementArg, "longDesc"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "border"))
    add_api(StorePropertyTemplate(IntegerArg, ha.HTMLImageElementArg, "border"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "x"))
    add_api(LoadPropertyTemplate(None, ha.HTMLImageElementArg, "y"))

    # HTMLOptGroupElement
    add_api(LoadPropertyTemplate(None, ha.HTMLOptGroupElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.HTMLOptGroupElementArg, "disabled"))
    add_api(LoadPropertyTemplate(None, ha.HTMLOptGroupElementArg, "label"))
    add_api(StorePropertyTemplate(StringArg, ha.HTMLOptGroupElementArg, "label"))

    # HTMLContentElement
    add_api(LoadPropertyTemplate(None, ha.HTMLContentElementArg, "select"))
    add_api(StorePropertyTemplate(ha.ContentSelectArg, ha.HTMLContentElementArg, "select"))

    # ElementList
    add_api(ArrayLoadIndexTemplate(hr.ElementRet, ha.ElementListArg))
    add_api(ArrayStoreIndexTemplate(ha.ElementArg, ha.ElementListArg))

    # HTMLElementList
    add_api(ArrayLoadIndexTemplate(hr.HTMLElementRet, ha.HTMLElementListArg))
    add_api(ArrayStoreIndexTemplate(ha.HTMLElementArg, ha.HTMLElementListArg))

    ######################################################
    # Web Media
    ######################################################
    # AudioTrackList
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.AudioTrackListArg, "onchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.AudioTrackListArg, "onaddtrack"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.AudioTrackListArg, "onremovetrack"))
    add_api(ArrayLoadIndexTemplate(hr.AudioTrackRet, ha.AudioTrackListArg))

    # AudioTrack
    add_api(LoadPropertyTemplate(None, ha.AudioTrackArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.AudioTrackArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.AudioTrackArg, "language"))
    add_api(LoadPropertyTemplate(None, ha.AudioTrackArg, "id"))
    add_api(LoadPropertyTemplate(None, ha.AudioTrackArg, "enabled"))
    add_api(StorePropertyTemplate(BooleanArg, ha.AudioTrackArg, "enabled"))

    # VideoTrackList
    add_api(LoadPropertyTemplate(None, ha.VideoTrackListArg, "selectedIndex"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.VideoTrackListArg, "onchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.VideoTrackListArg, "onaddtrack"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.VideoTrackListArg, "onremovetrack"))
    add_api(ArrayLoadIndexTemplate(hr.VideoTrackRet, ha.VideoTrackListArg))

    # VideoTrack
    add_api(LoadPropertyTemplate(None, ha.VideoTrackArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.VideoTrackArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.VideoTrackArg, "language"))
    add_api(LoadPropertyTemplate(None, ha.VideoTrackArg, "id"))
    add_api(LoadPropertyTemplate(None, ha.VideoTrackArg, "selected"))
    add_api(StorePropertyTemplate(BooleanArg, ha.VideoTrackArg, "selected"))

    # TextTrackList
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackListArg, "onchange"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackListArg, "onaddtrack"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackListArg, "onremovetrack"))
    add_api(ArrayLoadIndexTemplate(hr.TextTrackRet, ha.TextTrackListArg))

    # TextTrackCueList
    add_api(ArrayLoadIndexTemplate(hr.TextTrackCueRet, ha.TextTrackCueListArg))

    # TextTrackCue
    add_api(LoadPropertyTemplate(hr.TextTrackRet, ha.TextTrackCueArg, "track"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackCueArg, "id"))
    add_api(StorePropertyTemplate(StringArg, ha.TextTrackCueArg, "id"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackCueArg, "startTime"))
    add_api(StorePropertyTemplate(ClockArg, ha.TextTrackCueArg, "startTime"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackCueArg, "endTime"))
    add_api(StorePropertyTemplate(ClockArg, ha.TextTrackCueArg, "endTime"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackCueArg, "pauseOnExit"))
    add_api(StorePropertyTemplate(BooleanArg, ha.TextTrackCueArg, "pauseOnExit"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackCueArg, "onenter"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackCueArg, "onexit"))

    # TextTrack
    add_api(LoadPropertyTemplate(None, ha.TextTrackArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackArg, "label"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackArg, "language"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackArg, "id"))
    add_api(LoadPropertyTemplate(None, ha.TextTrackArg, "mode"))
    add_api(StorePropertyTemplate(ha.TextTrackModeArg, ha.TextTrackArg, "mode"))
    add_api(LoadPropertyTemplate(hr.TextTrackCueListRet, ha.TextTrackArg, "cues"))
    add_api(LoadPropertyTemplate(hr.TextTrackCueListRet, ha.TextTrackArg, "activeCues"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.TextTrackArg, "oncuechange"))
    add_api(LoadPropertyTemplate(hr.VTTRegionListRet, ha.TextTrackArg, "regions"))

    # VTTRegionList
    add_api(LoadPropertyTemplate(None, ha.VTTRegionListArg, "length"))

    # VTTRegion
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "id"))
    add_api(StorePropertyTemplate(StringArg, ha.VTTRegionArg, "id"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.VTTRegionArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.VTTRegionArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "regionAnchorX"))
    add_api(StorePropertyTemplate(FloatArg, ha.VTTRegionArg, "regionAnchorX"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "regionAnchorY"))
    add_api(StorePropertyTemplate(FloatArg, ha.VTTRegionArg, "regionAnchorY"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "viewportAnchorX"))
    add_api(StorePropertyTemplate(FloatArg, ha.VTTRegionArg, "viewportAnchorX"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "viewportAnchorY"))
    add_api(StorePropertyTemplate(FloatArg, ha.VTTRegionArg, "viewportAnchorY"))
    add_api(LoadPropertyTemplate(None, ha.VTTRegionArg, "scroll"))
    add_api(StorePropertyTemplate(ha.VTTRegionScrollArg, ha.VTTRegionArg, "scroll"))
    add_api(LoadPropertyTemplate(hr.TextTrackRet, ha.VTTRegionArg, "track"))

    # VTTCue
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "regionId"))
    add_api(StorePropertyTemplate(StringArg, ha.VTTCueArg, "regionId"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "vertical"))
    add_api(StorePropertyTemplate(ha.VTTCueVerticalArg, ha.VTTCueArg, "vertical"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "snapToLines"))
    add_api(StorePropertyTemplate(BooleanArg, ha.VTTCueArg, "snapToLines"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "line"))
    add_api(StorePropertyTemplate(ha.VTTCueLineArg, ha.VTTCueArg, "line"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "position"))
    add_api(StorePropertyTemplate(ha.VTTCuePositionArg, ha.VTTCueArg, "position"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "size"))
    add_api(StorePropertyTemplate(FloatArg, ha.VTTCueArg, "size"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "align"))
    add_api(StorePropertyTemplate(ha.VTTCueAlignArg, ha.VTTCueArg, "align"))
    add_api(LoadPropertyTemplate(None, ha.VTTCueArg, "text"))
    add_api(StorePropertyTemplate(StringArg, ha.VTTCueArg, "text"))

    ######################################################
    # Web Animations
    ######################################################
    # Animations
    add_api(ArrayLoadIndexTemplate(hr.AnimationRet, ha.AnimationsArg))
    add_api(ArrayStoreIndexTemplate(ha.AnimationArg, ha.AnimationsArg))

    # Animation
    add_api(LoadPropertyTemplate(hr.AnimationEffectReadOnlyRet, ha.AnimationArg, "effect"))
    add_api(StorePropertyTemplate(ha.AnimationEffectReadOnlyArg, ha.AnimationArg, "effect"))
    add_api(LoadPropertyTemplate(hr.AnimationTimelineRet, ha.AnimationArg, "timeline"))
    add_api(LoadPropertyTemplate(None, ha.AnimationArg, "startTime"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationArg, "startTime"))
    add_api(LoadPropertyTemplate(None, ha.AnimationArg, "currentTime"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationArg, "currentTime"))
    add_api(LoadPropertyTemplate(None, ha.AnimationArg, "playbackRate"))
    add_api(StorePropertyTemplate(FloatArg, ha.AnimationArg, "playbackRate"))
    add_api(LoadPropertyTemplate(None, ha.AnimationArg, "playState"))
    add_api(StorePropertyTemplate(ha.PlayStateArg, ha.AnimationArg, "playState"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.AnimationArg, "onfinish"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.AnimationArg, "oncancel"))
    # add_api(LoadPropertyTemplate(None, ha.AnimationArg, "finished"))
    # add_api(LoadPropertyTemplate(None, ha.AnimationArg, "ready"))

    # AnimationTimeline
    add_api(LoadPropertyTemplate(None, ha.AnimationTimelineArg, "currentTime"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationTimelineArg, "currentTime"))

    # AnimationEffectReadOnly
    add_api(LoadPropertyTemplate(hr.AnimationEffectTimingReadOnlyRet, ha.AnimationEffectReadOnlyArg, "timing"))

    # AnimationEffectTimingReadOnly
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "delay"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "endDelay"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "fill"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "iterationStart"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "iterations"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "duration"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "direction"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEffectTimingReadOnlyArg, "easing"))

    # AnimationEffectTiming
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationEffectTimingArg, "delay"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationEffectTimingArg, "endDelay"))
    add_api(StorePropertyTemplate(ha.AnimationFillArg, ha.AnimationEffectTimingArg, "fill"))
    add_api(StorePropertyTemplate(FloatArg, ha.AnimationEffectTimingArg, "iterationStart"))
    add_api(StorePropertyTemplate(IntegerArg, ha.AnimationEffectTimingArg, "iterations"))
    add_api(StorePropertyTemplate(ClockInMsArg, ha.AnimationEffectTimingArg, "duration"))
    add_api(StorePropertyTemplate(ha.AnimationDirectionArg, ha.AnimationEffectTimingArg, "direction"))
    add_api(StorePropertyTemplate(ha.AnimationEasingArg, ha.AnimationEffectTimingArg, "easing"))

    ######################################################
    # Event
    # TODO: TouchEvent, RelatedEvent, FontFaceSetLoadEvent, TrackEvent
    ######################################################
    # DataTransfer
    add_api(LoadPropertyTemplate(None, ha.DataTransferArg, "types"))
    add_api(LoadPropertyTemplate(None, ha.DataTransferArg, "dropEffect"))
    add_api(StorePropertyTemplate(ha.DropEffectArg, ha.DataTransferArg, "dropEffect"))
    add_api(LoadPropertyTemplate(None, ha.DataTransferArg, "effectAllowed"))
    add_api(StorePropertyTemplate(ha.EffectAllowedArg, ha.DataTransferArg, "effectAllowed"))
    add_api(LoadPropertyTemplate(hr.DataTransferItemListRet, ha.DataTransferArg, "items"))

    # DataTransferItemList
    add_api(ArrayLoadIndexTemplate(hr.DataTransferItemRet, ha.DataTransferItemListArg))

    # DataTransferItem
    add_api(LoadPropertyTemplate(None, ha.DataTransferItemArg, "kind"))
    add_api(LoadPropertyTemplate(None, ha.DataTransferItemArg, "type"))

    # ResourceProgressEvent
    add_api(LoadPropertyTemplate(None, ha.ResourceProgressEventArg, "url"))

    # TextEvent
    add_api(LoadPropertyTemplate(None, ha.TextEventArg, "data"))

    # ClipboardEvent
    add_api(LoadPropertyTemplate(hr.DataTransferRet, ha.ClipboardEventArg, "clipboardData"))

    # ProgressEvent
    add_api(LoadPropertyTemplate(None, ha.ProgressEventArg, "lengthComputable"))
    add_api(LoadPropertyTemplate(None, ha.ProgressEventArg, "loaded"))
    add_api(LoadPropertyTemplate(None, ha.ProgressEventArg, "total"))

    # WheelEvent
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "deltaX"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "deltaY"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "deltaZ"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "deltaMode"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "wheelDeltaX"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "wheelDeltaY"))
    add_api(LoadPropertyTemplate(None, ha.WheelEventArg, "wheelDelta"))

    # HashChangeEvent
    add_api(LoadPropertyTemplate(None, ha.HashChangeEventArg, "oldURL"))
    add_api(LoadPropertyTemplate(None, ha.HashChangeEventArg, "newURL"))

    # MouseEvent
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "screenX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "screenY"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "clientX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "clientY"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "ctrlKey"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "shiftKey"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "altKey"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "metaKey"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "button"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "buttons"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "pageX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "pageY"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "x"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "y"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "offsetX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "offsetY"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "movementX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "movementY"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "region"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MouseEventArg, "fromElement"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MouseEventArg, "toElement"))
    add_api(LoadPropertyTemplate(hr.EventTargetsRet, ha.MouseEventArg, "relatedTarget"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "which"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "layerX"))
    add_api(LoadPropertyTemplate(None, ha.MouseEventArg, "layerY"))

    # FocusEvent
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.FocusEventArg, "relatedTarget"))

    # TransitionEvent
    add_api(LoadPropertyTemplate(None, ha.TransitionEventArg, "propertyName"))
    add_api(LoadPropertyTemplate(None, ha.TransitionEventArg, "elapsedTime"))
    add_api(LoadPropertyTemplate(None, ha.TransitionEventArg, "pseudoElement"))

    # AnimationPlaybackEvent
    add_api(LoadPropertyTemplate(None, ha.AnimationPlaybackEventArg, "currentTime"))
    add_api(LoadPropertyTemplate(None, ha.AnimationPlaybackEventArg, "timelineTime"))

    # PopStateEvent
    add_api(LoadPropertyTemplate(None, ha.PopStateEventArg, "state"))

    # DragEvent
    add_api(LoadPropertyTemplate(hr.DataTransferRet, ha.DragEventArg, "dataTransfer"))

    # Event
    add_api(LoadPropertyTemplate(None, ha.EventArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "eventPhase"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "bubbles"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "cancelable"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "defaultPrevented"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "composed"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "isTrusted"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "timeStamp"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "returnValue"))
    add_api(StorePropertyTemplate(BooleanArg, ha.EventArg, "returnValue"))
    add_api(LoadPropertyTemplate(None, ha.EventArg, "cancelBubble"))
    add_api(StorePropertyTemplate(BooleanArg, ha.EventArg, "cancelBubble"))
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.EventArg, "path"))
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.EventArg, "target"))
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.EventArg, "currentTarget"))
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.EventArg, "srcElement"))

    # InputDeviceCapabilities
    add_api(LoadPropertyTemplate(None, ha.InputDeviceCapabilitiesArg, "firesTouchEvents"))

    # UIEvent
    add_api(LoadPropertyTemplate(None, ha.UIEventArg, "detail"))
    add_api(LoadPropertyTemplate(None, ha.UIEventArg, "which"))
    add_api(LoadPropertyTemplate(hr.WindowRet, ha.UIEventArg, "view"))
    add_api(LoadPropertyTemplate(hr.InputDeviceCapabilitiesRet, ha.UIEventArg, "sourceCapabilities"))

    # CompositionEvent
    add_api(LoadPropertyTemplate(None, ha.CompositionEventArg, "data"))

    # InputEvent
    add_api(LoadPropertyTemplate(None, ha.InputEventArg, "inputType"))
    add_api(LoadPropertyTemplate(None, ha.InputEventArg, "data"))
    add_api(LoadPropertyTemplate(hr.DataTransferRet, ha.InputEventArg, "dataTransfer"))
    add_api(LoadPropertyTemplate(None, ha.InputEventArg, "isComposing"))

    # PageTransitionEvent
    add_api(LoadPropertyTemplate(None, ha.PageTransitionEventArg, "persisted"))

    # StaticRanges
    add_api(ArrayLoadIndexTemplate(hr.StaticRangeRet, ha.StaticRangesArg))
    add_api(ArrayStoreIndexTemplate(ha.StaticRangeArg, ha.StaticRangesArg))

    # StaticRange
    add_api(LoadPropertyTemplate(None, ha.StaticRangeArg, "collapsed"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.StaticRangeArg, "endContainer"))
    add_api(StorePropertyTemplate(ha.ElementArg, ha.StaticRangeArg, "endContainer"))
    add_api(LoadPropertyTemplate(None, ha.StaticRangeArg, "endOffset"))
    add_api(StorePropertyTemplate(IntegerArg, ha.StaticRangeArg, "endOffset"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.StaticRangeArg, "startContainer"))
    add_api(StorePropertyTemplate(ha.ElementArg, ha.StaticRangeArg, "startContainer"))
    add_api(LoadPropertyTemplate(None, ha.StaticRangeArg, "startOffset"))
    add_api(StorePropertyTemplate(IntegerArg, ha.StaticRangeArg, "startOffset"))

    # PointerEvent
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "pointerId"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "pressure"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "tiltX"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "tiltY"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "pointerType"))
    add_api(LoadPropertyTemplate(None, ha.PointerEventArg, "isPrimary"))

    # PromiseRejectionEvent
    add_api(LoadPropertyTemplate(None, ha.PromiseRejectionEventArg, "promise"))
    add_api(LoadPropertyTemplate(None, ha.PromiseRejectionEventArg, "reason"))

    # MessageEvent
    add_api(LoadPropertyTemplate(None, ha.MessageEventArg, "data"))
    add_api(LoadPropertyTemplate(None, ha.MessageEventArg, "origin"))
    add_api(LoadPropertyTemplate(None, ha.MessageEventArg, "lastEventId"))
    add_api(LoadPropertyTemplate(hr.EventTargetRet, ha.MessageEventArg, "source"))
    add_api(LoadPropertyTemplate(hr.MessagePortRet, ha.MessageEventArg, "ports"))
    add_api(LoadPropertyTemplate(None, ha.MessageEventArg, "suborigin"))

    # MutationEvent
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MutationEventArg, "relatedNode"))
    add_api(LoadPropertyTemplate(None, ha.MutationEventArg, "prevValue"))
    add_api(LoadPropertyTemplate(None, ha.MutationEventArg, "newValue"))
    add_api(LoadPropertyTemplate(None, ha.MutationEventArg, "attrName"))
    add_api(LoadPropertyTemplate(None, ha.MutationEventArg, "attrChange"))

    # AnimationEvent
    add_api(LoadPropertyTemplate(None, ha.AnimationEventArg, "animationName"))
    add_api(LoadPropertyTemplate(None, ha.AnimationEventArg, "elapsedTime"))

    # ErrorEvent
    add_api(LoadPropertyTemplate(None, ha.ErrorEventArg, "message"))
    add_api(LoadPropertyTemplate(None, ha.ErrorEventArg, "filename"))
    add_api(LoadPropertyTemplate(None, ha.ErrorEventArg, "lineno"))
    add_api(LoadPropertyTemplate(None, ha.ErrorEventArg, "colno"))
    add_api(LoadPropertyTemplate(None, ha.ErrorEventArg, "error"))

    # KeyboardEvent
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "key"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "code"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "location"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "ctrlKey"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "shiftKey"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "altKey"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "metaKey"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "repeat"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "charCode"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "keyCode"))
    add_api(LoadPropertyTemplate(None, ha.KeyboardEventArg, "which"))

    # CustomEvent
    add_api(LoadPropertyTemplate(None, ha.CustomEventArg, "detail"))

    # ApplicationCacheErrorEvent
    add_api(LoadPropertyTemplate(None, ha.ApplicationCacheErrorEventArg, "reason"))
    add_api(LoadPropertyTemplate(None, ha.ApplicationCacheErrorEventArg, "url"))
    add_api(LoadPropertyTemplate(None, ha.ApplicationCacheErrorEventArg, "status"))
    add_api(LoadPropertyTemplate(None, ha.ApplicationCacheErrorEventArg, "message"))

    # SecurityPolicyViolationEvent
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "documentURI"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "referrer"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "blockedURI"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "violatedDirective"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "effectiveDirective"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "originalPolicy"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "sourceFile"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "statusCode"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "lineNumber"))
    add_api(LoadPropertyTemplate(None, ha.SecurityPolicyViolationEventArg, "columnNumber"))

    # BeforeUnloadEvent
    add_api(LoadPropertyTemplate(None, ha.BeforeUnloadEventArg, "returnValue"))
    add_api(StorePropertyTemplate(StringArg, ha.BeforeUnloadEventArg, "returnValue"))

    # MediaQueryListEvent
    add_api(LoadPropertyTemplate(None, ha.MediaQueryListEventArg, "media"))
    add_api(LoadPropertyTemplate(None, ha.MediaQueryListEventArg, "matches"))

    ######################################################
    # Misc
    ######################################################
    # XPathResult
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "resultType"))
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "numberValue"))
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "stringValue"))
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "booleanValue"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.XPathResultArg, "singleNodeValue"))
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "invalidIteratorState"))
    add_api(LoadPropertyTemplate(None, ha.XPathResultArg, "snapshotLength"))

    # ApplicationCache
    add_api(LoadPropertyTemplate(None, ha.ApplicationCacheArg, "status"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onchecking"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onnoupdate"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "ondownloading"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onprogress"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onupdateready"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "oncached"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.ApplicationCacheArg, "onobsolete"))

    # BarProp
    add_api(LoadPropertyTemplate(None, ha.BarPropArg, "visible"))

    # Screen
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "availWidth"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "availHeight"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "colorDepth"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "pixelDepth"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "availLeft"))
    add_api(LoadPropertyTemplate(None, ha.ScreenArg, "availTop"))

    # History
    add_api(LoadPropertyTemplate(None, ha.HistoryArg, "state"))
    add_api(LoadPropertyTemplate(None, ha.HistoryArg, "length"))
    add_api(LoadPropertyTemplate(None, ha.HistoryArg, "scrollRestoration"))
    add_api(StorePropertyTemplate(ha.ScrollRestorationArg, ha.HistoryArg, "scrollRestoration"))

    # VisualViewport
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "scrollLeft"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "scrollTop"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "pageX"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "pageY"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "clientWidth"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "clientHeight"))
    add_api(LoadPropertyTemplate(None, ha.VisualViewportArg, "scale"))

    # MessageChannel
    add_api(LoadPropertyTemplate(hr.MessagePortRet, ha.MessageChannelArg, "port1"))
    add_api(LoadPropertyTemplate(hr.MessagePortRet, ha.MessageChannelArg, "port2"))

    # MessagePort
    add_api(StorePropertyTemplate(ha.EventHandlerArg, ha.MessagePortArg, "onmessage"))

    # ValidityState
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "valueMissing"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "typeMismatch"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "patternMismatch"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "tooLong"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "tooShort"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "rangeUnderflow"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "rangeOverflow"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "stepMismatch"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "badInput"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "customError"))
    add_api(LoadPropertyTemplate(None, ha.ValidityStateArg, "valid"))

    # Navigator
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "vendor"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "vendorSub"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "productSub"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "maxTouchPoints"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "appCodeName"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "appName"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "appVersion"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "platform"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "product"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "userAgent"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "language"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "languages"))
    add_api(LoadPropertyTemplate(None, ha.NavigatorArg, "onLine"))

    # MediaError
    add_api(LoadPropertyTemplate(None, ha.MediaErrorArg, "code"))

    # Range
    add_api(LoadPropertyTemplate(None, ha.RangeArg, "collapsed"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.RangeArg, "commonAncestorContainer"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.RangeArg, "endContainer"))
    add_api(LoadPropertyTemplate(None, ha.RangeArg, "endOffset"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.RangeArg, "startContainer"))
    add_api(LoadPropertyTemplate(None, ha.RangeArg, "startOffset"))

    # MutationRecords
    add_api(ArrayLoadIndexTemplate(hr.MutationRecordRet, ha.MutationRecordsArg))

    # MutationRecord
    add_api(LoadPropertyTemplate(None, ha.MutationRecordArg, "type"))
    add_api(LoadPropertyTemplate(None, ha.MutationRecordArg, "oldValue"))
    add_api(LoadPropertyTemplate(None, ha.MutationRecordArg, "attributeName"))
    add_api(LoadPropertyTemplate(None, ha.MutationRecordArg, "attributeNamespace"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MutationRecordArg, "target"))
    add_api(LoadPropertyTemplate(hr.NodeListRet, ha.MutationRecordArg, "addedNodes"))
    add_api(LoadPropertyTemplate(hr.NodeListRet, ha.MutationRecordArg, "removedNodes"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MutationRecordArg, "previousSibling"))
    add_api(LoadPropertyTemplate(hr.ElementRet, ha.MutationRecordArg, "nextSibling"))

    # DOMRect
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "x"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "x"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "y"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "y"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "width"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "width"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "height"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "height"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "top"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "top"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "right"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "right"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "bottom"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "bottom"))
    add_api(LoadPropertyTemplate(None, ha.DOMRectArg, "left"))
    add_api(StorePropertyTemplate(IntegerArg, ha.DOMRectArg, "left"))

    # DOMRectList
    add_api(ArrayLoadIndexTemplate(hr.DOMRectRet, ha.DOMRectListArg))

    # URL
    add_api(LoadPropertyTemplate(None, ha.URLArg, "href"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "href"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "origin"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "protocol"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "protocol"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "username"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "username"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "password"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "password"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "host"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "host"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "hostname"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "hostname"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "port"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "port"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "pathname"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "pathname"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "search"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "search"))
    add_api(LoadPropertyTemplate(None, ha.URLArg, "hash"))
    add_api(StorePropertyTemplate(StringArg, ha.URLArg, "hash"))
    add_api(LoadPropertyTemplate(hr.URLSearchParamsRet, ha.URLArg, "searchParams"))

    # DOMTokenList
    # FIXME: set value
    add_api(LoadPropertyTemplate(None, ha.DOMTokenListArg, "length"))
    add_api(LoadPropertyTemplate(None, ha.DOMTokenListArg, "value"))
