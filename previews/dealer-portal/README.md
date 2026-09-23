# 舊簡化審閱頁（停止維護）

Dealer Portal 已改用 `portfolio-website` 正式模板，不再執行此處 build.py。

在相鄰 `portfolio-website` 執行 `npm ci`（初次還原），再執行 `npm run dev -- --host 127.0.0.1`，開啟終端顯示的網址並加上 `/#/dealer-portal`。

唯一正文來源是相鄰網站的 `src/data/cases/dealer-portal.ts`，可直接修改；舊重建腳本已停用。編輯方式見網站 `docs/content-to-website.md`。
