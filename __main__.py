# Sometimes companies are no longer listed like this company ticker 'BS'.
# TN_Listed_Stock_Companies = ['AB', 'ADWYA', 'AETEC', 'AL', 'AMS', 'ARTES', 'ASSAD', 'ATB', 'ATL', 'BH', 'BIAT', 'BNA',
#                              'BT', 'CC', 'CELL', 'CITY', 'CREAL', 'DH', 'ECYCL', 'GIF', 'ICF', 'LNDOR', 'LSTR', 'MGR',
#                              'MNP', 'MPBS', 'NAKL', 'NBL', 'OTH', 'PLAST', 'POULA', 'SAH', 'SAMAA', 'SERVI', 'SFBT',
#                              'SIAM', 'SMG', 'SOKNA', 'SOMOC', 'SOPAT', 'SOTE', 'STAR', 'STB', 'STPAP', 'STPIL',
#                              'STVR', 'TAIR', 'TGH', 'TLNET', 'TLS', 'TPR', 'TRE', 'UADH', 'UIB', 'UMED']

import Scrap_Files as SF
import os

def main():

    PATH = os.path.normpath(r"C:\Users\Almighty\PycharmProjects\Scrap_Tunisian_Stock_Exchange\Data")
    Ticker_Symbol = ['TAIR', 'ADWYA']
    Ticker_Years  = [2019, 2020]

    data = SF.Get_Data(PATH, Ticker_Symbol, Ticker_Years)
    data.head(20)

if __name__ == "__main__":
    main()

# https: // stackoverflow.com / questions / 19198166 / whats - the - difference - between - a - module - and -a - library - in -python