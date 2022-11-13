def hi():
    #ask Name
    name=input("Enter  Your name")
    print(f"Hi {name} , Let's start the game")
    print("\n\n\n\t\t ***Word Guessing Game*** ")
    print("\n You have 10 attempts to guess the word correctly .")

#hi()
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
    with open('words.txt','r') as f:
        re=f.readlines()
        n=0
        for i in re:
            n+=1
            print(n,'|',i ,end='')
          
            
#read()
def game():
    import random
    gms=open('words.txt','r')
    h=gms.readlines()
    rand=random.choice(h)
    return rand
wod=game()

