SVG_ELEMENTS = {
    "SVGAElement": "a",
    "SVGAltGlyphDefElement": "altGlyphDef",
    "SVGAltGlyphElement": "altGlyph",
    "SVGAltGlyphItemElement": "altGlyphItem",
    # "SVGAnimateColorElement": "animateColor",
    "SVGAnimateElement": "animate",
    "SVGAnimateMotionElement": "animateMotion",
    "SVGAnimateTransformElement": "animateTransform",
    "SVGCircleElement": "circle",
    "SVGClipPathElement": "clipPath",
    # "SVGColorProfileElement": "color-profile",
    "SVGCursorElement": "cursor",
    "SVGDefsElement": "defs",
    "SVGDescElement": "desc",
    "SVGDiscardElement": "discard",
    "SVGEllipseElement": "ellipse",
    "SVGFEBlendElement": "feBlend",
    "SVGFEColorMatrixElement": "feColorMatrix",
    "SVGFEComponentTransferElement": "feComponentTransfer",
    "SVGFECompositeElement": "feComposite",
    "SVGFEConvolveMatrixElement": "feConvolveMatrix",
    "SVGFEDiffuseLightingElement": "feDiffuseLighting",
    "SVGFEDisplacementMapElement": "feDisplacementMap",
    "SVGFEDistantLightElement": "feDistantLight",
    "SVGFEDropShadowElement": "feDropShadow",
    "SVGFEFloodElement": "feFlood",
    "SVGFEFuncAElement": "feFuncA",
    "SVGFEFuncBElement": "feFuncB",
    "SVGFEFuncGElement": "feFuncG",
    "SVGFEFuncRElement": "feFuncR",
    "SVGFEGaussianBlurElement": "feGaussianBlur",
    "SVGFEImageElement": "feImage",
    "SVGFEMergeElement": "feMerge",
    "SVGFEMergeNodeElement": "feMergeNode",
    "SVGFEMorphologyElement": "feMorphology",
    "SVGFEOffsetElement": "feOffset",
    "SVGFEPointLightElement": "fePointLight",
    "SVGFESpecularLightingElement": "feSpecularLighting",
    "SVGFESpotLightElement": "feSpotLight",
    "SVGFETileElement": "feTile",
    "SVGFETurbulenceElement": "feTurbulence",
    "SVGFilterElement": "filter",
    "SVGFontElement": "font",
    "SVGFontFaceElement": "font-face",
    "SVGFontFaceFormatElement": "font-face-format",
    "SVGFontFaceNameElement": "font-face-name",
    "SVGFontFaceSrcElement": "font-face-src",
    "SVGFontFaceUriElement": "font-face-uri",
    "SVGForeignObjectElement": "foreignObject",
    "SVGGElement": "g",
    "SVGGlyphElement": "glyph",
    "SVGGlyphRefElement": "glyphRef",
    # "SVGHatchElement": "hatch",
    # "SVGHatchpathElement": "hatchpath",
    "SVGHKernElement": "hkern",
    "SVGImageElement": "image",
    "SVGLineElement": "line",
    "SVGLinearGradientElement": "linearGradient",
    "SVGMPathElement": "mpath",
    "SVGMarkerElement": "marker",
    "SVGMaskElement": "mask",
    "SVGMetadataElement": "metadata",
    "SVGMissingGlyphElement": "missing-glyph",
    "SVGPathElement": "path",
    "SVGPatternElement": "pattern",
    "SVGPolygonElement": "polygon",
    "SVGPolylineElement": "polyline",
    "SVGRadialGradientElement": "radialGradient",
    "SVGRectElement": "rect",
    # "SVGScriptElement": "script",
    "SVGSVGElement": "svg",
    "SVGSetElement": "set",
    # "SVGSolidcolorElement": "solidcolor",
    "SVGStopElement": "stop",
    "SVGStyleElement": "style",
    "SVGSwitchElement": "switch",
    "SVGSymbolElement": "symbol",
    "SVGTRefElement": "tref",
    "SVGTSpanElement": "tspan",
    "SVGTextElement": "text",
    "SVGTextPathElement": "textPath",
    "SVGTitleElement": "title",
    "SVGUseElement": "use",
    "SVGVKernElement": "vkern",
    "SVGViewElement": "view"
}

SVG_ANIMATION_ELEMENTS = [
    "SVGAnimateElement",
    # "SVGAnimateColorElement",
    "SVGAnimateMotionElement",
    "SVGAnimateTransformElement",
    "SVGDiscardElement",
    "SVGSetElement"
]

SVG_PAINT_SERVER_ELEMENTS = [
    "SVGLinearGradientElement",
    "SVGRadialGradientElement",
    # "SVGSolidcolorElement",
    "SVGPatternElement",
    # "SVGHatchElement"
    # mesh
]

SVG_TEXT_CONTENT_ELEMENTS = [
    "SVGTextPathElement",
    "SVGTextElement",
    "SVGTSpanElement",
    "SVGTRefElement",
    "SVGAltGlyphElement"
]

SVG_TEXT_CONTENT_CHILD_ELEMENTS = [
    "SVGTextPathElement",
    "SVGTSpanElement",
    "SVGTRefElement",
    "SVGAltGlyphElement"
]

SVG_SHAPE_ELEMENTS = [
    "SVGRectElement",
    "SVGCircleElement",
    "SVGEllipseElement",
    "SVGLineElement",
    "SVGPathElement",
    "SVGPolylineElement",
    "SVGPolygonElement"
]

SVG_CONTAINER_ELEMENTS = [
    "SVGAElement",
    "SVGDefsElement",
    "SVGGElement",
    "SVGMarkerElement",
    "SVGMaskElement",
    "SVGMissingGlyphElement",
    "SVGPatternElement",
    # "SVGSVGElement",
    "SVGSwitchElement",
    "SVGSymbolElement",
    # use
]

SVG_GRAPHICS_ELEMENTS = [
    "SVGCircleElement",
    "SVGEllipseElement",
    "SVGForeignObjectElement",
    "SVGImageElement",
    "SVGLineElement",
    "SVGPathElement",
    "SVGPolygonElement",
    "SVGPolylineElement",
    "SVGRectElement",
    "SVGTextElement",
    # use
]

SVG_ESTABLISH_VIEWPORT_ELEMENTS = [
    # "SVGSVGElement",
    "SVGSymbolElement",
    "SVGImageElement",
    "SVGForeignObjectElement"
]

SVG_GRADIENT_ELEMENTS = [
    "SVGLinearGradientElement",
    "SVGRadialGradientElement",
    # mesh
]

SVG_FILTER_PRIMITIVES = [
    "SVGFEBlendElement",
    "SVGFEColorMatrixElement",
    "SVGFEComponentTransferElement",
    "SVGFECompositeElement",
    "SVGFEConvolveMatrixElement",
    "SVGFEDiffuseLightingElement",
    "SVGFEDisplacementMapElement",
    "SVGFEDropShadowElement",
    "SVGFEFloodElement",
    "SVGFEGaussianBlurElement",
    "SVGFEImageElement",
    "SVGFEMergeElement",
    "SVGFEMergeNodeElement",
    "SVGFEMorphologyElement",
    "SVGFEOffsetElement",
    "SVGFESpecularLightingElement",
    "SVGFETileElement",
    "SVGFETurbulenceElement",
]

SVG_MARKABLE_ELEMENTS = [
    "SVGLineElement",
    "SVGPathElement",
    "SVGPolylineElement",
    "SVGPolygonElement"
]

SVG_DESCRIPTIVE_ELEMENTS = [
    # "SVGDescElement",
    # "SVGTitleElement",
    # "SVGMetadataElement"
]

SVG_STRUCTURAL_ELEMENTS = [
    "SVGDefsElement",
    "SVGGElement",
    "SVGSVGElement",
    "SVGSymbolElement",
    "SVGUseElement",
]

SVG_LIGHT_SOURCES = [
    "SVGFEDistantLightElement",
    "SVGFEPointLightElement",
    "SVGFESpotLightElement"
]

SVG_CHILD_ELEMENTS = {
    "SVGAElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
            # style
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGAltGlyphDefElement":
        [
            "SVGGlyphRefElement",
            "SVGAltGlyphItemElement"
        ],

    "SVGAltGlyphElement": [],

    "SVGAltGlyphItemElement":
        [
            "SVGGlyphRefElement"
        ],

    # "SVGAnimateColorElement":
    #    SVG_DESCRIPTIVE_ELEMENTS,

    "SVGAnimateElement":
        SVG_DESCRIPTIVE_ELEMENTS,

    "SVGAnimateMotionElement":
        [
            "SVGMPathElement"
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGAnimateTransformElement":
        SVG_DESCRIPTIVE_ELEMENTS,

    "SVGCircleElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGClipPathElement":
        [
            "SVGTextElement"
            # use
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_SHAPE_ELEMENTS,

    # "SVGColorProfileElement":
    #    SVG_DESCRIPTIVE_ELEMENTS,

    "SVGCursorElement":
        SVG_DESCRIPTIVE_ELEMENTS,  # script

    "SVGDefsElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGDescElement": [],

    "SVGDiscardElement":
        SVG_DESCRIPTIVE_ELEMENTS,  # script 

    "SVGEllipseElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGFEBlendElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEColorMatrixElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEComponentTransferElement":
        [
            "SVGFEFuncAElement",
            "SVGFEFuncBElement",
            "SVGFEFuncGElement",
            "SVGFEFuncRElement",
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFECompositeElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEConvolveMatrixElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEDiffuseLightingElement":  # script
        SVG_DESCRIPTIVE_ELEMENTS
        + SVG_LIGHT_SOURCES,

    "SVGFEDisplacementMapElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEDistantLightElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEDropShadowElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEFloodElement":
        [
            "SVGAnimateElement",
            # "SVGAnimateColorElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEFuncAElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEFuncBElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEFuncGElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEFuncRElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEGaussianBlurElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEImageElement":
        [
            "SVGAnimateElement",
            "SVGAnimateTransformElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEMergeElement":
        [
            "SVGFEMergeNodeElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEMergeNodeElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEMorphologyElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEOffsetElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFEPointLightElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFESpecularLightingElement":
        SVG_DESCRIPTIVE_ELEMENTS
        + SVG_LIGHT_SOURCES,

    "SVGFESpotLightElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFETileElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFETurbulenceElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFilterElement":
        [
            "SVGAnimateElement",
            "SVGSetElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_FILTER_PRIMITIVES,

    "SVGForeignObjectElement": [],

    "SVGFontElement":
        [
            "SVGFontFaceElement",
            "SVGGlyphElement",
            "SVGHKernElement",
            "SVGMissingGlyphElement",
            "SVGVKernElement"
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFontFaceElement":
        [
            "SVGFontFaceSrcElement",
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGFontFaceFormatElement": [],

    "SVGFontFaceNameElement": [],

    "SVGFontFaceSrcElement":
        [
            "SVGFontFaceNameElement",
            "SVGFontFaceUriElement"
        ],

    "SVGFontFaceUriElement":
        [
            "SVGFontFaceFormatElement"
        ],

    "SVGGElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGGlyphElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGGlyphRefElement": [],

    "SVGHKernElement": [],

    # "SVGHatchElement":
    #    [
    #        "SVGHatchpathElement"
    #        # script
    #    ]
    #    + SVG_ANIMATION_ELEMENTS
    #    + SVG_DESCRIPTIVE_ELEMENTS,

    # "SVGHatchpathElement":
    #    SVG_ANIMATION_ELEMENTS
    #    + SVG_DESCRIPTIVE_ELEMENTS,  # script

    "SVGImageElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS,
        # + SVG_PAINT_SERVER_ELEMENTS,  # structurally external elements

    "SVGLineElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGLinearGradientElement":
        [
            "SVGAnimateElement",
            "SVGAnimateTransformElement",
            "SVGSetElement",
            "SVGStopElement"
            # script
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,
        # + SVG_PAINT_SERVER_ELEMENTS,

    "SVGMPathElement":
        SVG_DESCRIPTIVE_ELEMENTS,  # script

    "SVGMarkerElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGMaskElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGMetadataElement": [],

    "SVGMissingGlyphElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGPathElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGPatternElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGPolygonElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGPolylineElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGRadialGradientElement":
        [
            "SVGAnimateElement",
            "SVGAnimateTransformElement",
            "SVGSetElement",
            "SVGStopElement",
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,
        # + SVG_PAINT_SERVER_ELEMENTS,

    "SVGRectElement":
        [
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGSVGElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGSetElement":
        SVG_DESCRIPTIVE_ELEMENTS,

    "SVGStyleElement": [],

    # "SVGSolidcolorElement":
    #    [
    #        "SVGAnimateElement",
    #        # "SVGAnimateColorElement",
    #        "SVGSetElement",
    #        # script
    #    ]
    #    + SVG_PAINT_SERVER_ELEMENTS,

    "SVGStopElement":
        [
            "SVGAnimateElement",
            # "SVGAnimateColorElement",
            "SVGSetElement",
        ],

    "SVGSwitchElement":
        [
            "SVGAElement",
            "SVGClipPathElement",
            "SVGForeignObjectElement",
            "SVGGElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            # "SVGSVGElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGUseElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        # + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS,

    "SVGSymbolElement":
        [
            "SVGAElement",
            "SVGAltGlyphDefElement",
            "SVGClipPathElement",
            # "SVGColorProfileElement",
            "SVGCursorElement",
            "SVGFilterElement",
            "SVGFontElement",
            "SVGFontFaceElement",
            "SVGForeignObjectElement",
            "SVGImageElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # "SVGScriptElement",
            "SVGStyleElement",
            "SVGSwitchElement",
            "SVGTextElement",
            "SVGViewElement",
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_SHAPE_ELEMENTS
        + SVG_STRUCTURAL_ELEMENTS,

    "SVGTRefElement":
        [
            "SVGAnimateElement",
            # "SVGAnimateColorElement",
            "SVGSetElement"
        ]
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGTSpanElement":
        [
            "SVGAElement",
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_TEXT_CONTENT_CHILD_ELEMENTS,

    "SVGTextElement":
        [
            "SVGAElement",
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            # script
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS
        + SVG_PAINT_SERVER_ELEMENTS
        + SVG_TEXT_CONTENT_CHILD_ELEMENTS,

    "SVGTextPathElement":
        [
            "SVGAElement",
            "SVGAltGlyphElement",
            "SVGAnimateElement",
            # "SVGAnimateColorElement",
            "SVGClipPathElement",
            "SVGMarkerElement",
            "SVGMaskElement",
            "SVGSetElement",
            "SVGTRefElement",
            "SVGTSpanElement"
        ]
        + SVG_PAINT_SERVER_ELEMENTS,

    "SVGTitleElement": [],

    "SVGVKernElement": [],

    "SVGViewElement":
        SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS,

    "SVGUseElement":
        [
            "SVGClipPathElement",
            "SVGMaskElement",
            # script
            # style
        ]
        + SVG_ANIMATION_ELEMENTS
        + SVG_DESCRIPTIVE_ELEMENTS,
}

SVG_ANIMATABLE_ATTRIBUTES = [
    "alignment-baseline",
    "amplitude",
    "azimuth",
    "baseFrequency",
    "baseline-shift",
    "bias",
    "cap-height",
    "clip",
    "clip-path",
    "clip-rule",
    "clipPathUnits",
    "color",
    "color-interpolation",
    "color-interpolation-filters",
    "color-profile",
    "color-rendering",
    "cursor",
    "cx",
    "cy",
    "d",
    "diffuseConstant",
    "direction",
    "display",
    "divisor",
    "dominant-baseline",
    "dx",
    "dy",
    "edgeMode",
    "elevation",
    "exponent",
    "fill",
    "fill-opacity",
    "fill-rule",
    "filter",
    "filterPrimitiveUnits",
    "filterRes",
    "filterUnits",
    "flood-color",
    "flood-opacity",
    "font-family",
    "font-size",
    "font-size-adjust",
    "font-stretch",
    "font-style",
    "font-variant",
    "font-weight",
    "glyphRef",
    "gradientTransform",
    "gradientUnits",
    "hatchContentUnits",
    "hatchUnits",
    "height",
    "hreflang",
    "image-rendering",
    "in",
    "in2",
    "intercept",
    "k1",
    "k2",
    "k3",
    "k4",
    "kernelMatrix",
    "kernelUnitLength",
    "kerning",
    "lengthAdjust",
    "letter-spacing",
    "lighting-color",
    "limitingConeAngle",
    "marker-end",
    "marker-mid",
    "marker-start",
    "markerHeight",
    "markerUnits",
    "markerWidth",
    "mask",
    "maskContentUnits",
    "maskUnits",
    "method",
    "mode",
    "name",
    "numOctaves",
    "offset",
    "opacity",
    "operator",
    "order",
    "orient",
    "orientation",
    "overflow",
    "pathLength",
    "patternContentUnits",
    "patternTransform",
    "patternUnits",
    "pitch",
    "pointer-events",
    "points",
    "pointsAtX",
    "pointsAtY",
    "pointsAtZ",
    "preserveAlpha",
    "preserveAspectRatio",
    "primitiveUnits",
    "r",
    "radius",
    "refX",
    "refY",
    "rendering-intent",
    "result",
    "rx",
    "ry",
    "scale",
    "seed",
    "shape-rendering",
    "side",
    "slope",
    "solid-color",
    "solid-opacity",
    "spacing",
    "specularConstant",
    "specularExponent",
    "spreadMethod",
    "startOffset",
    "stdDeviation",
    "stitchTiles",
    "stop-color",
    "stop-opacity",
    "stroke",
    "stroke-dasharray",
    "stroke-dashoffset",
    "stroke-linecap",
    "stroke-linejoin",
    "stroke-miterlimit",
    "stroke-opacity",
    "stroke-width",
    "surfaceScale",
    "tableValues",
    "target",
    "targetX",
    "targetY",
    "text-anchor",
    "text-decoration",
    "text-rendering",
    "textLength",
    "transform",
    "type",
    "vector-effect",
    "viewBox",
    "visibility",
    "width",
    "word-spacing",
    "writing-mode",
    "x",
    "x1",
    "x2",
    "xChannelSelector",
    "y",
    "y1",
    "y2",
    "yChannelSelector",
    "z"
]

# SVG_ANIMATABLE_COLOR_ATTRIBUTES = [
#    "fill",
#    "stroke",
#    "color",
#    "stop-color",
#    "flood-color",
#    "lighting-color",
#    "solid-color"
# ]

SVG_ANIMATABLE_TRANSFORM_ATTRIBUTES = [
    "transform",
    "gradientTransform",
    "patternTransform"
]

SVG_ANIMATION_BEGIN_EVENTS = [
    "focus",
    "blur",
    "focusin",
    "focusout",
    "activate",
    "click",
    # "beforeinput",
    # "input",
    # "keydown",
    # "keyup",
    # "compositionstart",
    # "compositionupdate",
    # "compositionend",
    "load",
    # "unload",
    # "abort",
    # "error",
    "select",
    # "resize",
    "scroll",
    # "beginEvent",
    # "endEvent",
    # "repeatEvent"
]

SVG_ARIABLE_ELEMENTS = [
    "SVGAElement",
    "SVGCircleElement",
    "SVGCursorElement",
    "SVGDiscardElement",
    "SVGEllipseElement",
    "SVGForeignObjectElement",
    "SVGGElement",
    "SVGImageElement",
    "SVGLineElement",
    "SVGPathElement",
    "SVGPolygonElement",
    "SVGPolylineElement",
    "SVGRectElement",
    "SVGSVGElement",
    "SVGSwitchElement",
    "SVGSymbolElement",
    "SVGTSpanElement",
    "SVGTextElement",
    "SVGTextPathElement",
    "SVGViewElement"
]
