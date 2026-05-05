# PPT-video-converter

# 📽️ PPT to Video Converter (PPT 轉影片自動化工具)

這是一個基於 Python 開發的桌面應用程式，能夠將帶有「備忘稿」的 PowerPoint (PPTX) 檔案，全自動轉換為帶有 AI 語音配音、精準同步的 MP4 影片，並支援加入背景音樂。

適合用於製作**教學影片、自動化簡報報告、有聲書影片**等場景。

---

## ✨ 核心功能 (Features)

* **🤖 全自動 AI 配音**：自動提取 PPT 投影片內的「備忘稿」，並透過微軟 Edge TTS 轉換為自然流暢的中文語音。
* **⏱️ 精準影音同步**：自動根據每頁備忘稿語音的長度，調整該頁投影片在影片中的停留時間。
* **🎵 支援背景音樂 (BGM)**：可選擇放入 BGM，程式會自動循環播放並智慧調整音量。
* **⚙️ 智慧防呆設計**：若投影片沒有備忘稿，可自訂該頁面的停留（沉默）秒數。
* **🧹 乾淨無痕**：轉檔完成後，自動清理所有暫存的 PDF、圖片與語音檔，不佔用硬碟空間。
* **🖥️ 友善的圖形介面 (GUI)**：提供直覺的視窗介面與進度條，非技術人員也能輕鬆「一鍵轉檔」。

---

## 🛠️ 系統需求與前置準備 (Prerequisites)

本軟體內建了影片合成所需的輕量版 FFmpeg 引擎，一般使用者**無需手動安裝 FFmpeg**。但本程式依賴外部軟體來進行高品質的 PPT 轉 PDF 渲染，因此使用前請確保已安裝以下軟體：

### 必須安裝：LibreOffice
* **Windows / macOS / Linux**: 請前往 [LibreOffice 官方網站](https://www.libreoffice.org/) 免費下載並安裝最新版本。

> **💡 提示**：在軟體介面中，我們提供了快速帶入 `Windows 預設路徑` 與 `macOS 預設路徑` 的按鈕，若您安裝在預設位置，只需點擊按鈕即可自動配置。

---

## 🚀 快速安裝與使用 (For General Users)

如果您只是想使用這個軟體，不需要懂程式碼，請依循以下步驟：

1. 前往本專案的 [**Releases 頁面**](https://github.com/stingrayShih/PPT-video-converter/releases)。
2. 下載最新的安裝檔（如 `PPT_to_Video_Converter_v1.0.zip`）。
3. 解壓縮後，雙擊執行 `setup.exe` 進行安裝。
4. 安裝完成後，從桌面開啟「PPT轉影片自動化工具」。
5. **使用流程**：
   * 選擇您的目標 `.pptx` 檔案。
   * (可選) 選擇您的 `.mp3` 檔案作為背景音樂。
   * 確認 LibreOffice 的執行檔路徑正確。
   * 點擊「開始轉換」，等待進度條跑完即可在 PPT 同目錄下獲得您的 MP4 影片！

---

## 💻 開發者指南 (For Developers)

如果您想從原始碼執行或修改本專案，請參考以下步驟：

### 1. 取得專案並建立虛擬環境
```bash
git clone https://github.com/stingrayShih/PPT-video-converter.git
cd PPT-video-converter
python -m venv venv
