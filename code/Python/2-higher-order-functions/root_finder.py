import sys


def newton_raphson_solve(num, func_eval, der_eval, epsilon):
    if num > 0:
        low = 0
        high = num
    else:
        high = 0
        low = num

    guess = (low + high) / 2
    num_iterations = 0

    f_x = func_eval(guess) - num
    f_prime_x = der_eval(guess)

    while abs(f_x) >= epsilon and num_iterations < 200:
        guess = guess - f_x / f_prime_x
        f_x = func_eval(guess) - num
        f_prime_x = der_eval(guess)
        num_iterations += 1

    return((guess, num_iterations))


def create_function_evals(root):
    # returns a tuple consisting of ttwo lambda expressions
    return (lambda guess: guess**root, lambda guess: root * guess ** (root - 1))


def root_solver(root, num, epsilon):
    '''
    root can be any number greater than or equal to 1.
    num can be any number.
    returns a number x such that abs(x ** root - num) is within epsilon
    '''

    if root < 0 and num > 0:
        return (None, root)

    func_evals = create_function_evals(root)

    return newton_raphson_solve(num, func_evals[0], func_evals[1], epsilon)


if len(sys.argv) == 4:
    root = float(sys.argv[1])
    number = float(sys.argv[2])
    epsilon = float(sys.argv[3])

    answer, num_iterations = (root_solver(root, number, epsilon))

    if answer != None:
        print(f'The answer is {answer}')
        print(f'It took {num_iterations} iterations\n')
    else:
        print('No answer could be determined.\n')

else:
    print('Incorrect number of arguments.  Exactly three must be provided.\n')
