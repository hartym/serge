# local imports
from .object import ObjectType

class CollectionType(ObjectType, list):
    """ Represents a collection of business objects, each one being described
        by ``descriptor``.

        It extends :class:`ObjectType` but also :class:`list` to make available
        the standard list manipulation interface.


        The object itselfs describe a kind of collection, and its constraints
        (item count, type check ...).

        :param descriptor: Descriptor used to constraint each element.
        :param values: Initial value list.
        :type values: Iterable or None

    """

    def __init__(self, descriptor, values=None):
        """ Constructor

        """
        self.descriptor = descriptor

        list.__init__(self)
        ObjectType.__init__(self, values)

        if values is not None:
            self.extend(values)

    def append(self, x):
        return list.append(self, self.descriptor.normalize(x))

    def extend(self, L):
        return list.extend(self, [self.descriptor.normalize(i) for i in L])

    def insert(self, i, x):
        return list.insert(self, i, self.descriptor.normalize(x))

    def get(self, i):
        return self[i]

    def __iter__(self):
        for i in range(len(self)):
            yield i, self.get(i)

    def __repr__(self):
        return '<%s>%s</%s>' % (self.__class__.__name__, list.__repr__(self), self.__class__.__name__)

