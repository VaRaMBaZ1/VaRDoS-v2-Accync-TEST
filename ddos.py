import grequests

site = input("Введите URL сайта: ")
threads = int(input("Введите количество потоков: "))

while True:
    site_info = [site for x in range(threads)]

    response = (grequests.get(url) for url in site_info)
    resp = grequests.map(response)