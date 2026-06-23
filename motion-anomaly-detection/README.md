# Motion Fall Detection

### Lightweight model for detecting falls and abnormal movement from IMU sensor data

> **Phase 1** of a wearable-AI research journey.
> It starts with accessible movement classification and builds toward
> physiological-signal-based anomaly prediction in later phases.

---

## 🎯 Goal

Use public IMU (Inertial Measurement Unit) data to classify human movement,
with a focus on detecting **abnormal movements such as falls**. The model is
then compressed so it can run real-time inference on a local edge device.

### Research Question

> Can abnormal movement be detected accurately even from a low-stigma wearing
> position (e.g. around the neck)?

Existing wearables face a trade-off between positions that give high accuracy
(waist, foot) and positions users actually feel comfortable wearing
(neck, wrist). This project explores that gap with data.

---

## 📚 What I'm Learning

| Area          | Specifically                                          |
| ------------- | ----------------------------------------------------- |
| Data          | Handling time-series sensor data, windowing           |
| Preprocessing | Filtering, normalization, labeling                    |
| Modeling      | Time-series classification (CNN/LSTM), PyTorch basics |
| Evaluation    | Train/test split, accuracy / precision / recall / F1  |
| Deployment    | ONNX compression, inference-speed measurement         |
| Research      | Framing open problems and forming hypotheses          |

---

## 🪜 Milestones (4 weeks)

- [ ] **Week 1** — Understand the data + run the full pipeline once (flow over accuracy)
- [ ] **Week 2** — Form-factor comparison (neck vs waist vs wrist)
- [ ] **Week 3** — Collect my own data via smartphone → test
- [ ] **Week 4** — Model compression + results write-up + documentation

---

## 🗂️ Project Structure

```
motion-fall-detection/
├── README.md
├── requirements.txt
├── .gitignore
├── data/              # datasets (not tracked by git)
│   └── raw/
├── notebooks/         # exploration & experiments
│   └── 01_explore_data.ipynb
├── src/               # core code
│   ├── data.py        # data loading & preprocessing
│   ├── model.py       # model definition
│   └── train.py       # training loop
└── outputs/           # models & results
```

---

## 📊 Datasets

| Dataset  | Purpose                   | Notes                                       |
| -------- | ------------------------- | ------------------------------------------- |
| UCI HAR  | Intro / pipeline practice | 6 activities, standard benchmark            |
| SisFall  | Fall detection            | Includes elderly subjects, video provided   |
| FallAllD | Form-factor comparison    | Neck, waist & wrist measured simultaneously |

---

## ⚙️ Setup

```bash
conda create -n motion python=3.11
conda activate motion
pip install -r requirements.txt
```

---

## 📈 Progress

> Updated as the project moves along.

- Current: environment setup & data exploration

---

_A personal research project for learning purposes._
