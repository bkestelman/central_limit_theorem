import itertools
import numpy as np
from matplotlib import pyplot as plt

class IntegerRandomVariable:
    """
    Working with integer random variables avoids floating point precision issues
    When plotting, the values can be shifted and scaled as needed to achieve non-integer values
    """
    def __init__(self, values, pmf):
        """
        @param values: array of integer values the random variable can take
        @param pmf: probability distribution over values
        """
        self.values = values
        self.pmf = pmf
        if isinstance(self.values, list):
            self.values = np.array(self.values)
        if isinstance(self.pmf, list):
            self.pmf = np.array(self.pmf)
        #TODO: check that pmf is a valid probability distribution?
        #TODO: check that values are ints
    def plot(self, a=None, b=None):
        """Plot values and pmf as bar graph"""
        values = self.values
        if a is not None and b is not None:
            values = np.linspace(a, b, len(self.values))
        return plt.bar(
                values, 
                self.pmf, 
                width=(np.max(values) - np.min(values)) / len(values)
        )
    def __add__(self, other):
        """Add two IntegerRandomVariables"""
        val_combos = list(itertools.product(self.values, other.values)) # get all combinations (cartesian product) of values of the two random variables
        #print('val combos', val_combos)
        #new_vals = [np.sum([a, b], dtype=np.float64) for a, b in val_combos]
        new_vals = list(map(sum, val_combos))
        new_vals = np.array(new_vals)
        #new_vals = np.unique(new_vals.round(decimals=5)) # round sums to allow some floating point precision tolerance, then keep unique values
        new_vals = np.unique(new_vals)
        #TODO: the number 10 above was chosen arbitrarily and should be set elsewhere so it is not a "magic number"
        new_vals = np.sort(new_vals)
        #new_vals = list(set(new_vals)) # remove duplicates
        #new_vals.sort()

        #val_combos = np.array(np.meshgrid(self.values, other.values)).T.reshape(-1, 2)
        #print('val combos', val_combos)
        #new_vals = val_combos.sum(axis=1)
        #print('new vals', new_vals)
        #new_vals = np.sort(np.unique(new_vals))
        #print('new vals', new_vals)

        sum_pmf = np.convolve(self.pmf, other.pmf)
        #print('convolution', sum_pmf)
        result = IntegerRandomVariable(new_vals, sum_pmf)
        return result
#    @staticmethod
#    def from_pdf(pdf, a, b, n_values):
#        """
#        Constructs a IntegerRandomVariable by discretizing a continuous pdf.
#        @param pdf: continuous pdf. Should accept a numpy array of x values and return a numpy array of probabilities
#        @param a, b: the closed interval on which the IntegerRandomVariable has non-zero probability. a < b
#        @param n_classes: number of values in the interval to use. n >= 2, since the values will always include a and b
#        """
#        if a > b:
#            raise InvalidIntervalError(f'Interval left-endpoint a ({a}) must be smaller than right-endpoing b ({b})')
#        #TODO: exception if n < 2 (unless a=b?)
#        values = np.linspace(a, b, n_values)
#        pmf = pdf(values) / pdf(values).sum()
#        return IntegerRandomVariable(values, pmf)

#TODO: create tests to check if pmf is valid after creation or addition
