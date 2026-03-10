# Test: Planner

## Natürliche Sprache
Der Planner soll eine gültige Reihenfolge ohne Zyklus erzeugen.

## Maschinenlesbare Struktur
input:
  graph:
    nodes:
      - "build"
      - "test"
    edges:
      - from: "build"
        to: "test"

expected:
  has_cycle: false
  first_task: "build"
