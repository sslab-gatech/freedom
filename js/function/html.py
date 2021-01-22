import docs
from attribute import get_attribute_templates
from js import API, APITemplate, is_satiable_arg, add_api
from js.function import FunctionTemplate, ConstructTemplate, ConstructObjectTemplate
from js.arg import RandomSelectorArg, ColorArg, BooleanArg, IntegerArg, StringArg, NullArg, \
    ClockArg, ClockInMsArg, IndexArg, ConstStringArgWrapper, FloatArg, ConstValueArgWrapper, \
    Float01Arg, CharArg, DoNothingArg
from js.arg import html as ha
from js.ret import html as hr
from css.declaration import create_css_declaration
from utils import seq
from utils.random import Random


############################################################
# x.removeAttribute(x.attributes[i % x.attributes.length].name)
############################################################
class RemoveAttribute(API):
    def __init__(self, this, selector):
        super().__init__(None, this)
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        if Random.bool():
            self.selector.mutate(context)
        else:
            self.this.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "{0}.removeAttribute({0}.attributes[{1} % {0}.attributes.length].name)".format(
            str(self.this),
            str(self.selector)
        )


class RemoveAttributeTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return RemoveAttribute(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


#####################################
# x.insertBefore(y, x.childNodes[i % x.childNodes.length])
#####################################
class InsertBefore(API):
    def __init__(self, this, new_node, selector):
        super().__init__(None, this)
        self.new_node = new_node
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.new_node.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.new_node.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.new_node.merge_fix(merge_map)

    def __str__(self):
        return "{0}.insertBefore({1}, {0}.childNodes[{2} % {0}.childNodes.length])".format(
            str(self.this),
            str(self.new_node),
            str(self.selector)
        )


class InsertBeforeTemplate(APITemplate):
    def __init__(self, this_class, new_node_class):
        super().__init__(None, this_class)
        self.new_node_class = new_node_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return InsertBefore(self.this_class(), self.new_node_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.new_node_class, context)


#####################################
# x.removeChild(x.childNodes[i % x.childNodes.length])
#####################################
class RemoveChild(API):
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
        return "{0}.removeChild({0}.childNodes[{1} % {0}.childNodes.length])".format(
            str(self.this),
            str(self.selector)
        )


class RemoveChildTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return RemoveChild(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


#####################################
# x.replaceChild(y, x.childNodes[i % x.childNodes.length])
#####################################
class ReplaceChild(API):
    def __init__(self, this, new_node, selector):
        super().__init__(None, this)
        self.new_node = new_node
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.new_node.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.new_node.mutate(context)
        else:
            self.selector.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.new_node.merge_fix(merge_map)

    def __str__(self):
        return "{0}.replaceChild({1}, {0}.childNodes[{2} % {0}.childNodes.length])".format(
            str(self.this),
            str(self.new_node),
            str(self.selector)
        )


class ReplaceChildTemplate(APITemplate):
    def __init__(self, this_class, new_node_class):
        super().__init__(None, this_class)
        self.new_node_class = new_node_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return ReplaceChild(self.this_class(), self.new_node_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.new_node_class, context)


############################################################
# NodeList.remove(): x.remove(i % x.length)
############################################################
class ListRemove(API):
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
        return "{0}.remove({1} % {0}.length)".format(
            str(self.this),
            str(self.selector)
        )


class ListRemoveTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return ListRemove(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# List.item(): item = x.item(i % x.length)
############################################################
class ListItem(API):
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
        return lhs + "{0}.item({1} % {0}.length)".format(
            str(self.this),
            str(self.selector)
        )


class ListItemTemplate(APITemplate):
    def __init__(self, ret_class, this_class):
        super().__init__(ret_class, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        ret = self.ret_class() if self.ret_class is not None else None
        return ListItem(ret, self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# List.add(): x.add(y, i % x.length)
############################################################
class ListAdd(API):
    def __init__(self, this, item, selector):
        super().__init__(None, this)
        self.item = item
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.item.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.this.mutate(context)
        elif c == 1:
            self.selector.mutate(context)
        else:
            self.item.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.item.merge_fix(merge_map)

    def __str__(self):
        return "{0}.add({1}, {2} % {0}.length)".format(
            str(self.this),
            str(self.item),
            str(self.selector)
        )


class ListAddTemplate(APITemplate):
    def __init__(self, this_class, item_class):
        super().__init__(None, this_class)
        self.item_class = item_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return ListAdd(self.this_class(), self.item_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.item_class, context)


############################################################
# snapshotItem()
############################################################
class SnapshotItem(API):
    def __init__(self, ret, this, selector):
        super().__init__(ret, this)
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
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
        return "var {0} = {1}.snapshotItem({2} % {1}.snapshotLength)".format(
            str(self.ret),
            str(self.this),
            str(self.selector)
        )


class SnapshotItemTemplate(APITemplate):
    def __init__(self, ret_class, this_class):
        super().__init__(ret_class, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return SnapshotItem(self.ret_class(), self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# x.deleteRow(i % x.rows.length)
############################################################
class TableSectionDeleteRow(API):
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
        return "{0}.deleteRow({1} % {0}.rows.length)".format(
            str(self.this), str(self.selector)
        )


class TableSectionDeleteRowTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return TableSectionDeleteRow(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# setAttribute
############################################################
class SetAttribute(API):
    def __init__(self, this):
        super().__init__(None, this)
        self.attr = None

    def generate_attr(self, context):
        self.attr = None

        element = self.this.obj
        templates = get_attribute_templates(element.name, include_aria=True)
        assert templates is not None and len(templates) > 0

        while True:
            template = Random.choice(templates)
            self.attr = element.generate_attribute(context, template)
            if self.attr is not None:
                break

    def generate(self, context):
        self.this.generate(context)
        self.generate_attr(context.global_context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.attr.mutate(context.global_context)
        elif c == 1:
            self.generate_attr(context.global_context)
        else:
            self.generate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.attr.merge_fix(merge_map)

    def __str__(self):
        ns = None
        if self.attr.name.startswith("xlink"):
            ns = "http://www.w3.org/1999/xlink"
        elif self.attr.name.startswith("xml"):
            ns = "http://www.w3.org/XML/1998/namespace"

        method = "setAttribute" if ns is None else "setAttributeNS"
        args = []
        if ns is not None:
            args.append("\"{}\"".format(ns))
        args.extend(["\"{}\"".format(self.attr.name), "\"{}\"".format(str(self.attr.value))])
        return "{}.{}({})".format(str(self.this), method, seq(args))


class SetAttributeTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        # if get_attribute_count(this.name) <= 0:
        #    print(this.name)
        #    assert False

    def instantiate(self):
        return SetAttribute(self.this_class())

    def satiable(self, context):
        return True


############################################################
# style.setProperty(propertyName, value);
############################################################
class SetProperty(API):
    def __init__(self, this):
        super().__init__(None, this)
        self.decl = None

    def generate_decl(self, context):
        self.decl = create_css_declaration()
        self.decl.generate(context)

    def generate(self, context):
        self.this.generate(context)
        self.generate_decl(context.global_context)

    def mutate(self, context):
        c = Random.selector(3)
        if c == 0:
            self.decl.mutate(context.global_context)
        elif c == 1:
            self.generate_decl(context.global_context)
        else:
            self.generate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.decl.merge_fix(merge_map)

    def __str__(self):
        return "{}.setProperty(\"{}\", \"{}\")".format(
            str(self.this),
            self.decl.prop,
            str(self.decl.value)
        )


class SetPropertyTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)

    def instantiate(self):
        return SetProperty(self.this_class())

    def satiable(self, context):
        return True


############################################################
# style.removeProperty(style.item(i % style.length));
############################################################
class RemoveProperty(API):
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
        return "{0}.removeProperty({0}.item({1} % {0}.length))".format(str(self.this), str(self.selector))


class RemovePropertyTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return RemoveProperty(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


############################################################
# document.createElement(tag); -- interesting
############################################################
class CreateInterestingElement(API):
    html_elements = {
        "a": hr.HTMLAnchorElementRet,
        "area": hr.HTMLAreaElementRet,
        "button": hr.HTMLButtonElementRet,
        "canvas": hr.HTMLCanvasElementRet,
        "caption": hr.HTMLTableCaptionElementRet,
        "col": hr.HTMLTableColElementRet,
        "colgroup": hr.HTMLTableColGroupElementRet,
        "data": hr.HTMLDataElementRet,
        "datalist": hr.HTMLDataListElementRet,
        "dd": hr.HTMLDDElementRet,
        "details": hr.HTMLDetailsElementRet,
        "dialog": hr.HTMLDialogElementRet,
        "div": hr.HTMLDivElementRet,
        "dl": hr.HTMLDListElementRet,
        "dt": hr.HTMLDTElementRet,
        "embed": hr.HTMLEmbedElementRet,
        "fieldset": hr.HTMLFieldSetElementRet,
        "form": hr.HTMLFormElementRet,
        "h1": hr.HTMLHeading1ElementRet,
        "iframe": hr.HTMLIFrameElementRet,
        "img": hr.HTMLImageElementRet,
        "input": hr.HTMLInputElementRet,
        "label": hr.HTMLLabelElementRet,
        "map": hr.HTMLMapElementRet,
        "marquee": hr.HTMLMarqueeElementRet,
        "menu": hr.HTMLMenuElementRet,
        "menuitem": hr.HTMLMenuItemElementRet,
        "object": hr.HTMLObjectElementRet,
        "ol": hr.HTMLOListElementRet,
        "optgroup": hr.HTMLOptGroupElementRet,
        "option": hr.HTMLOptionElementRet,
        "output": hr.HTMLOutputElementRet,
        "p": hr.HTMLParagraphElementRet,
        "param": hr.HTMLParamElementRet,
        "script": hr.HTMLScriptElementRet,
        "section": hr.HTMLSectionElementRet,
        "select": hr.HTMLSelectElementRet,
        "shadow": hr.HTMLShadowElementRet,
        "span": hr.HTMLSpanElementRet,
        "style": hr.HTMLStyleElementRet,
        "summary": hr.HTMLSummaryElementRet,
        "table": hr.HTMLTableElementRet,
        "tbody": hr.HTMLTBodyElementRet,
        "td": hr.HTMLTableDataCellElementRet,
        "template": hr.HTMLTemplateElementRet,
        "textarea": hr.HTMLTextAreaElementRet,
        "tfoot": hr.HTMLTFootElementRet,
        "th": hr.HTMLTableHeaderCellElementRet,
        "thead": hr.HTMLTHeadElementRet,
        "tr": hr.HTMLTableRowElementRet,
        "track": hr.HTMLTrackElementRet,
        "ul": hr.HTMLUListElementRet,
    }

    def __init__(self, this):
        super().__init__(None, this)
        self.tag = None

    def generate(self, context):
        self.this.generate(context)
        self.tag = Random.choice(list(CreateInterestingElement.html_elements.keys()))
        self.ret = (CreateInterestingElement.html_elements[self.tag])()
        self.ret.generate(context)

    def mutate(self, _):
        pass

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "var {} = {}.createElement(\"{}\")".format(str(self.ret), str(self.this), self.tag)


class CreateInterestingElementTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)

    def instantiate(self):
        return CreateInterestingElement(self.this_class())

    def satiable(self, context):
        return True


def create_interesting_html_element(context):
    api = CreateInterestingElement(ha.DocumentArg())
    api.generate(context)
    return api


############################################################
# document.createElement(tag);
############################################################
class CreateElement(API):
    html_elements = {
        "a": hr.HTMLAnchorElementRet,
        "abbr": hr.HTMLAbbrElementRet,
        "acronym": hr.HTMLAcronymElementRet,
        "address": hr.HTMLAddressElementRet,
        "area": hr.HTMLAreaElementRet,
        "article": hr.HTMLArticleElementRet,
        "aside": hr.HTMLAsideElementRet,
        "audio": hr.HTMLAudioElementRet,
        "b": hr.HTMLBElementRet,
        "basefont": hr.HTMLBaseFontElementRet,
        "bdi": hr.HTMLBDIElementRet,
        "bdo": hr.HTMLBDOElementRet,
        "bgsound": hr.HTMLBgSoundElementRet,
        "big": hr.HTMLBigElementRet,
        "blockquote": hr.HTMLBlockQuoteElementRet,
        "br": hr.HTMLBRElementRet,
        "button": hr.HTMLButtonElementRet,
        "canvas": hr.HTMLCanvasElementRet,
        "caption": hr.HTMLTableCaptionElementRet,
        "center": hr.HTMLCenterElementRet,
        "cite": hr.HTMLCiteElementRet,
        "code": hr.HTMLCodeElementRet,
        "col": hr.HTMLTableColElementRet,
        "colgroup": hr.HTMLTableColGroupElementRet,
        "command": hr.HTMLCommandElementRet,
        "content": hr.HTMLContentElementRet,
        "data": hr.HTMLDataElementRet,
        "datalist": hr.HTMLDataListElementRet,
        "dd": hr.HTMLDDElementRet,
        "del": hr.HTMLDelElementRet,
        "details": hr.HTMLDetailsElementRet,
        "dfn": hr.HTMLDFNElementRet,
        "dialog": hr.HTMLDialogElementRet,
        "dir": hr.HTMLDirectoryElementRet,
        "div": hr.HTMLDivElementRet,
        "dl": hr.HTMLDListElementRet,
        "dt": hr.HTMLDTElementRet,
        "em": hr.HTMLEMElementRet,
        "embed": hr.HTMLEmbedElementRet,
        "fieldset": hr.HTMLFieldSetElementRet,
        "figcaption": hr.HTMLFigCaptionElementRet,
        "figure": hr.HTMLFigureElementRet,
        "font": hr.HTMLFontElementRet,
        "footer": hr.HTMLFooterElementRet,
        "form": hr.HTMLFormElementRet,
        "frame": hr.HTMLFrameElementRet,
        "frameset": hr.HTMLFrameSetElementRet,
        "h1": hr.HTMLHeading1ElementRet,
        "h2": hr.HTMLHeading2ElementRet,
        "h3": hr.HTMLHeading3ElementRet,
        "h4": hr.HTMLHeading4ElementRet,
        "h5": hr.HTMLHeading5ElementRet,
        "h6": hr.HTMLHeading6ElementRet,
        "header": hr.HTMLHeaderElementRet,
        "hgroup": hr.HTMLHGroupElementRet,
        "hr": hr.HTMLHRElementRet,
        "i": hr.HTMLIElementRet,
        "iframe": hr.HTMLIFrameElementRet,
        "img": hr.HTMLImageElementRet,
        "input": hr.HTMLInputElementRet,
        "ins": hr.HTMLInsElementRet,
        "isindex": hr.HTMLIsIndexElementRet,
        "kbd": hr.HTMLKBDElementRet,
        "keygen": hr.HTMLKeygenElementRet,
        "label": hr.HTMLLabelElementRet,
        "legend": hr.HTMLLegendElementRet,
        "li": hr.HTMLLIElementRet,
        "link": hr.HTMLLinkElementRet,
        "listing": hr.HTMLListingElementRet,
        "main": hr.HTMLMainElementRet,
        "map": hr.HTMLMapElementRet,
        "mark": hr.HTMLMarkElementRet,
        "marquee": hr.HTMLMarqueeElementRet,
        "menu": hr.HTMLMenuElementRet,
        "menuitem": hr.HTMLMenuItemElementRet,
        "meta": hr.HTMLMetaElementRet,
        "meter": hr.HTMLMeterElementRet,
        "nav": hr.HTMLNavElementRet,
        "object": hr.HTMLObjectElementRet,
        "ol": hr.HTMLOListElementRet,
        "optgroup": hr.HTMLOptGroupElementRet,
        "option": hr.HTMLOptionElementRet,
        "output": hr.HTMLOutputElementRet,
        "p": hr.HTMLParagraphElementRet,
        "param": hr.HTMLParamElementRet,
        "picture": hr.HTMLPictureElementRet,
        # "plaintext": hr.HTMLPlainTextElementRet,
        "pre": hr.HTMLPreElementRet,
        "progress": hr.HTMLProgressElementRet,
        "q": hr.HTMLQElementRet,
        "rp": hr.HTMLRPElementRet,
        "rt": hr.HTMLRTElementRet,
        "ruby": hr.HTMLRubyElementRet,
        "s": hr.HTMLSElementRet,
        "samp": hr.HTMLSampElementRet,
        "script": hr.HTMLScriptElementRet,
        "section": hr.HTMLSectionElementRet,
        "select": hr.HTMLSelectElementRet,
        "shadow": hr.HTMLShadowElementRet,
        "slot": hr.HTMLSlotElementRet,
        "small": hr.HTMLSmallElementRet,
        "source": hr.HTMLSourceElementRet,
        "span": hr.HTMLSpanElementRet,
        "strike": hr.HTMLStrikeElementRet,
        "strong": hr.HTMLStrongElementRet,
        "style": hr.HTMLStyleElementRet,
        "sub": hr.HTMLSubElementRet,
        "summary": hr.HTMLSummaryElementRet,
        "sup": hr.HTMLSupElementRet,
        "table": hr.HTMLTableElementRet,
        "tbody": hr.HTMLTBodyElementRet,
        "td": hr.HTMLTableDataCellElementRet,
        "template": hr.HTMLTemplateElementRet,
        "textarea": hr.HTMLTextAreaElementRet,
        "tfoot": hr.HTMLTFootElementRet,
        "th": hr.HTMLTableHeaderCellElementRet,
        "thead": hr.HTMLTHeadElementRet,
        "time": hr.HTMLTimeElementRet,
        "title": hr.HTMLTitleElementRet,
        "tr": hr.HTMLTableRowElementRet,
        "track": hr.HTMLTrackElementRet,
        "tt": hr.HTMLTTElementRet,
        "u": hr.HTMLUElementRet,
        "ul": hr.HTMLUListElementRet,
        "var": hr.HTMLVarElementRet,
        "video": hr.HTMLVideoElementRet,
        "wbr": hr.HTMLWBRElementRet,
        "xmp": hr.HTMLXMPElementRet,
    }

    def __init__(self, this):
        super().__init__(None, this)
        self.tag = None

    def generate(self, context):
        self.this.generate(context)
        while True:
            self.tag = Random.choice(docs.html_tags)
            if self.tag in CreateElement.html_elements:
                self.ret = (CreateElement.html_elements[self.tag])()
                break
        self.ret.generate(context)

    def mutate(self, _):
        pass

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "var {} = {}.createElement(\"{}\")".format(str(self.ret), str(self.this), self.tag)


class CreateElementTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)

    def instantiate(self):
        return CreateElement(self.this_class())

    def satiable(self, context):
        return True


def create_html_element(context):
    api = CreateElement(ha.DocumentArg())
    api.generate(context)
    return api


############################################################
# document.createEvent(event_name);
############################################################
class CreateEvent(API):
    events = {
        "InputEvent": hr.InputEventRet,
        "PointerEvent": hr.PointerEventRet,
        "ClipboardEvent": hr.ClipboardEventRet,
        "DragEvent": hr.DragEventRet,
        "ApplicationCacheErrorEvent": hr.ApplicationCacheErrorEventRet,
        "AnimationEvent": hr.AnimationEventRet,
        "MediaQueryListEvent": hr.MediaQueryListEventRet,
        "PromiseRejectionEvent": hr.PromiseRejectionEventRet,
        "AnimationPlaybackEvent": hr.AnimationPlaybackEventRet,
        "BeforeLoadEvent": hr.EventRet,
        "BeforeUnloadEvent": hr.BeforeUnloadEventRet,
        "CompositionEvent": hr.CompositionEventRet,
        "CustomEvent": hr.CustomEventRet,
        "ErrorEvent": hr.ErrorEventRet,
        "FocusEvent": hr.FocusEventRet,
        "HashChangeEvent": hr.HashChangeEventRet,
        "KeyboardEvent": hr.KeyboardEventRet,
        "MessageEvent": hr.MessageEventRet,
        "MouseEvent": hr.MouseEventRet,
        "MutationEvent": hr.MutationEventRet,
        "OverflowEvent": hr.EventRet,
        "PopStateEvent": hr.PopStateEventRet,
        "ProgressEvent": hr.ProgressEventRet,
        "ResourceProgressEvent": hr.ResourceProgressEventRet,
        "SecurityPolicyViolationEvent": hr.SecurityPolicyViolationEventRet,
        "TextEvent": hr.TextEventRet,
        "TransitionEvent": hr.TransitionEventRet,
        "UIEvent": hr.UIEventRet,
        "WebKitAnimationEvent": hr.EventRet,
        "WheelEvent": hr.WheelEventRet,
        "TrackEvent": hr.EventRet,
        "SVGZoomEvent": hr.EventRet,
        "Events": hr.EventRet,
        "HTMLEvents": hr.EventRet,
        "KeyboardEvents": hr.KeyboardEventRet,
        "MouseEvents": hr.MouseEventRet,
        "MutationEvents": hr.MutationEventRet,
        "OrientationEvent": hr.EventRet,
        "SVGEvents": hr.EventRet,
        "SVGZoomEvents": hr.EventRet,
        "UIEvents": hr.UIEventRet,
        "Event": hr.EventRet,
    }

    def __init__(self, this):
        super().__init__(None, this)
        self.event_type = None

    def generate(self, context):
        self.this.generate(context)
        self.event_type, event_class = Random.choice(list(CreateEvent.events.items()))
        self.ret = event_class()
        self.ret.generate(context)

    def mutate(self, _):
        pass

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        return "var {} = {}.createEvent(\"{}\")".format(str(self.ret), str(self.this), self.event_type)


class CreateEventTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)

    def instantiate(self):
        return CreateEvent(self.this_class())

    def satiable(self, context):
        return True


############################################################
# document.all[<int min=0 max=100>%document.all.length].appendChild(<Element>);
############################################################
class DocumentAppendChild(API):
    def __init__(self, this, element, selector):
        super().__init__(None, this)
        self.element = element
        self.selector = selector

    def generate(self, context):
        self.this.generate(context)
        self.element.generate(context)
        self.selector.generate(context)

    def mutate(self, context):
        if Random.bool():
            self.selector.mutate(context)
        else:
            self.element.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.element.merge_fix(merge_map)

    def __str__(self):
        return "{0}.all[{1} % {0}.all.length].appendChild({2})".format(
            str(self.this),
            str(self.selector),
            str(self.element)
        )


class DocumentAppendChildTemplate(APITemplate):
    def __init__(self, this_class, element_class):
        super().__init__(None, this_class)
        self.element_class = element_class
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return DocumentAppendChild(self.this_class(), self.element_class(), self.selector_class())

    def satiable(self, context):
        return is_satiable_arg(self.element_class, context)


############################################################
# cssStyleSheet.deleteRule(index)
############################################################
class DeleteRule(API):
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
        return "{0}.deleteRule({1} % {0}.cssRules.length)".format(
            str(self.this), str(self.selector)
        )


class DeleteRuleTemplate(APITemplate):
    def __init__(self, this_class):
        super().__init__(None, this_class)
        self.selector_class = RandomSelectorArg

    def instantiate(self):
        return DeleteRule(self.this_class(), self.selector_class())

    def satiable(self, context):
        return True


def initialize_html_functions():
    ######################################################
    # CSS
    ######################################################
    # CSSStyleDeclaration
    add_api(SetPropertyTemplate(ha.CSSStyleDeclarationArg))
    add_api(RemovePropertyTemplate(ha.CSSStyleDeclarationArg))
    add_api(ListItemTemplate(None, ha.CSSStyleDeclarationArg))
    add_api(FunctionTemplate(None, ha.CSSStyleDeclarationArg, "getPropertyValue", ha.CSSPropertyNameArg))
    add_api(FunctionTemplate(None, ha.CSSStyleDeclarationArg, "getPropertyPriority", ha.CSSPropertyNameArg))

    # CSSStyleSheet
    add_api(FunctionTemplate(None, ha.CSSStyleSheetArg, "insertRule", ha.CSSStyleRuleValueArg))
    add_api(DeleteRuleTemplate(ha.CSSStyleSheetArg))

    # CSSKeyframesSheet
    add_api(DeleteRuleTemplate(ha.CSSKeyframesSheetArg))

    # CSSKeyframesRule
    add_api(FunctionTemplate(None, ha.CSSKeyframesRuleArg, "appendRule", ha.CSSKeyframeRuleValueArg))
    add_api(FunctionTemplate(None, ha.CSSKeyframesRuleArg, "deleteRule", ha.CSSKeyframeNameArg))
    add_api(FunctionTemplate(None, ha.CSSKeyframesRuleArg, "findRule", ha.CSSKeyframeNameArg))

    # FontFaceSet
    add_api(FunctionTemplate(None, ha.FontFaceSetArg, "load", ha.FontArg))
    add_api(FunctionTemplate(None, ha.FontFaceSetArg, "load", ha.FontArg, StringArg))
    add_api(FunctionTemplate(None, ha.FontFaceSetArg, "check", ha.FontArg))
    add_api(FunctionTemplate(None, ha.FontFaceSetArg, "check", ha.FontArg, StringArg))

    # FontFace
    add_api(FunctionTemplate(None, ha.FontFaceArg, "load"))

    # DocumentOrShadowRoot
    add_api(FunctionTemplate(hr.SelectionRet, ha.DocumentOrShadowRootArg, "getSelection"))
    add_api(FunctionTemplate(hr.ElementRet, ha.DocumentOrShadowRootArg, "elementFromPoint", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(hr.ElementListRet, ha.DocumentOrShadowRootArg, "elementsFromPoint",
                             IntegerArg, IntegerArg))

    # History
    add_api(FunctionTemplate(None, ha.HistoryArg, "pushState", ha.HistoryStateArg, StringArg))
    add_api(FunctionTemplate(None, ha.HistoryArg, "replaceState", ha.HistoryStateArg, StringArg))

    # Window
    add_api(FunctionTemplate(None, ha.WindowArg, "stop"))
    add_api(FunctionTemplate(None, ha.WindowArg, "focus"))
    add_api(FunctionTemplate(None, ha.WindowArg, "blur"))
    add_api(FunctionTemplate(hr.RequestIDRet, ha.WindowArg, "requestAnimationFrame", ha.EventHandlerArg))
    add_api(FunctionTemplate(hr.RequestIDRet, ha.WindowArg, "webkitRequestAnimationFrame", ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "cancelAnimationFrame", ha.RequestIDArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "webkitCancelAnimationFrame", ha.RequestIDArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "webkitCancelRequestAnimationFrame", ha.RequestIDArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "getComputedStyle", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "moveTo", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "moveBy", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "resizeTo", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "resizeBy", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scroll"))
    add_api(FunctionTemplate(None, ha.WindowArg, "scroll", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scroll", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollTo"))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollTo", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollTo", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollBy"))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollBy", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "scrollBy", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(hr.SelectionRet, ha.WindowArg, "getSelection"))
    add_api(FunctionTemplate(None, ha.WindowArg, "find", StringArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "find", StringArg, BooleanArg, BooleanArg, BooleanArg,
                             BooleanArg, BooleanArg, BooleanArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "btoa", StringArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "atob", StringArg))
    add_api(FunctionTemplate(None, ha.WindowArg, "postMessage", StringArg, ConstStringArgWrapper("*")))
    add_api(FunctionTemplate(None, ha.WindowArg, "captureEvents"))
    add_api(FunctionTemplate(None, ha.WindowArg, "releaseEvents"))
    add_api(FunctionTemplate(None, ha.WindowArg, "getComputedStyle", ha.ElementArg))
    add_api(FunctionTemplate(hr.MediaQueryListRet, ha.WindowArg, "matchMedia", ha.MediaQueryArg))

    # MessagePort
    add_api(FunctionTemplate(None, ha.MessagePortArg, "postMessage", StringArg))
    add_api(FunctionTemplate(None, ha.MessagePortArg, "start"))
    add_api(FunctionTemplate(None, ha.MessagePortArg, "close"))

    # MediaQueryList
    add_api(FunctionTemplate(None, ha.MediaQueryListArg, "addListener", ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.MediaQueryListArg, "removeListener", ha.EventHandlerArg))

    # MediaList
    add_api(ListItemTemplate(None, ha.MediaListArg))
    add_api(FunctionTemplate(None, ha.MediaListArg, "appendMedium", ha.MediaQueryArg))
    add_api(FunctionTemplate(None, ha.MediaListArg, "deleteMedium", ha.MediaQueryArg))

    # StyleMedia
    add_api(FunctionTemplate(None, ha.StyleMediaArg, "matchMedium", ha.MediaQueryArg))

    # Navigator
    add_api(FunctionTemplate(None, ha.NavigatorArg, "sendBeacon", StringArg, StringArg))

    # Document
    add_api(DocumentAppendChildTemplate(ha.DocumentArg, ha.ElementArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("backColor"),
                             ConstValueArgWrapper("false"), ColorArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("bold"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("contentReadOnly"),
                             ConstValueArgWrapper("false"), BooleanArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("createLink"),
                             ConstValueArgWrapper("false"), ha.DummyUrlArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("decreaseFontSize"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("delete"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("enableInlineTableEditing"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("enableObjectResizing"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("fontName"),
                             ConstValueArgWrapper("false"), ha.FontArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("fontSize"),
                             ConstValueArgWrapper("false"), IntegerArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("foreColor"),
                             ConstValueArgWrapper("false"), ColorArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("formatBlock"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("forwardDelete"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("heading"),
                             ConstValueArgWrapper("false"), ha.HeadingArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("hiliteColor"),
                             ConstValueArgWrapper("false"), ColorArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("increaseFontSize"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("indent"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertBrOnReturn"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertHorizontalRule"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertHTML"),
                             ConstValueArgWrapper("false"), ha.HTMLStringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertHTML"),
                             ConstValueArgWrapper("false"), StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertImage"),
                             ConstValueArgWrapper("false"), ha.ImageSrcArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertOrderedList"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertUnorderedList"),
                             ConstValueArgWrapper("false"), NullArg))
    # add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertParagraph"),
    #                         ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("insertText"),
                             ConstValueArgWrapper("false"), StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("italic"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("justifyCenter"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("justifyFull"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("justifyLeft"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("justifyRight"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("outdent"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("redo"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("removeFormat"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("selectAll"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("strikeThrough"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("subscript"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("superscript"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("underline"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("undo"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("unlink"),
                             ConstValueArgWrapper("false"), NullArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("useCSS"),
                             ConstValueArgWrapper("false"), BooleanArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "execCommand", ConstStringArgWrapper("styleWithCSS"),
                             ConstValueArgWrapper("false"), BooleanArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "queryCommandEnabled", StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "queryCommandIndeterm", StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "queryCommandState", StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "queryCommandSupported", StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "queryCommandValue", StringArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "exitPointerLock"))
    add_api(FunctionTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "getElementsByTagName", ha.TagArg))
    add_api(FunctionTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "getElementsByTagNameNS",
                             ConstStringArgWrapper("http://www.w3.org/1999/xhtml"), ha.HTMLTagArg))
    add_api(FunctionTemplate(hr.HTMLCollectionRet, ha.DocumentArg, "getElementsByClassName", ha.ClassArg))
    add_api(FunctionTemplate(hr.DocumentFragmentRet, ha.DocumentArg, "createDocumentFragment"))
    add_api(FunctionTemplate(hr.TextRet, ha.DocumentArg, "createTextNode", StringArg))
    add_api(FunctionTemplate(hr.CommentRet, ha.DocumentArg, "createComment", StringArg))
    add_api(FunctionTemplate(hr.RangeRet, ha.DocumentArg, "createRange"))
    add_api(FunctionTemplate(hr.NodeIteratorRet, ha.DocumentArg, "createNodeIterator", ha.ElementArg))
    add_api(FunctionTemplate(hr.NodeIteratorRet, ha.DocumentArg, "createNodeIterator", ha.ElementArg, ha.WhatToShowArg))
    add_api(FunctionTemplate(hr.TreeWalkerRet, ha.DocumentArg, "createTreeWalker", ha.ElementArg))
    add_api(FunctionTemplate(hr.TreeWalkerRet, ha.DocumentArg, "createTreeWalker", ha.ElementArg, ha.WhatToShowArg))
    add_api(FunctionTemplate(hr.ProcessingInstructionRet, ha.DocumentArg, "createProcessingInstruction", StringArg,
                             StringArg))
    add_api(FunctionTemplate(hr.RangeRet, ha.DocumentArg, "caretRangeFromPoint"))
    add_api(FunctionTemplate(hr.RangeRet, ha.DocumentArg, "caretRangeFromPoint", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "captureEvents"))
    add_api(FunctionTemplate(None, ha.DocumentArg, "releaseEvents"))
    add_api(FunctionTemplate(None, ha.DocumentArg, "webkitCancelFullScreen"))
    add_api(FunctionTemplate(None, ha.DocumentArg, "webkitExitFullscreen"))
    add_api(FunctionTemplate(hr.ElementRet, ha.DocumentArg, "querySelector", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(hr.NodeListRet, ha.DocumentArg, "querySelectorAll", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(hr.XPathExpressionRet, ha.DocumentArg, "createExpression", ha.XPathArg))
    add_api(
        FunctionTemplate(hr.XPathExpressionRet, ha.DocumentArg, "createExpression", ha.XPathArg, ha.XPathNSResolverArg))
    add_api(FunctionTemplate(hr.XPathNSResolverRet, ha.DocumentArg, "createNSResolver", ha.ElementArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.DocumentArg, "evaluate", ha.XPathArg, ha.ElementArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.DocumentArg, "evaluate", ha.XPathArg, ha.ElementArg, NullArg,
                             ha.XPathResultTypeArg, ha.XPathResultArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.DocumentArg, "evaluate", ha.XPathArg, ha.DocumentArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.DocumentArg, "evaluate", ha.XPathArg, ha.DocumentArg, NullArg,
                             ha.XPathResultTypeArg, ha.XPathResultArg))
    add_api(FunctionTemplate(None, ha.DocumentArg, "hasFocus"))
    add_api(FunctionTemplate(hr.ElementRet, ha.DocumentArg, "importNode", ha.ElementArg, BooleanArg))
    add_api(FunctionTemplate(hr.ElementRet, ha.DocumentArg, "adoptNode", ha.ElementArg))
    add_api(FunctionTemplate(hr.AttrRet, ha.DocumentArg, "createAttribute", StringArg))
    add_api(FunctionTemplate(hr.AttrRet, ha.DocumentArg, "createAttributeNS",
                             ConstStringArgWrapper("http://www.w3.org/1999/xhtml"), StringArg))

    # DOMImplementation
    add_api(FunctionTemplate(None, ha.DOMImplementationArg, "createDocumentType", StringArg, StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.DOMImplementationArg, "createDocument", StringArg, StringArg))
    add_api(FunctionTemplate(hr.DocumentRet, ha.DOMImplementationArg, "createHTMLDocument", StringArg))
    add_api(FunctionTemplate(None, ha.DOMImplementationArg, "hasFeature"))

    # NamedNodeMap
    add_api(ListItemTemplate(hr.AttrRet, ha.NamedNodeMapArg))
    add_api(FunctionTemplate(None, ha.NamedNodeMapArg, "setNamedItem", ha.AttrArg))

    # EventTarget
    add_api(FunctionTemplate(None, ha.EventTargetArg, "addEventListener", ha.EventTypeArg, ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.EventTargetArg, "addEventListener", ha.EventTypeArg, ha.EventHandlerArg,
                             ha.AddEventListenerOptionsArg))
    add_api(FunctionTemplate(None, ha.EventTargetArg, "removeEventListener", ha.EventTypeArg, ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.EventTargetArg, "dispatchEvent", ha.EventArg))

    # Element
    add_api(FunctionTemplate(None, ha.ElementArg, "click"))
    add_api(FunctionTemplate(None, ha.ElementArg, "blur"))
    add_api(FunctionTemplate(None, ha.ElementArg, "focus"))
    add_api(FunctionTemplate(None, ha.ElementArg, "setPointerCapture", IntegerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "releasePointerCapture", IntegerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "hasPointerCapture", IntegerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "requestPointerLock"))
    # DOM event listeners
    add_api(FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMAttrModified"),
                             ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMCharacterDataModified"),
                             ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMNodeInserted"),
                             ha.EventHandlerArg))
    add_api(
        FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMNodeInsertedIntoDocument"),
                         ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMNodeRemoved"),
                             ha.EventHandlerArg))
    add_api(
        FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMNodeRemovedFromDocument"),
                         ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "addEventListener", ConstStringArgWrapper("DOMSubtreeModified"),
                             ha.EventHandlerArg))
    add_api(RemoveAttributeTemplate(ha.ElementArg))
    add_api(FunctionTemplate(hr.AnimationRet, ha.ElementArg, "animate", ha.KeyFramesArg, ClockInMsArg))
    add_api(FunctionTemplate(hr.AnimationRet, ha.ElementArg, "animate", ha.KeyFramesArg, ha.AnimateOptionsArg))
    add_api(FunctionTemplate(hr.AnimationsRet, ha.ElementArg, "getAnimations"))
    add_api(FunctionTemplate(hr.ElementRet, ha.ElementArg, "querySelector", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(hr.NodeListRet, ha.ElementArg, "querySelectorAll", ha.CSSSelectorValueArg))
    add_api(InsertBeforeTemplate(ha.ElementArg, ha.ElementArg))
    add_api(RemoveChildTemplate(ha.ElementArg))
    add_api(ReplaceChildTemplate(ha.ElementArg, ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "hasChildNodes"))
    add_api(FunctionTemplate(hr.ElementRet, ha.ElementArg, "getRootNode"))
    add_api(FunctionTemplate(hr.ElementRet, ha.ElementArg, "getRootNode", ha.GetRootNodeOptionsArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "normalize"))
    add_api(FunctionTemplate(hr.ElementRet, ha.ElementArg, "cloneNode", BooleanArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "isEqualNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "isSameNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "compareDocumentPosition", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "lookupPrefix", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "lookupNamespaceURI", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "isDefaultNamespace", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "contains", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "appendChild", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "before", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "before", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "after", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "after", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "replaceWith", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "replaceWith", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "remove"))
    add_api(FunctionTemplate(None, ha.ElementArg, "prepend", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "prepend", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "append", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "append", StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "hasAttributes"))
    add_api(FunctionTemplate(hr.ElementRet, ha.ElementArg, "closest", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "matches", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "webkitMatchesSelector", ha.CSSSelectorValueArg))
    add_api(FunctionTemplate(hr.HTMLCollectionRet, ha.ElementArg, "getElementsByTagName", ha.TagArg))
    add_api(FunctionTemplate(hr.HTMLCollectionRet, ha.ElementArg, "getElementsByClassName", ha.ClassArg))
    add_api(
        FunctionTemplate(hr.ElementRet, ha.ElementArg, "insertAdjacentElement", ha.InsertPositionArg, ha.ElementArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "insertAdjacentText", ha.InsertPositionArg, StringArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "insertAdjacentHTML", ha.InsertPositionArg, ha.HTMLStringArg))
    add_api(FunctionTemplate(hr.DOMRectListRet, ha.ElementArg, "getClientRects"))
    add_api(FunctionTemplate(hr.DOMRectRet, ha.ElementArg, "getBoundingClientRect"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollIntoView"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollIntoView", BooleanArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scroll"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scroll", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scroll", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollTo"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollTo", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollTo", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollBy"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollBy", ha.ScrollToOptionsArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollBy", IntegerArg, IntegerArg))
    # add_api(FunctionTemplate(None, ha.ElementArg, "setApplyScroll", ha.EventHandlerArg,
    #                         ConstStringArgWrapper("disable-native-scroll")))
    # add_api(FunctionTemplate(None, ha.ElementArg, "setDistributeScroll", ha.EventHandlerArg,
    #                         ConstStringArgWrapper("disable-native-scroll")))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollIntoViewIfNeeded"))
    add_api(FunctionTemplate(None, ha.ElementArg, "scrollIntoViewIfNeeded", BooleanArg))
    add_api(FunctionTemplate(None, ha.ElementArg, "webkitRequestFullScreen"))

    # ShadowHost
    add_api(FunctionTemplate(hr.ShadowRootRet, ha.ShadowHostArg, "attachShadow", ha.ShadowRootInitArg))

    # CharacterData
    add_api(FunctionTemplate(None, ha.CharacterDataArg, "substringData", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.CharacterDataArg, "appendData", StringArg))
    add_api(FunctionTemplate(None, ha.CharacterDataArg, "insertData", IntegerArg, StringArg))
    add_api(FunctionTemplate(None, ha.CharacterDataArg, "deleteData", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.CharacterDataArg, "replaceData", IntegerArg, IntegerArg, StringArg))

    # NodeIterator
    add_api(FunctionTemplate(hr.ElementRet, ha.NodeIteratorArg, "nextNode"))
    add_api(FunctionTemplate(hr.ElementRet, ha.NodeIteratorArg, "previousNode"))
    add_api(FunctionTemplate(None, ha.NodeIteratorArg, "detach"))

    # NodeFilter
    add_api(FunctionTemplate(None, ha.NodeFilterArg, "acceptNode"))
    add_api(FunctionTemplate(None, ha.NodeFilterArg, "acceptNode", ha.ElementArg))

    # TreeWalker
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "parentNode"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "firstChild"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "lastChild"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "previousSibling"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "nextSibling"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "previousNode"))
    add_api(FunctionTemplate(hr.ElementRet, ha.TreeWalkerArg, "nextNode"))

    # Text
    add_api(FunctionTemplate(hr.TextRet, ha.TextArg, "splitText", IntegerArg))

    # TimeRanges
    add_api(FunctionTemplate(None, ha.TimeRangesArg, "start", IntegerArg))
    add_api(FunctionTemplate(None, ha.TimeRangesArg, "end", IntegerArg))

    # Selection
    add_api(FunctionTemplate(hr.RangeRet, ha.SelectionArg, "getRangeAt", IntegerArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "addRange", ha.RangeArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "removeAllRanges"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "empty"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "collapse", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "collapse", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "setPosition", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "setPosition", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "collapseToStart"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "collapseToEnd"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "extend", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "extend", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "setBaseAndExtent", ha.ElementArg, IntegerArg,
                             ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "selectAllChildren", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "deleteFromDocument"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "containsNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "containsNode", ha.ElementArg, BooleanArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "modify"))
    add_api(FunctionTemplate(None, ha.SelectionArg, "modify", ha.SelectionModifyAlterArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "modify", ha.SelectionModifyAlterArg,
                             ha.SelectionModifyDirectionArg))
    add_api(FunctionTemplate(None, ha.SelectionArg, "modify", ha.SelectionModifyAlterArg,
                             ha.SelectionModifyDirectionArg, ha.SelectionModifyGranularityArg))

    # NodeList
    add_api(ListItemTemplate(hr.ElementRet, ha.NodeListArg))

    # HTMLCollection
    add_api(ListItemTemplate(hr.ElementRet, ha.HTMLCollectionArg))

    # HTMLAllCollection
    add_api(ListItemTemplate(hr.ElementRet, ha.HTMLAllCollectionArg))

    # HTMLOptionsCollection
    add_api(ListItemTemplate(hr.HTMLOptionElementRet, ha.HTMLOptionsCollectionArg))
    add_api(ListAddTemplate(ha.HTMLOptionsCollectionArg, ha.HTMLOptionElementArg))
    add_api(ListAddTemplate(ha.HTMLOptionsCollectionArg, ha.HTMLOptGroupElementArg))
    add_api(ListRemoveTemplate(ha.HTMLOptionsCollectionArg))

    # HTMLAreasCollection
    add_api(ListItemTemplate(hr.HTMLAreaElementRet, ha.HTMLAreasCollectionArg))

    # LabelElementList
    add_api(ListItemTemplate(hr.HTMLLabelElementRet, ha.HTMLLabelElementListArg))

    # AnimationTimeline
    add_api(FunctionTemplate(hr.AnimationsRet, ha.AnimationTimelineArg, "getAnimations"))

    # Animation
    add_api(ConstructTemplate(hr.AnimationRet, "Animation", ha.KeyframeEffectArg))
    add_api(ConstructTemplate(hr.AnimationRet, "Animation", ha.KeyframeEffectArg, ha.AnimationTimelineArg))
    add_api(FunctionTemplate(None, ha.AnimationArg, "finish"))
    add_api(FunctionTemplate(None, ha.AnimationArg, "play"))
    add_api(FunctionTemplate(None, ha.AnimationArg, "pause"))
    add_api(FunctionTemplate(None, ha.AnimationArg, "reverse"))
    add_api(FunctionTemplate(None, ha.AnimationArg, "cancel"))

    # AnimationEffectReadOnly
    add_api(FunctionTemplate(None, ha.AnimationEffectReadOnlyArg, "getComputedTiming"))

    # KeyframeEffect
    add_api(ConstructTemplate(hr.KeyframeEffectRet, "KeyframeEffect", ha.ElementArg, ha.KeyFramesArg))
    add_api(ConstructTemplate(hr.KeyframeEffectRet, "KeyframeEffect", ha.ElementArg, ha.KeyFramesArg, ClockInMsArg))
    add_api(ConstructTemplate(hr.KeyframeEffectRet, "KeyframeEffect", ha.ElementArg, ha.KeyFramesArg, ha.AnimateOptionsArg))

    # TextTrack
    add_api(FunctionTemplate(None, ha.TextTrackArg, "addCue", ha.TextTrackCueArg))
    add_api(FunctionTemplate(None, ha.TextTrackArg, "removeCue", ha.TextTrackCueArg))
    add_api(FunctionTemplate(None, ha.TextTrackArg, "addRegion", ha.VTTRegionArg))
    add_api(FunctionTemplate(None, ha.TextTrackArg, "removeRegion", ha.VTTRegionArg))

    # VTTRegionList
    add_api(ListItemTemplate(hr.VTTRegionRet, ha.VTTRegionListArg))

    # VTTCue
    add_api(ConstructTemplate(hr.VTTCueRet, "VTTCue", FloatArg, FloatArg, StringArg))
    add_api(FunctionTemplate(hr.DocumentFragmentRet, ha.VTTCueArg, "getCueAsHTML"))

    # HTMLMediaElement
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "load"))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "pause"))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "play"))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "canPlayType", ha.MediaTypeArg))
    add_api(FunctionTemplate(hr.TextTrackRet, ha.HTMLMediaElementArg, "addTextTrack", ha.TrackKindArg))
    add_api(FunctionTemplate(hr.TextTrackRet, ha.HTMLMediaElementArg, "addTextTrack", ha.TrackKindArg, ha.StringArg))
    add_api(FunctionTemplate(hr.TextTrackRet, ha.HTMLMediaElementArg, "addTextTrack", ha.TrackKindArg, ha.StringArg,
                             ha.LangArg))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "fastSeek", ClockArg))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "getStartDate"))
    add_api(FunctionTemplate(hr.VideoPlaybackQualityRet, ha.HTMLMediaElementArg, "getVideoPlaybackQuality"))
    add_api(FunctionTemplate(None, ha.HTMLMediaElementArg, "webkitShowPlaybackTargetPicker"))

    # HTMLButtonElement
    add_api(FunctionTemplate(None, ha.HTMLButtonElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLButtonElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLButtonElementArg, "setCustomValidity", StringArg))

    # HTMLTableElement
    add_api(FunctionTemplate(hr.HTMLTableCaptionElementRet, ha.HTMLTableElementArg, "createCaption"))
    add_api(FunctionTemplate(None, ha.HTMLTableElementArg, "deleteCaption"))
    add_api(FunctionTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableElementArg, "createTHead"))
    add_api(FunctionTemplate(None, ha.HTMLTableElementArg, "deleteTHead"))
    add_api(FunctionTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableElementArg, "createTFoot"))
    add_api(FunctionTemplate(None, ha.HTMLTableElementArg, "deleteTFoot"))
    add_api(FunctionTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableElementArg, "createTBody"))
    add_api(FunctionTemplate(hr.HTMLTableRowElementRet, ha.HTMLTableElementArg, "insertRow"))
    add_api(FunctionTemplate(hr.HTMLTableRowElementRet, ha.HTMLTableElementArg, "insertRow", IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLTableElementArg, "deleteRow", IntegerArg))

    add_api(ListItemTemplate(hr.HTMLTableSectionElementRet, ha.HTMLTableSectionsCollectionArg))
    add_api(ListItemTemplate(hr.HTMLTableRowElementRet, ha.HTMLTableRowsCollectionArg))

    # HTMLDialogElement
    add_api(FunctionTemplate(None, ha.HTMLDialogElementArg, "show"))
    add_api(FunctionTemplate(None, ha.HTMLDialogElementArg, "showModal"))
    add_api(FunctionTemplate(None, ha.HTMLDialogElementArg, "close"))
    add_api(FunctionTemplate(None, ha.HTMLDialogElementArg, "close", StringArg))

    # HTMLTextAreaElement
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setCustomValidity", StringArg))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "select"))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setRangeText", StringArg))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setRangeText", StringArg, IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setRangeText", StringArg, IntegerArg,
                             ha.SelectModeArg))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setSelectionRange", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLTextAreaElementArg, "setSelectionRange", IntegerArg, IntegerArg,
                             ha.SelectionDirectionArg))

    # HTMLFormElement
    add_api(FunctionTemplate(None, ha.HTMLFormElementArg, "submit"))
    add_api(FunctionTemplate(None, ha.HTMLFormElementArg, "reset"))
    add_api(FunctionTemplate(None, ha.HTMLFormElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLFormElementArg, "reportValidity"))

    # HTMLSlotElement
    add_api(FunctionTemplate(hr.HTMLElementListRet, ha.HTMLSlotElementArg, "assignedNodes"))
    add_api(FunctionTemplate(hr.HTMLElementListRet, ha.HTMLSlotElementArg, "assignedNodes", ha.AssignedNodesOptionArg))

    # HTMLKeygenElement
    add_api(FunctionTemplate(None, ha.HTMLKeygenElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLKeygenElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLKeygenElementArg, "setCustomValidity", StringArg))

    # HTMLTableRowElement
    add_api(FunctionTemplate(hr.HTMLTableCellElementRet, ha.HTMLTableRowElementArg, "insertCell"))
    add_api(FunctionTemplate(hr.HTMLTableCellElementRet, ha.HTMLTableRowElementArg, "insertCell", IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLTableRowElementArg, "deleteCell", IntegerArg))

    # HTMLTableCellElements
    add_api(ListItemTemplate(hr.HTMLTableCellElementRet, ha.HTMLTableCellsCollectionArg))

    # HTMLObjectElement
    add_api(FunctionTemplate(None, ha.HTMLObjectElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLObjectElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLObjectElementArg, "setCustomValidity", StringArg))

    # HTMLSelectElement
    add_api(ListAddTemplate(ha.HTMLSelectElementArg, ha.HTMLOptionElementArg))
    add_api(ListAddTemplate(ha.HTMLSelectElementArg, ha.HTMLOptGroupElementArg))
    add_api(ListRemoveTemplate(ha.HTMLSelectElementArg))
    add_api(FunctionTemplate(None, ha.HTMLSelectElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLSelectElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLSelectElementArg, "setCustomValidity", StringArg))

    # HTMLCanvasElement
    add_api(FunctionTemplate(None, ha.HTMLCanvasElementArg, "toDataURL"))
    add_api(FunctionTemplate(None, ha.HTMLCanvasElementArg, "toDataURL", ha.ImageTypeArg, Float01Arg))
    add_api(FunctionTemplate(None, ha.HTMLCanvasElementArg, "toBlob", ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.HTMLCanvasElementArg, "toBlob", ha.EventHandlerArg, ha.ImageTypeArg, Float01Arg))

    # HTMLOutputElement
    add_api(FunctionTemplate(None, ha.HTMLOutputElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLOutputElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLOutputElementArg, "setCustomValidity", StringArg))

    # HTMLVideoElement
    add_api(FunctionTemplate(None, ha.HTMLVideoElementArg, "webkitEnterFullscreen"))
    add_api(FunctionTemplate(None, ha.HTMLVideoElementArg, "webkitExitFullscreen"))

    # HTMLTableSectionElement
    add_api(FunctionTemplate(hr.HTMLTableRowElementRet, ha.HTMLTableSectionElementArg, "insertRow"))
    add_api(FunctionTemplate(hr.HTMLTableRowElementRet, ha.HTMLTableSectionElementArg, "insertRow", IndexArg))
    add_api(TableSectionDeleteRowTemplate(ha.HTMLTableSectionElementArg))

    # HTMLFieldSetElement
    add_api(FunctionTemplate(None, ha.HTMLFieldSetElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLFieldSetElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLFieldSetElementArg, "setCustomValidity", StringArg))

    # HTMLShadowElement
    add_api(FunctionTemplate(hr.NodeListRet, ha.HTMLShadowElementArg, "getDistributedNodes"))

    # HTMLInputElement
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "stepUp"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "stepUp", IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "stepDown"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "stepDown", IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "checkValidity"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "reportValidity"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setCustomValidity", StringArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "select"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setRangeText", StringArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setRangeText", StringArg, IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setRangeText", StringArg, IntegerArg,
                             ha.SelectModeArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setSelectionRange"))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setSelectionRange", IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setSelectionRange", IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.HTMLInputElementArg, "setSelectionRange", IntegerArg, IntegerArg,
                             ha.SelectionDirectionArg))

    # HTMLMarqueeElement
    add_api(FunctionTemplate(None, ha.HTMLMarqueeElementArg, "start"))
    add_api(FunctionTemplate(None, ha.HTMLMarqueeElementArg, "stop"))

    # HTMLContentElement
    add_api(FunctionTemplate(hr.NodeListRet, ha.HTMLContentElementArg, "getDistributedNodes"))

    # HTMLStyleElement
    add_api(FunctionTemplate(None, ha.HTMLStyleElementArg, "appendChild", ha.CSSStyleRuleValueTextArg))

    # createElement
    add_api(CreateElementTemplate(ha.DocumentArg))
    add_api(CreateInterestingElementTemplate(ha.DocumentArg))

    # setAttribute
    add_api(SetAttributeTemplate(ha.HTMLAbbrElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAcronymElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAddressElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAnchorElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAreaElementArg))
    add_api(SetAttributeTemplate(ha.HTMLArticleElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAsideElementArg))
    add_api(SetAttributeTemplate(ha.HTMLAudioElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBDIElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBDOElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBRElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBaseFontElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBgSoundElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBigElementArg))
    add_api(SetAttributeTemplate(ha.HTMLBlockQuoteElementArg))
    add_api(SetAttributeTemplate(ha.HTMLButtonElementArg))
    add_api(SetAttributeTemplate(ha.HTMLCanvasElementArg))
    add_api(SetAttributeTemplate(ha.HTMLCenterElementArg))
    add_api(SetAttributeTemplate(ha.HTMLCiteElementArg))
    add_api(SetAttributeTemplate(ha.HTMLCodeElementArg))
    add_api(SetAttributeTemplate(ha.HTMLCommandElementArg))
    add_api(SetAttributeTemplate(ha.HTMLContentElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDDElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDFNElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDListElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDTElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDataElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDataListElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDelElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDetailsElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDialogElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDirectoryElementArg))
    add_api(SetAttributeTemplate(ha.HTMLDivElementArg))
    add_api(SetAttributeTemplate(ha.HTMLEMElementArg))
    add_api(SetAttributeTemplate(ha.HTMLEmbedElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFieldSetElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFigCaptionElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFigureElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFontElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFooterElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFormElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFrameElementArg))
    add_api(SetAttributeTemplate(ha.HTMLFrameSetElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHGroupElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHRElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeaderElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading1ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading2ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading3ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading4ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading5ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLHeading6ElementArg))
    add_api(SetAttributeTemplate(ha.HTMLIElementArg))
    add_api(SetAttributeTemplate(ha.HTMLIFrameElementArg))
    add_api(SetAttributeTemplate(ha.HTMLImageElementArg))
    add_api(SetAttributeTemplate(ha.HTMLInputElementArg))
    add_api(SetAttributeTemplate(ha.HTMLInsElementArg))
    add_api(SetAttributeTemplate(ha.HTMLIsIndexElementArg))
    add_api(SetAttributeTemplate(ha.HTMLKBDElementArg))
    add_api(SetAttributeTemplate(ha.HTMLKeygenElementArg))
    add_api(SetAttributeTemplate(ha.HTMLLIElementArg))
    add_api(SetAttributeTemplate(ha.HTMLLabelElementArg))
    add_api(SetAttributeTemplate(ha.HTMLLegendElementArg))
    add_api(SetAttributeTemplate(ha.HTMLLinkElementArg))
    add_api(SetAttributeTemplate(ha.HTMLListingElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMainElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMapElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMarkElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMarqueeElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMenuElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMenuItemElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMetaElementArg))
    add_api(SetAttributeTemplate(ha.HTMLMeterElementArg))
    add_api(SetAttributeTemplate(ha.HTMLNavElementArg))
    add_api(SetAttributeTemplate(ha.HTMLOListElementArg))
    add_api(SetAttributeTemplate(ha.HTMLObjectElementArg))
    add_api(SetAttributeTemplate(ha.HTMLOptGroupElementArg))
    add_api(SetAttributeTemplate(ha.HTMLOptionElementArg))
    add_api(SetAttributeTemplate(ha.HTMLOutputElementArg))
    add_api(SetAttributeTemplate(ha.HTMLParagraphElementArg))
    add_api(SetAttributeTemplate(ha.HTMLParamElementArg))
    add_api(SetAttributeTemplate(ha.HTMLPictureElementArg))
    add_api(SetAttributeTemplate(ha.HTMLPlainTextElementArg))
    add_api(SetAttributeTemplate(ha.HTMLPreElementArg))
    add_api(SetAttributeTemplate(ha.HTMLProgressElementArg))
    add_api(SetAttributeTemplate(ha.HTMLQElementArg))
    add_api(SetAttributeTemplate(ha.HTMLRPElementArg))
    add_api(SetAttributeTemplate(ha.HTMLRTElementArg))
    add_api(SetAttributeTemplate(ha.HTMLRubyElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSampElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSectionElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSelectElementArg))
    add_api(SetAttributeTemplate(ha.HTMLShadowElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSlotElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSmallElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSourceElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSpanElementArg))
    add_api(SetAttributeTemplate(ha.HTMLStrikeElementArg))
    add_api(SetAttributeTemplate(ha.HTMLStrongElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSubElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSummaryElementArg))
    add_api(SetAttributeTemplate(ha.HTMLSupElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTBodyElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTFootElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTHeadElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTTElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableCaptionElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableColElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableColGroupElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableDataCellElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableHeaderCellElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTableRowElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTemplateElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTextAreaElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTimeElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTitleElementArg))
    add_api(SetAttributeTemplate(ha.HTMLTrackElementArg))
    add_api(SetAttributeTemplate(ha.HTMLUElementArg))
    add_api(SetAttributeTemplate(ha.HTMLUListElementArg))
    add_api(SetAttributeTemplate(ha.HTMLVarElementArg))
    add_api(SetAttributeTemplate(ha.HTMLVideoElementArg))
    add_api(SetAttributeTemplate(ha.HTMLWBRElementArg))
    add_api(SetAttributeTemplate(ha.HTMLXMPElementArg))

    ######################################################
    # Event
    ######################################################
    # createEvent
    add_api(CreateEventTemplate(ha.DocumentArg))

    # DataTransfer
    add_api(FunctionTemplate(None, ha.DataTransferArg, "setDragImage", ha.ElementArg, IntegerArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.DataTransferArg, "getData", StringArg))
    add_api(FunctionTemplate(None, ha.DataTransferArg, "setData", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.DataTransferArg, "clearData"))
    add_api(FunctionTemplate(None, ha.DataTransferArg, "clearData", StringArg))

    # DataTransferItemList
    add_api(FunctionTemplate(None, ha.DataTransferItemListArg, "add", StringArg, StringArg))
    add_api(ListRemoveTemplate(ha.DataTransferItemListArg))
    add_api(FunctionTemplate(None, ha.DataTransferItemListArg, "clear"))

    # DataTransferItem
    add_api(FunctionTemplate(None, ha.DataTransferItemArg, "getAsString", ha.EventHandlerArg))
    add_api(FunctionTemplate(hr.BlobRet, ha.DataTransferItemArg, "getAsFile"))

    # Event
    add_api(FunctionTemplate(None, ha.EventArg, "stopPropagation"))
    add_api(FunctionTemplate(None, ha.EventArg, "stopImmediatePropagation"))
    add_api(FunctionTemplate(None, ha.EventArg, "preventDefault"))
    add_api(FunctionTemplate(None, ha.EventArg, "initEvent", ha.EventTypeArg, BooleanArg, BooleanArg))
    add_api(FunctionTemplate(hr.EventTargetsRet, ha.EventArg, "composedPath"))

    # UIEvent
    add_api(FunctionTemplate(None, ha.UIEventArg, "initUIEvent", ha.UIEventTypeArg, BooleanArg, BooleanArg,
                             ha.WindowArg, StringArg))

    # CompositionEvent
    add_api(FunctionTemplate(None, ha.CompositionEventArg, "initCompositionEvent", ha.CompositionEventTypeArg,
                             BooleanArg, BooleanArg, ha.WindowArg, StringArg))

    # TextEvent
    add_api(FunctionTemplate(None, ha.TextEventArg, "initTextEvent", ha.TextEventTypeArg, BooleanArg, BooleanArg,
                             ha.WindowArg, StringArg))

    # MouseEvent
    add_api(FunctionTemplate(None, ha.MouseEventArg, "getModifierState", BooleanArg))
    add_api(FunctionTemplate(None, ha.MouseEventArg, "initMouseEvent", ha.MouseEventTypeArg, BooleanArg, BooleanArg,
                             ha.WindowArg, IntegerArg, IntegerArg, IntegerArg, IntegerArg, IntegerArg,
                             BooleanArg, BooleanArg, BooleanArg, BooleanArg, ha.MouseButtonTypeArg, ha.EventTargetArg))

    # StaticRange
    add_api(FunctionTemplate(None, ha.StaticRangeArg, "setStart", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.StaticRangeArg, "setEnd", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(hr.RangeRet, ha.StaticRangeArg, "toRange"))

    # InputEvent
    add_api(FunctionTemplate(hr.StaticRangesRet, ha.InputEventArg, "getTargetRanges"))

    # MessageEvent
    add_api(FunctionTemplate(None, ha.MessageEventArg, "initMessageEvent", ha.MessageEventTypeArg, BooleanArg,
                             BooleanArg, StringArg, StringArg, StringArg, ha.WindowArg))  # FIXME: message port

    # MutationEvent
    add_api(FunctionTemplate(None, ha.MutationEventArg, "initMutationEvent", ha.MutationEventTypeArg, BooleanArg,
                             BooleanArg, ha.ElementArg, StringArg, StringArg, StringArg, ha.AttrChangeTypeArg))

    # KeyboardEvent
    add_api(FunctionTemplate(None, ha.KeyboardEventArg, "getModifierState", CharArg))
    add_api(FunctionTemplate(None, ha.KeyboardEventArg, "initKeyboardEvent", ha.KeyboardEventTypeArg, BooleanArg,
                             BooleanArg, ha.WindowArg, CharArg, CharArg, ha.KeyLocationTypeArg, StringArg, BooleanArg))

    # CustomEvent
    add_api(FunctionTemplate(None, ha.CustomEventArg, "initCustomEvent", StringArg, BooleanArg, BooleanArg, StringArg))

    ######################################################
    # Web Animations
    ######################################################
    # AnimationEffectTiming
    add_api(ConstructObjectTemplate(hr.AnimationEffectTimingRet, {
        "delay": ClockInMsArg, "direction": ha.AnimationDirectionArg, "duration": ClockInMsArg,
        "easing": ha.AnimationEasingArg, "endDelay": ClockInMsArg, "fill": ha.AnimationFillArg,
        "iterationStart": FloatArg, "iterations": IntegerArg
    }))

    ######################################################
    # Misc
    ######################################################
    # Range
    add_api(FunctionTemplate(hr.DocumentFragmentRet, ha.RangeArg, "cloneContents"))
    add_api(FunctionTemplate(hr.RangeRet, ha.RangeArg, "cloneRange"))
    add_api(FunctionTemplate(None, ha.RangeArg, "collapse", BooleanArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "compareBoundaryPoints", ha.RangeCompareArg, ha.RangeArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "compareNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "comparePoint", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(hr.DocumentFragmentRet, ha.RangeArg, "createContextualFragment", StringArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "deleteContents"))
    add_api(FunctionTemplate(None, ha.RangeArg, "detach"))
    add_api(FunctionTemplate(hr.DocumentFragmentRet, ha.RangeArg, "extractContents"))
    add_api(FunctionTemplate(None, ha.RangeArg, "expand"))
    add_api(FunctionTemplate(None, ha.RangeArg, "expand", StringArg))
    add_api(FunctionTemplate(hr.DOMRectRet, ha.RangeArg, "getBoundingClientRect"))
    add_api(FunctionTemplate(hr.DOMRectListRet, ha.RangeArg, "getClientRects"))
    add_api(FunctionTemplate(None, ha.RangeArg, "insertNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "intersectsNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "isPointInRange", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "selectNode", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "selectNodeContents", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setEnd", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setEndAfter", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setEndBefore", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setStart", ha.ElementArg, IntegerArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setStartAfter", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "setStartBefore", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.RangeArg, "surroundContents", ha.ElementArg))

    # ApplicationCache
    add_api(FunctionTemplate(None, ha.ApplicationCacheArg, "update"))
    add_api(FunctionTemplate(None, ha.ApplicationCacheArg, "abort"))
    add_api(FunctionTemplate(None, ha.ApplicationCacheArg, "swapCache"))

    # XPathEvaluator
    # |evaluate| is a bit different from domato.
    add_api(ConstructTemplate(hr.XPathEvaluatorRet, "XPathEvaluator"))
    add_api(FunctionTemplate(hr.XPathExpressionRet, ha.XPathEvaluatorArg, "createExpression", ha.XPathArg))
    add_api(FunctionTemplate(hr.XPathExpressionRet, ha.XPathEvaluatorArg, "createExpression", ha.XPathArg,
                             ha.XPathNSResolverArg))
    add_api(FunctionTemplate(hr.XPathNSResolverRet, ha.XPathEvaluatorArg, "createNSResolver", ha.ElementArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathEvaluatorArg, "evaluate", ha.XPathArg, ha.ElementArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathEvaluatorArg, "evaluate", ha.XPathArg, ha.ElementArg, NullArg,
                             ha.XPathResultTypeArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathEvaluatorArg, "evaluate", ha.XPathArg, ha.DocumentArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathEvaluatorArg, "evaluate", ha.XPathArg, ha.DocumentArg, NullArg,
                             ha.XPathResultTypeArg))

    # XPathResult
    add_api(FunctionTemplate(hr.ElementRet, ha.XPathResultArg, "iterateNext"))
    add_api(SnapshotItemTemplate(hr.ElementRet, ha.XPathResultArg))

    # XMLSerializer
    add_api(ConstructTemplate(hr.XMLSerializerRet, "XMLSerializer"))
    add_api(FunctionTemplate(None, ha.XMLSerializerArg, "serializeToString", ha.ElementArg))

    # DOMParser
    add_api(ConstructTemplate(hr.DOMParserRet, "DOMParser"))
    add_api(FunctionTemplate(hr.DocumentRet, ha.DOMParserArg, "parseFromString", ConstStringArgWrapper(""),
                             ConstStringArgWrapper("text/html")))
    add_api(FunctionTemplate(hr.DocumentRet, ha.DOMParserArg, "parseFromString", ha.HTMLStringArg, ha.ContentTypeArg))
    add_api(FunctionTemplate(hr.DocumentRet, ha.DOMParserArg, "parseFromString", ha.HTMLStringArg,
                             ConstStringArgWrapper("text/html")))

    # XPathNSResolver
    add_api(FunctionTemplate(None, ha.XPathNSResolverArg, "lookupNamespaceURI"))
    add_api(FunctionTemplate(None, ha.XPathNSResolverArg, "lookupNamespaceURI", StringArg))

    # XPathExpression
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathExpressionArg, "evaluate", ha.ElementArg))
    add_api(FunctionTemplate(hr.XPathResultRet, ha.XPathExpressionArg, "evaluate", ha.ElementArg,
                             ha.XPathResultTypeArg, ha.XPathResultArg))

    # XSLTProcessor
    add_api(ConstructTemplate(hr.XSLTProcessorRet, "XSLTProcessor"))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "importStylesheet", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "transformToFragment", ha.ElementArg, ha.DocumentArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "transformToDocument", ha.ElementArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "setParameter", StringArg, StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "getParameter", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "removeParameter", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "clearParameters"))
    add_api(FunctionTemplate(None, ha.XSLTProcessorArg, "reset"))

    # CustomElementRegistry
    add_api(FunctionTemplate(None, ha.CustomElementRegistryArg, "define", ha.CustomElementNameArg, DoNothingArg))
    add_api(FunctionTemplate(None, ha.CustomElementRegistryArg, "get", ha.CustomElementNameArg))
    add_api(FunctionTemplate(None, ha.CustomElementRegistryArg, "whenDefined", ha.CustomElementNameArg))

    # MutationObserver
    add_api(ConstructTemplate(hr.MutationObserverRet, "MutationObserver", ha.EventHandlerArg))
    add_api(FunctionTemplate(None, ha.MutationObserverArg, "observe", ha.ElementArg, ha.MutationObserverInitArg))
    add_api(FunctionTemplate(None, ha.MutationObserverArg, "disconnect"))
    add_api(FunctionTemplate(hr.MutationRecordsRet, ha.MutationObserverArg, "takeRecords"))

    # MessageChannel
    add_api(ConstructTemplate(hr.MessageChannelRet, "MessageChannel"))

    # URL
    add_api(ConstructTemplate(hr.URLRet, "URL", ConstStringArgWrapper("http://foo/bar")))

    # FormData
    add_api(ConstructTemplate(hr.FormDataRet, "FormData"))
    add_api(FunctionTemplate(None, ha.FormDataArg, "append", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "append", StringArg, StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "delete", StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "has", StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "get", StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "getAll", StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "set", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.FormDataArg, "set", StringArg, StringArg, StringArg))

    # URLSearchParams
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "set", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "append", StringArg, StringArg))
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "delete", StringArg))
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "has", StringArg))
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "get", StringArg))
    add_api(FunctionTemplate(None, ha.URLSearchParamsArg, "getAll", StringArg))

    # DOMTokenList
    add_api(ListItemTemplate(None, ha.DOMTokenListArg))
    add_api(ListRemoveTemplate(ha.DOMTokenListArg))
    add_api(FunctionTemplate(None, ha.DOMTokenListArg, "add", StringArg))
    add_api(FunctionTemplate(None, ha.DOMTokenListArg, "contains", StringArg))
    add_api(FunctionTemplate(None, ha.DOMTokenListArg, "supports", StringArg))
    add_api(FunctionTemplate(None, ha.DOMTokenListArg, "toggle", StringArg, BooleanArg))
