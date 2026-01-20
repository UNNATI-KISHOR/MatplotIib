#bus topology simulation

import random
import matplotlib.pyplot as plt


SIMULATION_TIME = 200       
PACKET_RATE = 5               
ERROR_PROBABILITY = 0.1       
m = 3                         

WINDOW_GBN = 2 ** m          
WINDOW_SR = (2 ** m) - 1 + 1  

node_counts = [5, 10, 15, 20]

gbn_erroneous_packets = []
sr_erroneous_packets = []


for N in node_counts:

    
    sources = max(1, int(0.05 * N))

    total_packets_sent = sources * PACKET_RATE * SIMULATION_TIME

    
    gbn_errors = 0
    for _ in range(total_packets_sent):
        if random.random() < ERROR_PROBABILITY:
            
            gbn_errors += WINDOW_GBN

    
    sr_errors = 0
    for _ in range(total_packets_sent):
        if random.random() < ERROR_PROBABILITY:
            
            sr_errors += 1

    gbn_erroneous_packets.append(gbn_errors)
    sr_erroneous_packets.append(sr_errors)

plt.figure()
plt.plot(node_counts, gbn_erroneous_packets, marker='o', label="Go-Back-N")
plt.plot(node_counts, sr_erroneous_packets, marker='o', label="Selective Repeat")

plt.xlabel("Number of Nodes")
plt.ylabel("Erroneously Accepted Packets")
plt.title("Erroneous Packets vs Number of Nodes (Bus Topology)")
plt.legend()
plt.grid(True)
plt.show()
