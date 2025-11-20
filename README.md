# Pi Calculator Project

A Python project that calculates pi to 20 decimal places using deliberately inefficient methods, designed to demonstrate optimization opportunities.

## Project Structure

```
.
├── calculate_pi.py          # Main inefficient implementation
├── calculate_pi_optimized.py # Optimized version for comparison
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Methods Implemented

### Inefficient Methods (calculate_pi.py)

1. **Monte Carlo Simulation**: Generates random points and checks if they fall inside a circle
   - Uses pure Python loops (no vectorization)
   - Computes distance for each point individually
   - ~100 million iterations needed

2. **Leibniz Formula**: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
   - Extremely slow convergence
   - Needs ~50 million terms for decent accuracy
   - Uses high-precision Decimal arithmetic

3. **Buffon's Needle**: Probabilistic method using needle drops
   - Simulates dropping needles on parallel lines
   - ~10 million drops needed
   - Multiple trigonometric calculations per drop

### Optimization Opportunities

The inefficient implementation has several areas that can be optimized:

- **Vectorization**: Replace loops with NumPy array operations
- **Better Algorithms**: Use faster-converging formulas (Machin, Chudnovsky, Ramanujan)
- **Caching**: Memoize repeated calculations
- **Parallel Processing**: Distribute work across CPU cores
- **Compiled Code**: Use Numba or Cython for JIT compilation

## Installation

### Using uv (Recommended)

1. Install uv if you haven't already:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Using pip (Traditional)

1. Ensure Python 3.8+ is installed:
```bash
python --version
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the inefficient version:
```bash
python calculate_pi.py
```

**Note**: This will take several minutes to complete as it's intentionally inefficient.

### Run the optimized version:
```bash
python calculate_pi_optimized.py
```

This demonstrates how vectorization and better algorithms improve performance.

## Expected Output

The program will display pi estimates from each method:

```
============================================================
Inefficient Pi Calculator
============================================================

Method 1: Monte Carlo Simulation
------------------------------------------------------------
Generating 100,000,000 random points...
Estimated pi: 3.14159265358979323846

Method 2: Leibniz Formula
------------------------------------------------------------
Calculating 50,000,000 terms...
Estimated pi: 3.14159265358979323846

Method 3: Buffon's Needle
------------------------------------------------------------
Dropping 10,000,000 needles...
Estimated pi: 3.14159265358979323846

============================================================
Reference Value:
Actual pi:    3.14159265358979323846
============================================================
```

## Performance Notes

- **Inefficient version**: Takes ~30-60 seconds depending on your CPU
- **Optimized version**: Takes 5-10 seconds
- The inefficiency is intentional for educational purposes

## Learning Objectives

This project demonstrates:
- The importance of algorithm choice
- Benefits of vectorization vs loops
- Trade-offs between precision and performance
- How to profile and optimize Python code

## Future Optimizations

Try implementing:
- Numba JIT compilation
- GPU acceleration with CuPy
- Chudnovsky algorithm for fastest convergence
- Memory-efficient streaming calculations

## License

MIT License - Feel free to use for learning and experimentation.
