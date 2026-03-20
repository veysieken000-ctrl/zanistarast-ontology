🧠 MODEL MANTIĞI
Her agent (ajan):
Potansiyel (P)
Tanıklık (W)
Kaynak (R)
taşır.
Ve:
👉 birbirleriyle etkileşir
👉 bilgi üretir
👉 ekonomi oluşturur

import random

class Agent:
    def __init__(self):
        # Potential
        self.ehad = 1
        self.will = random.uniform(0, 1)
        self.power = random.uniform(0, 1)
        self.life = random.uniform(0, 1)

        # Witnessing
        self.perception = random.uniform(0, 1)
        self.differentiation = random.uniform(0, 1)
        self.recording = random.uniform(0, 1)

        # Resource
        self.resource = random.uniform(0, 100)

    def potential(self):
        return (self.ehad + self.will + self.power + self.life) / 4

    def witnessing(self):
        return (self.perception + self.differentiation + self.recording) / 3

    def being(self):
        return self.potential() * self.witnessing()

    def update_witnessing(self):
        # learning effect
        self.perception += random.uniform(-0.05, 0.05)
        self.differentiation += random.uniform(-0.05, 0.05)
        self.recording += random.uniform(-0.05, 0.05)

        # clamp values
        self.perception = max(0, min(1, self.perception))
        self.differentiation = max(0, min(1, self.differentiation))
        self.recording = max(0, min(1, self.recording))


# Initialize agents
agents = [Agent() for _ in range(100)]

def circulation(agents):
    avg = sum(a.resource for a in agents) / len(agents)
    for a in agents:
        a.resource = a.resource * 0.9 + avg * 0.1


def knowledge(agents):
    ws = [a.witnessing() for a in agents]
    avg = sum(ws) / len(ws)
    variance = sum((w - avg)**2 for w in ws) / len(ws)
    return avg, variance


# Simulation loop
for step in range(50):

    # Update witnessing (learning)
    for a in agents:
        a.update_witnessing()

    # Economic flow
    circulation(agents)

    # Knowledge check
    k, var = knowledge(agents)

    # Being stability
    beings = [a.being() for a in agents]

    print(f"Step {step}")
    print(f"Avg Being: {sum(beings)/len(beings):.4f}")
    print(f"Knowledge Coherence: {k:.4f}")
    print(f"Variance (truth stability): {var:.6f}")
    print("-"*40)

