# Bandwidth-Measurment-minimet

# Bandwidth Measurement and Analysis using Mininet

## Problem Statement

The objective of this project is to measure and compare network bandwidth across different network configurations using Mininet. The analysis is performed using iperf by evaluating throughput under various topologies and network conditions.

---

## Objectives

* Measure throughput using iperf
* Compare performance across multiple network topologies
* Analyze the impact of delay, bandwidth limits, and number of hops
* Understand network behavior under different configurations

---

## Tools and Technologies Used

* Mininet
* iperf
* Ubuntu Virtual Machine
* Open vSwitch

---

## Setup Instructions

1. Install Mininet:
   sudo apt update
   sudo apt upgrade -y
   sudo apt install mininet -y

2. Run Mininet:
   sudo mn

3. Test connectivity:
   pingall

Expected Result: 0 percent packet loss

---

## Topologies Implemented

1. Single Topology

* One switch and two hosts
* Used as baseline

2. Linear Topology

* Multiple switches connected in a chain
* Used to study multi-hop impact

3. Tree Topology

* Hierarchical structure
* Simulates real-world networks

---

## Running the Topologies

Single Topology:
sudo mn --custom topology/single_topo.py --topo singletopo

Linear Topology:
sudo mn --custom topology/linear_topo.py --topo lineartopo

Tree Topology:
sudo mn --custom topology/tree_topo.py --topo treetopo

---

## Bandwidth Measurement using iperf

Start server:
h1 iperf -s &

Run client:
h2 iperf -c h1

---

## Results

| Topology        | Delay | Bandwidth Limit | Throughput     |
| --------------- | ----- | --------------- | -------------- |
| Single          | 0 ms  | None            | 29.2 Gbits/sec |
| Linear          | 0 ms  | None            | 28.5 Gbits/sec |
| Tree (h3 to h1) | 0 ms  | None            | 26.0 Gbits/sec |
| Tree (h4 to h1) | 0 ms  | None            | 25.7 Gbits/sec |

---

## Analysis

* The highest throughput is observed in the single topology because there is only one switch between hosts.
* In the linear topology, throughput decreases slightly due to multiple switches introducing processing delay.
* In the tree topology, throughput decreases further as the network becomes more complex and packets travel longer paths.
* The results clearly show that as network complexity and number of hops increase, throughput decreases.
* The variation in throughput between hosts in the tree topology indicates the effect of network path length.

---

## Validation

Connectivity Test:
pingall

Observed Result:
50 percent packet loss (indicates connectivity or configuration issue)

---

## Proof of Execution

The repository includes:

* Screenshots of iperf outputs
* pingall results
* Topology execution

---

## Conclusion

This project demonstrates how network topology affects bandwidth performance. Simpler topologies provide higher throughput, while more complex topologies introduce delays and reduce performance. The use of iperf and Mininet effectively shows real-world network behavior.

---

## References

* https://mininet.org
* https://iperf.fr
* Course materials

