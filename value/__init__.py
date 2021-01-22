from abc import abstractmethod, ABCMeta


class Value(metaclass=ABCMeta):
    def __init__(self):
        self.value = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def generate(self, context):
        pass

    @abstractmethod
    def merge_fix(self, merge_map):
        pass

    def mutate(self, context) -> bool:
        self.generate(context)
        return True


# A string value that can be independently generated as always.
class StaticValue(Value, metaclass=ABCMeta):
    def merge_fix(self, _):
        pass

    def __str__(self):
        return self.value


class ConstValue(StaticValue):
    def __init__(self, const):
        super().__init__()
        self.value = const

    def generate(self, _):
        pass

    def mutate(self, _) -> bool:
        return False


def ConstValueWrapper(const):
    return lambda: ConstValue(const)


class DynamicValue(Value, metaclass=ABCMeta):
    @abstractmethod
    def generate(self, context):
        pass

    @abstractmethod
    def merge_fix(self, merge_map):
        pass
