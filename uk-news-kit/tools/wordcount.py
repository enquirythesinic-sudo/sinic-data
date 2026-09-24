"""計正文字數（中文字 + 英文字詞 + 數字各算一個）。範圍 300–450。

用法：python3 tools/wordcount.py posts-uk/YYYY-MM-DD/post.md
"""
import re
import sys

from common import sections

LOW, HIGH = 300, 450


def count(text):
    cjk = len(re.findall(r"[一-鿿]", text))
    words = len(re.findall(r"[A-Za-z]+|\d[\d,.]*", text))
    return cjk + words


def main():
    body = sections(sys.argv[1]).get("正文", "")
    if not body:
        sys.exit("BLOCK 搵唔到「# 正文」")
    n = count(body)
    status = "OK" if LOW <= n <= HIGH else "BLOCK"
    print(f"{status} 正文 {n} 字（範圍 {LOW}–{HIGH}）")
    sys.exit(0 if status == "OK" else 1)


if __name__ == "__main__":
    main()
