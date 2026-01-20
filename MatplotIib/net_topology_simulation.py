import matplotlib.pyplot as plt

SIMULATION_TIME = 100
PACKET_SIZE = 100
SEND_RATE = 10
LINK_CAPACITY = 50000

node_counts = [5, 10, 15, 20, 25]
topologies = ["Bus", "Star", "Hybrid"]

throughput = {t: [] for t in topologies}
packet_loss = {t: [] for t in topologies}

for N in node_counts:
    sources = (N + 1) // 2
    total_packets = sources * SEND_RATE * SIMULATION_TIME
    offered_load = sources * SEND_RATE * PACKET_SIZE

    for t in topologies:
        if t == "Bus":
            efficiency = max(0.3, 1 - 0.03 * N)
        elif t == "Star":
            efficiency = max(0.5, 1 - 0.02 * N)
        else:
            efficiency = max(0.4, 1 - 0.025 * N)

        successful_bits = min(offered_load, LINK_CAPACITY) * efficiency
        throughput[t].append(successful_bits / 1000)

        successful_packets = (successful_bits / PACKET_SIZE) * SIMULATION_TIME
        loss = total_packets - successful_packets
        packet_loss[t].append(max(loss, 0))

plt.figure()
for t in topologies:
    plt.plot(node_counts, throughput[t], marker='o', label=t)
plt.xlabel("Number of Nodes")
plt.ylabel("Throughput (kbps)")
plt.title("Throughput vs Number of Nodes")
plt.legend()
plt.grid()
plt.show()

plt.figure()
for t in topologies:
    plt.plot(node_counts, packet_loss[t], marker='o', label=t)
plt.xlabel("Number of Nodes")
plt.ylabel("Packet Loss")
plt.title("Packet Loss vs Number of Nodes")
plt.legend()
plt.grid()
plt.show()
