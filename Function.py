import pandas as pd
import numpy as py

def pywhich(list, condition):
    result = np.where(np.array(list)==condition)[0].tolist() # may also change == to other relation, like < > <= >=
    
    return result
