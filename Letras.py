import tkinter as tk
import pygame

# Lista con las letras del abecedario
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Inicializar pygame
pygame.init()

# Configuración de la ventana
root = tk.Tk()
root.title("Adivina la letra")
root.geometry("550x550")

letra_actual = 0

# Función para verificar la letra ingresada por el usuario
def verificar_letra(event):
    letra_ingresada = entrada.get().upper()
    if len(letra_ingresada) > 0:
        if letra_ingresada == letras[letra_actual]:
            if letra_ingresada == 'Z':
                reproducir_audio('ABC.mp3')
            else:
                reproducir_audio('done.mp3')
        else:
            reproducir_audio('error.mp3')
        entrada.delete(0, tk.END)  # Limpiar la entrada de texto después de verificar la letra

# Función para pasar a la siguiente letra
def siguiente_letra():
    global letra_actual
    if letra_actual < len(letras) - 1:
        letra_actual += 1
        imagen_letra.config(file=letras[letra_actual] + '.png')
        audio_letra = letras[letra_actual] + '.mp3'
        reproducir_audio(audio_letra)
    else:
        reproducir_audio('ABC.mp3')
    entrada.delete(0, tk.END)  # Limpiar la entrada de texto después de avanzar a la siguiente letra

# Función para reproducir el audio
def reproducir_audio(nombre_archivo):
    pygame.mixer.music.load(nombre_archivo)
    pygame.mixer.music.play()

# Mostrar la primera imagen y reproducir el primer audio
imagen_letra = tk.PhotoImage(file=letras[letra_actual] + '.png')
imagen_label = tk.Label(root, image=imagen_letra)
imagen_label.pack()

audio_letra = letras[letra_actual] + '.mp3'
reproducir_audio(audio_letra)

# Entrada de texto para ingresar la letra
def validar_letra(event):
    letra_ingresada = event.char.upper()
    if letra_ingresada.isalpha() and len(letra_ingresada) > 0:
        entrada.delete(0, tk.END)  # Limpiar la entrada de texto en cada ingreso de letra
        if letra_ingresada == letras[letra_actual]:
            siguiente_letra()
        else:
            reproducir_audio('error.mp3')

entrada = tk.Entry(root, font=('Arial', 24))
entrada.pack()
entrada.focus_set()  # Colocar el cursor en el cuadro de texto al inicio

# Vincular la verificación de letra a la pulsación de tecla en la entrada de texto
entrada.bind("<Key>", validar_letra)

root.mainloop()
