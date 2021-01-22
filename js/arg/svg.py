import docs
from js.arg import ObjectArg, Arg, StringArg
from css.selector import create_css_basic_selector
from utils import stringify
from utils.random import Random


#############################################
# SVG Elements
#############################################
class SVGCollectionArg(ObjectArg):
    name = "SVGCollection"


class SVGElementArg(ObjectArg):
    name = "SVGElement"


class SVGGraphicsElementArg(ObjectArg):
    name = "SVGGraphicsElement"


class SVGTextContentElementArg(ObjectArg):
    name = "SVGTextContentElement"


class SVGTextPositioningElementArg(ObjectArg):
    name = "SVGTextPositioningElement"


class SVGGradientElementArg(ObjectArg):
    name = "SVGGradientElement"


class SVGGeometryElementArg(ObjectArg):
    name = "SVGGeometryElement"


class SVGAnimationElementArg(ObjectArg):
    name = "SVGAnimationElement"


class SVGComponentTransferFunctionElementArg(ObjectArg):
    name = "SVGComponentTransferFunctionElement"


class SVGFEPointLightElementArg(ObjectArg):
    name = "SVGFEPointLightElement"


class SVGAElementArg(ObjectArg):
    name = "SVGAElement"


class SVGTextPathElementArg(ObjectArg):
    name = "SVGTextPathElement"


class SVGLinearGradientElementArg(ObjectArg):
    name = "SVGLinearGradientElement"


class SVGTSpanElementArg(ObjectArg):
    name = "SVGTSpanElement"


# deprecated
class SVGFontFaceUriElementArg(ObjectArg):
    name = "SVGFontFaceUriElement"


class SVGTRefElementArg(ObjectArg):
    name = "SVGTRefElement"


class SVGFETileElementArg(ObjectArg):
    name = "SVGFETileElement"


class SVGMPathElementArg(ObjectArg):
    name = "SVGMPathElement"


class SVGFEDisplacementMapElementArg(ObjectArg):
    name = "SVGFEDisplacementMapElement"


class SVGFontFaceFormatElementArg(ObjectArg):
    name = "SVGFontFaceFormatElement"


class SVGStyleElementArg(ObjectArg):
    name = "SVGStyleElement"


class SVGFEConvolveMatrixElementArg(ObjectArg):
    name = "SVGFEConvolveMatrixElement"


class SVGHatchElementArg(ObjectArg):
    name = "SVGHatchElement"


class SVGFEDiffuseLightingElementArg(ObjectArg):
    name = "SVGFEDiffuseLightingElement"


class SVGDiscardElementArg(ObjectArg):
    name = "SVGDiscardElement"


class SVGHatchpathElementArg(ObjectArg):
    name = "SVGHatchpathElement"


# deprecated
class SVGGlyphElementArg(ObjectArg):
    name = "SVGGlyphElement"


# deprecated
class SVGMissingGlyphElementArg(ObjectArg):
    name = "SVGMissingGlyphElement"


# deprecated
class SVGAltGlyphItemElementArg(ObjectArg):
    name = "SVGAltGlyphItemElement"


class SVGPolylineElementArg(ObjectArg):
    name = "SVGPolylineElement"


class SVGViewElementArg(ObjectArg):
    name = "SVGViewElement"


class SVGAnimateElementArg(ObjectArg):
    name = "SVGAnimateElement"


class SVGFESpecularLightingElementArg(ObjectArg):
    name = "SVGFESpecularLightingElement"


class SVGAltGlyphElementArg(ObjectArg):
    name = "SVGAltGlyphElement"


class SVGTextElementArg(ObjectArg):
    name = "SVGTextElement"


class SVGFEMorphologyElementArg(ObjectArg):
    name = "SVGFEMorphologyElement"


class SVGImageElementArg(ObjectArg):
    name = "SVGImageElement"


class SVGAnimateTransformElementArg(ObjectArg):
    name = "SVGAnimateTransformElement"


class SVGEllipseElementArg(ObjectArg):
    name = "SVGEllipseElement"


class SVGFontFaceSrcElementArg(ObjectArg):
    name = "SVGFontFaceSrcElement"


class SVGDescElementArg(ObjectArg):
    name = "SVGDescElement"


class SVGDefsElementArg(ObjectArg):
    name = "SVGDefsElement"


# deprecated
class SVGFontFaceElementArg(ObjectArg):
    name = "SVGFontFaceElement"


class SVGGElementArg(ObjectArg):
    name = "SVGGElement"


# deprecated
class SVGAltGlyphDefElementArg(ObjectArg):
    name = "SVGAltGlyphDefElement"


class SVGSwitchElementArg(ObjectArg):
    name = "SVGSwitchElement"


class SVGGlyphRefElementArg(ObjectArg):
    name = "SVGGlyphRefElement"


class SVGCircleElementArg(ObjectArg):
    name = "SVGCircleElement"


class SVGSymbolElementArg(ObjectArg):
    name = "SVGSymbolElement"


# deprecated
class SVGVKernElementArg(ObjectArg):
    name = "SVGVKernElement"


class SVGFilterElementArg(ObjectArg):
    name = "SVGFilterElement"


class SVGFEColorMatrixElementArg(ObjectArg):
    name = "SVGFEColorMatrixElement"


class SVGHKernElementArg(ObjectArg):
    name = "SVGHKernElement"


class SVGRadialGradientElementArg(ObjectArg):
    name = "SVGRadialGradientElement"


class SVGFETurbulenceElementArg(ObjectArg):
    name = "SVGFETurbulenceElement"


class SVGPolygonElementArg(ObjectArg):
    name = "SVGPolygonElement"


class SVGScriptElementArg(ObjectArg):
    name = "SVGScriptElement"


class SVGFEFuncRElementArg(ObjectArg):
    name = "SVGFEFuncRElement"


class SVGFEFloodElementArg(ObjectArg):
    name = "SVGFEFloodElement"


class SVGSolidcolorElementArg(ObjectArg):
    name = "SVGSolidcolorElement"


class SVGTitleElementArg(ObjectArg):
    name = "SVGTitleElement"


class SVGPatternElementArg(ObjectArg):
    name = "SVGPatternElement"


class SVGFEMergeNodeElementArg(ObjectArg):
    name = "SVGFEMergeNodeElement"


class SVGUseElementArg(ObjectArg):
    name = "SVGUseElement"


class SVGFEMergeElementArg(ObjectArg):
    name = "SVGFEMergeElement"


class SVGSetElementArg(ObjectArg):
    name = "SVGSetElement"


class SVGSVGElementArg(ObjectArg):
    name = "SVGSVGElement"


class SVGCursorElementArg(ObjectArg):
    name = "SVGCursorElement"


class SVGFEDistantLightElementArg(ObjectArg):
    name = "SVGFEDistantLightElement"


class SVGFEFuncGElementArg(ObjectArg):
    name = "SVGFEFuncGElement"


class SVGStopElementArg(ObjectArg):
    name = "SVGStopElement"


class SVGFESpotLightElementArg(ObjectArg):
    name = "SVGFESpotLightElement"


class SVGMarkerElementArg(ObjectArg):
    name = "SVGMarkerElement"


class SVGFECompositeElementArg(ObjectArg):
    name = "SVGFECompositeElement"


class SVGFEFuncBElementArg(ObjectArg):
    name = "SVGFEFuncBElement"


class SVGMaskElementArg(ObjectArg):
    name = "SVGMaskElement"


class SVGRectElementArg(ObjectArg):
    name = "SVGRectElement"


class SVGMetadataElementArg(ObjectArg):
    name = "SVGMetadataElement"


# deprecated
class SVGFontFaceNameElementArg(ObjectArg):
    name = "SVGFontFaceNameElement"


# deprecated
class SVGAnimateColorElementArg(ObjectArg):
    name = "SVGAnimateColorElement"


class SVGFEGaussianBlurElementArg(ObjectArg):
    name = "SVGFEGaussianBlurElement"


class SVGFEImageElementArg(ObjectArg):
    name = "SVGFEImageElement"


class SVGFEFuncAElementArg(ObjectArg):
    name = "SVGFEFuncAElement"


class SVGForeignObjectElementArg(ObjectArg):
    name = "SVGForeignObjectElement"


# deprecated
class SVGFontElementArg(ObjectArg):
    name = "SVGFontElement"


class SVGClipPathElementArg(ObjectArg):
    name = "SVGClipPathElement"


class SVGLineElementArg(ObjectArg):
    name = "SVGLineElement"


class SVGColorProfileElementArg(ObjectArg):
    name = "SVGColorProfileElement"


class SVGAnimateMotionElementArg(ObjectArg):
    name = "SVGAnimateMotionElement"


class SVGFEComponentTransferElementArg(ObjectArg):
    name = "SVGFEComponentTransferElement"


class SVGFEBlendElementArg(ObjectArg):
    name = "SVGFEBlendElement"


class SVGFEOffsetElementArg(ObjectArg):
    name = "SVGFEOffsetElement"


class SVGFEDropShadowElementArg(ObjectArg):
    name = "SVGFEDropShadowElement"


class SVGPathElementArg(ObjectArg):
    name = "SVGPathElement"


#############################################
# SVG interfaces 
#############################################
class SVGFilterPrimitiveStandardAttributesArg(ObjectArg):
    name = "SVGFilterPrimitiveStandardAttributes"


class SVGFitToViewBoxArg(ObjectArg):
    name = "SVGFitToViewBox"


class SVGViewSpecArg(ObjectArg):
    name = "SVGViewSpec"


#############################################
# SVG objects
#############################################
class SVGAnimatedStringArg(ObjectArg):
    name = "SVGAnimatedString"


class SVGAnimatedLengthListArg(ObjectArg):
    name = "SVGAnimatedLengthList"


class SuspendHandleIDArg(ObjectArg):
    name = "SuspendHandleID"


class SVGAnimatedAngleArg(ObjectArg):
    name = "SVGAnimatedAngle"


class SVGPathSegCurvetoCubicSmoothAbsArg(ObjectArg):
    name = "SVGPathSegCurvetoCubicSmoothAbs"


class SVGPathSegMovetoAbsArg(ObjectArg):
    name = "SVGPathSegMovetoAbs"


class SVGLengthListArg(ObjectArg):
    name = "SVGLengthList"


class SVGAnimatedRectArg(ObjectArg):
    name = "SVGAnimatedRect"


class SVGPathSegArg(ObjectArg):
    name = "SVGPathSeg"


class SVGAngleArg(ObjectArg):
    name = "SVGAngle"


class SVGPathSegArcRelArg(ObjectArg):
    name = "SVGPathSegArcRel"


class SVGPathSegCurvetoQuadraticAbsArg(ObjectArg):
    name = "SVGPathSegCurvetoQuadraticAbs"


class SVGPathSegLinetoAbsArg(ObjectArg):
    name = "SVGPathSegLinetoAbs"


class SVGPathSegLinetoVerticalRelArg(ObjectArg):
    name = "SVGPathSegLinetoVerticalRel"


class SVGPathSegCurvetoQuadraticSmoothRelArg(ObjectArg):
    name = "SVGPathSegCurvetoQuadraticSmoothRel"


class SVGPathSegCurvetoQuadraticSmoothAbsArg(ObjectArg):
    name = "SVGPathSegCurvetoQuadraticSmoothAbs"


class SVGPathSegListArg(ObjectArg):
    name = "SVGPathSegList"


class SVGAnimatedLengthArg(ObjectArg):
    name = "SVGAnimatedLength"


class SVGMatrixArg(ObjectArg):
    name = "SVGMatrix"


class SVGLengthArg(ObjectArg):
    name = "SVGLength"


class SVGNumberListArg(ObjectArg):
    name = "SVGNumberList"


class SVGPreserveAspectRatioArg(ObjectArg):
    name = "SVGPreserveAspectRatio"


class SVGURIReferenceArg(ObjectArg):
    name = "SVGURIReference"


class SVGPathSegLinetoVerticalAbsArg(ObjectArg):
    name = "SVGPathSegLinetoVerticalAbs"


class SVGTransformArg(ObjectArg):
    name = "SVGTransform"


class SVGAnimatedTransformListArg(ObjectArg):
    name = "SVGAnimatedTransformList"


class SVGPathSegLinetoRelArg(ObjectArg):
    name = "SVGPathSegLinetoRel"


class SVGPathSegLinetoHorizontalRelArg(ObjectArg):
    name = "SVGPathSegLinetoHorizontalRel"


class SVGNodeListArg(ObjectArg):
    name = "SVGNodeList"


class SVGPathSegMovetoRelArg(ObjectArg):
    name = "SVGPathSegMovetoRel"


class SVGPointListArg(ObjectArg):
    name = "SVGPointList"


class SVGTransformListArg(ObjectArg):
    name = "SVGTransformList"


class SVGAnimatedEnumerationArg(ObjectArg):
    name = "SVGAnimatedEnumeration"


class SVGAnimatedPreserveAspectRatioArg(ObjectArg):
    name = "SVGAnimatedPreserveAspectRatio"


class SVGPointArg(ObjectArg):
    name = "SVGPoint"


class SVGStringListArg(ObjectArg):
    name = "SVGStringList"


class SVGAnimatedNumberArg(ObjectArg):
    name = "SVGAnimatedNumber"


class SVGPathSegClosePathArg(ObjectArg):
    name = "SVGPathSegClosePath"


class SVGPathSegCurvetoQuadraticRelArg(ObjectArg):
    name = "SVGPathSegCurvetoQuadraticRel"


class SVGAnimatedIntegerArg(ObjectArg):
    name = "SVGAnimatedInteger"


class SVGNumberArg(ObjectArg):
    name = "SVGNumber"


class SVGPathSegLinetoHorizontalAbsArg(ObjectArg):
    name = "SVGPathSegLinetoHorizontalAbs"


class SVGAnimatedNumberListArg(ObjectArg):
    name = "SVGAnimatedNumberList"


class SVGPathSegArcAbsArg(ObjectArg):
    name = "SVGPathSegArcAbs"


class SVGPathSegCurvetoCubicAbsArg(ObjectArg):
    name = "SVGPathSegCurvetoCubicAbs"


class SVGPathSegCurvetoCubicSmoothRelArg(ObjectArg):
    name = "SVGPathSegCurvetoCubicSmoothRel"


class SVGPathSegCurvetoCubicRelArg(ObjectArg):
    name = "SVGPathSegCurvetoCubicRel"


class SVGRectArg(ObjectArg):
    name = "SVGRect"


class SVGHTMLStringArg(ObjectArg):
    name = "SVGHTMLString"


class SVGAnimatedBooleanArg(ObjectArg):
    name = "SVGAnimatedBoolean"


class SVGQuerySelectorArg(Arg):
    def __init__(self):
        super().__init__()
        self.selector = None

    def is_object(self):
        return False

    def generate(self, context):
        self.selector = create_css_basic_selector(docs.svg_elements)
        self.selector.generate(context.global_context)

    def mutate(self, context) -> bool:
        if Random.bool():
            # 1. mutate selector value
            return self.selector.mutate(context.global_context)
        else:
            # 2. change to another selector
            self.generate(context)
            return True

    def merge_fix(self, merge_map):
        self.selector.merge_fix(merge_map)

    def __str__(self):
        return stringify(self.selector)


class SVGTagArg(StringArg):
    def generate(self, context):
        elems = [elem for elem in context.global_context.in_tree_set if docs.is_svg_element(elem)]
        if len(elems) == 0:
            self.value = "svg"
        else:
            self.value = docs.tag_from_element(Random.choice(elems))


class SVGElementIDArg(Arg):
    def __init__(self):
        super().__init__()
        self.elem = None

    def is_object(self):
        return False

    def generate(self, context):
        self.elem = context.global_context.get_object(docs.svg_elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is not None:
            s = self.elem.id
        else:
            s = "foo"
        return stringify(s)
