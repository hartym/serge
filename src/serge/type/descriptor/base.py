class BaseDescriptor(object):
    """ Base class for type attribute descriptors.

        http://docs.python.org/reference/datamodel.html#descriptors

    """

    def __init__(self, default=None, **kwargs):
        self._default = default
        self.options = {
                'required': bool(kwargs.pop('required', True)),
            }
        self.options.update(self.setup(**kwargs))
        self.parent = None

    #: In descriptors for the most simple types, the default value is always the
    #: same, and is stored in _default.
    default = property(lambda self: self._default)

    def setup(self):
        return {}

    def __get__(self, parent, parent_type=None):
        if parent:
            return parent.get(self.find_index_in(parent))
        else:
            return parent_type, self

    def __set__(self, parent_type, value):
        parent_type.set(self.find_index_in(parent_type), value)

    def find_index_in(self, parent_type):
        if hasattr(self, '_index'):
            return self._index

        for index, descriptor in parent_type:
            if descriptor is self:
                self._index = index
                return self._index

        raise Exception('Logic error, type instance not found in container type.')

    def normalize(self, value):
        if self.options['required'] and value is None:
            raise Exception('Required.')

        return value

