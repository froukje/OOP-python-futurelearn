class MyClass():
    def __init__(self):
        self.my_attribute = 0

    def get_my_attribute(self):
        return self.my_attribute

    def set_my_attribute(self, value):
        self.my_attribute = value    

my_object = MyClass()

my_object.set_my_attribute(1)
print(my_object.get_my_attribute())

# Alternativly
class MyClass():
    def __init__(self):
        self._my_attribute = 0

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value

my_object = MyClass()

