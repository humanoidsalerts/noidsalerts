from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # this is just another way to install the driver so you don't
# have to install the new version every time


def scrape_floor_price():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://opensea.io/collection/thehumanoids?search[sortAscending]=true&search[sortBy]=PRICE&'
               'search[toggles][0]=BUY_NOW')  # get the buy now page. this directly gets the listings and sorts it by
    # lowest
    floor_price_for_lowest = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div['
                                                          '3]/div/div/div/div[3]/div[4]/div[2]/div/div/div['
                                                          '2]/article/a/div[2]/div/div[2]/div[1]/div/div[2]').text
    # long and ugly XPATH which extracts the first card's (lowest listed humanoids) value
    
    return floor_price_for_lowest


print(scrape_floor_price())
