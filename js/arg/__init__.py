from utils import dom_value as dv
from utils.random import Random
from abc import ABCMeta, abstractmethod


class Arg(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def is_object(self):
        pass

    @abstractmethod
    def generate(self, context):
        pass

    def mutate(self, context) -> bool:
        self.generate(context)
        return True

    def merge_fix(self, merge_map):
        pass

    @abstractmethod
    def __str__(self):
        pass


# ObjectArg has a name which indicates the object type
class ObjectArg(Arg):
    name = "Object"

    def __init__(self):
        super().__init__()
        self.obj = None

    def is_object(self):
        return True

    def generate(self, context):
        self.obj = context.get_offspring(self.name)
        assert (self.obj is not None)
        if self.obj is None:
            print("[-] Could not find objects: {}".format(self.name))
            assert False

    def merge_fix(self, merge_map):
        if self.obj in merge_map:
            self.obj = merge_map[self.obj]

    def __str__(self):
        return self.obj.id


# For misc apis that do not require a real object
class DummyArg(ObjectArg):
    name = "Dummy"


class ValueArg(Arg, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.value = None

    @abstractmethod
    def generate(self, context):
        pass

    def is_object(self):
        return False

    def __str__(self):
        return str(self.value)


class ConstValueArg(ValueArg):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def generate(self, _):
        pass


def ConstValueArgWrapper(value):
    return lambda: ConstValueArg(value)


class StringSetArg(ValueArg):
    def __init__(self, strings):
        super().__init__()
        self.strings = strings

    def generate(self, _):
        if len(self.strings):
            self.value = Random.choice(self.strings)
        else:
            self.value = Random.string()

    def __str__(self):
        return "\"" + self.value + "\""


def StringSetArgWrapper(strings):
    return lambda: StringSetArg(strings)


class Float01Arg(ValueArg):
    def generate(self, _):
        self.value = Random.float01()


class FloatArg(ValueArg):
    def generate(self, _):
        self.value = Random.number()


class StringArg(ValueArg):
    def generate(self, _):
        self.value = Random.string()

    def __str__(self):
        return "\"" + self.value + "\""


class StringArrayArg(ValueArg):
    def generate(self, _):
        self.value = "[\"{}\"]".format(Random.string())


class FloatStringArg(StringArg):
    def generate(self, _):
        self.value = Random.number()


class LengthPercentageArg(StringArg):
    def generate(self, _):
        self.value = dv.length_percentage()


class CharArg(StringArg):
    def generate(self, _):
        self.value = Random.char()


class ColorArg(StringArg):
    def generate(self, _):
        self.value = dv.color()


class ConstStringArg(StringArg):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def generate(self, _):
        if not self.value:
            self.value = Random.string()


def ConstStringArgWrapper(value):
    return lambda: ConstStringArg(value)


class DoNothingArg(ValueArg):
    def generate(self, _):
        self.value = "doNothing"


class BooleanArg(ValueArg):
    def generate(self, _):
        self.value = dv.boolean()


class IntegerArg(ValueArg):
    def generate(self, _):
        self.value = Random.integer()


class RangedIntegerArg(ValueArg):
    def __init__(self, low, high):
        super().__init__()
        self.low = low
        self.high = high

    def generate(self, _):
        self.value = Random.range(self.low, self.high)


RandomSelectorArg = lambda: RangedIntegerArg(0, 100)


class NullArg(ValueArg):
    def generate(self, _):
        pass

    def __str__(self):
        return "null"


class IndexArg(ValueArg):
    def generate(self, _):
        self.value = dv.index()


# ENUM
class EnumArg(ValueArg):
    def generate(self, _):
        self.value = Random.range(0, 16)


class ClockArg(ValueArg):
    def generate(self, _):
        self.value = dv.clock_in_s()


class ClockInMsArg(ValueArg):
    def generate(self, _):
        self.value = dv.clock_in_ms()


class RegexArg(StringArg):
    def generate(self, _):
        self.value = dv.regex()
