from js import APITemplate, API, add_api, is_satiable_arg
from js.arg import DummyArg
from js.arg.html import EventHandlerArg
from utils import dom_value as dv
from utils.random import Random


#####################################
# x = null; gc();
#####################################
def object_filter(obj):
    return (obj.name not in {
                "Document", "Function", "Window", "EventHandler", "Dummy", "CSSStyleSheet", "CSSKeyframesSheet"
            }) and (not (obj.is_element and obj.is_in_tree))


class DerefObject(API):
    def __init__(self):
        super().__init__(None, None)
        self.obj = None

    def generate(self, context):
        objs = list(filter(object_filter, context.iter_object()))
        if len(objs) > 0:
            self.obj = Random.choice(objs)
        else:
            self.obj = None
    
    def mutate(self, context):
        self.generate(context)

    def merge_fix(self, merge_map):
        if self.obj is not None and self.obj in merge_map:
            self.obj = merge_map[self.obj]

    def __str__(self):
        s = ""
        if self.obj is not None:
            s += "{} = null; ".format(self.obj.id)
        s += "gc()"
        return s


class DerefObjectTemplate(APITemplate):
    def __init__(self):
        super().__init__(None, DummyArg)

    def instantiate(self):
        return DerefObject()

    def satiable(self, context):
        return True


#####################################
# gc();
#####################################
class GC(API):
    def __init__(self):
        super().__init__(None, None)

    def generate(self, _):
        pass

    def mutate(self, _) -> bool:
        return False

    def merge_fix(self, _):
        pass

    def __str__(self):
        return "gc()"


class GCTemplate(APITemplate):
    def __init__(self):
        super().__init__(None, DummyArg)

    def instantiate(self):
        return GC()

    def satiable(self, context):
        return True


class SetTimeout(API):
    def __init__(self, eh):
        super().__init__(None, None)
        self.eh = eh
        self.timeout = None

    def generate(self, context):
        self.eh.generate(context)
        self.timeout = dv.clock_in_ms()
    
    def mutate(self, _):
        pass

    def merge_fix(self, _):
        pass

    def __str__(self):
        return "setTimeout({}, {})".format(str(self.eh), self.timeout)


class SetTimeoutTemplate(APITemplate):
    def __init__(self):
        super().__init__(None, DummyArg)
        self.eh_class = EventHandlerArg

    def instantiate(self):
        return SetTimeout(self.eh_class())

    def satiable(self, context):
        return is_satiable_arg(self.eh_class, context)


def initialize_misc_apis():
    # add_api(DerefObjectTemplate())
    add_api(GCTemplate())
    # add_api(SetTimeoutTemplate())
