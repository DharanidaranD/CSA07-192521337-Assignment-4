# Task 6 - Campus network for a new university (design document)

## Stage 1 - Interpret the requirement (estimates, state your own assumptions)
| Building | Wired ports | Wi-Fi clients (peak) | Peak traffic (est.) |
|---|---|---|---|
| Academic block | 400 | 1,500 | 1.5 Gbps |
| Laboratories | 600 PCs + 100 devices | 300 | 3 Gbps (labs run simultaneously) |
| Library | 150 | 800 | 1 Gbps |
| Hostels (3,000 students x 2 devices) | 600 (study/rooms) | 6,000 | 6 Gbps (evening video) |
| Auditorium | 60 | 1,200 | 1 Gbps |
| Data centre | 120 servers | - | 5 Gbps east-west |
| CCTV (~250 cameras @ 4 Mbps) | 250 | - | 1 Gbps to NVR |
Internet peak: 3,000 students x 2 Mbps concurrent 40% ~ 2.4 Gbps -> 2 x 2 Gbps ISP links (two providers, ISP-A 2G, ISP-B 2G) plus 20-30% for growth.
Testable requirements: R1 wired+Wi-Fi coverage in all buildings (RSSI >= -67 dBm); R2 student/staff/guest/CCTV VLANs - a guest
ping to staff/CCTV must fail; R3 failure of any one core link or one ISP must not drop services (failover < 5 s); R4 access
uplink oversubscription <= 20:1, distribution->core <= 4:1; R5 10-year growth: 30% spare ports, fibre pairs, address space;
R6 availability >= 99.9% for data centre services.

## Stage 2 - Topology (hierarchical hybrid)
Core: 2 L3 core switches fully meshed with each other (mesh); each edge firewall connected to both cores (redundant links).
Distribution: 4 switches (Hostels, Labs, Academic+Library, Data centre+Auditorium) each dual-homed to both cores (partial mesh).
Access: star from each closet switch to its distribution switch (dual uplink LAG); Wi-Fi 6 APs on PoE access ports. Two ISPs -
two firewalls, BGP/ static with SLA tracking. See campus_topology_diagram.png.

## Stage 3 - Critical decisions
Devices: L3 core/distribution (10/40G), PoE+ gigabit access switches, WLAN controller + Wi-Fi 6 APs, 2 NGFW, UPS everywhere.
Media: single-mode OS2 fibre between buildings (campus 40 acres: runs up to ~800 m), multimode OM4 inside buildings for 10G,
Cat6A horizontal (<=90 m), Cat6A to APs (PoE+, 2.5G). VLANs: 10 Student, 20 Staff, 30 Guest, 40 CCTV, 50 Labs, 60 Servers, 99 Mgmt.
Wireless: Wi-Fi 6 (802.11ax) 5 GHz, 2.4 GHz selectively, WPA3-Enterprise for staff/students, captive portal guest.
WAN: dual ISP (primary ISP-A, backup ISP-B), NAT/BGP, optional MPLS to a remote site later.

## Stage 4 - Design and calculate
See `campus_calc.py` / `campus_calc_output.txt` for the address plan (VLSM, no overlaps) and oversubscription:
access 48x1G over 2x10G = 2.4:1 (library 1x10G = 4.8:1), hostel distribution->core 240G/80G = 3:1, labs/academic 1.5:1.
Bill of materials (summary; fill unit prices from quotations): 2 core L3 switches, 4 distribution L3 switches, ~24 closets x
48-port PoE+ switches (more for hostels), ~250 APs (Wi-Fi 6), 2 NGFW, 1 WLAN controller, ~12 km OS2 fibre + ducts,
multimode/Cat6A horizontal for ~(users) outlets, 24 racks, UPS, SFP+/QSFP28 optics.

## Stage 5 - Simulation (Packet Tracer reduced build)
See `Task06/PACKET_TRACER_BUILD.md`.

## Alternative - collapsed core
Collapsed core removes the 6 distribution devices (see calc output) and about 12 fibre runs, but every closet must home straight
to the core, concentrating risk. With a single collapsed core a failure takes down everything (hostels, labs, servers, internet);
with a core pair it survives one failure but a distribution-level fault is replaced by a core-level one affecting all closets
and a bigger blast radius for misconfiguration/upgrades. Decision: with a 3,000-student hostel population and a 10-year life,
the Rs ~21 lakh (assumed prices) saving equals only ~14 outage-hours of campus-wide downtime, so keep three tiers for hostels
and labs, but accept a collapsed distribution for the small buildings (library/auditorium) as a compromise.
