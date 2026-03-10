# Test: Parser

## Natürliche Sprache
Der Parser soll Tasks mit Dependencies aus Zeilen extrahieren.

## Maschinenlesbare Struktur
input:
  lines:
    - "build:compile sources:"
    - "test:run tests:build"

expected:
  tasks_count: 2
  second_task_deps_contains: "build"
