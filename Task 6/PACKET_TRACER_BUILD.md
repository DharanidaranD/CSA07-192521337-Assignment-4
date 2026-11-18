# Task 6 Stage 5 - reduced Packet Tracer build
Devices: 2 core L3 switches (3650), 2 distribution (3650), 2 access switches, 2 routers as ISP-A and ISP-B, 1 edge router/firewall
(router + ACL), PCs in VLAN10/30/40, Server in VLAN60.
1. Core-1 <-> Core-2 (trunk), each distribution dual-homed to both cores (trunks), access dual-homed to dist.
2. `vlan 10,20,30,40,60` everywhere; `ip routing` on the cores; SVIs 10.x gateways (per the address plan); HSRP (`standby 1 ip ...`)
   or just OSPF area 0 between cores and distribution.
3. Edge router: two uplinks to ISP-A/ISP-B, default routes with `ip route 0.0.0.0 0.0.0.0 <ISP-A> 1` and floating `... <ISP-B> 10`; NAT overload.
4. ACLs: Guest VLAN permit only to internet (as in Task 5); CCTV VLAN reachable only from staff.
5. Demonstrate: pings within VLAN, guest -> staff blocked, guest -> internet works, shut a core link then a core switch uplink and ping again,
   shut ISP-A and show failover (`show ip route`).
Save university_campus_network.pkt, screenshots, and export device configs to device_configurations.txt (`show running-config`).
