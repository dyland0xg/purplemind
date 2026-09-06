# Il notebook e main.py eseguono sostanzialmente la stessa pipeline,
# ma hanno scopi diversi:
# main.py esegue automaticamente tutto il progetto,
# mentre pteamLab.ipynb serve per studiare e visualizzare ogni fase.


from config import (
    EVENTI_NORMALI,
    EVENTI_ATTACCO,
    SEME_RANDOM
)

from traffic import genera_traffico

from dataset import (
    crea_dataframe,
    salva_dataset,
    prepara_dati,
    dividi_dati
)

from eda import (
    analizza_dataset,
    grafico_bytes,
    grafico_correlazioni,
    grafico_pairplot
)

from models import (
    allena_logistic_regression,
    allena_random_forest,
    allena_isolation_forest,
    predici,
    predici_anomalie
)

from evaluation import (
    valuta_modello,
    crea_confronto,
    scegli_miglior_modello,
    stampa_report
)


def main():

    # 1. Generazione traffico
    eventi = genera_traffico(
        EVENTI_NORMALI,
        EVENTI_ATTACCO
    )

    # 2. Creazione dataset
    dataframe = crea_dataframe(eventi)

    salva_dataset(dataframe)

    # 3. EDA
    analizza_dataset(dataframe)

    grafico_bytes(dataframe)
    grafico_correlazioni(dataframe)
    grafico_pairplot(dataframe)

    # 4. Preparazione Machine Learning
    X, y = prepara_dati(dataframe)

    X_train, X_test, y_train, y_test = dividi_dati(
        X,
        y
    )

    # 5. Logistic Regression
    modello_logistic = allena_logistic_regression(
        X_train,
        y_train
    )

    predizione_logistic = predici(
        modello_logistic,
        X_test
    )

    stampa_report(
        "Logistic Regression",
        y_test,
        predizione_logistic
    )

    # 6. Random Forest
    modello_random_forest = allena_random_forest(
        X_train,
        y_train
    )

    predizione_random_forest = predici(
        modello_random_forest,
        X_test
    )

    stampa_report(
        "Random Forest",
        y_test,
        predizione_random_forest
    )

    # 7. Isolation Forest
    modello_isolation = allena_isolation_forest(
        X_train
    )

    predizione_isolation = predici_anomalie(
        modello_isolation,
        X_test
    )

    stampa_report(
        "Isolation Forest",
        y_test,
        predizione_isolation
    )

    # 8. Purple Team: confronto
    risultati = [
        valuta_modello(
            "Logistic Regression",
            y_test,
            predizione_logistic
        ),
        valuta_modello(
            "Random Forest",
            y_test,
            predizione_random_forest
        ),
        valuta_modello(
            "Isolation Forest",
            y_test,
            predizione_isolation
        )
    ]

    confronto = crea_confronto(risultati)

    print("\n=== CONFRONTO PURPLE TEAM ===")
    print(confronto)

    # 9. Scelta del miglior defender
    miglior_modello = scegli_miglior_modello(
        confronto
    )

    print("\n=== PURPLE TEAM VERDICT ===")
    print(
        "Miglior Defender:",
        miglior_modello["Modello"]
    )
    print(
        "Recall:",
        round(miglior_modello["Recall"], 3)
    )


if __name__ == "__main__":
    main()
