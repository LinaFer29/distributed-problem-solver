from typing import List
from .i_data_generator import IDataGenerator
from scipy.stats import uniform
import numpy as np


class UniformGenerator(IDataGenerator):

  def generate_numbers(self, quantity, lower, upper) -> List:
    print("I'm a Uniformal generator")
    long_range = int(upper) - int(lower)
    randoms = uniform.rvs(loc=int(lower) , scale = long_range, size=int(quantity))
    integer_randoms = np.round(randoms).astype(int)
    positive_int_randoms = np.abs(integer_randoms)
    randoms_list = positive_int_randoms.tolist()

    #[141, 393, 268, 263, 395, 310, 203, 285, 183, 387]

    return randoms_list
