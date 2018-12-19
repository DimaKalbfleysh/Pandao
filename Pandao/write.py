import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet("Pandao")


def write_to_excel(column, data, name):
    """ Функция записывает данные в excel таблицу. """
    sheet.write(0, column, name)
    row = 1
    for line in data:
        sheet.write(row, column, line)
        row += 1
    book.save("Pandao.xls")
