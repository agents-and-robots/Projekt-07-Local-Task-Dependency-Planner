# Architektur – Local Task Dependency Planner

## Module

- parser.py – parst Tasks und Dependencies
- graph_builder.py – baut Abhängigkeitsgraph
- planner.py – plant ausführbare Reihenfolge
- summarizer.py – erzeugt Summary
- agent.py – orchestriert den Prozess

## Datenfluss

1. Parser erzeugt Task-Liste
2. Graph Builder erzeugt Graph
3. Planner berechnet Reihenfolge
4. Summarizer erzeugt Summary
5. Agent orchestriert alles
