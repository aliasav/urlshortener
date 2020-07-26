import random
import string

def hashing(input_str):
    # hash the input string and return the out put hash
    N = 10
    res = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k = N))
    return res

