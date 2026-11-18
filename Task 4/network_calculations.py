"""Task 4: ALOHA, CSMA/CD minimum frame, ATM overhead, WLAN sizing."""
import math
print("== 4.1 ALOHA ==")
print(f"pure ALOHA    S = G e^-2G, max at G=0.5 -> 1/(2e) = {1/(2*math.e):.4f} (18.4%)")
print(f"slotted ALOHA S = G e^-G,  max at G=1   -> 1/e    = {1/math.e:.4f} (36.8%)")
print("== CSMA/CD minimum frame (10 Mbps, 2500 m, v = 2e8 m/s) ==")
d, v, R = 2500, 2e8, 10e6
tp = d / v; rtt = 2 * tp
print(f"propagation {tp*1e6:.1f} us, round trip {rtt*1e6:.1f} us")
print(f"min frame = R x 2tp = {R*rtt:.0f} bits = {R*rtt/8:.2f} bytes (propagation only)")
print("IEEE 802.3 fixes 512 bits (64 B) slot time = 51.2 us, which covers repeater/jam delays")
print(f"max span for 512 bits at 2e8 m/s: {512/R*v/2:.0f} m (one-way, ideal)")
print("== 4.3 ATM vs Ethernet overhead ==")
print(f"ATM cell header overhead 5/53 = {5/53*100:.2f}%")
for payload in (1500, 64, 46):
    cells = math.ceil((payload + 8) / 48)       # AAL5 trailer 8 B, padded to 48 B cells
    wire = cells * 53
    print(f"IP packet {payload:4d} B over AAL5/ATM: {cells} cells = {wire} B, overhead {(wire-payload)/wire*100:.1f}%")
    eth = max(payload, 46) + 18
    print(f"   Ethernet frame (14 hdr + 4 FCS): {eth} B, overhead {(eth-payload)/eth*100:.2f}%"
          f"; with preamble+IFG (38 B) {(max(payload,46)+38-payload)/(max(payload,46)+38)*100:.2f}%")
print("== 4.2 WLAN sizing: 300 phones ==")
for per_ap in (30, 40, 50):
    print(f"{per_ap} clients/AP -> {math.ceil(300/per_ap)} APs")
print("Chosen: 8 APs on 5 GHz (~38 phones each), 2.4 GHz radios only on 4 APs, channels 1/6/11 reused")
