# Author : Mrunal Nirajkumar Shah

"""
Implementation of Grover's Algorithms with Grover Oracle, Diffusion, 
and Algorithm Itself.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

class GroversAlgorithm:
    def __init__(self):
        pass

    @staticmethod
    def grover_oracle(circuit, n, target):
        """
        Grover Oracle for marking the target state.
        Marks the target qubit state as the solution.

        Very simple placeholder oracle:
        Phase-flip the target state
        """
        
        # Convert the target index to binary string
        target_bits = f"{target:0{n}b}"

        # X gate to match target
        for i, bit in enumerate(target_bits[::-1]):
            if bit == "0":
                circuit.x(i)

        # Multi-controlled Z
        circuit.h(n-1)
        circuit.mcx(list(range(n-1)), n-1)
        circuit.h(n-1)

        # Undo X gate
        for i, bit in enumerate(target_bits[::-1]):
            if bit == "0":
                circuit.x(i)

    @staticmethod
    def diffusion(circuit, n):
        """
        Diffusion operator for grover's algorithm.
        """
        circuit.h(range(n))
        circuit.x(range(n))

        circuit.h(n-1)
        circuit.mcx(list(range(n-1)), n-1)
        circuit.h(n-1)

        circuit.x(range(n))
        circuit.h(range(n))

    def grover_algorithm(n, target, num_iteration=2):
        """
        Implement Grover's search algorithm.
        n: number of qubits
        target: the index of the target state
        num_iterations: the number of Grover iterations to perform
        """

        qc = QuantumCircuit(n,n)
        
        # Put into superposition
        qc.h(range(n))

        # Grover's Iteration
        for _ in range(num_iteration):
            GroversAlgorithm.grover_oracle(qc, n, target)
            GroversAlgorithm.diffusion(qc,n)

        # Measurement
        qc.measure(range(n), range(n))

        # Simulate
        simulator = AerSimulator()
        tqc = transpile(qc, simulator)

        job = simulator.run(tqc, shots=1024)

        results = job.result()
        counts = results.get_counts()

        # Plot
        plot_histogram(counts)

        return counts