import winsound
import time
from selenium import webdriver

soundDur = 4000
soundFreq = 440
#Este es tu "path" para el chromedriver de tu PC
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.x-kom.pl/szukaj?q=3070&f%5Bgroups%5D%5B5%5D=1&sort_by=accuracy_desc&f%5Bcategories%5D%5B345%5D=1")

"""Es simple, después de específicar un sitio web, verifica tres cosas. Nombre del producto (tarjeta gráfica), precio y disponibilidad.
 guarda esos tres valores en variables, luego guarda esos valores en una matriz bidimensional y le alerta con sonido si hay alguna tarjeta disponible. """
while 1:
    cardName = driver.find_elements_by_class_name('sc-1yu46qn-11')
    cardPrices = driver.find_elements_by_class_name('hNZEsQ')
    cardAvailable = driver.find_elements_by_class_name('geHfky')

    cards = []
    for i in range(len(cardName)):
        currentCardName = cardName[i].get_attribute("title")[23:-9]
        currentCardPrice = cardPrices[i].get_attribute("innerHTML")
        currentCardAvailable = cardAvailable[i].is_enabled()
        cards.append([currentCardName, currentCardPrice, currentCardAvailable])
        if currentCardAvailable:
            print(f'{currentCardName} Esta disponible por {currentCardPrice} ')
            winsound.Beep(soundFreq,soundDur)
    
    time.sleep(300)
    driver.refresh()