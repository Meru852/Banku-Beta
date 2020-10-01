from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

#https://meet.google.com/btw-ekro-yrc

def googlelogin(browser, email, password):
    print('Logging into google.....')
    browser.get("https://accounts.google.com/login")
    time.sleep(2)

    #enter email
    webdriver.ActionChains(browser).send_keys(email).perform()
    time.sleep(1)
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(7)

    #enter password
    webdriver.ActionChains(browser).send_keys(password).perform()
    time.sleep(1)
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(10)


def meetlogin(browser, url, callDur):
    print('Joining Meeting....')
    browser.get(url)
    time.sleep(5)

    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)

    # webdriver.ActionChains(browser).send_keys(Keys.TAB * 7).perform()
    # webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()


    time.sleep(3)

    join = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
    join.click()

    print('Meeting Joined :):)')

    time.sleep(callDur * 60)

    browser.close()

def speech_alert():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Anything: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('Sorry I did not get it')

    
def main():
    print('Banku Beta is active:')

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    })

    browser = webdriver.Chrome(executable_path=r'C:\Users\NAMANJEET SINGH\Documents\chromedriver_win32\chromedriver.exe',options=chrome_options)
    browser.maximize_window()

    email = 'bankubeta123@gmail.com'                       # Enter G mail here
    password = 'brogrammers3211'                           # Enter PASSWORD here
    url = input('Enter meeting link: ')                    # Enter Meeting URL here
    callDur = int(input('Enter duration in minutes: '))    # Enter how long you want the call

    time.sleep(10)

    googlelogin(browser, email, password)

    meetlogin(browser, url, callDur)

main()
