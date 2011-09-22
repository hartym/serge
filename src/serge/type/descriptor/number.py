from decimal import Decimal

from .base   import BaseDescriptor

class NumberDescriptor(BaseDescriptor):
    number_type = None

    def setup(self, min=None, max=None):
        options = dict()

        if min is not None:
            options['min'] = self.number_type(min)
        if max is not None:
            options['max'] = self.number_type(max)

        return options

    def normalize(self, value):
        value = super(NumberDescriptor, self).normalize(value)
        value = self.number_type(value)

        if 'min' in self.options:
            if value < self.options['min']:
                raise Exception('Minimum value deceeded.')

        if 'max' in self.options:
            if value > self.options['max']:
                raise Exception('Maximum value exceeded.')

        return value

class IntegerDescriptor(BaseDescriptor):
    number_type = int

class DecimalDescriptor(BaseDescriptor):
    number_type = Decimal

class FloatDescriptor(BaseDescriptor):
    number_type = float

