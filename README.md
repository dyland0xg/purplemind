# PurpleMind

## Network Security and Machine Learning Laboratory

PurpleMind is a Python project for studying **network traffic, cybersecurity, data analysis, and Machine Learning**.

The project is designed for learning and experimentation in a controlled environment.

The main system is **PurpleTeam**, which manages the complete process:

**Network Traffic → Dataset → Data Analysis → Machine Learning → Evaluation**

---

## Project Goal

The main goal is to understand how Machine Learning can be used to analyze network events.

The project can:
- Generate simulated network events
- Analyze network traffic
- Create datasets
- Study data using EDA
- Train Machine Learning models
- Compare different models
- Evaluate detection performance

---

## Project Structure

### `config.py`
Contains configuration values such as the number of normal and malicious events, random seed, and simulation parameters.

### `traffic.py`
Generates controlled traffic with **Scapy** and analyzes authorized network captures with **PyShark**.

### `dataset.py`
Creates and prepares the dataset using **Pandas**.

### `eda.py`
Performs Exploratory Data Analysis using statistics and graphs.

### `models.py`
Contains the Machine Learning models:
- Logistic Regression
- Random Forest
- Isolation Forest

### `evaluation.py`
Evaluates models using Accuracy, Precision, Recall, Confusion Matrix, False Positives, and False Negatives.

### `main.py`
Runs the complete project pipeline.

### `pteamLab.ipynb`
Jupyter Notebook used to study the project step by step.

---

## Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Scapy
- PyShark

---

## Installation & Usage

### Clone the repository
```bash
git clone https://github.com/dyland0xg/purplemind.git
```

### Usage
Run the main script:
```bash
python main.py
```

Or open the interactive notebook:
```bash
jupyter notebook pteamLab.ipynb
```

---

## Dataset

The dataset contains features such as:
- **Timestamp**
- **Source IP**
- **Destination port**
- **Bytes sent**
- **Duration**
- **Failed logins**
- **Request rate**
- **Label**

### Labels
- `benign` = 0
- `malicious` = 1

*Note: The dataset includes overlap between benign and malicious events to make the experiment more realistic.*

---

## Model Evaluation

- **Accuracy**: Measures the percentage of correct predictions.
- **Precision**: Measures how many positive predictions are correct.
- **Recall**: Measures how many malicious events are detected.
- **False Positive**: A benign event is classified as malicious.
- **False Negative**: A malicious event is classified as benign.

---

## Network Traffic

PurpleMind supports both simulated traffic and authorized real network captures.

> **Important**: Real network traffic must only be captured and analyzed on systems where you have explicit permission.

---

## Learning Path

1. `config.py`
2. `traffic.py`
3. `dataset.py`
4. `eda.py`
5. `models.py`
6. `evaluation.py`
7. `main.py`
8. `pteamLab.ipynb`

---

## Skills Covered

- **Python**: Modular programming, functions, imports, data structures, file management, and libraries.
- **Networking**: IP addresses, ports, packets, network traffic, and traffic analysis.
- **Cybersecurity**: Network monitoring, detection, false positives, false negatives, and anomaly detection.
- **Machine Learning**: Datasets, features, labels, training, testing, classification, anomaly detection, and model evaluation.
- **Data Science**: Pandas, NumPy, data cleaning, statistics, EDA, and visualization.

---

## Future Improvements

- More realistic traffic generation
- Complex and dynamic datasets
- Automatic retraining pipeline
- Concept drift handling
- Advanced Ensemble models
- Real-time monitoring
- SOC dashboard integration
- MITRE ATT&CK framework mapping
- Graph-based network analysis

---

## Project Status

**Educational / Experimental**

PurpleMind is an educational and learning project that combines Python, networking, cybersecurity, data science, and machine learning.
