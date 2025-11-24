# Author : Mrunal Nirajkumar Shah
# Visualizing the Algorithm

import matplotlib.pyplot as plt
import os

class Visualization:
    @staticmethod
    def plot_classical_vs_quantum(classical_steps, classical_values,
                                  quantum_counts, file_name, save_folder="plots"):
        os.makedirs(save_folder, exist_ok=True)

        states = list(quantum_counts.keys())
        total = sum(quantum_counts.values())
        probabilities = [quantum_counts[state] / total for state in states]

        def save_plot(plot_type):
            plt.suptitle(f"Test {file_name} – {plot_type} Plot", fontsize=15)
            plt.tight_layout()
            plt.savefig(os.path.join(save_folder, f"{file_name}_{plot_type.lower()}.png"),
                        dpi=200, bbox_inches='tight')
            plt.close()

        # Stem Plot
        plt.figure(figsize=(11, 5))
        plt.subplot(1, 2, 1)
        if classical_steps:
            plt.stem(classical_steps, classical_values, 'b-', markerfmt='bo', basefmt='gray')
        else:
            plt.text(0.5, 0.5, "Target\nNOT FOUND", ha='center', va='center',
                     transform=plt.gca().transAxes, fontsize=20, color='red')
        plt.title("Classical Search")
        plt.xlabel("Step")
        plt.ylabel("Items Checked")
        plt.grid(True, alpha=0.3)

        plt.subplot(1, 2, 2)
        plt.stem(states, probabilities, 'g-', markerfmt='gs', basefmt='gray')
        plt.title("Quantum Probability (Grover)")
        plt.xlabel("State")
        plt.ylabel("Probability")
        plt.grid(True, alpha=0.3)

        save_plot("stem")

        # Line Plot
        plt.figure(figsize=(11, 5))
        plt.subplot(1, 2, 1)
        if classical_steps:
            plt.plot(classical_steps, classical_values, 'b-o', lw=2, ms=8)
        else:
            plt.text(0.5, 0.5, "NOT FOUND", ha='center', va='center',
                     transform=plt.gca().transAxes, fontsize=20, color='red')
        plt.title("Classical Search")
        plt.xlabel("Step")
        plt.ylabel("Items Checked")
        plt.grid(True, alpha=0.3)

        plt.subplot(1, 2, 2)
        plt.plot(states, probabilities, 'g-s', lw=2, ms=8)
        plt.title("Quantum Probability")
        plt.xlabel("State")
        plt.ylabel("Probability")
        plt.grid(True, alpha=0.3)

        save_plot("line")

        # Bar Plot
        plt.figure(figsize=(11, 5))
        plt.subplot(1, 2, 1)
        if classical_steps:
            plt.bar(classical_steps, classical_values, color='skyblue', edgecolor='navy')
        else:
            plt.text(0.5, 0.5, "TARGET\nNOT FOUND", ha='center', va='center',
                     transform=plt.gca().transAxes, fontsize=18, color='darkred')
        plt.title("Classical Search")
        plt.xlabel("Step")

        plt.subplot(1, 2, 2)
        plt.bar(states, probabilities, color='lightgreen', edgecolor='darkgreen')
        plt.title("Quantum State Probability")
        plt.xlabel("State")
        plt.ylabel("Probability")

        save_plot("box")  

        print(f"Saved 3 plots as '{file_name}'")