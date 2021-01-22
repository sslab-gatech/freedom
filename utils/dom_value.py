from utils import seq, cat
from utils.random import Random


##################################
# Helper
##################################
def list_size():
    if Random.bool():
        return Random.range(1, 5)
    else:
        # Special sizes that may trigger realloc
        # See ./animations/crash-when-animation-is-running-while-getting-value.html
        return Random.choice([7, 8, 9, 15, 16, 17, 31, 32, 33, 63, 64, 65])


##################################
# Basics
##################################
def boolean():
    return Random.choice(("true", "false"))


def number_optional_number(signed):
    if signed:
        return seq([Random.signed_number(), Random.signed_number()])
    else:
        return seq([Random.number(), Random.number()])


def length(relative=False):
    if (not relative) or Random.bool():
        if Random.bool():
            return "{}px".format(Random.integer())
        else:
            return "{}em".format(Random.number())
    else:
        return "{}{}".format(Random.integer(), Random.choice(["vw", "vh", "vmin", "vmax"]))


def percentage():
    if Random.bool():
        return Random.choice(["0%", "100%"])
    else:
        return "{}%".format(Random.range(0, 100))


def length_percentage(relative=False):
    if Random.bool():
        return length(relative)
    else:
        return percentage()


def number_percentage():
    if Random.bool():
        return Random.number()
    else:
        return percentage()


def angle():
    return "{}deg".format(Random.choice(["0", "90", "180", "360"]))


def angle_percentage():
    if Random.bool():
        return angle()
    else:
        return percentage()


def color():
    c = Random.selector(5)
    if c == 0:
        return Random.choice(["currentColor", "transparent"])
    elif c == 1:
        return Random.choice(["red", "blue", "green", "black", "white"])
    elif c == 2:
        return "#{}".format(Random.hex_digits(Random.choice([6, 8])))
    elif c == 3:
        return "rgb({})".format(seq([Random.hex_byte() for _ in range(3)]))
    else:
        return "rgba({})".format(seq([Random.hex_byte() for _ in range(4)]))


def index():
    if Random.selector(5) == 0:
        return Random.integer()
    else:
        return str(Random.range(0, 8))


##################################
# Url
##################################
def frame_url():
    return "data:text/html,foo"


def image_url():
    return "data:image/gif;base64,{}".format(Random.choice((
        "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAIAAABt"
        "+uBvAAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wDGhYvCNVA1EIAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAjklEQVR42u3QIQEAMAgAsHNNVspTgARY1BZh0ZWP3VcgSJAgQYIECRKEIEGCBAkSJEgQggQJEiRIkCBBCBIkSJAgQYIECUKQIEGCBAkSJAhBggQJEiRIkCAECRIkSJAgQYIEIUiQIEGCBAkShCBBggQJEiRIEIIECRIkSJAgQYIQJEiQIEGCBAlCkCBBdwaeugIthHvZ+AAAAABJRU5ErkJggg==",
        "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABGdBTUEAALGPC"
        "/xhBQAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABh0RVh0U29mdHdhcmUAUGFpbnQuTkVUIHYzLjIyt5EXfQAAAU5JREFUeF7t07ENACAMxMDA"
        "/jsDBTtcY6TUlmx+zcx510MGNuKG"
        "/QYKgL9CAQqADWB8CygANoDxLaAA2ADGt4ACYAMY3wIKgA1gfAsoADaA8S2gANgAxreAAmADGN8CCoANYHwLKAA2gPEtoADYAMa3gAJgAxjfAgqADWB8CygANoDxLaAA2ADGt4ACYAMY3wIKgA1gfAsoADaA8S2gANgAxreAAmADGN8CCoANYHwLKAA2gPEtoADYAMa3gAJgAxjfAgqADWB8CygANoDxLaAA2ADGt4ACYAMY3wIKgA1gfAsoADaA8S2gANgAxreAAmADGN8CCoANYHwLKAA2gPEtoADYAMa3gAJgAxjfAgqADWB8CygANoDxLaAA2ADGt4ACYAMY3wIKgA1gfAsoADaA8S2gANgAxreAAmADGN8CCoANYHwLKAA2gPEtAAe4i54BvwLfXFAAAAAASUVORK5CYII="
    )))


def video_url():
    return "data:video/mp4;base64,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 "


def audio_url():
    return "data:audio/mp3;base64,//uQxAAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAADAAAGhgBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVWqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr///////////////////////////////////////////8AAAA5TEFNRTMuOTlyAc0AAAAAAAAAABSAJAKjQgAAgAAABoaLLYLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//uQxAAAVHoO86Ch/wKrQh+UIz/YShKDZqEIAAE3kQFg+NSyUDm5f/yB+D/GP8hjmzG6Jy7lvFu8Iif7i7vApIeVfN/DkGIKGInCaJxNu9wifzeiTfJlaJX/Np//9wKClWWDcG4vBiIYwcB4NHigohguDcBcIxSiAaB4JAgT6jf2YDkQi5/mmabkya6nTRBy5uRyKB48TiFogeguDih66JwykEQBKzjbzTdl3FjUCgfnYZFWM01W3xx4g/qtMn//v/////9+j9oeZe+G35O3ZKZ9f+8N1LCTyD5/hhewsfDj0TDUzpMMkhzaPS6TS172Po89nnJ1mln9/pod31/j4jYgPWx7Aq5MUFns3tUmlSzP2fSvZYbOVT9OP3yLJ4kTEQacS6PSzeXtGQ2It0A5GhIiGn0WMgS8ajcLgZ5bBbhuIFSj0FuHwJQsY9yIPgmZ0C5kpLKpyAaBMiOBSC9Lmcypf2WJKVNItoAE2UDUo2XGvl3+5Sn5///efkKpqSl6nNZq7mRvk4LTEpFJ8EAuIIcxAhRdGejHgAcDIOpMMVju//uSxB6AVKYRAYCN/sKXwiAoFL/gDcjA/qGXMzOkX/l6QcZi6hvb6Y4WczOL93AnkfJl7CVqfnbUQ0Ho3KpwmVbcT59DQkvrEhSnUC6Vj6U8DvLevkCV5hs+WMupZKsylEjyvcT0cEcY7S2P0YSlVGAubM6oKYf5cj6jZk1KwsxdIeZzRc/S4vzv5eR9ur/9Leh0fZPPeV5uvbrzTv1SuTy5NxTyW3CF0vrF1tLFsuFa7336yxlTi7cnKcof3kvPKu5/1fyqy/lVf2b1DpDDpE7RIhSOJDZQicyQqsmKYEpKJ2M6IbchCvO84TjUCHIWP411MmlAd6cVrAhDUf5xJU/mJkJihqdI4dY9D5RrxBi+sQeEacRPSTBouAj48i+Lh04Z/8v/mf/f////+8V7RiRllObiOvpaJWu06xcyGP0pkpaptJDnnhj0eWiixyiewi5rebgxesayRHMuP+27WN/HfdbJvEP4fQXk7++VdHVMZm+0Oe2aU4o1xHQ5iSKepDeM60sIchLEqmFqep1TE9OEwxKtsdOtj1EFMyJsxcoWMv/7ksQ/gFTqEPwAmf7CYEId8BM/4JpLqWw6TTWAcxNS6msRk0RbhJT6D+FfP4lBBVSsgOJvhmkkOEjSBhUgSJQIpiTyc1V/nL+i/8UK//upf/4Sf9vjfy8+nynnTUTkjVVv7VZGEnfN9PLHSckai1d/TotT5X/9PLV2rznavW+ZYltU8yxyRqTkUTkjcaTlgpiU0XVgsUcmATAkqN8xYUZh3lOsCilexWJqjvXq8hR+qluTrIW5pOUyTCLESFHH6dLVGP5Li2qxlP1UD1JclJkro0lDNtVMQU1FMy45OS41VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVU="


def track_url():
    return "data:text/vtt;base64,V0VCVlRUCgowMDowMDowMC4wMDAgLS0+IDAwOjAwOjAxLjAwMApTb21ldGhpbmcuCgowMDowMDowMS4wMDAgLS0+IDAwOjAwOjAyLjAwMApBbm90aGVyLg=="


##################################
# Path
##################################
def move_to():
    cmd = Random.choice(["M", "m"])
    x = Random.integer()
    y = Random.integer()
    return "{} {},{}".format(cmd, x, y)


def line_to():
    if Random.bool():
        cmd = Random.choice(["L", "l"])
        x = Random.integer()
        y = Random.integer()
        return "{} {},{}".format(cmd, x, y)
    else:
        cmd = Random.choice(["H", "h", "V", "v"])
        x = Random.integer()
        return "{} {}".format(cmd, x)


def bezier_curve():
    c = Random.selector(3)
    if c == 0:
        cmd = Random.choice(["C", "c"])
        x1 = Random.integer()
        y1 = Random.integer()
        x2 = Random.integer()
        y2 = Random.integer()
        x = Random.integer()
        y = Random.integer()
        return "{} {},{} {},{} {},{}".format(cmd, x1, y1, x2, y2, x, y)
    elif c == 1:
        cmd = Random.choice(["Q", "q", "S", "s"])
        x2 = Random.integer()
        y2 = Random.integer()
        x = Random.integer()
        y = Random.integer()
        return "{} {},{} {},{}".format(cmd, x2, y2, x, y)
    else:
        cmd = Random.choice(["T", "t"])
        x = Random.integer()
        y = Random.integer()
        return "{} {},{}".format(cmd, x, y)


def arc_curve():
    cmd = Random.choice(["A", "a"])
    rx = Random.integer()
    ry = Random.integer()
    _angle = Random.integer()
    large_arc_flag = Random.range(0, 1)
    sweep_flag = Random.range(0, 1)
    dx = Random.integer()
    dy = Random.integer()
    return "{} {} {} {} {} {} {},{}".format(cmd, rx, ry, _angle, large_arc_flag, sweep_flag, dx, dy)


def close_path():
    return Random.choice(["Z", "z"])


def path_cmd():
    c = Random.selector(5)
    if c == 0:
        return move_to()
    elif c == 1:
        return line_to()
    elif c == 2:
        return bezier_curve()
    elif c == 3:
        return arc_curve()
    else:
        return close_path()


def path():
    num = list_size()
    if num == 0:
        return ""

    values = [move_to()]
    for _ in range(num - 1):
        values.append(path_cmd())

    return cat(values)


def position():
    c = Random.selector(3)
    if c == 0:
        values = [Random.choice(["left", "center", "right"])]
        if Random.bool():
            values.append(Random.choice(["top", "center", "bottom"]))
        return cat(values)
    elif c == 1:
        values = [Random.choice(["left", "center", "right"]), length_percentage()]
        if Random.bool():
            values.extend([Random.choice(["top", "center", "bottom"]), length_percentage()])
        return cat(values)
    else:
        return cat([length_percentage(), length_percentage()])


##################################
# Transform
##################################
def matrix():
    value = seq([Random.number() for _ in range(6)])
    return "matrix({})".format(value)


def translate():
    num = Random.range(1, 2)
    value = seq([length_percentage() for _ in range(num)])
    return "translate({})".format(value)


def translate_x():
    return "translateX({})".format(length_percentage())


def translate_y():
    return "translateY({})".format(length_percentage())


def scale():
    num = Random.range(1, 2)
    value = seq([Random.number() for _ in range(num)])
    return "scale({})".format(value)


def scale_x():
    return "scaleX({})".format(Random.number())


def scale_y():
    return "scaleY({})".format(Random.number())


def rotate():
    # values = [angle()]
    # if Random.bool():
    #    values.extend([Random.integer(), Random.integer()])
    return "rotate({})".format(angle())


def skew():
    num = Random.range(1, 2)
    value = seq([angle() for _ in range(num)])
    return "skew({})".format(value)


def skew_x():
    return "skewX({})".format(angle())


def skew_y():
    return "skewY({})".format(angle())


def matrix3d():
    value = seq([Random.number() for _ in range(16)])
    return "matrix3d({})".format(value)


def translate3d():
    value = seq([length_percentage(), length_percentage(), length()])
    return "translate3d({})".format(value)


def translate_z():
    return "translateZ({})".format(length())


def scale3d():
    value = seq([Random.number() for _ in range(3)])
    return "scale3d({})".format(value)


def scale_z():
    return "scaleZ({})".format(Random.number())


def rotate3d():
    values = [Random.number() for _ in range(3)]
    values.append(angle())
    return "rotate3d({})".format(seq(values))


def rotate_x():
    return "rotateX({})".format(angle())


def rotate_y():
    return "rotateY({})".format(angle())


def rotate_z():
    return "rotateZ({})".format(angle())


def perspective():
    return "perspective({})".format(length())


##################################
# Language
##################################
def lang():
    return Random.choice(
        ["ar", "af", "en", "am", "ar-SA", "bg", "bn", "cs", "cy", "da", "de-DE", "el-GR", "en-US", "es-ES", "eu",
         "fa", "fi", "fr-fR", "gd", "gu", "he", "hi", "hr", "hu", "hy", "id", "is", "it", "iu", "ja-JP", "jw", "ka",
         "kk", "kn", "ko", "ky", "lt", "mk", "mr", "nl", "no", "or", "pl", "pt-PT", "pt-BR", "ro", "ru", "sa", "sr",
         "si", "sl", "sq", "sv", "ta", "te", "tg", "th", "tl", "tr", "tt", "uk", "ur-IN", "ur-PK", "uz", "vi", "yi",
         "zh-CN", "zh-TW", "fr", "fr-CA"])


##################################
# Time
##################################
def clock_in_s():
    return str(Random.choice([0, 0.5, 1, 1.5, 2]))


def clock_in_ms():
    return str(Random.range(0, 3) * 100)


def clock():
    if Random.bool():
        return "{}s".format(clock_in_s())
    else:
        return "{}ms".format(clock_in_ms())


##################################
# Shapes
##################################
def fill_rule():
    return Random.choice(["nonzero", "evenodd"])


def border_radius():
    num = Random.range(1, 4)
    values = [length_percentage() for _ in range(num)]
    if Random.bool():
        values.append("/")
        num = Random.range(1, 4)
        values.extend([length_percentage() for _ in range(num)])
    return cat(values)


def shape_radius():
    if Random.bool():
        return length_percentage()
    else:
        return Random.choice(["closest-side", "farthest-side"])


def inset():
    num = Random.range(1, 4)
    values = [length_percentage() for _ in range(num)]
    if Random.bool():
        values.append("round {}".format(border_radius()))
    return "inset({})".format(cat(values))


def circle():
    values = []
    if Random.bool():
        values.append(shape_radius())
        if Random.bool():
            values.extend(["at", position()])
    return "circle({})".format(cat(values))


def ellipse():
    values = []
    if Random.bool():
        values.extend([shape_radius(), shape_radius()])
        if Random.bool():
            values.extend(["at", position()])
    return "ellipse({})".format(cat(values))


def polygon():
    values = []
    if Random.bool():
        values.append(fill_rule())
    num = Random.range(2, 5)
    for _ in range(num):
        values.append("{} {}".format(length_percentage(), length_percentage()))
    return "polygon({})".format(seq(values))


def path_shape():
    value = ""
    if Random.bool():
        value += fill_rule() + ","
    value += "'{}'".format(path())
    return "path({})".format(value)


##################################
# Fonts
##################################
def font():
    return Random.choice(["Arial", "Verdana", "serif", "sans-serif", "monospace"])


##################################
# DateTime
##################################
def date_time():
    return Random.choice([
        "1993-11-01", "1066-10-14", "0571-04-22", "0062-02-05",
        "1986-01-28T11:38:00.01", "0170-07-31T22:00:00"
    ])


##################################
# Charset
##################################
def charset():
    return Random.choice([
        "UTF-7", "UTF-8", "UTF-16", "UTF-32", "EUC-JP",
        "ISO-2022-JP", "iso-8859-1", "Big5", "US-ASCII"
    ])


##################################
# DOM Attribute Value
##################################
def auto_capitalize():
    return Random.choice(["none", "sentences", "words", "characters"])


def dir_():
    return Random.choice(["ltr", "rtl", "auto"])


def tab_index():
    c = Random.selector(3)
    if c == 0:
        return "-1"
    elif c == 1:
        return str(Random.range(0, 5))
    else:
        return Random.integer()


def drop_zone():
    return Random.choice(["copy", "move", "link"])


def coords():
    c = Random.selector(3)
    if c == 0:
        n = 4
    elif c == 1:
        n = 3
    else:
        n = Random.range(3, 5) * 2
    return seq([Random.integer() for _ in range(n)])


def shape():
    return Random.choice(["rect", "circle", "poly", "default"])


def target():
    return Random.choice(["_replace", "_self", "_parent", "_top", "_blank"])


def preload():
    return Random.choice(["none", "metadata", "auto"])


def track_kind():
    return Random.choice(["subtitles", "captions", "descriptions", "chapters", "metadata"])


def clear():
    return Random.choice(["none", "all", "both"])


def form_enc_type():
    return Random.choice(["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"])


def form_method():
    return Random.choice(["post", "get"])


def button_type():
    return Random.choice(["submit", "reset", "button"])


def align():
    return Random.choice(["left", "right", "center", "justify"])


def accept():
    return Random.choice([Random.string(), "audio/*", "video/*", "image/*"])


def caption_align():
    return Random.choice(["left", "top", "right", "bottom"])


def table_align():
    return Random.choice(["left", "right", "center", "justify", "char"])


def valign():
    return Random.choice(["baseline", "bottom", "middle", "top"])


def vtt_cue_align():
    return Random.choice(["start", "middle", "end", "left", "right"])


def input_mode():
    return Random.choice(["text", "decimal", "numeric", "tel", "search", "email", "url"])


def play_state():
    return Random.choice(["idle", "running", "paused", "finished"])


def animation_direction():
    return Random.choice(["normal", "reverse", "alternate", "alternate-reverse"])


def animation_easing():
    value = Random.choice(["linear", "ease", "ease-in", "ease-out", "ease-in-out", "cubic-bezier"])
    if value == "cubic-bezier":
        value += "({})".format(seq([Random.number() for _ in range(4)]))
    return value


def animation_fill_mode():
    return Random.choice(["forwards", "backwards", "both"])


# iframe, image, object
def object_align():
    return Random.choice(["left", "right", "middle", "top", "bottom"])


def scrolling():
    return Random.choice(["auto", "yes", "no"])


def vtt_region_scroll():
    return Random.choice(["", "up"])


def table_frame():
    return Random.choice(["void", "above", "below", "hsides", "vsides", "lhs", "rhs", "box", "border"])


def table_rules():
    return Random.choice(["none", "groups", "rows", "columns", "all"])


def wrap():
    return Random.choice(["soft", "hard", "off"])


def selection_direction():
    return Random.choice(["forward", "backward"])


def select_mode():
    return Random.choice(["select", "start", "end", "preserve"])


def numbering_type():
    return Random.choice(["a", "A", "i", "I", "1"])


def auto_complete():
    if Random.bool():
        return Random.choice(["on", "off"])
    else:
        return Random.choice([
            "name", "honorific-prefix", "given-name", "additional-name", "family-name", "honorific-suffix",
            "nickname", "email", "username", "new-password", "current-password", "one-time-code",
            "organization-title", "organization", "street-address", "address-line1", "address-line2",
            "address-line3", "address-level1", "address-level2", "address-level3", "address-level4", "country",
            "country-name", "postal-code", "cc-name", "cc-given-name", "cc-additional-name", "cc-family-name",
            "cc-number", "cc-exp", "cc-exp-month", "cc-exp-year", "cc-csc", "cc-type", "transaction-currency",
            "transaction-amount", "language", "bday", "bday-day", "bday-month", "bday-year", "sex", "tel",
            "tel-country-code", "tel-national", "tel-area-code", "tel-local", "tel-extension", "impp", "url",
            "photo"
        ])


def key_type():
    return Random.choice(["RSA", "DSA", "EC"])


# more images
def srcset():
    values = [image_url()]
    if Random.bool():
        values.append("{}w".format(Random.integer()))
    if Random.bool():
        values.append("{}x".format(Random.integer()))
    return cat(values)


def meta_scheme():
    return Random.choice(["NIST", "YYYY-MM-DD", "ISBN"])


def text_track_mode():
    return Random.choice(["disabled", "hidden", "showing"])


def vtt_cue_vertical():
    return Random.choice(["", "rl", "lr"])


def param_value_type():
    return Random.choice(["data", "ref", "object"])


def ulist_type():
    return Random.choice(["circle", "disc", "square"])


def link_as():
    return Random.choice([
            "audio", "document", "embed", "fetch", "font", "image",
            "object", "script", "style", "track", "video", "worker"
        ])


def table_scope():
    return Random.choice(["col", "row", "colgroup", "rowgroup"])


def menu_type():
    return Random.choice(["context", "toolbar"])


def regex():
    if Random.bool():
        return Random.string()
    else:
        return Random.choice(["^\\d+$", "^[a-zA-Z0-9]*$", ".*"])


def input_type():
    return Random.choice([
        "button", "checkbox", "color", "date", "datetime-local",
        "email", "hidden", "image", "month", "number", "password",
        "radio", "range", "reset", "search", "submit", "tel", "text",
        "time", "url", "week", "datetime", "foo"  # "file"
    ])


def menu_item_type():
    return Random.choice(["command", "checkbox", "radio"])


def marquee_behavior():
    return Random.choice(["scroll", "slide", "alternate"])


def marquee_direction():
    return Random.choice(["left", "right", "up", "down"])


def marquee_loop():
    if Random.bool():
        return "-1"
    else:
        return Random.integer()


def rel():
    return Random.choice([
        "alternate", "author", "bookmark", "external", "help",
        "license", "next", "nofollow", "noreferrer", "noopener",
        "prev", "search", "tag", "stylesheet"
    ])


def rev():
    return Random.choice([
        "alternate", "stylesheet", "start", "next", "prev",
        "contents", "index", "glossary", "copyright", "chapter",
        "section", "subsection", "appendix", "help", "bookmark",
        "stylesheet"
    ])


def font_weight():
    if Random.bool():
        return Random.choice(["normal", "bold", "bolder", "lighter"])
    else:
        return Random.integer()


def font_stretch_value():
    if Random.bool():
        return Random.choice(
            ["normal", "ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "semi-expanded",
             "expanded", "extra-expanded", "ultra-expanded"])
    else:
        return percentage()


def font_stretch():
    s = font_stretch_value()
    if Random.bool():
        s += " " + font_stretch_value()
    return s


def font_variant():
    return Random.choice(["normal", "small-caps"])


def font_feature_settings():
    def single():
        values = ["'{}'".format(
            Random.choice(["smcp", "c2sc", "zero", "hist", "liga", "tnum", "frac", "swsh", "ss07", "dlig", "vert",
                           "hwid", "twid", "qwid", "kern", "onum"])
        )]
        if Random.bool():
            if Random.bool():
                values.append(Random.choice(["on", "off"]))
            else:
                values.append(Random.integer())
        return cat(values)
    num = Random.range(1, 2)
    return seq([single() for _ in range(num)])


def unicode_range():
    return Random.choice(["U+0-7F", "U+0590-05FF", "U+2010-2011", "U+21E7", "U+25A0", "U+25E6", "U+FFFD"])


def media_query():
    media_type = Random.choice(["all", "print", "screen"])
    if Random.bool():
        return media_type

    media_feature = Random.choice(["min-width", "max-width", "min-height", "max-height", "orientation"])
    if media_feature == "orientation":
        media_feature_value = Random.choice(["portrait", "landscape"])
    else:
        media_feature_value = "{}px".format(Random.integer())
    return "{} and ({}:{})".format(media_type, media_feature, media_feature_value)


def keyframe_name():
    return "{}%".format(Random.choice([0, 20, 40, 60, 80, 100]))


def css_type():
    return "text/css"


def media_type():
    return Random.choice(["image/jpeg", "image/png", "video/mp4", "audio/mp3"])


def mime_type():
    return Random.choice(["image/jpeg", "image/png", "video/mp4", "audio/mp3", "text/html", "text/css"])


def image_type():
    return Random.choice(["image/png", "image/jpeg", "image/webp"])