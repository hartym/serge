from .base import BaseDescriptor

class ObjectDescriptor(BaseDescriptor):
    def __init__(self, type, **kwargs):
        self.type = type
        super(ObjectDescriptor, self).__init__(None, **kwargs)

    # Redefine the default property to generate instances of our type.
    default = property(lambda self: self.type())

