import requests


def getHtml(url):
    while True:
        try:
            r = requests.get(url)
            return r.json()
        except:
            continue


def getData(json, searching):
    global data_list
    if len(json["output"]) < 1000:
        return None
    else:
        index = 0
        json = json["output"].split("\n")
        while True:
            try:
                if json[index].split("=")[0].strip() == searching:
                    if searching == "data-id":
                        element = "https://pandao.ru/product/" + json[index].split("=")[1].strip().split("\"")[1]
                    else:
                        element = json[index].split("=")[1].strip().split("\"")[1]
                    data_list.append(element)
                index += 1
            except:
                break
        return data_list


def getDataLists(categories, searching):
    """ Функция возвращает списки names, prices, urls. """
    global data_list
    data_list = []
    for page in range(0, 51):
        url = "https://pandao.ru/ajax/catalog?category={}&page={}".format(categories, page)
        data = getData(getHtml(url), searching)
        if data is None:
            break
    print(data_list)
    return data_list
