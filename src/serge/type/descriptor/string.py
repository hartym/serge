from .base import BaseDescriptor

class StringDescriptor(BaseDescriptor):
    def setup(self, max_length=None):
        return {
            'max_length': max_length
            }

    def normalize(self, value):
        value = super(StringDescriptor, self).normalize(value)
        value = unicode(value)

        if self.options['max_length'] is not None and len(value) > self.options['max_length']:
            raise Exception('Max length exceeded.')

        return value
