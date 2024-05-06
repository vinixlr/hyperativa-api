def has_empty_or_null_value(dictionary):
    return any(value == '' or value is None for value in dictionary.values())