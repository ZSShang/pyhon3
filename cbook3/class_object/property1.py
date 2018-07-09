
class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can`t delete attribute')


if __name__ == '__main__':
    a = Person('miclefeng')
    print(a.first_name)
    a.first_name = 'striveftf'
    print(a.first_name)
    del a.first_name