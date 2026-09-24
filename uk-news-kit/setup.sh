#!/usr/bin/env bash
# 安裝出圖同出 Word 檔需要嘅工具。已裝就會跳過，每次開工跑一次。
set -e
cd "$(dirname "$0")"
python3 -c "import playwright, docx" 2>/dev/null || pip install -q playwright python-docx
if [ ! -f fonts/700.css ]; then
  tmp=$(mktemp -d)
  (cd "$tmp" && npm pack @fontsource/noto-sans-tc@5 --silent >/dev/null && tar xzf fontsource-noto-sans-tc-*.tgz)
  mkdir -p fonts
  cp "$tmp"/package/{400,700,900}.css fonts/
  cp -r "$tmp"/package/files fonts/
  rm -rf "$tmp"
fi
echo "setup OK"
