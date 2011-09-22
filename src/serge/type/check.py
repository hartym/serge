"""
Type check helpers.

"""

def is_unicode(x):
    return isinstance(x, unicode) or hasattr(x, '__unicode__')

def is_numeric(x):
    import decimal
    return isinstance(x, int) or isinstance(x, float) or isinstance(x, decimal.Decimal)

def is_descriptor(x):
    return hasattr(x, 'normalize')

