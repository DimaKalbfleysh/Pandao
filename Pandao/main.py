from functools import partial
from multiprocessing.pool import Pool
from Pandao.categories import CATEGORIES
from Pandao.parser import return_list_data
from Pandao.write import write_to_excel


def get_list_data(searching):
    data = []
    with Pool(22) as p:
        lists = p.map(partial(return_list_data, searching=searching), CATEGORIES)
    for list in lists:
        data.extend(list)
    return data


def main():
    data = get_list_data("data-name")
    write_to_excel(0, data, "Name")

    data = get_list_data("data-price")
    write_to_excel(1, data, "Price")

    data = get_list_data("data-id")
    write_to_excel(2, data, "URL")


if __name__ == '__main__':
    main()
