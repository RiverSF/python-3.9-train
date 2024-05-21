import numpy
import pandas as pd

#fd = pd.ExcelFile('Excel数据处理训练.xlsx')
excel = pd.read_excel('Excel数据处理训练.xlsx',
                      sheet_name=0,
                      header=0,
                      index_col=None,
                      usecols=None
                      )

title = excel.columns.values
data = excel.values
init = {}

for line, row in enumerate(data):
    json = {}
    for key, item in enumerate(row):
        json[title[key]] = item
    init[line] = json

_dict = dict(A=range(1, 4), B=range(4, 7), C=range(7, 10))
_data = pd.DataFrame(_dict, columns=list('ABC'))
_data.to_excel('测试导出Excel.xlsx', engine='xlsxwriter')
