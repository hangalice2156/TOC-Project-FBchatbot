# TOC-Project-FBchatbot
NCKU TOC class project to write a FBchat bot applying state machine with python 

## 環境
開發環境：kubuntu 18.04 LTS
語言：Python 3.6.5
相依套件：pygraphviz (graphviz is also required)

## 建置
bottle.py 與 ngrok 已經附在專案之中，如果有需要可以使用以下指令
`sudo apt-get install python-pip3` (if pip3 is not installed)
`pip3 install -r requirements.txt`

## 執行
執行`ngrok http <port>`，同時執行`python3 app.py` 就可以開始透過ngrok 運行bot，app.py 的port 要和ngrok 開的一樣。
要注意存取權杖與驗證權杖需要和自己管理的FB相符。

## 描述
嘗試用FBchatbot 做了一個簡單的小遊戲。

執行伺服器(ngrok 與app.py)
到粉絲專頁上面(可能要用訪客模式檢視)，對粉絲專頁傳送訊息
首先會在'user' 的state上，只要輸入隨意訊息都會到'manual'
接著就只要按照每個state 傳送給你的訊息，照著指示回覆訊息就可以完成小遊戲。

Features and bonus: 可以傳送圖片、原創的短篇故事劇情。

possible accepted input table (Note: all in lowercase)

- manual: `help`, `about`, `credits`, `show fsm`, `play`
- in almost all states: `back` (will return to manual)
- in game: `a`, `b`, `ab`, `ba...` (something like this, just string of combinations of a, b, c......)
