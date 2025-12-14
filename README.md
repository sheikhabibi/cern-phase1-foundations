# CMS Dimuon Analysis: Rediscovering the Z-Boson

## 1. The Problem
High-Energy Physics experiments at CERN produce petabytes of collision data. This project analyzes real data from the **CMS Detector (2011 Run)** to identify the **Z-Boson** and **J/Psi** meson by reconstructing their invariant mass from muon pairs ($Z \rightarrow \mu^+ \mu^-$).

## 2. Methods
* **Data Source:** CERN Open Data Portal (Double Muon Dataset).
* **Tools:** Python, Pandas, Matplotlib, SciPy.
* **Technique:**
    * Filtered events for opposite-charge muon pairs.
    * Calculated Invariant Mass.
    * Modeled the Z-Boson peak using a **Gaussian Curve Fit** ($f(x) = A e^{-(x-\mu)^2 / 2\sigma^2}$).

## 3. Results
* Successfully isolated the Z-Boson peak at **91 GeV**.
* Identified low-energy resonances: **J/Psi (3.1 GeV)** and **Upsilon (9.4 GeV)**.
* **Measured Mass:** 91.50 GeV (Error < 0.35% from standard model value of 91.1876 GeV).

## 4. Future Work
* Implement a Neural Network to classify signal vs. background noise.
* Analyze transverse momentum ($p_T$) distributions.