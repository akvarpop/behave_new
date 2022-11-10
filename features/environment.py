import time

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

'''options Chrome'''
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


def before_all(context):
    '''Work on MAC without Docker, with ChromeDriverManager'''
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    '''On Mac without Docker, with ChromeDriver'''
    # context.driver = webdriver.Chrome("/Users/antongrunt/Desktop/project/chromedriver", options=options)

    '''On MAC vs Docker'''
    # os.system("docker rm --force popravka_behave1")
    # os.system(f"docker run -d --name popravka_behave1 -p 4444:4444 -p 5900:5900 seleniarm/standalone-chromium")

    '''On Jenkins vs Docker'''
    os.system("docker rm --force popravka_behave1")
    os.system(f"docker run -d --name popravka_behave1 -p 4444:4444 selenium/standalone-chrome-debug")
    time.sleep(4)
    context.driver = webdriver.Remote(
        command_executor=f'http://localhost:4444/wd/hub',
        options=options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def after_all(context):
    time.sleep(3)
    context.driver.close()
    os.system("docker rm --force popravka_behave1")