# Manual Calculation Cases for Zanistarast

This document provides hand-calculable examples for validating Zanistarast claims.

These cases are designed for:

- old computers
- manual checking
- simple falsification

---

## Case 1 — Hebûn Stability

### Claim
Being requires stable witnessing.

### Data
Witnessing values:

- A1 = 0.50
- A2 = 0.52
- A3 = 0.49
- A4 = 0.51
- A5 = 0.48

### Mean
\[
K = (0.50 + 0.52 + 0.49 + 0.51 + 0.48)/5 = 0.50
\]

### Interpretation
Values are close to each other.

Expected:
- low variance
- stable pattern
- stronger Hebûn condition

---

## Case 2 — Zanabûn Coherence

### Claim
Knowledge emerges from coherent multi-agent witnessing.

### Data
Witnessing values:

- A1 = 0.20
- A2 = 0.80
- A3 = 0.10
- A4 = 0.90
- A5 = 0.40

### Mean
\[
K = (0.20 + 0.80 + 0.10 + 0.90 + 0.40)/5 = 0.48
\]

### Interpretation
Values are far apart.

Expected:
- high variance
- weak coherence
- misinformation risk

---

## Case 3 — Mabûn Circulation

### Claim
Circulation reduces extreme imbalance.

### Initial Resources
- R1 = 100
- R2 = 80
- R3 = 20
- R4 = 10
- R5 = 5

### Mean Resource
\[
Ravg = (100 + 80 + 20 + 10 + 5)/5 = 43
\]

### One Circulation Step
Formula:
\[
R_i(new) = 0.9R_i + 0.1Ravg
\]

Results:

- R1 = 0.9(100) + 0.1(43) = 94.3
- R2 = 0.9(80) + 0.1(43) = 76.3
- R3 = 0.9(20) + 0.1(43) = 22.3
- R4 = 0.9(10) + 0.1(43) = 13.3
- R5 = 0.9(5) + 0.1(43) = 8.8

### Interpretation
- high values go down slightly
- low values go up slightly
- system becomes smoother

---

## Case 4 — Rasterast Adaptive Decision

### Claim
Adaptive governance handles disturbances better.

### Scenario
A rigid system applies the same rule under all conditions.
An adaptive system changes decision based on local disturbance.

### Disturbance
Resource loss in one sub-region.

### Comparison
- rigid response → same rule everywhere
- adaptive response → local correction only

### Expected
- adaptive system preserves more total stability
- rigid system spreads disturbance

---

## Case 5 — Core Law

### Claim
Systems require control to remain structured.

### Example
Two systems:

1. System A  
   - has structure
   - has control
   - has interaction

2. System B
   - has structure
   - no control
   - has interaction

### Expected
- System A remains organized
- System B drifts into instability

---

## Final Rule

These manual cases are considered useful if:

- they are simple
- they are reproducible
- they support or challenge a claim clearly

