# Author : Mrunal Nirajkumar Shah
# Comparison between Classical & Grover's Algorithm

import time
import math

from src.classic_search import ClassicalSearch
from src.grovers_algorithm import GroversAlgorithm
from src.visualize import Visualization


def search_comparison(urange, target, name):
    n_qubit = math.ceil(math.log2(max(urange, target + 1))) # + 1 is to be safe
    arr = list(range(1, urange + 1)) 

    print(f"""
        Range   : 1 to {urange}
        Target  : {target}
        n_qubit : log2N ≈ {n_qubit}
    """)

    start_time_c = time.time()
    classical_result = ClassicalSearch.classical_brute_force_search(arr, target)
    classical_time = time.time() - start_time_c

    if classical_result == -1:
        print("Classical Search: Target NOT found")
        classical_results = []                     
        classical_steps_for_plot = [0]            
        classical_values_for_plot = [0]
    else:
        print(f"Classical Search: Target found at index {classical_result}")
        classical_results = list(range(1, classical_result + 2))  
        classical_steps_for_plot = list(range(1, len(classical_results) + 1))
        classical_values_for_plot = classical_results

    start_time_q = time.time()
    quantum_counts = GroversAlgorithm.grover_algorithm(n_qubit, target)
    quantum_time = time.time() - start_time_q

    Visualization.plot_classical_vs_quantum(
        classical_steps=classical_steps_for_plot,
        classical_values=classical_values_for_plot,
        quantum_counts=quantum_counts,
        file_name=name
    )

    print(f"""
        Time Taken:
         - Classical Brute Force : {classical_time:.6f} s
         - Grover's Algorithm    : {quantum_time:.6f} s
    """)