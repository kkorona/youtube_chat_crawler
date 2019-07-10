import glob
import ast
for filename in glob.glob('*.json'):
    print(filename)
    target_id = filename.split('.')[0]
    if glob.glob(target_id+".txt"):
        print("Exists")
        continue
    count = 1
    result = ""
    with open(filename,'r',encoding='utf8') as f:
        print("open")
        lines = f.readlines()
        for line in lines:
            print(count)
            if not 'liveChatTextMessageRenderer' in line:
                print("not chat")
                continue
            ql = line
            frac = ("#Chat No.%05d " % count)
            info = ast.literal_eval(ql)
            info = info['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatTextMessageRenderer']
            content = ""
            if 'simpleText' in info['message']:
                content = info['message']['simpleText']
            elif 'runs' in info['message']:
                for fragment in info['message']['runs']:
                    if 'text' in fragment:
                        content += fragment['text']
            else:
                print("no text")
                continue
            authorName = info['authorName']['simpleText']
            time = info['timestampText']['simpleText']
            frac += "user: \"" + authorName + "\" time: " + time + "\n- " + content + "\n" 
            result += frac
            count += 1
            

    target_id = filename.split('.')[0]
    with open(target_id+".txt",'w',encoding='utf8') as f:
        f.write(result)