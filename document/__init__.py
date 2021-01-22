from config import TreeConfig, JSConfig, token_limit
from document.dom_tree import DOMTree
from document.css import CSS
from document.context import DOMContext
from object import factory as of
from utils.random import Random
from utils import helper

from enum import Enum


class Document:
    def __init__(self, max_element_count):
        self.label = None
        self.dom_tree = DOMTree(max_element_count)
        self.dom_context = DOMContext(token_limit)

        # dummy
        self.dom_context.create_object("Dummy")

        # window
        self.window = of.create_object("Window")
        self.window.id = "window"
        self.dom_context.add_object(self.window)

        # document
        self.document = of.create_object("Document")
        self.document.id = "document"
        self.dom_context.add_object(self.document)

        # entry point
        self.main = of.create_object("Function")
        self.main.id = "main"
        self.dom_context.add_object(self.main)

        # event handlers
        self.event_handlers = []
        for i in range(JSConfig.callback_count):
            eh = of.create_object("EventHandler")
            eh.id = "f{}".format(i)
            self.dom_context.add_object(eh)
            self.event_handlers.append(eh)

        # css
        self.sheet0 = of.create_object("CSSStyleSheet")
        self.sheet0.id = "sheet0"
        self.dom_context.add_object(self.sheet0)
        self.sheet1 = of.create_object("CSSKeyframesSheet")
        self.sheet1.id = "sheet1"
        self.dom_context.add_object(self.sheet1)

        self.css = CSS()
        self.css.init_keyframes(self.dom_context)
        self.css.init_css_variables(self.dom_context)

        # init function context
        self.main.init(self.dom_context)
        for eh in self.event_handlers:
            eh.init(self.dom_context)

    ############################################
    # For dumb fuzz
    ############################################
    def generate_nodes(self):
        self.dom_tree.generate_nodes(self.dom_context)

    def generate_attributes(self):
        self.dom_tree.generate_attributes(self.dom_context)

    def generate_css_rules(self):
        self.css.generate_css_rules(self.dom_context)

    def generate_js_functions(self):
        self.main.generate_additional_elements()
        self.main.generate_apis()
        for eh in self.event_handlers:
            eh.generate_additional_elements()
            eh.generate_apis()

    ############################################
    # For cov fuzz
    ############################################
    def insert_node(self):
        element_count = self.dom_tree.element_count
        if Random.selector(element_count + 1) == 0:
            element = self.dom_tree.insert_root_element(self.dom_context)
        else:
            element = self.dom_tree.insert_element(self.dom_context)
        return element is not None

    def fuzz_dom_tree(self):
        class DOMTreeMode(Enum):
            InsertNode = 1
            AppendAttribute = 2
            MutateAttribute = 3
            ReplaceAttribute = 4
            MutateText = 5

        dom_tree_modes = [
            DOMTreeMode.InsertNode,
            DOMTreeMode.AppendAttribute,
            DOMTreeMode.MutateAttribute,
            DOMTreeMode.ReplaceAttribute,
            DOMTreeMode.MutateText
        ]

        trial = 0
        while trial < 10:
            c = Random.choices(dom_tree_modes, [3, 3, 2, 5, 1])[0]
            if c == DOMTreeMode.InsertNode:
                ok = self.insert_node()
            elif c == DOMTreeMode.AppendAttribute:
                ok = self.dom_tree.append_attribute(self.dom_context)
            elif c == DOMTreeMode.MutateAttribute:
                ok = self.dom_tree.mutate_attribute(self.dom_context)
            elif c == DOMTreeMode.ReplaceAttribute:
                ok = self.dom_tree.replace_attribute(self.dom_context)
            else:
                ok = self.dom_tree.mutate_text()
            assert ok is not None
            if ok:
                return True
            trial += 1
        return False

    def fuzz_css(self):
        class CSSMode(Enum):
            Mutate = 1
            Append = 2
            Replace = 3
            Misc = 4
        css_modes = [CSSMode.Mutate, CSSMode.Append, CSSMode.Replace, CSSMode.Misc]
        css_weights = [10, 5, 1, 1]

        trial = 0
        while trial < 10:
            c = Random.choices(css_modes, css_weights)[0]
            if c == CSSMode.Mutate:
                ok = self.css.mutate_css_style_rule(self.dom_context)
            elif c == CSSMode.Append:
                ok = self.css.append_css_style_rule(self.dom_context)
            elif c == CSSMode.Replace:
                ok = self.css.replace_css_style_rule(self.dom_context)
            else:
                if Random.bool():
                    ok = self.css.mutate_css_keyframes_rule(self.dom_context)
                else:
                    ok = self.css.mutate_css_variable(self.dom_context)
            assert ok is not None
            if ok:
                return True
            trial += 1
        return False

    def fuzz_js_functions(self):
        trial = 0
        while trial < 10:
            target_func = self.main if Random.bool() else Random.choice(self.event_handlers)
            c = Random.selector(4)
            if c == 0:
                ok = target_func.append_api()
            elif c == 1:
                ok = target_func.insert_api()
            elif c == 2:
                ok = target_func.replace_api()
            else:
                ok = target_func.mutate_api()
            if ok:
                return True
            trial += 1
        return False

    def merge(self, other):
        if not self.dom_tree.allow_merge():
            return False

        merge_map = {
            other.window: self.window,
            other.document: self.document,
            other.sheet0: self.sheet0,
            other.sheet1: self.sheet1
        }
        for i in range(len(self.event_handlers)):
            merge_map[other.event_handlers[i]] = self.event_handlers[i]

        merge_inserts = self.dom_tree.merge(self.dom_context, other.dom_tree, merge_map)
        for element in merge_map.values():
            if element.is_element and element.is_in_tree:
                element.merge_fix(merge_map)
        for element in merge_inserts:
            element.merge_fix(merge_map)

        if self.css.allow_merge():
            self.css.merge(other.css, merge_map)

        self.main.merge(other.main, merge_map)
        for i in range(len(self.event_handlers)):
            self.event_handlers[i].merge(other.event_handlers[i], merge_map)

        # for x, y in merge_map.items():
        #    print("{}: {}".format(x.id, y.id))
        # print(other.dom_tree.element_count)
        # print(self.dom_tree.element_count)
        return True

    def __str__(self):
        head = "<head>\n"
        head += str(self.css)

        head += "<script>\n"
        head += helper.do_nothing + "\n"
        head += helper.gc + "\n"

        head += "var run_count = { \"main\": 0, "
        for eh in self.event_handlers:
            head += "\"{}\": 0, ".format(eh.id)
        head += "};\n"

        head += str(self.main)
        for eh in self.event_handlers:
            head += str(eh)
        head += "</script>\n"
        head += "</head>\n\n"

        body = "<body onload=\"{}()\">\n".format(self.main.id)
        body += str(self.dom_tree)
        body += "</body>\n\n"

        return "<!DOCTYPE html>\n<html>\n\n{}{}</html>\n".format(head, body)
