
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8') as f:
        for list in f:
            chat.append(list.strip())
    return chat

def convert(chat):
    new = []
    person = None
    kiwe_word_count = 0
    Chi_Ting_word_count = 0
    kiwe_sticker_count = 0
    Chi_Ting_sticker_count = 0
    kiwe_image_count = 0
    Chi_Ting_image_count = 0
    for list in chat:
        s = list.split(' ')
        time = s[0]
        name = s[1]        
        if name == 'kiwe':
            if s[2] == '貼圖':
                kiwe_sticker_count += 1
            elif s[2] == '圖片':
                kiwe_image_count += 1
            else:
                for m in s[2:]:
                    kiwe_word_count += len(m)
        elif name == 'Chi_Ting':
            if s[2] == '貼圖':
                Chi_Ting_sticker_count += 1
            elif s[2] == '圖片':
                Chi_Ting_image_count += 1
            else:
                for m in s[2:]:
                    Chi_Ting_word_count += len(m)                              
                
    print('kiwe say', kiwe_word_count, 'words')
    print('kiwe send', kiwe_sticker_count, 'picturts')
    print('kiwe send', kiwe_image_count, 'images')

    print('Chi_Ting say', Chi_Ting_word_count, 'words')
    print('Chi_Ting send', Chi_Ting_sticker_count, 'picturts')
    print('Chi_Ting send', Chi_Ting_image_count, 'images')



        #print(s)

    return new

def write_file(filename, chat):
    with open(filename, 'w') as f:
        for list in chat:
            f.write(list + '\n')
def main():
    chat = read_file('[LINE]Chi_Ting.txt') 
    chat = convert(chat)
    #write_file('output.txt', chat)

main() # 程式進入點

''''''

def open_file(filename):
    chat=[]
    with open(filename, 'r', encoding='utf-8') as f: # 打開檔案
        for list in f:
            chat.append(list.strip())
    return chat
    print(chat)
         
       

def main():
    chat = open_file('input.txt')

main()


''''''