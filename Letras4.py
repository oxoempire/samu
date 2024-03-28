import tkinter as tk
import pygame

# Lista con las letras del abecedario
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Inicializar pygame
pygame.init()

# Configuración de la ventana
root = tk.Tk()
root.title("Adivina la letra")
root.geometry("1100x550")  # Doble ancho para dos frames

# Frame izquierdo para la imagen principal
frame_izquierdo = tk.Frame(root, width=550, height=550)
frame_izquierdo.pack(side=tk.LEFT)

# Frame derecho para la segunda imagen
frame_derecho = tk.Frame(root, width=550, height=550)
frame_derecho.pack(side=tk.RIGHT)

letra_actual = 0
ventana_opciones = None  # Variable global para la ventana emergente

# Función para verificar la letra ingresada por el usuario
def verificar_letra(event):
    global letra_actual
    letra_ingresada = entrada.get()
    if len(letra_ingresada) == 1 and letra_ingresada.isalpha():
        letra_ingresada = letra_ingresada.upper()
        if letra_ingresada == letras[letra_actual]:
            if letra_ingresada == 'Z':
                reproducir_audio('ABC.mp3')
            elif letra_ingresada == 'A':
                reproducir_audio(letras[letra_actual] + '.mp3')
            else:
                reproducir_audio('done.mp3')
            siguiente_letra()
        else:
            reproducir_audio('error.mp3')
        entrada.delete(0, tk.END)  # Limpiar la entrada de texto después de verificar la letra
    else:
        entrada.delete(0, tk.END)  # Limpiar la entrada de texto si se ingresa un carácter inválido

# Función para pasar a la siguiente letra
def siguiente_letra():
    global letra_actual
    if letra_actual < len(letras) - 1:
        letra_actual += 1
        imagen_letra.config(file=letras[letra_actual] + '.png')
        imagen_letra2.config(file=letras[letra_actual] + '_.png')  # Cambiar imagen en el frame derecho
        audio_letra = letras[letra_actual] + '.mp3'
        reproducir_audio(audio_letra)
    else:
        mostrar_opciones()

# Función para reproducir el audio
def reproducir_audio(nombre_archivo):
    pygame.mixer.music.load(nombre_archivo)
    pygame.mixer.music.play()

# Función para mostrar la ventana emergente con las opciones
def mostrar_opciones():
    global ventana_opciones
    ventana_opciones = tk.Toplevel(root)
    ventana_opciones.title("Opciones")
    ventana_opciones.geometry("300x100")
    
    boton_reiniciar = tk.Button(ventana_opciones, text="Empezar de nuevo", command=reiniciar_juego)
    boton_reiniciar.pack(side=tk.LEFT)
    
    boton_salir_opciones = tk.Button(ventana_opciones, text="Salir", command=root.quit)
    boton_salir_opciones.pack(side=tk.RIGHT)

# Función para reiniciar el juego desde la letra "A"
def reiniciar_juego():
    global letra_actual
    letra_actual = 0
    imagen_letra.config(file=letras[letra_actual] + '.png')
    imagen_letra2.config(file=letras[letra_actual] + '_.png')
    audio_letra = letras[letra_actual] + '.mp3'
    reproducir_audio(audio_letra)
    ventana_opciones.destroy()  # Cerrar la ventana emergente

# Mostrar la primera imagen y reproducir el primer audio
imagen_letra = tk.PhotoImage(file=letras[letra_actual] + '.png')
imagen_label = tk.Label(frame_izquierdo, image=imagen_letra)
imagen_label.pack(side=tk.LEFT)

imagen_letra2 = tk.PhotoImage(file=letras[letra_actual] + '_.png')
imagen_label2 = tk.Label(frame_derecho, image=imagen_letra2)
imagen_label2.pack(side=tk.RIGHT)

audio_letra = letras[letra_actual] + '.mp3'
reproducir_audio(audio_letra)

# Entrada de texto para ingresar la letra
entrada = tk.Entry(root, font=('Arial', 24))
entrada.pack()
entrada.focus_set()  # Colocar el cursor en el cuadro de texto al inicio

# Vincular la verificación de letra a la pulsación de tecla en la entrada de texto
entrada.bind("<KeyRelease>", verificar_letra)

root.mainloop()
