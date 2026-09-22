# Dealer Portal 中文圖文審閱

內容唯一來源：../../projects/dealer-portal/案例.md。預覽為未定稿本機審閱，不是公開網站。

在儲存庫根目錄執行：

```sh
python3 previews/dealer-portal/build.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory previews/dealer-portal
```

開啟 http://127.0.0.1:8765/ 。換電腦先 git pull，再執行上述指令。修改中文稿後重建並重新整理瀏覽器。

版型樣式已保存於 template.css，不依賴另一個網站資料夾。未提供字型時使用系統替代字型。index.html 與 media 為本機產物，不重複提交；圖片來源保存在專案 assets。互動與排版仍為簡化審閱版。
