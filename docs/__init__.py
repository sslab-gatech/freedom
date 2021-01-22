from docs import html, svg, css, hierarchy


# Object Hierarchy
def get_object_offsprings(name):
    ret = [name]
    if name in hierarchy.OFFSPRINGS:
        ret.extend(hierarchy.OFFSPRINGS[name])
    return ret


def get_object_ancestors(name):
    ret = [name]
    if name in hierarchy.ANCESTORS:
        ret.extend(hierarchy.ANCESTORS[name])
    return ret


# HTML
html_tags = list(html.HTML_ELEMENT_MAP.values())
html_elements = html.HTML_ELEMENTS
html_general_child_elements = html.HTML_GENERAL_CHILD_ELEMENTS
html_other_child_elements = html.HTML_OTHER_CHILD_ELEMENTS
html_child_elements = html.HTML_CHILD_ELEMENTS
html_labelable_elements = html.HTML_LABELABLE_ELEMENTS
html_elem_to_tag_map = html.HTML_ELEMENT_MAP
html_tag_to_elem_map = {v: k for k, v in html.HTML_ELEMENT_MAP.items()}
html_block_elements = html.BLOCK_ELEMENTS
html_link_elements = html.LINK_ELEMENTS
html_submittable_elements = html.SUBMITTABLE_ELEMENTS

# SVG
svg_tags = list(svg.SVG_ELEMENTS.values())
svg_elements = list(svg.SVG_ELEMENTS.keys())
svg_child_elements = svg.SVG_CHILD_ELEMENTS
svg_animation_elements = svg.SVG_ANIMATION_ELEMENTS
svg_paint_server_elements = svg.SVG_PAINT_SERVER_ELEMENTS
svg_shape_elements = svg.SVG_SHAPE_ELEMENTS
svg_gradient_elements = ["SVGLinearGradientElement", "SVGRadialGradientElement"]
svg_text_content_elements = svg.SVG_TEXT_CONTENT_ELEMENTS
svg_filter_primitives = svg.SVG_FILTER_PRIMITIVES

svg_elem_to_tag_map = svg.SVG_ELEMENTS
svg_tag_to_elem_map = {v: k for k, v in svg.SVG_ELEMENTS.items()}

svg_animation_begin_events = svg.SVG_ANIMATION_BEGIN_EVENTS
svg_animatable_attributes = svg.SVG_ANIMATABLE_ATTRIBUTES
svg_animatable_transform_attributes = svg.SVG_ANIMATABLE_TRANSFORM_ATTRIBUTES

svg_ariable_elements = svg.SVG_ARIABLE_ELEMENTS

elements = html_elements + svg_elements
image_elements = ["HTMLImageElement", "SVGImageElement"]


def tag_from_element(elem):
    if elem in svg_elements:
        return svg_tag_from_element(elem)
    elif elem in html_elements:
        return html_tag_from_element(elem)
    assert False


def html_tag_from_element(elem):
    return html_elem_to_tag_map[elem]


def is_html_text_element(elem):
    return elem in html.HTML_TEXT_ELEMENTS


def is_html_element(elem):
    return elem in html_elements


def is_svg_element(elem):
    return elem in svg_elements


def svg_tag_from_element(elem):
    return svg_elem_to_tag_map[elem]


def is_svg_text_element(elem):
    return elem in svg.SVG_DESCRIPTIVE_ELEMENTS or \
        elem in svg.SVG_TEXT_CONTENT_ELEMENTS


def is_html_empty_element(elem):
    return elem in html.HTML_EMPTY_ELEMENTS


def is_html_raw_text_element(elem):
    return elem in html.HTML_RAW_TEXT_ELEMENTS


# CSS
css_animatable_properties = css.CSS_ANIMATABLE_PROPERTIES


# Event
# TODO: composition events
text_events = ["textInput"]
base_ui_events = ["load", "unload", "abort", "error", "select"]
mouse_events = ["click", "mousedown", "mouseup", "mouseover", "mousemove", "mouseout"]
focus_events = ["blur", "focus", "focusin", "focusout"]
wheel_events = ["wheel"]
input_events = ["beforeinput", "input"]
keyboard_events = ["keydown", "keyup", "keypress"]
composition_events = ["compositionstart", "compositionupdate", "compositionend"]
ui_events = base_ui_events + mouse_events + focus_events + wheel_events + input_events + keyboard_events + composition_events

mutation_events = ["DOMSubtreeModified", "DOMNodeInserted", "DOMNodeRemoved", "DOMAttrModified", "DOMCharacterDataModified"]
