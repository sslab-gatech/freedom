class Ret:
    name = "Object"

    def __init__(self):
        super().__init__()
        self.obj = None

    def generate(self, context):
        self.obj = context.create_object(self.name)

    def merge_fix(self, context):
        self.obj.id = None
        context.add_object(self.obj)

    def __str__(self):
        return self.obj.id
