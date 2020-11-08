class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    # getter
    @property
    def description(self):
        return self._description 

    # setter
    # _ means that the attribute is protected
    @description.setter
    def description(self, value):
        self._description = value

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

