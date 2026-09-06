import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)


def valuta_modello(nome_modello, y_test, predizioni):

    accuratezza = accuracy_score(
        y_test,
        predizioni
    )

    precisione = precision_score(
        y_test,
        predizioni,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predizioni,
        zero_division=0
    )

    matrice = confusion_matrix(
        y_test,
        predizioni
    )

    veri_negativi, falsi_positivi, falsi_negativi, veri_positivi = (
        matrice.ravel()
    )

    return {
        "Modello": nome_modello,
        "Accuracy": accuratezza,
        "Precision": precisione,
        "Recall": recall,
        "False Positives": falsi_positivi,
        "False Negatives": falsi_negativi
    }


def crea_confronto(risultati):

    return pd.DataFrame(risultati)


def scegli_miglior_modello(confronto):

    indice_migliore = confronto["Recall"].idxmax()

    return confronto.loc[indice_migliore]


def stampa_report(nome_modello, y_test, predizioni):

    print(f"\n=== {nome_modello} ===")

    print(
        classification_report(
            y_test,
            predizioni,
            zero_division=0
        )
    )
