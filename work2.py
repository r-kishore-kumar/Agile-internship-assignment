import pandas as pd

inputData=pd.read_excel('Python Assignment.xlsx')

outputData=inputData.copy()

with pd.ExcelWriter('output.xlsx') as writer:
    outputData.to_excel(writer,index=False,sheet_name='outputSheet')