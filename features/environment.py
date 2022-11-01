from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# options Chrome
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')


def before_all(context):
    #Work on MAC without Docker
    #context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    #On Jenkins vs Docker (not work for me)
    context.driver = webdriver.Remote(
        command_executor=f'http://localhost:4444/wd/hub',
        options=options
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


# def after_all(context):
#     context.driver.quit()