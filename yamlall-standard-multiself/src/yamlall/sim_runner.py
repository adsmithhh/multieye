import json
from dataclasses import dataclass
from typing import Any, Dict, Optional
import yaml

from .alpha_barrier import AlphaBarrierConfig, effective_energy

@dataclass
class RunConfig:
    tau: float = 1e-9   # default coherence time [s]
    e_base: float = 0.0
    k_leak: float = 0.0

def load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run(yaml_path: str, tau: float, e_base: float, k_leak: float) -> Dict[str, Any]:
    spec = load_yaml(yaml_path)
    cfg = AlphaBarrierConfig(tau=tau, e_base=e_base, k_leak=k_leak)
    e_eff = effective_energy(cfg)
    report = {
        "alpha_barrier": {
            "tau_s": tau,
            "e_base_J": e_base,
            "k_leak": k_leak,
            "effective_energy_J": e_eff,
        },
        "input_yaml_meta": {
            "path": yaml_path,
            "top_keys": list(spec.keys()) if isinstance(spec, dict) else None,
        },
    }
    return report
