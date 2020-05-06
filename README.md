# youtube_chat_crawler(KR)

유튜브 스트리밍에서의 liveChat 데이터를 크롤링하는 Python 3 script입니다.

원본 코드는 雑記帳(@watagasi)님의 코드를 참조했습니다. (http://watagassy.hatenablog.com/entry/2018/10/08/132939)

원본 코드에서는 liveChat 내용에서 '=' 가 포함되어있으면 작동이 제대로 되지 않습니다.

Python 3.x를 요구하며, bs4 / requests / ast 모듈의 설치를 요구합니다.

사용법 : python YoutubeChatReplayCrawler.py {유튜브 스트리밍 링크}

(예 : python YoutubeChatReplayCrawler.py https://www.youtube.com/watch?v=WuMzBTDz9DI)

이러면 해당 방송의 제목을 이름으로 가지는 json 파일이 생성됩니다.

python chatReplayConverter.py 명령을 통해 해당 json 파일을 알아보기 쉬운 text file 형태로 변환할 수 있습니다. chatReplayConverter.py는 해당 스크립트가 포함된 폴더 내의 모든 json 파일을 text 형식으로 변환합니다.

# youtube_chat_crawler(EN)
youtube_chat_crawler crawls liveChat messages from finished live stream.

I've forked the original source code from 雑記帳(@watagasi). ( http://watagassy.hatenablog.com/entry/2018/10/08/132939 )

Added minor fixes (like parsing problems)

Python 3.x, bs4 / request / ast module is required.

Usage : python YoutubeChatReplayCrawler.py {YOUR_TARGET_STREAM_LINK

(example : python YoutubeChatReplayCrawler.py https://www.youtube.com/watch?v=WuMzBTDz9DI)

You can get a json file, which contains the live stream chat data.

chatReplayConverter.py converts all the json file in the same directory to easy-to-read text file form.
