# Hybrid Digital Twin for NH₃-H₂ Spark Ignition Engines (HDTwinNH₃H₂)

## 🧠 Overview
This project develops a **hybrid digital twin** of a spark-ignition (SI) engine operating with ammonia-hydrogen blends. It integrates high-fidelity simulations, system-level models, and machine learning surrogates to predict engine behavior efficiently.

## 🎯 Goals

- Model SI engine behavior with NH₃-H₂ blends
- Fuse CFD, GT-SUITE/Simulink, and ML surrogates
- Validate hybrid twin using synthetic/open datasets
- Support optimization and sensitivity studies

## ⚙️ Tech Stack

- Python (scikit-learn, PyTorch/TensorFlow)
- MATLAB/Simulink or OpenModelica
- GT-SUITE or OpenFOAM
- Docker, GitHub Actions, Jupyter

## 🗂️ Modules

- `data-prep/`: Preprocess multi-fidelity data
- `physics-model/`: Link GT-SUITE/Simulink outputs
- `surrogate-model/`: ML models (GPR, NN)
- `validation/`: Test performance on blend ratios
- `docs/`: Architecture, diagrams, usage notes

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/HDTwinNH3H2.git
cd HDTwinNH3H2
pip install -r requirements.txt
