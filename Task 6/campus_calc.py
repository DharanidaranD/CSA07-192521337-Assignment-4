"""Task 6 - address plan check, oversubscription, collapsed-core alternative.
Unit costs are ILLUSTRATIVE ASSUMPTIONS - replace with real quotations."""
import ipaddress, math
print("== Address plan (10.0.0.0/8 VLSM, one /16 per site type) ==")
plan = [("Students (hostels, 3000 x 2 dev)", "10.10.0.0/19", 6000),
        ("Lab computers (600)",              "10.20.0.0/22", 600),
        ("Staff wired+wifi",                 "10.30.0.0/22", 700),
        ("Library public + wifi",            "10.31.0.0/23", 300),
        ("Guest wifi",                       "10.40.0.0/22", 800),
        ("CCTV (~250 cameras)",              "10.50.0.0/23", 250),
        ("Servers / data centre",            "10.60.0.0/24", 120),
        ("Management (switches, APs)",       "10.99.0.0/24", 150),
        ("DMZ",                              "10.61.0.0/27", 20),
        ("Core point-to-point /30 links",    "10.254.0.0/24", 60)]
nets = [ipaddress.ip_network(p[1]) for p in plan]
for (name, cidr, need), net in zip(plan, nets):
    print(f"{name:34} {cidr:15} usable {net.num_addresses-2:6d} need {need:5d} {'OK' if net.num_addresses-2>=need else 'TOO SMALL'}")
print("overlaps:", any(a.overlaps(b) for i, a in enumerate(nets) for b in nets[i+1:]))
print("\n== Uplink oversubscription (access ports x speed / uplink) ==")
rows = [("Hostel access (48x1G, 4 closets/block)", 48, 1, 2, 10, "2x10G LAG"),
        ("Lab access (48x1G)",                     48, 1, 2, 10, "2x10G"),
        ("Academic access (48x1G PoE)",            48, 1, 2, 10, "2x10G"),
        ("Library/Auditorium access (48x1G)",      48, 1, 1, 10, "1x10G"),
        ("Distribution->Core (hostel zone, 12 closets)", 12*2*10, 1, 2, 40, "2x40G"),
        ("Distribution->Core (labs+academic)",     6*2*10, 1, 2, 40, "2x40G")]
for name, ports, sp, nup, upsp, lbl in rows:
    down = ports * sp if sp == 1 else ports
    up = nup * upsp
    print(f"{name:48} down {down:4d} G / up {up:3d} G = {down/up:5.1f}:1  ({lbl})")
print("Target: access:dist <= 20:1, dist:core <= 4:1 (typical Cisco guideline).")
print("\n== Collapsed core vs three-tier (assumed costs, Rs) ==")
core, dist, access_links = 900_000, 350_000, 24
three = 2*core + 6*dist
coll = 2*core
fibre_run, port = 60_000, 18_000
three_links = 2*6 + 24*2           # core-dist dual + access dual-homed to 2 dist
coll_links = 24*2                   # every closet dual-homed straight to both cores
print(f"three-tier: 2 core + 6 distribution = 8 devices, cost devices Rs {three:,}; fibre runs core-dist 12 + dist-access {24*2}")
print(f"collapsed : 2 core = 2 devices (saves 6), device cost Rs {coll:,}; saves Rs {three-coll:,} but needs longer runs/ports on core: {coll_links} runs of core ports")
print(f"net device+port+fibre saving = Rs {three-coll + (three_links-coll_links)*(fibre_run+2*port):,} (links removed: {three_links-coll_links})")
out_hr_cost = 150_000
print(f"If a campus-wide outage costs Rs {out_hr_cost:,}/hour (assumed), break-even = {(three-coll)/out_hr_cost:.1f} outage-hours in 10 years")
print("Single core failure: collapsed core with ONE core = whole campus down; with a pair, it survives but all load and all")
print("risk sit on 2 boxes; three-tier confines a distribution failure to its zone (hostels, labs, ...).")
