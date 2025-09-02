import pandas as pd
import matplotlib.pyplot as pl
df=pd.read_csv("C:\\Users\\janvi\\Documents\\reservation table.csv")
print (df)
pl.title("fare according to age")
pl.xlabel("age")
pl.ylabel("fare")
pl.bar(df["age"],df["fare"],color="lightblue")
pl.show()

