DEBUG = False


def cat(args: [str]) -> str:
    return " ".join(args)


def seq(args: [str]) -> str:
    return ",".join(args)


def semi(args: [str]) -> str:
    return ";".join(args)


def stringify(s: str) -> str:
    return "\"{}\"".format(s)


def debug_print(s):
    if DEBUG:
        print(s)


def wprint(s):
    print(bcolors.WARNING + s + bcolors.ENDC)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'