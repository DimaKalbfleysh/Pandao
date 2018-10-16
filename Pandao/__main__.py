import threading
from functools import partial
from multiprocessing.pool import Pool
from Pandao.Categories import categories
from Pandao.Parser import getDataLists
from Pandao.Write import saveExcel


def getList(dates):
    """ Функция плюсует списки и возвращает единый список. """
    lists = []
    for data in dates:
        lists += data
    return lists


def pool(searched_data):
    """ Функция возвращает список searched_data"""
    global r
    for category in categories:
        r = threading.Thread(target=getDataLists, args=(category, searched_data))
        r.start()
    return r


def main():

    name = getList(pool("data-name"))
    saveExcel(0, name, "Name")

    price = getList(pool("data-price"))
    saveExcel(1, price, "Price")

    url = getList(pool("data-id"))
    saveExcel(2, url, "URL")


if __name__ == '__main__':
    main()
