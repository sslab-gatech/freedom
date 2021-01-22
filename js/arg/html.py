from config import CSSConfig
from css import get_css_property, get_css_property_name, get_css_property_value
from css.rule import CSSStyleRule, CSSKeyframeRule
from css.selector import create_css_selector
from css.declaration import CSSStyleDeclaration
from js.arg import Arg, ObjectArg, ValueArg, StringSetArgWrapper, StringArg, RangedIntegerArg, ConstStringArgWrapper
from object import get_object_id
from utils import cat, stringify
from utils import dom_value as dv
from utils.random import Random
import docs


#############################################
# HTML global objects
#############################################
# We confuse Node with Element like domato,
# which does not matter regarding fuzzing.
class DocumentArg(ObjectArg):
    name = "Document"


class WindowArg(ObjectArg):
    name = "Window"


class DOMTokenListArg(ObjectArg):
    name = "DOMTokenList"


class URLArg(ObjectArg):
    name = "URL"


class FormDataArg(ObjectArg):
    name = "FormData"


class URLSearchParamsArg(ObjectArg):
    name = "URLSearchParams"


class DOMStringMapArg(ObjectArg):
    name = "DOMStringMap"


class AttrArg(ObjectArg):
    name = "Attr"


class NamedNodeMapArg(ObjectArg):
    name = "NamedNodeMap"


class DOMImplementationArg(ObjectArg):
    name = "DOMImplementation"


class ApplicationCacheArg(ObjectArg):
    name = "ApplicationCache"


class XPathEvaluatorArg(ObjectArg):
    name = "XPathEvaluator"


class XPathNSResolverArg(ObjectArg):
    name = "XPathNSResolver"


class XPathExpressionArg(ObjectArg):
    name = "XPathExpression"


class XPathResultArg(ObjectArg):
    name = "XPathResult"


class XMLSerializerArg(ObjectArg):
    name = "XMLSerializer"


class XSLTProcessorArg(ObjectArg):
    name = "XSLTProcessor"


class DOMParserArg(ObjectArg):
    name = "DOMParser"


class DataTransferArg(ObjectArg):
    name = "DataTransfer"


class DataTransferItemListArg(ObjectArg):
    name = "DataTransferItemList"


class DataTransferItemArg(ObjectArg):
    name = "DataTransferItem"


class BlobArg(ObjectArg):
    name = "Blob"


class FontFaceSetArg(ObjectArg):
    name = "FontFaceSet"


class FontFaceArg(ObjectArg):
    name = "FontFace"


class EventArg(ObjectArg):
    name = "Event"


class EventTargetArg(ObjectArg):
    name = "EventTarget"


class EventTargetsArg(ObjectArg):
    name = "EventTargets"


class CustomEventArg(ObjectArg):
    name = "CustomEvent"


class MediaQueryListEventArg(ObjectArg):
    name = "MediaQueryListEvent"


class ApplicationCacheErrorEventArg(ObjectArg):
    name = "ApplicationCacheErrorEvent"


class SecurityPolicyViolationEventArg(ObjectArg):
    name = "SecurityPolicyViolationEvent"


class BeforeUnloadEventArg(ObjectArg):
    name = "BeforeUnloadEvent"


class UIEventArg(ObjectArg):
    name = "UIEvent"


class PointerEventArg(ObjectArg):
    name = "PointerEvent"


class PromiseRejectionEventArg(ObjectArg):
    name = "PromiseRejectionEvent"


class FocusEventArg(ObjectArg):
    name = "FocusEvent"


class CompositionEventArg(ObjectArg):
    name = "CompositionEvent"


class InputEventArg(ObjectArg):
    name = "InputEvent"


class InputDeviceCapabilitiesArg(ObjectArg):
    name = "InputDeviceCapabilities"


class ResourceProgressEventArg(ObjectArg):
    name = "ResourceProgressEvent"


class TextEventArg(ObjectArg):
    name = "TextEvent"


class ClipboardEventArg(ObjectArg):
    name = "ClipboardEvent"


class ProgressEventArg(ObjectArg):
    name = "ProgressEvent"


class WheelEventArg(ObjectArg):
    name = "WheelEvent"


class HashChangeEventArg(ObjectArg):
    name = "HashChangeEvent"


class MouseEventArg(ObjectArg):
    name = "MouseEvent"


class TransitionEventArg(ObjectArg):
    name = "TransitionEvent"


class AnimationPlaybackEventArg(ObjectArg):
    name = "AnimationPlaybackEvent"


class PopStateEventArg(ObjectArg):
    name = "PopStateEvent"


class DragEventArg(ObjectArg):
    name = "DragEvent"


class PageTransitionEventArg(ObjectArg):
    name = "PageTransitionEvent"


class MessageEventArg(ObjectArg):
    name = "MessageEvent"


class MutationEventArg(ObjectArg):
    name = "MutationEvent"


class AnimationEventArg(ObjectArg):
    name = "AnimationEvent"


class ErrorEventArg(ObjectArg):
    name = "ErrorEvent"


class KeyboardEventArg(ObjectArg):
    name = "KeyboardEvent"


class NavigatorArg(ObjectArg):
    name = "Navigator"


class CustomElementRegistryArg(ObjectArg):
    name = "CustomElementRegistry"


class BarPropArg(ObjectArg):
    name = "BarProp"


class ScreenArg(ObjectArg):
    name = "Screen"


class HistoryArg(ObjectArg):
    name = "History"


class VisualViewportArg(ObjectArg):
    name = "VisualViewport"


class ShadowRootArg(ObjectArg):
    name = "ShadowRoot"


class DocumentOrShadowRootArg(ObjectArg):
    name = "DocumentOrShadowRoot"


class DocumentTypeArg(ObjectArg):
    name = "DocumentType"


class ElementArg(ObjectArg):
    name = "Element"


class CharacterDataArg(ObjectArg):
    name = "CharacterData"


class DocumentFragmentArg(ObjectArg):
    name = "DocumentFragment"


class CommentArg(ObjectArg):
    name = "Comment"


class TextArg(ObjectArg):
    name = "Text"


class CDATASectionArg(ObjectArg):
    name = "CDATASection"


class EventHandlerArg(ObjectArg):
    name = "EventHandler"

    def mutate(self, _) -> bool:
        return False


class SelectionArg(ObjectArg):
    name = "Selection"


class StyleSheetArg(ObjectArg):
    name = "StyleSheet"


class CSSStyleSheetArg(ObjectArg):
    name = "CSSStyleSheet"


class CSSKeyframesSheetArg(ObjectArg):
    name = "CSSKeyframesSheet"


class CSSStyleRuleListArg(ObjectArg):
    name = "CSSStyleRuleList"


class CSSKeyframesRuleListArg(ObjectArg):
    name = "CSSKeyframesRuleList"


class CSSKeyframeRuleListArg(ObjectArg):
    name = "CSSKeyframeRuleList"


class CSSRuleArg(ObjectArg):
    name = "CSSRule"


class CSSStyleRuleArg(ObjectArg):
    name = "CSSStyleRule"


class CSSKeyframesRuleArg(ObjectArg):
    name = "CSSKeyframesRule"


class CSSKeyframeRuleArg(ObjectArg):
    name = "CSSKeyframeRule"


class CSSStyleDeclarationArg(ObjectArg):
    name = "CSSStyleDeclaration"


class DocumentTimelineArg(ObjectArg):
    name = "DocumentTimeline"


class TreeWalkerArg(ObjectArg):
    name = "TreeWalker"


class NodeIteratorArg(ObjectArg):
    name = "NodeIterator"


class NodeFilterArg(ObjectArg):
    name = "NodeFilter"


class RangeArg(ObjectArg):
    name = "Range"


class StaticRangesArg(ObjectArg):
    name = "StaticRanges"


class StaticRangeArg(ObjectArg):
    name = "StaticRange"


class TimeRangesArg(ObjectArg):
    name = "TimeRanges"


class DOMRectArg(ObjectArg):
    name = "DOMRect"


class DOMRectListArg(ObjectArg):
    name = "DOMRectList"


class NodeListArg(ObjectArg):
    name = "NodeList"


class ElementListArg(ObjectArg):
    name = "ElementList"


class HTMLCollectionArg(ObjectArg):
    name = "HTMLCollection"


class HTMLAllCollectionArg(ObjectArg):
    name = "HTMLAllCollection"


class HTMLOptionsCollectionArg(ObjectArg):
    name = "HTMLOptionsCollection"


class HTMLElementListArg(ObjectArg):
    name = "HTMLElementList"


class HTMLLabelElementListArg(ObjectArg):
    name = "HTMLLabelElementList"


class HTMLTableCellsCollectionArg(ObjectArg):
    name = "HTMLTableCellsCollection"


class HTMLTableRowsCollectionArg(ObjectArg):
    name = "HTMLTableRowsCollection"


class HTMLTableSectionsCollectionArg(ObjectArg):
    name = "HTMLTableSectionsCollection"


class HTMLAreasCollectionArg(ObjectArg):
    name = "HTMLAreasCollection"


###########################################
# Animation
###########################################
class AnimationEffectTimingReadOnlyArg(ObjectArg):
    name = "AnimationEffectTimingReadOnly"


class AnimationEffectReadOnlyArg(ObjectArg):
    name = "AnimationEffectReadOnly"


class AnimationEffectTimingArg(ObjectArg):
    name = "AnimationEffectTiming"


class AnimationsArg(ObjectArg):
    name = "Animations"


class AnimationArg(ObjectArg):
    name = "Animation"


class AnimationTimelineArg(ObjectArg):
    name = "AnimationTimeline"


class KeyframeEffectArg(ObjectArg):
    name = "KeyframeEffect"


class ValidityStateArg(ObjectArg):
    name = "ValidityState"


class MediaErrorArg(ObjectArg):
    name = "MediaError"


class MediaControllerArg(ObjectArg):
    name = "MediaController"


class MediaSessionArg(ObjectArg):
    name = "MediaSession"


class MediaStreamArg(ObjectArg):
    name = "MediaStream"


class VideoPlaybackQualityArg(ObjectArg):
    name = "VideoPlaybackQuality"


class TextTrackListArg(ObjectArg):
    name = "TextTrackList"


class TextTrackCueListArg(ObjectArg):
    name = "TextTrackCueList"


class TextTrackCueArg(ObjectArg):
    name = "TextTrackCue"


class TextTrackArg(ObjectArg):
    name = "TextTrack"


class VideoTrackListArg(ObjectArg):
    name = "VideoTrackList"


class VideoTrackArg(ObjectArg):
    name = "VideoTrack"


class AudioTrackListArg(ObjectArg):
    name = "AudioTrackList"


class AudioTrackArg(ObjectArg):
    name = "AudioTrack"


class VTTRegionListArg(ObjectArg):
    name = "VTTRegionList"


class VTTRegionArg(ObjectArg):
    name = "VTTRegion"


class VTTCueArg(ObjectArg):
    name = "VTTCue"


class HTMLElementArg(ObjectArg):
    name = "HTMLElement"


class HTMLMediaElementArg(ObjectArg):
    name = "HTMLMediaElement"


class HTMLTableSectionElementArg(ObjectArg):
    name = "HTMLTableSectionElement"


class HTMLTableCellElementArg(ObjectArg):
    name = "HTMLTableCellElement"


class HTMLModElementArg(ObjectArg):
    name = "HTMLModElement"


class HTMLQuoteElementArg(ObjectArg):
    name = "HTMLQuoteElement"


class HTMLAnchorElementArg(ObjectArg):
    name = "HTMLAnchorElement"


class HTMLAbbrElementArg(ObjectArg):
    name = "HTMLAbbrElement"


class HTMLAcronymElementArg(ObjectArg):
    name = "HTMLAcronymElement"


class HTMLAddressElementArg(ObjectArg):
    name = "HTMLAddressElement"


class HTMLAreaElementArg(ObjectArg):
    name = "HTMLAreaElement"


class HTMLArticleElementArg(ObjectArg):
    name = "HTMLArticleElement"


class HTMLAsideElementArg(ObjectArg):
    name = "HTMLAsideElement"


class HTMLAudioElementArg(ObjectArg):
    name = "HTMLAudioElement"


class HTMLBElementArg(ObjectArg):
    name = "HTMLBElement"


class HTMLBaseFontElementArg(ObjectArg):
    name = "HTMLBaseFontElement"


class HTMLBDIElementArg(ObjectArg):
    name = "HTMLBDIElement"


class HTMLBDOElementArg(ObjectArg):
    name = "HTMLBDOElement"


class HTMLBgSoundElementArg(ObjectArg):
    name = "HTMLBgSoundElement"


class HTMLBigElementArg(ObjectArg):
    name = "HTMLBigElement"


class HTMLBlockQuoteElementArg(ObjectArg):
    name = "HTMLBlockQuoteElement"


class HTMLBRElementArg(ObjectArg):
    name = "HTMLBRElement"


class HTMLButtonElementArg(ObjectArg):
    name = "HTMLButtonElement"


class HTMLCanvasElementArg(ObjectArg):
    name = "HTMLCanvasElement"


class HTMLTableCaptionElementArg(ObjectArg):
    name = "HTMLTableCaptionElement"


class HTMLCenterElementArg(ObjectArg):
    name = "HTMLCenterElement"


class HTMLCiteElementArg(ObjectArg):
    name = "HTMLCiteElement"


class HTMLCodeElementArg(ObjectArg):
    name = "HTMLCodeElement"


class HTMLTableColElementArg(ObjectArg):
    name = "HTMLTableColElement"


class HTMLTableColGroupElementArg(ObjectArg):
    name = "HTMLTableColGroupElement"


class HTMLCommandElementArg(ObjectArg):
    name = "HTMLCommandElement"


class HTMLContentElementArg(ObjectArg):
    name = "HTMLContentElement"


class HTMLDataElementArg(ObjectArg):
    name = "HTMLDataElement"


class HTMLDataListElementArg(ObjectArg):
    name = "HTMLDataListElement"


class HTMLDDElementArg(ObjectArg):
    name = "HTMLDDElement"


class HTMLDelElementArg(ObjectArg):
    name = "HTMLDelElement"


class HTMLDetailsElementArg(ObjectArg):
    name = "HTMLDetailsElement"


class HTMLDFNElementArg(ObjectArg):
    name = "HTMLDFNElement"


class HTMLDialogElementArg(ObjectArg):
    name = "HTMLDialogElement"


class HTMLDirectoryElementArg(ObjectArg):
    name = "HTMLDirectoryElement"


class HTMLDivElementArg(ObjectArg):
    name = "HTMLDivElement"


class HTMLDListElementArg(ObjectArg):
    name = "HTMLDListElement"


class HTMLDTElementArg(ObjectArg):
    name = "HTMLDTElement"


class HTMLEMElementArg(ObjectArg):
    name = "HTMLEMElement"


class HTMLEmbedElementArg(ObjectArg):
    name = "HTMLEmbedElement"


class HTMLFieldSetElementArg(ObjectArg):
    name = "HTMLFieldSetElement"


class HTMLFigCaptionElementArg(ObjectArg):
    name = "HTMLFigCaptionElement"


class HTMLFigureElementArg(ObjectArg):
    name = "HTMLFigureElement"


class HTMLFontElementArg(ObjectArg):
    name = "HTMLFontElement"


class HTMLFooterElementArg(ObjectArg):
    name = "HTMLFooterElement"


class HTMLFormElementArg(ObjectArg):
    name = "HTMLFormElement"


class HTMLFrameElementArg(ObjectArg):
    name = "HTMLFrameElement"


class HTMLFrameSetElementArg(ObjectArg):
    name = "HTMLFrameSetElement"


class HTMLHeadingElementArg(ObjectArg):
    name = "HTMLHeadingElement"


class HTMLHeading1ElementArg(ObjectArg):
    name = "HTMLHeading1Element"


class HTMLHeading2ElementArg(ObjectArg):
    name = "HTMLHeading2Element"


class HTMLHeading3ElementArg(ObjectArg):
    name = "HTMLHeading3Element"


class HTMLHeading4ElementArg(ObjectArg):
    name = "HTMLHeading4Element"


class HTMLHeading5ElementArg(ObjectArg):
    name = "HTMLHeading5Element"


class HTMLHeading6ElementArg(ObjectArg):
    name = "HTMLHeading6Element"


class HTMLHeaderElementArg(ObjectArg):
    name = "HTMLHeaderElement"


class HTMLHGroupElementArg(ObjectArg):
    name = "HTMLHGroupElement"


class HTMLHRElementArg(ObjectArg):
    name = "HTMLHRElement"


class HTMLIElementArg(ObjectArg):
    name = "HTMLIElement"


class HTMLIFrameElementArg(ObjectArg):
    name = "HTMLIFrameElement"


class HTMLImageElementArg(ObjectArg):
    name = "HTMLImageElement"


class HTMLInputElementArg(ObjectArg):
    name = "HTMLInputElement"


class HTMLInsElementArg(ObjectArg):
    name = "HTMLInsElement"


class HTMLIsIndexElementArg(ObjectArg):
    name = "HTMLIsIndexElement"


class HTMLKBDElementArg(ObjectArg):
    name = "HTMLKBDElement"


class HTMLKeygenElementArg(ObjectArg):
    name = "HTMLKeygenElement"


class HTMLLabelElementArg(ObjectArg):
    name = "HTMLLabelElement"


class HTMLLegendElementArg(ObjectArg):
    name = "HTMLLegendElement"


class HTMLLIElementArg(ObjectArg):
    name = "HTMLLIElement"


class HTMLLinkElementArg(ObjectArg):
    name = "HTMLLinkElement"


class HTMLStyleElementArg(ObjectArg):
    name = "HTMLStyleElement"


class HTMLListingElementArg(ObjectArg):
    name = "HTMLListingElement"


class HTMLMainElementArg(ObjectArg):
    name = "HTMLMainElement"


class HTMLMapElementArg(ObjectArg):
    name = "HTMLMapElement"


class HTMLMarkElementArg(ObjectArg):
    name = "HTMLMarkElement"


class HTMLMarqueeElementArg(ObjectArg):
    name = "HTMLMarqueeElement"


class HTMLMenuElementArg(ObjectArg):
    name = "HTMLMenuElement"


class HTMLMenuItemElementArg(ObjectArg):
    name = "HTMLMenuItemElement"


class HTMLMetaElementArg(ObjectArg):
    name = "HTMLMetaElement"


class HTMLMeterElementArg(ObjectArg):
    name = "HTMLMeterElement"


class HTMLNavElementArg(ObjectArg):
    name = "HTMLNavElement"


class HTMLObjectElementArg(ObjectArg):
    name = "HTMLObjectElement"


class HTMLOListElementArg(ObjectArg):
    name = "HTMLOListElement"


class HTMLOptGroupElementArg(ObjectArg):
    name = "HTMLOptGroupElement"


class HTMLOptionElementArg(ObjectArg):
    name = "HTMLOptionElement"


class HTMLOutputElementArg(ObjectArg):
    name = "HTMLOutputElement"


class HTMLParagraphElementArg(ObjectArg):
    name = "HTMLParagraphElement"


class HTMLParamElementArg(ObjectArg):
    name = "HTMLParamElement"


class HTMLPictureElementArg(ObjectArg):
    name = "HTMLPictureElement"


class HTMLPlainTextElementArg(ObjectArg):
    name = "HTMLPlainTextElement"


class HTMLPreElementArg(ObjectArg):
    name = "HTMLPreElement"


class HTMLProgressElementArg(ObjectArg):
    name = "HTMLProgressElement"


class HTMLQElementArg(ObjectArg):
    name = "HTMLQElement"


class HTMLRPElementArg(ObjectArg):
    name = "HTMLRPElement"


class HTMLRTElementArg(ObjectArg):
    name = "HTMLRTElement"


class HTMLRubyElementArg(ObjectArg):
    name = "HTMLRubyElement"


class HTMLSElementArg(ObjectArg):
    name = "HTMLSElement"


class HTMLSampElementArg(ObjectArg):
    name = "HTMLSampElement"


class HTMLScriptElementArg(ObjectArg):
    name = "HTMLScriptElement"


class HTMLSectionElementArg(ObjectArg):
    name = "HTMLSectionElement"


class HTMLSelectElementArg(ObjectArg):
    name = "HTMLSelectElement"


class HTMLShadowElementArg(ObjectArg):
    name = "HTMLShadowElement"


class HTMLSlotElementArg(ObjectArg):
    name = "HTMLSlotElement"


class HTMLSmallElementArg(ObjectArg):
    name = "HTMLSmallElement"


class HTMLSourceElementArg(ObjectArg):
    name = "HTMLSourceElement"


class HTMLSpanElementArg(ObjectArg):
    name = "HTMLSpanElement"


class HTMLStrikeElementArg(ObjectArg):
    name = "HTMLStrikeElement"


class HTMLStrongElementArg(ObjectArg):
    name = "HTMLStrongElement"


class HTMLSubElementArg(ObjectArg):
    name = "HTMLSubElement"


class HTMLSummaryElementArg(ObjectArg):
    name = "HTMLSummaryElement"


class HTMLSupElementArg(ObjectArg):
    name = "HTMLSupElement"


class HTMLTimeElementArg(ObjectArg):
    name = "HTMLTimeElement"


class HTMLTableElementArg(ObjectArg):
    name = "HTMLTableElement"


class HTMLTBodyElementArg(ObjectArg):
    name = "HTMLTBodyElement"


class HTMLTableDataCellElementArg(ObjectArg):
    name = "HTMLTableDataCellElement"


class HTMLTemplateElementArg(ObjectArg):
    name = "HTMLTemplateElement"


class HTMLTextAreaElementArg(ObjectArg):
    name = "HTMLTextAreaElement"


class HTMLTFootElementArg(ObjectArg):
    name = "HTMLTFootElement"


class HTMLTableHeaderCellElementArg(ObjectArg):
    name = "HTMLTableHeaderCellElement"


class HTMLTHeadElementArg(ObjectArg):
    name = "HTMLTHeadElement"


class HTMLTitleElementArg(ObjectArg):
    name = "HTMLTitleElement"


class HTMLTableRowElementArg(ObjectArg):
    name = "HTMLTableRowElement"


class HTMLTrackElementArg(ObjectArg):
    name = "HTMLTrackElement"


class HTMLTTElementArg(ObjectArg):
    name = "HTMLTTElement"


class HTMLUElementArg(ObjectArg):
    name = "HTMLUElement"


class HTMLUListElementArg(ObjectArg):
    name = "HTMLUListElement"


class HTMLVarElementArg(ObjectArg):
    name = "HTMLVarElement"


class HTMLVideoElementArg(ObjectArg):
    name = "HTMLVideoElement"


class HTMLWBRElementArg(ObjectArg):
    name = "HTMLWBRElement"


class HTMLXMPElementArg(ObjectArg):
    name = "HTMLXMPElement"


class HTMLStringArg(ObjectArg):
    name = "HTMLString"


class ShadowHostArg(ObjectArg):
    name = "ShadowHost"


class MutationObserverArg(ObjectArg):
    name = "MutationObserver"


class MutationRecordsArg(ObjectArg):
    name = "MutationRecords"


class MutationRecordArg(ObjectArg):
    name = "MutationRecord"


class ProcessingInstructionArg(ObjectArg):
    name = "ProcessingInstruction"


class MessageChannelArg(ObjectArg):
    name = "MessageChannel"


class MessagePortArg(ObjectArg):
    name = "MessagePort"


class RequestIDArg(ObjectArg):
    name = "RequestID"


class MediaQueryListArg(ObjectArg):
    name = "MediaQueryList"


class MediaListArg(ObjectArg):
    name = "MediaList"


class StyleMediaArg(ObjectArg):
    name = "StyleMedia"


#############################################
# HTML values
#############################################
class ShadowRootInitArg(ValueArg):
    def generate(self, _):
        self.value = "{{mode: \"{}\", delegatesFocus: {}}}".format(
            Random.choice(["open", "closed"]),
            dv.boolean()
        )


class MutationObserverInitArg(ValueArg):
    def generate(self, _):
        self.value = "{{ attributeOldValue: {}, attributes: {}, characterData: {}, " \
                     "characterDataOldValue: {}, childList: {}, subtree:{} }}".format(
            dv.boolean(), dv.boolean(), dv.boolean(), dv.boolean(), dv.boolean(), dv.boolean())


class ScrollToOptionsArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = "{{top: {}, left: {}, behavior: \"{}\"}}".format(
            Random.number(),
            Random.number(),
            Random.choice(["auto", "smooth"])
        )


class ScrollIntoViewOptionsArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = "{{behavior: \"{}\", block: \"{}\", inline: \"{}\"}}".format(
            Random.choice(["auto", "smooth"]),
            Random.choice(["start", "center", "end", "nearest"]),
            Random.choice(["start", "center", "end", "nearest"])
        )


class FontArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.font()


class HeadingArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = "H{}".format(Random.range(1, 6))


InsertPositionArg = StringSetArgWrapper(("beforebegin", "afterbegin", "beforeend", "afterend"))
DesignModeArg = StringSetArgWrapper(("on", "off"))


class AutoCapitalizeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.auto_capitalize()


class ContentEditableArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.boolean()


class DirArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.dir_()


class LangArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.lang()


class TabIndexArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.tab_index()


class DropZoneArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.drop_zone()


class CharsetArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.charset()


class CoordsArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.coords()


class ShapeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.shape()


class TargetArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.target()


class PreloadArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.preload()


class MediaSrcArg(StringArg):
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


class TrackSrcArg(StringArg):
    def generate(self, _):
        if Random.bool():
            self.value = "x"
        else:
            self.value = dv.track_url()


class VolumeArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = Random.float01()


class ClearArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.clear()


class TrackKindArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.track_kind()


class FormEncTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.form_enc_type()


class FormMethodArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.form_method()


class ButtonTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.button_type()


class AlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.align()


class WhatToShowArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = str(Random.choice([-1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]))


class PlayStateArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.play_state()


class AnimateOptionsArg(ValueArg):
    def generate(self, _):
        self.value = "{{ delay: {}, direction: \"{}\", duration: {}, easing: \"{}\", endDelay: {}, fill: \"{}\", " \
                     "iterationStart: {}, iterations: {} }}".format(
            dv.clock_in_ms(), dv.animation_direction(), dv.clock_in_ms(), dv.animation_easing(),
            dv.clock_in_ms(), dv.animation_fill_mode(), Random.number(), Random.integer())


class AnimationDirectionArg(StringArg):
    def generate(self, _):
        self.value = dv.animation_direction()


class AnimationEasingArg(StringArg):
    def generate(self, _):
        self.value = dv.animation_easing()


class AnimationFillArg(StringArg):
    def generate(self, _):
        self.value = dv.animation_fill_mode()


class AssignedNodesOptionArg(ValueArg):
    def generate(self, _):
        self.value = "{{ flatten: {} }}".format(dv.boolean())


class AddEventListenerOptionsArg(ValueArg):
    def generate(self, _):
        self.value = "{{ capture: {}, once: {}, passive: {} }}".format(
            dv.boolean(), dv.boolean(), dv.boolean()
        )


class ObjectAlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.object_align()


class ScrollingArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.scrolling()


class TableFrameArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.table_frame()


class TableRulesArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.table_rules()


class TableAlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.table_align()


class VAlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.valign()


class InputModeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.input_mode()


class WrapArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.wrap()


class SelectionDirectionArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.selection_direction()


class SelectModeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.select_mode()


class NumberingTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.numbering_type()


class AutoCompleteArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.auto_complete()


class CaptionAlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.caption_align()


class KeyTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.key_type()


class ImageSrcArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        if Random.bool():
            self.value = dv.image_url()
        else:
            self.value = "x"


class SrcSetArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.srcset()


class MetaSchemeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.meta_scheme()


class TextTrackModeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.text_track_mode()


class VTTRegionScrollArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.vtt_region_scroll()


class VTTCueVerticalArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.vtt_cue_vertical()


class VTTCueLineArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = Random.number()


class VTTCuePositionArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        if Random.bool():
            self.value = "auto"
        else:
            self.value = Random.number()


class VTTCueAlignArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.vtt_cue_align()


class DateTimeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.date_time()


class ParamValueTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.param_value_type()


class LinkAsArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.link_as()


class UListTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.ulist_type()


class TableScopeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.table_scope()


class MenuTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.menu_type()


class AcceptArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.accept()


class InputTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.input_type()


class MenuItemTypeArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.menu_item_type()


class MarqueeBehaviorArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.marquee_behavior()


class MarqueeDirectionArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.marquee_direction()


class MarqueeLoopArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = dv.marquee_loop()


class SelectionModifyAlterArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = Random.choice(("move", "extend"))


class SelectionModifyDirectionArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = Random.choice(("forward", "backward", "left", "right"))


class SelectionModifyGranularityArg(StringArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = Random.choice(("character", "word", "sentence", "line", "paragraph",
                                    "lineboundary", "sentenceboundary", "paragraphboundary",
                                    "documentboundary"))


class GetRootNodeOptionsArg(ValueArg):
    def __init__(self):
        super().__init__()

    def generate(self, _):
        self.value = "{{ composed: {} }}".format(dv.boolean())


class RangeCompareArg(ValueArg):
    def generate(self, _):
        self.value = Random.choice((
            "Range.END_TO_END",
            "Range.END_TO_START",
            "Range.START_TO_END",
            "Range.START_TO_START"
        ))


class CSSFloatArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["left", "right", "none", "initial", "inherit"])


class ContentTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["text/html", "application/xml", "image/svg+xml"])


class RelArg(StringArg):
    def generate(self, _):
        self.value = dv.rel()


class RevArg(StringArg):
    def generate(self, _):
        self.value = dv.rev()


class FrameSrcArg(StringArg):
    def generate(self, _):
        if Random.bool():
            self.value = "x"
        else:
            self.value = dv.frame_url()


class MediaQueryArg(StringArg):
    def generate(self, _):
        self.value = dv.media_query()


class ImageTypeArg(StringArg):
    def generate(self, _):
        self.value = dv.image_type()


class MediaTypeArg(StringArg):
    def generate(self, _):
        self.value = dv.media_type()


class MIMETypeArg(StringArg):
    def generate(self, _):
        self.value = dv.mime_type()


class CSSTypeArg(StringArg):
    def generate(self, _):
        self.value = dv.css_type()


class DropEffectArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["none", "copy", "link", "move"])


class EffectAllowedArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["none", "copy", "copyLink", "copyMove", "link",
                                    "linkMove", "move", "all", "uninitialized"])


class FontWeightArg(StringArg):
    def generate(self, _):
        self.value = dv.font_weight()


class FontStretchArg(StringArg):
    def generate(self, _):
        self.value = dv.font_stretch()


class FontVariantArg(StringArg):
    def generate(self, _):
        self.value = dv.font_variant()


class FontFeatureSettingsArg(StringArg):
    def generate(self, _):
        self.value = dv.font_feature_settings()


class UnicodeRangeArg(StringArg):
    def generate(self, _):
        self.value = dv.unicode_range()


class ScrollRestorationArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["auto", "manual"])


class HistoryStateArg(ValueArg):
    def generate(self, _):
        self.value = "{{ \"{}\": \"{}\" }}".format(Random.string(), Random.string())


class CSSPropertyNameArg(StringArg):
    def generate(self, _):
        self.value = get_css_property_name()


class CustomElementNameArg(StringArg):
    def generate(self, _):
        self.value = "custom-{}".format(Random.choice(["a", "b", "c"]))


#####################################
# Context-aware arg
#####################################
class MediaGroupArg(StringArg):
    def generate(self, context):
        self.value = context.global_context.get_token("mediagroup")


class TagArg(StringArg):
    def generate(self, context):
        elem = Random.choice(list(context.global_context.in_tree_set) + ["HTMLBodyElement"])
        self.value = docs.tag_from_element(elem)


class HTMLTagArg(StringArg):
    def generate(self, context):
        elem = Random.choice([e for e in context.global_context.in_tree_set if docs.is_html_element(e)] +
                              ["HTMLBodyElement"])
        self.value = docs.tag_from_element(elem)


class ClassArg(StringArg):
    def generate(self, context):
        self.value = context.global_context.get_token("class")


class KeyFramesArg(Arg):
    def __init__(self):
        super().__init__()
        self.props = {}

    def is_object(self):
        return False

    def append_prop(self, context):
        while True:
            prop, value_class = get_css_property(animatable=True)
            if prop not in self.props:
                break
        self.props[prop] = []
        for _ in range(2):
            value = value_class()
            value.generate(context)
            self.props[prop].append(value)

    def generate(self, context):
        self.append_prop(context)

    def mutate(self, context) -> bool:
        c = Random.selector(4)
        if c == 0:
            prop = Random.choice(list(self.props.keys()))
            value_class = get_css_property_value(prop)
            value = value_class()
            value.generate(context)
            self.props[prop].append(value)
            return True
        elif c == 1:
            prop = Random.choice(list(self.props.keys()))
            values = self.props[prop]
            value = Random.choice(values)
            return value.mutate(context)
        elif c == 2:
            self.append_prop(context)
            return True
        else:
            # 3. replace property
            prop = Random.choice(list(self.props.keys()))
            del self.props[prop]
            self.append_prop(context)
            return True

    def merge_fix(self, merge_map):
        for values in self.props.values():
            for value in values:
                value.merge_fix(merge_map)

    def __str__(self):
        s = "{ "
        for prop in self.props:
            s += "\"{}\": [".format(prop)
            for value in self.props[prop]:
                s += stringify(str(value)) + ", "
            s += "], "
        s += " }"
        return s


class TableAxisArg(StringArg):
    def generate(self, context):
        self.value = context.global_context.get_token("axis")


class RadioGroupArg(StringArg):
    def generate(self, context):
        self.value = context.global_context.get_token("radiogroup")


class XPathArg(StringArg):
    def generate(self, context):
        elem = Random.choice(list(context.global_context.in_tree_set) + ["HTMLBodyElement"])
        self.value = "//{}".format(docs.tag_from_element(elem))


XPathResultTypeArg = lambda: RangedIntegerArg(0, 9)

MouseButtonTypeArg = lambda: RangedIntegerArg(0, 5)


class TextEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["textInput", "foo"])


class MouseEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.mouse_events + ["foo"])


class CompositionEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.composition_events + ["foo"])


class UIEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.ui_events + ["foo"])


class MessageEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(["message", "foo"])


class EventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.ui_events + docs.mutation_events + ["textInput", "foo"])


class MutationEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.mutation_events + ["foo"])


AttrChangeTypeArg = lambda: RangedIntegerArg(0, 3)


class KeyboardEventTypeArg(StringArg):
    def generate(self, _):
        self.value = Random.choice(docs.keyboard_events + ["foo"])


KeyLocationTypeArg = lambda: RangedIntegerArg(0, 5)


DummyUrlArg = ConstStringArgWrapper("x")


##################################################
# Dynamic arg
##################################################
class SlotArg(Arg):
    def __init__(self):
        super().__init__()
        self.slot = None

    def is_object(self):
        return False

    def generate(self, context):
        self.slot = context.global_context.get_object(["HTMLSlotElement"])

    def merge_fix(self, merge_map):
        if self.slot is not None and self.slot in merge_map:
            self.slot = merge_map[self.slot]

    def __str__(self):
        if self.slot is None:
            s = "foo"
        else:
            s = self.slot.id
        return stringify(s)


class UseMapArg(Arg):
    def __init__(self):
        super().__init__()
        self.map = None

    def is_object(self):
        return False

    def generate(self, context):
        self.map = context.global_context.get_object(["HTMLMapElement"])

    def merge_fix(self, merge_map):
        if self.map is not None and self.map in merge_map:
            self.map = merge_map[self.map]

    def __str__(self):
        if self.map is None:
            s = "#foo"
        else:
            s = "#{}".format(self.map.id)
        return stringify(s)


class ContentSelectArg(Arg):
    def __init__(self):
        super().__init__()
        self.cla = None
        self.elem = None

    def is_object(self):
        return False

    def generate(self, context):
        if Random.bool():
            self.cla = context.global_context.get_token("class")
            self.elem = None
        else:
            self.cla = None
            self.elem = context.global_context.get_object(docs.elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.cla is not None:
            s = ".{}".format(self.cla)
        elif self.elem is not None:
            s = "#{}".format(self.elem.id)
        else:
            s = "#foo"
        return stringify(s)


class LabelForArg(Arg):
    def __init__(self):
        super().__init__()
        self.elem = None

    def is_object(self):
        return False

    def generate(self, context):
        self.elem = context.global_context.get_object(docs.html_labelable_elements)

    def merge_fix(self, merge_map):
        if self.elem is not None and self.elem in merge_map:
            self.elem = merge_map[self.elem]

    def __str__(self):
        if self.elem is not None:
            s = self.elem.id
        else:
            s = "foo"
        return stringify(s)


class TableHeadersArg(Arg):
    def __init__(self):
        super().__init__()
        self.ths = []

    def is_object(self):
        return False

    def append_th(self, context):
        elem = context.global_context.get_object(["HTMLTableHeaderCellElement"])
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
        return stringify(cat(list(map(get_object_id, self.ths))))


class CSSSelectorValueArg(Arg):
    def __init__(self):
        super().__init__()
        self.selector = None

    def is_object(self):
        return False

    def generate(self, context):
        self.selector = create_css_selector()
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
        return stringify(str(self.selector))


class CSSStyleDeclarationValueArg(Arg):
    def __init__(self):
        super().__init__()
        self.style_declaration = CSSStyleDeclaration()

    def is_object(self):
        return False

    def generate(self, context):
        self.style_declaration.generate(context.global_context)
        for _ in range(CSSConfig.max_css_internal_decl_count - 1):
            self.style_declaration.append(context.global_context)

    def mutate(self, context):
        return self.style_declaration.mutate(context.global_context)

    def merge_fix(self, merge_map):
        self.style_declaration.merge_fix(merge_map)

    def __str__(self):
        return stringify(str(self.style_declaration))


class CSSStyleRuleValueArg(Arg):
    def __init__(self):
        super().__init__()
        self.rule = CSSStyleRule()

    def is_object(self):
        return False

    def generate(self, context):
        self.rule.generate(context.global_context)
        for _ in range(CSSConfig.max_css_internal_decl_count - 1):
            self.rule.append_decl(context.global_context)

    def mutate(self, context):
        return self.rule.mutate(context.global_context)

    def merge_fix(self, merge_map):
        self.rule.merge_fix(merge_map)

    def __str__(self):
        return stringify(str(self.rule))


class CSSStyleRuleValueTextArg(Arg):
    def __init__(self):
        super().__init__()
        self.rule = CSSStyleRule()

    def is_object(self):
        return False

    def generate(self, context):
        self.rule.generate(context.global_context)
        for _ in range(CSSConfig.max_css_internal_decl_count - 1):
            self.rule.append_decl(context.global_context)

    def mutate(self, context):
        return self.rule.mutate(context.global_context)

    def merge_fix(self, merge_map):
        self.rule.merge_fix(merge_map)

    def __str__(self):
        return "document.createTextNode({})".format(stringify(str(self.rule)))


class CSSKeyframeNameArg(StringArg):
    def generate(self, _):
        self.value = dv.keyframe_name()


class CSSKeyframeRuleValueArg(Arg):
    def __init__(self):
        super().__init__()
        self.keyframe_rule = CSSKeyframeRule(dv.keyframe_name())

    def is_object(self):
        return False

    def mutate(self, context) -> bool:
        if Random.selector(5) == 0:
            self.keyframe_rule.name = dv.keyframe_name()
            return True
        else:
            return self.keyframe_rule.mutate(context.global_context)

    def generate(self, context):
        self.keyframe_rule.generate(context.global_context)

    def merge_fix(self, merge_map):
        self.keyframe_rule.merge_fix(merge_map)

    def __str__(self):
        return stringify(str(self.keyframe_rule))
