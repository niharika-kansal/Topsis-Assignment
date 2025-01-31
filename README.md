# TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) Python Implementation

This repository contains a Python implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method, which is used for multi-criteria decision analysis. It ranks alternatives based on the performance data of various criteria and provides a final score and rank.

## Features

- **Multi-Criteria Decision Making (MCDM)**: Helps in evaluating and ranking alternatives based on multiple criteria.
- **Customizable Weights & Impacts**: Define the importance of each criterion and whether it's beneficial or non-beneficial.
- **Automated Scoring and Ranking**: Automatically computes a TOPSIS score and ranks the alternatives.

## Requirements

- Python 3.x
- `numpy` and `pandas` libraries

To install the required libraries, you can use:

```bash
pip install numpy pandas

Dataset
The dataset used in this project is a CSV file containing alternatives and criteria. The first row contains column headers (criteria names), and the first column contains the names of alternatives. The remaining columns represent the performance scores for each criterion.

Example Dataset (102203344-data.csv):
Fund Name	P1	P2	P3	P4	P5
M1	0.84	0.71	6.7	42.1	12.59
M2	0.91	0.83	7	31.7	10.11
M3	0.79	0.62	4.8	46.7	13.23
M4	0.78	0.61	6.4	42.4	12.55
M5	0.94	0.88	3.6	62.2	16.91
M6	0.88	0.77	6.5	51.5	14.91
M7	0.66	0.44	5.3	48.9	13.83
M8	0.93	0.86	3.4	37	    10.55

Usage

Input Format
Input CSV File: A CSV file where the first column is the alternative name, and the remaining columns represent the performance scores for each criterion.
Weights: A comma-separated string defining the weights for each criterion (e.g., 0.25,0.25,0.25,0.15,0.10).
Impacts: A comma-separated string defining the impact of each criterion (e.g., +,+,+,+,-). + represents a beneficial criterion, while - represents a non-beneficial criterion.

Running the Package
To run the script, use the following command in the terminal or command prompt:
python Topsis.py 102203344-data.csv 0.25,0.25,0.25,0.15,0.10 +,+,+,+,- output.csv

Output
After running the command, the package will generate an output file output.csv with the following additional columns:

TOPSIS Score: The calculated score for each alternative.
Rank: The rank based on the TOPSIS score (1 is the best).

Fund Name	P1	P2	P3	P4	P5	TOPSIS Score	Rank
M1	0.84	0.71	6.7	42.1	12.59	0.644718515	2
M2	0.91	0.83	7	31.7	10.11	0.680361059	1
M3	0.79	0.62	4.8	46.7	13.23	0.443784812	7
M4	0.78	0.61	6.4	42.4	12.55	0.563499544	4
M5	0.94	0.88	3.6	62.2	16.91	0.489616631	6
M6	0.88	0.77	6.5	51.5	14.91	0.639262133	3
M7	0.66	0.44	5.3	48.9	13.83	0.376340122	8
M8	0.93	0.86	3.4	37	    10.55	0.514142481	5

License

This project is licensed under the MIT License 