from .check import is_descriptor

class ObjectType(object):
    """ Represents a business object.

    """
    #: Optional attribute order overriding
    __order__ = []

    #: Current values
    _values = None

    @classmethod
    def get_descriptors(cls):
        """ Returns a list of ordered (``index``, ``descriptor``) tuples for
            this ObjectType.

            :rtype: list

        """
        if not hasattr(cls, '_descriptors'):
            cls._descriptors = []
            cls._descriptors_index = {}

            # Build unsorted dictionary
            _unsorted = {}
            for index, descriptor in cls.__dict__.iteritems():
                if is_descriptor(descriptor):
                    _unsorted[index] = descriptor

            for index in cls.__order__:
                cls._descriptors.append((index, _unsorted.pop(index)))
                cls._descriptors_index[index] = len(cls._descriptors) - 1

            for index, descriptor in _unsorted.iteritems():
                cls._descriptors.append((index, descriptor))
                cls._descriptors_index[index] = len(cls._descriptors) - 1

        return cls._descriptors

    @classmethod
    def get_descriptor(cls, index):
        """ Returns descriptor for attribute named ``index``.

            :param index: The attribute name.
            :type index: str
            :rtype: serge.descriptor.descriptor.Descriptor
        """

        descriptors = cls.get_descriptors()

        if not index in cls._descriptors_index:
            raise AttributeError('No descriptor for attribute %r.' % index)

        # why use __dict__ here ?
        return descriptors[cls._descriptors_index[index]][1]

    @classmethod
    def has_descriptor(cls, name):
        """ Checks is an attribute ``name`` has a descriptor.

            :type name: str
            :rtype: bool
        """
        # ensure descriptors are indexed
        cls.get_descriptors()

        # search the index
        return name in cls._descriptors_index


    def get(self, name):
        """Gets the value of attribute `name`.

        """

        try:
            return self.__get(name)
        except KeyError, e:
            self.__set(name, self.__class__.get_descriptor(name).default)
            return self.__get(name)


    def set(self, name, value):
        """Sets the value of attribute `name` to `value`.

        """

        current_value = self.get(name)
        new_value = self.__class__.get_descriptor(name).normalize(value)

        if new_value != current_value:
            self._values[name] = new_value


    def __init__(self, values=None):
        self._values = {}

        if values is not None:
            for k, v in values.iteritems():
                self.set(k, v)


    def __setattr__(self, index, value):
        #: TODO fixme
        return super(ObjectType, self).__setattr__(index, value)

        raise AttributeError('No descriptor for attribute %r.' % index)


    def __iter__(self):
        for index, descriptor in self.__class__.get_descriptors():
            yield index, descriptor


    def __repr__(self):
        """Returns a fancy representation of this instance, giving attributes'
        names, types and values. Mostly usefull for debugging purposes.

        """
        classname = self.__class__.__name__

        r = ['<%s>' % classname]
        for index, descriptor in self.__class__.get_descriptors():
            r.append('  %s(%s): %r' % (index, descriptor.__class__.__name__, getattr(self, index)))
        r += ['</%s>' % classname]

        return '\n'.join(r)


    def __get(self, name):
        if not self.__class__.has_descriptor(name):
            raise AttributeError, 'No descriptor for attribute %r.' % name

        return self._values[name]


    def __set(self, name, value):
        if not self.__class__.has_descriptor(name):
            raise AttributeError, 'No descriptor for attribute %r.' % name

        self._values[name] = value
