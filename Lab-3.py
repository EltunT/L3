import tkinter as tk
import random
import pygame

pygame.init()
pygame.mixer.music.load("Чинчан.mp3")

def play_music():
    pygame.mixer.music.play()

def generate_word():
    letter_list = list("abcdefghijklmnopqrstuvwxyz")
    number_list = list("0123456789")
    word =''
    word_list = list(random.sample(letter_list, 3) + random.sample(number_list, 2))
    random.shuffle(word_list)
    for i in word_list:
        word+=i
    return word

def generate_key():
    key = f"{generate_word()}-{generate_word()}-{generate_word()}"
    key_label.config(text=key)

window = tk.Tk()
window.title("Мудрость китайских генераторов")

play_music()

bg_image = tk.PhotoImage(file='Drakon.png')
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

window.geometry(f"{bg_image.width()}x{bg_image.height()}")


word_label = tk.Label(window, text="Попроси мудрости у великого дракона", font=("Times New Roman", 30))
word_label.pack()

generate_button = tk.Button(window, text="Воззвать дракона", command=generate_key, font=("Times New Roman", 15))
generate_button.pack()

key_label = tk.Label(window, text="", font=("Times New Roman", 25))
key_label.pack()

window.mainloop()
