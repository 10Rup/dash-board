import pandas as pd

res_data = pd.read_csv("result_data.csv")

res_data

# headers = [x for x in res_data.columns]
headers =list(res_data.columns)
print(headers)