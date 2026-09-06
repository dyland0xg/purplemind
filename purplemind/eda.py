import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Mostra le informazioni principali del dataset
def analizza_dataset(dataframe):

    print("\n=== PRIME RIGHE ===")
    print(dataframe.head())

    print("\n=== DIMENSIONI ===")
    print(dataframe.shape)

    print("\n=== DISTRIBUZIONE CLASSI ===")
    print(dataframe["label"].value_counts())

    print("\n=== STATISTICHE ===")
    print(dataframe.describe(include="all"))


# Mostra la distribuzione dei bytes
def grafico_bytes(dataframe):

    sns.boxplot(
        x="label",
        y="bytes_sent",
        data=dataframe
    )

    plt.title("Bytes inviati")
    plt.show()


# Mostra le correlazioni tra le feature numeriche
def grafico_correlazioni(dataframe):

    correlazioni = dataframe.corr(
        numeric_only=True
    )

    sns.heatmap(
        correlazioni,
        annot=True
    )

    plt.title("Correlazione tra feature")
    plt.show()


# Mostra le relazioni tra le feature
def grafico_pairplot(dataframe):

    sns.pairplot(
        dataframe,
        hue="label"
    )

    plt.show()
