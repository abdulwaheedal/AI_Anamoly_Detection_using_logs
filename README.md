# AI-Based Anomaly Detection System for HDFS Logs

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abdulwaheedal/AI_Anamoly_Detection_using_logs/blob/main/Anomaly_Detection_System_HDFS.ipynb)

An **AI-powered unsupervised anomaly detection system** for large-scale HDFS logs using **Drain3 log parsing** and **Isolation Forest** with optimized threshold tuning.

---

## 🎯 Project Highlights

* **F1-Score:** 71.59%
* **Recall:** 81.14% — captures most anomalies
* **Precision:** 64.06%
* **11.1 Million logs processed**
* **45 log templates extracted**
* **575K HDFS blocks analyzed**

---

## 🧠 Final System Pipeline

```
Raw HDFS Logs
      ↓
Drain3 Log Parsing
      ↓
Template Extraction
      ↓
Feature Engineering (TF-IDF)
      ↓
Block-Level Aggregation
      ↓
Isolation Forest Model
      ↓
Dynamic Threshold Optimization
      ↓
Anomaly Prediction
      ↓
Visualization & Application Interface (app.py)
```

**Final Decision:**
The project uses the **earlier trained model** after evaluation showed better stability and performance compared to the live experimental model.

---

## 📥 Dataset Download

⚠️ Dataset must be downloaded before execution.

### HDFS Dataset (1.47 GB)

Download:
https://zenodo.org/record/3227177/files/HDFS_1.tar.gz

Source:
https://github.com/logpai/loghub

The notebook automatically extracts and preprocesses the dataset.

---

## 🚀 Quick Start

### Option 1 — Google Colab (Recommended)

1. Click **Open in Colab**
2. Run all cells sequentially
3. Outputs will be generated automatically

---

### Option 2 — Local Setup

#### 1. Clone Repository

```bash
git clone https://github.com/abdulwaheedal/AI_Anamoly_Detection_using_logs.git
cd AI_Anamoly_Detection_using_logs
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Download Dataset

```bash
wget https://zenodo.org/record/3227177/files/HDFS_1.tar.gz
tar -xvf HDFS_1.tar.gz
```

#### 4. Run Notebook

```bash
jupyter notebook Anomaly_Detection_System_HDFS.ipynb
```

#### 5. Run Application Interface

```bash
python app.py
```

---

## 📊 Repository Structure

```
AI_Anamoly_Detection_using_logs/
│
├── Anomaly_Detection_System_HDFS.ipynb   # Core ML pipeline
├── app.py                                # Application interface
├── requirements.txt                      # Dependencies
├── README.md
└── .gitignore
```

### Generated Automatically

* parsed_logs.csv
* block_features.csv
* anomaly_detection_results.csv
* PCA visualizations
* Performance reports

---

## 🛠️ Technologies Used

* Drain3 — Log template mining
* Scikit-learn — Isolation Forest, PCA, TF-IDF
* Pandas & NumPy — Data processing
* Matplotlib — Visualization
* Python — End-to-end implementation

---

## 📝 Methodology

1. **Log Parsing** — Drain3 extracts structured templates from raw logs
2. **Feature Engineering** — TF-IDF vectorization
3. **Anomaly Detection** — Isolation Forest model
4. **Threshold Optimization** — Precision-Recall based tuning
5. **Deployment Layer** — Application interface via `app.py`

---

## 📈 Performance Metrics

| Metric    | Score  |
| --------- | ------ |
| F1 Score  | 71.59% |
| Precision | 64.06% |
| Recall    | 81.14% |
| Accuracy  | 98.11% |

✅ Dynamic threshold optimization improves performance over fixed contamination models.

---

## 🎓 Use Cases

* Distributed system monitoring
* Log intelligence systems
* Predictive maintenance
* Cybersecurity anomaly detection

---

## 📚 References

* Drain3: https://github.com/logpai/Drain3
* LogHub Dataset: https://github.com/logpai/loghub
* Isolation Forest Paper: https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf

---

⭐ If you find this project useful, consider starring the repository!
