import random


class Random:
    shuffle = random.shuffle
    uniform = random.uniform
    sample = random.sample
    choices = random.choices
    interesting_chars = ["0", "1", "A"]

    @staticmethod
    def choice(l):
        if len(l) == 0: return None
        return random.choice(l)

    @staticmethod
    def bool():
        return bool(random.getrandbits(1))

    @staticmethod
    def selector(num):
        return Random.range(0, num - 1)

    @staticmethod
    # low <= n <= high
    def range(low: int, high: int) -> int:
        return random.randint(low, high)

    @staticmethod
    def string():
        size = Random.choice([0, 1, 2, 4, 8, 10, 15, 16, 20, 31, 32, 40, 63, 64, 100, 200])
        # return "".join([Random.choice(Random.interesting_chars) for _ in range(size)])
        return "A" * size

    @staticmethod
    def char():
        return Random.choice(Random.interesting_chars + [" ", ""])

    @staticmethod
    def integer():
        c = Random.selector(7)
        if c == 0:
            v = 0
        elif c == 1:
            v = 0
        elif c == 2:
            v = 1
        elif c == 3:
            v = Random.range(0, 16)
        elif c == 4:
            v = Random.range(0, 100)
        elif c == 5:
            v = Random.range(0, 1000)
        else:
            c2 = Random.selector(4)
            if c2 == 0:
                v = 1 << Random.range(1, 16)
            elif c2 == 1:
                v = 1 << Random.range(1, 16) + 1
            elif c2 == 2:
                v = 1 << Random.range(1, 16) - 1
            else:
                v = Random.range(0, 50000)
        return str(v)

    @staticmethod
    def signed_integer():
        if Random.bool():
            return Random.integer()
        else:
            return "-{}".format(Random.integer())

    @staticmethod
    def hex_digit():
        return Random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])

    @staticmethod
    def hex_digits(num):
        return "".join([Random.hex_digit() for _ in range(num)])

    @staticmethod
    def hex_byte():
        return str(Random.range(0, 255))

    @staticmethod
    def float01():
        if Random.bool():
            return str(random.choice([0, 1]))
        else:
            return "%.2f" % random.uniform(0, 1)

    @staticmethod
    def number():
        if Random.bool():
            return Random.float01()
        else:
            return Random.integer()

    @staticmethod
    def signed_number():
        if Random.bool():
            return Random.number()
        else:
            return "-{}".format(Random.number())

    @staticmethod
    def selectors(n):
        x = Random.range(1, (1 << n) - 1)
        bits = []
        while x > 0:
            bits.append(x & 1)
            x = x >> 1
        while len(bits) < n:
            bits.append(0)
        return bits
