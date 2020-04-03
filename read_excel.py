#coding:utf-8
import xlrd

class OperationExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'D://Python_WorkSpace//new_test//formatting.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return  tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        tables = self.data
        cell = tables.cell_value(row,col)
        return cell

if __name__ == '__main__':
    scores = {}
    opexcel = OperationExcel()
    lines = opexcel.get_lines()
    for _index in range(lines):
        # print(opexcel.get_cell_value(_index, 0), '---->', opexcel.get_cell_value(_index, 1))
        scores[opexcel.get_cell_value(_index, 0)] = int(opexcel.get_cell_value(_index, 1))
        # scores['ddd'] = 17
    print(scores)