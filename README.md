# Local Task Dependency Planner (Offline, CPU-only)

Dieses Projekt analysiert Tasks mit Abhängigkeiten und erzeugt einen ausführbaren Plan.
Es arbeitet vollständig offline, benötigt keine GPU und verwendet keine KI-Modelle.

Funktionen:
- Tasks mit Abhängigkeiten einlesen
- Abhängigkeitsgraph aufbauen
- ausführbare Reihenfolge planen (Topological Sort)
- Zyklen erkennen
- Plan und kurze Summary erzeugen

Das Projekt demonstriert:
- Graph-Denken
- deterministische Planung
- einfache Dependency-Analyse
- Prompt-Driven Development (PDD)

## Projektstruktur

/src  
    parser.py  
    graph_builder.py  
    planner.py  
    summarizer.py  
    agent.py  

/docs  
    architecture.md  

/tests  
    test_parser.md  
    test_graph_builder.md  
    test_planner.md  
    test_summarizer.md  
    test_agent.md  

hardware-requirements.md  
instructions.md  
README.md  
credits.md

## Hardware Requirements

Dieses Projekt ist vollständig lokal ausführbar und benötigt keine spezielle Hardware.
Siehe `hardware-requirements.md`.

## Lizenz

MIT License.

## Credits

Siehe `credits.md`.
