from yamlall.alpha_barrier import AlphaBarrierConfig, energetic_cost, effective_energy, ALPHA, HBAR
import math
import pytest

def test_positive_tau():
    cfg = AlphaBarrierConfig(tau=1e-9)
    assert energetic_cost(cfg) > 0

def test_tau_nonpositive():
    with pytest.raises(ValueError):
        energetic_cost(AlphaBarrierConfig(tau=0))

def test_effective_energy_monotonic_in_tau():
    cfg1 = AlphaBarrierConfig(tau=1e-9)
    cfg2 = AlphaBarrierConfig(tau=1e-6)
    assert effective_energy(cfg1) > effective_energy(cfg2)
