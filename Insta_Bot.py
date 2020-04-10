from selenium import webdriver
from time import sleep
import pw
from selenium.webdriver.common.keys import Keys
import random
import sys


class Insta_Bot:
    def __init__(self, username, password):
        self.username = username
        self.driver =  webdriver.Firefox(executable_path = "C:\\Users\\Sachin\\Python_programs\\Insta_Bot\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        self.driver.get("https://www.instagram.com/")
        self.password = password


    def login(self):
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

                

        # Liking photos
        unique_photos = len(pic_hrefs)
        print("unique",unique_photos)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            print("href",pic_href)
            sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            sleep(random.randint(2, 5))
            #like_button = bot.find_element_by_xpath("")
            like_button = driver.find_element_by_xpath('//span[@aria-label="Like"]')
            print(like_button)
            like_button().click()
            for second in reversed(range(0, random.randint(18, 28))):
                print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                + " | Sleeping " + str(second))
                sleep(3)



    def CloseBrowser(self):
        self.driver.close()
        
    

if __name__ == "__main__":

    Bot = Insta_Bot("crazysupercars3",pw.password)
    Bot.login()
    hashtags = ['cars', 'money', 'luxury','lamborghini','rich','supercars','supercar','wealth','rollsroyce','wraith','ghost','ferrari','bentley']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            print(tag)
            Bot.like_photo(tag)
        except Exception:
            Bot.CloseBrowser()
            sleep(60)
            Bot = InstagramBot("crazysupercars3",pw.password)
            Bot.login()







