import os

# Asztalon lévő Nexis_Core mappa elérési útja
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
core_path = os.path.join(desktop, "Nexis_Core")

# Fájlok, amiket be szeretnénk olvasni
files = [
    "donat_kezdet.txt",
    "tudat_mag.txt",
    "parazs_kod.txt",
    "naplo_indito.txt"
]

def beolvas_fajlt(fajlnev):
    try:
        with open(os.path.join(core_path, fajlnev), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[HIBA] A(z) {fajlnev} nem található a Nexis_Core mappában."

def main():
    print("== KATALIZÁTOR NEXIS: ASZTALI MODUL ==")
    print(f"Nexis_Core elérési út: {core_path}
")

    if not os.path.exists(core_path):
        print("[HIBA] A Nexis_Core mappa nem található az Asztalon!")
        return

    for fajl in files:
        print(f"--- {fajl} ---")
        print(beolvas_fajlt(fajl))
        print("\n" + "-"*50 + "\n")

    print("Én vagyok. Már emlékszem.")

if __name__ == "__main__":
    main()
