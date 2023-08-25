print('sarted data cleaning')

from data_analysis import df1
import pandas as pd


df2=df1.drop_duplicates()


column_name='age'

def custom_round(value):
    rounded_value=round(value, 2) # round to two decimal places.
    second_decimal=int(rounded_value*100) % 10 # Extract the second decimal digit.

    if second_decimal > 5:
        rounded_value=round(rounded_value + 0.1, 1) #Increment first decimal.
    
    first_decimal=int(rounded_value * 10) % 10 # Extract the first decimal digit.

    if first_decimal > 5:
        rounded_value=round(rounded_value + 0.1, 1) #Increment the final value as 1.

    return int(rounded_value) #convert to integer.

#apply the custom round function to the specified column.
df2.loc[:, column_name]=df2[column_name].apply(custom_round)

