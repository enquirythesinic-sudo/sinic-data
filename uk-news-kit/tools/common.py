"""讀 post.md 嘅共用函數。post.md 用「# 章節名」分節。"""
import re
from pathlib import Path


def sections(path):
    text = Path(path).read_text(encoding="utf-8")
    out, name = {}, None
    for line in text.splitlines():
        m = re.match(r"^# (.+)$", line)
        if m:
            name = m.group(1).strip()
            out[name] = []
        elif name:
            out[name].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}
