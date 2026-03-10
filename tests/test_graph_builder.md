# Test: Graph Builder

## Natürliche Sprache
Der Graph Builder soll aus Tasks Nodes und Edges erzeugen.

## Maschinenlesbare Struktur
input:
  tasks:
    - id: "build"
      description: "compile"
      deps: []
    - id: "test"
      description: "run tests"
      deps: ["build"]

expected:
  nodes_count: 2
  edges_count: 1
