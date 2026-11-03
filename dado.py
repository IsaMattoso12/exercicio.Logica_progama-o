import random
import tkinter

janela = tk.Tk()
janela.title("dado da sorte")

class tk:
    ...

resultado = tk.label(janela, text="?", font=("Arial", 60))
resultado.pack(padx=60, pady=10)


def jogar():
    numero = random.randint(1,6)
    resultado.config(text=numero)

botao = tk.button(janela, text="Jogar o dado", comand=jogar)
botao.pack(pady=10)

janela.mainloop()