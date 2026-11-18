"""Task 2.1-2.3 + alternative: hospital cost and failure analysis (5 blocks)."""
from itertools import combinations
from collections import deque

PORT, RUN = 18_000, 60_000
B = ["Emergency", "Outpatient", "Theatres", "Lab", "Admin(DC)"]  # data centre in Admin

def cost(links):  # each link = 1 fibre run + 2 ports
    return len(links), 2 * len(links), len(links) * RUN + 2 * len(links) * PORT

def reach(nodes, links, start):
    adj = {x: [] for x in nodes}
    for a, b in links:
        adj[a].append(b); adj[b].append(a)
    seen, q = {start}, deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return seen

E, O, P, L, D = B
designs = {
 "Bus (E-O-T-L-D order)": [(E, O), (O, "x"), ("x", L), (L, D)],
 "Ring": [(E, O), (O, "Theatres"), ("Theatres", L), (L, D), (D, E)],
 "Star (DC = Admin)": [(D, E), (D, O), (D, "Theatres"), (D, L)],
 "Full mesh": list(combinations(B, 2)),
 "Hybrid (triangle core)": [(D, E), (D, "Theatres"), (E, "Theatres"), (D, O), (D, L)],
}
# fix the bus (Emergency-Outpatient-Theatres-Lab-Admin in a line)
designs["Bus (E-O-T-L-D order)"] = [(E, O), (O, "Theatres"), ("Theatres", L), (L, D)]

print(f"{'Design':26}{'links':>6}{'ports':>7}{'cost Rs':>10}  single cuts that isolate Emergency/Theatres from DC")
for name, lk in designs.items():
    n, p, c = cost(lk)
    bad = []
    for cut in lk:
        rem = [l for l in lk if l != cut]
        r = reach(B, rem, D)
        for crit in (E, "Theatres"):
            if crit not in r:
                bad.append(f"{cut[0]}-{cut[1]} cuts {crit}")
    print(f"{name:26}{n:6d}{p:7d}{c:10,d}  {'; '.join(bad) if bad else 'NONE (survives every single cut)'}")

print("\nDouble-cut survival (both critical blocks still reach the data centre):")
for name in ("Ring", "Hybrid (triangle core)"):
    lk = designs[name]; pairs = list(combinations(lk, 2)); ok = 0
    for c1, c2 in pairs:
        rem = [l for l in lk if l not in (c1, c2)]
        r = reach(B, rem, D)
        ok += (E in r and "Theatres" in r)
    print(f"{name:26} {ok}/{len(pairs)} double cuts survived")
