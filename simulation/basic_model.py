🚀 AŞAMA 1 — BASİT SİMÜLASYON

# Witnessing (W)
def witnessing():
    perception = random.uniform(0, 1)
    differentiation = random.uniform(0, 1)
    recording = random.uniform(0, 1)
    return (perception + differentiation + recording) / 3

# Potential (P)
def potential():
    ehad = 1 # sabit birlik
    will = random.uniform(0, 1)
    power = random.uniform(0, 1)
    life = random.uniform(0, 1)
    return (ehad + will + power + life) / 4

# Interaction (V)
def being():
    P = potential()
    W = witnessing()
    return P * W # ilk yaklaşım

# Simulation
results = [being() for _ in range(1000)]

print("Average Being:", sum(results)/len(results))
print("Max Being:", max(results))
print("Min Being:", min(results))

🚀 AŞAMA 2 — BİLGİ TESTİ

def knowledge(witnesses):
    avg = sum(witnesses) / len(witnesses)
    variance = sum((w - avg)**2 for w in witnesses) / len(witnesses)
    return avg, variance

Ws = [witnessing() for _ in range(100)]

k, var = knowledge(Ws)

print("Knowledge:", k)
print("Consistency (low variance better):", var)

🚀 AŞAMA 3 — MABÛN TESTİ

resources = [random.uniform(0, 100) for _ in range(50)]

def circulation(resources):
    avg = sum(resources) / len(resources)
    return [r * 0.9 + avg * 0.1 for r in resources]

for _ in range(10):
    resources = circulation(resources)

print("Final distribution:", resources)


