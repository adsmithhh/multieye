from dataclasses import dataclass
from typing import Optional

# Fundamental constants (SI)
HBAR = 1.054_571_817e-34  # J·s
ALPHA = 1.0 / 137.035999084  # fine-structure constant (CODATA 2018/2022-ish)

@dataclass
class AlphaBarrierConfig:
    tau: float  # coherence time [s]
    e_base: float = 0.0  # baseline energy [J]
    k_leak: float = 0.0  # leakage coefficient (dimensionless; multiplies alpha^2)

def energetic_cost(cfg: AlphaBarrierConfig) -> float:
    """Irreducible energetic cost due to α-barrier.
    E_cost = α * (ħ / τ)
    """
    if cfg.tau <= 0:
        raise ValueError("tau must be > 0")
    return ALPHA * (HBAR / cfg.tau)

def effective_energy(cfg: AlphaBarrierConfig) -> float:
    """Simple effective energy model.
    E_eff = E_base + k_leak * α^2 + α * (ħ / τ)
    """
    return (
        cfg.e_base
        + cfg.k_leak * (ALPHA ** 2)
        + energetic_cost(cfg)
    )
