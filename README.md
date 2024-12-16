功能說明
這個 Azure Function 程式旨在處理來自 Azure Event Grid 的事件，並將事件數據儲存到 MongoDB 中。當 Event Grid 發送一個事件時，這個 Function 會觸發，解析事件資料，並將其存儲為 MongoDB 中的一個新文檔。

主要流程：
1. 事件觸發：當有事件來自 Event Grid 時，EventGridTrigger 函數會被觸發。事件數據將通過 azeventgrid 參數接收到。
2. 事件數據解析：函數將解析事件的 JSON 數據並記錄到日誌中。
3. 文檔存儲：將解析後的事件數據（包括事件 ID、類型、主題、數據和事件時間）儲存為 MongoDB 中的一個新文檔。


----------------------------------------------------------------------------------------------------------------------

host.json 配置
host.json 是 Azure Functions 的全局配置文件。以下是本專案的 host.json 文件及其詳細說明：


設置說明：
version: 表示 Function 的版本。此處設置為 2.0，表示該應用使用 Azure Functions 2.x 版本。

logging:

applicationInsights: 配置應用內的日誌跟蹤。這裡啟用了 SamplingSettings，它會限制傳送到 Application Insights 的數據量，以減少數據存儲的開銷。
isEnabled: 設置為 true 表示啟用日誌采樣。
extensionBundle:

id: 這指定了要使用的擴展包。Microsoft.Azure.Functions.ExtensionBundle 提供了內建的 Azure Function 擴展，例如 Event Grid 和 Blob Storage 等。
version: 設置了擴展包的版本範圍。[2.*, 3.0.0) 表示使用 2.x 版本，但不包括 3.0.0 版本及以上。

