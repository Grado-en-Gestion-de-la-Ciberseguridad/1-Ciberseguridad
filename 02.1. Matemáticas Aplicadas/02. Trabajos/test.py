import numpy as np
import matplotlib.pyplot as plt

# Adjacency Matrix Representation
# Example network: 3 switches, 4 endpoints
# Nodes: S1, S2, S3, P1, P2, P3, P4
adj_matrix = np.array([
    # S1 S2 S3 P1 P2 P3 P4
    [ 0,  1,  0,  1,  1,  0,  0],  # S1
    [ 1,  0,  1,  0,  1,  0,  1],  # S2
    [ 0,  1,  0,  0,  0,  1,  1],  # S3
    [ 1,  0,  0,  0,  0,  0,  0],  # P1
    [ 1,  1,  0,  0,  0,  0,  0],  # P2
    [ 0,  0,  1,  0,  0,  0,  0],  # P3
    [ 0,  1,  1,  0,  0,  0,  0],  # P4
])

# Basic parameters
beta = 0.3   # Infection rate
gamma = 0.1  # Recovery rate
time_steps = 100

# SIR Model Initialization
n_nodes = adj_matrix.shape[0]
states = np.zeros(n_nodes)  # 0: Susceptible, 1: Infected, 2: Recovered
states[3] = 1  # Initial infection at node P1

# History of states
S_history = [np.sum(states == 0)]
I_history = [np.sum(states == 1)]
R_history = [np.sum(states == 2)]

# Simulation loop
for t in range(time_steps):
    new_states = states.copy()
    for node in range(n_nodes):
        if states[node] == 0:  # Susceptible
            # Check infection from neighbors
            neighbors = np.where(adj_matrix[node] > 0)[0]
            for neighbor in neighbors:
                if states[neighbor] == 1 and np.random.rand() < beta:
                    new_states[node] = 1
                    break
        elif states[node] == 1:  # Infected
            # Recover with probability gamma
            if np.random.rand() < gamma:
                new_states[node] = 2
    states = new_states
    # Track SIR counts
    S_history.append(np.sum(states == 0))
    I_history.append(np.sum(states == 1))
    R_history.append(np.sum(states == 2))

    # Print progress every 10 steps
    if t % 10 == 0 or t == time_steps - 1:
        print(f"Step {t}: S={np.sum(states == 0)}, I={np.sum(states == 1)}, R={np.sum(states == 2)}")

# Results and plotting
plt.figure(figsize=(10, 6))
plt.plot(S_history, label="Susceptible")
plt.plot(I_history, label="Infected")
plt.plot(R_history, label="Recovered")
plt.xlabel("Time Steps")
plt.ylabel("Node Count")
plt.title("SIR Model of Malware Propagation")
plt.legend()
plt.grid()
plt.show()
