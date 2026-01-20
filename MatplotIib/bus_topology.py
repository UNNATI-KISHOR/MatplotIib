# ------------------------------------------------------------
# Simulation of Go-Back-N and Selective Repeat ARQ Protocols
# Bus Topology
# Measuring Erroneously Accepted Packets vs Number of Nodes
# ------------------------------------------------------------

import random
import matplotlib.pyplot as plt

# ---------------- Simulation Parameters ----------------
SIMULATION_TIME = 200          # seconds
PACKET_RATE = 5               # packets per second per source
ERROR_PROBABILITY = 0.1       # packet error probability
m = 3                         # number of bits in sequence number

WINDOW_GBN = 2 ** m           # Go-Back-N window size
WINDOW_SR = (2 ** m) - 1 + 1  # Selective Repeat window size

node_counts = [5, 10, 15, 20]

gbn_erroneous_packets = []
sr_erroneous_packets = []

# ---------------- Simulation Logic ----------------
for N in node_counts:

    # 5% of total nodes selected as sources (minimum 1)
    sources = max(1, int(0.05 * N))

    total_packets_sent = sources * PACKET_RATE * SIMULATION_TIME

    # -------- Go-Back-N --------
    gbn_errors = 0
    for _ in range(total_packets_sent):
        if random.random() < ERROR_PROBABILITY:
            # Entire window retransmitted
            gbn_errors += WINDOW_GBN

    # -------- Selective Repeat --------
    sr_errors = 0
    for _ in range(total_packets_sent):
        if random.random() < ERROR_PROBABILITY:
            # Only erroneous packet retransmitted
            sr_errors += 1

    gbn_erroneous_packets.append(gbn_errors)
    sr_erroneous_packets.append(sr_errors)

# ---------------- Plot ----------------
plt.figure()
plt.plot(node_counts, gbn_erroneous_packets, marker='o', label="Go-Back-N")
plt.plot(node_counts, sr_erroneous_packets, marker='o', label="Selective Repeat")

plt.xlabel("Number of Nodes")
plt.ylabel("Erroneously Accepted Packets")
plt.title("Erroneous Packets vs Number of Nodes (Bus Topology)")
plt.legend()
plt.grid(True)
plt.show()
