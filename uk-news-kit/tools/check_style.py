"""檢查正文同標題：粵語口語字、半形標點、禁用字、無主語句。

用法：python3 tools/check_style.py posts-uk/YYYY-MM-DD/post.md
BLOCK 一定要改；WARN 要人手判斷。
"""
import re
import sys

from common import sections

COLLOQUIAL = "嘅咗喺唔啲冇嘢睇佢嚟乜哋嗰攞諗咁噉俾畀緊晒"
BANNED = ["震撼", "驚人", "崩盤", "必將", "注定", "暴雷", "恐慌", "揭秘", "真相"]
NO_SUBJECT = ["有分析認為", "市場普遍相信", "市場普遍認為", "有意見認為", "有專家指"]
# 中文字旁邊嘅半形標點
HALF_PUNCT = re.compile(r"(?<=[一-鿿])[,;:!?]|[,;:!?](?=[一-鿿])|(?<=[一-鿿])\((?=[一-鿿])")


def check(name, text):
    blocks, warns = [], []
    for i, line in enumerate(text.splitlines(), 1):
        for ch in sorted(set(line) & set(COLLOQUIAL)):
            blocks.append(f"{name} 第{i}行：粵語口語字「{ch}」")
        for w in BANNED:
            if w in line:
                blocks.append(f"{name} 第{i}行：禁用字「{w}」")
        for w in NO_SUBJECT:
            if w in line:
                blocks.append(f"{name} 第{i}行：無主語句「{w}」")
        if HALF_PUNCT.search(line):
            warns.append(f"{name} 第{i}行：中文旁邊有半形標點")
        if name == "正文" and re.search(r"[*_`#>\[\]]", line) and not line.lstrip().startswith("#"):
            warns.append(f"{name} 第{i}行：有 markdown 符號，貼上 Facebook 會變亂碼")
    return blocks, warns


def main():
    s = sections(sys.argv[1])
    blocks, warns = [], []
    for name in ("標題選項", "正文"):
        if name not in s:
            blocks.append(f"搵唔到「# {name}」")
            continue
        b, w = check(name, s[name])
        blocks += b
        warns += w
    for w in warns:
        print(f"WARN {w}")
    for b in blocks:
        print(f"BLOCK {b}")
    if not blocks and not warns:
        print("OK 冇發現問題")
    sys.exit(1 if blocks else 0)


if __name__ == "__main__":
    main()
