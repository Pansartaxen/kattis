inpt = int(input())
letters = ''
caps = False
for _ in range(inpt):
    sound = input()
    
    if sound == 'clank':
        sound = 'a'
    elif sound =='bong':
        sound = 'b'
    elif sound =='click':
        sound = 'c'
    elif sound =='tap':
        sound = 'd'
    elif sound =='poing':
        sound = 'e'
    elif sound =='clonk':
        sound = 'f'
    elif sound =='clack':
        sound = 'g'
    elif sound =='ping':
        sound = 'h'
    elif sound =='tip':
        sound = 'i'
    elif sound =='cloing':
        sound = 'j'
    elif sound =='tic':
        sound = 'k'
    elif sound =='cling':
        sound = 'l'
    elif sound =='bing':
        sound = 'm'
    elif sound =='pong':
        sound = 'n'
    elif sound =='clang':
        sound = 'o'
    elif sound =='pang':
        sound = 'p'
    elif sound =='clong':
        sound = 'q'
    elif sound =='tac':
        sound = 'r'
    elif sound =='boing':
        sound = 's'
    elif sound =='boink':
        sound = 't'
    elif sound =='cloink':
        sound = 'u'
    elif sound =='rattle':
        sound = 'v'
    elif sound =='clock':
        sound = 'w'
    elif sound =='toc':
        sound = 'x'
    elif sound =='clink':
        sound = 'y'
    elif sound =='tuc':
        sound = 'z'
    elif sound =='whack':
        sound = ''
        letters = letters + ' '
    elif sound =='bump':
        sound = ''
        if caps == True:
            caps = False
        elif caps == False:
            caps = True
    elif sound =='pop':
        sound = ''
        letters = letters[:-1]
    elif sound == 'dink':
        sound = ''
        caps = True
    elif sound == 'thumb':
        sound = ''
        caps = False
    if caps == True:
        sound = sound.upper()
    if sound != '':
        letters = letters + sound
print(letters)