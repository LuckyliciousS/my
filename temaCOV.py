
from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\acer\\Desktop\\python\\chromedriver")

num = [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
fisier = open("Covidut.txt", 'w+')

for i, j in enumerate(num):
    url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"+ str(j) +"-aprilie-2020-ora-13-00/"
    browser.get(url)
    xpath = ['//*[@id="post-20928"]/div/div/table[1]', '//*[@id="post-20948"]/div/div/div[1]/table[1]',
             '//*[@id="post-20986"]/div/div/table[1]', '//*[@id="post-21004"]/div/div/table[1]',
             '//*[@id="post-21053"]/div/div/table[1]', '//*[@id="post-21056"]/div/div/table[1]',
             '//*[@id="post-21076"]/div/div/table[1]', '//*[@id="post-21085"]/div/div/table[1]',
             '//*[@id="post-21095"]/div/div/table[1]', '//*[@id="post-21106"]/div/div/table[1]',
             '//*[@id="post-21113"]/div/div/table[1]', '//*[@id="post-21150"]/div/div/table[1]',
             '//*[@id="post-21169"]/div/div/table[1]', '//*[@id="post-21193"]/div/div/table[1]',
             '//*[@id="post-21198"]/div/div/table[1]', '//*[@id="post-21205"]/div/div/table[1]',
             '//*[@id="post-21210"]/div/div/table[1]', '//*[@id="post-21244"]/div/div/table[1]',
             '//*[@id="post-21260"]/div/div/table[1]', '//*[@id="post-21267"]/div/div/table[1]',
             '//*[@id="post-21270"]/div/div/table[1]', '//*[@id="post-21272"]/div/div/table[1]',
             '//*[@id="post-21274"]/div/div/table[1]']

    table = browser.find_element_by_xpath(xpath[i])
    fisier.writelines(table.text)
    fisier.close()

    tabel = table.text
    lista = tabel.split('\n')

browser.close()
