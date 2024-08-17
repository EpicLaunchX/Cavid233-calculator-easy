def set_value(value, type):
    if not isinstance(value, type):
            raise TypeError(f'Expecting an {type}, got {type(value)}.')
    else:
        return value