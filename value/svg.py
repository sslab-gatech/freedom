import docs
from value import StaticValue, DynamicValue, ConstValueWrapper
from utils import dom_value as dv
from utils import cat, seq, semi
from utils.random import Random


#############################################
# SVG value generators
#############################################
def coordinate():
    return seq([Random.integer(), Random.integer()])


def points():
    num = dv.list_size()
    return cat([coordinate() for _ in range(num)])


#############################################
# SVG static values
#############################################
XMLNSValue = ConstValueWrapper("http://www.w3.org/2000/svg")


# SVG Presentation Attributes
class AlignmentBaselineValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "baseline", "before-edge", "text-before-edge", "middle", "central",
                                    "after-edge", "text-after-edge", "ideographic", "alphabetic", "hanging",
                                    "mathematical", "top", "center", "bottom"])


class ClipRuleValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["evenodd", "nonzero", "inherit"])


class ColorInterpolationValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "linearRGB", "sRGB"])


class RenderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "optimizeSpeed", "optimizeQuality"])


class EnableBackgroundValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "accumulate"
        else:
            values = ["new"]
            if Random.bool():
                values.extend([Random.integer() for _ in range(4)])
            self.value = cat(values)


class GlyphRefValue(StaticValue):
    def generate(self, _):
        self.value = "blah"


class UValue(StaticValue):
    def generate(self, _):
        self.value = Random.char()


class UnicodeValue(StaticValue):
    def generate(self, _):
        self.value = Random.string()


# glyph-orientation-vertical
class GlyphOrientationVerticalValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.angle()


class NameValue(StaticValue):
    def generate(self, _):
        # font-face-name
        self.value = Random.choice(["Courier", "SVGraffiti", "Font", "VeryUnlikelyToExistFont"])


class OffsetValue(StaticValue):
    def generate(self, _):
        self.value = dv.number_percentage()


class OverflowValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["visible", "hidden", "scroll", "auto"])


class FeMorphologyOperatorValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["erode", "dilate"])


class FeCompositeOperatorValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["over", "in", "out", "atop", "xor", "lighter", "arithmetic"])


class OrderValue(StaticValue):
    def generate(self, _):
        self.value = str(Random.range(0, 2))


class PointerEventsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["bounding-box", "visiblePainted", "visibleFill", "visibleStroke", "visible",
                                    "painted", "fill", "stroke", "all"])


class ShapeRenderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "optimizeSpeed", "crispEdges", "geometricPrecision"])


class AnimateFillValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["freeze", "remove"])


class StrokeDasharrayValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([dv.length_percentage() for _ in range(num)])


class StrokeLinecapValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["butt", "round", "square"])


class StrokeLinejoinValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["arcs", "bevel", "miter", "miter-clip", "round"])


class TextAnchorValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["start", "middle", "end"])


class VectorEffectValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"])


class WordSpacingValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "normal"
        else:
            self.value = dv.length_percentage()


class FilterDxValue(StaticValue):
    def generate(self, _):
        self.value = Random.number()


class DxValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([dv.length_percentage() for _ in range(num)])


class FormatValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(
            ["truedoc-pfr", "embedded-opentype", "type-1", "truetype", "opentype", "truetype-gx", "speedo",
             "intellifont"])


class AutoWidthValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.length_percentage()


class BBoxValue(StaticValue):
    def generate(self, _):
        self.value = seq([Random.number() for _ in range(4)])


class OrientValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = Random.choice(["auto", "auto-start-reverse"])
        elif c == 1:
            self.value = dv.angle()
        else:
            self.value = Random.number()


class PanoseValue(StaticValue):
    def generate(self, _):
        self.value = cat([Random.integer() for _ in range(10)])


class PointsValue(StaticValue):
    def generate(self, _):
        self.value = points()


class PreserveAspectRatioValue(StaticValue):
    def generate(self, _):
        values = [Random.choice(["xMinYMin", "xMidYMin", "xMaxYMin", "xMinYMid", "xMidYMid", "xMaxYMid",
                                 "xMinYMax", "xMidYMax", "xMaxYMax"])]
        if Random.bool():
            values.append(Random.choice(["meet", "slice"]))
        self.value = cat(values)


# FIXME: SVG 1.1 only
class MarkerRefXValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.length_percentage()
        else:
            self.value = Random.number()


# FIXME: SVG 1.1 only
class SymbolRefXValue(StaticValue):
    def generate(self, _):
        self.value = dv.length()


class RXValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.length_percentage()


class TableValuesValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([Random.float01() for _ in range(num)])


class UnicodeRangeValue(StaticValue):
    def generate(self, _):
        self.value = dv.unicode_range()


class ViewBoxValue(StaticValue):
    def generate(self, _):
        self.value = seq([Random.integer() for _ in range(4)])


class AltGlyphXValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 5)
        self.value = cat([dv.length() for _ in range(num)])


class TextXValue(StaticValue):
    def generate(self, _):
        num = dv.list_size()
        if num > 0:
            self.value = seq([dv.length_percentage() for _ in range(num)])
        else:
            self.value = "0"


class SpacingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "exact"])


class MethodValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["align", "stretch"])


class SideValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["left", "right"])


class UnitsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["userSpaceOnUse", "objectBoundingBox"])


class OrientationValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["h", "v"])


class AltValue(StaticValue):
    def generate(self, _):
        self.value = "icon"


class ArabicFormValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["isolated", "medial", "terminal", "initial"])


class BaseProfileValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["tiny", "basic", "full"])


class EdgeModeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["duplicate", "wrap"])


class LengthAdjustValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["spacing", "spacingAndGlyphs"])


class MarkerUnitsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["userSpaceOnUse", "strokeWidth"])


class SpreadMethodValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["pad", "reflect", "repeat"])


class StitchTilesValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["noStitch", "stitch"])


class RenderingIntentValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(
            ["auto", "perceptual", "relative-colorimetric", "saturation", "absolute-colorimetric"])


class RGBAValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["R", "G", "B", "A"])


class ZoomAndPanValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["disable", "magnify"])


class DurValue(StaticValue):
    def generate(self, _):
        self.value = dv.clock() if Random.bool() else "indefinite"


class RestartValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["always", "whenNotActive", "never"])


class RepeatCountValue(StaticValue):
    def generate(self, _):
        self.value = Random.integer() if Random.bool() else "indefinite"


class AdditiveValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["replace", "sum"])


class AccumulateValue(StaticValue):
    def generate(self, _):
        self.value = "sum"


class CalcModeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["discrete", "linear", "paced", "spline"])


class RotateValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "auto"
        elif c == 1:
            self.value = "auto-reverse"
        else:
            self.value = Random.integer()


class AnimateTransformTypeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["translate", "scale", "rotate", "skewX", "skewY"])


class FeColorMatrixTypeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["matrix", "saturate", "hueRotate", "luminanceToAlpha"])


class FeFuncTypeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["identity", "table", "discrete", "linear", "gamma"])


class FeTurbulenceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["fractalNoise", "turbulence"])


# type = "translate"
class TransformTranslateValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([dv.length_percentage() for _ in range(num)])


# type = "scale"
class TransformScaleValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([Random.number() for _ in range(num)])


# type = "rotate"
class TransformRotateValue(StaticValue):
    def generate(self, _):
        values = [dv.angle()]
        if Random.bool():
            values.extend([Random.integer(), Random.integer()])
        self.value = cat(values)


# type = "skewX" / "skewY"
class TransformSkewXValue(StaticValue):
    def generate(self, _):
        self.value = dv.angle()


class CoordinateValue(StaticValue):
    def generate(self, _):
        self.value = coordinate()


class PathValue(StaticValue):
    def generate(self, _):
        self.value = dv.path()


class BufferedRenderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "dynamic", "static"])


# baseline-shift
class BaselineShiftValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.length_percentage()
        else:
            self.value = Random.choice(["sub", "super"])


# color-interpolation-filters
class ColorInterpolationFiltersValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "linearRGB", "sRGB"])


# color-profile
class ColorProfileValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "sRGB"])


# dominant-baseline
class DominantBaselineValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "ideographic", "alphabetic", "hanging", "mathematical", "middle",
                                    "text-bottom", "central", "text-top"])


# fill-rule
class FillRuleValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["nonzero", "evenodd"])


# kerning
class KerningValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.length()


class PaintOrderValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "normal"
        else:
            selectors = Random.selectors(3)
            values = []
            if selectors[0]:
                values.append("fill")
            if selectors[1]:
                values.append("stroke")
            if selectors[2]:
                values.append("markers")
            self.value = cat(values)


class ImageHrefValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.image_url()
        else:
            self.value = "x"


class WhiteSpaceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "pre", "nowrap", "pre-wrap", "pre-line"])


class TextOverflowValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["ellipsis", "clip"])


class CrossoriginValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["anonymous", "use-credentials"])


def svg_transform():
    c = Random.selector(6)
    if c == 0:
        return dv.translate()
    elif c == 1:
        return dv.scale()
    elif c == 2:
        return dv.rotate()
    elif c == 3:
        return dv.skew_x()
    elif c == 4:
        return dv.skew_y()
    else:
        return dv.matrix()


class TransformValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([svg_transform() for _ in range(num)])


class KeySplinesValue(StaticValue):
    def __init__(self, value_count):
        super().__init__()
        self.value_count = value_count

    @staticmethod
    def control_point():
        return cat([Random.float01() for _ in range(4)])

    def generate(self, _):
        if self.value_count <= 1:
            self.value = ""
        self.value = semi([KeySplinesValue.control_point() for _ in range(self.value_count - 1)])


class KeyPointsValue(StaticValue):
    def __init__(self, value_count):
        super().__init__()
        self.value_count = value_count

    def generate(self, _):
        self.value = semi([Random.float01() for _ in range(self.value_count)])


class KeyTimesValue(StaticValue):
    def __init__(self, value_count):
        super().__init__()
        self.value_count = value_count

    @staticmethod
    def linear_time_list(num):
        if num == 1:
            return "0"
        values = [0]
        for _ in range(num - 2):
            values.append(float(Random.float01()))
        values.append(1)
        return semi(list(map(str, sorted(values))))

    @staticmethod
    def discrete_time_list(num):
        values = [str(i) for i in range(num)]
        return semi(values)

    def generate(self, _):
        if Random.bool():
            self.value = KeyTimesValue.linear_time_list(self.value_count)
        else:
            self.value = KeyTimesValue.discrete_time_list(self.value_count)


class KernelMatrixValue(StaticValue):
    def generate(self, _):
        order = Random.range(0, 2)
        self.value = cat([Random.integer() for _ in range(order ** 2)])


class FeColorMatrixValuesValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = cat([Random.number() for _ in range(20)])
        else:
            self.value = Random.float01()


#############################################
# Dynamic values
#############################################
class SVGElementIDValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.elem = None

    def generate(self, context):
        self.elem = context.get_object(docs.svg_elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is not None:
            return self.elem.id
        else:
            return "foo"


class FillValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.fill_value = None
        self.paint_server = None
        self.color = None

    def generate_static(self):
        self.paint_server = None
        if Random.bool():
            self.fill_value = Random.choice(["context-fill", "context-stroke"])
        else:
            self.fill_value = dv.color()

    def generate_dynamic(self, context):
        self.fill_value = None

        self.paint_server = context.get_object(docs.svg_paint_server_elements)
        if self.paint_server is None:
            self.generate_static()
            return

        if Random.bool():
            self.color = dv.color()
        else:
            self.color = None

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.paint_server is not None and self.paint_server in merge_map:
            self.paint_server = merge_map[self.paint_server]

    def __str__(self):
        if self.fill_value is not None:
            return self.fill_value

        s = "url(#{})".format(self.paint_server.id)
        if self.color is not None:
            s += " " + self.color
        return s


class BeginValue(DynamicValue):
    def __init__(self):
        super().__init__()
        # case 1
        self.abs = None
        # case 2
        self.elem = None
        self.action = None
        self.repeat_num = None
        # case 3
        self.event = None

    def generate_abs(self):
        self.elem = None
        self.action = None
        self.repeat_num = None
        self.event = None
        if Random.bool():
            self.abs = dv.clock()
        else:
            self.abs = "indefinite"

    def generate_rel1(self, context):
        self.abs = None
        self.action = None
        self.repeat_num = None
        self.event = None
        self.elem = context.get_object(docs.svg_animation_elements)
        if self.elem is None:
            self.generate_abs()
            return
        self.action = Random.choice(["begin", "end", "repeat"])
        if self.action == "repeat":
            self.repeat_num = Random.integer()

    def generate_rel2(self, context):
        self.abs = None
        self.action = None
        self.repeat_num = None
        self.event = None
        self.elem = context.get_object(docs.elements)
        if self.elem is None:
            self.generate_abs()
            return
        self.event = Random.choice(docs.svg_animation_begin_events)

    def generate(self, context):
        c = Random.selector(5)
        if c == 0 or c == 1:
            self.generate_abs()
        elif c == 2 or c == 3:
            self.generate_rel1(context)
        else:
            self.generate_rel2(context)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.abs is not None:
            return self.abs
        if self.elem is None:
            return ""
        if self.action is not None:
            s = "{}.{}".format(self.elem.id, self.action)
            if self.action == "repeat":
                s += "({})".format(self.repeat_num)
            return s
        else:
            return "{}.{}".format(self.elem.id, self.event)


# marker-start/mid/end
class MarkerValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.marker = None

    def generate(self, context):
        self.marker = context.get_object(["SVGMarkerElement"])

    def merge_fix(self, merge_map):
        if self.marker is not None and self.marker in merge_map:
            self.marker = merge_map[self.marker]

    def __str__(self):
        if self.marker is None:
            return "none"
        return "url(#{})".format(self.marker.id)


class PatternHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.pattern = None

    def generate(self, context):
        self.pattern = context.get_object(["SVGPatternElement"])

    def merge_fix(self, merge_map):
        if self.pattern is not None and self.pattern in merge_map:
            self.pattern = merge_map[self.pattern]

    def __str__(self):
        if self.pattern is None:
            return "none"
        return "url(#{})".format(self.pattern.id)


class FeImageHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.value = None
        self.image = None

    def generate_static(self):
        self.image = None
        if Random.bool():
            self.value = dv.image_url()
        else:
            self.value = "x"

    def generate_dynamic(self, context):
        self.value = None
        self.image = context.get_object(docs.image_elements)
        if self.image is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.image is not None and self.image in merge_map:
            self.image = merge_map[self.image]

    def __str__(self):
        if self.value is not None:
            return self.value
        return "#{}".format(self.image.id)


class UseHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.elem = None

    def generate(self, context):
        self.elem = context.get_object(docs.svg_elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is None:
            return "#foo"
        return "#{}".format(self.elem.id)


class GradientHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.gradient = None

    def generate(self, context):
        self.gradient = context.get_object(docs.svg_gradient_elements)

    def merge_fix(self, merge_map):
        if self.gradient is not None and self.gradient in merge_map:
            self.gradient = merge_map[self.gradient]

    def __str__(self):
        if self.gradient is None:
            return "#foo"
        return "#{}".format(self.gradient.id)


class PathHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.path = None

    def generate(self, context):
        self.path = context.get_object(["SVGPathElement"])

    def merge_fix(self, merge_map):
        if self.path is not None and self.path in merge_map:
            self.path = merge_map[self.path]

    def __str__(self):
        if self.path is None:
            return "#foo"
        return "#{}".format(self.path.id)


class CursorHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.image = None

    def generate_static(self):
        self.image = None
        if Random.bool():
            self.value = dv.image_url()
        else:
            self.value = "x"

    def generate_dynamic(self, context):
        self.value = None
        self.image = context.get_object(docs.image_elements)
        if self.image is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.image is not None and self.image in merge_map:
            self.image = merge_map[self.image]

    def __str__(self):
        if self.value is not None:
            return self.value
        return "#{}".format(self.image.id)


class TRefXlinkHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.text = None

    def generate(self, context):
        self.text = context.get_object(docs.svg_text_content_elements)

    def merge_fix(self, merge_map):
        if self.text is not None and self.text in merge_map:
            self.text = merge_map[self.text]

    def __str__(self):
        if self.text is None:
            return "#foo"
        return "#{}".format(self.text.id)


class GlyphRefXlinkHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.glyph = None

    def generate(self, context):
        self.glyph = context.get_object(["SVGGlyphElement"])

    def merge_fix(self, merge_map):
        if self.glyph is not None and self.glyph in merge_map:
            self.glyph = merge_map[self.glyph]

    def __str__(self):
        if self.glyph is None:
            return "#foo"
        return "#{}".format(self.glyph.id)


class AltGlyphXlinkHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.glyph = None

    def generate(self, context):
        self.glyph = context.get_object(["SVGGlyphElement", "SVGAltGlyphDefElement"])

    def merge_fix(self, merge_map):
        if self.glyph is not None and self.glyph in merge_map:
            self.glyph = merge_map[self.glyph]

    def __str__(self):
        if self.glyph is None:
            return "#foo"
        return "#{}".format(self.glyph.id)


class FontFaceUriXlinkHrefValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.font = None

    def generate(self, context):
        self.font = context.get_object(["SVGFontElement"])

    def merge_fix(self, merge_map):
        if self.font is not None and self.font in merge_map:
            self.font = merge_map[self.font]

    def __str__(self):
        if self.font is None:
            return "#foo"
        return "#{}".format(self.font.id)


class GValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.glyph = None

    def generate(self, context):
        self.glyph = context.get_object(["SVGGlyphElement"])

    def merge_fix(self, merge_map):
        if self.glyph is not None and self.glyph in merge_map:
            self.glyph = merge_map[self.glyph]

    def __str__(self):
        if self.glyph is None:
            return "foo"
        return self.glyph.id


class InValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.filter_primitive = None

    def generate_static(self):
        self.filter_primitive = None
        self.value = Random.choice(
            ["SourceGraphic", "SourceAlpha", "BackgroundImage", "BackgroundAlpha", "FillPaint", "StrokePaint"])

    def generate_dynamic(self, context):
        self.value = None
        self.filter_primitive = context.get_object(docs.svg_filter_primitives)
        if self.filter_primitive is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.filter_primitive is not None and self.filter_primitive in merge_map:
            self.filter_primitive = merge_map[self.filter_primitive]

    def __str__(self):
        if self.filter_primitive is not None:
            return self.filter_primitive.id
        return self.value


#############################################
# Animation values
#############################################
class FromValue(DynamicValue):
    def __init__(self, value_class):
        super().__init__()
        self.value_class = value_class
        self.value = None

    def generate(self, context):
        self.value = self.value_class()
        self.value.generate(context)

    def mutate(self, context) -> bool:
        self.value.mutate(context)
        return True

    def merge_fix(self, merge_map):
        self.value.merge_fix(merge_map)

    def __str__(self):
        return str(self.value)


class AnimationValuesValue(DynamicValue):
    def __init__(self, value_class, value_count):
        super().__init__()
        self.value_class = value_class
        self.value_count = value_count
        self.values = []

    def generate(self, context):
        for _ in range(self.value_count):
            value = self.value_class()
            value.generate(context)
            self.values.append(value)

    def mutate(self, context) -> bool:
        value = Random.choice(self.values)
        value.mutate(context)
        return True

    def merge_fix(self, merge_map):
        for value in self.values:
            value.merge_fix(merge_map)

    def __str__(self):
        return semi(list(map(str, self.values)))
