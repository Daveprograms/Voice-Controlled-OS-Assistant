from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

warnings.simplefilter("ignore")
url = 'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Chat%20with%20bot%22%2C%22botConversationDescription%22%3A%22This%20chatbot%20was%20built%20surprisingly%20fast%20with%20Botpress%22%2C%22botId%22%3A%22bf1a0cc1-9d79-48e9-ace5-287f5696eb4d%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%22bf1a0cc1-9d79-48e9-ace5-287f5696eb4d%22%2C%22webhookId%22%3A%22dd60f24f-6fe2-4cf9-b369-dba674d809a4%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22frontendVersion%22%3A%22v1%22%2C%22showPoweredBy%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22LCPIfkCmfihCoym5SxYI3WarW8TyUqAp%22%7D%7D'


chrome_driver_path = r"C:\Users\davfa\OneDrive\Desktop\Voice controll\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)



def click_on_chat_button():
    button = driver.find_element(By.XPATH, '/html/body/div/div/button').click()
    sleep(2)
    while True:
        try:
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            print('Initializing Meli...')

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Meli is Initializing.')
            break
        sleep(1)


def sendQuery(text):

    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    sleep(1)

    send_btn = driver.find_element(By.ID, 'btn-send').click()
    sleep(1)


def isBubbleLoaderVisible():
    print('Meli Is Typing...')
    while True:
        try:
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Meli Is Sending Mesage...')
            break
        sleep(1)


chatnumber = 2


def retriveData():
    print(' Meli is Retriving Chat...')
    global chatnumber
    sleep(1)
    p = driver.find_element(
        By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')
    print("\nMeli: " + p.text.replace('You:', ''))
    chatnumber = chatnumber + 2
    return p.text.replace('You:', '')


# click_on_chat_button()
# def ai_brain():
#     query = input('\nYou: ')
#     sendQuery(query)
#     isBubbleLoaderVisible()
#     retriveData()


# /html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[4]/div/div[2]/div/div/div/div/div/p
#/html/body/div/