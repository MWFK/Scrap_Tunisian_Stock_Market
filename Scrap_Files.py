import os
import shutil
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Scrap_Function import Scrap_Bot #import Scrap_Function


def Get_Data(PATH, Ticker_Symbol, Ticker_Years):

    for ticker_name in range(len(Ticker_Symbol)):

        print('Ticker to Scrap: ', str(Ticker_Symbol[ticker_name]))

        # Ticker_PATH =  PATH + r'\\' + Ticker_Symbol # we need to format it from string to path
        Ticker_PATH   =  os.path.normpath(PATH + r'\\' + Ticker_Symbol[ticker_name])

        # Create a folder for Data Ticker by Overwriting previous Directories
        print('Overwrite Existing files')
        if os.path.exists(Ticker_PATH):
            shutil.rmtree(Ticker_PATH)
        os.makedirs(Ticker_PATH)

        '''
        This function scraps a single Ticker at a time for the specified range of years
        and download it to a specific folder
        '''
        SB = Scrap_Bot(PATH, Ticker_Symbol[ticker_name], Ticker_Years)
        SB.Scrap()

        # Count the number of downloaded files
        path, dirs, files = next(os.walk(Ticker_PATH))
        file_count = len(files)

        # Join all data files into one dataset
        data = pd.DataFrame()
        # Add the first file to the dataframe, because is does not have the same name pattern
        Ticker_PATH_File = os.path.normpath(Ticker_PATH + r'\cotations_' + Ticker_Symbol[ticker_name] + '.csv')
        df_file          = pd.read_csv(Ticker_PATH_File, sep=';')
        data             = data.append(df_file, ignore_index=True)

        # Add the rest of the files
        for file in range(1, file_count, 1):
            Ticker_PATH_File = os.path.normpath( Ticker_PATH + r'\cotations_' + Ticker_Symbol[ticker_name] + ' (' + str(file) + str(').csv') )
            df_file = pd.read_csv(Ticker_PATH_File, sep=';')
            data = data.append(df_file, ignore_index=True)

        Ticker_PATH_Export = os.path.normpath(Ticker_PATH + r'\\' + Ticker_Symbol[ticker_name] +'.csv')
        data.to_csv(Ticker_PATH_Export, index=False, sep=';')
        print(Ticker_Symbol[ticker_name], ' Data Exported Successfully!')

    return data

