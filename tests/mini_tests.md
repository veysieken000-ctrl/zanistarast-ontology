# Mini Tests for Zanistarast

This file defines lightweight validation checks for Zanistarast.

These tests are designed for low-resource computers and manual verification.

---

## Test 1 — Hebûn Stability Check

Claim:
Being requires stable witnessing.

Method:
- Define 5 agents
- Assign witnessing values manually
- Compare low-variance and high-variance cases

Expected:
- Low variance → stable being
- High variance → unstable being

---

## Test 2 — Zanabûn Coherence Check

Claim:
Knowledge emerges from coherent multi-agent witnessing.

Method:
- Use 5 witnessing values
- Compute mean
- Compute simple variance manually

Expected:
- Lower variance = higher coherence
- Higher variance = misinformation risk

---

## Test 3 — Mabûn Circulation Check

Claim:
Circulation stabilizes systems better than accumulation.

Method:
- Start with 5 resource values
- Apply one circulation step:
  Ri(new) = 0.9Ri + 0.1Ravg

Expected:
- Extreme values reduce
- Distribution becomes smoother

---

## Test 4 — Rasterast Governance Check

Claim:
Adaptive governance improves system stability.

Method:
- Compare two decision styles:
  1. rigid fixed rule
  2. adaptive rule
- Use a small disturbance scenario

Expected:
- Adaptive rule recovers faster

---

## Rule

A test is accepted if:

- input is clear
- result is calculable
- expectation is falsifiable

