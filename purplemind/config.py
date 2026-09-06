from pathlib import Path


# Cartella principale del progetto
CARTELLA_PROGETTO = Path(__file__).resolve().parent

# Cartella dei dataset
CARTELLA_DATI = CARTELLA_PROGETTO / "data"

# Cartella dei risultati
CARTELLA_RISULTATI = CARTELLA_PROGETTO / "output"

CARTELLA_DATI.mkdir(exist_ok=True)
CARTELLA_RISULTATI.mkdir(exist_ok=True)


# Numero di eventi normali
EVENTI_NORMALI = 500

# Numero di eventi di attacco
EVENTI_ATTACCO = 100

# Permette di ottenere gli stessi risultati
SEME_RANDOM = 42


# Livello della simulazione
DIFFICOLTA = "medium"

# Quantità di rumore nei dati
LIVELLO_RUMORE = 0.10

# Probabilità di generare un attacco stealth
PROBABILITA_STEALTH = 0.20


# Feature utilizzate dal Machine Learning
FEATURE = [
    "dst_port",
    "bytes_sent",
    "duration",
    "failed_logins",
    "request_rate"
]

# Colonna che contiene la risposta corretta
COLONNA_TARGET = "label"


# Percentuale dei dati utilizzata per il test
PERCENTUALE_TEST = 0.20


# Porte utilizzate dal traffico normale
PORTE_NORMALI = [
    80,
    443,
    8080
]


# Porte utilizzate nella simulazione degli attacchi
PORTE_ATTACCO = [
    21,
    22,
    23,
    445,
    3389
]


# Parametri Random Forest
NUMERO_ALBERI = 100
PROFONDITA_MASSIMA = None


# Percentuale di anomalie prevista
CONTAMINAZIONE = (
    EVENTI_ATTACCO /
    (EVENTI_NORMALI + EVENTI_ATTACCO)
)


# Configurazione cattura PyShark
INTERFACCIA_RETE = None
NUMERO_PACCHETTI = 100


# File del dataset simulato
FILE_DATASET_SIMULATO = (
    CARTELLA_DATI / "traffico_simulato.csv"
)

# File del dataset reale
FILE_DATASET_REALE = (
    CARTELLA_DATI / "traffico_reale.csv"
)

# Negli altri moduli possiamo importare i valori da config.py:
# from config import EVENTI_NORMALI, EVENTI_ATTACCO
#
# In questo modo non dobbiamo riscrivere 500 e 100
# dentro ogni file.
