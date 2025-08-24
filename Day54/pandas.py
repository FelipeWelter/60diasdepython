#instalar requisitos > !pip install pandas matplotlib seaborn
#UTILIZANDO GOOGLE COLAB

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df.head()

df.info()

df.describe()

df['Survived'].value_counts()

df['Survived'].value_counts(normalize=True) * 100

df['Age'].hist(bins=20)
plt.title("Idades dos passageiros do Titanic")
plt.xlabel("Idade")
plt.ylabel("Frequência")

pd.crosstab(df['Survived'], df['Sex'])

sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title("Classe x Sobrevivência")
plt.xlabel("Classe")
plt.ylabel("Frequência")

