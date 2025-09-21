# Video Emotion Classification

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Competition](https://img.shields.io/badge/Competition-Satria%20Data%202025-green.svg)](https://satriadata.kemdikbud.go.id/)

A machine learning project for classifying human emotions from video content, developed for the **Satria Data 2025 (Big Data Challenge)** competition.

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Features](#features)
- [Usage](#usage)
- [Models & Methodology](#models--methodology)
- [Results](#results)
- [Team](#team)
- [License](#license)

## 🎯 Overview

This project focuses on **emotion classification from video content** using machine learning techniques. The goal is to automatically classify human emotions into 8 distinct categories based on video data from Instagram reels.

### Key Objectives

- Develop robust emotion classification models
- Handle multimodal data (video, audio, text)
- Achieve high accuracy on emotion recognition
- Create reproducible and scalable solutions

## 📊 Dataset

### Data Source

- **Competition**: Satria Data 2025 (Big Data Challenge)
- **Domain**: Human emotion analysis
- **Format**: CSV files with video URLs and emotion labels
- **Total Records**: 803 training samples + 201 test samples

### Emotion Categories

| Label | Emotion  | Description                        |
| ----- | -------- | ---------------------------------- |
| 0     | Proud    | Pride, achievement, accomplishment |
| 1     | Trust    | Trust, confidence, security        |
| 2     | Joy      | Happiness, joy, laughter           |
| 3     | Surprise | Shock, surprise, unexpected        |
| 4     | Neutral  | Neutral, calm, indifferent         |
| 5     | Sadness  | Sadness, grief, melancholy         |
| 6     | Fear     | Fear, anxiety, worry               |
| 7     | Anger    | Anger, frustration, rage           |

### Data Distribution

- **Surprise**: ~50% (most frequent)
- **Trust**: ~20% (common)
- **Proud**: ~15% (common)
- **Others**: Joy, Anger, Sadness, Fear, Neutral (less frequent)

## 📁 Project Structure

```
project/
├── 📊 data/
│   ├── datatrain.csv              # Training dataset
│   ├── datatest.csv               # Test dataset
│   ├── final_datatrain.csv        # Processed training data
│   ├── final_datatest.csv         # Processed test data
│   ├── submission_*.csv           # Model predictions
│   ├── train/                     # Training media files
│   │   ├── audio/                 # Audio files
│   │   ├── text/                  # Text transcriptions
│   │   └── video/                 # Video files
│   └── test/                      # Test media files
│       ├── audio/
│       ├── text/
│       └── video/
├── 📓 main.ipynb                  # Main analysis notebook
├── 📓 labelisasi.ipynb            # Data labeling notebook
├── 📓 analisis-submission.ipynb   # Submission analysis
├── 🤖 catboost_info/             # CatBoost model artifacts
├── 📄 LICENSE                     # MIT License
└── 📖 README.md                   # This file
```

## ✨ Features

### Data Processing

- **Multimodal Feature Extraction**: Audio, video, and text features
- **Data Cleaning**: Handle missing values and inconsistent formats
- **Feature Engineering**: Advanced feature extraction from multimedia content
- **Label Encoding**: Emotion mapping and preprocessing

### Machine Learning

- **Multiple Models**: CatBoost, ensemble methods
- **Cross-Validation**: Robust model evaluation
- **Hyperparameter Tuning**: Optimized model performance
- **Feature Selection**: Automated feature importance analysis

### Analysis Tools

- **Exploratory Data Analysis**: Comprehensive dataset insights
- **Visualization**: Emotion distribution and model performance plots
- **Model Comparison**: Performance benchmarking
- **Submission Analysis**: Results evaluation and comparison

## 💻 Usage

### Quick Start

1. **Open the main notebook**

   ```bash
   jupyter notebook main.ipynb
   ```

2. **Run data analysis**

   - Execute cells sequentially
   - Follow the structured analysis workflow
   - Review data insights and visualizations

3. **Train models**

   - Run model training sections
   - Compare different algorithms
   - Evaluate performance metrics

### Notebooks Overview

- **`main.ipynb`**: Complete analysis pipeline

  - Data understanding and exploration
  - Feature engineering
  - Model training and evaluation
  - Results visualization

- **`labelisasi.ipynb`**: Data labeling workflow

  - Automated emotion labeling using AI
  - Label quality assurance
  - Data preprocessing

- **`analisis-submission.ipynb`**: Submission analysis
  - Model performance comparison
  - Error analysis
  - Submission file generation

## 🧠 Models & Methodology

### Approach

1. **Feature Extraction**

   - Audio features (MFCC, spectral features)
   - Visual features (facial expressions, scene analysis)
   - Text features (sentiment, linguistic patterns)

2. **Model Development**

   - Gradient boosting (CatBoost primary)
   - Ensemble methods
   - Cross-validation for robustness

3. **Evaluation Metrics**
   - Accuracy
   - F1-score (macro/weighted)
   - Confusion matrix analysis
   - Per-class performance

### Best Practices

- **Data Preprocessing**: Standardization and normalization
- **Feature Selection**: Importance-based filtering
- **Model Validation**: Stratified cross-validation
- **Hyperparameter Optimization**: Grid search and Bayesian optimization

## 📈 Results

### Model Performance

- **Best Model**: Ensemble (Voting Classifier)
- **Validation Accuracy**: 41%
- **F1-Score**: 0.254
- **Top Predictions**: Surprise, Trust, Proud (aligned with data distribution)

### Key Insights

- Surprise is the most predictable emotion (high frequency)
- Trust and Proud show distinct patterns
- Minority classes require careful handling
- Multimodal features improve performance

## 👥 Team

**Team Name**: "Ihre einzige grenze ist ihr verstand"

### Contributors

- **Harry Mardika** - Project Lead & Data Scientist
  - Model development and optimization
  - Feature engineering
  - Repository maintenance

### Acknowledgments

- Satria Data 2025 Competition organizers
- Kemdikbud for hosting the competition
- Open source community for tools and libraries

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Harry Mardika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```