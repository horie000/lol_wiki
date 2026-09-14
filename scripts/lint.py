#!/usr/bin/env python3
"""Wiki のLint入口。出典タグ、生成済みの効率・分類・パワースパイクを検証する。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKERS = (
    ROOT / "scripts" / "data_dragon_tags.py",
    ROOT / "scripts" / "gold_efficiency.py",
    ROOT / "scripts" / "item_synergy.py",
    ROOT / "scripts" / "power_spikes.py",
)


def main() -> int:
    for checker in CHECKERS:
        result = subprocess.run([sys.executable, str(checker), "--check"], cwd=ROOT)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
