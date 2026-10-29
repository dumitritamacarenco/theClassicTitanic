import numpy as np
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df.info()
print(df.head()) # 5 first rows

print(df.duplicated()) #check for duplocated rows - returns a bool