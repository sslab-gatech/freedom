HTML_ELEMENT_MAP = {
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
    # "HTMLBaseFontElement": "basefont",
    "HTMLBDIElement": "bdi",
    "HTMLBDOElement": "bdo",
    "HTMLBgSoundElement": "bgsound",
    "HTMLBigElement": "big",
    "HTMLBlockQuoteElement": "blockquote",
    "HTMLBodyElement": "body",
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
    # "HTMLPlainTextElement": "plaintext",
    "HTMLPreElement": "pre",
    "HTMLProgressElement": "progress",
    "HTMLQElement": "q",
    "HTMLRPElement": "rp",
    "HTMLRTElement": "rt",
    "HTMLRubyElement": "ruby",
    "HTMLSElement": "s",
    "HTMLSampElement": "samp",
    "HTMLScriptElement": "script",
    "HTMLSectionElement": "section",
    "HTMLSelectElement": "select",
    "HTMLShadowElement": "shadow",
    "HTMLSlotElement": "slot",
    "HTMLSmallElement": "small",
    "HTMLSourceElement": "source",
    "HTMLSpanElement": "span",
    "HTMLStrikeElement": "strike",
    "HTMLStrongElement": "strong",
    "HTMLStyleElement": "style",
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

HTML_ELEMENTS = list(HTML_ELEMENT_MAP.keys())

HTML_GENERAL_CHILD_ELEMENTS = [
    "HTMLAnchorElement",
    "HTMLAreaElement",
    "HTMLAudioElement",
    "HTMLBlockQuoteElement",
    "HTMLBRElement",
    "HTMLButtonElement",
    "HTMLCanvasElement",
    "HTMLContentElement",
    "HTMLDataElement",
    "HTMLDataListElement",
    "HTMLDelElement",
    "HTMLDetailsElement",
    "HTMLDialogElement",
    "HTMLDirectoryElement",
    "HTMLDivElement",
    "HTMLDListElement",
    "HTMLEmbedElement",
    "HTMLFieldSetElement",
    "HTMLFontElement",
    "HTMLFormElement",
    # "HTMLFrameElement",
    "HTMLFrameSetElement",
    "HTMLHeading1Element",
    "HTMLHeading2Element",
    "HTMLHeading3Element",
    "HTMLHeading4Element",
    "HTMLHeading5Element",
    "HTMLHeading6Element",
    "HTMLHRElement",
    "HTMLIFrameElement",
    "HTMLImageElement",
    "HTMLInputElement",
    "HTMLInsElement",
    "HTMLKeygenElement",
    "HTMLLabelElement",
    "HTMLLinkElement",
    "HTMLMapElement",
    "HTMLMarqueeElement",
    "HTMLMenuElement",
    "HTMLMeterElement",
    "HTMLObjectElement",
    "HTMLOListElement",
    "HTMLOutputElement",
    "HTMLParagraphElement",
    "HTMLPictureElement",
    "HTMLPreElement",
    "HTMLProgressElement",
    "HTMLQElement",
    "HTMLSelectElement",
    "HTMLShadowElement",
    "HTMLSlotElement",
    "HTMLSpanElement",
    "HTMLStyleElement",
    "HTMLTimeElement",
    "HTMLTableElement",
    "HTMLTemplateElement",
    "HTMLTextAreaElement",
    "HTMLTitleElement",
    "HTMLUListElement",
    "HTMLVideoElement",
]

HTML_OTHER_CHILD_ELEMENTS = [
    "HTMLAbbrElement",
    "HTMLAcronymElement",
    "HTMLAddressElement",
    "HTMLArticleElement",
    "HTMLAsideElement",
    "HTMLBElement",
    "HTMLBDIElement",
    "HTMLBDOElement",
    "HTMLBgSoundElement",
    "HTMLBigElement",
    "HTMLCenterElement",
    "HTMLCiteElement",
    "HTMLCodeElement",
    "HTMLCommandElement",
    "HTMLDFNElement",
    "HTMLEMElement",
    "HTMLFigureElement",
    "HTMLFooterElement",
    "HTMLHeaderElement",
    "HTMLHGroupElement",
    "HTMLIElement",
    "HTMLIsIndexElement",
    "HTMLKBDElement",
    "HTMLListingElement",
    "HTMLMainElement",
    "HTMLMetaElement",
    "HTMLMarkElement",
    "HTMLNavElement",
    # "HTMLPlainTextElement",
    "HTMLRubyElement",
    "HTMLSElement",
    "HTMLSampElement",
    "HTMLSectionElement",
    "HTMLSmallElement",
    "HTMLStrikeElement",
    "HTMLStrongElement",
    "HTMLSubElement",
    "HTMLSupElement",
    "HTMLTTElement",
    "HTMLUElement",
    "HTMLVarElement",
    "HTMLWBRElement",
    "HTMLXMPElement"
]

FORM_CHILD_ELEMENTS = [
    "HTMLLegendElement",
    "HTMLInputElement",
    "HTMLTextAreaElement",
    "HTMLButtonElement",
    "HTMLKeygenElement",
    "HTMLObjectElement",
    "HTMLSelectElement",
    "HTMLOutputElement",
    "HTMLLabelElement",
    "HTMLFieldSetElement",
    "HTMLOptionElement",
    "HTMLDataListElement"
]

TABLE_CHILD_ELEMENTS = [
    "HTMLTableCaptionElement",
    "HTMLTBodyElement",
    "HTMLTFootElement",
    "HTMLTHeadElement",
    "HTMLTableColGroupElement",
    "HTMLTableRowElement"
]

MEDIA_CHILD_ELEMENTS = [
    "HTMLSourceElement",
    "HTMLTrackElement"
]

HTML_LABELABLE_ELEMENTS = [
    "HTMLButtonElement",
    "HTMLInputElement",
    "HTMLKeygenElement",
    "HTMLMeterElement",
    "HTMLOutputElement",
    "HTMLProgressElement",
    "HTMLSelectElement",
    "HTMLTextAreaElement"
]

# The elements not here can have any html elements as its children.
HTML_CHILD_ELEMENTS = {
    "HTMLAudioElement": MEDIA_CHILD_ELEMENTS,
    "HTMLFormElement": FORM_CHILD_ELEMENTS,
    "HTMLFieldSetElement": FORM_CHILD_ELEMENTS,
    "HTMLSelectElement": ["HTMLOptionElement", "HTMLOptGroupElement"],
    "HTMLMapElement": ["HTMLAreaElement"],
    "HTMLTableElement": TABLE_CHILD_ELEMENTS,
    "HTMLTableColGroupElement": ["HTMLTableColElement"],
    "HTMLTBodyElement": ["HTMLTableRowElement"],
    "HTMLTFootElement": ["HTMLTableRowElement"],
    "HTMLTHeadElement": ["HTMLTableRowElement"],
    "HTMLTableRowElement": ["HTMLTableHeaderCellElement", "HTMLTableDataCellElement"],
    "HTMLDirectoryElement": ["HTMLLIElement"],
    "HTMLDataListElement": ["HTMLOptionElement"],
    "HTMLOListElement": ["HTMLLIElement"],
    "HTMLOptGroupElement": ["HTMLOptionElement"],
    "HTMLUListElement": ["HTMLLIElement"],
    "HTMLDetailsElement": ["HTMLSummaryElement"],
    "HTMLDListElement": ["HTMLDTElement", "HTMLDDElement"],
    "HTMLFigureElement": ["HTMLFigCaptionElement"],
    "HTMLFrameSetElement": ["HTMLFrameElement"],
    "HTMLMenuElement": ["HTMLMenuElement", "HTMLMenuItemElement", "HTMLLIElement"],
    "HTMLObjectElement": ["HTMLParamElement"],
    "HTMLRubyElement": ["HTMLRPElement", "HTMLRTElement"],
    "HTMLVideoElement": MEDIA_CHILD_ELEMENTS,
}


HTML_EMPTY_ELEMENTS = [
    # Empty elements
    "HTMLAreaElement",
    # HTMLBaseElement,
    "HTMLBRElement",
    "HTMLTableColElement",
    "HTMLEmbedElement",
    "HTMLHRElement",
    "HTMLImageElement",
    "HTMLInputElement",
    "HTMLKeygenElement",
    "HTMLLinkElement",
    "HTMLMetaElement",
    "HTMLParamElement",
    "HTMLSourceElement",
    "HTMLTrackElement",
    "HTMLWBRElement",
    "HTMLIsIndexElement"
]


HTML_RAW_TEXT_ELEMENTS = [
    "HTMLTitleElement",
    "HTMLTextAreaElement",
    "HTMLIFrameElement",
    "HTMLXMPElement",
    "HTMLStyleElement"
]


HTML_TEXT_ELEMENTS = [
    "HTMLAnchorElement",
    "HTMLAbbrElement",
    "HTMLAcronymElement",
    "HTMLAddressElement",
    "HTMLArticleElement",
    "HTMLAsideElement",
    "HTMLAudioElement",
    "HTMLBElement",
    # "HTMLBaseFontElement",
    "HTMLBDIElement",
    "HTMLBDOElement",
    "HTMLBgSoundElement",
    "HTMLBigElement",
    "HTMLBlockQuoteElement",
    "HTMLButtonElement",
    "HTMLCanvasElement",
    "HTMLTableCaptionElement",
    "HTMLCenterElement",
    "HTMLCiteElement",
    "HTMLCodeElement",
    "HTMLTableColGroupElement",
    "HTMLCommandElement",
    "HTMLContentElement",
    "HTMLDataElement",
    "HTMLDataListElement",
    "HTMLDDElement",
    "HTMLDelElement",
    "HTMLDetailsElement",
    "HTMLDFNElement",
    "HTMLDialogElement",
    "HTMLDirectoryElement",
    "HTMLDivElement",
    "HTMLDListElement",
    "HTMLDTElement",
    "HTMLEMElement",
    "HTMLFieldSetElement",
    "HTMLFigCaptionElement",
    "HTMLFigureElement",
    "HTMLFontElement",
    "HTMLFooterElement",
    "HTMLFormElement",
    "HTMLFrameElement",
    "HTMLFrameSetElement",
    "HTMLHeading1Element",
    "HTMLHeading2Element",
    "HTMLHeading3Element",
    "HTMLHeading4Element",
    "HTMLHeading5Element",
    "HTMLHeading6Element",
    "HTMLHeaderElement",
    "HTMLHGroupElement",
    "HTMLIElement",
    "HTMLIFrameElement",
    "HTMLInsElement",
    "HTMLIsIndexElement",
    "HTMLKBDElement",
    "HTMLLabelElement",
    "HTMLLegendElement",
    "HTMLLIElement",
    "HTMLListingElement",
    "HTMLMainElement",
    "HTMLMapElement",
    "HTMLMarkElement",
    "HTMLMarqueeElement",
    "HTMLMenuElement",
    "HTMLMenuItemElement",
    "HTMLMeterElement",
    "HTMLNavElement",
    "HTMLObjectElement",
    "HTMLOListElement",
    "HTMLOptGroupElement",
    "HTMLOptionElement",
    "HTMLOutputElement",
    "HTMLParagraphElement",
    "HTMLPictureElement",
    # "HTMLPlainTextElement",
    "HTMLPreElement",
    "HTMLProgressElement",
    "HTMLQElement",
    "HTMLRPElement",
    "HTMLRTElement",
    "HTMLRubyElement",
    "HTMLSElement",
    "HTMLSampElement",
    "HTMLSectionElement",
    "HTMLSelectElement",
    "HTMLShadowElement",
    "HTMLSmallElement",
    "HTMLSpanElement",
    "HTMLStrikeElement",
    "HTMLStrongElement",
    "HTMLSubElement",
    "HTMLSummaryElement",
    "HTMLSupElement",
    "HTMLTimeElement",
    "HTMLTableElement",
    "HTMLTBodyElement",
    "HTMLTableDataCellElement",
    "HTMLTemplateElement",
    "HTMLTextAreaElement",
    "HTMLTFootElement",
    "HTMLTableHeaderCellElement",
    "HTMLTHeadElement",
    "HTMLTitleElement",
    "HTMLTableRowElement",
    "HTMLTTElement",
    "HTMLUElement",
    "HTMLUListElement",
    "HTMLVarElement",
    "HTMLVideoElement",
    "HTMLXMPElement",
]

BLOCK_ELEMENTS = [
    "HTMLParagraphElement",
    "HTMLHeading1Element",
    "HTMLHeading2Element",
    "HTMLHeading3Element",
    "HTMLHeading4Element",
    "HTMLHeading5Element",
    "HTMLHeading6Element",
    "HTMLUListElement",
    "HTMLOListElement",
    "HTMLDListElement",
    "HTMLPreElement",
    "HTMLHRElement",
    "HTMLBlockQuoteElement",
    "HTMLAddressElement"
]

LINK_ELEMENTS = ["HTMLAnchorElement", "HTMLAreaElement", "HTMLLinkElement"]

SUBMITTABLE_ELEMENTS = [
    "HTMLButtonElement",
    "HTMLInputElement",
    "HTMLObjectElement",
    "HTMLSelectElement",
    "HTMLTextAreaElement"
]
