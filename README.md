host.json 是 Azure Functions 的全域設定檔案

extensionBundle 設定
作用：定義要使用的 Azure Functions 擴展套件（Extension Bundle）版本範圍。
id：指定要引用的擴展套件。
version：指定版本範圍，[2.*, 3.0.0) 表示：
支援 2.x 版本（含）到 3.0.0 版本（不含）。
用途：
用於支援各種 Azure Functions 綁定（如 Timer Trigger、Event Grid、Blob Trigger 等）。
