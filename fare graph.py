import pandas as pd
import matplotlib.pyplot as pl
df=pd.read_csv("C:\\Users\\janvi\\Documents\\reservation table.csv")
print (df);
pl.plot(df["fare"])
pl.show();