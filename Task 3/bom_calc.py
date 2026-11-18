"""Task 3.3 - outpatient block bill of materials (assumed counts, edit to your layout)."""
import math, csv
# Assumptions (state them in the report): 12 consulting rooms x 2 outlets, 6 Wi-Fi 6 APs,
# pharmacy 4 outlets via small switch (96 m is too long for copper)
runs = [("Consulting rooms (24 outlets, avg 57.5 m)", 24, 57.5, "Cat6A U/FTP"),
        ("Waiting-hall APs (6, 60 m)",                6, 60,   "Cat6A U/FTP"),
        ("Pharmacy uplink (OM4 duplex, 96 m)",        1, 96,   "OM4 duplex fibre"),
        ("Link to main building (OS2 duplex, 420 m)", 1, 420,  "OS2 single-mode duplex fibre")]
rows = []
print(f"{'Run':46}{'qty':>4}{'m each':>8}{'total m':>9}{'+10% m':>9}")
cu = 0
for name, q, l, med in runs:
    tot = q * l; sp = math.ceil(tot * 1.10)
    print(f"{name:46}{q:4d}{l:8.1f}{tot:9.0f}{sp:9d}  {med}")
    rows.append([name, med, q, l, tot, sp])
    if "Cat6A" in med: cu += sp
print(f"\nCat6A total with spare = {cu} m -> {math.ceil(cu/305)} boxes of 305 m")
items = [
 ("48-port PoE+ L2/L3 access switch (4x SFP+)", 1, "consulting rooms, APs, uplinks"),
 ("8-port PoE+ switch with 2 SFP (pharmacy)", 1, "4 outlets + fibre uplink"),
 ("Wi-Fi 6 access point (PoE, 2.5G port)", 6, "waiting hall"),
 ("Cat6A RJ45 keystone jack", 34, "24 consulting + 6 AP + 4 pharmacy"),
 ("Cat6A patch panel 48-port 1U", 1, ""),
 ("Cat6A patch cord 1-2 m (switch side)", 34, ""),
 ("Cat6A patch cord 3 m (work-area side)", 28, "24 rooms + 4 pharmacy"),
 ("SFP+ 10G-LR single-mode transceiver", 2, "main building link, both ends"),
 ("SFP 1000BASE-SX / 10G-SR multimode transceiver", 2, "pharmacy link"),
 ("LC-LC duplex patch cord", 4, ""),
 ("Fibre patch tray / ODF 1U, LC adapters", 1, ""),
 ("Outdoor-rated armoured fibre (420 m) + gland/ducting", 1, "see run table"),
 ("12U wall-mount rack with cable manager, PDU", 1, "approx 6U used, 6U spare"),
 ("Line-interactive UPS 1-2 kVA (2U)", 1, ""),
 ("Surge/earthing kit for rack", 1, ""),
 ("Labels, velcro ties, cable tester", 1, "")]
with open("bill_of_materials.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Section", "Item/Run", "Medium or note", "Qty", "Length each (m)", "Total (m)", "With 10% spare (m)"])
    for r in rows: w.writerow(["Cabling"] + r)
    w.writerow(["Cat6A boxes (305 m)", "", "", math.ceil(cu/305)])
    for n, q, note in items: w.writerow(["Equipment", n, note, q])
print("wrote bill_of_materials.csv")
