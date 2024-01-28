from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


LINKS_WITH_GREY_METRIC = []
LINKS_OF_PAGE = []


"""Создание драйвера с помощью которого можно открыть веб-страницу через Яндекс-браузер"""
def open_links(main_link):
    service = Service(executable_path='') #Путь к chromedriver
    options = Options()
    options.add_argument("--headless")
    options.binary_location = '' #Путь к бинарному файлу Яндекс Браузера
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(main_link)
    return driver


"""Функция, которая ищет на странице интересующий нас тег '"""
def search_teg(link):
    global LINKS_WITH_GREY_METRIC
    page = open_links(link)
    f = open("html_of_page.txt", "w+")
    f.write(page.page_source)
    f.close()
    f = open("html_of_page.txt", "r")
    if 'class=" sensor level_5 m3_popover"' in f.read():
        LINKS_WITH_GREY_METRIC.append(link)
    f.close()


"""Функция, которая собирает с главных страниц все ссылки"""
def search_links():
    main_links = []
    global LINKS_OF_PAGE
    for link in main_links:
        main_page = open_links(link)
        soup = BeautifulSoup(main_page.page_source, "html.parser")
        for teg_a in soup.select('a'):
            teg_href = teg_a.get('href')
            if '.html' in teg_href:
                LINKS_OF_PAGE.append(link + '/' + teg_href)


def search_grey_metricks():
    global LINKS_OF_PAGE
    search_links()
    for link in LINKS_OF_PAGE:
        search_teg(link)
    LINKS_OF_PAGE = []

