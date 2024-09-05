def get_data_type(value):
    return f"The data type of {value} is {type(value).__name__}"

# Test cases
print(get_data_type(10))           # Output: The data type of 10 is int
print(get_data_type(10.5))         # Output: The data type of 10.5 is float
print(get_data_type("Hello"))      # Output: The data type of Hello is str
print(get_data_type([1, 2, 3]))    # Output: The data type of [1, 2, 3] is list
print(get_data_type((1, 2, 3)))    # Output: The data type of (1, 2, 3) is tuple
print(get_data_type({"key": "value"}))  # Output: The data type of {'key': 'value'} is dict
