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
