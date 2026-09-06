import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import IsolationForest

from config import (
    SEME_RANDOM,
    NUMERO_ALBERI,
    PROFONDITA_MASSIMA,
    CONTAMINAZIONE
)


# Logistic Regression
def crea_logistic_regression():
    return LogisticRegression()


def allena_logistic_regression(X_train, y_train):
    modello = crea_logistic_regression()
    modello.fit(X_train, y_train)

    return modello


# Random Forest
def crea_random_forest():
    return RandomForestClassifier(
        n_estimators=NUMERO_ALBERI,
        max_depth=PROFONDITA_MASSIMA,
        random_state=SEME_RANDOM
    )


def allena_random_forest(X_train, y_train):
    modello = crea_random_forest()
    modello.fit(X_train, y_train)

    return modello


# Isolation Forest
def crea_isolation_forest():
    return IsolationForest(
        contamination=CONTAMINAZIONE,
        random_state=SEME_RANDOM
    )


def allena_isolation_forest(X_train):
    modello = crea_isolation_forest()
    modello.fit(X_train)

    return modello


# Predizione dei modelli supervisionati
def predici(modello, X_test):
    return modello.predict(X_test)


# Predizione Isolation Forest
def predici_anomalie(modello, X_test):
    predizioni = modello.predict(X_test)

    # Isolation Forest:
    # 1  = normale
    # -1 = anomalia
    #
    # PurpleMind:
    # 0 = benign
    # 1 = malicious

    return np.where(
        predizioni == -1,
        1,
        0
    )
