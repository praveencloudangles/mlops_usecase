print("started feature engineering")

from data_visualization import df2
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder


string_columns=df2.select_dtypes(include=['object']).columns
print(string_columns)


label_encoder=preprocessing.LabelEncoder()

column_name='age'
df2.loc[:, column_name]=df2[column_name].astype('int')


for col in string_columns:
    df2.loc[:, col]=label_encoder.fit_transform(df2[col])