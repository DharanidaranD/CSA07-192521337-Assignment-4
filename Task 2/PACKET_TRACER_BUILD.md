# Task 2.4 - Packet Tracer build (hospital hybrid core)
1. Place 5 Cisco 3560/3650 (or 2960) switches named SW-ADMIN-DC, SW-EMERG, SW-THEATRE, SW-OUTPT, SW-LAB. Use Copper Straight-Through
   (or Fibre if modules are fitted) links: ADMIN-EMERG, ADMIN-THEATRE, EMERG-THEATRE, ADMIN-OUTPT, ADMIN-LAB.
2. Put 2 PCs in each block (PC-E1, PC-T1, ...) and a Server-PT "Records" in the Admin block (192.168.1.10/24); PCs 192.168.1.x/24.
3. Spanning tree (RSTP): `spanning-tree mode rapid-pvst` on all switches; check with `show spanning-tree`.
4. Test: ping Records from PC-E1 and PC-T1. Delete the ADMIN-EMERG cable (or `shutdown` Gi0/1 on SW-ADMIN-DC). Ping again - it must
   still work via EMERG-THEATRE-ADMIN. Wait for RSTP convergence (a few seconds). Repeat removing ADMIN-THEATRE.
5. Screenshot ping before/after to screenshots/pt_failover_test.png; save hospital_hybrid_topology.pkt.
