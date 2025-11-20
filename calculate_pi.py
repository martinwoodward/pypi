"""
Pi Calculator - Monte Carlo Method
Calculates pi to 20 decimal places
"""

import random
from decimal import Decimal, getcontext
from codecarbon import EmissionsTracker
import warnings
import logging

# Suppress codecarbon warnings
logging.getLogger('codecarbon').setLevel(logging.ERROR)
warnings.filterwarnings('ignore', category=UserWarning, module='codecarbon')

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


def format_pi_with_color(value, reference):
    """
    Format pi value with red coloring where it diverges from reference.
    
    Args:
        value: The calculated pi value
        reference: The actual pi value
    
    Returns:
        Formatted string with ANSI color codes
    """
    value_str = f"{value:.20f}"
    reference_str = f"{reference:.20f}"
    
    result = []
    diverged = False
    
    for i, (v_char, r_char) in enumerate(zip(value_str, reference_str)):
        if not diverged and v_char == r_char:
            result.append(v_char)
        else:
            if not diverged:
                diverged = True
                result.append('\033[91m')  # Red color
            result.append(v_char)
    
    if diverged:
        result.append('\033[0m')  # Reset color
    
    return ''.join(result)


def main():
    """Main function to calculate and display pi estimates."""
    print("=" * 60)
    print("Pi Calculator")
    print("=" * 60)
    print()
    
    emissions_data = []
    
    # Method 1: Monte Carlo (moderate accuracy)
    print("Method 1: Monte Carlo Simulation")
    print("-" * 60)
    iterations = 10_000_000  # 10 million points
    print(f"Generating {iterations:,} random points...")
    tracker = EmissionsTracker(log_level='error', save_to_file=False)
    tracker.start()
    pi_monte_carlo = calculate_pi_monte_carlo(iterations)
    emissions_monte_carlo = tracker.stop()
    print(f"Estimated pi: {pi_monte_carlo:.20f}")
    emissions_data.append(('Monte Carlo', emissions_monte_carlo))
    print()
    
    # Method 2: Leibniz Formula
    print("Method 2: Leibniz Formula")
    print("-" * 60)
    terms = 5_000_000  # 5 million terms
    print(f"Calculating {terms:,} terms...")
    tracker = EmissionsTracker(log_level='error', save_to_file=False)
    tracker.start()
    pi_leibniz = calculate_pi_leibniz(terms)
    emissions_leibniz = tracker.stop()
    print(f"Estimated pi: {pi_leibniz:.20f}")
    emissions_data.append(('Leibniz', emissions_leibniz))
    print()
    
    # Method 3: Buffon's Needle
    print("Method 3: Buffon's Needle")
    print("-" * 60)
    drops = 2_000_000  # 2 million drops
    print(f"Dropping {drops:,} needles...")
    tracker = EmissionsTracker(log_level='error', save_to_file=False)
    tracker.start()
    pi_buffon = calculate_pi_buffon_needle(drops)
    emissions_buffon = tracker.stop()
    print(f"Estimated pi: {pi_buffon:.20f}")
    emissions_data.append(('Buffon Needle', emissions_buffon))
    print()
    
    # Summary comparison
    actual_pi = 3.14159265358979323846
    print("=" * 60)
    print("Results Summary")
    print("=" * 60)
    print(f"{'Method':<20} {'Value':<25} {'Error':<15}")
    print("-" * 60)
    print(f"{'Monte Carlo':<20} {format_pi_with_color(pi_monte_carlo, actual_pi):<25} {abs(pi_monte_carlo - actual_pi):<15.10e}")
    print(f"{'Leibniz':<20} {format_pi_with_color(pi_leibniz, actual_pi):<25} {abs(pi_leibniz - actual_pi):<15.10e}")
    print(f"{'Buffon Needle':<20} {format_pi_with_color(pi_buffon, actual_pi):<25} {abs(pi_buffon - actual_pi):<15.10e}")
    print(f"{'Actual π':<20} {actual_pi:<25.20f}")
    print("=" * 60)
    
    # Carbon emissions comparison
    print()
    print("=" * 60)
    print("Carbon Emissions")
    print("=" * 60)
    print(f"{'Method':<20} {'CO₂ (kg)':<20} {'Difference':<20}")
    print("-" * 60)
    
    # Find min emissions for comparison
    min_emissions = min(e[1] for e in emissions_data)
    
    for method, emissions in emissions_data:
        diff = emissions - min_emissions
        diff_pct = (diff / min_emissions * 100) if min_emissions > 0 else 0
        print(f"{method:<20} {emissions:<20.6e} {diff_pct:>6.2f}% more")
    
    total_emissions = sum(e[1] for e in emissions_data)
    print("-" * 60)
    print(f"{'Total':<20} {total_emissions:<20.6e}")
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()
