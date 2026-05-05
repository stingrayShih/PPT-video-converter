[Setup]
; 應用程式的基本資訊
AppName=PPTtoVideoConverter
AppVersion=1.0
AppPublisher=您的名字或團隊名稱
AppPublisherURL=https://github.com/您的GitHub帳號/您的專案

; 安裝預設路徑 (會安裝在 C:\Program Files (x86)\PPTtoVideoConverter)
DefaultDirName={autopf}\PPTtoVideoConverter
DisableProgramGroupPage=yes

; 輸出的安裝檔設定
OutputDir=.\release
OutputBaseFilename=PPT_to_Video_Converter_Setup_v1.0
Compression=lzma
SolidCompression=yes

; 讓安裝檔支援高 DPI 螢幕
WizardStyle=modern

[Tasks]
; 預設勾選建立桌面捷徑
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkablealone

[Files]
Source: "release\dist\main\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "release\dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; 建立開始菜單與桌面的捷徑
Name: "{autoprograms}\PPTtoVideoConverter"; Filename: "{app}\main.exe"
Name: "{autodesktop}\PPTtoVideoConverter"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
; 安裝完成後提供立即執行的選項
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,PPTtoVideoConverter}"; Flags: nowait postinstall skipifsilent

[Code]
// InitializeSetup 是一個內建函數，會在安裝程式剛啟動、畫面還沒出來前執行
function InitializeSetup(): Boolean;
begin
  MsgBox('【安裝前重要提醒】' + #13#10#13#10 +
         '本工具需要依賴「LibreOffice」才能將 PPT 順利轉換為影片。' + #13#10#13#10 +
         '如果您尚未安裝，請務必前往官方網站免費下載並安裝：' + #13#10 +
         'https://www.libreoffice.org/' + #13#10#13#10 +
         '(您可以先繼續完成本工具的安裝，之後再去安裝 LibreOffice 即可)', 
         mbInformation, MB_OK);
  
  // 回傳 True 代表允許安裝程式繼續執行
  Result := True;
end;