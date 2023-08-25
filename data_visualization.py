print("started data visualization")

from data_cleaning import df2
import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x='gender', y='age', data=df2)
# plt.show()

sns.barplot(x=df2['smoking_history'], y=df2['HbA1c_level'], hue = df2["gender"])
# plt.show()

sns.scatterplot(x=df2["age"], y=df2["bmi"], hue=df2["gender"])
# plt.show()

sns.scatterplot(x=df2["age"], y=df2["blood_glucose_level"], hue=df2["gender"], style=df2['blood_glucose_level'])
# plt.show()
