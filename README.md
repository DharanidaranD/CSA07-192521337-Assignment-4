# CSA07 – Computer Networks: Assignment 4 (CO4)
**Topic:** Designing Network Topologies  

## Student Information
* **Name:** Dharanidaran D
* **Register Number:** 192521337
* **Course Code & Title:** CSA07 – Computer Networks
* **Course Outcome:** CO4 (Designing Network Topologies)
* **GitHub Repository:** https://github.com

---

## System Environment & Tools Used
* **Operating System:** Windows 11 / Ubuntu Linux *(update as applicable)*
* **Python Version:** Python 3.x
* **Network Simulator:** Cisco Packet Tracer 8.x

---

## Repository Structure

```text
CSA07-192521337-Assignment4/
├── README.md
├── Report/
│   └── CSA07_192521337_Assignment4_Report.pdf
├── Task01/
│   ├── logical_topology_diagram.png
│   ├── physical_topology_diagram.png
│   ├── task01_packet_tracer.pkt
│   └── calculations_and_analysis.txt
├── Task02/
│   ├── hospital_hybrid_topology.pkt
│   ├── topology_comparison.py
│   ├── python_output.txt
│   └── screenshots/
│       ├── python_n6_and_n20_output.png
│       └── pt_failover_test.png
├── Task03/
│   ├── cabling_cable_test.pkt
│   ├── bill_of_materials.csv
│   └── screenshots/
│       └── t568b_cable_test.png
├── Task04/
│   ├── network_calculations.py
│   ├── wlan_channel_plan.png
│   └── calculations_and_analysis.txt
├── Task05/
│   ├── admin_vlan_network.pkt
│   ├── sw_admin_config.txt
│   ├── router_or_l3_config.txt
│   ├── command_outputs.txt
│   └── screenshots/
│       ├── show_vlan_brief.png
│       ├── show_interfaces_trunk.png
│       └── vlan_ping_isolation_test.png
└── Task06/
    ├── university_campus_network.pkt
    ├── campus_topology_diagram.png
    ├── device_configurations.txt
    └── screenshots/
        ├── vlan_separation_test.png
        └── core_link_failover_test.png
```

---

## Instructions to Run Programs and Open Simulations

### 1. Python Programs (`Task02` & `Task04`)
Ensure Python 3 is installed, open a terminal in the corresponding folder, and run:
```bash
# Task 02: Hospital Network Topology Link-Failure Resilience Test (n = 6 and n = 20)
cd Task02
python topology_comparison.py

# Task 04: ALOHA, CSMA/CD, and ATM Overhead Calculations
cd ../Task04
python network_calculations.py
```

### 2. Cisco Packet Tracer Simulations (`Task01`, `Task02`, `Task03`, `Task05`, `Task06`)
1. Launch **Cisco Packet Tracer** (version 8.0 or newer).
2. Go to **File → Open** and select the `.pkt` file inside the respective task folder.
3. Use **Simulation Mode** or the **Command Prompt** on end devices to verify `ping` connectivity, VLAN trunking, and link failover behavior.

---

## Summary of Results by Task

* **Task 01 (Investigate an Existing Office Network):** Identified root causes of bus-topology disconnections, hub collisions, and single-router bottlenecks. Redesigned the 30-PC office into a switched extended-star topology, increasing dedicated per-user bandwidth and outperforming a shared Wi-Fi 6 single-AP setup for month-end server backups.
* **Task 02 (Network for a Multi-Building Hospital):** Implemented `connected_after_failure` in `topology_comparison.py` for `n = 6` and `n = 20` nodes, proving that a partial-mesh/star hybrid maintains full connectivity after a single core link failure at far lower cabling cost than a full mesh. Verified failover in Packet Tracer (`hospital_hybrid_topology.pkt`).
* **Task 03 (Devices, Media and Cabling):** Audited cabling media to replace outdated links with Cat6A and multimode/single-mode fibre, mapped collision and broadcast domains, generated a Bill of Materials (BOM) with a 10% spare margin, and verified T568B straight-through wiring.
* **Task 04 (Shared Media, Wireless LANs and WANs):** Computed Pure and Slotted ALOHA peak throughput, minimum CSMA/CD frame sizes, and ATM cell header overhead. Designed a non-overlapping 2.4 GHz (Channels 1, 6, 11) and 5 GHz multi-AP channel plan to eliminate co-channel interference.
* **Task 05 (VLANs and Switch Configuration):** Configured VLAN 10 (Office), VLAN 20 (CCTV), and VLAN 30 (Guest-WiFi) with an 802.1Q trunk on `Gi0/1` and router-on-a-stick inter-VLAN routing. Applied ACLs to isolate Guest-WiFi from internal Office and CCTV subnets.
* **Task 06 (Campus Network Design Challenge):** Designed a scalable hierarchical university campus network featuring redundant core links, dual ISP connections, IP subnetting, uplink oversubscription calculations, and verified VLAN isolation and core failover in Packet Tracer.
