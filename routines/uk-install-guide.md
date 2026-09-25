# 英國每日新聞 Routine：安裝指南

呢個包入面有三樣嘢：

| 檔案 | 用途 |
|---|---|
| `news-repo/` | 上載去你 GitHub `news` repo 嘅工具（出圖、檢查、出 Word 檔） |
| `routine-prompt.txt` | 貼入 Routine 嘅 prompt |
| `安裝指南.md` | 呢份文件 |

全部步驟都喺**另一個 account** 做。

---

## 第一步：將工具上載去 `news` repo

1. 喺電腦解壓呢個 zip。
2. 打開 GitHub 上面嘅 `news` repo，撳 **Add file → Upload files**。
3. 打開 `news-repo` 資料夾，**揀晒入面所有嘢**（唔係揀 `news-repo` 資料夾本身），拖入 GitHub 個上載框。
   - 要包括 `graphics`、`tools`、`examples` 三個資料夾，同埋 `setup.sh`、`settings.json`、`TOOLS.md`、`.gitignore`。
   - `.gitignore` 係隱藏檔案。Mac 喺 Finder 撳 `Cmd + Shift + .` 就見到；Windows 喺檔案總管「檢視」勾選「隱藏的項目」。
4. 最底 commit message 填「加入英國新聞工具」，揀 **Commit directly to the main branch**，撳 **Commit changes**。
5. 上載完，repo 最外層應該見到 `setup.sh`，唔係一個叫 `news-repo` 嘅資料夾。如果見到 `news-repo/`，即係拖錯咗成個資料夾，要刪走重新上載。

**想改專頁名或者背景色**：喺 GitHub 打開 `settings.json`，撳鉛筆圖示修改：
```json
{"brand": "英國觀察", "theme": "navy"}
```
- `brand`：印喺每張圖右下角嘅專頁名
- `theme`：`navy`（深藍 #1f3443）或者 `brown`（啡 #4a2d1f）

---

## 第二步：俾 Claude 用到 `news` repo

1. 用另一個 account 登入 claude.ai，打開 **Settings → Connectors**，確認 GitHub 已經連接。
2. 確認已經安裝 Claude GitHub App，而且權限包括 `news` repo：
   https://github.com/apps/claude/installations/select_target

---

## 第三步：設定 Environment 網絡

Routine 開工時要下載兩樣嘢：Python 套件（pypi.org）同中文字體（registry.npmjs.org）。
預設網絡設定通常已經容許。如果試跑時 `setup.sh` 失敗，就要改 environment 設定：
- 打開 environment 設定，Network access 揀較寬嘅權限；或者
- 將 `pypi.org`、`files.pythonhosted.org`、`registry.npmjs.org` 加入 allowed domains。

字體下載唔到都唔會停，只係會改用後備字體，圖冇咁靚。

建議順手加埋呢啲網站，Routine 可以直接打開官方原文，唔使靠搜尋摘要：
`www.bankofengland.co.uk`、`www.ons.gov.uk`、`www.gov.uk`、`obr.uk`、`commonslibrary.parliament.uk`、
`ifs.org.uk`、`www.resolutionfoundation.org`、`niesr.ac.uk`、`migrationobservatory.ox.ac.uk`、`institute.global`

---

## 第四步：開 Routine

1. 新增一個 Routine：
   - **Repository**：揀 `news`
   - **每次開新 session**：開
   - **時間**：cron `0 6 * * *`（UTC 06:00，即英國 07:00、香港 14:00；英國 10 月 25 日轉冬令後變成英國 06:00）
   - **通知**：開 push 或者 email，每日出稿會通知你標題同第一句
2. **Prompt**：打開 `routine-prompt.txt`，全選 copy，貼入去。
3. 如果 repo 設定有「容許 push 去任何分支」之類嘅選項，要開。Routine 要將紀錄推去 `main`，否則下次開工會唔記得之前寫過咩。

---

## 第五步：試跑

1. 撳 **Run now**。
2. 跑完之後，去 `news` repo 睇 `main` 分支有冇多咗：
   - `posts-uk/今日日期/`，入面有 `post.md`、`card.png`、`post.docx`
   - `uk-ledger.csv`
   - `uk-backlog.md`
3. 睇 Routine 嘅最終回覆，最尾應該有：
   - `check_style.py`、`wordcount.py` 嘅結果
   - `CONTENT_READY=YES`、`UPLOAD=SUCCESS`
   - 「流程含糊或者卡住嘅位」

**常見問題**
| 情況 | 原因同解決方法 |
|---|---|
| `UPLOAD=FAILED` | 冇權限 push 去 `main`：睇第二步同第四步第 3 點 |
| `setup.sh` 失敗 | 網絡擋住：睇第三步 |
| 圖入面中文字好醜 | 字體下載唔到：睇第三步，加 `registry.npmjs.org` |
| 「今日無合格選題」 | 正常，唔係錯誤。睇 `posts-uk/今日日期/no-post.md` 了解原因 |

試跑咗之後，將最終回覆貼返俾我，我幫你睇下有冇要調整。
