

# Next Word Prediction Model

Deep Learning based Next Word Prediction system built using LSTM networks and trained on Shakespeare’s *Hamlet* dataset.

This project demonstrates sequence modeling, NLP preprocessing, and language generation using TensorFlow & Keras.

---

## 🚀 Project Overview

This model predicts the most probable next word given a sequence of input text.

It showcases:

- Natural Language Processing (Tokenization, Sequence Generation)
- Stacked LSTM Architecture
- Overfitting control using Dropout & EarlyStopping
- Model saving & inference pipeline

---

## 🧠 Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Pickle
- Jupyter Notebook

---

## 📊 Model Architecture

- Embedding Layer
- Stacked LSTM Layers
- Dropout Regularization
- Dense Softmax Output Layer

The model is trained using categorical crossentropy and optimized with Adam.

---

## 📁 Repository Structure

```

├── training.ipynb        # Model training notebook
├── app.py                # Inference / prediction script
├── hamlet.txt            # Training dataset
├── lstm.h5               # Trained model
├── tokenizer.pickle      # Saved tokenizer
├── requirements.txt      # Dependencies

```

---

## ▶️ How to Run

1. Clone the repository
```

git clone [https://github.com/yeripallivijay/Next-Word-Prediction-Model.git](https://github.com/yeripallivijay/Next-Word-Prediction-Model.git)

```

2. Install dependencies
```

pip install -r requirements.txt

```

3. Run prediction script
```

python app.py

```

---

## 📈 Results

- Achieved strong training convergence on literary dataset
- Implemented EarlyStopping to prevent overfitting
- Successfully generates context-aware next-word predictions

---

## 🎯 Key Learnings

- Sequence modeling using LSTM
- Handling overfitting in small NLP datasets
- Vocabulary management & softmax scaling challenges
- Practical deployment-ready NLP pipeline

---

## 👤 Author

Vijay Arjun  
Aspiring Data Scientist | Deep Learning & NLP Enthusiast
```

