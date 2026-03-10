def run(lines: list[str]) -> dict:
    """
    Baseline-Agent: orchestriert noch nichts.
    """
    return {
        "tasks": [],
        "graph": {
            "nodes": [],
            "edges": []
        },
        "plan": {
            "order": [],
            "has_cycle": False
        },
        "summary": "",
        "steps": []
    }
