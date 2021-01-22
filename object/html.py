import docs
from object import Element
from utils.random import Random


class HTMLElement(Element):
    def __init__(self, name):
        super().__init__(name)
        self.tag = docs.html_tag_from_element(name)

    @staticmethod
    def create(name):
        if name == "HTMLSlotElement":
            return HTMLSlotElement(name)
        elif name == "HTMLMapElement":
            return HTMLMapElement(name)
        else:
            return HTMLElement(name)

    def generate_child(self, child_name):
        child = HTMLElement.create(child_name)
        self.add_child(child)
        return child

    def generate_text(self):
        if docs.is_html_text_element(self.name) and Random.selector(5) == 0:
            self.last_text = Random.string()
        if (self.parent is None or docs.is_html_text_element(self.parent.name)) and \
                Random.selector(5) == 0:
            self.ahead_text = Random.string()

    def mutate_text(self) -> bool:
        if Random.bool():
            if docs.is_html_text_element(self.name):
                self.last_text = Random.string()
                return True
            return False
        else:
            if self.parent is None or docs.is_html_text_element(self.parent.name):
                self.ahead_text = Random.string()
                return True
            return False

    def insert_child(self):
        if docs.is_html_empty_element(self.name) or docs.is_html_raw_text_element(self.name):
            return None

        children = None
        if self.name in docs.html_child_elements:
            if Random.selector(10) > 0:
                children = docs.html_child_elements[self.name]

        if children is None:
            if Random.selector(5) > 0:
                children = docs.html_general_child_elements
            else:
                children = docs.html_other_child_elements

        if len(children) == 0:
            return None

        child = Random.choice(children)        
        return self.generate_child(child)


class HTMLSlotElement(HTMLElement):
    @property
    def additional_label(self):
        return " name=\"{}\"".format(self.id)


class HTMLMapElement(HTMLElement):
    @property
    def additional_label(self):
        return " name=\"{}\"".format(self.id)
