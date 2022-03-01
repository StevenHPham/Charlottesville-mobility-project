from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


walkScoreArray = []

roseHillStreets = []
starHillStreets = []

with open("/Users/stevenpham/PycharmProjects/Cmp/roseHill.txt") as fp:
    roseHillStreets.extend(word.strip() for word in fp.readlines())



def getDict(arr):
    """
    :param arr: Takes in an array of all streets in neighborhood
    :return: return a keys only dictionary
    """
    dictionary = {}
    dictionary.fromkeys(arr)
    for i in arr:
        dictionary[i] = None
    return dictionary

def PrintString(s):
    myString = ""
    myString = str(source)[36:len(myString)-4]
    return myString


#Create a driver to automate Safari Access
driver = webdriver.Safari()

#Open the page
driver.get("https://www.walkscore.com")


#Type the name of the street in the address box
driver.find_element(by=By.XPATH, value="//*[@id='gs-street']").send_keys("monticello ave" + " Charlottesville ")

#Hit enter
driver.find_element(by=By.XPATH, value="//*[@id='gs-street']").send_keys(Keys.RETURN)




try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='address-header']/div[4]/div[1]/div[1]/div/img"))
    )
finally:
    #driver.maximize_window()
    aboutLink = driver.find_element(by=By.XPATH, value="//*[@id='address-header']/div[4]/div[1]/div[1]/div/img")
    source = aboutLink.get_attribute('src')
    walkScoreArray.append(PrintString(source))



print(walkScoreArray)
