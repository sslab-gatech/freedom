from js import API, APITemplate, is_satiable_arg
from utils.random import Random


class LoadProperty(API):
    def __init__(self, ret, this, prop):
        super().__init__(ret, this)
        self.prop = prop

    def generate(self, context):
        self.this.generate(context)
        if self.ret is not None:
            self.ret.generate(context)
    
    def mutate(self, context) -> bool:
        return self.this.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)

    def __str__(self):
        if self.ret is None:
            return "{}.{}".format(str(self.this), self.prop)
        else:
            return "var {} = {}.{}".format(str(self.ret), str(self.this), self.prop)


class StoreProperty(API):
    def __init__(self, value, this, prop):
        super().__init__(None, this)
        self.value = value
        self.prop = prop

    def generate(self, context):
        self.this.generate(context)
        self.value.generate(context)
    
    def mutate(self, context) -> bool:
        if Random.bool():
            return self.this.mutate(context)
        else:
            return self.value.mutate(context)

    def merge_fix(self, merge_map):
        self.this.merge_fix(merge_map)
        self.value.merge_fix(merge_map)

    def __str__(self):
        return "{}.{} = {}".format(str(self.this), self.prop, str(self.value))


class LoadPropertyTemplate(APITemplate):
    def __init__(self, ret_class, this_class, prop):
        super().__init__(ret_class, this_class)
        self.prop = prop

    def instantiate(self):
        # assert self.ret_class is not None
        ret = self.ret_class() if self.ret_class is not None else None
        return LoadProperty(ret, self.this_class(), self.prop)

    def satiable(self, context):
        return True


class StorePropertyTemplate(APITemplate):
    def __init__(self, value_class, this_class, prop):
        super().__init__(None, this_class)
        self.value_class = value_class
        self.prop = prop

    def instantiate(self):
        assert self.value_class is not None
        return StoreProperty(self.value_class(), self.this_class(), self.prop)

    def satiable(self, context):
        return is_satiable_arg(self.value_class, context)
