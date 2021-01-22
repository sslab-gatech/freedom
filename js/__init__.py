from abc import ABCMeta, abstractmethod

apis = {}


class API(metaclass=ABCMeta):
    def __init__(self, ret, this):
        self.ret = ret
        self.this = this

    @abstractmethod
    def generate(self, context):
        pass

    @abstractmethod
    def mutate(self, context) -> bool:
        pass

    @abstractmethod
    def merge_fix(self, merge_map):
        pass

    @abstractmethod
    def __str__(self):
        pass


class APITemplate(metaclass=ABCMeta):
    def __init__(self, ret_class, this_class):
        self.ret_class = ret_class
        self.this_class = this_class

    @abstractmethod
    def instantiate(self):
        pass

    @abstractmethod
    def satiable(self, context):
        pass


def is_satiable_arg(arg, context):
    if not hasattr(arg, "name"):
        return True
    return context.contains(arg.name)


def get_api_count(name):
    if name not in apis:
        return 0
    return len(apis[name])


def add_api(t):
    name = t.this_class.name
    if name not in apis:
        apis[name] = []
    apis[name].append(t)
