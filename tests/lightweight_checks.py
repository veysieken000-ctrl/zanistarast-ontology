# Lightweight validation checks for Zanistarast
# Works on very low-spec computers

# -----------------------------
# 1. VARIANCE (Zanabûn / Hebûn)
# -----------------------------

def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)

def test_coherence():
    low_variance = [0.50, 0.52, 0.49, 0.51, 0.48]
    high_variance = [0.20, 0.80, 0.10, 0.90, 0.40]

    print("Low variance:", variance(low_variance))
    print("High variance:", variance(high_variance))


# -----------------------------
# 2. CIRCULATION (Mabûn)
# -----------------------------

def circulation_step(resources, alpha=0.1):
    avg = mean(resources)
    return [(1 - alpha) * r + alpha * avg for r in resources]

def test_circulation():
    resources = [100, 80, 20, 10, 5]
    new_resources = circulation_step(resources)

    print("Before:", resources)
    print("After :", [round(r, 2) for r in new_resources])


# -----------------------------
# 3. STABILITY CHECK
# -----------------------------

def stability(values):
    return 1 - variance(values)

def test_stability():
    values = [0.50, 0.52, 0.49, 0.51, 0.48]
    print("Stability:", stability(values))


# -----------------------------
# RUN ALL TESTS
# -----------------------------

if __name__ == "__main__":
    print("\n--- COHERENCE TEST ---")
    test_coherence()

    print("\n--- CIRCULATION TEST ---")
    test_circulation()

    print("\n--- STABILITY TEST ---")
    test_stability()
Nasıl çalıştırılır
Terminal:
Bash
Kodu kopyala
python tests/lightweight_checks.py
