import docs
from config import CSSConfig
from value import StaticValue, DynamicValue
from utils import cat, seq
from utils import dom_value as dv
from utils.random import Random


#####################################
# CSS value generators
#####################################
def geometry_box():
    return Random.choice(
        ["margin-box", "border-box", "padding-box", "content-box", "fill-box", "stroke-box", "view-box"])


def shape_box():
    return Random.choice(["border-box", "padding-box", "content-box", "margin-box"])


def blur():
    return "blur({})".format(dv.length())


def brightness():
    return "brightness({})".format(dv.number_percentage())


def contrast():
    return "contrast({})".format(dv.number_percentage())


def drop_shadow():
    num = Random.range(2, 3)
    values = [dv.length() for _ in range(num)]
    if Random.bool():
        values.append(dv.color())
    return "drop-shadow({})".format(cat(values))


def grayscale():
    return "grayscale({})".format(dv.number_percentage())


def hue_rotate():
    return "hue-rotate({})".format(dv.angle())


def invert():
    return "invert({})".format(dv.number_percentage())


def opacity():
    return "opacity({})".format(dv.number_percentage())


def saturate():
    return "saturate({})".format(dv.number_percentage())


def sepia():
    return "sepia({})".format(dv.number_percentage())


def filter_function():
    c = Random.selector(10)
    if c == 0:
        return blur()
    elif c == 1:
        return brightness()
    elif c == 2:
        return contrast()
    elif c == 3:
        return drop_shadow()
    elif c == 4:
        return grayscale()
    elif c == 5:
        return hue_rotate()
    elif c == 6:
        return invert()
    elif c == 7:
        return opacity()
    elif c == 8:
        return saturate()
    else:
        return sepia()


def alpha():
    if Random.bool():
        return Random.float01()
    else:
        return dv.percentage()


def repeat():
    return Random.choice(["repeat", "space", "round", "no-repeat"])


def step_position():
    return Random.choice(["jump-start", "jump-end", "jump-none", "jump-both", "start", "end"])


def step_timing_function():
    if Random.bool():
        return Random.choice(["step-start", "step-end"])
    else:
        values = [Random.integer()]
        if Random.bool():
            values.append(step_position())
        return "steps({})".format(seq(values))


def line_width():
    if Random.bool():
        return Random.choice(["thin", "medium", "thick"])
    else:
        return dv.length()


def line_height():
    c = Random.selector(4)
    if c == 0:
        return "normal"
    elif c == 1:
        return Random.number()
    elif c == 2:
        return dv.length()
    else:
        return dv.percentage()


def line_style():
    return Random.choice(["hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"])


def side_or_corner():
    c = Random.selector(3)
    if c == 0:
        return Random.choice(["left", "right"])
    elif c == 1:
        return Random.choice(["top", "bottom"])
    else:
        return cat([Random.choice(["left", "right"]), Random.choice(["top", "bottom"])])


def linear_color_stop():
    values = [dv.color()]
    if Random.bool():
        num = Random.range(1, 2)
        values.extend([dv.length_percentage() for _ in range(num)])
    return cat(values)


def angular_color_stop():
    values = [dv.color()]
    if Random.bool():
        num = Random.range(1, 2)
        values.extend([dv.angle_percentage() for _ in range(num)])
    return cat(values)


def color_stop_list():
    return linear_color_stop()


def angular_color_stop_list():
    return angular_color_stop()


def _linear_gradient():
    values = []
    if Random.bool():
        if Random.bool():
            values.append(dv.angle())
        else:
            values.extend(["to", side_or_corner()])

    _color_stop_list = color_stop_list()
    if len(values) > 0:
        value = seq([cat(values), _color_stop_list])
    else:
        value = _color_stop_list
    return value


def linear_gradient():
    return "linear-gradient({})".format(_linear_gradient())


def repeating_linear_gradient():
    return "repeating-linear-gradient({})".format(_linear_gradient())


def ending_shape():
    return Random.choice(["circle", "ellipse"])


def radial_gradient_size():
    c = Random.selector(3)
    if c == 0:
        return Random.choice(["closest-side", "farthest-side", "closest-corner", "farthest-corner"])
    elif c == 1:
        return dv.length()
    else:
        return dv.length_percentage() + " " + dv.length_percentage()


def _radial_gradient():
    values = []
    if Random.bool():
        selectors = Random.selectors(2)
        if selectors[0]:
            values.append(ending_shape())
        if selectors[1]:
            values.append(radial_gradient_size())
    if Random.bool():
        values.extend(["at", dv.position()])

    _color_stop_list = color_stop_list()
    if len(values) > 0:
        value = seq([cat(values), _color_stop_list])
    else:
        value = _color_stop_list
    return value


def radial_gradient():
    return "radial-gradient({})".format(_radial_gradient())


def repeating_radial_gradient():
    return "repeating-radial-gradient({})".format(_radial_gradient())


def conic_gradient():
    values = []
    if Random.bool():
        values.extend(["from", dv.angle()])
    if Random.bool():
        values.extend(["at", dv.position()])

    _angular_color_stop_list = angular_color_stop_list()
    if len(values) > 0:
        value = seq([cat(values), _angular_color_stop_list])
    else:
        value = _angular_color_stop_list
    return "conic-gradient({})".format(value)


def image():
    c = Random.selector(6)
    if c == 0:
        return "url({})".format(dv.image_url())
    elif c == 1:
        return linear_gradient()
    elif c == 2:
        return repeating_linear_gradient()
    elif c == 3:
        return radial_gradient()
    elif c == 4:
        return repeating_radial_gradient()
    else:
        return conic_gradient()


def column_width():
    return dv.length() if Random.bool() else "auto"


def column_count():
    return Random.integer() if Random.bool() else "auto"


def flex_basis():
    return dv.length_percentage() if Random.bool() else "auto"


def quote():
    return Random.choice(["open-quote", "close-quote", "no-open-quote", "no-close-quote"])


def leader():
    leader_type = Random.choice(["dotted", "solid", "space"]) if Random.bool() else Random.string()
    return "leader({})".format(leader_type)


def flex_direction():
    return Random.choice(["row", "row-reverse", "column", "column-reverse"])


def flex_wrap():
    return Random.choice(["nowrap", "wrap", "wrap-reverse"])


def flex():
    return "{}fr".format(Random.number())


def track_breadth():
    c = Random.selector(3)
    if c == 0:
        return Random.choice(["auto", "min-content", "max-content"])
    elif c == 1:
        return flex()
    else:
        return dv.length_percentage()


def inflexible_breadth():
    if Random.bool():
        return Random.choice(["auto", "min-content", "max-content"])
    else:
        return dv.length_percentage()


def track_size():
    c = Random.selector(3)
    if c == 0:
        return track_breadth()
    elif c == 1:
        return "minmax({}, {})".format(inflexible_breadth(), track_breadth())
    else:
        return "fit-content({})".format(dv.length_percentage())


# TODO: > 1
def track_repeat():
    return "repeat({}, {})".format(Random.integer(), track_size())


# TODO: > 1
def fixed_repeat():
    return "repeat({}, {})".format(Random.integer(), fixed_size())


def auto_repeat():
    return "repeat({}, {})".format(Random.choice(["auto-fill", "auto-fit"]), fixed_size())


def fixed_size():
    c = Random.selector(3)
    if c == 0:
        return dv.length_percentage()
    elif c == 1:
        return "minmax({}, {})".format(inflexible_breadth(), track_breadth())
    else:
        return "fit-content({})".format(dv.length_percentage())


def track():
    if Random.bool():
        return track_size()
    else:
        return track_repeat()


def fixed():
    if Random.bool():
        return fixed_size()
    else:
        return fixed_repeat()


def track_list():
    num = Random.range(1, 2)
    return cat([track() for _ in range(num)])


def auto_track_list():
    num = Random.range(0, 1)
    values = [fixed() for _ in range(num)]
    values.append(auto_repeat())
    num = Random.range(0, 1)
    values.extend([fixed() for _ in range(num)])
    return cat(values)


def explicit_track_list():
    num = Random.range(1, 2)
    return cat([track_size() for _ in range(num)])


def baseline_position():
    values = []
    if Random.bool():
        values.append(Random.choice(["first", "last"]))
    values.append("baseline")
    return cat(values)


def overflow_position():
    return Random.choice(["unsafe", "safe"])


def self_position():
    return Random.choice(["center", "start", "end", "self-start", "self-end", "flex-start", "flex-end"])


def location():
    c = Random.selector(3)
    if c == 0:
        return dv.length()
    elif c == 1:
        return dv.percentage()
    else:
        return "auto"


def basic_shape():
    c = Random.selector(5)
    if c == 0:
        return dv.inset()
    elif c == 1:
        return dv.circle()
    elif c == 2:
        return dv.ellipse()
    elif c == 3:
        return dv.polygon()
    else:
        return dv.path_shape()


#####################################
# CSS variables
#####################################
class CSSColorValue(StaticValue):
    def generate(self, _):
        if Random.selector(CSSConfig.use_css_var) == 0:
            self.value = "var(--css-color)"
        else:
            self.value = dv.color()


class CSSLineWidthValue(StaticValue):
    def generate(self, _):
        if Random.selector(CSSConfig.use_css_var) == 0:
            self.value = "var(--css-line-width)"
        else:
            self.value = line_width()


class CSSLengthValue(StaticValue):
    def generate(self, _):
        if Random.selector(CSSConfig.use_css_var) == 0:
            self.value = "var(--css-length)"
        else:
            self.value = dv.length()


class CSSLengthPercentageValue(StaticValue):
    def generate(self, _):
        if Random.selector(CSSConfig.use_css_var) == 0:
            self.value = "var(--css-length-percent)"
        else:
            self.value = dv.length_percentage()


#####################################
# Static CSS values
#####################################
class ColorValue(StaticValue):
    def generate(self, _):
        self.value = dv.color()


class LineWidthValue(StaticValue):
    def generate(self, _):
        self.value = line_width()


class ImageValue(StaticValue):
    def generate(self, _):
        self.value = image()


class RadiusValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([dv.length_percentage() for _ in range(num)])


class LineStyleValue(StaticValue):
    def generate(self, _):
        self.value = line_style()


class LocationValue(StaticValue):
    def generate(self, _):
        self.value = location()


class BottomValue(StaticValue):
    def generate(self, _):
        if Random.selector(5) == 0:
            self.value = "auto"
        else:
            self.value = dv.length_percentage(relative=True)


# opacity
class OpacityValue(StaticValue):
    def generate(self, _):
        self.value = alpha()


# -webkit-app-region
class WebkitAppRegionValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["drag", "no-drag"])


# appearance
class AppearanceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["searchfield-cancel-button", "radio", "relevancy-level-indicator",
                                    "push-button", "media-controls-background", "button", "media-sliderthumb",
                                    "media-volume-sliderthumb", "media-play-button", "sliderthumb-vertical",
                                    "menulist-button", "slider-vertical", "slider-horizontal", "textarea",
                                    "square-button", "sliderthumb-horizontal", "discrete-capacity-level-indicator",
                                    "media-volume-slider-container", "media-volume-slider-mute-button", "textfield",
                                    "caps-lock-indicator", "progress-bar", "meter"])


# -webkit-color-correction
class WebkitColorCorrectionValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["sRGB", "default"])


# -webkit-flow-from
class WebkitFlowFromValue(StaticValue):
    def generate(self, _):
        self.value = "flow0"


# -webkit-flow-into
class WebkitFlowIntoValue(StaticValue):
    def generate(self, _):
        self.value = "flow0"


# -webkit-font-smoothing
class WebkitFontSmoothingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "antialiased", "subpixel-antialiased", "none"])


# -webkit-hyphenate-character
class WebkitHyphenateCharacterValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "floating", "'-'"])


def webkit_margin_collapse():
    return Random.choice(["collapse", "separate", "discard"])


# -webkit-margin-after-collapse
class WebkitMarginAfterCollapseValue(StaticValue):
    def generate(self, _):
        self.value = webkit_margin_collapse()


# -webkit-margin-collapse
class WebkitMarginCollapseValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([webkit_margin_collapse() for _ in range(num)])


# -webkit-marquee-speed
class WebkitMarqueeSpeedValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["fast", "inherit", "normal", "slow"])
        else:
            self.value = dv.clock_in_ms()


# -webkit-mask-box-image
class WebkitMaskBoxImageValue(StaticValue):
    def generate(self, _):
        values = []
        selectors = Random.selectors(2)
        if selectors[0]:
            values.append(image())
        if selectors[1]:
            values.extend([dv.length_percentage() for _ in range(4)])
            values.extend([border_image_repeat() for _ in range(2)])
        self.value = cat(values)


# mask
def mask_repeat_style():
    if Random.bool():
        return Random.choice(["repeat-x", "repeat-y"])
    else:
        num = Random.range(1, 2)
        return cat([repeat() for _ in range(num)])


def mask_composite():
    return Random.choice(["add", "subtract", "intersect", "exclude"])


def mask_mode():
    return Random.choice(["alpha", "luminance", "match-source"])


def mask_clip():
    if Random.bool():
        return geometry_box()
    else:
        return "no-clip"


def mask_position():
    num = Random.range(1, 2)
    return seq([dv.position() for _ in range(num)])


# mask-clip
class MaskClipValue(StaticValue):
    def generate(self, _):
        self.value = mask_clip()


# mask-composite
class MaskCompositeValue(StaticValue):
    def generate(self, _):
        self.value = mask_composite()


# mask-origin
class MaskOriginValue(StaticValue):
    def generate(self, _):
        self.value = geometry_box()


# mask-position
class MaskPositionValue(StaticValue):
    def generate(self, _):
        self.value = mask_position()


# mask-repeat
class MaskRepeatValue(StaticValue):
    def generate(self, _):
        self.value = mask_repeat_style()


# mask-source-type
class MaskSourceTypeValue(StaticValue):
    def generate(self, _):
        self.value = mask_mode()


# -webkit-mask-repeat-x/y
class WebkitMaskRepeatXValue(StaticValue):
    def generate(self, _):
        self.value = repeat()


# mask-size
class MaskSizeValue(StaticValue):
    def generate(self, _):
        self.value = background_size()


# -webkit-nbsp-mode
class WebkitNbspModeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "space"])


# -webkit-overflow-scrolling
class WebkitOverflowScrollingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "touch"])


# -webkit-print-color-adjust
class WebkitPrintColorAdjustValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["economy", "exact"])


# -webkit-rtl-ordering
class WebkitRtlOrderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["logical", "visual"])


# -webkit-ruby-position
class WebkitRubyPositionValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["before", "after", "inter-character"])


# -webkit-text-combine
class WebkitTextCombineValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["horizontal", "none"])


def text_emphasis_style():
    if Random.bool():
        return "'{}'".format(Random.choice(["*", "@", "x", "\\25B2"]))
    else:
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(Random.choice(["filled", "open"]))
        if selectors[1]:
            values.append(Random.choice(["dot", "circle", "double-circle", "triangle", "sesame"]))
        return cat(values)


# text-emphasis
class TextEmphasisValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(text_emphasis_style())
        if selectors[1]:
            values.append(dv.color())
        self.value = cat(values)


# text-emphasis-position
class TextEmphasisPositionValue(StaticValue):
    def generate(self, _):
        self.value = cat([Random.choice(["over", "under"]), Random.choice(["right", "left"])])


# text-emphasis-style
class TextEmphasisStyleValue(StaticValue):
    def generate(self, _):
        self.value = text_emphasis_style()


# -webkit-text-security
class WebkitTextSecurityValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["circle", "disc", "square", "none", "not-secure"])


# -webkit-text-stroke
class WebkitTextStrokeValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(dv.length())
        if selectors[1]:
            values.append(dv.color())
        self.value = cat(values)


# -webkit-text-stroke-color
class WebkitTextStrokeColorValue(StaticValue):
    def generate(self, _):
        self.value = dv.color()


# -webkit-text-stroke-width
class WebkitTextStrokeWidthValue(StaticValue):
    def generate(self, _):
        self.value = dv.length()


# -webkit-user-drag
class WebkitUserDragValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "element", "none"])


# -webkit-user-modify
class WebkitUserModifyValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["read-only", "read-write", "read-write-plaintext-only", "write-only"])


# -webkit-wrap-flow
class WebkitWrapFlowValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "both", "start", "end", "maximum", "clear"])


# align-content
class AlignContentValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = "normal"
        elif c == 1:
            values = []
            if Random.bool():
                values.append(Random.choice(["first", "last"]))
            values.append("baseline")
            self.value = cat(values)
        elif c == 2:
            self.value = Random.choice(["space-between", "space-around", "space-evenly", "stretch"])
        else:
            values = []
            if Random.bool():
                values.append(Random.choice(["unsafe", "safe"]))
            values.append(Random.choice(["center", "start", "end", "flex-start", "flex-end"]))
            self.value = cat(values)


# align-items
class AlignItemsValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = "normal"
        elif c == 1:
            self.value = "stretch"
        elif c == 2:
            values = []
            if Random.bool():
                values.append(Random.choice(["first", "last"]))
            values.append("baseline")
            self.value = cat(values)
        else:
            values = []
            if Random.bool():
                values.append(Random.choice(["unsafe", "safe"]))
            values.append(Random.choice(["center", "start", "end", "flex-start", "flex-end", "self-start", "self-end"]))
            self.value = cat(values)


# align-self
class AlignSelfValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = Random.choice(["auto", "normal"])
        elif c == 1:
            self.value = "stretch"
        elif c == 2:
            values = []
            if Random.bool():
                values.append(Random.choice(["first", "last"]))
            values.append("baseline")
            self.value = cat(values)
        else:
            values = []
            if Random.bool():
                values.append(Random.choice(["unsafe", "safe"]))
            values.append(Random.choice(["center", "start", "end", "flex-start", "flex-end", "self-start", "self-end"]))
            self.value = cat(values)


# all
class AllValue(StaticValue):
    def generate(self, _):
        self.value = "revert"


def animation_name(context):
    count = Random.range(1, 2)
    return seq([context.get_token("keyframes") for _ in range(count)])


def animation_duration():
    return dv.clock()


def animation_timing_function():
    def single():
        if Random.bool():
            return dv.animation_easing()
        else:
            return step_timing_function()
    count = Random.range(1, 2)
    return seq([single() for _ in range(count)])


def animation_delay():
    value = dv.clock()
    if Random.bool():
        value = "-" + value
    return value


def animation_direction():
    count = Random.range(1, 2)
    return seq([dv.animation_direction() for _ in range(count)])


def animation_iteration_count():
    if Random.bool():
        return "infinite"
    else:
        return Random.number()


def animation_fill_mode():
    count = Random.range(1, 2)
    return seq([dv.animation_fill_mode() for _ in range(count)])


# animation-delay
class AnimationDelayValue(StaticValue):
    def generate(self, _):
        self.value = animation_delay()


# animation-direction
class AnimationDirectionValue(StaticValue):
    def generate(self, _):
        self.value = animation_direction()


# animation-duration
class AnimationDurationValue(StaticValue):
    def generate(self, _):
        self.value = animation_duration()


# animation-fill-mode
class AnimationFillModeValue(StaticValue):
    def generate(self, _):
        self.value = animation_fill_mode()


# animation-iteration-count
class AnimationIterationCountValue(StaticValue):
    def generate(self, _):
        self.value = animation_iteration_count()


# animation-play-state
class AnimationPlayStateValue(StaticValue):
    def generate(self, _):
        self.value = dv.play_state()


# animation-timing-function
class AnimationTimingFunctionValue(StaticValue):
    def generate(self, _):
        self.value = animation_timing_function()


# backface-visibility
class BackfaceVisibilityValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["visible", "hidden"])


def background_clip():
    num = Random.range(1, 2)
    return seq([Random.choice(["border-box", "padding-box", "content-box", "text"]) for _ in range(num)])


def background_origin():
    num = Random.range(1, 2)
    return seq([Random.choice(["border-box", "padding-box", "content-box"]) for _ in range(num)])


def background_size():
    if Random.bool():
        return Random.choice(["cover", "contain", "auto"])
    else:
        def single():
            if Random.bool():
                return "auto"
            else:
                return dv.length_percentage()

        num = Random.range(1, 2)
        return cat([single() for _ in range(num)])


def background_attachment():
    return Random.choice(["scroll", "fixed", "local"])


def background_repeat():
    if Random.bool():
        return Random.choice(["repeat-x", "repeat-y"])
    else:
        num = Random.range(1, 2)
        return cat([Random.choice(["repeat", "space", "round", "no-repeat"]) for _ in range(num)])


def background_position():
    c = Random.selector(3)
    if c == 0:
        if Random.bool():
            return Random.choice(["left", "center", "right", "top", "bottom"])
        else:
            return dv.length_percentage()
    elif c == 1:
        values = []
        if Random.bool():
            if Random.bool():
                values.append(Random.choice(["left", "center", "right"]))
            else:
                values.append(dv.length_percentage())
        else:
            if Random.bool():
                values.append(Random.choice(["top", "center", "bottom"]))
            else:
                values.append(dv.length_percentage())
        return cat(values)
    else:
        values = []
        if Random.bool():
            values.append("center")
        else:
            values.append(Random.choice(["left", "right"]))
            if Random.bool():
                values.append(dv.length_percentage())
        if Random.bool():
            values.append("center")
        else:
            values.append(Random.choice(["top", "bottom"]))
            if Random.bool():
                values.append(dv.length_percentage())
        return cat(values)


# background
class BackgroundValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(7)
        values = []
        if selectors[0]:
            values.append(dv.color())
        if selectors[1]:
            values.append(image())
        if selectors[2]:
            values.append(background_position())
            if Random.bool():
                values.extend(["/", background_size()])
        if selectors[3]:
            values.append(background_repeat())
        if selectors[4]:
            values.append(background_attachment())
        if selectors[5]:
            values.append(background_origin())
        if selectors[6]:
            values.append(background_clip())
        self.value = cat(values)


# background-attachment
class BackgroundAttachmentValue(StaticValue):
    def generate(self, _):
        self.value = background_attachment()


def blend_mode():
    return Random.choice(
        ["normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "color-burn", "hard-light",
         "soft-light", "difference", "exclusion", "hue", "saturation", "color", "luminosity"])


#  mode / mix-blend-mode in SVG
class BlendModeValue(StaticValue):
    def generate(self, _):
        self.value = blend_mode()


# background-blend-mode
class BackgroundBlendModeValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = seq([blend_mode() for _ in range(num)])


# background-clip
class BackgroundClipValue(StaticValue):
    def generate(self, _):
        self.value = background_clip()


# background-origin
class BackgroundOriginValue(StaticValue):
    def generate(self, _):
        self.value = background_origin()


# background-position
class BackgroundPositionValue(StaticValue):
    def generate(self, _):
        self.value = background_position()


# background-position-x
class BackgroundPositionXValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "center"
        elif c == 1:
            self.value = Random.choice(["left", "right", "x-start", "x-end"])
        else:
            self.value = dv.length_percentage()


# background-position-y
class BackgroundPositionYValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "center"
        elif c == 1:
            self.value = Random.choice(["left", "right", "y-start", "y-end"])
        else:
            self.value = dv.length_percentage()


# background-repeat
class BackgroundRepeatValue(StaticValue):
    def generate(self, _):
        self.value = background_repeat()


# background-repeat-x
class BackgroundRepeatXValue(StaticValue):
    def generate(self, _):
        self.value = repeat()


# background-size
class BackgroundSizeValue(StaticValue):
    def generate(self, _):
        self.value = background_size()


def border_style():
    return Random.choice(["hidden", "dotted", "dashed", "solid", "double", "groove", "ridge",
                          "inset", "outset"])


def border_color():
    num = Random.range(1, 4)
    return cat([dv.color() for _ in range(num)])


# border / column-rule
class BorderValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(3)
        values = []
        if selectors[0]:
            values.append(line_width())
        if selectors[1]:
            values.append(border_style())
        if selectors[2]:
            values.append(dv.color())
        self.value = cat(values)


# border-bottom
class LineValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(3)
        values = []
        if selectors[0]:
            values.append(line_width())
        if selectors[1]:
            values.append(line_style())
        if selectors[2]:
            values.append(dv.color())
        self.value = cat(values)


# border-collapse
class BorderCollapseValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["collapse", "separate"])


def border_image_slice():
    num = Random.range(1, 4)
    values = [dv.number_percentage() for _ in range(num)]
    if Random.bool():
        values.append("fill")
    return cat(values)


def border_image_width():
    num = Random.range(1, 4)
    values = []
    for _ in range(num):
        c = Random.selector(3)
        if c == 0:
            values.append(dv.length_percentage())
        elif c == 1:
            values.append(Random.number())
        else:
            values.append("auto")
    return cat(values)


def border_image_outset():
    num = Random.range(1, 4)
    values = []
    for _ in range(num):
        if Random.bool():
            values.append(dv.length())
        else:
            values.append(Random.number())
    return cat(values)


def border_image_repeat():
    num = Random.range(1, 2)
    return cat([Random.choice(["stretch", "repeat", "round", "space"]) for _ in range(num)])


# border-image
class BorderImageValue(StaticValue):
    def generate(self, _):
        values = []
        selectors = Random.selectors(3)
        if selectors[0]:
            values.append(image())
        if selectors[1]:
            values.append(border_image_slice())
            if Random.bool():
                values.extend(["/", border_image_width()])
            else:
                if Random.bool():
                    values.extend(["/", border_image_width()])
                values.extend(["/", border_image_outset()])
        if selectors[2]:
            values.append(border_image_repeat())
        self.value = cat(values)


# border-image-outset
class BorderImageOutsetValue(StaticValue):
    def generate(self, _):
        self.value = border_image_outset()


# border-image-repeat
class BorderImageRepeatValue(StaticValue):
    def generate(self, _):
        self.value = border_image_repeat()


# border-image-slice
class BorderImageSliceValue(StaticValue):
    def generate(self, _):
        self.value = border_image_slice()


# border-image-width
class BorderImageWidthValue(StaticValue):
    def generate(self, _):
        self.value = border_image_width()


# border-radius
class BorderRadiusValue(StaticValue):
    def generate(self, _):
        if Random.selector(5) == 0:
            self.value = "inherit"
        else:
            self.value = dv.border_radius()


# border-spacing
class BorderSpacingValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([dv.length() for _ in range(num)])


# border-style
class BorderStyleValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([border_style() for _ in range(num)])


# border-width
class BorderWidthValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([line_width() for _ in range(num)])


# box-align
class BoxAlignValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["start", "center", "end", "baseline", "stretch"])


# box-decoration-break
class BoxDecorationBreakValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["slice", "clone"])


# box-direction
class BoxDirectionValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "reverse", "inherit"])


# box-lines
class BoxLinesValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["single", "multiple"])


# box-orient
class BoxOrientValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["horizontal", "vertical", "inline-axis", "block-axis", "inherit"])


# box-pack
class BoxPackValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["start", "center", "end", "justify"])


# box-reflect
class BoxReflectValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(3)
        values = []
        if selectors[0]:
            values.append(Random.choice(["above", "below", "right", "left"]))
        if selectors[1]:
            values.append(dv.length())
        if selectors[2]:
            values.append(image())
        self.value = cat(values)


# box-shadow
class BoxShadowValue(StaticValue):
    def generate(self, _):
        values = []
        num = Random.range(2, 4)
        values.extend([dv.length() for _ in range(num)])
        if Random.bool():
            values.append("inset")
        if Random.bool():
            values.append(dv.color())
        self.value = cat(values)


# box-sizing
class BoxSizingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["content-box", "border-box", "padding-box"])


# page
class PageValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["Rotated", "Auto", "Auto Rotated"])
        else:
            self.value = "{}cm".format(Random.integer())


# break-after
class BreakValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "avoid", "always", "all", "avoid-page", "page", "left", "right", "recto",
                                    "verso", "avoid-column", "column", "avoid-region", "region"])


# break-inside
class BreakInsideValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "avoid", "avoid-page", "avoid-column", "avoid-region"])


# caption-side
class CaptionSideValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["top", "bottom", "block-start", "block-end", "inline-start", "inline-end"])


# clear
class ClearValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["left", "right", "both", "inline-start", "inline-end"])


# clip
class ClipValue(StaticValue):
    def generate(self, _):
        def edge():
            if Random.bool():
                return "auto"
            else:
                return dv.length()

        if Random.selector(5) == 0:
            self.value = "auto"
        else:
            self.value = "rect({})".format(seq([edge() for _ in range(4)]))


# column-break-after
class ColumnBreakAfterValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["always", "auto", "avoid"])


# column-count
class ColumnCountValue(StaticValue):
    def generate(self, _):
        self.value = column_count()


# column-fill
class ColumnFillValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "balance", "balance-all"])


# column-gap
class ColumnGapValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["initial", "normal"])
        else:
            self.value = dv.length_percentage()


# column-span
class ColumnSpanValue(StaticValue):
    def generate(self, _):
        self.value = "all"


# column-width
class ColumnWidthValue(StaticValue):
    def generate(self, _):
        self.value = column_width()


# columns
class ColumnsValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(column_width())
        if selectors[1]:
            values.append(column_count())
        self.value = cat(values)


# contain
class ContainValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["strict", "content"])
        else:
            selectors = Random.selectors(4)
            values = []
            if selectors[0]:
                values.append("size")
            if selectors[1]:
                values.append("layout")
            if selectors[2]:
                values.append("style")
            if selectors[3]:
                values.append("paint")
            self.value = cat(values)


# content
class ContentValue(StaticValue):
    def generate(self, context):
        c = Random.selector(7)
        if c == 0:
            self.value = Random.choice(["normal", "contents"])
        elif c == 1:
            self.value = "'foo'"
        elif c == 2:
            self.value = quote()
        elif c == 3:
            self.value = leader()
        elif c == 4:
            self.value = "counter({}, {})".format(
                context.get_token("counter"),
                Random.choice(["disc", "circle", "decimal", "lower-alpha", "upper-alpha",
                               "lower-latin", "upper-latin", "lower-roman", "upper-roman"])
            )
        elif c == 5:
            self.value = "counters({}, '.', {})".format(
                context.get_token("counter"),
                Random.choice(["disc", "circle", "decimal", "lower-alpha", "upper-alpha",
                               "lower-latin", "upper-latin", "lower-roman", "upper-roman"])
            )
        else:
            self.value = image()


def cursor_fallback():
    return Random.choice(
        ["auto", "default", "context-menu", "help", "pointer", "progress", "wait", "cell", "crosshair",
         "text", "vertical-text", "alias", "copy", "move", "no-drop", "not-allowed", "e-resize", "n-resize",
         "ne-resize", "nw-resize", "s-resize", "se-resize", "sw-resize", "w-resize", "ew-resize", "ns-resize",
         "nesw-resize", "nwse-resize", "col-resize", "row-resize", "all-scroll", "zoom-in", "zoom-out", "grab",
         "grabbing"]
    )


# direction
class DirectionValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["ltr", "rtl"])


# display
class DisplayValue(StaticValue):
    def generate(self, _):
        c = Random.selector(5)
        if c == 0:
            selectors = Random.selectors(2)
            values = []
            if selectors[0]:
                values.append(Random.choice(["block", "inline", "run-in"]))
            if selectors[1]:
                values.append(Random.choice(["flow", "flow-root", "table", "flex", "grid", "ruby"]))
            self.value = cat(values)
        elif c == 1:
            values = ["list-item"]
            if Random.bool():
                values.append(Random.choice(["block", "inline", "run-in"]))
            if Random.bool():
                values.append(Random.choice(["flow", "flow-root"]))
            self.value = cat(values)
        elif c == 2:
            self.value = Random.choice(["table-row-group", "table-header-group", "table-footer-group", "table-row",
                                        "table-cell", "table-column-group", "table-column", "table-caption"])
        elif c == 3:
            self.value = "contents"
        else:
            self.value = Random.choice(
                ["inline-block", "inline-list-item", "inline-table", "inline-flex", "inline-grid"])


# empty-cells
class EmptyCellsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["show", "hide"])


# flex
class FlexValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            if Random.bool():
                self.value = "auto"
            else:
                self.value = Random.number()
        elif c == 1:
            self.value = Random.number() + " " + flex_basis()
        else:
            self.value = Random.number() + " " + Random.number() + flex_basis()


# flex-basis
class FlexBasisValue(StaticValue):
    def generate(self, _):
        self.value = flex_basis()


# flex-direction
class FlexDirectionValue(StaticValue):
    def generate(self, _):
        self.value = flex_direction()


# flex-flow
class FlexFlowValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = flex_direction()
        elif c == 1:
            self.value = flex_wrap()
        else:
            self.value = flex_direction() + " " + flex_wrap()


# flex-wrap
class FlexWrapValue(StaticValue):
    def generate(self, _):
        self.value = flex_wrap()


# float
class FloatValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["left", "right", "inline-start", "inline-end", "none"])


def font_style():
    return Random.choice(["normal", "italic", "oblique"])


def font_size():
    c = Random.selector(3)
    if c == 0:
        return Random.choice(["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"])
    elif c == 1:
        return Random.choice(["larger", "smaller"])
    else:
        return dv.length_percentage(relative=True)


def font_family():
    def single():
        return Random.choice([
            "monospace",
            "Consolas",
            "'Liberation Mono'",
            "Menlo",
            "Courier",
            "sans-serif",
            "system-ui",
            "Times",
            "'Courier New'",
            "Arial",
            "Helvetica",
            "'Comic Sans MS'",
            "serif",
            "Verdana",
            "'Times New Roman'"
        ])
    num = Random.range(1, 2)
    return seq([single() for _ in range(num)])


# font
class FontValue(StaticValue):
    def generate(self, _):
        if Random.selector(5) == 0:
            self.value = Random.choice(["initial", "caption", "icon", "menu", "message-box",
                                        "small-caption", "status-bar"])
        else:
            selectors = Random.selectors(4)
            values = []
            if selectors[0]:
                values.append(font_style())
            if selectors[1]:
                values.append(dv.font_variant())
            if selectors[2]:
                values.append(dv.font_weight())
            if selectors[3]:
                values.append(dv.font_stretch())

            size = font_size()
            if Random.bool():
                size += " / " + line_height()
            values.append(size)
            values.append(font_family())
            self.value = cat(values)


# font-family
class FontFamilyValue(StaticValue):
    def generate(self, _):
        self.value = font_family()


# font-feature-settings
class FontFeatureSettingsValue(StaticValue):
    def generate(self, _):
        self.value = dv.font_feature_settings()


# font-smooth
class FontSmoothValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["auto", "never", "always"])
        else:
            self.value = dv.length()


# font-kerning
class FontKerningValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "normal"])


# font-size
class FontSizeValue(StaticValue):
    def generate(self, _):
        if Random.selector(10) == 0:
            self.value = "inherit"
        else:
            self.value = font_size()


# font-size-adjust
class FontSizeAdjustValue(StaticValue):
    def generate(self, _):
        self.value = Random.number()


# font-stretch
class FontStretchValue(StaticValue):
    def generate(self, _):
        self.value = dv.font_stretch()


# font-style
class FontStyleValue(StaticValue):
    def generate(self, _):
        if Random.selector(5) == 0:
            self.value = "inherit"
        else:
            self.value = font_style()


# font-variant
class FontVariantValue(StaticValue):
    def generate(self, _):
        self.value = dv.font_variant()


# font-variant-caps
class FontVariantCapsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(
            ["normal", "small-caps", "all-small-caps", "petite-caps", "all-petite-caps", "unicase", "titling-caps"])


# font-variant-ligatures
class FontVariantLigaturesValue(StaticValue):
    def generate(self, _):
        if Random.selector(5) == 0:
            self.value = "normal"
        else:
            selectors = Random.selectors(4)
            values = []
            if selectors[0]:
                values.append(Random.choice(["common-ligatures", "no-common-ligatures"]))
            if selectors[1]:
                values.append(Random.choice(["discretionary-ligatures", "no-discretionary-ligatures"]))
            if selectors[2]:
                values.append(Random.choice(["historical-ligatures", "no-historical-ligatures"]))
            if selectors[3]:
                values.append(Random.choice(["contextual", "no-contextual"]))
            self.value = cat(values)


# font-weight
class FontWeightValue(StaticValue):
    def generate(self, _):
        self.value = dv.font_weight()


def grid_template_rows():
    if Random.selector(5) == 0:
        return "auto"
    else:
        if Random.bool():
            return track_list()
        else:
            return auto_track_list()


def grid_template():
    return grid_template_rows() + " / " + grid_template_rows()


def grid_auto_rows():
    num = Random.range(1, 2)
    return cat([track_size() for _ in range(num)])


# grid
class GridValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = grid_template()
        elif c == 1:
            values = [grid_template_rows(), "/", "auto-flow"]
            if Random.bool():
                values.append("dense")
            if Random.bool():
                values.append(grid_auto_rows())
            self.value = cat(values)
        else:
            values = ["auto-flow"]
            if Random.bool():
                values.append("dense")
            if Random.bool():
                values.append(grid_auto_rows())
            values.extend(["/", grid_template_rows()])
            self.value = cat(values)


def grid_line():
    c = Random.selector(4)
    if c == 0:
        return "auto"
    elif c == 1:
        return Random.choice(["a", "b", "c"])
    elif c == 2:
        s = Random.integer()
        if Random.bool():
            s += " " + Random.choice(["a", "b", "c"])
        return s
    else:
        s = "span"
        if Random.bool():
            if Random.bool():
                s += " " + Random.integer()
            else:
                s += " " + Random.choice(["a", "b", "c"])
        return s


# grid-area
class GridAreaValue(StaticValue):
    def generate(self, _):
        values = [grid_line()]
        num = Random.range(0, 3)
        for _ in range(num):
            values.extend(["/", grid_line()])
        self.value = cat(values)


# grid-auto-rows, columns
class GridAutoRowsColumnsValue(StaticValue):
    def generate(self, _):
        self.value = grid_auto_rows()


# grid-auto-flow
class GridAutoFlowValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(Random.choice(["row", "column"]))
        if selectors[1]:
            values.append("dense")
        self.value = cat(values)


# grid-row, column
# TODO: custom-ident
class GridRowValue(StaticValue):
    def generate(self, _):
        values = [grid_line()]
        if Random.bool():
            values.extend(["/", grid_line()])
        self.value = cat(values)


# grid-column-end
class GridLineValue(StaticValue):
    def generate(self, _):
        self.value = grid_line()


# grid-column-gap
class GridLineGapValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["normal", "inherit"])
        else:
            self.value = dv.length_percentage(relative=True)


# grid-gap
class GridGapValue(StaticValue):
    def generate(self, _):
        self.value = dv.length_percentage()
        if Random.bool():
            self.value += " " + dv.length_percentage()


# grid-template
class GridTemplateValue(StaticValue):
    def generate(self, _):
        self.value = grid_template()


# grid-template-areas
class GridTemplateAreasValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice([
            "'a'", "'b'", "'c'",
            "'a b'", "'a a'", "'b c'",
            "'a a .'", "'a b b'",
            "'a b b' 'a c c'"
        ])


# grid-template-columns
class GridTemplateRowsColumnsValue(StaticValue):
    def generate(self, _):
        self.value = grid_template_rows()


# height / width
class HeightValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = dv.length_percentage(relative=True)
        elif c == 1:
            self.value = "fit-content({})".format(dv.length_percentage(relative=True))
        elif c == 2:
            self.value = Random.choice(["min-content", "max-content", "auto"])
        else:
            self.value = "auto"


# hyphens
class HyphensValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["manual", "auto", "none"])


# image-orientation
class ImageOrientationValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "from-image"
        elif c == 1:
            self.value = dv.angle()
        else:
            self.value = "flip"
            if Random.bool():
                self.value = dv.angle() + " " + self.value


# image-rendering
class ImageRenderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "smooth", "high-quality", "crisp-edges", "pixelated",
                                    "-webkit-optimize-contrast"])


# isolation
class IsolationValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "isolate"])


# justify-content
class JustifyContentValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "normal"
        elif c == 1:
            self.value = Random.choice(["space-between", "space-around", "space-evenly", "stretch"])
        else:
            self.value = Random.choice(["center", "start", "end", "flex-start", "flex-end", "left", "right"])
            if Random.bool():
                self.value = Random.choice(["unsafe", "safe"]) + " " + self.value


# justify-items
class JustifyItemsValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = Random.choice(["normal", "stretch", "legacy"])
        elif c == 1:
            self.value = "legacy {}".format(Random.choice(["left", "right", "center"]))
        elif c == 2:
            self.value = baseline_position()
        else:
            self.value = self_position() if Random.bool() else Random.choice(["left", "right"])
            if Random.bool():
                self.value = overflow_position() + " " + self.value


# justify-self
class JustifySelfValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = Random.choice(["normal", "stretch", "auto"])
        elif c == 1:
            self.value = baseline_position()
        else:
            self.value = self_position() if Random.bool() else Random.choice(["left", "right"])
            if Random.bool():
                self.value = overflow_position() + " " + self.value


# kerning
class KerningValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["auto", "normal"])
        else:
            self.value = dv.length()


# letter-spacing
class LetterSpacingValue(StaticValue):
    def generate(self, _):
        self.value = dv.length() if Random.bool() else "normal"


# line-break
class LineBreakValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "loose", "normal", "strict", "anywhere",
                                    "after-white-space", "before-white-space"])


class WebKitLocaleValue(StaticValue):
    def generate(self, _):
        self.value = "'zh_CN'"


# line-height
class LineHeightValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = "normal"
        elif c == 1:
            self.value = Random.number()
        elif c == 2:
            self.value = dv.length(relative=True)
        else:
            self.value = dv.percentage()


def list_style_image():
    return "url({})".format(dv.image_url())


def list_style_type():
    if Random.bool():
        return Random.choice(["disc", "disclosure-open", "disclosure-closed"])
    else:
        return Random.choice(
            ["circle", "square", "decimal", "cjk-decimal", "decimal-leading-zero", "lower-roman", "upper-roman",
             "lower-greek", "lower-alpha", "lower-latin", "upper-alpha", "upper-latin", "arabic-indic", "armenian",
             "bengali", "cambodian", "cjk-earthly-branch", "cjk-heavenly-stem", "cjk-ideographic", "devanagari",
             "ethiopic-numeric", "georgian", "gujarati", "gurmukhi", "hebrew", "hiragana", "hiragana-iroha",
             "japanese-formal", "japanese-informal", "kannada", "katakana", "katakana-iroha", "khmer",
             "korean-hangul-formal", "korean-hanja-formal", "korean-hanja-informal", "lao", "lower-armenian",
             "malayalam", "mongolian", "myanmar", "oriya", "persian", "simp-chinese-formal",
             "simp-chinese-informal", "tamil", "telugu", "thai", "tibetan", "trad-chinese-formal",
             "trad-chinese-informal", "upper-armenian"])


def list_style_position():
    return Random.choice(["inside", "outside"])


# list-style
class ListStyleValue(StaticValue):
    def generate(self, _):
        if Random.selector(10) == 0:
            self.value = "inherit"
        else:
            selectors = Random.selectors(3)
            values = []
            if selectors[0]:
                values.append(list_style_image())
            if selectors[1]:
                values.append(list_style_position())
            if selectors[2]:
                values.append(list_style_type())
            self.value = cat(values)


# list-style-image
class ListStyleImageValue(StaticValue):
    def generate(self, _):
        self.value = list_style_image()


# list-style-position
class ListStylePositionValue(StaticValue):
    def generate(self, _):
        self.value = list_style_position()


# list-style-type
class ListStyleTypeValue(StaticValue):
    def generate(self, _):
        self.value = list_style_type()


# margin
class MarginValue(StaticValue):
    def generate(self, _):
        def single():
            if Random.bool():
                return dv.length_percentage()
            else:
                return "auto"
        num = Random.range(1, 4)
        self.value = cat([single() for _ in range(num)])


# max-zoom
class MaxZoomValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.number_percentage()


# object-fit
class ObjectFitValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["fill", "contain", "cover", "scale-down"])


def offset_rotate():
    selectors = Random.selectors(2)
    values = []
    if selectors[0]:
        values.append(Random.choice(["auto", "reverse"]))
    if selectors[1]:
        values.append(dv.angle())
    return cat(values)


def offset_anchor():
    if Random.bool():
        return "auto"
    else:
        return dv.position()


# offset-anchor
class OffsetAnchorValue(StaticValue):
    def generate(self, _):
        self.value = offset_anchor()


# offset-position
class OffsetPositionValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.position()


# offset-rotate/ion
class OffsetRotateValue(StaticValue):
    def generate(self, _):
        self.value = offset_rotate()


def outline_color():
    if Random.bool():
        return dv.color()
    else:
        return "invert"


def outline_style():
    if Random.bool():
        return border_style()
    else:
        return "auto"


# outline
class OutlineValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(3)
        values = []
        if selectors[0]:
            values.append(outline_color())
        if selectors[1]:
            values.append(outline_style())
        if selectors[2]:
            values.append(line_width())
        self.value = cat(values)


# outline-color
class OutlineColorValue(StaticValue):
    def generate(self, _):
        self.value = outline_color()


# outline-style
class OutlineStyleValue(StaticValue):
    def generate(self, _):
        self.value = outline_style()


def overflow():
    return Random.choice(["visible", "hidden", "clip", "scroll", "auto"
                          "-webkit-paged-x", "-webkit-paged-y"])


# overflow
class OverflowValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([overflow() for _ in range(num)])


# overflow-anchor
class OverflowAnchorValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "none"])


# overflow-wrap
class OverflowWrapValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "break-word", "anywhere"])


# overflow-x
class OverflowXValue(StaticValue):
    def generate(self, _):
        self.value = overflow()


# padding
class PaddingValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([dv.length_percentage() for _ in range(num)])


# perspective
class PerspectiveValue(StaticValue):
    def generate(self, _):
        self.value = dv.length()


# perspective-origin
class PerspectiveOriginValue(StaticValue):
    def generate(self, _):
        values = []
        selectors = Random.selectors(2)
        if selectors[0]:
            if Random.bool():
                values.append(dv.length_percentage())
            else:
                values.append(Random.choice(["left", "center", "right"]))
        if selectors[1]:
            if Random.bool():
                values.append(dv.length_percentage())
            else:
                values.append(Random.choice(["top", "center", "bottom"]))
        self.value = cat(values)


# pointer-events
class PointerEventsValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "none"])


class PositionValue(StaticValue):
    def generate(self, _):
        self.value = dv.position()


# position
class PositionWayValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["static", "relative", "absolute", "sticky", "fixed"])


# prince-hyphens
class PrinceHyphensValue(StaticValue):
    def generate(self, _):
        self.value = "auto"


# quotes
class QuotesValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["auto", "none", "initial"])
        else:
            self.value = Random.choice([
                "'{' '}'",
                "'A' 'B' 'C' 'D'",
                "'-' '-'",
                "'(' ')' '[' ']'",
                "'a' 'b' 'c' 'd'",
                "'a' 'b'",
                "'a' 'v' 'b' 'u'",
            ])


# resize
class ResizeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["both", "horizontal", "vertical", "block", "inline"])


# rotate
class RotateValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.angle()
        else:
            c = Random.selector(4)
            if c == 0:
                self.value = "x"
            elif c == 1:
                self.value = "y"
            elif c == 2:
                self.value = "z"
            else:
                self.value = cat([Random.integer() for _ in range(3)])
            self.value += " " + dv.angle()


# scale
class ScaleValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 3)
        self.value = cat([Random.number() for _ in range(num)])


# scroll-behavior
class ScrollBehaviorValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "smooth"])


# scroll-snap-coordinate
class ScrollSnapCoordinateValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = seq([dv.position() for _ in range(num)])


# scroll-snap-points-x
class ScrollSnapPointsXValue(StaticValue):
    def generate(self, _):
        self.value = "repeat({})".format(dv.length_percentage())


# scroll-snap-type
class ScrollSnapTypeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["x", "y", "block", "inline", "both"])
        if Random.bool():
            self.value += " " + Random.choice(["mandatory", "proximity"])


# shape-image-threshold
class ShapeImageThresholdValue(StaticValue):
    def generate(self, _):
        self.value = alpha()


# shape-outside
class ShapeOutsideValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            selectors = Random.selectors(2)
            values = []
            if selectors[0]:
                values.append(shape_box())
            if selectors[1]:
                values.append(basic_shape())
            self.value = cat(values)
        else:
            self.value = image()


# table-layout
class TableLayoutValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "fixed"])


# text-align
class TextAlignValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["start", "end", "left", "right", "center", "justify", "match-parent"])


# text-align-last
class TextAlignLastValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "start", "end", "left", "right", "center", "justify"])


# text-combine-upright
class TextCombineUprightValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "all"
        else:
            values = ["digits"]
            if Random.bool():
                values.append(Random.integer())
            self.value = cat(values)


def text_decoration_line():
    selectors = Random.selectors(4)
    values = []
    if selectors[0]:
        values.append("underline")
    if selectors[1]:
        values.append("overline")
    if selectors[2]:
        values.append("line-through")
    if selectors[3]:
        values.append("blink")
    return cat(values)


def text_decoration_style():
    return Random.choice(["solid", "double", "dotted", "dashed", "wavy"])


def text_decoration_thickness():
    if Random.bool():
        return Random.choice(["auto", "from-font"])
    else:
        return dv.length()


# text-decoration
class TextDecorationValue(StaticValue):

    def generate(self, _):
        selectors = Random.selectors(4)
        values = []
        if selectors[0]:
            values.append(text_decoration_line())
        if selectors[1]:
            values.append(dv.color())
        if selectors[2]:
            values.append(text_decoration_style())
        if selectors[3]:
            values.append(text_decoration_thickness())
        self.value = cat(values)


# text-decoration-line
class TextDecorationLineValue(StaticValue):
    def generate(self, _):
        self.value = text_decoration_line()


# text-decoration-skip
class TextDecorationSkipValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(4)
        values = []
        if selectors[0]:
            values.append("objects")
        if selectors[1]:
            c = Random.selector(3)
            if c == 0:
                values.append("spaces")
            elif c == 1:
                values.append("leading-spaces")
            else:
                values.append("trailing-spaces")
        if selectors[2]:
            values.append("edges")
        if selectors[3]:
            values.append("box-decoration")
        self.value = cat(values)


# text-decoration-style
class TextDecorationStyleValue(StaticValue):
    def generate(self, _):
        self.value = text_decoration_style()


# text-decoration-thickness
class TextDecorationThicknessValue(StaticValue):
    def generate(self, _):
        self.value = text_decoration_thickness()


# text-indent
class TextIndentValue(StaticValue):
    def generate(self, _):
        values = [dv.length_percentage(relative=True)]
        if Random.bool():
            values.append("hanging")
        if Random.bool():
            values.append("each-line")
        self.value = cat(values)


# text-justify
class TextJustifyValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "inter-character", "inter-word", "distribute"])


# text-orientation
class TextOrientationValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["inherit", "initial", "mixed", "upright", "sideways", "sideways-right"])


# text-overflow
class TextOverflowValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["clip", "ellipsis"])


# text-rendering
class TextRenderingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"])


# text-shadow
class TextShadowValue(StaticValue):
    def generate(self, _):
        if Random.selector(10) == 0:
            self.value = "inherit"
        else:
            selectors = Random.selectors(4)
            values = []
            if selectors[0]:
                values.append(dv.color())
            if selectors[1]:
                values.append(dv.length())
            if selectors[2]:
                values.append(dv.length())
            if selectors[3]:
                values.append(dv.length())
            self.value = cat(values)


# text-transform
class TextTransformValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["none", "capitalize", "uppercase", "lowercase", "full-width", "full-size-kana"])


def text_underline_position():
    return Random.choice(["auto", "before-edge", "alphabetic", "after-edge"])


def text_underline_mode():
    return Random.choice(["continuous", "skip-white-space"])


def text_underline_style():
    return Random.choice(["solid", "double", "dotted", "dashed", "dot-dash", "dot-dot-dash", "wave"])


def text_underline_width():
    c = Random.selector(6)
    if c == 0:
        return "auto"
    elif c == 1:
        return "normal"
    elif c == 2:
        return Random.number()
    elif c == 3:
        return dv.length()
    elif c == 4:
        return dv.percentage()
    else:
        return Random.choice(["thin", "medium", "thick"])


# text-underline
class TextUnderlineValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(4)
        values = []
        if selectors[0]:
            values.append(text_underline_style())
        if selectors[1]:
            values.append(dv.color())
        if selectors[2]:
            values.append(text_underline_mode())
        if selectors[3]:
            values.append(text_underline_position())
        self.value = cat(values)


# text-underline-mode
class TextUnderlineModeValue(StaticValue):
    def generate(self, _):
        self.value = text_underline_mode()


# text-underline-style
class TextUnderlineStyleValue(StaticValue):
    def generate(self, _):
        self.value = text_underline_style()


# text-underline-width
class TextUnderlineWidthValue(StaticValue):
    def generate(self, _):
        self.value = text_underline_width()


# text-underline-offset
class TextUnderlineOffsetValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.length()


# text-underline-position
class TextUnderlinePositionValue(StaticValue):
    def generate(self, _):
        self.value = text_underline_position()


# touch-action
class TouchActionValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            selectors = Random.selectors(3)
            values = []
            if selectors[0]:
                values.append(Random.choice(["pan-x", "pan-left", "pan-right"]))
            if selectors[1]:
                values.append(Random.choice(["pan-y", "pan-up", "pan-down"]))
            if selectors[2]:
                values.append("pinch-zoom")
            self.value = cat(values)
        else:
            self.value = Random.choice(["auto", "manipulation"])


def css_transform():
    c = Random.selector(21)
    if c == 0:
        return dv.matrix()
    elif c == 1:
        return dv.translate()
    elif c == 2:
        return dv.translate_x()
    elif c == 3:
        return dv.translate_y()
    elif c == 4:
        return dv.scale()
    elif c == 5:
        return dv.scale_x()
    elif c == 6:
        return dv.scale_y()
    elif c == 7:
        return dv.rotate()
    elif c == 8:
        return dv.skew()
    elif c == 9:
        return dv.skew_x()
    elif c == 10:
        return dv.skew_y()
    elif c == 11:
        return dv.matrix3d()
    elif c == 12:
        return dv.translate3d()
    elif c == 13:
        return dv.translate_z()
    elif c == 14:
        return dv.scale3d()
    elif c == 15:
        return dv.scale_z()
    elif c == 16:
        return dv.rotate3d()
    elif c == 17:
        return dv.rotate_x()
    elif c == 18:
        return dv.rotate_y()
    elif c == 19:
        return dv.rotate_z()
    else:
        return dv.perspective()


# transform
class TransformValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([css_transform() for _ in range(num)])


# transform-origin
class TransformOriginValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            if Random.bool():
                self.value = Random.choice(["left", "center", "right", "top", "bottom"])
            else:
                self.value = dv.length_percentage()
        else:
            values = []
            if Random.bool():
                values.append(Random.choice(["left", "center", "right"]))
            else:
                values.append(dv.length_percentage())
            if Random.bool():
                values.append(Random.choice(["top", "center", "bottom"]))
            else:
                values.append(dv.length_percentage())
            if Random.bool():
                values.append(dv.length())
            self.value = cat(values)


# transform-style
class TransformStyleValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["flat", "preserve-3d"])


def transition_property():
    if Random.bool():
        return "all"
    else:
        return Random.choice(docs.css_animatable_properties)


def transition():
    selectors = Random.selectors(3)
    values = [transition_property()]
    if selectors[0]:
        values.append(dv.clock())
    if selectors[1]:
        values.append(animation_timing_function())
    if selectors[2]:
        values.append(dv.clock())
    return cat(values)


# transition
class TransitionValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = seq([transition() for _ in range(num)])


# transition-property
class TransitionPropertyValue(StaticValue):
    def generate(self, _):
        self.value = transition_property()


# transition-timing-function
class TransitionTimingFunctionValue(StaticValue):
    def generate(self, _):
        self.value = animation_timing_function()


# translate
class TranslateValue(StaticValue):
    def generate(self, _):
        selectors = Random.selectors(2)
        values = []
        if selectors[0]:
            values.append(dv.length_percentage())
        if selectors[1]:
            values.append(dv.length_percentage())
            if Random.bool():
                values.append(dv.length())
        self.value = cat(values)


# unicode-bidi
class UnicodeBidiValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "embed", "isolate", "bidi-override", "isolate-override", "plaintext"])


# user-select
class UserSelectValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["all", "element", "elements", "text", "toggle"])


# user-zoom
class UserZoomValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["zoom", "fixed"])


# vertical-align
class VerticalAlignValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["baseline", "sub", "super", "text-top", "text-bottom", "middle", "top",
                                        "bottom"])
        else:
            self.value = dv.length_percentage(relative=True)


# visibility
class VisibilityValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["visible", "hidden", "collapse"])


# white-space
class WhiteSpaceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "pre", "nowrap", "pre-wrap", "pre-line"])


# will-change
class WillChangeValue(StaticValue):
    def generate(self, _):
        def single():
            if Random.bool():
                return Random.choice(["scroll-position", "contents"])
            else:
                return Random.choice(docs.css_animatable_properties)
        if Random.selector(10) == 0:
            self.value = "auto"
        else:
            num = Random.range(1, 2)
            self.value = seq([single() for _ in range(num)])


# word-break
class WordBreakValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["normal", "break-all", "keep-all", "break-word"])


# word-spacing
class WordSpacingValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "normal"
        else:
            self.value = dv.length_percentage()


# writing-mode
class WritingModeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(
            ["horizontal-tb", "vertical-rl", "vertical-lr", "sideways-rl", "sideways-lr", "lr", "lr-tb", "rl", "tb",
             "tb-rl"])


# z-index
class ZIndexValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = Random.integer()


# zoom
class ZoomValue(StaticValue):
    def generate(self, _):
        c = Random.selector(3)
        if c == 0:
            self.value = "normal"
        elif c == 1:
            self.value = "reset"
        else:
            self.value = dv.number_percentage()


# -webkit-text-decorations-in-effect
class WebkitTextDecorationInEffectValue(StaticValue):
    def generate(self, _):
        self.value = "underline"


# caret-color
class CaretColorValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = dv.color()


# font-variation-settings
class FontVariationSettingsValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "normal"
        else:
            axis_tag = Random.choice(["XHGT", "wght", "wdth", "slnt", "ital", "opsz"])
            self.value = cat([axis_tag, Random.number()])


# inset
class InsetValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([location() for _ in range(num)])


# inset-block
class InsetBlockValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([location() for _ in range(num)])


# inset-inline
class InsetInlineValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([location() for _ in range(num)])


# mask-border (border-image)
class MaskBorderValue(StaticValue):
    @staticmethod
    def mask_border_mode():
        return Random.choice(["luminance", "alpha"])

    def generate(self, _):
        selectors = Random.selectors(5)
        values = []
        if selectors[0]:
            values.append(image())
        if selectors[1]:
            values.append(border_image_slice())
        if selectors[2]:
            values.extend(["/", border_image_width()])
            if Random.bool():
                values.extend(["/", border_image_outset()])
        if selectors[3]:
            values.append(border_image_repeat())
        if selectors[4]:
            values.append(MaskBorderValue.mask_border_mode())
        self.value = cat(values)


class MaskBorderModeValue(StaticValue):
    def generate(self, _):
        self.value = MaskBorderValue.mask_border_mode()


# scroll-margin
class ScrollMarginValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([dv.length() for _ in range(num)])


# scroll-margin-block
class ScrollMarginBlockValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([dv.length() for _ in range(num)])


# scroll-margin-inline
class ScrollMarginInlineValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([dv.length() for _ in range(num)])


def single_scroll_padding():
    if Random.bool():
        return "auto"
    else:
        return dv.length_percentage()


# scroll-padding
class ScrollPaddingValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 4)
        self.value = cat([single_scroll_padding() for _ in range(num)])


# scroll-padding-block
class ScrollPaddingBlockValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([single_scroll_padding() for _ in range(num)])


# scroll-padding-block-start/end
# scroll-padding-inline-start/end
# scroll-padding-bottom/top/left/right
class ScrollPaddingLineValue(StaticValue):
    def generate(self, _):
        self.value = single_scroll_padding()


# scroll-padding-inline
class ScrollPaddingInlineValue(StaticValue):
    def generate(self, _):
        num = Random.range(1, 2)
        self.value = cat([single_scroll_padding() for _ in range(num)])


# scrollbar-color
class ScrollbarColorValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.choice(["auto", "dark", "light"])
        else:
            self.value = cat([dv.color() for _ in range(2)])


# animation: https://developer.mozilla.org/en-US/docs/Web/CSS/animation
class AnimationValue(StaticValue):
    def generate(self, context):
        values = [animation_name(context)]
        c = Random.selectors(7)
        if c[0]:
            values.append(animation_duration())
        if c[1]:
            values.append(animation_timing_function())
        if c[2]:
            values.append(animation_delay())
        if c[3]:
            values.append(animation_iteration_count())
        if c[4]:
            values.append(animation_direction())
        if c[5]:
            values.append(animation_fill_mode())
        if c[6]:
            values.append(dv.play_state())
        self.value = cat(values)


# animation-name
class AnimationNameValue(StaticValue):
    def generate(self, context):
        self.value = animation_name(context)


# counter-increment
class CounterIncrementValue(StaticValue):
    def generate(self, context):
        self.value = context.get_token("counter")
        if Random.bool():
            self.value += " " + Random.integer()


class CursorValue(StaticValue):
    def generate(self, context):
        if Random.bool():
            self.value = cursor_fallback()
        else:
            self.value = "url({})".format(dv.image_url())


#####################################
# Dynamic CSS values
#####################################
class ClipPathValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.clip_path = None
        self.value = None

    def generate_dynamic(self, context):
        self.value = None
        self.clip_path = context.get_object(["SVGClipPathElement"])
        if self.clip_path is None:
            self.generate_static()

    def generate_static(self):
        self.clip_path = None
        self.value = basic_shape()
        if Random.bool():
            self.value += " " + geometry_box()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.clip_path is not None and self.clip_path in merge_map:
            self.clip_path = merge_map[self.clip_path]

    def __str__(self):
        if self.clip_path is not None:
            return "url(#{})".format(self.clip_path.id)
        else:
            return self.value


class OffsetValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.path = None
        self.path_value = None

        self.position = None
        self.distance = None
        self.rotate = None
        self.anchor = None

    def generate_static_path(self):
        self.path = None
        c = Random.selector(3)
        if c == 0:
            s = dv.angle()
            if Random.bool():
                s += " " + radial_gradient_size()
            if Random.bool():
                s += " contain"
            self.path_value = "ray({})".format(s)
        elif c == 1:
            self.path_value = "path('{}')".format(dv.path())
        else:
            self.path_value = basic_shape()
            if Random.bool():
                self.path_value += " " + geometry_box()

    def generate_dynamic_path(self, context):
        self.path_value = None
        self.path = context.get_object(docs.svg_shape_elements)
        if self.path is None:
            self.generate_static_path()

    def generate_path(self, context):
        if Random.bool():
            self.generate_static_path()
        else:
            self.generate_dynamic_path(context)

    def generate_position(self):
        self.position = dv.position() if Random.bool() else None

    def generate_distance(self):
        self.distance = dv.length_percentage() if Random.bool() else None

    def generate_rotate(self):
        self.rotate = offset_rotate() if Random.bool() else None

    def generate_anchor(self):
        self.anchor = offset_anchor() if Random.bool() else None

    def generate(self, context):
        self.generate_position()
        self.generate_path(context)
        if Random.bool():
            self.generate_distance()
            self.generate_rotate()
        self.generate_anchor()

    def mutate(self, context) -> bool:
        c = Random.selector(5)
        if c == 0:
            self.generate_position()
        elif c == 1:
            self.generate_path(context)
        elif c == 2:
            self.generate_distance()
        elif c == 3:
            self.generate_rotate()
        else:
            self.generate_anchor()
        return True

    def merge_fix(self, merge_map):
        if self.path is not None and self.path in merge_map:
            self.path = merge_map[self.path]

    def __str__(self):
        values = []
        if self.position is not None:
            values.append(self.position)
        if self.path is not None:
            values.append("url(#{})".format(self.path.id))
        else:
            values.append(self.path_value)
        if self.distance is not None:
            values.append(self.distance)
        if self.rotate is not None:
            values.append(self.rotate)
        if self.anchor is not None:
            values.extend(["/", self.anchor])
        return cat(values)


# offset-path
class OffsetPathValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.path = None
        self.value = None

    def generate_static(self):
        self.path = None
        c = Random.selector(3)
        if c == 0:
            s = dv.angle()
            if Random.bool():
                s += " " + radial_gradient_size()
            if Random.bool():
                s += " contain"
            self.value = "ray({})".format(s)
        elif c == 1:
            self.value = "path('{}')".format(dv.path())
        else:
            self.value = basic_shape()
            if Random.bool():
                self.value += " " + geometry_box()

    def generate_dynamic(self, context):
        self.value = None
        self.path = context.get_object(docs.svg_shape_elements)
        if self.path is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.path is not None and self.path in merge_map:
            self.path = merge_map[self.path]

    def __str__(self):
        if self.path is not None:
            return "url(#{})".format(self.path.id)
        return self.value


# filter
class FilterValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.filter = None
        self.filter_value = None

    def generate_static(self):
        self.filter = None
        num = Random.range(1, 2)
        self.filter_value = cat([filter_function() for _ in range(num)])

    def generate_dynamic(self, context):
        self.filter_value = None
        self.filter = context.get_object(["SVGFilterElement"])
        if self.filter is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.filter is not None and self.filter in merge_map:
            self.filter = merge_map[self.filter]

    def __str__(self):
        if self.filter is not None:
            return "url(#{})".format(self.filter.id)
        else:
            return self.filter_value


class MaskValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.mask = None
        self.image_value = None

        self.position = None
        self.repeat = None
        self.origin = None
        self.clip = None
        self.composite = None
        self.mode = None

    def generate_mask_static(self):
        self.mask = None
        self.image_value = image()

    def generate_mask_dynamic(self, context):
        self.image_value = None
        self.mask = context.get_object(["SVGMaskElement"])
        if self.mask is None:
            self.generate_mask_static()

    def generate_mask(self, context):
        if Random.bool():
            self.generate_mask_static()
        else:
            self.generate_mask_dynamic(context)

    def generate_position(self):
        if Random.bool():
            self.position = None
        else:
            self.position = dv.position()
            if Random.bool():
                self.position += " / " + background_size()

    def generate_repeat(self):
        self.repeat = mask_repeat_style() if Random.bool() else None

    def generate_origin(self):
        self.origin = geometry_box() if Random.bool() else None

    def generate_clip(self):
        self.clip = mask_clip() if Random.bool() else None

    def generate_composite(self):
        self.composite = mask_composite() if Random.bool() else None

    def generate_mode(self):
        self.mode = mask_mode() if Random.bool() else None

    def generate(self, context):
        self.generate_mask(context)
        self.generate_position()
        self.generate_repeat()
        self.generate_origin()
        self.generate_clip()
        self.generate_composite()
        self.generate_mode()

    def mutate(self, context) -> bool:
        c = Random.selector(7)
        if c == 0:
            self.generate_mask(context)
        elif c == 1:
            self.generate_position()
        elif c == 2:
            self.generate_repeat()
        elif c == 3:
            self.generate_origin()
        elif c == 4:
            self.generate_clip()
        elif c == 5:
            self.generate_composite()
        else:
            self.generate_mode()
        return True

    def merge_fix(self, merge_map):
        if self.mask is not None and self.mask in merge_map:
            self.mask = merge_map[self.mask]

    def __str__(self):
        values = []
        if self.mask is not None:
            values.append("url(#{})".format(self.mask.id))
        else:
            values.append(self.image_value)
        if self.position is not None:
            values.append(self.position)
        if self.repeat is not None:
            values.append(self.repeat)
        if self.origin is not None:
            values.append(self.origin)
        if self.clip is not None:
            values.append(self.clip)
        if self.composite is not None:
            values.append(self.composite)
        if self.mode is not None:
            values.append(self.mode)
        return cat(values)


# mask-image
class MaskImageValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.mask = None
        self.image_value = None

    def generate_static(self):
        self.mask = None
        self.image_value = image()

    def generate_dynamic(self, context):
        self.image_value = None
        self.mask = context.get_object(["SVGMaskElement"])
        if self.mask is None:
            self.generate_static()

    def generate(self, context):
        if Random.bool():
            self.generate_static()
        else:
            self.generate_dynamic(context)

    def merge_fix(self, merge_map):
        if self.mask is not None and self.mask in merge_map:
            self.mask = merge_map[self.mask]

    def __str__(self):
        if self.mask is not None:
            return "url(#{})".format(self.mask.id)
        else:
            return self.image_value
