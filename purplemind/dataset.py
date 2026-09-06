import pandas as pd

from sklearn.model_selection import train_test_split

from config import (
    FEATURE,
    COLONNA_TARGET,
    PERCENTUALE_TEST,
    SEME_RANDOM,
    FILE_DATASET_SIMULATO
)


# Trasforma gli eventi in un DataFrame
def crea_dataframe(eventi):
    dataframe = pd.DataFrame(eventi)

    dataframe = dataframe.sample(
        frac=1,
        random_state=SEME_RANDOM
    ).reset_index(drop=True)

    return dataframe


# Salva il dataset in formato CSV
def salva_dataset(dataframe):
    dataframe.to_csv(
        FILE_DATASET_SIMULATO,
        index=False
    )


# Prepara i dati per il Machine Learning
def prepara_dati(dataframe):

    dati_ml = dataframe[
        FEATURE + [COLONNA_TARGET]
    ].copy()

    dati_ml[COLONNA_TARGET] = (
        dati_ml[COLONNA_TARGET]
        .map({
            "benign": 0,
            "malicious": 1
        })
    )

    X = dati_ml[FEATURE]
    y = dati_ml[COLONNA_TARGET]

    return X, y


# Divide i dati in training e test
def dividi_dati(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=PERCENTUALE_TEST,
        random_state=SEME_RANDOM,
        stratify=y
    )

    return X_train, X_test, y_train, y_test
