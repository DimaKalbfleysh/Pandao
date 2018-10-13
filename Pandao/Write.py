import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Pandao")


def saveExcel(column, data, name):
    """ Функция записывает данные в excel таблицу. """
    sheet1.write(0, column, name)
    row = 1
    for line in data:
        sheet1.write(row, column, line)
        row += 1
    book.save("Pandao.xls")
