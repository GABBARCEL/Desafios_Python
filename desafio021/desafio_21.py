# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('/media/gabriel/1E36BD3F36BD192B/Users/GABRIEL/.vscode/Principais/aprender_python/Desafios_Python/desafio021/musica.mp3')
mixer.music.play()
sleep(120)
