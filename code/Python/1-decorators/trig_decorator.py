import math

pi_ = math.pi
values = (0, pi_/8, pi_/6, pi_/4, pi_/3, pi_/2, pi_)
str_values = []

for value in values:
    # Avoid division by zero error
    if value > 0.001 or value < -0.001:
        str_val = 'pi/' + str(pi_ / value)
    else:
        str_val = '0'

    str_values.append(str_val)


def find_values(func):
    def wrapper(*args, **kwargs):
        print()
        print('*****************************************')
        print('\t\tINPUT')
        print('*****************************************')
        print(args)
        print()
        print('*****************************************')
        print('\t\tRESULTS')
        print('*****************************************')
        func(*args, **kwargs)
    return wrapper


@find_values
def trig_func_comparison(vals, str_values):
    i = 0
    for val in vals:
        print(f'sin({str_values[i]}) = {math.sin(val)}')
        print(f'cos({str_values[i]}) = {math.cos(val)}')
        print(f'tan({str_values[i]}) = {math.tan(val)}')
        print()
        i += 1

# This is what is happening behind the scenes
# find_values(trig_func_comparison)(values, str_values)


trig_func_comparison(values, str_values)
