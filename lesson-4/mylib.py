def payroll_calculation(hours, rate):
    try:
        return int(hours)*int(rate)
    except ValueError:
        print('Incorrect hours or rate value')
        return 0
