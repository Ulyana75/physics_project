import pandas as pd
import openpyxl

ss = openpyxl.load_workbook('../new_data/31_03_2021.xlsx')
names = []
for i in range(1, 49):
    s = str(i)
    if len(s) == 1:
        s = '0' + s
    names.append(s)
for i in names[1:]:
    df = pd.read_excel('new_data/31-03-2021/31_03_2021.xlsx', sheet_name=i)
    col_name = df.columns.ravel()[1][:-5]
    col_name = col_name.replace('[', '')
    col_name = col_name.replace(']', '')
    ss_sheet = ss[i]
    ss_sheet.title = col_name
    ss.save('new_data/31-03-2021/31_03_2021.xlsx')