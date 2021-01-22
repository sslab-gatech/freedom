bitmap_size = 1 << 16


class TreeConfig:
    attribute_weight = {
        "regular": 5,
        "presentation": 3,
        "global": 2,
        "aria": 1
    }
    max_attribute_count = 10
    root_element_count = 10
    max_element_count = 80
    min_element_count = 40
    avg_element_count = 60
    max_depth = 3


class JSConfig:
    callback_count = 5
    max_api_count = 1000
    additional_html_var_count = 5


class CSSConfig:
    use_css_var = 10
    max_css_count = 50
    max_css_selector_count = 3
    max_css_decl_count = 20
    max_css_keyframe_count = 5
    max_css_keyframe_decl_count = 5
    max_css_internal_decl_count = 5


token_limit = {
    "class": 5,
    "part": 2,
    "keyframes": 5,
    "counter": 2,
    "mediagroup": 2,
    "radiogroup": 2,
    "axis": 2
}


class GlobalConfig:
    merge = False
    generation = False
    merge_count = 5
    mutation_count = 5
    mutation_trials = 50
