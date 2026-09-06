# purplemind: Network Security and Machine Learning Laboratory

PurpleMind is a Python project for studying network traffic, cybersecurity, data analysis, and Machine Learning.

The project is designed for learning and experimentation in a controlled environment.

The main system is PurpleTeam, which manages the complete process:

Network Traffic → Dataset → Data Analysis → Machine Learning → Evaluation

Project Goal

The main goal is to understand how Machine Learning can be used to analyze network events.

The project can:

Generate simulated network events
Analyze network traffic
Create datasets
Study data using EDA
Train Machine Learning models
Compare different models
Evaluate detection performance
Project Structure
config.py

Contains the main configuration values, such as:

Number of normal events
Number of malicious events
Random seed
Simulation parameters
traffic.py

Manages network traffic.

It can generate controlled simulated traffic with Scapy and analyze authorized network captures with PyShark.

dataset.py

Creates and prepares the dataset.

Network events are converted into a Pandas DataFrame.

eda.py

Contains the Exploratory Data Analysis (EDA) functionality.

It is used to study the dataset using statistics and graphs.

models.py

Contains the Machine Learning models:

Logistic Regression
Random Forest
Isolation Forest
evaluation.py

Evaluates the models using:

Accuracy
Precision
Recall
Confusion Matrix
False Positives
False Negatives
main.py

Runs the complete project pipeline.

pteamLab.ipynb

Jupyter Notebook used to study the project step by step.

main.py runs the process automatically, while the notebook is intended for learning and experimentation.

Libraries

The main libraries are:

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Scapy
PyShark
Installation

Clone the repository:

git clone <repository-url>
cd PurpleMind


Install the required libraries:

python -m pip install pandas numpy scikit-learn matplotlib seaborn scapy pyshark


Or, if a requirements.txt file is available:

python -m pip install -r requirements.txt

Usage

Run the complete project with:

python main.py


To study the project step by step, open:

pteamLab.ipynb

Machine Learning Models
Logistic Regression

Used as the baseline model.

It is simple and provides a reference for comparing other models.

Random Forest

A more complex supervised model based on multiple decision trees.

It can learn more complex patterns in the data.

Isolation Forest

Used for anomaly detection.

Unlike the supervised classification models, it focuses on identifying unusual events.

Dataset

The dataset contains network event features such as:

Timestamp
Source IP
Destination port
Bytes sent
Duration
Failed logins
Request rate
Label

The labels are:

benign
malicious

For Machine Learning:

benign = 0
malicious = 1

Dataset Overlap

The dataset should not be completely perfect.

Benign and malicious events can have similar feature values. This is called overlap.

Overlap makes the experiment more realistic because the models cannot separate all events using a single simple rule.

Model Evaluation

PurpleMind uses several evaluation metrics.

Accuracy

Percentage of correct predictions.

Precision

Measures how many positive predictions are actually correct.

Recall

Measures how many real malicious events are detected.

Recall is particularly important in cybersecurity because missing a malicious event can be a serious problem.

False Positive

The model predicts that an event is malicious, but the event is actually benign.

False Negative

The model predicts that an event is benign, but the event is actually malicious.

False negatives are especially important in cybersecurity because they represent events that were not detected.

Network Traffic

PurpleMind can work with two types of traffic.

Simulated Traffic

Controlled traffic generated for laboratory experiments.

This approach is useful because the expected labels are known.

Real Traffic

PyShark can be used to analyze authorized network captures.

Real traffic is more complex because a captured packet does not automatically have a malicious or benign label.

Reliable labeling is therefore required before using real traffic for supervised Machine Learning.

Safety

Network capture must only be performed on systems and networks where you have permission.

For learning, it is recommended to use:

Your own computer
Virtual machines
Private laboratory networks
Authorized network captures
Public datasets with appropriate licenses

Real attacks are not required for the Machine Learning experiments. Simulated data is sufficient for the first experiments.

Learning Path

A recommended way to study the project is:

Read config.py
Study traffic.py
Study dataset.py
Study eda.py
Study models.py
Study evaluation.py
Study main.py
Use pteamLab.ipynb to repeat the experiments

The main objective is to understand the complete process, not only the Machine Learning models.

Skills
Python
Modular programming
Functions
Imports
Data structures
File management
Libraries
Networking
IP addresses
Ports
Packets
Network traffic
Traffic analysis
Cybersecurity
Network monitoring
Detection
False positives
False negatives
Anomaly detection
Machine Learning
Datasets
Features
Labels
Training
Testing
Classification
Anomaly detection
Model evaluation
Data Science
Pandas
NumPy
Data cleaning
Statistics
EDA
Visualization
Future Improvements

Possible future improvements include:

Dynamic configuration
More realistic traffic
More difficult datasets
Automatic retraining
Concept drift
Ensemble models
Real-time monitoring
SOC dashboard
MITRE ATT&CK mapping
Graph-based network analysis
Event streaming
Project Status

Educational / Experimental

PurpleMind is a learning project designed to explore the connection between Python, networking, cybersecurity, data science, and Machine Learning.

The project should be improved step by step while keeping the system understandable and controlled.
