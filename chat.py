
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8') as f:
        for list in f:
            chat.append(list.strip())
    return chat

def convert(chat):
    new = []
    person = None
    for list in chat:
        if list == 'Allen':
            person = 'Allen'
            continue
        elif list == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + list)
    return new

def write_file(filename, chat):
    with open(filename, 'w') as f:
        for list in chat:
            f.write(list + '\n')
def main():
    chat = read_file('input.txt') 
    chat = convert(chat)
    write_file('output.txt', chat)

main() # 程式進入點



#filename = 'input.txt'
#chat=[]
#with open(filename, 'r', encoding='utf-8') as f: # 打開檔案
#    for list in f:
#        print(list.strip())
