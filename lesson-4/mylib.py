def payroll_calculation(hours, rate):
    try:
        return int(hours) * int(rate)
    except ValueError:
        print('Incorrect hours or rate value')
        return 0


def max_numbers_list(number_list):
    prev = None
    for number in number_list:
        if prev is not None:
            if number > prev:
                prev = number
                yield number
        prev = number


def sum_of_two(rev_element, element):
    return rev_element + element
