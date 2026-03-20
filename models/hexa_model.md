# Mathematical Model of Hexa-Nizam

We define six state variables:

P(t) = Physical  
B(t) = Biological  
C(t) = Cognitive  
T(t) = Temporal  
S(t) = Spiritual  
J(t) = Social (Justice)

## System Dynamics

dP/dt = a1*P - b1*entropy  
dB/dt = a2*B + f(P) - decay  
dC/dt = a3*C + g(B) - noise  
dT/dt = constant renewal cycle  
dS/dt = a5*S + h(C) - deviation  
dJ/dt = a6*J + k(S) - conflict  

## Coupling Functions

f(P): Physical → Biological  
g(B): Biological → Cognitive  
h(C): Cognitive → Spiritual  
k(S): Spiritual → Social  

## Interpretation
Each layer is dynamically coupled, forming a nonlinear system.

