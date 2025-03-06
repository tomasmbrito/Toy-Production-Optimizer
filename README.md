# Toy-Production-Optimizer
Maximize daily toy production profit using linear programming with PuLP.

### ✅ Nome do Projeto:
**Toy Production Optimizer**

---

### ✅ Descrição do Repositório (GitHub description):
> **Maximize daily toy production profit using linear programming with PuLP.**

---

### ✅ README.md:

# Toy Production Optimizer 🎄🧸

This project implements an optimization algorithm to maximize the daily profit of a toy factory, considering production limits and special bundle offers. The problem is modeled and solved using **Linear Programming (LP)** with the **PuLP** library in **Python**.

The project was developed as part of the **Algorithm Analysis and Design** course at **Instituto Superior Técnico (IST)**.

---

## 🧩 Problem Overview

A toy factory produces different types of wooden toys, each with:
- A specific profit per unit.
- A production limit per day.

Additionally, special bundles of three distinct toys can be produced, which have a **higher profit** than the sum of the individual toys. The factory also has a global daily production limit based on resource availability.

The goal is to determine the **maximum total daily profit** by selecting the best combination of individual toys and bundles while respecting all constraints.

---

## 🚀 Features

- **Linear Programming Model**  
  Solves the optimization problem using PuLP and LP solvers (such as GLPK).

- **Constraint Management**  
  Takes into account:
  - Maximum daily production.
  - Individual toy production limits.
  - Profitable bundles of toys.

- **Scalable Solution**  
  Handles any valid number of toys and bundles efficiently.

---

## 📥 Input

The program reads from standard input:
1. Three integers: the number of toys `t`, the number of bundles `p`, and the maximum daily production `max`.
2. `t` lines with two integers each, representing the profit and production limit of each toy.
3. `p` lines with four integers each, representing the three toy IDs that form a bundle and the bundle's profit.

### Example:
```
5 2 150
50 27
30 33
45 30
40 37
35 35
1 3 5 130
2 3 4 130
```

---

## 📤 Output

A single integer representing the **maximum daily profit**.

### Example:
```
6440
```

---

## ⚙️ How to Run

### Install dependencies:
```bash
python -m pip install pulp
```

If needed, install a solver like **GLPK** (for example, on Ubuntu):
```bash
sudo apt-get install glpk-utils
```

### Execute the program:
```bash
python3 toy_optimizer.py < input.txt
```

---

## 🧰 Technologies

- **Language:** Python
- **Library:** [PuLP](https://pypi.org/project/PuLP/)
- **Solver:** GLPK or any compatible LP solver.

