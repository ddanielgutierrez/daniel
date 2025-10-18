# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names():
    for name in targets:
        print(name)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_and_type():
      for name, info in targets.items():
        print(f"{name}: {info['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_mag_greater_than(threshold=0.1):
    out = []
    for name, info in targets.items():
        if info["Magnitude"] > threshold:
            out.append(name)
    print(out)
    return out
# 4) Look up another target, add all the necessary information to the targets list. 
def add_target(name, ra, dec, magnitude, spectral_type):
    targets[name] = {
        "RA": ra,
        "Dec": dec,
        "Magnitude": float(magnitude),
        "Spectral Type": spectral_type
    }
    return name

def _parse_dec_deg(dec_str):
    s = dec_str.replace('−', '-')  
    deg = float(s.split('°')[0].strip())
    return deg

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_closest_to_dec(dec_target=20.0):
    best_name = None
    best_key = None  
    for name, info in targets.items():
        dec_deg = _parse_dec_deg(info["Dec"])
        mag = info["Magnitude"]
        key = (abs(dec_deg - dec_target), mag)  
        if best_key is None or key < best_key:
            best_key = key
            best_name = name
    print(best_name)
    return best_name




# 6) What is your favorite constellation?
favorite_constellation = "Orion"

if __name__ == "__main__":
    print("Star names:")
    print_star_names()

    print("\n Star + Spectral Type:")
    print_star_and_type()

    print("\n Stars with magnitude > 0.1:")
    print(stars_mag_greater_than())

    print("\n Adding new star: Altair")
    add_target("Altair", "19h 50m 47.0s", "+08° 52′ 06″", 0.77, "A7V")
    print("Altair added successfully.\n")

    print(" Brightest star closest to 20° Dec:")
    print(brightest_closest_to_dec())

    print("\n My favorite constellation is:", favorite_constellation)