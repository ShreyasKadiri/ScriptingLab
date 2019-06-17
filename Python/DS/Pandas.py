# import the pandas library
import pandas as pd #'pandas' stands for panel data
import numpy as np #'numpy' stands for numerical python

df = pd.DataFrame(np.random.randn(4,3), index=['a', 'c', 'e','h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print ("------Prints the data frame----\n", df)

print ("------Prints True if NULL value in column one ----\n", df['one'].isnull())

print ("------Fills NAN with 0 in the data frame----\n", df.fillna(0))

print ("------Drops the missing values in the data frame----\n", df.dropna())

print ("------Forward fills the missing values in the data frame----\n", df.fillna(method='pad'))

print ("------Backward fills the missing values in the data frame----\n",df.fillna(method='bfill')) 
