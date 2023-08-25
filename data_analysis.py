from data_loading import df

print("started data analysis")

df1=df

null_values=df1.isnull()
final_nulls=null_values.sum()

duplicate_rows=df1.duplicated()
duplicates=df1[duplicate_rows]