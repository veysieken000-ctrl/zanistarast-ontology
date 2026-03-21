# Expected Results for Zanistarast Lightweight Tests

This file defines the expected interpretation of test outputs.

Its purpose is to make the project scientifically clearer and easier to verify.

---

## 1. Coherence Test (Zanabûn)

### Input Types

| Case | Witnessing Pattern | Expected Variance | Expected Interpretation |
|------|--------------------|------------------|-------------------------|
| A | close values | low | high coherence |
| B | scattered values | high | low coherence |
| C | identical values | zero | perfect coherence |

### Scientific Meaning

- lower variance = stronger truth coherence
- higher variance = misinformation risk

---

## 2. Stability Test (Hebûn)

### Formula

Stability = 1 - Variance

### Interpretation Table

| Variance | Stability | Meaning |
|----------|-----------|---------|
| 0.00 - 0.02 | very high | stable being pattern |
| 0.02 - 0.10 | medium | partially stable |
| above 0.10 | low | unstable pattern |

---

## 3. Circulation Test (Mabûn)

### Input Pattern

Unequal resources:

- one or two high agents
- several low agents

### Expected Output

| Before | After Circulation | Interpretation |
|--------|-------------------|----------------|
| very high extremes | slightly reduced extremes | circulation works |
| very low agents | slightly improved values | smoothing effect |
| average stays similar | preserved | system does not collapse |

### Scientific Meaning

Circulation should:

- reduce extremes
- preserve total system
- increase smoothness

---

## 4. Governance Logic Test (Rasterast)

### Comparison

| Model | Response Type | Expected Outcome |
|------|---------------|------------------|
| rigid rule | same response everywhere | disturbance spreads |
| adaptive rule | local correction | disturbance contained |

### Scientific Meaning

Adaptive governance is expected to:

- reduce total instability
- recover faster
- protect system integrity better

---

## 5. Core Law Test

### Comparison

| System Type | Control Present | Expected Outcome |
|------------|-----------------|------------------|
| structured system | yes | stable |
| structured system | no | drift / instability |

### Scientific Meaning

If control disappears, structured behavior should weaken.

---

## 6. Result Acceptance Rule

A lightweight test is considered consistent with Zanistarast if:

- coherence behaves as predicted
- circulation reduces imbalance
- stability tracks variance
- adaptive decision performs better than rigid decision

---

## 7. Goal

This document ensures that outputs are not only observed,
but also interpreted in a consistent scientific way.

