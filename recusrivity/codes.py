def find_maximum(numbers_list):
    if len(numbers_list) <= 2:
        return max(numbers_list)
    else:
        return max(find_maximum(numbers_list[0:len(numbers_list) // 2]), find_maximum(numbers_list[len(numbers_list) // 2:]))

def add_numbers(numbers_list):
    if len(numbers_list) <= 2:
        r = 0
        match len(numbers_list):
            case 2:
                r = numbers_list[0] + numbers_list[1]
            case 1:
                r = numbers_list[0]
        return r
    else:
        return add_numbers(numbers_list[0:len(numbers_list) // 2]) + add_numbers(numbers_list[len(numbers_list) // 2:])