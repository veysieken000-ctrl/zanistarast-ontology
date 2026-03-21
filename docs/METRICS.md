# Simulation Metrics Framework for Zanistarast

This document defines how system performance is measured.

Without metrics, no scientific evaluation is possible.

---

## 1. Purpose

To quantify:

- stability
- knowledge coherence
- economic balance
- governance effectiveness

---

## 2. Stability Index

Measures how stable the system is over time.

\[
Stability = 1 - Var(V)
\]

Where:

- V = being state of agents

Interpretation:

- close to 1 → stable
- close to 0 → unstable

---

## 3. Knowledge Coherence

Measures consistency of witnessing.

\[
Coherence = 1 - Var(W_i)
\]

Where:

- W_i = witnessing values

Low variance = high truth

---

## 4. Resource Inequality (Gini Coefficient)

Measures economic imbalance.

\[
Gini = \frac{\sum |R_i - R_j|}{2n^2 \bar{R}}
\]

Interpretation:

- 0 → perfect equality
- 1 → extreme inequality

---

## 5. Collapse Rate

Measures system failure frequency.

\[
Collapse = \frac{\text{agents removed}}{\text{total agents}}
\]

---

## 6. Adaptation Speed

Measures how fast system recovers from disturbance.

\[
Adaptation = \frac{1}{time\ to\ recovery}
\]

---

## 7. Rights Violation Index

Measures governance failure.

\[
Violation = \frac{\text{invalid decisions}}{\text{total decisions}}
\]

---

## 8. Circulation Efficiency

Measures economic flow effectiveness.

\[
Efficiency = \frac{\text{flow volume}}{\text{resource variance}}
\]

---

## 9. Composite Score

Overall system score:

\[
Score = w1*Stability + w2*Coherence + w3*(1-Gini) + w4*(1-Collapse)
\]

---

## 10. Scientific Rule

No experiment is valid unless at least 3 metrics are reported.

---

## 11. Goal

To transform Zanistarast into:

- measurable
- comparable
- falsifiable system

