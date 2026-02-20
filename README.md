# Linear Regression from Scratch: Normal Equation Implementation (Work in progress)

This repository features a custom implementation of a **Linear Regression** model using the **Normal Equation**. Unlike iterative methods like Gradient Descent, this approach provides an analytical solution to find the optimal parameters for the model.

## 📖 Introduction
In this project, I demonstrate the underlying mathematics of linear models by implementing the core logic from scratch using Python and NumPy. This project serves as a deep dive into the closed-form solution for minimizing the Mean Squared Error (MSE) in a regression context.

## 📐 The Mathematics
The Normal Equation is a method to find the vector $\theta$ (the weights) that minimizes the cost function without the need for feature scaling or iterative optimization:

$$\theta = (X^T X)^{-1} X^T y$$

Where:
* $\theta$: The weight vector we want to find.
* $X$: The input feature matrix (including the bias term).
* $y$: The target values vector.

## 📁 Project Structure
The repository is organized as follows to ensure scalability and clarity:

* `src/`: Contains the core implementation (`linear_regression.py`).
* `notebooks/`: A Jupyter Notebook demonstrating the model's application on a real-world dataset.
* `data/`: Sample CSV data used for training and testing.
* `requirements.txt`: Necessary Python libraries (NumPy, Pandas, Matplotlib).

## 🛠 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/simonhandle/Linear-Regression-via-the-Normal-Equation.git](https://github.com/simonhandle/Linear-Regression-via-the-Normal-Equation.git)
cd Linear-Regression-via-the-Normal-Equation
```

### 2. Recommended: Use virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Open the Demo
```bash
jupyter notebook notebooks/linear_regression_demo.ipynb
```


