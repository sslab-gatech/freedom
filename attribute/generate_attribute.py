HTML_ELEMENT_MAP = {
    # Text content
    "HTMLAnchorElement": "a",
    "HTMLAbbrElement": "abbr",
    "HTMLAcronymElement": "acronym",
    "HTMLAddressElement": "address",
    # "HTMLAppletElement": "applet",
    "HTMLAreaElement": "area",
    "HTMLArticleElement": "article",
    "HTMLAsideElement": "aside",
    "HTMLAudioElement": "audio",
    "HTMLBElement": "b",
    # "HTMLBaseElement": "base",
    "HTMLBaseFontElement": "basefont",
    "HTMLBDIElement": "bdi",
    "HTMLBDOElement": "bdo",
    "HTMLBgSoundElement": "bgsound",
    "HTMLBigElement": "big",
    "HTMLBlockQuoteElement": "blockquote",
    # "HTMLBodyElement": "body",
    "HTMLBRElement": "br",
    "HTMLButtonElement": "button",
    "HTMLCanvasElement": "canvas",
    "HTMLTableCaptionElement": "caption",
    "HTMLCenterElement": "center",
    "HTMLCiteElement": "cite",
    "HTMLCodeElement": "code",
    "HTMLTableColElement": "col",
    "HTMLTableColGroupElement": "colgroup",
    "HTMLCommandElement": "command",
    "HTMLContentElement": "content",
    "HTMLDataElement": "data",
    "HTMLDataListElement": "datalist",
    "HTMLDDElement": "dd",
    "HTMLDelElement": "del",
    "HTMLDetailsElement": "details",
    "HTMLDFNElement": "dfn",
    "HTMLDialogElement": "dialog",
    "HTMLDirectoryElement": "dir",
    "HTMLDivElement": "div",
    "HTMLDListElement": "dl",
    "HTMLDTElement": "dt",
    "HTMLEMElement": "em",
    "HTMLEmbedElement": "embed",
    "HTMLFieldSetElement": "fieldset",
    "HTMLFigCaptionElement": "figcaption",
    "HTMLFigureElement": "figure",
    "HTMLFontElement": "font",
    "HTMLFooterElement": "footer",
    "HTMLFormElement": "form",
    "HTMLFrameElement": "frame",
    "HTMLFrameSetElement": "frameset",
    "HTMLHeading1Element": "h1",
    "HTMLHeading2Element": "h2",
    "HTMLHeading3Element": "h3",
    "HTMLHeading4Element": "h4",
    "HTMLHeading5Element": "h5",
    "HTMLHeading6Element": "h6",
    # "HTMLHeadElement": "head",
    "HTMLHeaderElement": "header",
    "HTMLHGroupElement": "hgroup",
    "HTMLHRElement": "hr",
    # "HTMLHtmlElement": "html",
    "HTMLIElement": "i",
    "HTMLIFrameElement": "iframe",
    # "HTMLImageElement": "image",
    "HTMLImageElement": "img",
    "HTMLInputElement": "input",
    "HTMLInsElement": "ins",
    "HTMLIsIndexElement": "isindex",
    "HTMLKBDElement": "kbd",
    "HTMLKeygenElement": "keygen",
    "HTMLLabelElement": "label",
    # "HTMLLayerElement": "layer",
    "HTMLLegendElement": "legend",
    "HTMLLIElement": "li",
    "HTMLLinkElement": "link",
    "HTMLListingElement": "listing",
    "HTMLMainElement": "main",
    "HTMLMapElement": "map",
    "HTMLMarkElement": "mark",
    "HTMLMarqueeElement": "marquee",
    "HTMLMenuElement": "menu",
    "HTMLMenuItemElement": "menuitem",
    "HTMLMetaElement": "meta",
    "HTMLMeterElement": "meter",
    "HTMLNavElement": "nav",
    # "HTMLNoBRElement": "nobr",
    # "HTMLNoEmbedElement": "noembed",
    # "HTMLNoFramesElement": "noframes",
    # "HTMLNoLayerElement": "nolayer",
    # "HTMLNoScriptElement": "noscript",
    "HTMLObjectElement": "object",
    "HTMLOListElement": "ol",
    "HTMLOptGroupElement": "optgroup",
    "HTMLOptionElement": "option",
    "HTMLOutputElement": "output",
    "HTMLParagraphElement": "p",
    "HTMLParamElement": "param",
    "HTMLPictureElement": "picture",
    "HTMLPlainTextElement": "plaintext",
    "HTMLPreElement": "pre",
    "HTMLProgressElement": "progress",
    "HTMLQElement": "q",
    "HTMLRPElement": "rp",
    "HTMLRTElement": "rt",
    "HTMLRubyElement": "ruby",
    "HTMLSElement": "s",
    "HTMLSlotElement": "slot",
    "HTMLSampElement": "samp",
    # "HTMLScriptElement": "script",
    "HTMLSectionElement": "section",
    "HTMLSelectElement": "select",
    "HTMLShadowElement": "shadow",
    "HTMLSmallElement": "small",
    "HTMLSourceElement": "source",
    "HTMLSpanElement": "span",
    "HTMLStrikeElement": "strike",
    "HTMLStrongElement": "strong",
    # "HTMLStyleElement": "style",
    "HTMLSubElement": "sub",
    "HTMLSummaryElement": "summary",
    "HTMLSupElement": "sup",
    "HTMLTimeElement": "time",
    "HTMLTableElement": "table",
    "HTMLTBodyElement": "tbody",
    "HTMLTableDataCellElement": "td",
    "HTMLTemplateElement": "template",
    "HTMLTextAreaElement": "textarea",
    "HTMLTFootElement": "tfoot",
    "HTMLTableHeaderCellElement": "th",
    "HTMLTHeadElement": "thead",
    "HTMLTitleElement": "title",
    "HTMLTableRowElement": "tr",
    "HTMLTrackElement": "track",
    "HTMLTTElement": "tt",
    "HTMLUElement": "u",
    "HTMLUListElement": "ul",
    "HTMLVarElement": "var",
    "HTMLVideoElement": "video",
    "HTMLWBRElement": "wbr",
    "HTMLXMPElement": "xmp",
}

html_elements = list(HTML_ELEMENT_MAP.keys())

global_attributes = {
    # TODO: is, data-*, exportparts
    "accesskey": "common.CharValue",
    "autocapitalize": "html.AutoCapitalizeValue",
    "class": "html.ClassValue",
    "contenteditable": "common.BooleanValue",
    "contextmenu": "html.ContextMenuValue",
    "dir": "html.DirValue",
    "draggable": "common.BooleanValue",
    "webkitdropzone": "html.DropZoneValue",
    "hidden": "common.EmptyValue",
    "inputmode": "html.InputModeValue",
    "itemid": "common.StringValue",
    "itemgroup": "common.StringValue",
    "itemref": "html.ElementIDValue",
    "itemscope": "common.EmptyValue",
    "itemtype": "common.StringValue",
    "lang": "html.LangValue",
    "part": "html.PartValue",
    "slot": "html.SlotValue",
    "spellcheck": "common.BooleanValue",
    "style": "CSSStyleDeclarationValue",
    "tabindex": "html.TabIndexValue",
    "title": "common.StringValue",
    "translate": "common.YesOrNoValue"
}

regular_attributes = {
    "HTMLAnchorElement": {
        # TODO: download, referrerpolicy, name
        "href": "html.DummyUrlValue",
        "ping": "html.DummyUrlValue",
        "target": "html.TargetValue",
        "hreflang": "html.LangValue",
        "type": "html.MIMETypeValue",
        "shape": "html.ShapeValue",
        "coords": "html.CoordsValue",
        "charset": "html.CharsetValue",
        "rel": "html.RelValue",
        "rev": "html.RevValue"
    },
    "HTMLAreaElement": {
        # TODO: download, referrerpolicy
        "href": "html.DummyUrlValue",
        "ping": "html.DummyUrlValue",
        "alt": "common.StringValue",
        "coords": "html.CoordsValue",
        "hreflang": "html.LangValue",
        "nohref": "common.BooleanValue",
        "rel": "html.RelValue",
        "shape": "html.ShapeValue",
        "target": "html.TargetValue"
    },
    "HTMLAudioElement": {
        # TODO: crossorigin
        "autoplay": "common.EmptyValue",
        "controls": "common.EmptyValue",
        "currentTime": "common.IntegerValue",
        "disableRemotePlayback": "common.EmptyValue",
        "loop": "common.EmptyValue",
        "muted": "common.EmptyValue",
        "preload": "html.PreloadValue",
        "src": "html.AudioSrcValue"
    },
    "HTMLBaseFontElement": {
        "color": "css.ColorValue",
        "face": "css.FontFamilyValue",
        "size": "common.IntegerValue",
    },
    "HTMLBgSoundElement": {
        "balance": "common.SignedIntegerValue",
        "loop": "html.SoundLoopValue",
        "volume": "common.SignedIntegerValue",
        "src": "html.AudioSrcValue",
    },
    "HTMLBlockQuoteElement": {
        "cite": "html.DummyUrlValue",
    },
    "HTMLBRElement": {
        "clear": "html.ClearValue",
    },
    "HTMLButtonElement": {
        "autofocus": "common.EmptyValue",
        "autocomplete": "common.OnOrOffValue",
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
        "formaction": "html.DummyUrlValue",
        "formenctype": "html.FormEncTypeValue",
        "formmethod": "html.FormMethodValue",
        "formnovalidate": "common.EmptyValue",
        "formtarget": "html.TargetValue",
        "name": "common.StringValue",
        "type": "html.ButtonTypeValue",
        "value": "common.StringValue"
    },
    "HTMLCanvasElement": {
        "height": "common.IntegerValue",
        "width": "common.IntegerValue"
    },
    "HTMLTableCaptionElement": {
        "align": "html.CaptionAlignValue"
    },
    "HTMLTableColElement": {
        "span": "common.IntegerValue",
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue",
        "width": "common.LengthPercentageValue"
    },
    "HTMLTableColGroupElement": {
        "span": "common.IntegerValue",
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue",
    },
    "HTMLCommandElement": {
        # TODO: icon
        "checked": "common.EmptyValue",
        "disabled": "common.EmptyValue",
        "label": "common.StringValue",
        "radiogroup": "html.RadioGroupValue",
        "type": "html.CommandTypeValue"
    },
    "HTMLContentElement": {
        "select": "html.ContentSelectValue"
    },
    "HTMLDataElement": {
        "value": "common.StringValue",
    },
    "HTMLDDElement": {
        "nowrap": "common.YesOrNoValue"
    },
    "HTMLDelElement": {
        "cite": "html.DummyUrlValue",
        "datetime": "html.DateTimeValue"
    },
    "HTMLDetailsElement": {
        "open": "common.EmptyValue",
    },
    "HTMLDialogElement": {
        "open": "common.EmptyValue",
    },
    "HTMLDirectoryElement": {
        "compact": "common.EmptyValue",
    },
    "HTMLDivElement": {
        "align": "html.AlignValue",
    },
    "HTMLEmbedElement": {
        "type": "html.MediaTypeValue",
        "height": "common.IntegerValue",
        "src": "html.MediaSrcValue",
        "width": "common.IntegerValue"
    },
    "HTMLFieldSetElement": {
        # TODO: name
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
    },
    "HTMLFontElement": {
        "color": "css.ColorValue",
        "face": "css.FontFamilyValue",
        "size": "common.IntegerValue",
    },
    "HTMLFormElement": {
        # TODO: name, action
        "accept": "html.AcceptValue",
        "accept-charset": "html.CharsetValue",
        "autocapitalize": "html.AutoCapitalizeValue",
        "autocomplete": "html.AutoCompleteValue",
        "enctype": "html.FormEncTypeValue",
        "method": "html.FormMethodValue",
        "rel": "html.RelValue",
        "novalidate": "common.EmptyValue",
        "target": "html.TargetValue"
    },
    "HTMLFrameElement": {
        # TODO: name
        "src": "html.FrameSrcValue",
        "noresize": "common.EmptyValue",
        "scrolling": "html.ScrollingValue",
        "marginheight": "common.IntegerValue",
        "marginwidth": "common.IntegerValue",
        "frameborder": "common.IntegerValue"
    },
    "HTMLFrameSetElement": {
        "cols": "common.IntegerValue",
        "rows": "common.IntegerValue",
    },
    "HTMLHeading1Element": {
        "align": "html.AlignValue",
    },
    "HTMLHeading2Element": {
        "align": "html.AlignValue",
    },
    "HTMLHeading3Element": {
        "align": "html.AlignValue",
    },
    "HTMLHeading4Element": {
        "align": "html.AlignValue",
    },
    "HTMLHeading5Element": {
        "align": "html.AlignValue",
    },
    "HTMLHeading6Element": {
        "align": "html.AlignValue",
    },
    "HTMLHRElement": {
        "align": "html.AlignValue",
        "color": "css.ColorValue",
        "noshade": "common.EmptyValue",
        "size": "common.IntegerValue",
        "width": "common.LengthPercentageValue"
    },
    "HTMLIFrameElement": {
        # TODO: allow
        # "allowfullscreen": "common.BooleanValue",
        # TODO: allowpaymentrequest
        # TODO: csp
        "height": "common.IntegerValue",
        "importance": "html.ImportanceValue",
        "loading": "html.LoadingValue",
        # FIXME: target/formtarget! ("name": "html.IFrameNameValue")
        # TODO: referrerpolicy
        # TODO: sandbox
        "src": "html.FrameSrcValue",
        "srcdoc": "common.StringValue",
        "width": "common.IntegerValue",
        "align": "html.ObjectAlignValue",
        "frameborder": "common.IntegerValue",
        "longdesc": "common.StringValue",
        "marginheight": "common.IntegerValue",
        "marginwidth": "common.IntegerValue",
        "scrolling": "html.ScrollingValue"
    },
    "HTMLImageElement": {
        "alt": "common.StringValue",
        "align": "html.ObjectAlignValue",
        # TODO: crossorigin
        "decoding": "html.ImageDecodingValue",
        "height": "common.IntegerValue",
        "importance": "html.ImportanceValue",
        "intrinsicsize": "html.IntrinsicSizeValue",
        "ismap": "common.EmptyValue",
        "loading": "html.LoadingValue",
        # TODO: referrerpolicy
        # TODO: sizes
        "srcset": "html.SrcSetValue",
        "src": "html.ImageSrcValue",
        "width": "common.IntegerValue",
        "usemap": "html.UseMapValue",
        "border": "common.IntegerValue",
        "hspace": "common.IntegerValue",
        "longdesc": "common.StringValue",
        # TODO: name
        "vspace": "common.IntegerValue"
    },
    "HTMLInputElement": {
        # TODO: usemap?
        "type": "html.InputTypeValue",
        "accept": "html.AcceptValue",
        "align": "html.ObjectAlignValue",
        "alt": "common.StringValue",
        "autocomplete": "html.AutoCompleteValue",
        "autofocus": "common.EmptyValue",
        "capture": "html.InputCaptureValue",
        "checked": "common.EmptyValue",
        # "dirname": "common.StringValue",
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
        # TODO: formaction
        "formenctype": "html.FormEncTypeValue",
        "formmethod": "html.FormMethodValue",
        "formnovalidate": "common.EmptyValue",
        "formtarget": "html.TargetValue",
        "height": "common.IntegerValue",
        "inputmode": "html.InputModeValue",
        "list": "html.ListValue",
        "max": "common.IntegerValue",
        "maxlength": "common.IntegerValue",
        "min": "common.IntegerValue",
        "minlength": "common.IntegerValue",
        "multiple": "common.EmptyValue",
        "pattern": "common.RegexValue",
        "placeholder": "common.StringValue",
        "required": "common.EmptyValue",
        "size": "common.IntegerValue",
        "src": "html.ImageSrcValue",
        "step": "common.IntegerValue",
        "value": "common.StringValue",
        "width": "common.IntegerValue",
        "incremental": "common.EmptyValue",
        "autocorrect": "common.OnOrOffValue",
        # TODO: mozactionhint
        # TODO: orient
        "results": "common.IntegerValue",
        # TODO: webkitdirectory
    },
    "HTMLInsElement": {
        "cite": "html.DummyUrlValue",
        "datetime": "html.DateTimeValue"
    },
    "HTMLIsIndexElement": {
        # TODO: prompt, action
    },
    "HTMLKeygenElement": {
        "autofocus": "common.EmptyValue",
        "challenge": "common.StringValue",
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
        "keytype": "html.KeyTypeValue",
    },
    "HTMLLabelElement": {
        "for": "html.LabelForValue",
        "form": "html.FormValue"
    },
    "HTMLLegendElement": {
        "align": "html.CaptionAlignValue",
    },
    "HTMLLIElement": {
        "value": "common.IntegerValue",
        "type": "html.NumberingTypeValue",
    },
    "HTMLLinkElement": {
        # TODO: crossorigin, integrity, referrerpolicy
        "as": "html.LinkAsValue",
        "disabled": "common.EmptyValue",
        "href": "html.DummyUrlValue",
        "hreflang": "html.LangValue",
        "importance": "html.ImportanceValue",
        "media": "html.MediaQueryValue",
        "rel": "html.RelValue",
        "sizes": "html.SizesValue",
        # methods
        # prefetch,
        "target": "html.TargetValue",
        "charset": "html.CharsetValue",
        "rev": "html.RevValue"
    },
    "HTMLMapElement": {
        # "name": "html.MapNameValue",
    },
    "HTMLMarqueeElement": {
        "behavior": "html.MarqueeBehaviorValue",
        "bgcolor": "css.ColorValue",
        "direction": "html.MarqueeDirectionValue",
        "height": "common.LengthPercentageValue",
        "hspace": "common.IntegerValue",
        "loop": "html.MarqueeLoopValue",
        "scrollamount": "common.IntegerValue",
        "scrolldelay": "common.ClockInMsValue",
        "truespeed": "common.EmptyValue",
        "vspace": "common.IntegerValue",
        "width": "common.LengthPercentageValue"
    },
    "HTMLMenuElement": {
        "label": "common.StringValue",
        "type": "html.MenuTypeValue"
    },
    "HTMLMenuItemElement": {
        "checked": "common.EmptyValue",
        "command": "html.CommandValue",
        "default": "common.EmptyValue",
        "icon": "html.ImageSrcValue",
        "label": "common.StringValue",
        "radiogroup": "html.RadioGroupValue",
        "type": "html.MenuItemTypeValue"
    },
    "HTMLMetaElement": {
        # TODO: http-equiv, name
        "charset": "html.CharsetValue",
        "content": "common.StringValue",
        "scheme": "html.MetaSchemeValue",
    },
    "HTMLMeterElement": {
        "value": "common.IntegerValue",
        "min": "common.IntegerValue",
        "max": "common.IntegerValue",
        "low": "common.IntegerValue",
        "high": "common.IntegerValue",
        "optimum": "common.IntegerValue",
        "form": "html.FormValue",
    },
    "HTMLObjectElement": {
        "archive": "html.DummyUrlValue",
        "border": "common.IntegerValue",
        "classid": "common.StringValue",
        "codebase": "common.StringValue",
        "codetype": "html.AcceptValue",
        "data": "html.DummyUrlValue",
        "declare": "common.EmptyValue",
        "form": "html.FormValue",
        "height": "common.IntegerValue",
        "standby": "common.StringValue",
        "type": "html.MediaTypeValue",
        "typemustmatch": "common.EmptyValue",
        "usemap": "html.UseMapValue",
        "width": "common.IntegerValue"
    },
    "HTMLOListElement": {
        "reversed": "common.EmptyValue",
        "start": "common.IntegerValue",
        "type": "html.NumberingTypeValue"
    },
    "HTMLOptGroupElement": {
        "disabled": "common.EmptyValue",
        "label": "common.StringValue"
    },
    "HTMLOptionElement": {
        "disabled": "common.EmptyValue",
        "label": "common.StringValue",
        "selected": "common.EmptyValue",
        "value": "common.StringValue"
    },
    "HTMLOutputElement": {
        "for": "html.ElementIDListValue",
        "form": "html.FormValue",
        # TODO: name
    },
    "HTMLParagraphElement": {
        "align": "html.AlignValue"
    },
    "HTMLParamElement": {
        # FIXME: name
        "name": "common.StringValue",
        "type": "html.MediaTypeValue",
        "value": "common.StringValue",
        "valuetype": "html.ParamValueTypeValue"
    },
    "HTMLPreElement": {
        "cols": "common.IntegerValue",
        "width": "common.IntegerValue",
        "wrap": "html.WrapValue",
    },
    "HTMLProgressElement": {
        "max": "common.IntegerValue",
        "value": "common.IntegerValue"
    },
    "HTMLQElement": {
        "cite": "html.DummyUrlValue"
    },
    "HTMLSelectElement": {
        "autocomplete": "html.AutoCompleteValue",
        "autofocus": "common.EmptyValue",
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
        "multiple": "common.EmptyValue",
        # TODO: name
        "required": "common.EmptyValue",
        "size": "common.IntegerValue"
    },
    "HTMLSlotElement": {
        # "name": "html.SlotNameValue",
    },
    "HTMLSourceElement": {
        # TODO: media
        # TODO: sizes
        "src": "html.ImageSrcValue",
        "srcset": "html.SrcSetValue",
        # TODO: type
    },
    "HTMLTimeElement": {
        "datetime": "html.DateTimeValue",
    },
    "HTMLTableElement": {
        "align": "html.AlignValue",
        "bgcolor": "css.ColorValue",
        "border": "common.IntegerValue",
        "cellpadding": "common.LengthPercentageValue",
        "cellspacing": "common.LengthPercentageValue",
        "frame": "html.TableFrameValue",
        "rules": "html.TableRulesValue",
        "summary": "common.StringValue",
        "width": "common.LengthPercentageValue"
    },
    "HTMLTBodyElement": {
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue"
    },
    "HTMLTableDataCellElement": {
        "abbr": "common.StringValue",
        "align": "html.TableAlignValue",
        "axis": "html.TableAxisValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "colspan": "common.IntegerValue",
        "headers": "html.TableHeadersValue",
        "height": "common.LengthPercentageValue",
        "rowspan": "common.IntegerValue",
        "scope": "html.TableScopeValue",
        "valign": "html.VAlignValue",
        "width": "common.LengthPercentageValue"
    },
    # TODO: <template>: content
    "HTMLTextAreaElement": {
        "autocapitalize": "html.AutoCapitalizeValue",
        "autocomplete": "html.AutoCompleteValue",
        "autofocus": "common.EmptyValue",
        "cols": "common.IntegerValue",
        "disabled": "common.EmptyValue",
        "form": "html.FormValue",
        "maxlength": "common.IntegerValue",
        "minlength": "common.IntegerValue",
        # TODO: name
        # TODO: dirname
        "placeholder": "common.StringValue",
        "readonly": "common.EmptyValue",
        "required": "common.EmptyValue",
        "rows": "common.IntegerValue",
        "spellcheck": "common.BooleanValue",
        "wrap": "html.WrapValue"
    },
    "HTMLTFootElement": {
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue"
    },
    "HTMLTableHeaderCellElement": {
        "abbr": "common.StringValue",
        "align": "html.TableAlignValue",
        "axis": "html.TableAxisValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "colspan": "common.IntegerValue",
        "headers": "html.TableHeadersValue",
        "height": "common.LengthPercentageValue",
        "rowspan": "common.IntegerValue",
        "scope": "html.TableScopeValue",
        "valign": "html.VAlignValue",
        "width": "common.LengthPercentageValue"
    },
    "HTMLTHeadElement": {
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue"
    },
    "HTMLTableRowElement": {
        "align": "html.TableAlignValue",
        "bgcolor": "css.ColorValue",
        "char": "common.CharValue",
        "charoff": "common.IntegerValue",
        "valign": "html.VAlignValue"
    },
    "HTMLTrackElement": {
        "default": "common.EmptyValue",
        "kind": "html.TrackKindValue",
        "label": "common.StringValue",
        "src": "html.TrackSrcValue",
        "srclang": "html.LangValue"
    },
    "HTMLUListElement": {
        "compact": "common.EmptyValue",
        "type": "html.UListTypeValue"
    },
    "HTMLVideoElement": {
        "autoplay": "common.EmptyValue",
        "autoPictureInPicture": "common.EmptyValue",
        # TODO: buffered
        "controls": "common.EmptyValue",
        "controlslist": "html.VideoControlsListValue",
        # TODO: crossorigin
        "currentTime": "common.IntegerValue",
        "disablePictureInPicture": "common.EmptyValue",
        "disableRemotePlayback": "common.EmptyValue",
        # "duration": "common.IntegerValue",
        "height": "common.IntegerValue",
        "intrinsicsize": "html.IntrinsicSizeValue",
        "loop": "common.EmptyValue",
        "muted": "common.EmptyValue",
        "playsinline": "common.EmptyValue",
        "poster": "html.ImageSrcValue",
        "preload": "html.PreloadValue",
        "src": "html.VideoSrcValue",
        "width": "common.IntegerValue"
    },
    "HTMLStyleElement": {
        "type": "html.CSSTypeValue",
        "media": "html.MediaQueryValue",
        "nonce": "html.NonceValue"
    },
}

event_handlers = {
    "onabort": [
        "HTMLObjectElement",
        "HTMLVideoElement",
        "HTMLAudioElement",
        "HTMLImageElement"
    ],
    "onblur":
        list(set(html_elements).difference({
            "HTMLBaseElement",
            "HTMLBDOElement",
            "HTMLBRElement",
            "HTMLHeadElement",
            "HTMLIFrameElement",
            "HTMLMetaElement",
            "HTMLParamElement",
            "HTMLScriptElement",
            "HTMLStyleElement",
            "HTMLTitleElement"
        })),
    "oncancel": [
        "HTMLDialogElement",
    ],
    # "oncanplay": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "oncanplaythrough": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    "onchange": [
        "HTMLInputElement",
        "HTMLSelectElement",
        "HTMLTextAreaElement"
    ],
    "onclick": list(set(html_elements).difference({
        "HTMLBaseElement",
        "HTMLBDOElement",
        "HTMLBRElement",
        "HTMLHeadElement",
        "HTMLIFrameElement",
        "HTMLMetaElement",
        "HTMLParamElement",
        "HTMLScriptElement",
        "HTMLStyleElement",
        "HTMLTitleElement"
    })),
    "onclose": [
        "HTMLDialogElement",
    ],
    "oncuechange": [
        "HTMLTrackElement"
    ],
    # "ondurationchange": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "onended": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    "onerror": [
        "HTMLImageElement",
        "HTMLInputElement",
        "HTMLObjectElement",
        "HTMLLinkElement",
        "HTMLScriptElement",
        "HTMLVideoElement",
        "HTMLAudioElement",
    ],
    "onfocus":
        list(set(html_elements).difference({
            "HTMLBaseElement",
            "HTMLBDOElement",
            "HTMLBRElement",
            "HTMLHeadElement",
            "HTMLIFrameElement",
            "HTMLMetaElement",
            "HTMLParamElement",
            "HTMLScriptElement",
            "HTMLStyleElement",
            "HTMLTitleElement"
        })),
    "onfocusin":
        list(set(html_elements).difference({
            "HTMLBaseElement",
            "HTMLBDOElement",
            "HTMLBRElement",
            "HTMLHeadElement",
            "HTMLIFrameElement",
            "HTMLMetaElement",
            "HTMLParamElement",
            "HTMLScriptElement",
            "HTMLStyleElement",
            "HTMLTitleElement"
        })),
    "onfocusout":
        list(set(html_elements).difference({
            "HTMLBaseElement",
            "HTMLBDOElement",
            "HTMLBRElement",
            "HTMLHeadElement",
            "HTMLIFrameElement",
            "HTMLMetaElement",
            "HTMLParamElement",
            "HTMLScriptElement",
            "HTMLStyleElement",
            "HTMLTitleElement"
        })),
    # "fullscreenchange": html_elements,
    # "fullscreenerror": html_elements,
    # TODO: onhashchange
    "oninput": [
        "HTMLInputElement",
        "HTMLSelectElement",
        "HTMLTextAreaElement"
    ],
    "oninvalid": [
        "HTMLInputElement",
    ],
    # "onloadeddata": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    # "onloadedmetadata": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    # "onloadstart": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "onpause": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    # "onplay": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "onplaying": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "onprogress": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    # "onratechange": [
    #     "HTMLVideoElement",
    #     "HTMLAudioElement"
    # ],
    "onreset": [
        "HTMLFormElement",
    ],
    "onscroll": [
        "HTMLAddressElement",
        "HTMLBlockQuoteElement",
        "HTMLTableCaptionElement",
        "HTMLCenterElement",
        "HTMLDDElement",
        "HTMLDirectoryElement",
        "HTMLDivElement",
        "HTMLDListElement",
        "HTMLDTElement",
        "HTMLFieldSetElement",
        "HTMLFormElement",
        "HTMLHeading1Element",
        "HTMLHeading2Element",
        "HTMLHeading3Element",
        "HTMLHeading4Element",
        "HTMLHeading5Element",
        "HTMLHeading6Element",
        "HTMLLIElement",
        "HTMLMenuElement",
        "HTMLObjectElement",
        "HTMLOListElement",
        "HTMLParagraphElement",
        "HTMLPreElement",
        "HTMLSelectElement",
        "HTMLTBodyElement",
        "HTMLTextAreaElement",
        "HTMLTFootElement",
        "HTMLTHeadElement",
        "HTMLUListElement"
    ],
    "onsearch": [
        "HTMLInputElement"
    ],
    "onselect": [
        "HTMLInputElement",
        "HTMLTextAreaElement"
    ],
    "onshow": [
        "HTMLMenuElement"
    ],
    # "onstalled": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    "onsubmit": [
        "HTMLFormElement"
    ],
    # "onsuspend": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "ontimeupdate": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    "ontoggle": [
        "HTMLDetailsElement",
    ],
    # "onvolumechange": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "onwaiting": [
    #    "HTMLVideoElement",
    #    "HTMLAudioElement"
    # ],
    # "ontransitionend": html_elements,
    # "ontransitionrun": html_elements,
    # "ontransitionstart": html_elements,
    # "ontransitioncancel": html_elements,
    # "onanimationend": html_elements,
    # "onanimationiteration": html_elements,
    # "onanimationstart": html_elements,
    # "onanimationcancel": html_elements
}

if __name__ == "__main__":
    print("# Auto-generated by generate_attribute.py")
    print("def initialize_html_attributes():")

    print("    # regular attributes")
    for element in HTML_ELEMENT_MAP:
        if element not in regular_attributes:
            continue

        attributes = regular_attributes[element]
        for attr, value in attributes.items():
            print('    add_regular_attribute(AttributeTemplate("{}", "{}", {}))'.format(
                element, attr, value
            ))

    print("")
    print("    # global attributes")
    for element in HTML_ELEMENT_MAP:
        for attr, value in global_attributes.items():
            print('    add_global_attribute(AttributeTemplate("{}", "{}", {}))'.format(
                element, attr, value
            ))

    for element in HTML_ELEMENT_MAP:
        for event in event_handlers:
            if element in event_handlers[event]:
                print('    add_global_attribute(AttributeTemplate("{}", "{}", html.CallEventHandlerValue))'.format(
                    element, event
                ))
