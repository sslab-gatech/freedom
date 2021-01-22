import docs
from object import Object
from object.html import HTMLElement
from object.svg import SVGElement
from object.function import Function, EventHandler


dummy = Object("Dummy", "dummy")


def create_function():
    return Function()


def create_event_handler():
    return EventHandler()


def create_object(name):
    if name in docs.svg_elements:
        return SVGElement.create(name)
    elif name in docs.html_elements:
        return HTMLElement.create(name)
    elif name == "Function":
        return Function()
    elif name == "EventHandler":
        return EventHandler()
    elif name == "Dummy":
        return dummy
    else:
        return Object(name)
