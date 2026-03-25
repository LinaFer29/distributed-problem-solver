from typing import List
from .i_data_generator import IDataGenerator
from scipy.stats import norm
import numpy as np

class NormalGenerator(IDataGenerator):
  
  def generate_numbers(self, quantity, lower, upper) -> List:
    
    print("I'm a normal generator")
    mu = (int(lower)+ int(upper))/2   # Media
    sigma = 0.5  # Standard deviation

    randoms = norm.rvs(loc=mu, scale=sigma, size=int(quantity))
    integer_randoms = np.round(randoms).astype(int)
    positive_int_randoms = np.abs(integer_randoms)
    randoms_list = positive_int_randoms.tolist()

    #[141, 393, 268, 263, 395, 310, 203, 285, 183, 387]
    
    return randoms_list
  