import marshmallow as mm


class Slice(mm.fields.Field):
    """Slice is a :class:'Field' type that supports a range or slice argument for
    selecting some subset of a larger dataset.  The syntax is identical to
    numpy slicing. Examples: "10:20", "40", ":30", "10:2:40"

    :param kwargs: the same as any :class:'Field' receives"""

    def __init__(self, **kwargs):
        kwargs['metadata'] = kwargs.get(
            'metadata', {'description': 'slice the dataset'})
        kwargs['default'] = kwargs.get('default', slice(None))
        super(Slice, self).__init__( **kwargs)

    def _deserialize(self, value, attr, obj):
        try:
            args = tuple([int(c) if c else None for c in value.split(':')])
            return slice(*args)
        except:
            raise mm.ValidationError(
                '{} is not a properly formatted slice'.format(value))
