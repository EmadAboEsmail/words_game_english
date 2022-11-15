def write_file():
        '''
        برنامج يقوم بتخزين الكلمات المدخله
        اذا كانت الكلمة موجود في الملف
        لايتم تخزينها
        '''
        while True:
            file=open('words.txt','r')
            r=file.readlines()
            e=input('enter words ')
            if e+'\n' in r:
                print('the word is in the file')
                continue
            elif e=='':
                break
            elif e!='':
                f=open('words.txt','a')
                f.write(e+'\n')
                f.close()
            file.close()
#write_file()

def read():
        #read a file
        f=open('words.txt','r')
        re=f.readlines()
        n=0
        for i in re:
            n+=1
            print(n,'|',i ,end='')


def wel():
    import history
    #welcome massage
    name=input('Enter the name : ')

    print(f'\n\t\t Hi ««({name})»» \n\nlast login : ',history.read_history())
    history.write_history()
wel()

