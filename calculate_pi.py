"""
Pi Calculator - Monte Carlo Method
Calculates pi to 20 decimal places
"""

import random
from decimal import Decimal, getcontext

def calculate_pi_monte_carlo(iterations):
    """
    Calculate pi using Monte Carlo method.
    
    Args:
        iterations: Number of random points to generate
    
    Returns:
        Estimated value of pi
    """
    inside_circle = 0
    
    for _ in range(iterations):
        # Generate random point in unit square
        x = random.random()
        y = random.random()
        
        # Check if point is inside quarter circle
        distance = (x * x + y * y) ** 0.5
        
        if distance <= 1.0:
            inside_circle += 1
    
    # Estimate pi
    pi_estimate = 4.0 * inside_circle / iterations
    return pi_estimate


def calculate_pi_leibniz(terms):
    """
    Calculate pi using Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    
    Args:
        terms: Number of terms to calculate
    
    Returns:
        Estimated value of pi
    """
    # Set high precision for decimal calculations
    getcontext().prec = 50
    
    pi_over_4 = Decimal(0)
    
    for n in range(terms):
        numerator = Decimal((-1) ** n)
        denominator = Decimal(2 * n + 1)
        term = numerator / denominator
        pi_over_4 += term
    
    return float(pi_over_4 * 4)


def calculate_pi_buffon_needle(drops, needle_length=1.0, line_distance=1.0):
    """
    Calculate pi using Buffon's Needle problem.
    Drop needles randomly and count how many cross lines.
    
    Args:
        drops: Number of needle drops
        needle_length: Length of needle
        line_distance: Distance between parallel lines
    
    Returns:
        Estimated value of pi
    """
    import math
    crosses = 0
    
    for _ in range(drops):
        # Random position and angle
        y = random.random() * (line_distance / 2)
        theta = random.random() * math.pi
        
        # Calculate needle endpoints
        y_end = y + (needle_length / 2) * math.sin(theta)
        
        # Check if needle crosses a line
        if y_end >= line_distance / 2 or y_end <= 0:
            crosses += 1
    
    # Estimate pi using Buffon's formula
    if crosses > 0:
        pi_estimate = (2 * needle_length * drops) / (line_distance * crosses)
        return pi_estimate
    return 0


def main():
    """Main function to calculate and display pi estimates."""
    print("=" * 60)
    print("Pi Calculator")
    print("=" * 60)
    print()
    
    # Method 1: Monte Carlo (moderate accuracy)
    print("Method 1: Monte Carlo Simulation")
    print("-" * 60)
    iterations = 100_000_000  # 100 million points
    print(f"Generating {iterations:,} random points...")
    pi_monte_carlo = calculate_pi_monte_carlo(iterations)
    print(f"Estimated pi: {pi_monte_carlo:.20f}")
    print()
    
    # Method 2: Leibniz Formula
    print("Method 2: Leibniz Formula")
    print("-" * 60)
    terms = 50_000_000  # 50 million terms
    print(f"Calculating {terms:,} terms...")
    pi_leibniz = calculate_pi_leibniz(terms)
    print(f"Estimated pi: {pi_leibniz:.20f}")
    print()
    
    # Method 3: Buffon's Needle
    print("Method 3: Buffon's Needle")
    print("-" * 60)
    drops = 10_000_000
    print(f"Dropping {drops:,} needles...")
    pi_buffon = calculate_pi_buffon_needle(drops)
    print(f"Estimated pi: {pi_buffon:.20f}")
    print()
    
    # Reference value
    print("=" * 60)
    print("Reference Value:")
    print(f"Actual pi:    {3.14159265358979323846:.20f}")
    print("=" * 60)
    
    print()

if __name__ == "__main__":
    main()
