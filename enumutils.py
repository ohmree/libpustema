from enum import Enum
from random import choice

class Methods(Enum):
    NN = 0
    NV = 1
    VV = 2
    NC = 3
    
class Types(Enum):
    "Types of words that can occur in dictionaries"
    NOUN = 0
    VERB = 1
    CUSS = 2