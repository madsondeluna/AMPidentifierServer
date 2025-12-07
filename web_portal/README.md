# AMPidentifier Web Portal

> A modern, minimalist web interface for antimicrobial peptide prediction using ensemble machine learning

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://madsondeluna.github.io/AMPidentifier)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Table of Contents

- [Overview](#overview)
- [Current Status](#current-status)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Features](#features)
- [Limitations](#limitations)
- [Deployment](#deployment)
- [Next Steps](#next-steps)
- [Local Development](#local-development)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The AMPidentifier Web Portal is a static frontend interface for the AMPidentifier tool, designed to provide an accessible, user-friendly way to interact with antimicrobial peptide prediction models. The portal features a minimalist design with liquid glass aesthetics and is currently deployed on GitHub Pages.

**Live URL:** https://madsondeluna.github.io/AMPidentifier

### Workflow Diagram

The AMPidentifier tool follows a modular pipeline architecture:

![AMPidentifier Workflow](../img/workflow.svg)

**Pipeline Steps:**

1. **Input:** FASTA-formatted amino acid sequences
2. **Feature Extraction:** Physicochemical descriptors via `modlamp` library
3. **Normalization:** StandardScaler transformation
4. **Model Selection:** Single model (RF/SVM/GB) or Ensemble mode
5. **Prediction:** AMP vs Non-AMP classification
6. **Output:** Prediction report + feature matrix (CSV format)

---

## Current Status

### What's Available

- **Static Frontend:** Fully functional HTML/CSS/JavaScript interface
- **Design System:** Minimalist liquid glass aesthetic with subtle animations
- **UI Components:**
  - Homepage with feature overview and performance metrics
  - Prediction interface with FASTA input and model selection
  - About page with comprehensive project information
- **Demo Mode:** Mock data demonstration for UI/UX testing
- **Responsive Design:** Mobile, tablet, and desktop compatibility

### What's Missing

- **Backend API:** No server-side processing capability
- **Real Predictions:** Cannot execute actual ML model inference
- **Database:** No storage for prediction history
- **User Authentication:** No user accounts or session management
- **File Upload:** Limited to text input (no file upload functionality)

---

## Technology Stack

### Frontend

| Technology | Version | Purpose |
|-----------|---------|---------|
| **HTML5** | - | Semantic markup and structure |
| **CSS3** | - | Styling with custom properties and glassmorphism effects |
| **JavaScript (ES6+)** | - | Client-side interactivity and DOM manipulation |
| **Google Fonts** | - | Inter typeface for typography |

**Design Patterns:**
- CSS Custom Properties for design tokens
- BEM-inspired class naming
- Mobile-first responsive design
- Progressive enhancement

### Backend (Not Deployed)

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.8+ | Server runtime |
| **Flask** | 3.0.0 | Web framework |
| **pandas** | 2.1.0 | Data manipulation |
| **scikit-learn** | 1.3.0 | ML model loading |
| **modlamp** | 4.3.0 | Physicochemical feature extraction |

### Deployment

| Platform | Purpose | Status |
|----------|---------|--------|
| **GitHub Pages** | Static hosting | Active |
| **Render.com** | Backend API (planned) | Not configured |

---

## Architecture

### Current Architecture (Static Only)

```
┌─────────────────────────────────────────┐
│         GitHub Pages (Static)           │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   HTML/CSS/JS Frontend          │   │
│  │   - index.html                  │   │
│  │   - predict.html                │   │
│  │   - about.html                  │   │
│  │   - static/css/style.css        │   │
│  │   - static/js/main.js           │   │
│  └─────────────────────────────────┘   │
│              │                          │
│              ▼                          │
│      Mock Data (Demo Mode)             │
└─────────────────────────────────────────┘
```

### Target Architecture (Full Stack)

```
┌──────────────────┐         ┌──────────────────────┐
│  GitHub Pages    │         │   Render.com/Heroku  │
│  (Static)        │         │   (Backend API)      │
│                  │         │                      │
│  Frontend        │  HTTPS  │  Flask Application   │
│  HTML/CSS/JS     │◄───────►│  - app.py            │
│                  │  CORS   │  - API endpoints     │
└──────────────────┘         │                      │
                             │  ┌────────────────┐  │
                             │  │ AMPidentifier  │  │
                             │  │ Core Library   │  │
                             │  │ - RF Model     │  │
                             │  │ - SVM Model    │  │
                             │  │ - GB Model     │  │
                             │  │ - Scaler       │  │
                             │  └────────────────┘  │
                             └──────────────────────┘
```

---

## Features

### User Interface

- **Minimalist Design:** Clean, professional aesthetic with subtle glassmorphism effects
- **Responsive Layout:** Optimized for all screen sizes (320px - 2560px)
- **Accessibility:** Semantic HTML, ARIA labels, keyboard navigation support
- **Performance:** Optimized CSS with minimal JavaScript overhead

### Functionality (Demo Mode)

- **FASTA Input:** Text area for sequence submission
- **Model Selection:** Dropdown for RF, SVM, GB, or Ensemble mode
- **Example Data:** Pre-loaded sample sequences
- **Results Display:** Tabular presentation of predictions and features
- **CSV Export:** Download functionality for results

### Design System

**Color Palette:**
- Primary: `#667eea` → `#764ba2` (gradient)
- Success: `#43e97b` → `#38f9d7` (gradient)
- Background: `#0a0a0f` (dark mode)
- Glass effect: `rgba(255, 255, 255, 0.05)` with 20px blur

**Typography:**
- Font Family: Inter (Google Fonts)
- Base Size: 16px
- Scale: Fluid typography with `clamp()`

**Spacing:**
- Base unit: 1rem (16px)
- Scale: 0.5rem, 1rem, 1.5rem, 2rem, 3rem, 4rem

---

## Limitations

### Technical Constraints

1. **Static Hosting Limitation**
   - GitHub Pages only serves static files
   - No server-side code execution
   - No Python/Flask backend support
   - Cannot run ML model inference

2. **API Dependency**
   - Requires external API for real predictions
   - CORS configuration needed for cross-origin requests
   - Additional infrastructure cost for API hosting

3. **Performance**
   - Large model files (>100MB) cannot be served from GitHub Pages
   - Feature extraction requires server-side processing
   - No caching mechanism for repeated predictions

4. **Security**
   - No authentication or authorization
   - No rate limiting
   - No input sanitization on server side
   - Public API endpoint (if deployed) vulnerable to abuse

5. **Functionality**
   - No prediction history
   - No batch processing
   - No user accounts
   - Limited to demo mode without backend

### Browser Compatibility

- Modern browsers only (ES6+ support required)
- No Internet Explorer support
- Requires JavaScript enabled
- CSS backdrop-filter support needed for glass effects

---

## Deployment

### Current Deployment (GitHub Pages)

The static frontend is deployed at: https://madsondeluna.github.io/AMPidentifier

**Deployment Process:**

1. Push changes to `main` branch
2. GitHub Actions automatically builds and deploys
3. Changes live within 1-3 minutes

**Files Deployed:**
```
AMPidentifier/
├── index.html
├── predict.html
├── about.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

### Backend Deployment (Not Configured)

To enable real predictions, deploy the Flask backend separately:

**Option 1: Render.com (Recommended)**

1. Create account at https://render.com
2. Create new Web Service
3. Connect GitHub repository
4. Configure:
   ```yaml
   Build Command: pip install -r web_portal/requirements.txt
   Start Command: cd web_portal && gunicorn app:app
   Environment: Python 3
   ```
5. Set environment variables (if needed)
6. Deploy

**Option 2: Heroku**

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: cd web_portal && gunicorn app:app
   ```
3. Deploy:
   ```bash
   heroku create ampidentifier-api
   git push heroku main
   ```

**Option 3: Railway.app**

1. Connect repository at https://railway.app
2. Configure root directory: `web_portal`
3. Auto-deploy on push

**CORS Configuration:**

After deploying backend, update `predict.html`:

```javascript
const API_URL = 'https://your-api.onrender.com/api/predict';
```

And enable CORS in `app.py`:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['https://madsondeluna.github.io'])
```

---

## Next Steps

### Phase 1: Backend Deployment (High Priority)

- [ ] Deploy Flask API to Render.com or Heroku
- [ ] Configure CORS for GitHub Pages origin
- [ ] Update frontend API endpoint URL
- [ ] Test end-to-end prediction workflow
- [ ] Add error handling and retry logic

**Estimated Time:** 2-4 hours  
**Complexity:** Medium  
**Dependencies:** None

### Phase 2: Enhanced Functionality (Medium Priority)

- [ ] Implement file upload for FASTA files
- [ ] Add batch processing support (multiple files)
- [ ] Create prediction history (localStorage)
- [ ] Add export to PDF functionality
- [ ] Implement progress indicators for long-running predictions

**Estimated Time:** 8-12 hours  
**Complexity:** Medium  
**Dependencies:** Phase 1 complete

### Phase 3: Advanced Features (Low Priority)

- [ ] User authentication (OAuth or JWT)
- [ ] Database integration (PostgreSQL)
- [ ] Prediction history persistence
- [ ] API rate limiting
- [ ] Caching layer (Redis)
- [ ] Asynchronous job queue (Celery)
- [ ] Email notifications for completed predictions

**Estimated Time:** 20-30 hours  
**Complexity:** High  
**Dependencies:** Phase 1 & 2 complete

### Phase 4: Optimization (Ongoing)

- [ ] Performance profiling
- [ ] Lighthouse audit and optimization
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] SEO optimization
- [ ] Analytics integration (Google Analytics)
- [ ] Error tracking (Sentry)

**Estimated Time:** 4-6 hours  
**Complexity:** Low  
**Dependencies:** None

---

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Modern web browser
- Git

### Setup

1. **Clone Repository:**
   ```bash
   git clone https://github.com/madsondeluna/AMPidentifier.git
   cd AMPidentifier/web_portal
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Development Server:**

   **Option A: Static Server (Frontend Only)**
   ```bash
   python3 -m http.server 8080
   ```
   Access at: http://localhost:8080

   **Option B: Flask Server (Full Stack)**
   ```bash
   python3 app.py
   ```
   Access at: http://localhost:5000

### Development Workflow

1. Make changes to HTML/CSS/JS files
2. Refresh browser to see changes (no build step required)
3. For Flask changes, restart server
4. Test in multiple browsers
5. Commit and push to GitHub

### Testing

**Manual Testing Checklist:**

- [ ] Homepage loads correctly
- [ ] Navigation works between pages
- [ ] FASTA input accepts text
- [ ] Example data loads
- [ ] Model selection dropdown works
- [ ] Submit button triggers prediction
- [ ] Results display correctly
- [ ] CSV download works
- [ ] Responsive design on mobile
- [ ] Glass effects render properly

**Browser Testing:**

- Chrome/Edge (Chromium)
- Firefox
- Safari
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## Project Structure

```
web_portal/
├── README.md                 # This file
├── DEPLOY.md                 # Deployment guide
├── QUICKSTART.md             # Quick start guide
├── app.py                    # Flask backend (not deployed)
├── requirements.txt          # Python dependencies
│
├── index.html                # Homepage
├── predict.html              # Prediction interface
├── about.html                # About page
│
└── static/
    ├── css/
    │   └── style.css         # Main stylesheet (600+ lines)
    └── js/
        └── main.js           # Client-side logic (300+ lines)
```

### File Descriptions

| File | Lines | Purpose |
|------|-------|---------|
| `index.html` | ~150 | Homepage with features and metrics |
| `predict.html` | ~260 | Prediction interface and results |
| `about.html` | ~320 | Project information and team |
| `style.css` | ~600 | Complete design system |
| `main.js` | ~300 | Interactivity and API calls |
| `app.py` | ~150 | Flask API endpoints |

### Code Statistics

- **Total Lines:** ~1,780
- **Languages:** HTML (43%), CSS (34%), JavaScript (17%), Python (6%)
- **Files:** 8 core files
- **Dependencies:** 6 Python packages

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- **HTML:** Semantic, accessible markup
- **CSS:** BEM-inspired naming, mobile-first
- **JavaScript:** ES6+, functional style, JSDoc comments
- **Python:** PEP 8, type hints, docstrings

### Commit Messages

Follow conventional commits:

```
feat: add batch processing support
fix: resolve CORS issue with API
docs: update deployment guide
style: improve button hover effects
refactor: simplify prediction logic
test: add unit tests for API
```

---

## License

This project is part of the AMPidentifier toolkit and follows the same license terms.

**Copyright © 2025 Madson A. de Luna Aragão**

**Registration:** BR 51 2025 005859-4 (INPI - Brazil)

---

## Citation

If you use this web portal in your research, please cite:

```bibtex
@software{ampidentifier_portal_2025,
  author = {Luna-Aragão, Madson A. and da Silva, Rafael L. and Pacífico, João and Santos-Silva, Carlos A. and Benko-Iseppon, Ana M.},
  title = {AMPidentifier Web Portal: A minimalist interface for antimicrobial peptide prediction},
  year = {2025},
  url = {https://madsondeluna.github.io/AMPidentifier},
  note = {Web interface for the AMPidentifier toolkit}
}
```

---

## Contact

**Lead Developer:** Madson A. de Luna Aragão  
**Email:** madsondeluna@gmail.com  
**Institution:** UFMG - Universidade Federal de Minas Gerais  
**GitHub:** [@madsondeluna](https://github.com/madsondeluna)

**Issues:** https://github.com/madsondeluna/AMPidentifier/issues  
**Discussions:** https://github.com/madsondeluna/AMPidentifier/discussions

---

**Last Updated:** December 2025  
**Version:** 1.0.0  
**Status:** Production (Static Frontend) | Development (Backend API)
