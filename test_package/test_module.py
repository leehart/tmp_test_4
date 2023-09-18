
class test_class():
    """This is the test_class docstring"""

    class_var = "class variable"

    def __init__(self, instance_var=None):
        self.instance_var = instance_var

    def test_function(self, number):
        """This is the test_function docstring"""
        return number + 1
    
    @property
    def test_property(self):
        """This is the test_property docstring"""
        return self.instance_var
    
    def test_instance_method(self):
        """This is the test_instance_method docstring"""
        return 'Instance method', self
    @classmethod
    def test_class_method(a):
        """This is the test_class_method docstring"""
        return 'Class method', a
    @staticmethod
    def test_static_method():
        """This is the test_static_method docstring"""
        return 'Static method'