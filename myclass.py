class MyClass:
    def __init__(self):
        self._my_attribute = 0

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value


my_object = MyClass()

my_object.my_attribute = 3
print(my_object.my_attribute)
