import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from converter import PPTConverter
from proglog import ProgressBarLogger

# 建立一個自訂的 Logger 來攔截 moviepy 的進度
class TkinterLogger(ProgressBarLogger):
    def __init__(self, root, progress_var):
        super().__init__()
        self.root = root
        self.progress_var = progress_var

    def bars_callback(self, bar, attr, value, old_value=None):
        # moviepy 生成影片時使用的進度條標籤通常是 't' (代表時間/幀數)
        if bar == 't':
            total = self.bars[bar]['total']
            if total > 0:
                percentage = (value / total) * 100
                # 使用 after 確保從背景執行緒安全地更新主執行緒的 GUI
                self.root.after(0, self.progress_var.set, percentage)

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PPT 轉影片自動化工具")
        self.root.geometry("550x450") # 把視窗稍微拉高一點容納進度條

        self.ppt_path = tk.StringVar()
        self.bgm_path = tk.StringVar()
        self.silent_sec = tk.DoubleVar(value=1.5)
        self.libreoffice_path = tk.StringVar(value="soffice") 

        self._build_ui()

    def _build_ui(self):
        # PPT 選擇
        tk.Label(self.root, text="PPT 檔案路徑:").pack(pady=(10, 0))
        frame_ppt = tk.Frame(self.root)
        frame_ppt.pack()
        tk.Entry(frame_ppt, textvariable=self.ppt_path, width=45).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_ppt, text="瀏覽", command=self.select_ppt).pack(side=tk.LEFT)

        # BGM 選擇
        tk.Label(self.root, text="BGM 檔案路徑 (可選):").pack(pady=(10, 0))
        frame_bgm = tk.Frame(self.root)
        frame_bgm.pack()
        tk.Entry(frame_bgm, textvariable=self.bgm_path, width=45).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_bgm, text="瀏覽", command=self.select_bgm).pack(side=tk.LEFT)

        # 沉默秒數
        tk.Label(self.root, text="無文字投影片停留秒數:").pack(pady=(10, 0))
        tk.Scale(self.root, from_=0.5, to=10.0, resolution=0.5, orient=tk.HORIZONTAL, variable=self.silent_sec).pack()

        # LibreOffice 路徑
        tk.Label(self.root, text="LibreOffice 執行檔路徑 (如有設定環境變數可保留 soffice):").pack(pady=(10, 0))
        tk.Entry(self.root, textvariable=self.libreoffice_path, width=55).pack(padx=5)

        # === 新增：進度條 UI ===
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate", variable=self.progress_var)
        self.progress_bar.pack(pady=15)

        # 狀態與執行按鈕
        self.status_label = tk.Label(self.root, text="準備就緒", fg="blue")
        self.status_label.pack(pady=5)

        self.run_btn = tk.Button(self.root, text="開始轉換", command=self.start_conversion, bg="green", fg="white", font=("Arial", 12, "bold"))
        self.run_btn.pack(pady=10)

    def select_ppt(self):
        path = filedialog.askopenfilename(filetypes=[("PowerPoint", "*.pptx *.ppt")])
        if path: self.ppt_path.set(path)

    def select_bgm(self):
        path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
        if path: self.bgm_path.set(path)

    def update_status(self, msg):
        self.root.after(0, lambda: self.status_label.config(text=msg))

    def start_conversion(self):
        if not self.ppt_path.get():
            messagebox.showwarning("警告", "請先選擇 PPT 檔案！")
            return

        # 鎖定按鈕，進度條歸零
        self.run_btn.config(state=tk.DISABLED)
        self.progress_var.set(0)
        
        # 啟動背景執行緒進行轉檔
        thread = threading.Thread(target=self.process_task)
        thread.daemon = True
        thread.start()

    def process_task(self):
        try:
            converter = PPTConverter(
                ppt_path=self.ppt_path.get(),
                bgm_path=self.bgm_path.get(),
                silent_sec=self.silent_sec.get(),
                libreoffice_path=self.libreoffice_path.get()
            )
            
            # 建立自訂的 logger 並傳入
            video_logger = TkinterLogger(self.root, self.progress_var)
            
            output_path = converter.run_pipeline(
                progress_callback=self.update_status, 
                video_logger=video_logger
            )
            
            # 確保最後進度條跑到 100%
            self.root.after(0, self.progress_var.set, 100.0)
            self.root.after(0, lambda: messagebox.showinfo("成功", f"影片已輸出至：\n{output_path}"))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("錯誤", f"發生錯誤：\n{str(e)}"))
            self.update_status("發生錯誤，請檢查設定。")
        finally:
            self.root.after(0, lambda: self.run_btn.config(state=tk.NORMAL))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
