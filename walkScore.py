from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


walkScoreArray = []

#Create an empty list
roseHillStreets = []
starHillStreets = []


#Get the streets name from file
with open("/Users/stevenpham/PycharmProjects/Cmp/roseHill.txt") as fp:
    roseHillStreets.extend(word.strip() for word in fp.readlines())

with open("/Users/stevenpham/PycharmProjects/Cmp/starHill.txt") as fp2:
    starHillStreets.extend(word.strip() for word in fp2.readlines())




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
    myString = str(s)[36:len(s)-4]
    return myString







def startUp(arr):

    dictionary = getDict(arr)

    #Create a driver to automate Safari Access
    driver = webdriver.Safari()

    for word in arr:
        #Open the page
        driver.get("https://www.walkscore.com")

        #Type the name of the street in the address box
        driver.find_element(by=By.XPATH, value="//*[@id='gs-street']").send_keys(word + " Charlottesville ")

        #Hit enter
        driver.find_element(by=By.XPATH, value="//*[@id='gs-street']").send_keys(Keys.RETURN)




        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='address-header']/div[4]/div[1]/div[1]/div/img"))
            )
        finally:
            source = driver.find_element(by=By.XPATH, value="//*[@id='address-header']/div[4]/div[1]/div[1]/div/img").get_attribute('src')
            dictionary[word] = PrintString(source)
            #walkScoreArray.append(PrintString(source)) change this to dictionary insteead of list

    return dictionary

print(startUp(roseHillStreets))
/Users/stevenpham/PycharmProjects/Cmp
