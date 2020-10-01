from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import speech_recognition as sr
import time
import pyautogui
# import cv2
# import pytesseract
# from PIL import Image
import re

#https://meet.google.com/ksk-wupz-nsw

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

    time.sleep(3)

    join = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
    join.click()

    print('Meeting Joined :):)')
    time.sleep(20)

    answerAttendance()

    time.sleep(callDur * 60)
    print('Meeting Over!!')
    browser.close()

def speech_alert():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Anything: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
            # let us assume that banku's name is called or his roll number 5 is called out
            if (text.find("bankubeta") != -1 or text.find("banku") != -1):
                answerAttendance()

            if (text.find("five") != -1 or text.find("5") != -1):
                answerAttendance()
        except:
            print('Sorry I did not get it')


def answerAttendance():
    pyautogui.moveTo(1602,181, duration=1 )
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1505,984, duration=1 )
    pyautogui.click()
    pyautogui.typewrite( "present sir", 1 )
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

def printnametime(x):
    matchobj = re.search("(.+)(\d?\d:\d{2}\s*[AP]M)", x)
    return(matchobj.group(1), matchobj.group(2))

# under programming so won't work

# def response():
#     time.sleep(20)
#     im2 = pyautogui.screenshot("ss2.png")
#     img2 = cv2.imread('ss2.png')
#     crop2 = img2[280:911, 1520:1900]
#     cv2.imwrite("ss2.png", crop2)
#     try:
#         if (compare("ss1.png", "ss2.png", 1) >= 5):
#
#             a1, b1 = MostCommonWord("ss2.png")
#             print(a1)
#             print(b1)
#             if (b1 >= 3):
#                 pyautogui.moveTo(1602, 181, duration=1)
#                 pyautogui.click()
#                 time.sleep(2)
#                 pyautogui.moveTo(1505, 984, duration=1)
#                 pyautogui.click()
#                 pyautogui.typewrite(a1, 1)
#                 pyautogui.press('enter')
#                 time.sleep(2)
#         else:
#             print("nothing new here")
#     except:
#         print('everything under control!!')
#     cv2.imwrite("ss1.png", crop2)
#     time.sleep(20)


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