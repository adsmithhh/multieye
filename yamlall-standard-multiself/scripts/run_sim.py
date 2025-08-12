#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
from yamlall.sim_runner import run

def main():
    p = argparse.ArgumentParser(description="Run standard_multiself with α-barrier model.")
    p.add_argument("--yaml", required=True, help="Path to YAML spec")
    p.add_argument("--tau", type=float, default=1e-9, help="Coherence time [s]")
    p.add_argument("--e-base", type=float, default=0.0, help="Baseline energy [J]")
    p.add_argument("--k-leak", type=float, default=0.0, help="Leakage coefficient (dimensionless)")
    p.add_argument("--emit-json", type=str, default=None, help="Write JSON report to file")
    args = p.parse_args()

    report = run(args.yaml, args.tau, args.e_base, args.k_leak)

    if args.emit_json:
        Path(args.emit_json).write_text(json.dumps(report, indent=2))
        print(f"Report written to {args.emit_json}")
    else:
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    sys.exit(main())
