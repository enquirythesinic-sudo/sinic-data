# 英國新聞 Routine 工具

將呢個資料夾**入面嘅全部檔案**上載到 `news` repo 最外層（即係 `news/setup.sh`、`news/graphics/`、`news/tools/`）。

## 檔案

| 檔案 | 用途 |
|---|---|
| `setup.sh` | 安裝出圖同出 Word 檔需要嘅工具同中文字體，每次開工跑一次 |
| `settings.json` | 專頁名（`brand`）同預設背景（`theme`：`navy` 深藍 #1f3443／`brown` 啡 #4a2d1f） |
| `graphics/card.html` | 圖卡設計，用 IG palette。改顏色：改最頂 `:root` 嗰幾行 |
| `graphics/render.py` | 由 JSON 出 1080×1350 PNG，QC 唔過會 exit 1 |
| `tools/check_style.py` | 檢查口語字、禁用字、無主語句、半形標點 |
| `tools/wordcount.py` | 檢查正文字數（300–450） |
| `tools/make_docx.py` | 將 post.md 連圖轉做 Word 檔，俾人手覆核 |
| `examples/` | 五款圖卡同一篇範例稿 |

## 圖卡類型

| type | 用途 | 數據 |
|---|---|---|
| `stat` | 一個主數字 + 最多 3 個支撐數字 | `items: [{value, unit, label, key}]`，`key: true` 嗰個做大字 |
| `bar` | 3–6 項比大細 | `items: [{label, value, key}]`、`unit` |
| `line` | 4 點以上時間變化 | `points: [{label, value, key}]`、`unit` |
| `policy` | 政策、規則、公告重點 | `points: ["…", "…"]`，2–4 點 |
| `quote` | 一句關鍵引述 | `text`、`speaker` |

單張圖想用另一個背景，喺 card.json 加 `"theme": "brown"`。

全部類型都要：`kicker`（小標）、`title`（標題，用 `\n` 手動換行，唔好拆散詞語）、`source`（來源）。
數值想保留小數位（例如 `4.0`），加 `"display": "4.0"`。

## 用法

```bash
./setup.sh
python3 graphics/render.py card.json posts-uk/2026-09-25/card.png
python3 tools/check_style.py posts-uk/2026-09-25/post.md
python3 tools/wordcount.py  posts-uk/2026-09-25/post.md
python3 tools/make_docx.py  posts-uk/2026-09-25/post.md
```
