import docs
from js import API, APITemplate, add_api
from js.function import FunctionTemplate, is_satiable_arg
from js.function.html import ListItemTemplate, SetAttributeTemplate, \
    InsertBeforeTemplate, ReplaceChildTemplate, RemoveChildTemplate
from js.arg import IntegerArg, FloatArg, ClockArg, NullArg, StringArg, \
    BooleanArg, IndexArg, RandomSelectorArg, ClockInMsArg, ConstStringArgWrapper
from utils.random import Random
import js.arg.html as ha
import js.arg.svg as sa
import js.ret.html as hr
import js.ret.svg as sr


############################################################
# x.getItem(i % x.numberOfItems)
############################################################
class GetItem(API):
    def __init__(self, ret, this, selector):
        super().__init__(ret, this)
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        if self.ret is not None:
            self.ret.generate(context)
        self.selector.generate(context)
    
    def mutate(self, context):
        if Random.bool():
            self.this.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        lhs = "var {} = ".format(str(self.ret)) if self.ret is not None else ""
        return "{0}{1}.getItem({2} % {1}.numberOfItems)".format(
            lhs,
            str(self.this),
            str(self.selector)
        )


class GetItemTemplate(APITemplate):
    def __init__(self, ret_class, this_class):
        super().__init__(ret_class, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return GetItem(self.ret_class(), self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# x.removeItem(i % x.numberOfItems)
############################################################
class RemoveItem(API):
    def __init__(self, this, selector):
        super().__init__(None, this)
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.selector.generate(context)
    
    def mutate(self, context):
        if Random.bool():
            self.this.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "{0}.removeItem({1} % {0}.numberOfItems)".format(
            str(self.this),
            str(self.selector)
        )


class RemoveItemTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return RemoveItem(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# x.insertItemBefore(y, i % x.numberOfItems)
############################################################
class InsertItemBefore(API):
    def __init__(self, this, arg, selector):
        super().__init__(None, this)
        self.arg = arg
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.arg.generate(context)
        self.selector.generate(context)
    
    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.arg.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.arg.merge_fix(merge_map)

    def __str__(self):
        return "{0}.insertItemBefore({1}, {2} % {0}.numberOfItems)".format(
            str(self.this),
            str(self.arg),
            str(self.selector)
        )


class InsertItemBeforeTemplate(APITemplate):
    def __init__(self, this_class, arg_class):
        super().__init__(None, this_class)
        self.arg_class = arg_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return InsertItemBefore(self.this_class(), self.arg_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.arg_class, context)


############################################################
# x.replaceItem(y, i % x.numberOfItems)
############################################################
class ReplaceItem(API):
    def __init__(self, this, arg, selector):
        super().__init__(None, this)
        self.arg = arg
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.arg.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.arg.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.arg.merge_fix(merge_map)

    def __str__(self):
        return "{0}.replaceItem({1}, {2} % {0}.numberOfItems)".format(
            str(self.this),
            str(self.arg),
            str(self.selector)
        )


class ReplaceItemTemplate(APITemplate):
    def __init__(self, this_class, arg_class):
        super().__init__(None, this_class)
        self.arg_class = arg_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return ReplaceItem(self.this_class(), self.arg_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.arg_class, context)


class CreateElementNS(API):
    svg_elements = {
        "a": sr.SVGAElementRet,
        "altGlyphDef": sr.SVGAltGlyphDefElementRet,
        "altGlyph": sr.SVGAltGlyphElementRet,
        "altGlyphItem": sr.SVGAltGlyphItemElementRet,
        "animate": sr.SVGAnimateElementRet,
        "animateMotion": sr.SVGAnimateMotionElementRet,
        "animateTransform": sr.SVGAnimateTransformElementRet,
        "circle": sr.SVGCircleElementRet,
        "clipPath": sr.SVGClipPathElementRet,
        "cursor": sr.SVGCursorElementRet,
        "defs": sr.SVGDefsElementRet,
        "desc": sr.SVGDescElementRet,
        "discard": sr.SVGDiscardElementRet,
        "ellipse": sr.SVGEllipseElementRet,
        "feBlend": sr.SVGFEBlendElementRet,
        "feColorMatrix": sr.SVGFEColorMatrixElementRet,
        "feComponentTransfer": sr.SVGFEComponentTransferElementRet,
        "feComposite": sr.SVGFECompositeElementRet,
        "feConvolveMatrix": sr.SVGFEConvolveMatrixElementRet,
        "feDiffuseLighting": sr.SVGFEDiffuseLightingElementRet,
        "feDisplacementMap": sr.SVGFEDisplacementMapElementRet,
        "feDistantLight": sr.SVGFEDistantLightElementRet,
        "feDropShadow": sr.SVGFEDropShadowElementRet,
        "feFlood": sr.SVGFEFloodElementRet,
        "feFuncA": sr.SVGFEFuncAElementRet,
        "feFuncB": sr.SVGFEFuncBElementRet,
        "feFuncG": sr.SVGFEFuncGElementRet,
        "feFuncR": sr.SVGFEFuncRElementRet,
        "feGaussianBlur": sr.SVGFEGaussianBlurElementRet,
        "feImage": sr.SVGFEImageElementRet,
        "feMerge": sr.SVGFEMergeElementRet,
        "feMergeNode": sr.SVGFEMergeNodeElementRet,
        "feMorphology": sr.SVGFEMorphologyElementRet,
        "feOffset": sr.SVGFEOffsetElementRet,
        "fePointLight": sr.SVGFEPointLightElementRet,
        "feSpecularLighting": sr.SVGFESpecularLightingElementRet,
        "feSpotLight": sr.SVGFESpotLightElementRet,
        "feTile": sr.SVGFETileElementRet,
        "feTurbulence": sr.SVGFETurbulenceElementRet,
        "filter": sr.SVGFilterElementRet,
        "font": sr.SVGFontElementRet,
        "font-face": sr.SVGFontFaceElementRet,
        "font-face-format": sr.SVGFontFaceFormatElementRet,
        "font-face-name": sr.SVGFontFaceNameElementRet,
        "font-face-src": sr.SVGFontFaceSrcElementRet,
        "font-face-uri": sr.SVGFontFaceUriElementRet,
        "foreignObject": sr.SVGForeignObjectElementRet,
        "g": sr.SVGGElementRet,
        "glyph": sr.SVGGlyphElementRet,
        "glyphRef": sr.SVGGlyphRefElementRet,
        "hkern": sr.SVGHKernElementRet,
        "image": sr.SVGImageElementRet,
        "line": sr.SVGLineElementRet,
        "linearGradient": sr.SVGLinearGradientElementRet,
        "mpath": sr.SVGMPathElementRet,
        "marker": sr.SVGMarkerElementRet,
        "mask": sr.SVGMaskElementRet,
        "metadata": sr.SVGMetadataElementRet,
        "missing-glyph": sr.SVGMissingGlyphElementRet,
        "path": sr.SVGPathElementRet,
        "pattern": sr.SVGPatternElementRet,
        "polygon": sr.SVGPolygonElementRet,
        "polyline": sr.SVGPolylineElementRet,
        "radialGradient": sr.SVGRadialGradientElementRet,
        "rect": sr.SVGRectElementRet,
        "svg": sr.SVGSVGElementRet,
        "set": sr.SVGSetElementRet,
        "stop": sr.SVGStopElementRet,
        "style": sr.SVGStyleElementRet,
        "switch": sr.SVGSwitchElementRet,
        "symbol": sr.SVGSymbolElementRet,
        "tref": sr.SVGTRefElementRet,
        "tspan": sr.SVGTSpanElementRet,
        "text": sr.SVGTextElementRet,
        "textPath": sr.SVGTextPathElementRet,
        "title": sr.SVGTitleElementRet,
        "use": sr.SVGUseElementRet,
        "vkern": sr.SVGVKernElementRet,
        "view": sr.SVGViewElementRet,
    }

    def __init__(self, this):
        super().__init__(None, this)
        self.tag = None

    def generate(self, context):
        self.this.generate(context)
        self.tag = Random.choice(docs.svg_tags)
        self.ret = (CreateElementNS.svg_elements[self.tag])()
        self.ret.generate(context)

    def mutate(self, _):
        pass

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "var {} = {}.createElementNS(\"http://www.w3.org/2000/svg\", \"{}\")".format(
            str(self.ret), str(self.this), self.tag
        )


class CreateElementNSTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)

    def instantiate(self):
        return CreateElementNS(self.this_class())

    def satiable(self, context):
        return True


def initialize_svg_functions():
    # SVGAngle
    add_api(FunctionTemplate(None, sa.SVGAngleArg, "convertToSpecifiedUnits", IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGAngleArg, "newValueSpecifiedUnits", IntegerArg, FloatArg))

    # SVGAnimationElementArg
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "beginElement"))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "beginElementAt", ClockArg))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "endElement"))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "endElementAt", ClockArg))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "getCurrentTime"))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "getSimpleDuration"))
    add_api(FunctionTemplate(None, sa.SVGAnimationElementArg, "getStartTime"))

    # SVGElement
    add_api(FunctionTemplate(None, sa.SVGElementArg, "after", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "after", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "append", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "append", sa.SVGElementArg))
    add_api(FunctionTemplate(sr.SVGCollectionRet, sa.SVGElementArg, "getElementsByTagName", sa.SVGTagArg))
    add_api(FunctionTemplate(sr.SVGCollectionRet, sa.SVGElementArg, "getElementsByTagNameNS",
                             ConstStringArgWrapper("http://www.w3.org/2000/svg"), sa.SVGTagArg))
    add_api(FunctionTemplate(sr.SVGCollectionRet, sa.SVGElementArg, "getElementsByClassName", ha.ClassArg))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGElementArg, "querySelector", sa.SVGQuerySelectorArg))
    add_api(FunctionTemplate(sr.SVGNodeListRet, sa.SVGElementArg, "querySelectorAll", sa.SVGQuerySelectorArg))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGElementArg, "closest", sa.SVGQuerySelectorArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "matches", sa.SVGQuerySelectorArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "webkitMatchesSelector", sa.SVGQuerySelectorArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "appendChild", sa.SVGElementArg))
    add_api(FunctionTemplate(hr.ShadowRootRet, sa.SVGElementArg, "attachShadow", ha.ShadowRootInitArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "before", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "before", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "blur"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "compareDocumentPosition", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "contains", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "focus"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "hasAttributes"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "hasChildNodes"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "insertAdjacentElement", ha.InsertPositionArg, sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "insertAdjacentText", ha.InsertPositionArg, StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "insertAdjacentHTML", ha.InsertPositionArg, sa.SVGHTMLStringArg))
    add_api(InsertBeforeTemplate(sa.SVGElementArg, sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "insertBefore", sa.SVGElementArg, NullArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "isDefaultNamespace", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "isEqualNode", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "isSameNode", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "lookupNamespaceURI", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "lookupPrefix", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "normalize"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "prepend", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "prepend", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "remove"))
    add_api(RemoveChildTemplate(sa.SVGElementArg))
    add_api(ReplaceChildTemplate(sa.SVGElementArg, sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "replaceWith", StringArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "replaceWith", sa.SVGElementArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "requestPointerLock"))
    add_api(FunctionTemplate(hr.DOMRectListRet, sa.SVGElementArg, "getClientRects"))
    add_api(FunctionTemplate(hr.DOMRectRet, sa.SVGElementArg, "getBoundingClientRect"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scroll"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scroll", FloatArg, FloatArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scroll", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollIntoView", BooleanArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollIntoView", ha.ScrollIntoViewOptionsArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollIntoViewIfNeeded", BooleanArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollTo"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollTo", FloatArg, FloatArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollTo", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollBy"))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollBy", FloatArg, FloatArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "scrollBy", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "setPointerCapture", IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "releasePointerCapture", IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGElementArg, "hasPointerCapture", IntegerArg))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGElementArg, "cloneNode", BooleanArg))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGElementArg, "getRootNode"))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGElementArg, "getRootNode", ha.GetRootNodeOptionsArg))

    # SVGFEDropShadowElement
    add_api(FunctionTemplate(None, sa.SVGFEDropShadowElementArg, "setStdDeviation", FloatArg, FloatArg))

    # SVGFEGaussianBlurElement
    add_api(FunctionTemplate(None, sa.SVGFEGaussianBlurElementArg, "setStdDeviation", FloatArg, FloatArg))

    # SVGFEMorphologyElement
    add_api(FunctionTemplate(None, sa.SVGFEMorphologyElementArg, "setRadius", FloatArg, FloatArg))

    # SVGGeometryElement
    add_api(FunctionTemplate(None, sa.SVGGeometryElementArg, "isPointInFill", sa.SVGPointArg))
    add_api(FunctionTemplate(None, sa.SVGGeometryElementArg, "isPointInStroke", sa.SVGPointArg))

    # SVGLength
    add_api(FunctionTemplate(None, sa.SVGLengthArg, "convertToSpecifiedUnits", IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGLengthArg, "newValueSpecifiedUnits", IntegerArg, FloatArg))

    # SVGLengthList
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "appendItem", sa.SVGLengthArg))
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "initialize", sa.SVGLengthArg))
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "insertItemBefore", sa.SVGLengthArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGLengthListArg, sa.SVGLengthArg))
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGLengthListArg))
    add_api(FunctionTemplate(None, sa.SVGLengthListArg, "replaceItem", sa.SVGLengthArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGLengthListArg, sa.SVGLengthArg))
    add_api(FunctionTemplate(sr.SVGLengthRet, sa.SVGLengthListArg, "getItem", IndexArg))
    add_api(GetItemTemplate(sr.SVGLengthRet, sa.SVGLengthListArg))

    # SVGMarkerElement
    add_api(FunctionTemplate(None, sa.SVGMarkerElementArg, "setOrientToAngle", sa.SVGAngleArg))
    add_api(FunctionTemplate(None, sa.SVGMarkerElementArg, "setOrientToAuto"))

    # SVGNumberList
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "appendItem", sa.SVGNumberArg))
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "initialize", sa.SVGNumberArg))
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "insertItemBefore", sa.SVGNumberArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGNumberListArg, sa.SVGNumberArg))
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGNumberListArg))
    add_api(FunctionTemplate(None, sa.SVGNumberListArg, "replaceItem", sa.SVGNumberArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGNumberListArg, sa.SVGNumberArg))
    add_api(FunctionTemplate(sr.SVGNumberRet, sa.SVGNumberListArg, "getItem", IndexArg))
    add_api(GetItemTemplate(sr.SVGNumberRet, sa.SVGNumberListArg))

    # SVGPathSegList
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "appendItem", sa.SVGPathSegArg))
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "initialize", sa.SVGPathSegArg))
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "insertItemBefore", sa.SVGPathSegArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGPathSegListArg, sa.SVGPathSegArg))
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGPathSegListArg))
    add_api(FunctionTemplate(None, sa.SVGPathSegListArg, "replaceItem", sa.SVGPathSegArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGPathSegListArg, sa.SVGPathSegArg))
    add_api(FunctionTemplate(sr.SVGPathSegRet, sa.SVGPathSegListArg, "getItem", IndexArg))
    add_api(GetItemTemplate(sr.SVGPathSegRet, sa.SVGPathSegListArg))

    # SVGPointList
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "appendItem", sa.SVGPointArg))
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "initialize", sa.SVGPointArg))
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "insertItemBefore", sa.SVGPointArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGPointListArg, sa.SVGPointArg))
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGPointListArg))
    add_api(FunctionTemplate(None, sa.SVGPointListArg, "replaceItem", sa.SVGPointArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGPointListArg, sa.SVGPointArg))
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGPointListArg, "getItem", IndexArg))
    add_api(GetItemTemplate(sr.SVGPointRet, sa.SVGPointListArg))

    # SVGSVGElement
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "animationsPaused"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "checkEnclosure", sa.SVGElementArg, sa.SVGRectArg))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "checkIntersection", sa.SVGElementArg, sa.SVGRectArg))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "deselectAll"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "forceRedraw"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "getCurrentTime"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "pauseAnimations"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "setCurrentTime", ClockArg))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "unsuspendRedrawAll"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "unpauseAnimations"))
    add_api(FunctionTemplate(None, sa.SVGSVGElementArg, "unsuspendRedraw", sa.SuspendHandleIDArg))
    add_api(
        FunctionTemplate(sr.SVGNodeListRet, sa.SVGSVGElementArg, "getEnclosureList", sa.SVGRectArg, sa.SVGElementArg))
    add_api(FunctionTemplate(sr.SVGNodeListRet, sa.SVGSVGElementArg, "getIntersectionList", sa.SVGRectArg,
                             sa.SVGElementArg))
    add_api(FunctionTemplate(sr.SVGNumberRet, sa.SVGSVGElementArg, "createSVGNumber"))
    add_api(FunctionTemplate(sr.SVGLengthRet, sa.SVGSVGElementArg, "createSVGLength"))
    add_api(FunctionTemplate(sr.SVGAngleRet, sa.SVGSVGElementArg, "createSVGAngle"))
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGSVGElementArg, "createSVGPoint"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGSVGElementArg, "createSVGMatrix"))
    add_api(FunctionTemplate(sr.SVGRectRet, sa.SVGSVGElementArg, "createSVGRect"))
    add_api(FunctionTemplate(sr.SVGTransformRet, sa.SVGSVGElementArg, "createSVGTransform"))
    add_api(FunctionTemplate(sr.SVGTransformRet, sa.SVGSVGElementArg, "createSVGTransformFromMatrix", sa.SVGMatrixArg))
    add_api(FunctionTemplate(sr.SuspendHandleIDRet, sa.SVGSVGElementArg, "suspendRedraw", ClockInMsArg))
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGSVGElementArg, "getElementById", sa.SVGElementIDArg))

    # SVGStringList
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "appendItem", StringArg))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "initialize", StringArg))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "insertItemBefore", StringArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGStringListArg, StringArg))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGStringListArg))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "replaceItem", StringArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGStringListArg, StringArg))
    add_api(FunctionTemplate(None, sa.SVGStringListArg, "getItem", IndexArg))

    # SVGTextContentElement
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "getCharNumAtPosition", sa.SVGPointArg))
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "getComputedTextLength"))
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "getNumberOfChars"))
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "getRotationOfChar", IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "getSubStringLength", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, sa.SVGTextContentElementArg, "selectSubString", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGTextContentElementArg, "getEndPositionOfChar", IntegerArg))
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGTextContentElementArg, "getStartPositionOfChar", IntegerArg))
    add_api(FunctionTemplate(sr.SVGRectRet, sa.SVGTextContentElementArg, "getExtentOfChar", IntegerArg))

    # SVGTransform
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setMatrix", sa.SVGMatrixArg))
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setRotate", FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setScale", FloatArg, FloatArg))
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setSkewX", FloatArg))
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setSkewY", FloatArg))
    add_api(FunctionTemplate(None, sa.SVGTransformArg, "setTranslate", FloatArg, FloatArg))

    # SVGTransformList
    add_api(FunctionTemplate(None, sa.SVGTransformListArg, "appendItem", sa.SVGTransformArg))
    add_api(FunctionTemplate(None, sa.SVGTransformListArg, "clear"))
    add_api(FunctionTemplate(None, sa.SVGTransformListArg, "insertItemBefore", sa.SVGTransformArg, IndexArg))
    add_api(InsertItemBeforeTemplate(sa.SVGTransformListArg, sa.SVGTransformArg))
    add_api(FunctionTemplate(None, sa.SVGTransformListArg, "removeItem", IndexArg))
    add_api(RemoveItemTemplate(sa.SVGTransformListArg))
    add_api(FunctionTemplate(None, sa.SVGTransformListArg, "replaceItem", sa.SVGTransformArg, IndexArg))
    add_api(ReplaceItemTemplate(sa.SVGTransformListArg, sa.SVGTransformArg))
    add_api(FunctionTemplate(sr.SVGTransformRet, sa.SVGTransformListArg, "consolidate"))
    add_api(
        FunctionTemplate(sr.SVGTransformRet, sa.SVGTransformListArg, "createSVGTransformFromMatrix", sa.SVGMatrixArg))
    add_api(FunctionTemplate(sr.SVGTransformRet, sa.SVGTransformListArg, "getItem", IndexArg))
    add_api(GetItemTemplate(sr.SVGTransformRet, sa.SVGTransformListArg))
    add_api(FunctionTemplate(sr.SVGTransformRet, sa.SVGTransformListArg, "initialize", sa.SVGTransformArg))

    # SVGNodeList
    add_api(FunctionTemplate(sr.SVGElementRet, sa.SVGNodeListArg, "item", IndexArg))
    add_api(ListItemTemplate(sr.SVGElementRet, sa.SVGNodeListArg))

    # SVGGraphicsElement
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGGraphicsElementArg, "getCTM"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGGraphicsElementArg, "getScreenCTM"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGGraphicsElementArg, "getTransformToElement"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGGraphicsElementArg, "getTransformToElement", sa.SVGElementArg))
    add_api(FunctionTemplate(sr.SVGRectRet, sa.SVGGraphicsElementArg, "getBBox"))

    # SVGMatrix
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "flipX"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "flipY"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "inverse"))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "multiply", sa.SVGMatrixArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "rotate", FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "rotateFromVector", FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "scale", FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "scaleNonUniform", FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "skewX", FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "skewY", FloatArg))
    add_api(FunctionTemplate(sr.SVGMatrixRet, sa.SVGMatrixArg, "translate", FloatArg, FloatArg))

    # SVGPathElement
    add_api(FunctionTemplate(None, sa.SVGPathElementArg, "getTotalLength"))
    add_api(FunctionTemplate(None, sa.SVGPathElementArg, "getPathSegAtLength", IntegerArg))
    add_api(FunctionTemplate(sr.SVGPathSegArcAbsRet, sa.SVGPathElementArg, "createSVGPathSegArcAbs",
                             FloatArg, FloatArg, FloatArg, FloatArg, FloatArg, BooleanArg, BooleanArg))
    add_api(FunctionTemplate(sr.SVGPathSegArcRelRet, sa.SVGPathElementArg, "createSVGPathSegArcRel",
                             FloatArg, FloatArg, FloatArg, FloatArg, FloatArg, BooleanArg, BooleanArg))
    add_api(FunctionTemplate(sr.SVGPathSegClosePathRet, sa.SVGPathElementArg, "createSVGPathSegClosePath"))
    add_api(
        FunctionTemplate(sr.SVGPathSegCurvetoCubicAbsRet, sa.SVGPathElementArg, "createSVGPathSegCurvetoCubicAbs",
                         FloatArg, FloatArg, FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(
        FunctionTemplate(sr.SVGPathSegCurvetoCubicRelRet, sa.SVGPathElementArg, "createSVGPathSegCurvetoCubicRel",
                         FloatArg, FloatArg, FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoCubicSmoothAbsRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoCubicSmoothAbs",
                             FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoCubicSmoothRelRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoCubicSmoothRel",
                             FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoQuadraticAbsRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoQuadraticAbs",
                             FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoQuadraticRelRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoQuadraticRel",
                             FloatArg, FloatArg, FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoQuadraticSmoothAbsRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoQuadraticSmoothAbs",
                             FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegCurvetoQuadraticSmoothRelRet, sa.SVGPathElementArg,
                             "createSVGPathSegCurvetoQuadraticSmoothRel",
                             FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegLinetoAbsRet, sa.SVGPathElementArg, "createSVGPathSegLinetoAbs",
                             FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegLinetoHorizontalAbsRet, sa.SVGPathElementArg,
                             "createSVGPathSegLinetoHorizontalAbs",
                             FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegLinetoHorizontalRelRet, sa.SVGPathElementArg,
                             "createSVGPathSegLinetoHorizontalRel",
                             FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegLinetoRelRet, sa.SVGPathElementArg, "createSVGPathSegLinetoRel",
                             FloatArg, FloatArg))
    add_api(
        FunctionTemplate(sr.SVGPathSegLinetoVerticalAbsRet, sa.SVGPathElementArg, "createSVGPathSegLinetoVerticalAbs",
                         FloatArg))
    add_api(
        FunctionTemplate(sr.SVGPathSegLinetoVerticalRelRet, sa.SVGPathElementArg, "createSVGPathSegLinetoVerticalRel",
                         FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegMovetoAbsRet, sa.SVGPathElementArg, "createSVGPathSegMovetoAbs",
                             FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPathSegMovetoRelRet, sa.SVGPathElementArg, "createSVGPathSegMovetoRel",
                             FloatArg, FloatArg))
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGPathElementArg, "getPointAtLength", IntegerArg))

    # SVGPoint
    add_api(FunctionTemplate(sr.SVGPointRet, sa.SVGPointArg, "matrixTransform", sa.SVGMatrixArg))

    # SVGCollection
    add_api(ListItemTemplate(sr.SVGElementRet, sa.SVGCollectionArg))

    ########################################
    # Document
    ########################################
    # createElementNS
    add_api(CreateElementNSTemplate(ha.DocumentArg))

    # setAttribute
    add_api(SetAttributeTemplate(sa.SVGAElementArg))
    # add_api(SetAttributeTemplate(sa.SVGAltGlyphDefElementArg))
    add_api(SetAttributeTemplate(sa.SVGAltGlyphElementArg))
    # add_api(SetAttributeTemplate(sa.SVGAltGlyphItemElementArg))
    # add_api(SetAttributeTemplate(sa.SVGAnimateColorElementArg))
    add_api(SetAttributeTemplate(sa.SVGAnimateElementArg))
    add_api(SetAttributeTemplate(sa.SVGAnimateMotionElementArg))
    add_api(SetAttributeTemplate(sa.SVGAnimateTransformElementArg))
    add_api(SetAttributeTemplate(sa.SVGCircleElementArg))
    add_api(SetAttributeTemplate(sa.SVGClipPathElementArg))
    # add_api(SetAttributeTemplate(sa.SVGColorProfileElementArg))
    add_api(SetAttributeTemplate(sa.SVGCursorElementArg))
    add_api(SetAttributeTemplate(sa.SVGDefsElementArg))
    add_api(SetAttributeTemplate(sa.SVGDescElementArg))
    add_api(SetAttributeTemplate(sa.SVGDiscardElementArg))
    add_api(SetAttributeTemplate(sa.SVGEllipseElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEBlendElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEColorMatrixElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEComponentTransferElementArg))
    add_api(SetAttributeTemplate(sa.SVGFECompositeElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEConvolveMatrixElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEDiffuseLightingElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEDisplacementMapElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEDistantLightElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEDropShadowElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEFloodElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEFuncAElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEFuncBElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEFuncGElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEFuncRElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEGaussianBlurElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEImageElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEMergeElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEMergeNodeElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEMorphologyElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEOffsetElementArg))
    add_api(SetAttributeTemplate(sa.SVGFEPointLightElementArg))
    add_api(SetAttributeTemplate(sa.SVGFESpecularLightingElementArg))
    add_api(SetAttributeTemplate(sa.SVGFESpotLightElementArg))
    add_api(SetAttributeTemplate(sa.SVGFETileElementArg))
    add_api(SetAttributeTemplate(sa.SVGFETurbulenceElementArg))
    add_api(SetAttributeTemplate(sa.SVGFilterElementArg))
    add_api(SetAttributeTemplate(sa.SVGFontElementArg))
    add_api(SetAttributeTemplate(sa.SVGFontFaceElementArg))
    add_api(SetAttributeTemplate(sa.SVGFontFaceFormatElementArg))
    add_api(SetAttributeTemplate(sa.SVGFontFaceNameElementArg))
    # add_api(SetAttributeTemplate(sa.SVGFontFaceSrcElementArg))
    add_api(SetAttributeTemplate(sa.SVGFontFaceUriElementArg))
    add_api(SetAttributeTemplate(sa.SVGForeignObjectElementArg))
    add_api(SetAttributeTemplate(sa.SVGGElementArg))
    add_api(SetAttributeTemplate(sa.SVGGlyphElementArg))
    add_api(SetAttributeTemplate(sa.SVGGlyphRefElementArg))
    add_api(SetAttributeTemplate(sa.SVGHKernElementArg))
    add_api(SetAttributeTemplate(sa.SVGHatchElementArg))
    add_api(SetAttributeTemplate(sa.SVGHatchpathElementArg))
    add_api(SetAttributeTemplate(sa.SVGImageElementArg))
    add_api(SetAttributeTemplate(sa.SVGLineElementArg))
    add_api(SetAttributeTemplate(sa.SVGLinearGradientElementArg))
    add_api(SetAttributeTemplate(sa.SVGMPathElementArg))
    add_api(SetAttributeTemplate(sa.SVGMarkerElementArg))
    add_api(SetAttributeTemplate(sa.SVGMaskElementArg))
    add_api(SetAttributeTemplate(sa.SVGMetadataElementArg))
    add_api(SetAttributeTemplate(sa.SVGMissingGlyphElementArg))
    add_api(SetAttributeTemplate(sa.SVGPathElementArg))
    add_api(SetAttributeTemplate(sa.SVGPatternElementArg))
    add_api(SetAttributeTemplate(sa.SVGPolygonElementArg))
    add_api(SetAttributeTemplate(sa.SVGPolylineElementArg))
    add_api(SetAttributeTemplate(sa.SVGRadialGradientElementArg))
    add_api(SetAttributeTemplate(sa.SVGRectElementArg))
    add_api(SetAttributeTemplate(sa.SVGSVGElementArg))
    # add_api(SetAttributeTemplate(sa.SVGScriptElementArg))
    add_api(SetAttributeTemplate(sa.SVGSetElementArg))
    add_api(SetAttributeTemplate(sa.SVGSolidcolorElementArg))
    add_api(SetAttributeTemplate(sa.SVGStopElementArg))
    # add_api(SetAttributeTemplate(sa.SVGStyleElementArg))
    add_api(SetAttributeTemplate(sa.SVGSwitchElementArg))
    add_api(SetAttributeTemplate(sa.SVGSymbolElementArg))
    add_api(SetAttributeTemplate(sa.SVGTRefElementArg))
    add_api(SetAttributeTemplate(sa.SVGTSpanElementArg))
    add_api(SetAttributeTemplate(sa.SVGTextElementArg))
    add_api(SetAttributeTemplate(sa.SVGTextPathElementArg))
    add_api(SetAttributeTemplate(sa.SVGTitleElementArg))
    add_api(SetAttributeTemplate(sa.SVGUseElementArg))
    add_api(SetAttributeTemplate(sa.SVGVKernElementArg))
    add_api(SetAttributeTemplate(sa.SVGViewElementArg))
