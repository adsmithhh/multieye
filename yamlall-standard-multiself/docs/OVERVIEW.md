# Overview

This doc explains the minimal α-barrier integration for **standard_multiself**.
The goal is to provide a small, testable hook:
- Input: a YAML spec (kept as-is for now)
- Process: compute an effective energy with α as an internal resistance
- Output: a small JSON report

You can expand this by mapping YAML fields to τ, k_leak, and e_base, or by
propagating α into chamber dynamics and echo layers.
