import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from Month_Number_Days import Month_Days

class Scrap_Bot:

    def __init__(self, PATH, Ticker, Year):
        self.PATH = PATH
        self.Ticker = Ticker
        self.Year = Year


    def Create_Chrome_Instance(self):

        Ticker_PATH = os.path.normpath(self.PATH + r'\\' + self.Ticker)

        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': Ticker_PATH}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        return driver


    def Scrap(self):

        driver = Scrap_Bot.Create_Chrome_Instance(self)

        try:
            for year in range(len(self.Year)):

                print('Year to Scrap: ', self.Year[year])

                Link = "https://www.ilboursa.com/marches/download.aspx?s=" + str(self.Ticker)
                driver.get(Link)
                sleep(3)

                datefield_from = driver.find_element_by_id('ctl00_BodyABC_txtFrom')
                datefield_to   = driver.find_element_by_id('ctl00_BodyABC_txtTo')
                month_from = -2
                month_to   = 0
                sleep(3)

                # if driver.find_element_by_id('hideModalPopupViaClientButton').is_displayed():
                #     driver.find_element_by_id('hideModalPopupViaClientButton').click()

                for row in range(4):
                    # if driver.find_element_by_id('hideModalPopupViaClientButton').is_displayed():
                    #     driver.find_element_by_id('hideModalPopupViaClientButton').click()


                    month_from += 3
                    month_to   += 3

                    md = Month_Days(self.Year[year], month_to)
                    month_to_nbr_days = md.GetDays()

                    date_from = '01/' + str(str(month_from) + r'/') + str(self.Year[year])
                    date_to   = str(str(month_to_nbr_days) + r'/') + str(str(month_to) + r'/')   + str(self.Year[year])


                    ActionChains(driver).move_to_element(datefield_from).click().click().click().send_keys(date_from).perform()
                    sleep(1)
                    ActionChains(driver).move_to_element(datefield_to).click().click().click().send_keys(date_to).perform()
                    sleep(1)
                    ActionChains(driver).move_to_element(datefield_from).click().click().click().send_keys(date_from).perform()
                    sleep(1)
                    ActionChains(driver).move_to_element(datefield_to).click().click().click().send_keys(date_to).perform()
                    sleep(1)
                    driver.find_element_by_id("ctl00_BodyABC_Button1").click()

                    sleep(2)
                sleep(2)
            print('Finished Scrapping Successfully...')
        except:
            print('Unsuccessful Finish...')

        driver.quit()

