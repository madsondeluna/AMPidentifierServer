# AMPidentifier - Server

> The server component of the AMPidentifier project

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://madsondeluna.github.io/AMPidentifier)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![INPI](https://img.shields.io/badge/INPI-BR%2051%202025%20005859--4-green.svg)](https://www.gov.br/inpi)

```
////////////////////////////////////////////////////////////////////////
//                                                                    //
//                                                                    //
//      _    __  __ ____  _     _            _   _  __ _              //
//     / \  |  \/  |  _ \(_) __| | ___ _ __ | |_(_)/ _(_) ___ _ __    //
//    / _ \ | |\/| | |_) | |/ _` |/ _ \ '_ \| __| | |_| |/ _ \ '__|   //
//   / ___ \| |  | |  __/| | (_| |  __/ | | | |_| |  _| |  __/ |      //
//  /_/   \_\_|  |_|_|   |_|\__,_|\___|_| |_|\__|_|_| |_|\___|_|      //
//                                                                    //
//                                                                    //
////////////////////////////////////////////////////////////////////////

```

## Table of Contents

- [Overview](#overview)
- [Web Portal](#web-portal)
- [CLI Tool](#cli-tool)
- [Workflow](#workflow)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Performance Metrics](#performance-metrics)
- [Web Portal Details](#web-portal-details)
- [CLI Usage](#cli-usage)
- [Model Training](#model-training)
- [Project Structure](#project-structure)
- [Limitations and Next Steps](#limitations-and-next-steps)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Overview

AMPidentifier is a comprehensive toolkit for antimicrobial peptide (AMP) prediction, offering both a **command-line interface** for local analysis and a **web portal** for accessible, user-friendly interaction. The tool leverages ensemble machine learning (Random Forest, SVM, Gradient Boosting) to provide robust AMP classification with detailed physicochemical feature analysis.

### Key Capabilities

- **Ensemble Learning:** Majority voting across three ML models for robust predictions
- **Physicochemical Analysis:** Comprehensive feature extraction via modlamp library
- **Dual Interface:** CLI for batch processing + Web portal for interactive use
- **Open Source:** Fully transparent, modular architecture
- **High Performance:** 87.47% accuracy in ensemble mode, 88.45% with Random Forest
- **Flexible Deployment:** Local execution or cloud-based API

---

## Web Portal

**Live Demo:** https://madsondeluna.github.io/AMPidentifier

A minimalist, responsive web interface featuring:

- Modern liquid glass design aesthetic
- Interactive FASTA sequence input
- Real-time model selection (RF/SVM/GB/Ensemble)
- Tabular results display with CSV export
- Comprehensive project documentation

### Current Status

**Available:**
- Static frontend deployed on GitHub Pages
- Demo mode with mock data
- Full UI/UX functionality
- Responsive design (mobile/tablet/desktop)

**In Development:**
- Backend API for real predictions
- File upload functionality
- Prediction history
- User authentication

See [Web Portal Details](#web-portal-details) for technical specifications.

---

## CLI Tool

Full-featured command-line interface for local AMP prediction:

```bash
python3 main.py --input sequences.fasta --output_dir ./results --ensemble
```

**Features:**
- Batch processing of FASTA files
- Single model or ensemble mode
- External model integration (.pkl files)
- Comprehensive CSV reports
- Physicochemical feature extraction

See [CLI Usage](#cli-usage) for detailed documentation.

---

## Workflow

![AMPidentifier Workflow](img/workflow.svg)


### Workflow Steps

1. **Input:** FASTA-formatted amino acid sequences
2. **Feature Extraction:** Compute physicochemical descriptors using modlamp
3. **Normalization:** Apply StandardScaler transformation
4. **Model Inference:** Execute selected model(s) on normalized features
5. **Ensemble Voting:** Combine predictions via majority vote (if enabled)
6. **Output Generation:** Export predictions and features to CSV

---

## Technology Stack

### Core Technologies

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Runtime** | Python | 3.8+ | Core language |
| **ML Framework** | scikit-learn | 1.3.0 | Model training and inference |
| **Feature Extraction** | modlamp | 4.3.0 | Physicochemical descriptors |
| **Data Processing** | pandas | 2.1.0 | Data manipulation |
| **Numerical Computing** | NumPy | 1.24.0 | Array operations |

### Web Portal Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | HTML5/CSS3/JavaScript | User interface |
| **Styling** | Custom CSS (Vanilla) | Liquid glass design system |
| **Typography** | Google Fonts (Inter) | Professional typeface |
| **Backend** | Flask 3.0.0 | API server (not deployed) |
| **Hosting** | GitHub Pages | Static site hosting |

### Machine Learning Models

| Model | Algorithm | Accuracy | Use Case |
|-------|-----------|----------|----------|
| **RF** | Random Forest | 88.45% | Best single-model performance |
| **SVM** | Support Vector Machine | 87.40% | High precision |
| **GB** | Gradient Boosting | 85.85% | Good generalization |
| **Ensemble** | Majority Voting | 87.47% | Recommended for production |

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

1. **Clone Repository:**
   ```bash
   git clone https://github.com/madsondeluna/AMPidentifier.git
   cd AMPidentifier
   ```

2. **Create Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation:**
   ```bash
   python3 main.py --help
   ```

---

## Quick Start

### CLI Quick Test

Run a prediction using sample data:

```bash
python3 main.py --input data-for-tests/sequences_to_predict.fasta --output_dir ./test_results --ensemble
```

**Expected Output:**
```
test_results/
├── physicochemical_features.csv
└── prediction_comparison_report.csv
```

### Web Portal Quick Test

1. **Local Development Server:**
   ```bash
   cd web_portal
   python3 -m http.server 8080
   ```

2. **Access:** http://localhost:8080

3. **Test Prediction:**
   - Click "Carregar Exemplo"
   - Select "Ensemble" model
   - Click "Executar Predição"
   - View demo results

---

## Performance Metrics

### Individual Model Performance

| Metric | Random Forest | SVM | Gradient Boosting |
|--------|--------------|-----|-------------------|
| **Accuracy** | **88.45%** | 87.40% | 85.85% |
| **Precision** | **89.10%** | 88.80% | 86.65% |
| **Recall** | **87.62%** | 85.58% | 84.75% |
| **Specificity** | **89.28%** | 89.21% | 86.94% |
| **F1-Score** | **88.36%** | 87.16% | 85.69% |
| **MCC** | **0.7692** | 0.7484 | 0.7172 |
| **AUC-ROC** | **0.9503** | 0.9356 | 0.9289 |

### Ensemble Mode Performance

**Confusion Matrix:**

|  | Predicted: Negative | Predicted: Positive | Total |
|---|---------------------|---------------------|-------|
| **Actual: Negative** | TN = 1179 (88.98%) | FP = 146 (11.02%) | 1325 |
| **Actual: Positive** | FN = 186 (14.04%) | TP = 1139 (85.96%) | 1325 |
| **Total** | 1365 | 1285 | **2650** |

**Metrics:**
- **Accuracy:** 87.47%
- **Sensitivity (Recall):** 85.96%
- **Specificity:** 88.98%

**Recommendation:** Use Ensemble mode for production deployments.

---

## Web Portal Details

### Architecture

**Current (Static Frontend):**
```
GitHub Pages → HTML/CSS/JS → Mock Data
```

**Target (Full Stack):**
```
GitHub Pages (Frontend) ←→ Render.com (Flask API) ←→ AMPidentifier Core
```

### Technology Details

**Frontend:**
- **HTML5:** Semantic markup, accessibility features
- **CSS3:** 600+ lines, custom properties, glassmorphism effects
- **JavaScript:** ES6+, async/await, fetch API
- **Design:** Mobile-first, responsive (320px - 2560px)

**Backend (Not Deployed):**
- **Framework:** Flask 3.0.0
- **API Endpoints:**
  - `POST /api/predict` - Execute prediction
  - `POST /api/download/<type>` - Download results
- **CORS:** Configured for GitHub Pages origin
- **Processing:** Async job queue (planned)

### Features

**Available:**
- Interactive FASTA input with validation
- Model selection dropdown (RF/SVM/GB/Ensemble)
- Example data loading
- Results display in tabular format
- CSV export functionality
- Responsive navigation
- Error handling and user feedback

**Planned:**
- File upload (drag-and-drop)
- Batch processing
- Prediction history (localStorage)
- PDF export
- User authentication
- API rate limiting

### Limitations

1. **Static Hosting:** GitHub Pages cannot execute Python code
2. **No Backend:** Requires external API for real predictions
3. **Demo Mode:** Currently shows mock data only
4. **No Persistence:** No database or session storage
5. **CORS:** Cross-origin requests require proper configuration

### Deployment

**Frontend (Live):**
```bash
# Automatic deployment via GitHub Actions
git push origin main
# Live at: https://madsondeluna.github.io/AMPidentifier
```

**Backend (Manual - Not Configured):**

Option 1: Render.com
```yaml
Build: pip install -r web_portal/requirements.txt
Start: cd web_portal && gunicorn app:app
```

Option 2: Heroku
```bash
heroku create ampidentifier-api
git push heroku main
```

See `web_portal/DEPLOY.md` for detailed instructions.

---

## CLI Usage

### Basic Usage

```bash
python3 main.py --input <fasta_file> --output_dir <output_directory> [options]
```

### Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `-i, --input` | str | Yes | - | Path to input FASTA file |
| `-o, --output_dir` | str | Yes | - | Output directory path |
| `-m, --model` | str | No | `rf` | Model choice: `rf`, `svm`, `gb` |
| `--ensemble` | flag | No | False | Enable ensemble mode |
| `-e, --external_models` | str | No | - | Comma-separated paths to external .pkl models |

### Examples

**Single Model (Random Forest):**
```bash
python3 main.py --input sequences.fasta --output_dir ./results_rf
```

**Ensemble Mode (Recommended):**
```bash
python3 main.py --input sequences.fasta --output_dir ./results_ensemble --ensemble
```

**With External Model:**
```bash
python3 main.py --input sequences.fasta --output_dir ./results_comparison --model svm --external_models /path/to/custom_model.pkl
```

### Output Files

**1. `physicochemical_features.csv`**

Contains computed descriptors for each sequence:
- Sequence ID and amino acid sequence
- Hydrophobicity indices
- Charge and isoelectric point (pI)
- Aromaticity and aliphatic index
- Molecular weight and GRAVY score
- Secondary structure predictions
- 40+ additional features

**2. `prediction_comparison_report.csv`**

Contains prediction results:
- Sequence ID
- AMP classification (0 = Non-AMP, 1 = AMP)
- Individual model predictions (if ensemble)
- Confidence scores
- Ensemble vote (if applicable)

---

## Model Training

### Training Your Own Models

The `model_training/` directory contains scripts for custom model training:

```bash
cd model_training
python3 train.py
```

**Training Pipeline:**

1. **Data Preparation:**
   - Positive sequences: `data/positive_sequences.fasta`
   - Negative sequences: `data/negative_sequences.fasta`

2. **Feature Extraction:**
   - Compute physicochemical descriptors
   - Apply StandardScaler normalization

3. **Model Training:**
   - Train RF, SVM, and GB models
   - 80/20 train-test split
   - Cross-validation for hyperparameter tuning

4. **Evaluation:**
   - Generate performance metrics
   - Create confusion matrices
   - Export evaluation reports

**Output:**
```
model_training/saved_model/
├── amp_model_rf.pkl
├── amp_model_svm.pkl
├── amp_model_gb.pkl
├── feature_scaler.pkl
├── evaluation_report.txt
└── evaluation_report.csv
```

### Model Evaluation

```bash
python3 model_training/evaluate.py
```

Generates comprehensive metrics:
- Accuracy, Precision, Recall
- Specificity, F1-Score, MCC
- AUC-ROC curves
- Confusion matrices

---

## Project Structure

```
AMPidentifier/
├── README.md                      # This file
├── LICENSE                        # Software license
├── requirements.txt               # Python dependencies
├── main.py                        # CLI entry point
│
├── amp_identifier/                # Core library
│   ├── __init__.py
│   ├── core.py                    # Main prediction workflow
│   ├── data_io.py                 # FASTA file handling
│   ├── feature_extraction.py     # Physicochemical descriptors
│   ├── prediction.py              # Model inference
│   └── reporting.py               # CSV report generation
│
├── model_training/                # Model training pipeline
│   ├── train.py                   # Training script
│   ├── evaluate.py                # Evaluation script
│   ├── data/                      # Training datasets
│   │   ├── positive_sequences.fasta
│   │   └── negative_sequences.fasta
│   └── saved_model/               # Trained models
│       ├── amp_model_rf.pkl
│       ├── amp_model_svm.pkl
│       ├── amp_model_gb.pkl
│       └── feature_scaler.pkl
│
├── web_portal/                    # Web interface
│   ├── README.md                  # Web portal documentation
│   ├── DEPLOY.md                  # Deployment guide
│   ├── app.py                     # Flask backend
│   ├── requirements.txt           # Web dependencies
│   ├── index.html                 # Homepage
│   ├── predict.html               # Prediction interface
│   ├── about.html                 # About page
│   └── static/
│       ├── css/
│       │   └── style.css          # Design system (600+ lines)
│       └── js/
│           └── main.js            # Client-side logic (300+ lines)
│
├── data-for-tests/                # Example data
│   ├── sequences_to_predict.fasta
│   └── results_ensemble/
│
├── benchmarking/                  # Benchmark datasets
│   └── base/
│       ├── bacterial_pos.fasta
│       ├── bacterial_neg.fasta
│       ├── fungal_pos.fasta
│       ├── fungal_neg.fasta
│       ├── viral_pos.fasta
│       └── viral_neg.fasta
│
├── img/                           # Documentation images
│   ├── workflow.svg               # Pipeline diagram
│   └── logo-use2.png
│
├── normalization-info/            # Normalization documentation
│   ├── README.md
│   ├── normalization_impact_report.md
│   └── resumo_normalizacao.md
│
└── tests/                         # Unit tests
    ├── __init__.py
    └── test_prediction.py
```

### Code Statistics

- **Total Lines:** ~8,000+
- **Python Code:** ~3,500 lines
- **Web Code:** ~1,800 lines (HTML/CSS/JS)
- **Documentation:** ~2,700 lines
- **Languages:** Python (60%), HTML/CSS/JS (25%), Markdown (15%)

---

## Limitations and Next Steps

### Current Limitations

**Technical:**
1. Web portal requires external API for real predictions
2. GitHub Pages cannot execute server-side code
3. No user authentication or session management
4. Limited to single-sequence processing in web interface
5. No caching mechanism for repeated predictions

**Functional:**
6. No batch file upload in web portal
7. No prediction history persistence
8. No email notifications
9. No API rate limiting
10. No asynchronous job processing

### Next Steps

**Phase 1: Backend Deployment (Priority: High)**

- [ ] Deploy Flask API to Render.com or Heroku
- [ ] Configure CORS for cross-origin requests
- [ ] Update frontend API endpoint
- [ ] Implement error handling and retry logic
- [ ] Add request validation and sanitization

**Complexity:** Medium

**Phase 2: Enhanced Functionality (Priority: Medium)**

- [ ] File upload with drag-and-drop
- [ ] Batch processing support
- [ ] Prediction history (localStorage)
- [ ] PDF export functionality
- [ ] Progress indicators for long predictions
- [ ] Input validation and error messages

**Complexity:** Medium

**Phase 3: Advanced Features (Priority: Low)**

- [ ] User authentication (OAuth/JWT)
- [ ] Database integration (PostgreSQL)
- [ ] Persistent prediction history
- [ ] API rate limiting (Redis)
- [ ] Asynchronous job queue (Celery)
- [ ] Email notifications
- [ ] Admin dashboard
 
**Complexity:** High

**Phase 4: Optimization (Priority: Ongoing)**

- [ ] Performance profiling and optimization
- [ ] Lighthouse audit (score > 90)
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] SEO optimization
- [ ] Analytics integration
- [ ] Error tracking (Sentry)
- [ ] API documentation (Swagger/OpenAPI)

**Complexity:** Low

---

## Contributing

Contributions are welcome! Please follow these guidelines:

### Reporting Issues

**Bug Reports:**
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Error messages and logs

**Feature Requests:**
- Use case description
- Proposed solution
- Alternative approaches
- Additional context

### Development Workflow

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes with clear commits
4. Add tests for new functionality
5. Update documentation
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open Pull Request

### Code Style

- **Python:** PEP 8, type hints, docstrings
- **HTML:** Semantic markup, accessibility
- **CSS:** BEM-inspired naming, mobile-first
- **JavaScript:** ES6+, JSDoc comments
- **Commits:** Conventional commits format

---

## Citation

If you use AMPidentifier in your research, please cite:

```bibtex
@software{ampidentifier2025,
  author = {Luna-Aragão, Madson A. and da Silva, Rafael L. and Pacífico, João and Santos-Silva, Carlos A. and Benko-Iseppon, Ana M.},
  title = {AMPidentifier: A Python toolkit for predicting antimicrobial peptides using ensemble machine learning and physicochemical descriptors},
  year = {2025},
  url = {https://github.com/madsondeluna/AMPidentifier},
  note = {Software registered at INPI Brazil, BR 51 2025 005859-4}
}
```

---

## License

This software is officially registered with **INPI** (Instituto Nacional da Propriedade Industrial - Brazil).

**Registration Number:** BR 51 2025 005859-4  
**Registration Date:** November 18, 2025  
**Registered Authors:** Madson A. de Luna Aragão, Rafael L. da Silva, João Pacífico, Carlos A. dos Santos-Silva, Ana M. Benko-Iseppon

**Copyright © 2025** - All rights reserved.

**Institutional Holder:** UFPE (Universidade Federal de Pernambuco, Brazil)

---

## Acknowledgments

**Funding:**
- FACEPE (Fundação de Amparo à Pesquisa do Estado de Pernambuco, Brazil)

**Institutional Support:**
- PPGGBM (Programa de Pós-Graduação em Genética e Biologia Molecular, UFPE)
- UFMG (Universidade Federal de Minas Gerais)

**Contributors:**

| Name | Role | Institution |
|------|------|-------------|
| Madson A. de Luna Aragão, MSc | Lead Developer | UFMG |
| Rafael L. da Silva, BSc | Collaborator | UFPE |
| Ana M. Benko-Iseppon, PhD | Advisor | UFPE |
| João Pacífico, PhD | Co-Advisor | UPE |
| Carlos A. dos Santos-Silva, PhD | Co-Advisor | CESMAC |

---

## Contact

**Lead Developer:** Madson A. de Luna Aragão  
**Email:** madsondeluna@gmail.com  
**Institution:** UFMG - Belo Horizonte, MG, Brazil  
**GitHub:** [@madsondeluna](https://github.com/madsondeluna)

**Project Links:**
- **Web Portal:** https://madsondeluna.github.io/AMPidentifier
- **Repository:** https://github.com/madsondeluna/AMPidentifier
- **Issues:** https://github.com/madsondeluna/AMPidentifier/issues
- **Discussions:** https://github.com/madsondeluna/AMPidentifier/discussions

---

**Version:** 1.0.0  
**Last Updated:** December 2025  
**Status:** Production (CLI) | Beta (Web Portal)
