import xlrd

path="TestData.xlsx"
inputxl=xlrd.open_workbook(path) # Opened entire excell file
inputsheet= inputxl.sheet_by_name("Sheet1") # selected specifc sheet required

#print(inputsheet.nrows)
#print(inputsheet.ncols)

for i in range(1,inputsheet.nrows):
    for j in range(inputsheet.ncols):
        print(inputsheet.cell_value(i,j))
