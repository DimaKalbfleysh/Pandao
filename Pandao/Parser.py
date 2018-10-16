import requests


def getDataLists(category, searched):
    """ Функция возвращает списки names, prices, urls. """
    global data_list
    data_list = []
    for page in range(0, 51):
        url = "https://pandao.ru/ajax/catalog?category={}&page={}".format(category, page)
        data = DataLists(url, searched).getData()
    print(data_list)
    return data_list


class DataLists:
    def __init__(self, url, searched):
        self.url = url
        self.json = self.getHtml()
        self.searched = searched

    def getHtml(self):
        while True:
            try:
                r = requests.get(self.url)
                return r.json()
            except:
                continue

    def getData(self):
        if len(self.json["output"]) < 1000:
            return None
        else:
            index = 0
            json = self.json["output"].split("\n")
            while True:
                try:
                    if json[index].split("=")[0].strip() == self.searched:
                        if self.searched == "data-id":
                            element = "https://pandao.ru/product/" + json[index].split("=")[1].strip().split("\"")[1]
                        else:
                            element = json[index].split("=")[1].strip().split("\"")[1]
                        data_list.append(element)
                    index += 1
                except IndexError:
                    break
            return data_list



