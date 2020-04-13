from selenium import webdriver
from time import sleep
import pw
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import sys


class Insta_Bot:
    def __init__(self, username, password):
        self.username = username
        self.driver =  webdriver.Firefox(executable_path = "C:\\Users\\Sachin\\Python_programs\\Insta_Bot\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        self.driver.get("https://www.instagram.com/")
        self.password = password
        action_chains = ActionChains(self.driver)


    def login(self):
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        sleep(1)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()
        sleep(6)   # increase this sleep if internet is slow to load "not now" button
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    

    def follow_suggested(self):   # blindly follow people from suggestion list, but insta gives verifies accounds in suggestion who won't follow back
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[3]/div[1]/a/div').click()  # see all suggestion link
        sleep(2)
        for j in range(1,6): #can only scroll down only 3-4 times down
            print("Scrolling",j)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            print(j)
        # follow all the people after scrolling down to maximum scrolling
        for i in range(1,14): #number of people follow at one go
            fol = ("/html/body/div[1]/section/main/div/div[2]/div/div/div[%s]/div[3]/button" % (i))
            try:
                print("Following",l)
                sleep(random.randint(1, 3))
                self.driver.find_element_by_xpath(fol).click()
                sleep(random.randint(1, 3))
            except:
                pass

    def follow_tag(self,tag):   # go to that tag page and follow the people who follow that tag, high probablity those people will follow back
        print(tag)
        self.driver.get("https://www.instagram.com/" + tag + "/")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        sleep(2)
        for i in range(1,14):
            for j in range(2,4):
                foll = ("/html/body/div[4]/div/div[2]/ul/div/li[%s]/div/div[%s]/button" %(i,j))
                try:
                    sleep(random.randint(1, 2))
                    print(foll)
                    self.driver.find_element_by_xpath(foll).click()
                    sleep(random.randint(1, 2))
                except:
                    pass

    def followers_check(self):
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()                                                                         #click on the username
        sleep(3)
        try:
            No_of_foll = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").text
        except:
            pass
        if not No_of_foll:
            No_of_foll = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
                                                            
        No_of_foll = No_of_foll.split(" ")              
        No_of_foll =  No_of_foll[0]
        No_of_foll = int(No_of_foll)
        print("Number of followers ",No_of_foll)
        if No_of_foll < 500:         # change here to set limit below which unfollow people
            x = "No need to unfollow"
            print(x)
        else:
            x = "Unfollow"
            print(x)
        return x

    def scroll_following(self):   #scroll till the end
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").click()  #click the following
        sleep(2)

        #################### Script for scrolling ########################
        for i in range(3,5):
            scrol_box_xpath = ("/html/body/div[%s]/div/div[2]"%(i))
            print(scrol_box_xpath)
            try:
                scroll_box = self.driver.find_element_by_xpath(scrol_box_xpath)
                last_ht, ht = 0, 1                              
                while last_ht != ht:
                    last_ht = ht
                    sleep(2)
                    ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
            except:
                pass

    def unfollow(self):  #unfollow the old users
        try:
            No_of_foll = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").text
        except:
            pass
        if not No_of_foll:
            No_of_foll = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text 
        No_of_foll = No_of_foll.split(" ")
        No_of_foll =  No_of_foll[0]
        No_of_foll = int(No_of_foll)
        print("Number of followers ",No_of_foll)
        if No_of_foll < 500:   # change here to set limit below which unfollow people
            print("No of followers less than 400, do nothing")
            pass
        else:
            m = No_of_foll - 500   # change here to set limit below which unfollow people
            print("No of people to unfollow", m)
            for m in range(m):
                s = No_of_foll - m
                print("unfolling person number",s)
                sleep(3)
                try:
                    self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[%s]/div/div[2]/button"%(s)).click()
                    sleep(1)                           
                    self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]").click()
                except:                                 
                    pass

    def CloseBrowser(self):  # close the browser
        self.driver.close()
        
    

if __name__ == "__main__":

    Bot = Insta_Bot("YourUserName",pw.password)  # first time loggining in
    Bot.login()  #login with the username and password


    hashtags = ['cars___official','corvette','dodgeofficial','bugatti','bentleymotors', 'supercars.world46','lamborghini','wealth','rollsroycecars','ferrari']

    # while True:       
    #     try:          
    #         Bot.follow_suggested()
    #     except:
    #         Bot.CloseBrowser()
    #         random_sleep = random.randint(1800, 2800)
    #         sleep(random_sleep)
    #         Bot = Insta_Bot("YourUserName",pw.password)
    #         Bot.login()

    while True: #infi loop      #go to random hastags from the list and follow people who follow that hashtag, then count following people, if they are above limit, then unfollow and after random login and repeat
        try:    # wont give error 
            tag = random.choice(hashtags)
            print("Random tag",tag)
            Bot.follow_tag(tag)
            Bot.CloseBrowser()
            print("sleeping 1 min")
            rand_slp = random.randint(1000, 1500)
            print("Sleeping for ", rand_slp, "s Before unfolling people")
            sleep(rand_slp)
            Bot = Insta_Bot("YourUserName",pw.password)
            Bot.login()
            limit = Bot.followers_check()
            if limit == "Unfollow":  #Check if the followers are above desired number, then unfollow
                Bot.scroll_following()
                Bot.unfollow()
                Bot.CloseBrowser()
            else:
                Bot.CloseBrowser()
            random_sleep = random.randint(1800, 3600)
            print("Random sleep before logging in, time = ", random_sleep, "s")
            sleep(random_sleep)
            Bot = Insta_Bot("YourUserName",pw.password)   # inifinite logging in
            print("Logging in")
            Bot.login()
        except:
            pass