from functools import partial
from multiprocessing.pool import Pool
from Pandao.Categories import categories
from Pandao.GetData import sendData
from Pandao.Write import saveExcel


def getList(dates):
    lists = []
    for data in dates:
        lists += data
    return lists


def pool(searching):
    with Pool(22) as p:
        data = p.map(partial(sendData, searching=searching), categories)
    return data


def main():
    saveExcel(0, getList(pool("data-name")), "Name")
    saveExcel(1, getList(pool("data-price")), "Price")
    saveExcel(2, getList(pool("data-id")), "URL")


if __name__ == '__main__':
    main()
