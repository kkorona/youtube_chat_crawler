import glob
import ast
import sys
for filename in glob.glob('*.json'):
    print(filename)
    target_id = filename.split('.')[0]
    if glob.glob(target_id+".txt"):
        print("Exists")
        continue
    count = 1
    result = ""
    with open(filename,'r',encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            sys.stdout.write('\rProcessing line %d' % (count))
            if 'liveChatTickerPaidMessageItemRenderer' in line:
                continue
            if not 'liveChatTextMessageRenderer' in line and not 'liveChatPaidMessageRenderer' in line:
                continue
            ql = line
            frac = ("#Chat No.%05d " % count)
            info = ast.literal_eval(ql)
            
            #Case Normal Chat
            if 'liveChatTextMessageRenderer' in line:
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
                frac += "type: NORMALCHAT user: \"" + authorName + "\" time: " + time + "\n- " + content + "\n" 

            
            #Case Super Chat
            if 'liveChatPaidMessageRenderer' in line:
                info = info['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatPaidMessageRenderer']
                content = ""
                if 'message' in info:
                    if 'simpleText' in info['message']:
                        content = info['message']['simpleText']
                    elif 'runs' in info['message']:
                        for fragment in info['message']['runs']:
                            if 'text' in fragment:
                                content += fragment['text']
                    else:
                        print("no text")
                        continue
                 
                if 'authorName' in info:
                    authorName = info['authorName']['simpleText']
                else:
                    authorName = "%anonymous%"
                time = info['timestampText']['simpleText']
                purchaseAmout = info['purchaseAmountText']['simpleText']
                frac += "type: SUPERCHAT user: \"" + authorName + "\" time: " + time + " amount: " + purchaseAmout + "\n- " + content + "\n" 
            result += frac
            count += 1
            

    target_id = filename.split('.')[0]
    sys.stdout.write('\nDone!')
    with open(target_id+".txt",'w',encoding='utf8') as f:
        f.write(result)