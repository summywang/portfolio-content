# Git 與跨電腦還原規範

本文件供使用者與 AI 在維護 `portfolio`（內容規劃）及 `portfolio-website`（實際網站）時共同遵守。兩者是獨立 Git repository；GitHub 是版本與跨電腦同步來源，Google Drive 僅作額外備份，不取代 commit、push、pull。

## Repository 與可見性

- `portfolio` 保存訪談、內部判斷、案例草稿、來源與素材，必須維持 **Private**。
- `portfolio-website` 保存可部署的網站原始碼，預設 **Private**；公開網站使用部署平台，不以公開工作歷史作為必要條件。
- 未經使用者明確同意，不得將任一 repository 改為 Public，也不得建立含機密內容的公開 fork、gist 或分享連結。

## 每次提交前，AI 必須檢查

1. 先看 `git status` 與 staged diff，確認沒有無關檔案、刪除或大量二進位變更。
2. 搜尋秘密資料：API key、access token、密碼、private key、cookie、session、服務帳戶、憑證、`.env*` 與本機設定。
3. 檢查個資與保密內容：未公開姓名、email、電話、客戶／雇主內部資料、研究參與者資訊、NDA 內容及未授權設計素材。
4. 檢查新二進位檔與檔案大小；單檔超過 10 MB 先說明，超過 50 MB 不直接提交，接近 GitHub 100 MB 硬限制時必須改用其他方案。
5. 確認沒有 `node_modules/`、`dist/`、coverage、快取、系統檔或編輯器暫存檔。
6. 若秘密曾被加入 commit，單純刪檔不足；先停止 push、撤銷或輪替秘密，再清理歷史。

## 可以與不可以提交的內容

可以提交：

- Markdown、網站原始碼、設定範例、lockfile、必要的小型圖片與短影片。
- `.env.example`，但值只能是假的占位字串，不得放真實帳密。
- 有明確使用權的字型、圖片、影片與 PDF。

不可提交：

- `.env`、token、密碼、private key、cookies、憑證與本機登入狀態。
- `.claude/settings.local.json` 等只屬於單一電腦的設定。
- `node_modules/`、`dist/`、測試輸出、快取與可重新生成的檔案。
- 未確認授權或受 NDA 約束的素材。Private repository 不是規避授權或保密義務的方法。

## 圖片與影片策略

- 網站目前的短 MP4 單支約 1–2 MB，屬於介面動態展示，直接隨網站原始碼保存可確保版面、靜音循環、自動播放與離線還原，暫時不使用 Vimeo。
- 圖片優先使用適合網頁的 WebP／AVIF；需要透明或無損時才使用 PNG。提交前移除不必要的 EXIF／位置資訊並合理壓縮。
- 短而關鍵的 UI 示範影片可留在 repository；使用 MP4/H.264，必要時補 WebM，並保留 poster、字幕或文字替代。
- 長影片、訪談、旁白展示、需串流分析或單檔明顯增大時，才評估 Vimeo。使用 Vimeo 前要檢查方案限制、嵌入隱私、追蹤、密碼與 domain-level privacy；外部影片仍需保留原始檔的獨立備份。
- Git LFS 只在必須版本化大型原始素材時採用；它有儲存與流量配額，不能當一般影片 CDN。

## 換電腦還原

1. 安裝 Git、Node.js 的相容版本與必要開發工具，設定 Git 身分及 GitHub SSH key 或其他安全登入方式。
2. 將兩個 Private repositories clone 到本機；建議放在一般開發資料夾，不直接依賴雲端同步資料夾處理 `.git`。
3. 在網站 repository 執行 `npm ci`，不可複製舊電腦的 `node_modules`。
4. 如專案需要秘密資料，從密碼管理器或部署平台重新建立 `.env`；不得從 Git 歷史取回。
5. 執行 `npm run typecheck`、`npm run build`、`npm run test:sites`，再啟動本地預覽確認圖片、影片與字型都可載入。
6. 比對 `git status`；乾淨工作樹與通過檢查後，才視為還原完成。

## 日常同步

- 開始工作前先 pull；結束一個可辨識的變更後 commit 並 push。
- 換電腦前確認所有必要修改已 commit 且 push 成功，不以 Google Drive 的綠色勾選代替 GitHub 狀態。
- 啟用 GitHub 帳號兩步驟驗證；SSH key 使用 passphrase，遺失或淘汰的裝置要移除 key。
- Private repository 只邀請必要協作者，定期檢查成員、deploy keys、GitHub Apps、Actions secrets 與部署權限。
- 重要內容另保留可恢復備份；GitHub 是版本控制服務，不是唯一備份。

