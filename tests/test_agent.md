# Test: Agent

## Natürliche Sprache
Der Agent soll Tasks, Graph, Plan und Summary zurückgeben (Baseline: leer).

## Maschinenlesbare Struktur
input:
  lines:
    - "build:compile sources:"

expected:
  tasks: []
  plan:
    order: []
