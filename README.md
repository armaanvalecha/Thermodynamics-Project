# Thermodynamic Property Analysis of Vinyl Chloride (C2H3Cl)

# Overview

This project involves generating a complete thermodynamic property chart for Vinyl Chloride (C2H3Cl), an essential material used in the production of Polyvinyl Chloride (PVC). The project includes calculations for heat capacity, enthalpy, entropy, and volume using Python-based numerical integration techniques and comparisons with reference experimental data.

# Motivation

Why Study Vinyl Chloride?

Crucial Raw Material for PVC Production:

Vinyl chloride is the monomer used to manufacture PVC, one of the most widely used plastics globally.

PVC is extensively used in industries such as construction, healthcare, and consumer goods.

Industry Demand and Economic Importance:

Companies like Reliance Industries Limited (RIL) are investing in large-scale PVC plants in India.

Optimizing the production process of Vinyl Chloride can enhance efficiency and cost-effectiveness in industrial applications.

# Methodology

# 1. Thermodynamic Property Calculation

Heat Capacity (Cp) Equation:

The specific heat capacity is modeled as a polynomial function of temperature:



Enthalpy Calculation:

Using numerical integration (SciPy’s quad function), enthalpy is determined as:



Entropy Calculation:

Similarly, entropy is calculated by integrating  over temperature:



# 2. Volume Calculation

Based on the ideal gas equation:



Used to explore pressure-volume relationships assuming ideal gas behavior.

# 3. Code Implementation

Python scripts are used for numerical calculations and data visualization.

Libraries used: NumPy, SciPy, Matplotlib.

Outputs include:

Tables listing values of Cp, H, and S at various temperatures.

Graphs plotting these thermodynamic properties over a temperature range of 273K to 1500K.

# Results and Observations

1. Comparison with Experimental Data

Reference data taken from Journal of Research of the National Bureau of Standards (by Shu-Shing Chang).

At lower temperatures (~273K), the computed Cp values closely match experimental data (~50.82 J/mol·K vs. 50.43 J/mol·K).

At mid-range temperatures (~335K), the deviation remains minimal (~58.04 J/mol·K vs. 67 J/mol·K).

Higher Temperature Deviations:

At temperatures above 700K, computed values start diverging significantly from experimental values.

Indicates potential improvements needed in the model at high temperatures.

# Limitations and Future Improvements

Deviations at High Temperatures: The polynomial fit may need refinement or additional correction factors.

Assumption of Ideal Gas Behavior: Real gas equations may improve volume predictions.

Incorporating Experimental Data: Additional sources could help refine accuracy.
