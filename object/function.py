from config import JSConfig, GlobalConfig
from object import Object
from document.context import JSContext
from js import get_api_count
from js import apis as js_apis
from js.function.html import create_interesting_html_element
from utils.random import Random


def try_catch(s):
    # return "try {{ {}; }} catch (e) {{ console.log(e.message); }}\n".format(s)
    return "try {{ {}; }} catch (e) {{ }}\n".format(s)


class Function(Object):
    def __init__(self, name="Function", is_callback=False):
        super().__init__(name)
        self.is_callback = is_callback
        self.apis = []
        self.context = None

    @property
    def api_count(self):
        return len(self.apis)

    @property
    def full(self):
        return self.api_count >= JSConfig.max_api_count

    def init(self, dom_context):
        self.context = JSContext(dom_context)

    def generate_additional_elements(self):
        for _ in range(JSConfig.additional_html_var_count):
            self.apis.append(create_interesting_html_element(self.context))
            self.context.line += 1

    def generate_api(self):
        # 1. select an alive object (type)
        obj_names = list(self.context.superset_at_line)
        weights = [get_api_count(name) for name in obj_names]

        # 2. select an api that uses the object name as |this|
        while True:
            name = Random.choices(obj_names, weights)[0]
            template = Random.choice(js_apis[name])
            if template.satiable(self.context):
                api = template.instantiate()
                api.generate(self.context)
                return api

    ############################################
    # For dumb fuzz
    ############################################
    def generate_apis(self):
        if not self.is_callback:
            count = JSConfig.max_api_count
        else:
            count = int(JSConfig.max_api_count / 2)
        for _ in range(count):
            self.append_api()

    ############################################
    # For cov fuzz
    ############################################
    # A1
    def append_api(self):
        if self.full:
            return False
        self.context.line = len(self.apis)
        api = self.generate_api()
        self.apis.append(api)
        return True

    # A2
    def insert_api(self):
        line = Random.selector(self.api_count + 1)
        self.context.shift_object_location(line)
        self.context.line = line
        api = self.generate_api()
        self.apis.insert(line, api)
        return True

    # A3
    def replace_api(self):
        if self.api_count == 0:
            return False
        trial = 0
        while trial < self.api_count:
            line = Random.selector(self.api_count)
            self.context.line = line
            old_api = self.apis[line]
            if old_api.ret is None:
                new_api = self.generate_api()
                self.apis[line] = new_api
                return True
            trial += 1
        return False

    # A4
    def mutate_api(self):
        if self.api_count == 0:
            return False
        line = Random.selector(self.api_count)
        self.context.line = line
        api = self.apis[line]
        return api.mutate(self.context)

    def merge_api(self, api, line):
        self.context.line = line
        self.context.shift_object_location(line)
        self.apis.insert(line, api)
        if api.ret is not None:
            api.ret.merge_fix(self.context)

    def merge(self, other, merge_map):
        p = q = 0
        while p < self.api_count and q < other.api_count:
            if Random.bool():
                p += 1
                continue

            other_api = other.apis[q]
            other_api.merge_fix(merge_map)
            self.merge_api(other_api, p)
            p += 1
            q += 1

        if q < other.api_count:
            for i in range(q, other.api_count):
                self.merge_api(other.apis[i], p)
                p += 1

    def __str__(self):
        s = "function {}() {{\n\n".format(self.id)

        s += "run_count[\"{}\"]++;\n".format(self.id)
        s += "if (run_count[\"{}\"] > 2) return;\n\n".format(self.id)

        # include all elements from dom tree
        for o in self.context.global_context.in_tree_elements:
            s += "var {0} = document.getElementById(\"{0}\");\n".format(o.id)
        s += try_catch("var sheet0 = document.styleSheets[0]")
        s += try_catch("var sheet1 = document.styleSheets[1]")

        for api in self.apis:
            s += try_catch(str(api))

        s += "gc();\n}\n"
        return s


class EventHandler(Function):
    def __init__(self):
        super().__init__("EventHandler", True)
