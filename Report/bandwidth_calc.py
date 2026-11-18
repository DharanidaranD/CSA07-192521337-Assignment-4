"""Task 1.2 - bandwidth per computer before / after, plus Wi-Fi 6 alternative."""
N = 30
FILE_MB = 50                      # example month-end file
bits = FILE_MB * 8
print("BEFORE: one 10 Mbps shared coax bus (hub floor is the same collision domain)")
print(f"  worst-case share per PC  = 10/{N} = {10/N:.3f} Mbps")
print(f"  with ~55% CSMA/CD efficiency at heavy load = {10*0.55/N:.3f} Mbps")
print(f"  {FILE_MB} MB save, all {N} busy: {bits/(10/N):.0f} s ({bits/(10/N)/60:.0f} min)")
print("AFTER: switched star, 1 Gbps full duplex per PC port")
print("  dedicated link per PC = 1000 Mbps (no sharing at the edge)")
for name, g in (("server on 1G", 1000), ("server on 2x1G LAG", 2000), ("server on 10G", 10000)):
    share = g / N
    print(f"  {name:20}: all {N} saving at once -> {share:7.1f} Mbps each, {FILE_MB} MB in {bits/share:5.1f} s")
print(f"  one user alone: {bits/1000:.2f} s for {FILE_MB} MB")
print("ALTERNATIVE: all-Wi-Fi 6, one AP (2x2, 80 MHz, MCS11 PHY 1201 Mbps)")
phy = 1201
for eff in (0.6, 0.4):
    tot = phy * eff
    print(f"  usable {int(eff*100)}% airtime efficiency = {tot:.0f} Mbps shared, half duplex -> {tot/N:.1f} Mbps per user")
print(f"  {FILE_MB} MB at ~20 Mbps = {bits/20:.0f} s  -> switched star wins for month-end saves")
