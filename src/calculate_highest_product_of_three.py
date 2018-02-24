def calculate_highest_product_of_three(array):
    # check the array type and length
    if is_list(array) and is_valid_length(array):
        sorted_list = sorted(array)

        # The highest product can be reached in one of two possible cases:
        # 1. As a product of 3 biggest integers (the end of the sorted list)
        # 2. As a product of 2 smallest integers (the begining of the sorted list) and 1 biggest integer
        product_first = sorted_list[0] * sorted_list[1] * sorted_list[-1]
        product_second = sorted_list[-1] * sorted_list[-2] * sorted_list[-3]

        return max(product_first, product_second)
    else:
        raise TypeError("Expected type: {0}. Actual type: {1}".format(type(list()), type(array)))


def is_list(array):
    if array is None or not isinstance(array, list):
        return False
    else:
        for item in array:
            if not isinstance(item, int):
                raise TypeError("Expected argument in list is {0}. Actual - {1}".format(type(int()), type(item)))
        return True


def is_valid_length(array, length=3):
    if len(array) >= length:
        return True
    else:
        raise ValueError("Length is too short. Please, input list of length, at least, {0}".format(length))
