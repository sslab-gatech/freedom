from js import API, APITemplate, is_satiable_arg
from js.arg import DummyArg
from utils import seq
from utils.random import Random


class CallFunction(API):
    def __init__(self, ret, this, method, args):
        super().__init__(ret, this)
        self.method = method
        self.args = args

    def generate(self, context):
        self.this.generate(context)
        for arg in self.args:
            arg.generate(context)
        if self.ret is not None:
            self.ret.generate(context)
    
    def mutate(self, context) -> bool:
        c = Random.selector(1 + len(self.args))
        if c == 0:
            return self.this.mutate(context)
        else:
            arg = Random.choice(self.args)
            return arg.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        for arg in self.args:
            arg.merge_fix(merge_map)

    def __str__(self):
        lhs = ""
        if self.ret is not None:
            lhs = "var {} = ".format(str(self.ret))
        rhs = "{}.{}({})".format(str(self.this), self.method, ",".join(list(map(str, self.args))))
        return lhs + rhs


class FunctionTemplate(APITemplate):
    def __init__(self, ret_class, this_class, method, *arg_classes):
        super().__init__(ret_class, this_class)
        self.method = method
        self.arg_classes = arg_classes

    def instantiate(self):
        args = []
        for arg_class in self.arg_classes:
            args.append(arg_class())
        ret = self.ret_class() if self.ret_class is not None else None
        return CallFunction(ret, self.this_class(), self.method, args)

    def satiable(self, context):
        for arg_class in self.arg_classes:
            if not is_satiable_arg(arg_class, context):
                return False
        return True


class Construct(API):
    def __init__(self, ret, ctor, args):
        super().__init__(ret, None)
        self.ctor = ctor
        self.args = args

    def generate(self, context):
        for arg in self.args:
            arg.generate(context)
        self.ret.generate(context)
    
    def mutate(self, context) -> bool:
        if len(self.args) == 0:
            return False

        arg = Random.choice(self.args)
        return arg.mutate(context)

    def merge_fix(self, merge_map):
        for arg in self.args:
            arg.merge_fix(merge_map)

    def __str__(self):
        return "var {} = new {}({})".format(str(self.ret), self.ctor, ",".join(list(map(str, self.args))))


class ConstructTemplate(APITemplate):
    def __init__(self, ret_class, ctor, *arg_classes):
        super().__init__(ret_class, DummyArg)
        self.ctor = ctor
        self.arg_classes = arg_classes

    def instantiate(self):
        args = []
        for arg_class in self.arg_classes:
            args.append(arg_class())
        return Construct(self.ret_class(), self.ctor, args)

    def satiable(self, context):
        for arg_class in self.arg_classes:
            if not is_satiable_arg(arg_class, context):
                return False
        return True


class ConstructObject(API):
    def __init__(self, ret, shape):
        super().__init__(ret, None)
        self.shape = shape

    def generate(self, context):
        for value in self.shape.values():
            value.generate(context)
        self.ret.generate(context)

    def mutate(self, context) -> bool:
        if len(self.shape) == 0:
            return False

        value = Random.choice(list(self.shape.values()))
        return value.mutate(context)

    def merge_fix(self, merge_map):
        for value in self.shape.values():
            value.merge_fix(merge_map)

    def __str__(self):
        return "var {} = {{ {} }}".format(
            str(self.ret),
            seq(["{}: {}".format(prop, str(value)) for prop, value in self.shape.items()])
        )


class ConstructObjectTemplate(APITemplate):
    def __init__(self, ret_class, shape_classes):
        super().__init__(ret_class, DummyArg)
        self.shape_classes = shape_classes

    def instantiate(self):
        shape = {}
        for prop, value_class in self.shape_classes.items():
            shape[prop] = value_class()
        return ConstructObject(self.ret_class(), shape)

    def satiable(self, context):
        for value_class in self.shape_classes.values():
            if not is_satiable_arg(value_class, context):
                return False
        return True
