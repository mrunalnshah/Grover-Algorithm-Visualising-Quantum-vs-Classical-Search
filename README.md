# Grover's Algorithm - Visualizing Quantum vs Classical Search

### Result
#### In Classical Brute Force
- Searches one item at a time
- Takes O(N) steps in the worst case
- If target is found → stops immediately
- If target is not found → must check all N items

#### In Grover's Algorithm
- All possible answers are explored at once using superposition
- Uses O(√N) iterations
- If target exists → probability of the correct answer becomes very high (one tall bar in histogram)
- If target does not exist → probabilities remain almost equal and low (flat/uniform histogram)
- A single dominant bar = solution found  
  Flat distribution = no solution exists

#### In test 4, you see a dominant bar, but its just 0.08 out of 1 probability, so no its not the target.

<table border="1" cellpadding="10" cellspacing="0" width="150%">
  <thead>
    <tr>
      <th>Experiment Details</th>
      <th>Box Plot</th>
      <th>Line Plot</th>
      <th>Stem Plot / Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 10<br>
        <strong>Target</strong>: 5<br>
        <strong>n_qubits</strong>: ≈4 <br><br>
      </td>
      <td align="center"><img src="plots\1_box.png" ></td>
      <td align="center"><img src="plots\1_line.png" ></td>
      <td align="center"><img src="plots\1_stem.png"></td>
    </tr>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 50<br>
        <strong>Target</strong>: 49<br>
        <strong>n_qubits</strong>: ≈6 <br><br>
      </td>
      <td align="center"><img src="plots\2_box.png" ></td>
      <td align="center"><img src="plots\2_line.png" ></td>
      <td align="center"><img src="plots\2_stem.png" ></td>
    </tr>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 50<br>
        <strong>Target</strong>: 80<br>
        <strong>n_qubits</strong>: 7<br><br>
      </td>
      <td align="center"><img src="plots\3_box.png" ></td>
      <td align="center"><img src="plots\3_line.png" ></td>
      <td align="center"><img src="plots\3_stem.png" ></td>
    </tr>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 256<br>
        <strong>Target</strong>: 108<br>
        <strong>n_qubits</strong>: 8<br><br>
      </td>
      <td align="center"><img src="plots\4_box.png" ></td>
      <td align="center"><img src="plots\4_line.png" ></td>
      <td align="center"><img src="plots\4_stem.png" ></td>
    </tr>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 1000<br>
        <strong>Target</strong>: 555<br>
        <strong>n_qubits</strong>: 10<br><br>
      </td>
      <td align="center"><img src="plots\5_box.png" ></td>
      <td align="center"><img src="plots\5_line.png" ></td>
      <td align="center"><img src="plots\5_stem.png" ></td>
    </tr>
    <tr>
      <td valign="top">
        <strong>Range</strong>: 1 to 1000<br>
        <strong>Target</strong>: 1001<br>
        <strong>n_qubits</strong>: 10<br><br>
      </td>
      <td align="center"><img src="plots\6_box.png" ></td>
      <td align="center"><img src="plots\6_line.png" ></td>
      <td align="center"><img src="plots\6_stem.png" ></td>
    </tr>
  </tbody>
</table>


### TO FIND N_QUBITS REQUIRED.
For N iterations, 

$$
    n\\_qubits = log_2 N
$$

for safety, you must add + 1 or apply ceiling operation as log will be a float.


## Problem Statement
Given an unstructured search space of size $N = 2^n$, find a marked item $|w⟩$ (the "winner" or solution) using as few queries as possible. 

`Classical brute-force search` requires $O(N)$ queries in the worst case.

`Grover’s algorithm` achieves this in $O(\sqrt{N})$ queries — a quadratic speedup.

## Mathematical Foundation

### Initial State
$$
    |\psi_0⟩ = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x⟩ = H^{\otimes n} |0^n⟩
$$

We can decompose the Hilbert space into two subspaces:
1. Good states (solutions): $|w⟩$ → there is M solutions (usually M = 1)
2. Bad states (non-solutions): all others

### Define

$$
\begin{aligned}
|\alpha\rangle &= \frac{1}{\sqrt{N-M}} \sum_{x \notin w} |x\rangle && \text{(bad states)} \\
|\beta\rangle  &= \frac{1}{\sqrt{M}} \sum_{x \in w} |x\rangle   && \text{(good states, here |w⟩ if M = 1)}
\end{aligned}
$$


### Then, 

$$
|\psi_0\rangle = \sqrt{\frac{N-M}{N}} \; |\alpha\rangle + \sqrt{\frac{M}{N}} \; |\beta\rangle \quad \approx \quad |\alpha\rangle \quad \text{(since } M \ll N\text{)}
$$

### The initial angle between the state and the bad subspace:

$$
\sin\theta = \sqrt{\frac{M}{N}} \quad \Rightarrow \quad \theta \approx \sqrt{\frac{M}{N}} \approx \frac{\pi}{2} \text{ when } M=1
$$

### Actually, standard notation uses:
$$
    |s⟩ = |\psi_0⟩, \quad |s'⟩ = \text{state without phase (orthogonal to } |w⟩)
$$

$$
    |s⟩ = \cos(\theta/2) |s'⟩ + \sin(\theta/2) |w⟩, \quad \sin(\theta/2) = \sqrt{M/N}
$$

## Grover's Iteration: Oracle + Diffusion
Each iteration rotates the state by angle $\theta$ towards the solution.

### Step 1: Oracle $U_f$
The oracle marks the solution by flipping its phase:
$$
    U_f |x⟩ = 
    \begin{cases}
    -|x⟩ & \text{if } x = w \\
    \;\; |x⟩ & \text{otherwise}
    \end{cases}
$$

In matrix form: $U_f = I - 2|w⟩⟨w|$
This corresponds to reflection about the subspace orthogonal to |w⟩.
Geometrically: reflects the current state over the hyperplane perpendicular to |w⟩.

### Step 2: Diffusion Operator (Inversion About Average) $U_s$
$$
    U_s = 2|s⟩⟨s| - I
$$

Also implementable as:

$$
    U_s = H^{\otimes n} (I - 2|0^n⟩⟨0^n|) H^{\otimes n} = 2|0^n⟩⟨0^n| - I \quad \text{(up to global phase)}
$$

This reflects the state over the original superposition state |s⟩.

One full Grover iteration $G = U_s U_f$ performs two reflections → rotation by $2\theta$ in the plane spanned by |s'⟩ and |w⟩.

After $k$ iterations:

$$
    G^k |s⟩ = \sin((2k+1)\theta/2) |w⟩ + \cos((2k+1)\theta/2) |s'⟩
$$

We want $(2k+1)\theta/2 \approx \pi/2$, so amplitude of |w⟩ ≈ 1.

For one solution (M=1):

$$
    \theta \approx 2 \arcsin(1/\sqrt{N}) \approx 2/\sqrt{N}
$$

Optimal number of iterations:

$$
    k_{\text{opt}} = \left\lfloor \frac{\pi}{4} \sqrt{N} - \frac{1}{2} \right\rfloor \approx \left\lfloor \frac{\pi}{4} \cdot 2^{n/2} \right\rfloor
$$

## Benefit?
1. For SHA256, Traditional Computers uses $2^{256}$, while a quantum computer can do it in $2^{128}$ iterations.

## Code Walkthrough.
1. `main.py` is the file with `main()`. 
2. `src/classic_search.py` contains classical brute force algorithm
3. `src/comparison.py` contains code used to compare both grover's and classical algorithms on same test_set.
4. `src/grovers_algorithm.py` contains implementation of grover's algorithm with grover oracle and diffusion code.
5. `src/visualize.py` contains code used to visualize both the algorithms side by side on same test_set. I have used `bar, line, and stem plots`.



