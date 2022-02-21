
chat = []
with open('Chi_Ting.txt', 'r', encoding='utf-8-sig') as f:
    for talk in f:
        chat.append(talk.strip())

for list in chat:
    s = list.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(time)
    print(name)
    #print(s)




