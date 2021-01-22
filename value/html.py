from value import StaticValue, DynamicValue, ConstValueWrapper
from object import get_object_id
from utils import dom_value as dv
from utils import cat
from utils.random import Random
import docs


#############################################
# Static values
#############################################
class ShapeValue(StaticValue):
    def generate(self, _):
        self.value = dv.shape()


class CoordsValue(StaticValue):
    def generate(self, _):
        self.value = dv.coords()


# <image>.href
class ImageSrcValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.image_url()
        else:
            self.value = "x"


class LangValue(StaticValue):
    def generate(self, _):
        self.value = dv.lang()


class ReferrerPolicyValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["no-referrer", "no-referrer-when-downgrade", "same-origin", "origin",
                                    "strict-origin", "origin-when-cross-origin", "strict-origin-when-cross-origin",
                                    "unsafe-url"])


class AcceptValue(StaticValue):
    def generate(self, _):
        self.value = dv.accept()


class PreloadValue(StaticValue):
    def generate(self, _):
        self.value = dv.preload()


class VideoSrcValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.video_url()
        else:
            self.value = "x"


class AudioSrcValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.audio_url()
        else:
            self.value = "x"


class FrameSrcValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.frame_url()
        else:
            self.value = "x"


class SoundLoopValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "infinite"
        else:
            self.value = Random.integer()


class AutoCapitalizeValue(StaticValue):
    def generate(self, _):
        self.value = dv.auto_capitalize()


class ButtonTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.button_type()


class CaptionAlignValue(StaticValue):
    def generate(self, _):
        self.value = dv.caption_align()


class TableAlignValue(StaticValue):
    def generate(self, _):
        self.value = dv.table_align()


class VAlignValue(StaticValue):
    def generate(self, _):
        self.value = dv.valign()


class CommandTypeValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["command", "checkbox", "radio"])


class TrackSrcValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = "x"
        else:
            self.value = dv.track_url()


class MediaSrcValue(StaticValue):
    def generate(self, _):
        c = Random.selector(4)
        if c == 0:
            self.value = "x"
        elif c == 1:
            self.value = dv.image_url()
        elif c == 2:
            self.value = dv.audio_url()
        else:
            self.value = dv.video_url()


class ImportanceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "low", "high"])


class LoadingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["eager", "lazy"])


class DirValue(StaticValue):
    def generate(self, _):
        self.value = dv.dir_()


class DropZoneValue(StaticValue):
    def generate(self, _):
        self.value = dv.drop_zone()


class InputModeValue(StaticValue):
    def generate(self, _):
        self.value = dv.input_mode()


class FormEncTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.form_enc_type()


class FormMethodValue(StaticValue):
    def generate(self, _):
        self.value = dv.form_method()


class AlignValue(StaticValue):
    def generate(self, _):
        self.value = dv.align()


class ObjectAlignValue(StaticValue):
    def generate(self, _):
        self.value = dv.object_align()


class SizesValue(StaticValue):
    def generate(self, _):
        def single():
            return "{}x{}".format(Random.integer(), Random.integer())
        num = Random.range(1, 2)
        self.value = cat([single() for _ in range(num)])


class ScrollingValue(StaticValue):
    def generate(self, _):
        self.value = dv.scrolling()


class ImageDecodingValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["auto", "sync", "async"])


class IntrinsicSizeValue(StaticValue):
    def generate(self, _):
        self.value = "{} x {}".format(Random.integer(), Random.integer())


class InputTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.input_type()


class AutoCompleteValue(StaticValue):
    def generate(self, _):
        self.value = dv.auto_complete()


class InputCaptureValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["user", "environment"])


class KeyTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.key_type()


class NumberingTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.numbering_type()


class LinkAsValue(StaticValue):
    def generate(self, _):
        self.value = dv.link_as()


class RelValue(StaticValue):
    def generate(self, _):
        self.value = dv.rel()


class RevValue(StaticValue):
    def generate(self, _):
        self.value = dv.rev()


class MarqueeBehaviorValue(StaticValue):
    def generate(self, _):
        self.value = dv.marquee_behavior()


class MarqueeDirectionValue(StaticValue):
    def generate(self, _):
        self.value = dv.marquee_direction()


class MarqueeLoopValue(StaticValue):
    def generate(self, _):
        self.value = dv.marquee_loop()


class MenuItemTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.menu_item_type()


class MetaSchemeValue(StaticValue):
    def generate(self, _):
        self.value = dv.meta_scheme()


class MenuTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.menu_type()


class ParamValueTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.param_value_type()


class WrapValue(StaticValue):
    def generate(self, _):
        self.value = dv.wrap()


class SrcSetValue(StaticValue):
    def generate(self, _):
        self.value = dv.srcset()


class TableFrameValue(StaticValue):
    def generate(self, _):
        self.value = dv.table_frame()


class TableRulesValue(StaticValue):
    def generate(self, _):
        self.value = dv.table_rules()


class TableScopeValue(StaticValue):
    def generate(self, _):
        self.value = dv.table_scope()


class TrackKindValue(StaticValue):
    def generate(self, _):
        self.value = dv.track_kind()


class UListTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.ulist_type()


class VideoControlsListValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["nodownload", "nofullscreen", "noremoteplayback"])


class TabIndexValue(StaticValue):
    def generate(self, _):
        self.value = dv.tab_index()


class CharsetValue(StaticValue):
    def generate(self, _):
        self.value = dv.charset()


class ClearValue(StaticValue):
    def generate(self, _):
        self.value = dv.clear()


# ARIA
class AriaAutocompleteValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["inline", "list", "both"])


class AriaCheckedValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false", "mixed", "undefined"])


class AriaCurrentValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false", "page", "step", "location", "date", "time"])


class AriaDropeffectValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["copy", "execute", "link", "move", "popup"])


class AriaExpandedValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false"])


class AriaGrabbedValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false"])


class AriaHaspopupValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false", "menu", "listbox", "tree", "grid", "dialog"])


class AriaHiddenValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false"])


class AriaInvalidValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["true", "false", "grammar", "spelling"])


class AriaLabelValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["", "face", "left-eye", "right-eye", "nose", "smile"])


class AriaLiveValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["assertive", "off", "polite"])


class AriaOrientationValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["horizontal", "vertical"])


class AriaPressedValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["false", "mixed", "true"])


class AriaRelevantValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["additions", "additions text", "all", "removals", "text"])


class AriaSelectedValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["false", "true"])


class AriaSortValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["ascending", "descending", "other"])


class RoleValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(
            ["treegrid", "checkbox", "radiogroup", "text", "menuitemcheckbox", "spinbutton", "radio", "slider", "tab",
             "listbox", "checkbox", "textbox", "group", "log", "img", "combobox", "columnheader", "tooltip", "note",
             "application", "listitem", "row", "presentation", "menuitem", "searchbox", "treeitem", "status", "main",
             "rowheader", "option", "form", "complementary", "gridcell", "contentinfo", "alert", "alertdialog",
             "link", "article", "banner", "toolbar", "menuitemradio", "definition", "search", "dom", "tree",
             "marquee", "menubar", "button", "list", "timer", "progressbar", "scrollbar", "separator", "math", "dialog",
             "menu", "directory", "grid", "tablist", "region", "navigation", "heading", "tabpanel", "unknown"])


class DateTimeValue(StaticValue):
    def generate(self, _):
        self.value = dv.date_time()


class ClassValue(StaticValue):
    def generate(self, context):
        self.value = context.get_token("class")


class PartValue(StaticValue):
    # FIXME: multiple part names
    def generate(self, context):
        self.value = context.get_token("part")


class RadioGroupValue(StaticValue):
    def generate(self, context):
        self.value = context.get_token("radiogroup")


class TableAxisValue(StaticValue):
    def generate(self, context):
        self.value = context.get_token("axis")


class MediaTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.media_type()


class CSSTypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.css_type()


class MIMETypeValue(StaticValue):
    def generate(self, _):
        self.value = dv.mime_type()


class MediaQueryValue(StaticValue):
    def generate(self, _):
        self.value = dv.media_query()


class NonceValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["A", "B", "C"])


#############################################
# Dynamic values
#############################################
class SlotValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.slot = None

    def generate(self, context):
        self.slot = context.get_object(["HTMLSlotElement"])

    def merge_fix(self, merge_map):
        if self.slot is not None and self.slot in merge_map:
            self.slot = merge_map[self.slot]

    def __str__(self):
        if self.slot is None:
            return "foo"
        return self.slot.id


class UseMapValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.map = None

    def generate(self, context):
        self.map = context.get_object(["HTMLMapElement"])

    def merge_fix(self, merge_map):
        if self.map is not None and self.map in merge_map:
            self.map = merge_map[self.map]

    def __str__(self):
        if self.map is None:
            return "#foo"
        return "#{}".format(self.map.id)


DummyUrlValue = ConstValueWrapper("x")


class ElementIDValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.elem = None

    def generate(self, context):
        self.elem = context.get_object(docs.elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is None:
            return "foo"
        return self.elem.id


class EventHandlerValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.eh = None

    def generate(self, context):
        self.eh = context.get_object(["EventHandler"])

    def mutate(self, _) -> bool:
        return False

    def merge_fix(self, merge_map):
        if self.eh is not None and self.eh in merge_map:
            self.eh = merge_map[self.eh]

    def __str__(self):
        return self.eh.id


class CallEventHandlerValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.eh = None

    def generate(self, context):
        self.eh = context.get_object(["EventHandler"])

    def mutate(self, _) -> bool:
        return False

    def merge_fix(self, merge_map):
        if self.eh is not None and self.eh in merge_map:
            self.eh = merge_map[self.eh]

    def __str__(self):
        return "{}()".format(self.eh.id)


class ContextMenuValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.menu = None

    def generate(self, context):
        self.menu = context.get_object(["HTMLMenuElement"])

    def merge_fix(self, merge_map):
        if self.menu is not None and self.menu in merge_map:
            self.menu = merge_map[self.menu]

    def __str__(self):
        if self.menu is None:
            return "foo"
        return self.menu.id


class FormValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.form = None

    def generate(self, context):
        self.form = context.get_object(["HTMLFormElement"])

    def merge_fix(self, merge_map):
        if self.form is not None and self.form in merge_map:
            self.form = merge_map[self.form]

    def __str__(self):
        if self.form is None:
            return "foo"
        return self.form.id


class ContentSelectValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.cla = None
        self.elem = None

    def generate(self, context):
        if Random.bool():
            self.cla = context.get_token("class")
            self.elem = None
        else:
            self.cla = None
            self.elem = context.get_object(docs.elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.cla is not None:
            return ".{}".format(self.cla)
        elif self.elem is not None:
            return "#{}".format(self.elem.id)
        else:
            return "#foo"


class ListValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.dl = None

    def generate(self, context):
        self.dl = context.get_object(["HTMLDataListElement"])

    def merge_fix(self, merge_map):
        if self.dl is not None and self.dl in merge_map:
            self.dl = merge_map[self.dl]

    def __str__(self):
        if self.dl is None:
            return "foo"
        return self.dl.id


class LabelForValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.elem = None

    def generate(self, context):
        self.elem = context.get_object(docs.html_labelable_elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is None:
            return "foo"
        return self.elem.id


class CommandValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.command = None

    def generate(self, context):
        self.command = context.get_object(["HTMLCommandElement"])

    def merge_fix(self, merge_map):
        if self.command is not None and self.command in merge_map:
            self.command = merge_map[self.command]

    def __str__(self):
        if self.command is None:
            return "foo"
        return self.command.id


class ElementIDListValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.elements = []

    def append_element(self, context):
        element = context.get_object(docs.elements)
        if (element is not None) and (element not in self.elements):
            self.elements.append(element)

    def generate(self, context):
        self.append_element(context)

    def mutate(self, context) -> bool:
        if len(self.elements) == 0 or Random.bool():
            # 1. add one
            self.append_element(context)
        else:
            # 2. replace one
            del self.elements[Random.selector(len(self.elements))]
            self.append_element(context)
        return True

    def merge_fix(self, merge_map):
        for i in range(len(self.elements)):
            if self.elements[i] in merge_map:
                self.elements[i] = merge_map[self.elements[i]]

    def __str__(self):
        return cat(list(map(get_object_id, self.elements)))


class TableHeadersValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.ths = []

    def append_th(self, context):
        elem = context.get_object(["HTMLTableHeaderCellElement"])
        if (elem is not None) and (elem not in self.ths):
            self.ths.append(elem)

    def generate(self, context):
        self.append_th(context)

    def mutate(self, context) -> bool:
        if len(self.ths) == 0 or Random.bool():
            # 1. add one
            self.append_th(context)
        else:
            # 2. replace one
            del self.ths[Random.selector(len(self.ths))]
            self.append_th(context)
        return True

    def merge_fix(self, merge_map):
        for i in range(len(self.ths)):
            if self.ths[i] in merge_map:
                self.ths[i] = merge_map[self.ths[i]]

    def __str__(self):
        return cat(list(map(get_object_id, self.ths)))


class TargetValue(DynamicValue):
    def __init__(self):
        super().__init__()
        self.frame = None

    def generate(self, context):
        self.frame = context.get_object(["HTMLFrameElement", "HTMLIFrameElement"])

    def merge_fix(self, merge_map):
        if self.frame is not None and self.frame in merge_map:
            self.frame = merge_map[self.frame]

    def __str__(self):
        if self.frame is None:
            return "foo"
        return self.frame.id
