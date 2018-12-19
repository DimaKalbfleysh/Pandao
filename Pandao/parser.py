import requests
from requests.exceptions import ConnectionError

list_data = []


def get_html(url):
    while True:
        try:
            r = requests.get(url)
            return r.json()
        except ConnectionError:
            continue


def append_data_in_list(json, searching):
    if len(json["output"]) > 1000:
        elements = json["output"].split("\n")
        for element in elements:
            if element.split("=")[0].strip() == searching:
                if searching == "data-id":
                    element = "https://pandao.ru/product/" + element.split("=")[1].strip().split("\"")[1]
                else:
                    element = element.split("=")[1].strip().split("\"")[1]
                list_data.append(element)


def return_list_data(category, searching):
    for page in range(0, 51):
        url = "https://pandao.ru/ajax/catalog?category={0}&page={1}".format(category, page)
        json = get_html(url)
        append_data_in_list(json, searching)
    return list_data



