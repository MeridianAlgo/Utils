"""Interactive launcher for the educational Python programs.

Run this script from the project root to explore each level:

    python main.py

The launcher will walk you through the available programs located under
`Documentation/Programs/` and call each script using `runpy` so you can
see the original source code while it executes.
"""

from __future__ import annotations

import runpy
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent
PROGRAMS: List[Dict[str, str]] = [
    {
        "option": "1",
        "title": "Level 1 – Python Fundamentals",
        "path": "Documentation/Programs/level1_fundamentals.py",
        "description": "Start here to review variables, control flow, and core syntax.",
        "resources": [
            "UTILS - Python Basics - Strings/strings_tutorial.py",
            "UTILS - Python Basics - Numbers/numbers_tutorial.py",
            "UTILS - Python Basics - Strings/README.md",
            "UTILS - Python Basics - Numbers/README.md",
        ],
    },
    {
        "option": "2",
        "title": "Level 2 – Intermediate Python",
        "path": "Documentation/Programs/level2_intermediate.py",
        "description": "Practice object-oriented design, file I/O, and NumPy/pandas workflows.",
        "resources": [
            "UTILS - Data Structures - Lists/lists.py",
            "UTILS - Data Structures - Arrays/arrays.py",
        ],
    },
    {
        "option": "3",
        "title": "Level 3 – Financial Python",
        "path": "Documentation/Programs/level3_financial.py",
        "description": "Work through portfolio analytics, indicators, and time value of money.",
        "resources": [
            "UTILS - Quantitative Methods - Time Series/time_series_tools.py",
            "UTILS - Technical Indicators/technical_indicators.py",
            "UTILS - News Fetching/fetchNews.js",
            "UTILS - News Fetching/README.md",
        ],
    },
    {
        "option": "4",
        "title": "Level 4 – Advanced Python for Finance",
        "path": "Documentation/Programs/level4_advanced.py",
        "description": "Run a mean-reversion backtest, machine learning pipeline, and vectorization demo.",
        "resources": [
            "UTILS - Advanced Quant Strategies/" if (BASE_DIR / "UTILS - Advanced Quant Strategies").exists() else "Documentation/Programs/level4_advanced.py",
            "UTILS - Quantitative Methods - Time Series/time_series_tools.py",
        ],
    },
    {
        "option": "5",
        "title": "Interactive Learning Platform (CLI)",
        "path": "UTILS - Learning Platform/learning_platform_cli.py",
        "description": "Guided lessons with quizzes and practice prompts covering Python essentials.",
        "resources": [
            "UTILS - Learning Platform/content.py",
            "Run host: python \"UTILS - Learning Platform/learning_platform_web.py\"",
        ],
        "interactive": True,
    },
]


def print_banner() -> None:
    """Display a high-level overview so the learner knows where to look."""
    print("=" * 80)
    print("FINANCE & AI UTILITIES – EDUCATIONAL PROGRAM LAUNCHER")
    print("=" * 80)
    print("Source folder: Documentation/Programs/")
    print("Open the corresponding *.py file in that folder while each level runs to follow along.\n")


def print_menu() -> None:
    """Show the user the available options."""
    print("Select a learning module to run:")
    for program in PROGRAMS:
        print(f"  {program['option']}. {program['title']}\n     ↳ File: {program['path']}\n     ↳ {program['description']}")
    print("  A. Run ALL levels in sequence")
    print("  Q. Quit the launcher")


def run_program(program: Dict[str, str]) -> None:
    """Execute a program by loading and running the target script path."""
    script_path = BASE_DIR / program["path"]
    print("\n" + "-" * 80)
    print(f"Launching {program['title']}")
    print(f"Reading source: {script_path.relative_to(BASE_DIR)}")
    print("Open this file in your editor to follow the inline comments while it runs.\n")
    runpy.run_path(str(script_path), run_name="__main__")
    resource_paths = program.get("resources", [])
    if resource_paths:
        print("Suggested follow-up resources:")
        for resource in resource_paths:
            print(f"  • {resource}")
    print("-" * 80 + "\n")


def run_all_programs() -> None:
    """Run all modules sequentially."""
    for program in PROGRAMS:
        if program.get("interactive"):
            print(f"\nSkipping {program['title']} during run-all because it requires interactive input. Run it from the main menu instead.\n")
            continue
        run_program(program)


def main() -> None:
    """Command loop for the launcher."""
    print_banner()
    while True:
        print_menu()
        choice = input("Enter option (1-4, A, or Q): ").strip().upper()
        if choice == "Q":
            print("Exiting the launcher. Happy learning!")
            break
        if choice == "A":
            run_all_programs()
            continue

        matched = next((p for p in PROGRAMS if p["option"] == choice), None)
        if matched:
            run_program(matched)
        else:
            print("Invalid selection. Please choose 1-4, A, or Q.\n")


if __name__ == "__main__":
    main()
