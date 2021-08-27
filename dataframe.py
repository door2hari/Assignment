import numpy as np
import pandas as pd

class dataframe:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def generateRandomN(self):
        self.arr = np.random.randn(int(self.row),int(self.column))
        print(self.arr.shape)

    def convertToDataFrame(self):
        df = pd.DataFrame(self.arr)
        df[2].plot.hist()
        df.to_csv("file.csv")

row = input("Enter the number of rows: ")
column = input("\nEnter the number of columns: ")

obj = dataframe(row, column)
obj.generateRandomN()
obj.convertToDataFrame()
