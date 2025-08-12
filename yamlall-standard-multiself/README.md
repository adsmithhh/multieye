# YAMLALL — Standard Multiself (α-barrier edition)

This repository hosts a minimal, reproducible scaffold for the **standard_multiself** simulation with an
**α-as-internal-resistance** (fine-structure constant) model embedded as a first-class concept.

- **Core idea:** Treat the electromagnetic coupling (α ≈ 1/137) as a *consistency barrier / energetic cost* that
  modulates entanglement stability and interaction bandwidth in electron-like agents.
- **Scope:** Run a simple pipeline that reads `yaml/standard_multiself_001.yaml`, injects an α-barrier into
  the reasoning/simulation step, and emits a lightweight report to STDOUT (and JSON if requested).

> Design goal: small, auditable, easy to fork, with room to grow into your larger lab structure.

## Repo layout

```
yamlall-standard-multiself/
├─ src/yamlall/
│  ├─ __init__.py
│  ├─ alpha_barrier.py        # α-barrier math, constants, and helpers
│  └─ sim_runner.py           # simple loader + executor reading the YAML spec
├─ scripts/
│  └─ run_sim.py              # CLI entry
├─ yaml/
│  └─ standard_multiself_001.yaml
├─ docs/
│  └─ OVERVIEW.md
├─ tests/
│  └─ test_alpha_barrier.py
├─ .github/workflows/ci.yml   # lint + tests
├─ requirements.txt
├─ LICENSE
└─ README.md
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# Run with default YAML
python scripts/run_sim.py --yaml yaml/standard_multiself_001.yaml --emit-json report.json
cat report.json
```

## α-barrier model (minimal)

Let τ be an effective coherence time for a unit process. We model an *irreducible energetic cost* as:
\[ E_\text{cost} = \alpha \cdot \frac{\hbar}{\tau} \]
with optional terms for leakage and scaling:
\[ E_\text{eff} = E_\text{base} + k\_\text{leak}\,\alpha^2 + \alpha\,\frac{\hbar}{\tau}. \]

This is deliberately modest: it’s an auditable hook you can expand in later commits.

## Roadmap (suggested)

- [ ] Add chamber registry IO (`standard_registry/standard_*.yaml`).
- [ ] Add Layer-2 / Layer-3 echo dynamics gated by α.
- [ ] Implement entanglement bandwidth caps via α-imposed impedance.
- [ ] Export full **inout.yaml** (reflex logger + anchors) on each run.
- [ ] Publish a `pda veritas` PDF report from run artifacts.

## License

MIT — open for research and modification.
