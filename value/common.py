from value import StaticValue
from utils import dom_value as dv
from utils.random import Random


class EmptyValue(StaticValue):
    def generate(self, _):
        self.value = ""


class YesOrNoValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["yes", "no"])


class BooleanValue(StaticValue):
    def generate(self, _):
        self.value = dv.boolean()


class StringValue(StaticValue):
    def generate(self, _):
        self.value = Random.string()


class IntegerValue(StaticValue):
    def generate(self, _):
        self.value = Random.integer()


class IntegerLengthValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = Random.integer()
        else:
            self.value = dv.length()


class SignedIntegerValue(StaticValue):
    def generate(self, _):
        self.value = Random.signed_integer()


class NumberValue(StaticValue):
    def generate(self, _):
        self.value = Random.number()


class NumberOptionalNumberValue(StaticValue):
    def generate(self, _):
        self.value = dv.number_optional_number(False)


class SignedNumberOptionalNumberValue(StaticValue):
    def generate(self, _):
        self.value = dv.number_optional_number(True)


class LengthValue(StaticValue):
    def generate(self, _):
        self.value = dv.length()


class LengthPercentageValue(StaticValue):
    def generate(self, _):
        self.value = dv.length_percentage()


class LengthPercentageIntegerValue(StaticValue):
    def generate(self, _):
        if Random.bool():
            self.value = dv.length_percentage()
        else:
            self.value = Random.integer()


class AngleValue(StaticValue):
    def generate(self, _):
        self.value = dv.angle()


class IndexValue(StaticValue):
    def generate(self, _):
        self.value = dv.index()


class ClockValue(StaticValue):
    def generate(self, _):
        self.value = dv.clock()


class CharValue(StaticValue):
    def generate(self, _):
        self.value = Random.char()


class OnOrOffValue(StaticValue):
    def generate(self, _):
        self.value = Random.choice(["on", "off"])


class RegexValue(StaticValue):
    def generate(self, _):
        self.value = dv.regex()


class ClockInMsValue(StaticValue):
    def generate(self, _):
        self.value = dv.clock_in_ms()
