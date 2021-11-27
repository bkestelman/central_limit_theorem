import copy
import numpy as np
from random_variable import IntegerRandomVariable
from matplotlib import pyplot as plt

def main():
    # Create a uniform discrete random variable
    a, b = -1, 1
    n_values = 4 
    uniform_rv = create_uniform_rv(n_values)

    uniform_rv.plot()
    uniform_rv.plot(a, b)
    plt.show()

#    # Create a Gaussian discrete random variable from the continuous pdf
#    def gaussian_pdf(x, mu=0, sigma=1):
#        return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) / sigma)**2 / 2)
#
#    a, b = -2, 2
#    n_values = 20
#    gaussian_rv = IntegerRandomVariable.from_pdf(gaussian_pdf, a, b, n_values)
#
#    gaussian_rv.plot()
#    plt.show()

    # Add two uniform random variables
    uniform_rv2 = copy.deepcopy(uniform_rv)
    sum_uniforms = uniform_rv + uniform_rv2
    sum_uniforms.plot()
    plt.show()

    # Add lots of uniform random variables
    iterations = 10
    sum_uniforms = uniform_rv
    for i in range(iterations):
        plt.cla()
        sum_uniforms.plot()
        plt.pause(1)
        sum_uniforms = sum_uniforms + uniform_rv
    plt.show()

def create_uniform_rv(n_values):
    values = np.arange(n_values)
    pmf = np.repeat(1 / n_values, n_values)
    uniform_rv = IntegerRandomVariable(values, pmf)
    return uniform_rv

if __name__ == '__main__':
    main()
