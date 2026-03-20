import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self):
        self.physical = random.random()
        self.biological = random.random()
        self.cognitive = random.random()
        self.spiritual = random.random()
        self.justice = random.random()

    def update(self):
        self.biological += 0.05 * self.physical
        self.cognitive += 0.05 * self.biological
        self.spiritual += 0.05 * self.cognitive
        self.justice += 0.05 * self.spiritual

# Create agents
agents = [Agent() for _ in range(100)]

# Track averages
physical_avg = []
biological_avg = []
cognitive_avg = []
spiritual_avg = []
justice_avg = []

# Simulation loop
for step in range(50):
    for agent in agents:
        agent.update()

    physical_avg.append(sum(a.physical for a in agents)/len(agents))
    biological_avg.append(sum(a.biological for a in agents)/len(agents))
    cognitive_avg.append(sum(a.cognitive for a in agents)/len(agents))
    spiritual_avg.append(sum(a.spiritual for a in agents)/len(agents))
    justice_avg.append(sum(a.justice for a in agents)/len(agents))

# Plot results
plt.plot(physical_avg, label="Physical")
plt.plot(biological_avg, label="Biological")
plt.plot(cognitive_avg, label="Cognitive")
plt.plot(spiritual_avg, label="Spiritual")
plt.plot(justice_avg, label="Justice")

plt.legend()
plt.title("Hexa-Layer Interaction Simulation")
plt.xlabel("Time Step")
plt.ylabel("State Value")

plt.savefig("simulation_result.png")
plt.show()
