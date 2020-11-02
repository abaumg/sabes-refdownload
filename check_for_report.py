from configparser import ConfigParser
import requests
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


# set firefox headless mode
options = Options()
#options.headless = True

# read configuration file
parser = ConfigParser()
parser.read('config.ini')

fiscalcode = parser.get('SabesData', 'FiscalCode')
token = parser.get('SabesData', 'Token')
bottoken = parser.get('Telegram', 'BotToken')
chatid = parser.get('Telegram', 'ChatId')

# stop if new report was detected
if parser.getboolean('Run', 'Stop') is True:
    quit()

browser = webdriver.Firefox(
    options=options,
    executable_path='./geckodriver'
    )

browser.get('https://refonline.sabes.it/?AspxAutoDetectCookieSupport=1')

# click Privacy "Accept" button
browser.find_element_by_class_name('btn-primary').click()

# fill out fiscal code and token
browser.find_element_by_id('FiscalCode').send_keys(fiscalcode)
browser.find_element_by_id('Otp').send_keys(token)

# click Submit button
browser.find_element_by_class_name('btn-primary').click()

# find content
content = browser.find_element_by_class_name('tbl_wartezeiten').get_attribute('innerHTML')

if 'REPORT NOT AVAILABLE' in content:
    pass
else:
    requests.get(
        'https://api.telegram.org/bot{bottoken}/sendMessage?chat_id={chatid}&text={message}'.format(
            bottoken=bottoken,
            chatid=chatid,
            message=urllib.parse.quote('Report online!')
        )
    )

    # write stop flag
    parser.set('Run', 'Stop', 'True')
    with open('config.ini', 'w') as configfile:
        parser.write(configfile)

# close browser
browser.quit()