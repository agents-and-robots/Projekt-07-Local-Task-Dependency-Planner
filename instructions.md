# LLM Instructions – Local Task Dependency Planner (Offline)

Diese Datei definiert alles, was ein LLM benötigt, um dieses Projekt vollständig selbständig umzusetzen:
- Input/Output-Protokoll
- Modul- und Agenten-Logik
- Regelwerk
- Hardware-Constraints
- How-To-Use

---

## 1. Ziel

Erstelle ein System, das Tasks mit Abhängigkeiten analysiert, einen ausführbaren Plan erzeugt,
Zyklen erkennt und eine kurze Summary liefert — vollständig offline.

---

## 2. Hardware Constraints

Dieses Projekt muss vollständig auf normaler Consumer-Hardware lauffähig sein:

- CPU-only
- keine GPU-Abhängigkeiten
- keine Modelle > 1 GB
- keine externen APIs oder Cloud-Dienste
- alles offline
- Python-Standardbibliothek

---

## 3. Modul-Spezifikationen

### 3.1 Parser (/src/parser.py)

Signatur: parse(lines: list[str]) -> list[dict]

Aufgabe:
- Tasks aus einfachen Zeilen parsen
- Format-Beispiel:
  - "task_id:do something:dep1,dep2"

Rückgabeformat:
- tasks: Liste von Objekten:
  - id: string
  - description: string
  - deps: list[string]

---

### 3.2 Graph Builder (/src/graph_builder.py)

Signatur: build(tasks: list[dict]) -> dict

Aufgabe:
- Abhängigkeitsgraph aufbauen

Rückgabeformat:
- graph:
  - nodes: list[string]
  - edges: list[dict]
    - from: string
    - to: string

---

### 3.3 Planner (/src/planner.py)

Signatur: plan(graph: dict) -> dict

Aufgabe:
- ausführbare Reihenfolge planen (Topological Sort)
- Zyklen erkennen

Rückgabeformat:
- order: list[string] (Task-IDs)
- has_cycle: bool

---

### 3.4 Summarizer (/src/summarizer.py)

Signatur: summarize(tasks: list[dict], plan_result: dict) -> str

Aufgabe:
- kurze, deterministische Summary erzeugen
- z. B. Anzahl Tasks, ob Zyklen existieren, erste Tasks im Plan

---

### 3.5 Agent (/src/agent.py)

Signatur: run(lines: list[str]) -> dict

Aufgabe:
- orchestriert parser, graph_builder, planner, summarizer

Rückgabeformat:
- tasks: list[dict]
- graph: dict
- plan: dict
- summary: string
- steps: list[str]

---

## 4. Orchestrator-Logik

1. tasks = parse(lines)
2. graph = build(tasks)
3. plan_result = plan(graph)
4. summary = summarize(tasks, plan_result)
5. Ergebnis zurückgeben

---

## 5. Regelwerk / Constraints

### Parser
- deterministisch
- ignoriert leere Zeilen und Kommentare (#)
- wenn keine Dependencies: leere Liste

### Graph
- jeder Task wird Node
- jede Dependency wird Edge (dep → task)

### Planner
- Topological Sort
- wenn Zyklus: has_cycle = true, order ggf. unvollständig

### Summary
- deterministisch
- z. B.:
  - "N tasks, M edges, cycle: yes/no"

---

## 6. Aufgaben an das LLM

Das LLM soll:

1. parser.py implementieren  
2. graph_builder.py implementieren  
3. planner.py implementieren  
4. summarizer.py implementieren  
5. agent.py implementieren  
6. architecture.md ergänzen  
7. Tests in /tests aktualisieren  

---

## 7. How-To-Use (für Code-Assistenten)

1. Öffne das Repository.  
2. Öffne `instructions.md`.  
3. Markiere den gesamten Inhalt.  
4. Sende ihn an deinen Code-Assistenten mit:

„Lies diese instructions.md vollständig. Implementiere dann alle beschriebenen Module und Dateien. Halte dich strikt an das Input/Output-Protokoll, das Regelwerk und die Hardware-Constraints. Beginne mit parser.py.“

Damit kann ein LLM das Projekt vollständig autonom umsetzen.
