# Quantum Portfolio Optimization with RIT-Penalized QAOA

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-blueviolet.svg)](https://qiskit.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **13-qubit quantum optimization** pipeline for constrained portfolio selection, implementing a novel **Relational Information Theory (RIT)** penalty framework for QUBO formulation.

## 🎯 Problem Statement

Select K=4 assets from an 8-stock universe (NVDA, MSFT, LLY, XOM, JNJ, PG, JPM, BRK-B) to minimize portfolio variance while maximizing returns, subject to:
- **Cardinality constraint**: Exactly 4 assets
- **Budget constraint**: Normalized cost ≤ B' = 1.638
- **Sector caps**: ≤2 assets per sector

## 🔬 Methodology

### Four-Phase Pipeline

| Phase | Description | Key Output |
|-------|-------------|------------|
| **Phase 1** | Market data retrieval, covariance estimation, QUBO formulation | 8×8 covariance matrix, penalty coefficients |
| **Phase 2** | Classical baseline (brute force, greedy, continuous relaxation) | Optimal portfolio: {NVDA, JNJ, PG, JPM} |
| **Phase 3** | QUBO validation, Ising mapping, spectral analysis | 13×13 QUBO matrix, ground state E* = -0.6156 |
| **Phase 4** | QAOA with CVaR objective, multi-start Powell optimization | Quantum solution recovery |

### RIT Penalty Framework

Penalty coefficients derived from information-theoretic principles:
- **α₁ (cardinality)** = 0.036058 (sufficiency floor × 1.05 safety margin)
- **α₂ (budget)** = 0.007356 (peer condition)

## 📊 Results

### Classical vs Quantum Comparison

| Method | Portfolio | Objective | Runtime |
|--------|-----------|-----------|---------|
| Brute Force (exact) | NVDA, JNJ, PG, JPM | -0.018961 | 0.1s |
| Greedy | NVDA, JNJ, PG, JPM | -0.018961 | <0.1s |
| QAOA p=5 | NVDA, JNJ, PG, JPM | -0.018961 | 45s |

### QAOA Convergence

| Depth (p) | ⟨H⟩ Energy | P(ground state) | Target Match |
|-----------|------------|-----------------|--------------|
| 1 | -0.491 | 0.000122 | ✗ |
| 3 | -0.543 | 0.000456 | ✗ |
| 5 | -0.598 | 0.002341 | ✓ |
| 8 | -0.612 | 0.008912 | ✓ |

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running the Pipeline

Run the full pipeline end-to-end:
```bash
python main.py
```

Run individual phases:
```bash
python src/phase1_data_preparation.py
python src/phase2_classical_baseline.py
python src/phase3_qubo_validation.py
python src/phase4_qaoa_optimization.py
```

Generate publication figures:
```bash
python figures/plot.py
```

## 📁 Repository Structure

```text
.
├── main.py                             # Master pipeline entrypoint
├── project-quantum-circuit.ipynb       # QAOA Execution Jupyter Notebook
├── README.md                          # Project documentation
├── requirements.txt                    # Python dependencies
├── fig1_efficient_frontier.png         # Efficient Frontier plot
├── fig2_qaoa_convergence.png          # QAOA Convergence plot
├── fig3_solution_comparison.png       # Solution Comparison plot
├── src/                                # Core python source files
│   ├── main.py
│   ├── phase1_data_preparation.py
│   ├── phase2_classical_baseline.py
│   ├── phase3_qubo_validation.py
│   └── phase4_qaoa_optimization.py
├── figures/                            # Research figure generation
│   └── plot.py
├── docs/                               # Methodology & analysis documentation
└── outputs/                            # Log outputs from pipeline execution
```
