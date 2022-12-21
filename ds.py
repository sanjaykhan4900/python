import pandas as pd
a=pd.read_csv(r"C:\Users\priya\OneDrive\Desktop\python\dataset\bitcoin_price_1week_Test - Test.csv")

print(a)
print(a.head(20))

# clean empty cell
print("drop values")
print(a.dropna())

#remove duplicates
print("duplicacy removal:-")
print(a.drop_duplicates())