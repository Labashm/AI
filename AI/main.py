from gtts import gTTS

voz1 = gTTS("Digite o seu nome no terminal",lang="pt")
voz1.save("Cache/Vozes/voz1.mp3")
import subprocess as s
s.call(['mplayer','Cache/Vozes/voz1.mp3'])


nome = input("Seu nome: ")

voz = gTTS("Olá,"+ nome ,lang="pt")
voz.save("Cache/Vozes/voz.mp3")
import subprocess as s
s.call(['mplayer','Cache/Vozes/voz.mp3'])

voz2 = gTTS("em que posso ajudar?",lang="pt")
voz2.save("Cache/Vozes/voz2.mp3")
import subprocess as s
s.call(['mplayer','Cache/Vozes/voz2.mp3'])

def open_google():
    s.Popen('google-chrome')

def open_firefox():
    s.Popen('firefox')

def open_discord():
    s.Popen('discord')


def menu():
    print('''

[1] - Abrir o Google
[2] - Abrir o Firefox
[3] - Abrir o Discord    

    ''')

menu()      
escolha = input('\n: ')
if escolha == '1':
    open_google()
    voz3 = gTTS("O Google foi aberto",lang="pt")
    voz3.save("Cache/Vozes/voz3.mp3")
    import subprocess as s
    s.call(['mplayer','Cache/Vozes/voz3.mp3'])
elif escolha == '2':
    open_firefox()
    voz4 = gTTS("O Firefox foi aberto",lang="pt")
    voz4.save("Cache/Vozes/voz4.mp3")
    import subprocess as s
    s.call(['mplayer','Cache/Vozes/voz4.mp3'])
elif escolha == '3':
    open_discord()
    voz5 = gTTS("O Discord foi aberto",lang="pt")
    voz5.save("Cache/Vozes/voz5.mp3")
    import subprocess as s
    s.call(['mplayer','Cache/Vozes/voz5.mp3'])
else:
    
    voz6 = gTTS("Essa escolha ainda não foi incluida no meu sistema",lang="pt")
    voz6.save("Cache/Vozes/voz6.mp3")
    import subprocess as s
    s.call(['mplayer','Cache/Vozes/voz6.mp3'])
    menu()
    escolha = input('\n: ')