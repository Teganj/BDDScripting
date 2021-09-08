from selenium import webdriver

from variables.variables import chrome_location


def before_all(context):
    context.browser = webdriver.Chrome
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': '/home/QA/BDD_Scripting/data/in/'}
    options.add_experimental_option('prefs', prefs)
    # options.add_argument('--headless')
    # options.add_argument('disable-gpu')
    options.add_argument('start-maximized')
    options.add_argument('./data/in/')
    context.browser = webdriver.Chrome(chrome_location, options=options,)
    context.browser.implicitly_wait(30)


def after_all(context):
    context.browser.close()
