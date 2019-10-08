from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

target_url = "https://www.youtube.com/watch?v=FxRWHzcO-8o"
options = Options ()
options.add_argument ( '--headless' )
options.add_argument ( '--disable-gpu' )
options.add_argument ( '--disable-desktop-notifications' )
options.add_argument ( "--disable-extensions" )
options.add_argument ( '--blink-settings = imagesEnabled = false' )
dict_str = "" 
next_url = ""
comment_data = []

# 우선 동영상 페이지에 requests를 실행 html 소스를 손에 넣어 live_chat_replay의 선두 url을 입수
html = requests.get (target_url)
soup = BeautifulSoup (html.text, "html.parser" )

for iframe in soup.find_all ( "iframe" ) :
     if ( "live_chat_replay"  in iframe [ "src" ] ) :
        next_url = iframe [ "src" ]


while ( 1 ) :

    try :
         # chromedriver를 엽니 next_url 소스를 입수 
        driver = webdriver.Chrome (chrome_options = options, executable_path = r"C:\\chromedriver_win32\\chromedriver.exe" )
        driver.get (next_url)
        soup = BeautifulSoup (driver.page_source, "lxml" )
         # 반드시 quit한다. 잊어 버리면 google chrome가 열린 마구 큰일된다
        driver.quit ()

        # 다음 날 url의 데이터가있는 부분을 find_all에서 찾고 split로 성형 
        for scrp in soup.find_all ( "script" ) :
             if  "window [ \" ytInitialData \" ]"  in scrp.text :
                dict_str = scrp.text.split ( "=" ) [ 1 ]

        # javascript 표기이므로 더 성형. false와 true의 표기를 치유 
        dict_str = dict_str.replace ( "false" , "False" )
        dict_str = dict_str.replace ( "true" , "True" )

        # 사전 형식으로 인식하면 쉽게 데이터를 얻을 수 있지만, 끝에 방해 것이 있기 때문에 지운다 ( "공백 2 개 + \ n +;"을 끄는) 
        dict_str = dict_str.rstrip ( "   \ n ;" )
         # 사전 형식으로 변환 
        dics = eval (dict_str)

        # "https://www.youtube.com/live_chat_replay?continuation="+ continue_url가 다음 live_chat_replay의 url 
        continue_url = dics [ "continuationContents" ] [ "liveChatContinuation" ] [ "continuations" ] [ 0 ] [ "liveChatReplayContinuationData" ] [ "continuation" ]
        next_url = "https://www.youtube.com/live_chat_replay?continuation=" + continue_url
         # dics [ "continuationContents"] [ "liveChatContinuation"] [ "actions"] 코멘트 데이터의 목록입니다. 선두는 노이즈 데이터이므로 [1 :]에서 저장 
        for samp in dics [ "continuationContents" ] [ "liveChatContinuation" ] [ "actions" ] [ 1 :] :
            comment_data.append ( str (samp) + " \ n " )

    # next_url를 사용할 수 없게되면 마지막 
    except :
         break

# comment_data.txt 코멘트 데이터를 기록 
with  open ( "comment_data.txt" , mode = 'w' , encoding = "utf-8" ) as f :
    f.writelines (comment_data)