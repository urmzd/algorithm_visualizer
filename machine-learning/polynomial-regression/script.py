from sklearn import model_selection, preprocessing, linear_model, pipeline
import numpy as np
import pandas as pd

"""
    Headers: Year Month Min Max
    Headers Index: 0 1 2 3
"""

df = pd.DataFrame(pd.read_csv('./input00.txt', sep=" ", skiprows=1))
min_df = df.loc[df["Min"].str.contains(r'^missing_\.$')]
print(min_df)
