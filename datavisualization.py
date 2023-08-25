print("started data visualization")

from data_cleaning import df2
import matplotlib.pyplot as plt
import seaborn as sns

# sns.barplot(x='gender', y='age', data=df2)
# plt.show()

# sns.barplot(x=df2['smoking_history'], y=df2['HbA1c_level'], hue = df2["gender"])
# plt.show()

# sns.scatterplot(x=df2["age"], y=df2["bmi"], hue=df2["gender"])
# plt.show()

# sns.scatterplot(x=df2["age"], y=df2["blood_glucose_level"], hue=df2["gender"], style=df2['blood_glucose_level'])
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrame
# df2 = ...  # Your DataFrame here

# List of plot specifications
plot_specs = [
    ('barplot', ['gender'], ['age']),
    ('barplot', ['smoking_history'], ['HbA1c_level'], 'gender'),
    ('scatterplot', ['age'], ['bmi'], 'gender'),
    ('scatterplot', ['age'], ['blood_glucose_level'], 'gender', 'blood_glucose_level')
]

# Loop through plot specifications and create plots
for spec in plot_specs:
    plot_type, x_columns, y_columns = spec[:3]
    hue_column = spec[3] if len(spec) > 3 else None
    style_column = spec[4] if len(spec) > 4 else None
    
    plt.figure()
    
    if plot_type == 'barplot':
        sns.barplot(x=x_columns[0], y=y_columns[0], data=df2, hue=hue_column)
    elif plot_type == 'scatterplot':
        sns.scatterplot(x=x_columns[0], y=y_columns[0], data=df2, hue=hue_column, style=style_column)
    
    plt.title(f'{plot_type.capitalize()} for {", ".join(x_columns)} vs {", ".join(y_columns)}')
    plt.show()
