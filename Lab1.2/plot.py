from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('C:\\Users\\p.mykhailyk\\Seafile\\p4ne_training\\data_analysis_lab.xlsx')

sheet_data = wb['Data']

sheet_A = sheet_data['A'][1:]
sheet_B = sheet_data['B'][1:]

def getV(x):    return x.value
A_V = list(map(getV,sheet_data['A'][1:]))
B_V = list(map(getV,sheet_data['B'][1:]))
C_V = list(map(getV,sheet_data['C'][1:]))
print(A_V)

grap1 = pyplot.plot(A_V, B_V)
grap2 = pyplot.plot(A_V, C_V)
pyplot.show(grap1)
pyplot.show(grap2)
