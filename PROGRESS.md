# CERN Openlab Application Progress Tracker

**Start Date:** December 10, 2025
**Deadline:** January 26, 2026

---

## 🟢 PHASE 1: Learn & Foundation (Weeks 1-2)

### Week 1: Core Python, NumPy & Scientific Computing (Dec 10-16)
*Goal: Master the stack, set up environment, and build ML pipeline basics.*

- **Wed, Dec 10: Python Refresh & Setup**
  - [x] Review Python OOP (classes, modules, best practices).
  - [x] Set up env (Python 3.11+, venv, pip).
  - [x] Install NumPy, SciPy, Matplotlib, scikit-learn, pandas.
  - [x] **Deliverable:** Working dev environment + small script testing all libs.

- **Thu-Fri, Dec 11-12: NumPy Deep-dive & SciPy**
  - [x] Master vectorization, broadcasting, performance tips.
  - [x] Write 5 NumPy benchmark snippets (dot product, FFT, etc.).
  - [x] Learn scipy.integrate (RK45), optimize, stats.
  - [x] Implement ODE integrator (Lorenz system).
  - [x] **Deliverable:** `NumPy_benchmark.py` with results.
  - [x] **Deliverable:** `lorenz_integrators.py` comparing 3 methods.

- **Sat, Dec 13: Data Handling & Plotting**
  - [x] Master pandas (read CSV, groupby) & Matplotlib (subplots, colormaps).
  - [x] Build data pipeline: load -> summarize -> plot.
  - [x] **Deliverable:** `small_data_pipeline.py` + 3 publication-quality plots.

- **Sun, Dec 14: Git & GitHub Setup**
  - [x] Initialize 2 GitHub repos.
  - [x] Create skeleton READMEs.
  - [x] **Deliverable:** Both repos live on GitHub with structure.

- **Mon-Tue, Dec 15-16: ML Pipeline Fundamentals**
  - [ ] Learn branching, .gitignore.
  - [ ] Install PyTorch/TensorFlow; learn tensors, autograd.
  - [ ] Write toy MLP classifier (iris/mnist).
  - [ ] Implement train/val/test split & metrics (AUC, ROC).
  - [ ] **Deliverable:** `simple_mlp.py` (toy data).
  - [ ] **Deliverable:** `ml_pipeline_template.py` (reproducible split + metrics).

**Week 1 Status:** [ ] COMPLETE

---

### Week 2: Advanced HPC & C++ (Dec 17-23)
*Goal: Master Numba, Cython, C++, and OpenMP optimization.*

- **Wed, Dec 17: Numba & Profiling**
  - [ ] Learn `@numba.jit`, `@numba.vectorize`, parallel.
  - [ ] Profile NumPy function (cProfile).
  - [ ] Optimize slow loop with Numba.
  - [ ] **Deliverable:** `numba_optimization_example.py` with speed-up plots.

- **Thu, Dec 18: Cython Intro (Optional)**
  - [ ] Understand syntax and compilation.
  - [ ] Write Cython integrator for Lorenz.
  - [ ] **Deliverable:** `cython_example.pyx` + `setup.py`.

- **Fri-Sun, Dec 19-21: C++ Ecosystem & Numerics**
  - [ ] Install g++, CMake. Write 5 small C++ snippets.
  - [ ] Implement ODE integrator (RK4) in C++ (Standard Lib).
  - [ ] Set up CMake build + timing code (chrono).
  - [ ] **Deliverable:** `lorenz_integrator.cpp` (matches Python output).
  - [ ] **Deliverable:** `benchmark.cpp` + `CMakeLists.txt` + speed-up plot.

- **Mon, Dec 22: OpenMP Parallelization**
  - [ ] Learn `#pragma omp parallel for`.
  - [ ] Parallelize C++ ODE integrator.
  - [ ] **Deliverable:** `openmp_version.cpp`.

- **Tue, Dec 23: Review & Consolidation**
  - [ ] Run full ML pipeline template.
  - [ ] Run full C++ benchmark.
  - [ ] **Deliverable:** Solid skeleton code in both repos.

**Week 2 Status:** [ ] COMPLETE

---

## 🟡 PHASE 2: Project 1 - ML on Collider Data (Weeks 3-4)

### Week 3: Data & Engineering (Dec 24-30)
*Goal: Clean pipeline, EDA, feature engineering, and baselines.*

- **Wed, Dec 24: Dataset Selection**
  - [ ] Download public HEP dataset (CMS Open Data or Kaggle).
  - [ ] **Deliverable:** Data downloaded + `data_overview.txt`.

- **Thu, Dec 25: EDA**
  - [ ] Compute summary stats, correlations.
  - [ ] Create 6-8 plots (histograms, scatter).
  - [ ] **Deliverable:** `eda_notebook.ipynb` + 8 plots.

- **Fri, Dec 26: Preprocessing**
  - [ ] Handle missing values, normalize features.
  - [ ] Engineer physics features (invariant mass, etc.).
  - [ ] **Deliverable:** `preprocessing.py` + `feature_engineering.py`.

- **Sat, Dec 27: Splitting & Imbalance**
  - [ ] Handle class imbalance (resampling/weighting).
  - [ ] Split Train (60) / Val (20) / Test (20).
  - [ ] **Deliverable:** `train_val_test_splits.py`.

- **Sun, Dec 28: Baseline Models**
  - [ ] Train Logistic Regression & Random Forest.
  - [ ] Plot ROC, AUC, Feature Importance.
  - [ ] **Deliverable:** `baseline_models.py` + ROC plots.

- **Mon, Dec 29: Hyperparameter Tuning**
  - [ ] GridSearch or RandomizedSearch.
  - [ ] **Deliverable:** `grid_search_results.txt`.

- **Tue, Dec 30: Consolidation**
  - [ ] Modularize code.
  - [ ] Write `main.py` for end-to-end run.
  - [ ] **Deliverable:** Clean, modular GitHub structure.

**Week 3 Status:** [ ] COMPLETE

---

### Week 4: Deep Learning & Polish (Dec 31 - Jan 6)
*Goal: Deep Learning model, advanced metrics, and documentation.*

- **Wed-Fri, Dec 31-Jan 2: Deep Learning Model**
  - [ ] Design MLP (PyTorch/TF).
  - [ ] Implement training loop with early stopping.
  - [ ] Evaluate on Test Set (AUC-ROC, F1, Calibration).
  - [ ] **Deliverable:** `mlp_model.py` + `train.py`.
  - [ ] **Deliverable:** `test_evaluation.py` + metric plots.

- **Sat, Jan 3: Interpretability**
  - [ ] Analyze misclassified events.
  - [ ] **Deliverable:** `error_analysis.py` + plots.

- **Sun, Jan 4: Documentation**
  - [ ] Write comprehensive README (Problem, Methods, Results).
  - [ ] Discuss scalability/GPUs.
  - [ ] **Deliverable:** `README.md` (500+ words) + `requirements.txt`.

- **Mon, Jan 5: Reproducibility Check**
  - [ ] Run entire pipeline from scratch in clean env.
  - [ ] **Deliverable:** `reproducibility_check.log`.

- **Tue, Jan 6: Final Polish**
  - [ ] Push all code. Tag v1.0.
  - [ ] **Deliverable:** Repo ready for external review.

**Week 4 Status:** [ ] COMPLETE

---

## 🔵 PHASE 3: Project 2 - HPC Chaos Simulation (Weeks 5-6)

### Week 5: Python Optimization (Jan 7-13)
*Goal: Python implementations and physics analysis.*

- **Wed, Jan 7: Baseline Python**
  - [ ] Clean Python integrator (Lorenz).
  - [ ] **Deliverable:** `lorenz_baseline.py` + phase-space plots.

- **Thu, Jan 8: Multi-trajectory**
  - [ ] Generalize for N trajectories (Monte Carlo).
  - [ ] **Deliverable:** `multi_trajectory.py`.

- **Fri, Jan 9: Numba**
  - [ ] Port to Numba `@jit` + parallel.
  - [ ] **Deliverable:** `numba_integrator.py` + speedup plot.

- **Sat, Jan 10: Cython (Optional)**
  - [ ] Write `.pyx` version.
  - [ ] **Deliverable:** `cython_integrator.pyx` + speedup plot.

- **Sun, Jan 11: Memory Efficiency**
  - [ ] Profile memory (tracemalloc). Optimize types.
  - [ ] **Deliverable:** `memory_profile.py`.

- **Mon, Jan 12: Feature Extraction**
  - [ ] Compute Lyapunov exponents / Recurrence plots.
  - [ ] **Deliverable:** `lyapunov_exponents.py` + analysis plots.

- **Tue, Jan 13: Review**
  - [ ] Consolidate modules. Write `main_python.py`.
  - [ ] **Deliverable:** Full Python pipeline running.

**Week 5 Status:** [ ] COMPLETE

---

### Week 6: C++ & Benchmarking (Jan 14-20)
*Goal: C++ implementations, OpenMP, and final benchmarking.*

- **Wed, Jan 14: C++ Baseline**
  - [ ] Implement Lorenz in C++ (O2/O3 optimization).
  - [ ] Verify output vs Python.
  - [ ] **Deliverable:** `lorenz_cpp.cpp` + verification test.

- **Thu, Jan 15: OpenMP**
  - [ ] Add `#pragma omp parallel`. Measure speedup.
  - [ ] **Deliverable:** `openmp_lorenz.cpp` + speedup plots.

- **Fri-Sat, Jan 16-17: Optimization & CMake**
  - [ ] Optimize memory layout / SIMD.
  - [ ] Set up professional CMake structure.
  - [ ] **Deliverable:** `optimized_lorenz.cpp` + `CMakeLists.txt`.

- **Sun, Jan 18: Comprehensive Benchmark**
  - [ ] Script to test ALL versions (Python vs Numba vs C++ vs OpenMP).
  - [ ] **Deliverable:** `final_benchmark.py` + combined plot.

- **Mon-Tue, Jan 19-20: Documentation & Final**
  - [ ] Write detailed README (HPC focus).
  - [ ] Push all code. Tag v1.0.
  - [ ] **Deliverable:** `README.md` + `performance_report.md`.
  - [ ] **Deliverable:** Project 2 Repo Live.

**Week 6 Status:** [ ] COMPLETE

---

## 🔴 PHASE 4: Final Polish & Application (Week 7)

### Week 7: Documents & Submission (Jan 21-26)
*Goal: Professional application package and submission.*

- **Wed, Jan 21: CV**
  - [ ] Write 1-2 page CV (Skills, Projects, Education).
  - [ ] **Deliverable:** `cv.pdf`.

- **Thu, Jan 22: Motivation Letter**
  - [ ] Write 250-350 words (Why CERN, Project 1 relevance, Project 2 relevance).
  - [ ] **Deliverable:** `motivation_letter.pdf`.

- **Fri, Jan 23: Transcript & Reference**
  - [ ] Get official transcript.
  - [ ] Request academic reference letter.
  - [ ] **Deliverable:** `transcript.pdf` + `reference_letter.pdf`.

- **Sat-Sun, Jan 24-25: Final Checks**
  - [ ] Re-read READMEs. Check all GitHub links.
  - [ ] Dry run application on portal.
  - [ ] **Deliverable:** Application checklist completed.

- **Mon, Jan 26: SUBMISSION DAY**
  - [ ] **Morning:** Final review of docs.
  - [ ] **Afternoon:** Log into careers.cern. Submit before 23:59 Geneva time.
  - [ ] **Deliverable:** Confirmation email received.

**Final Status:** [ ] SUBMITTED