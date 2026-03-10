# Test: Summarizer

## Natürliche Sprache
Der Summarizer soll eine Summary mit Task-Anzahl erzeugen.

## Maschinenlesbare Struktur
input:
  tasks:
    - id: "build"
      description: "compile"
      deps: []
  plan_result:
    order:
      - "build"
    has_cycle: false

expected_contains:
  "1 task"
