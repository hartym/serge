from serge.type.collection import CollectionType

from .base   import BaseDescriptor
from .object import ObjectDescriptor

class CollectionDescriptor(BaseDescriptor):
    def __init__(self, type, **kwargs):
        self.type = type
        super(CollectionDescriptor, self).__init__(None, **kwargs)

    # Redefine the default property to generate instances of our type.
    default = property(lambda self: CollectionType(ObjectDescriptor(self.type)))
