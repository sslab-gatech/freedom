from js import add_api
from js.property import StorePropertyTemplate, LoadPropertyTemplate
from js.arg import BooleanArg, EnumArg, FloatArg, IntegerArg, StringArg, FloatStringArg
import js.arg.svg as sa
import js.arg.html as ha
import js.ret.svg as sr
import js.ret.html as hr


def initialize_svg_properties():
    # TODO: SVGScriptElement

    # SVGElement
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "tabIndex"))
    add_api(StorePropertyTemplate(ha.TabIndexArg, sa.SVGElementArg, "tabIndex"))
    add_api(LoadPropertyTemplate(hr.CSSStyleDeclarationRet, sa.SVGElementArg, "style"))
    add_api(LoadPropertyTemplate(hr.HTMLSlotElementRet, sa.SVGElementArg, "assignedSlot"))
    add_api(LoadPropertyTemplate(hr.DOMStringMapRet, sa.SVGElementArg, "dataset"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "attributes"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "baseURI"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "childElementCount"))
    add_api(LoadPropertyTemplate(sr.SVGCollectionRet, sa.SVGElementArg, "children"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "clientHeight"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "clientLeft"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "clientTop"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "clientWidth"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "computedName"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "computedRole"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "isConnected"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "localName"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "namespaceURI"))
    add_api(LoadPropertyTemplate(hr.DocumentRet, sa.SVGElementArg, "ownerDocument"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "nodeName"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "nodeType"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "prefix"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "scrollHeight"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "scrollWidth"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "tagName"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "className"))
    add_api(StorePropertyTemplate(ha.ClassArg, sa.SVGElementArg, "className"))
    add_api(LoadPropertyTemplate(hr.DOMTokenListRet, sa.SVGElementArg, "classList"))
    add_api(LoadPropertyTemplate(hr.ShadowRootRet, sa.SVGElementArg, "shadowRoot"))
    add_api(LoadPropertyTemplate(sr.SVGHTMLStringRet, sa.SVGElementArg, "innerHTML"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGElementArg, "innerHTML"))
    add_api(StorePropertyTemplate(sa.SVGHTMLStringArg, sa.SVGElementArg, "innerHTML"))
    add_api(LoadPropertyTemplate(sr.SVGHTMLStringRet, sa.SVGElementArg, "outerHTML"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGElementArg, "outerHTML"))
    add_api(StorePropertyTemplate(sa.SVGHTMLStringArg, sa.SVGElementArg, "outerHTML"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "ongotpointercapture"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onlostpointercapture"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "firstChild"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "firstElementChild"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "lastChild"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "lastElementChild"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "nextElementSibling"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "nextSibling"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "parentElement"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "parentNode"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "previousElementSibling"))
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGElementArg, "previousSibling"))
    add_api(LoadPropertyTemplate(sr.SVGNodeListRet, sa.SVGElementArg, "childNodes"))
    add_api(LoadPropertyTemplate(sr.SVGSVGElementRet, sa.SVGElementArg, "ownerSVGElement"))
    add_api(LoadPropertyTemplate(sr.SVGSVGElementRet, sa.SVGElementArg, "viewportElement"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "scrollLeft"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGElementArg, "scrollLeft"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "scrollTop"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGElementArg, "scrollTop"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "nodeValue"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGElementArg, "nodeValue"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "slot"))
    add_api(StorePropertyTemplate(ha.SlotArg, sa.SVGElementArg, "slot"))
    add_api(LoadPropertyTemplate(None, sa.SVGElementArg, "textContent"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGElementArg, "textContent"))

    # SVGStyleElement
    add_api(LoadPropertyTemplate(None, sa.SVGStyleElementArg, "type"))
    add_api(StorePropertyTemplate(ha.CSSTypeArg, sa.SVGStyleElementArg, "type"))
    add_api(LoadPropertyTemplate(None, sa.SVGStyleElementArg, "media"))
    add_api(StorePropertyTemplate(ha.MediaQueryArg, sa.SVGStyleElementArg, "media"))
    add_api(LoadPropertyTemplate(None, sa.SVGStyleElementArg, "title"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGStyleElementArg, "title"))
    add_api(LoadPropertyTemplate(None, sa.SVGStyleElementArg, "disabled"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGStyleElementArg, "disabled"))

    # SVGViewSpec
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGViewSpecArg, "viewTarget"))
    add_api(LoadPropertyTemplate(sr.SVGTransformListRet, sa.SVGViewSpecArg, "transform"))
    add_api(LoadPropertyTemplate(None, sa.SVGViewSpecArg, "zoomAndPan"))
    add_api(StorePropertyTemplate(IntegerArg, sa.SVGViewSpecArg, "zoomAndPan"))
    add_api(LoadPropertyTemplate(None, sa.SVGViewSpecArg, "preserveAspectRatioString"))
    add_api(LoadPropertyTemplate(None, sa.SVGViewSpecArg, "transformString"))
    add_api(LoadPropertyTemplate(None, sa.SVGViewSpecArg, "viewBoxString"))
    add_api(LoadPropertyTemplate(None, sa.SVGViewSpecArg, "viewTargetString"))

    # SVGAnimatedAngle
    add_api(LoadPropertyTemplate(sr.SVGAngleRet, sa.SVGAnimatedAngleArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGAngleRet, sa.SVGAnimatedAngleArg, "baseVal"))

    # SVGMarkerElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedAngleRet, sa.SVGMarkerElementArg, "orientAngle"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGMarkerElementArg, "markerUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGMarkerElementArg, "orientType"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMarkerElementArg, "markerHeight"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMarkerElementArg, "markerWidth"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMarkerElementArg, "refX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMarkerElementArg, "refY"))

    # SVGClipPathElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGClipPathElementArg, "clipPathUnits"))

    # SVGComponentTransferFunctionElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGComponentTransferFunctionElementArg, "type"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGComponentTransferFunctionElementArg, "amplitude"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGComponentTransferFunctionElementArg, "exponent"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGComponentTransferFunctionElementArg, "intercept"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGComponentTransferFunctionElementArg, "offset"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGComponentTransferFunctionElementArg, "slope"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberListRet, sa.SVGComponentTransferFunctionElementArg,
                                 "tableValues"))

    # SVGFEBlendElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEBlendElementArg, "mode"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEBlendElementArg, "in1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEBlendElementArg, "in2"))

    # SVGFEColorMatrixElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEColorMatrixElementArg, "type"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberListRet, sa.SVGFEColorMatrixElementArg, "values"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberListRet, sa.SVGFEConvolveMatrixElementArg, "kernelMatrix"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEColorMatrixElementArg, "in1"))

    # SVGFECompositeElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFECompositeElementArg, "operator"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFECompositeElementArg, "k1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFECompositeElementArg, "k2"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFECompositeElementArg, "k3"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFECompositeElementArg, "k4"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFECompositeElementArg, "in1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFECompositeElementArg, "in2"))

    # SVGFEConvolveMatrixElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEConvolveMatrixElementArg, "edgeMode"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFEConvolveMatrixElementArg, "orderX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFEConvolveMatrixElementArg, "orderY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFEConvolveMatrixElementArg, "targetX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFEConvolveMatrixElementArg, "targetY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEConvolveMatrixElementArg, "bias"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEConvolveMatrixElementArg, "divisor"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEConvolveMatrixElementArg, "kernelUnitLengthX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEConvolveMatrixElementArg, "kernelUnitLengthY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEConvolveMatrixElementArg, "in1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedBooleanRet, sa.SVGFEConvolveMatrixElementArg, "preserveAlpha"))

    # SVGFEDisplacementMapElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEDisplacementMapElementArg, "xChannelSelector"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEDisplacementMapElementArg, "yChannelSelector"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDisplacementMapElementArg, "scale"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEDisplacementMapElementArg, "in1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEDisplacementMapElementArg, "in2"))

    # SVGFEMorphologyElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFEMorphologyElementArg, "operator"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEMorphologyElementArg, "radiusX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEMorphologyElementArg, "radiusY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEMorphologyElementArg, "in1"))

    # SVGFETurbulenceElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFETurbulenceElementArg, "stitchTiles"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFETurbulenceElementArg, "type"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFETurbulenceElementArg, "numOctaves"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFETurbulenceElementArg, "baseFrequencyX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFETurbulenceElementArg, "baseFrequencyY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFETurbulenceElementArg, "seed"))

    # SVGFilterElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFilterElementArg, "filterUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGFilterElementArg, "primitiveUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFilterElementArg, "filterResX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedIntegerRet, sa.SVGFilterElementArg, "filterResY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterElementArg, "y"))

    # SVGGradientElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGGradientElementArg, "gradientUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGGradientElementArg, "spreadMethod"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedTransformListRet, sa.SVGGradientElementArg, "gradientTransform"))

    # SVGMaskElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGMaskElementArg, "maskContentUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGMaskElementArg, "maskUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMaskElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMaskElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMaskElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGMaskElementArg, "y"))

    # SVGPatternElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGPatternElementArg, "patternContentUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGPatternElementArg, "patternUnits"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGPatternElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGPatternElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGPatternElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGPatternElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedTransformListRet, sa.SVGPatternElementArg, "patternTransform"))

    # SVGTextContentElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGTextContentElementArg, "lengthAdjust"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGTextContentElementArg, "textLength"))

    # SVGTextPathElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGTextPathElementArg, "method"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedEnumerationRet, sa.SVGTextPathElementArg, "spacing"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGTextPathElementArg, "startOffset"))

    # SVGCircleElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGCircleElementArg, "cx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGCircleElementArg, "cy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGCircleElementArg, "r"))

    # SVGCursorElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGCursorElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGCursorElementArg, "y"))

    # SVGEllipseElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGEllipseElementArg, "cx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGEllipseElementArg, "cy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGEllipseElementArg, "rx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGEllipseElementArg, "ry"))

    # SVGFilterPrimitiveStandardAttributes
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterPrimitiveStandardAttributesArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterPrimitiveStandardAttributesArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterPrimitiveStandardAttributesArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGFilterPrimitiveStandardAttributesArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFilterPrimitiveStandardAttributesArg, "result"))

    # SVGForeignObjectElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGForeignObjectElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGForeignObjectElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGForeignObjectElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGForeignObjectElementArg, "y"))

    # SVGImageElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGImageElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGImageElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGImageElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGImageElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedPreserveAspectRatioRet, sa.SVGImageElementArg, "preserveAspectRatio"))

    # SVGLineElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLineElementArg, "x1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLineElementArg, "x2"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLineElementArg, "y1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLineElementArg, "y2"))

    # SVGLinearGradientElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLinearGradientElementArg, "x1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLinearGradientElementArg, "x2"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLinearGradientElementArg, "y1"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGLinearGradientElementArg, "y2"))

    # SVGRadialGradientElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "cx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "cy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "fr"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "fx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "fy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRadialGradientElementArg, "r"))

    # SVGRectElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "rx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "ry"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGRectElementArg, "y"))

    # SVGSVGElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGSVGElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGSVGElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGSVGElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGSVGElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGPointRet, sa.SVGSVGElementArg, "currentTranslate"))
    add_api(LoadPropertyTemplate(sr.SVGRectRet, sa.SVGSVGElementArg, "viewport"))
    add_api(LoadPropertyTemplate(None, sa.SVGSVGElementArg, "useCurrentView"))
    add_api(LoadPropertyTemplate(sr.SVGViewSpecRet, sa.SVGSVGElementArg, "currentView"))
    add_api(LoadPropertyTemplate(None, sa.SVGSVGElementArg, "currentScale"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGSVGElementArg, "currentScale"))

    # SVGUseElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGUseElementArg, "height"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGUseElementArg, "width"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGUseElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthRet, sa.SVGUseElementArg, "y"))

    # SVGTextPositioningElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthListRet, sa.SVGTextPositioningElementArg, "dx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthListRet, sa.SVGTextPositioningElementArg, "dy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthListRet, sa.SVGTextPositioningElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedLengthListRet, sa.SVGTextPositioningElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberListRet, sa.SVGTextPositioningElementArg, "rotate"))

    # SVGFEDiffuseLightingElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDiffuseLightingElementArg, "diffuseConstant"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDiffuseLightingElementArg, "kernelUnitLengthX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDiffuseLightingElementArg, "kernelUnitLengthY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDiffuseLightingElementArg, "surfaceScale"))

    # SVGFEDistantLightElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDistantLightElementArg, "azimuth"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDistantLightElementArg, "elevation"))

    # SVGFEDropShadowElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDropShadowElementArg, "dx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDropShadowElementArg, "dy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDropShadowElementArg, "stdDeviationX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEDropShadowElementArg, "stdDeviationY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEDropShadowElementArg, "in1"))

    # SVGFEGaussianBlurElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEGaussianBlurElementArg, "stdDeviationX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEGaussianBlurElementArg, "stdDeviationY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEGaussianBlurElementArg, "in1"))

    # SVGFEOffsetElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEOffsetElementArg, "dx"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEOffsetElementArg, "dy"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEOffsetElementArg, "in1"))

    # SVGFEPointLightElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEPointLightElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEPointLightElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFEPointLightElementArg, "z"))

    # SVGFESpecularLightingElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpecularLightingElementArg, "kernelUnitLengthX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpecularLightingElementArg, "kernelUnitLengthY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpecularLightingElementArg, "specularConstant"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpecularLightingElementArg, "specularExponent"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpecularLightingElementArg, "surfaceScale"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFESpecularLightingElementArg, "in1"))

    # SVGFESpotLightElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "limitingConeAngle"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "pointsAtX"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "pointsAtY"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "pointsAtZ"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "specularExponent"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "x"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "y"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGFESpotLightElementArg, "z"))

    # SVGPathElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGPathElementArg, "pathLength"))
    add_api(LoadPropertyTemplate(sr.SVGPathSegListRet, sa.SVGPathElementArg, "animatedNormalizedPathSegList"))
    add_api(LoadPropertyTemplate(sr.SVGPathSegListRet, sa.SVGPathElementArg, "animatedPathSegList"))
    add_api(LoadPropertyTemplate(sr.SVGPathSegListRet, sa.SVGPathElementArg, "pathSegList"))

    # SVGStopElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedNumberRet, sa.SVGStopElementArg, "offset"))

    # SVGFEImageElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedPreserveAspectRatioRet, sa.SVGFEImageElementArg, "preserveAspectRatio"))

    # SVGFitToViewBox
    add_api(LoadPropertyTemplate(sr.SVGAnimatedPreserveAspectRatioRet, sa.SVGFitToViewBoxArg, "preserveAspectRatio"))
    add_api(LoadPropertyTemplate(sr.SVGAnimatedRectRet, sa.SVGFitToViewBoxArg, "viewBox"))

    # SVGAElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGAElementArg, "target"))

    # SVGFEComponentTransferElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEComponentTransferElementArg, "in1"))

    # SVGFEDiffuseLightingElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEDiffuseLightingElementArg, "in1"))

    # SVGFEMergeNodeElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFEMergeNodeElementArg, "in1"))

    # SVGFETileElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedStringRet, sa.SVGFETileElementArg, "in1"))

    # SVGAnimationElement
    add_api(LoadPropertyTemplate(sr.SVGElementRet, sa.SVGAnimationElementArg, "targetElement"))

    # SVGAnimatedLength
    add_api(LoadPropertyTemplate(sr.SVGLengthRet, sa.SVGAnimatedLengthArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGLengthRet, sa.SVGAnimatedLengthArg, "baseVal"))

    # SVGAnimatedLengthList
    add_api(LoadPropertyTemplate(sr.SVGLengthListRet, sa.SVGAnimatedLengthListArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGLengthListRet, sa.SVGAnimatedLengthListArg, "baseVal"))

    # SVGTransform
    add_api(LoadPropertyTemplate(sr.SVGMatrixRet, sa.SVGTransformArg, "matrix"))
    add_api(LoadPropertyTemplate(None, sa.SVGTransformArg, "angle"))
    add_api(LoadPropertyTemplate(None, sa.SVGTransformArg, "type"))

    # SVGAnimatedNumberList
    add_api(LoadPropertyTemplate(sr.SVGNumberListRet, sa.SVGAnimatedNumberListArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGNumberListRet, sa.SVGAnimatedNumberListArg, "baseVal"))

    # SVGAnimatedNumber
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedNumberArg, "animVal"))
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedNumberArg, "baseVal"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGAnimatedNumberArg, "baseVal"))

    # SVGPolygonElement
    add_api(LoadPropertyTemplate(sr.SVGPointListRet, sa.SVGPolygonElementArg, "animatedPoints"))
    add_api(LoadPropertyTemplate(sr.SVGPointListRet, sa.SVGPolygonElementArg, "points"))

    # SVGPolylineElement
    add_api(LoadPropertyTemplate(sr.SVGPointListRet, sa.SVGPolylineElementArg, "animatedPoints"))
    add_api(LoadPropertyTemplate(sr.SVGPointListRet, sa.SVGPolylineElementArg, "points"))

    # SVGAnimatedPreserveAspectRatio
    add_api(LoadPropertyTemplate(sr.SVGPreserveAspectRatioRet, sa.SVGAnimatedPreserveAspectRatioArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGPreserveAspectRatioRet, sa.SVGAnimatedPreserveAspectRatioArg, "baseVal"))

    # SVGAnimatedRect
    add_api(LoadPropertyTemplate(sr.SVGRectRet, sa.SVGAnimatedRectArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGRectRet, sa.SVGAnimatedRectArg, "baseVal"))

    # SVGGraphicsElement
    add_api(LoadPropertyTemplate(sr.SVGAnimatedTransformListRet, sa.SVGGraphicsElementArg, "transform"))
    add_api(LoadPropertyTemplate(sr.SVGSVGElementRet, sa.SVGGraphicsElementArg, "farthestViewportElement"))
    add_api(LoadPropertyTemplate(sr.SVGSVGElementRet, sa.SVGGraphicsElementArg, "nearestViewportElement"))

    # SVGViewElement
    add_api(LoadPropertyTemplate(sr.SVGStringListRet, sa.SVGViewElementArg, "viewTarget"))

    # SVGAnimatedTransformList
    add_api(LoadPropertyTemplate(sr.SVGTransformListRet, sa.SVGAnimatedTransformListArg, "animVal"))
    add_api(LoadPropertyTemplate(sr.SVGTransformListRet, sa.SVGAnimatedTransformListArg, "baseVal"))

    # SVGAnimatedBoolean
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedBooleanArg, "baseVal"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGAnimatedBooleanArg, "baseVal"))
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedBooleanArg, "animVal"))

    # SVGAnimatedEnumeration
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedEnumerationArg, "animVal"))
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedEnumerationArg, "baseVal"))
    add_api(StorePropertyTemplate(EnumArg, sa.SVGAnimatedEnumerationArg, "baseVal"))

    # SVGAngle
    add_api(LoadPropertyTemplate(None, sa.SVGAngleArg, "unitType"))
    add_api(LoadPropertyTemplate(None, sa.SVGAngleArg, "valueAsString"))
    add_api(StorePropertyTemplate(FloatStringArg, sa.SVGAngleArg, "valueAsString"))
    add_api(LoadPropertyTemplate(None, sa.SVGAngleArg, "value"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGAngleArg, "value"))
    add_api(LoadPropertyTemplate(None, sa.SVGAngleArg, "valueInSpecifiedUnits"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGAngleArg, "valueInSpecifiedUnits"))

    # SVGPathSeg*
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "largeArcFlag"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGPathSegArcAbsArg, "largeArcFlag"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "sweepFlag"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGPathSegArcAbsArg, "sweepFlag"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "largeArcFlag"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGPathSegArcRelArg, "largeArcFlag"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "sweepFlag"))
    add_api(StorePropertyTemplate(BooleanArg, sa.SVGPathSegArcRelArg, "sweepFlag"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "angle"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcAbsArg, "angle"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "r1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcAbsArg, "r1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "r2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcAbsArg, "r2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "angle"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcRelArg, "angle"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "r1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcRelArg, "r1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "r2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcRelArg, "r2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegArcRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegArcRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "x1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "x1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "x2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "x2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "y1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "y1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicAbsArg, "y2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicAbsArg, "y2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "x1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "x1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "x2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "x2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "y1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "y1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicRelArg, "y2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicRelArg, "y2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "x2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "x2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "y2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothAbsArg, "y2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothRelArg, "x2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothRelArg, "x2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoCubicSmoothRelArg, "y2"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoCubicSmoothRelArg, "y2"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticAbsArg, "x1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticAbsArg, "x1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticAbsArg, "y1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticAbsArg, "y1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticRelArg, "x1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticRelArg, "x1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticRelArg, "y1"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticRelArg, "y1"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticSmoothAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticSmoothAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticSmoothAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticSmoothAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticSmoothRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticSmoothRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegCurvetoQuadraticSmoothRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegCurvetoQuadraticSmoothRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoHorizontalAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoHorizontalRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoRelArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoVerticalAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoVerticalAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegLinetoVerticalRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegLinetoVerticalRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegMovetoAbsArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegMovetoAbsArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegMovetoAbsArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegMovetoAbsArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegMovetoRelArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegMovetoRelArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPathSegMovetoRelArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPathSegMovetoRelArg, "y"))

    # SVGGlyphRefElement
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "dx"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGGlyphRefElementArg, "dx"))
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "dy"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGGlyphRefElementArg, "dy"))
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGGlyphRefElementArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGGlyphRefElementArg, "y"))
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "format"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGGlyphRefElementArg, "format"))
    add_api(LoadPropertyTemplate(None, sa.SVGGlyphRefElementArg, "glyphRef"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGGlyphRefElementArg, "glyphRef"))

    # SVGLength
    add_api(LoadPropertyTemplate(None, sa.SVGLengthArg, "unitType"))
    add_api(LoadPropertyTemplate(None, sa.SVGLengthArg, "value"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGLengthArg, "value"))
    add_api(LoadPropertyTemplate(None, sa.SVGLengthArg, "valueAsString"))
    add_api(StorePropertyTemplate(FloatStringArg, sa.SVGLengthArg, "valueAsString"))
    add_api(LoadPropertyTemplate(None, sa.SVGLengthArg, "valueInSpecifiedUnits"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGLengthArg, "valueInSpecifiedUnits"))

    # SVGMatrix
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "a"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "a"))
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "b"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "b"))
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "c"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "c"))
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "d"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "d"))
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "e"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "e"))
    add_api(LoadPropertyTemplate(None, sa.SVGMatrixArg, "f"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGMatrixArg, "f"))

    # SVGPoint
    add_api(LoadPropertyTemplate(None, sa.SVGPointArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPointArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGPointArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGPointArg, "y"))

    # SVGRect
    add_api(LoadPropertyTemplate(None, sa.SVGRectArg, "height"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGRectArg, "height"))
    add_api(LoadPropertyTemplate(None, sa.SVGRectArg, "width"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGRectArg, "width"))
    add_api(LoadPropertyTemplate(None, sa.SVGRectArg, "x"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGRectArg, "x"))
    add_api(LoadPropertyTemplate(None, sa.SVGRectArg, "y"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGRectArg, "y"))

    # SVGAnimatedInteger
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedIntegerArg, "animVal"))
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedIntegerArg, "baseVal"))
    add_api(StorePropertyTemplate(IntegerArg, sa.SVGAnimatedIntegerArg, "baseVal"))

    # SVGPreserveAspectRatio
    add_api(LoadPropertyTemplate(None, sa.SVGPreserveAspectRatioArg, "align"))
    add_api(StorePropertyTemplate(IntegerArg, sa.SVGPreserveAspectRatioArg, "align"))
    add_api(LoadPropertyTemplate(None, sa.SVGPreserveAspectRatioArg, "meetOrSlice"))
    add_api(StorePropertyTemplate(IntegerArg, sa.SVGPreserveAspectRatioArg, "meetOrSlice"))

    # SVGAnimatedString
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedStringArg, "animVal"))
    add_api(LoadPropertyTemplate(None, sa.SVGAnimatedStringArg, "baseVal"))
    add_api(StorePropertyTemplate(StringArg, sa.SVGAnimatedStringArg, "baseVal"))

    # SVGNumber
    add_api(LoadPropertyTemplate(None, sa.SVGNumberArg, "value"))
    add_api(StorePropertyTemplate(FloatArg, sa.SVGNumberArg, "value"))

    # Event
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGAnimationElementArg, "onbegin"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGAnimationElementArg, "onend"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGAnimationElementArg, "onrepeat"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGSVGElementArg, "onerror"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGSVGElementArg, "onresize"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGSVGElementArg, "onscroll"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onsearch"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onwheel"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onselectstart"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onactivate"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onfocusin"))
    add_api(StorePropertyTemplate(ha.EventHandlerArg, sa.SVGElementArg, "onfocusout"))