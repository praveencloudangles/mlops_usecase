print("started data visualization")

from data_cleaning import df2
import matplotlib.pyplot as plt
import seaborn as sns
# from matplotlib.backends.backend_pdf import PdfPages

# sns.barplot(x='gender', y='age', data=df2)
# plt.show()

# sns.barplot(x=df2['smoking_history'], y=df2['HbA1c_level'], hue = df2["gender"])
# plt.show()

# sns.scatterplot(x=df2["age"], y=df2["bmi"], hue=df2["gender"])
# plt.show()

# sns.scatterplot(x=df2["age"], y=df2["blood_glucose_level"], hue=df2["gender"], style=df2['blood_glucose_level'])
# plt.show()



categ = []
numer = []
for col in df2.columns:
    if df2[col].dtypes == object:
        categ.append(col)
    else:
        numer.append(col)

# print(categ)
# print(numer)

# # Histogram plots for categerical values.

# for i in categ:
#     sns.histplot(df2[i])
#     plt.show()


# # Count plot for categerical values.

# for i in categ:
#     sns.countplot(x=df2[i])
#     plt.show()

# # Distribution plots for numeric values.

# for i in numer:
#     plt.subplots(1,1, figsize=(8,4))
#     sns.histplot(x = df2[i])
#     plt.xlabel(i)
# plt.show()


# # Scatter plots for both numerical and categorical values.

# plt.scatter(x='gender', y='age', data=df2)
# plt.xlabel('gender')
# plt.ylabel('age')
# plt.show()

# plt.scatter(x='gender', y='smoking_history', data=df2)
# plt.xlabel('gender')
# plt.ylabel('smoking_history')
# plt.show()

# plt.scatter(x='gender', y='blood_glucose_level', data=df2)
# plt.xlabel('gender')
# plt.ylabel('blood_glucose_level')
# plt.show()


# Box plot for numerical values.
for num in numer:
    plt.figure(figsize=(5,5))
    sns.boxplot(data=df2, x=num)
    plt.xlabel(num)
plt.show()


# violin plots for numeric values.
for num in numer:
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=df2, x=num)
    plt.xlabel(num)
plt.show()
