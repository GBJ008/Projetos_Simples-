#importar as bibliotecas
import pyautogui  
from time import sleep
import customtkinter as tk
from tkinter import messagebox

tk.set_appearance_mode("dark")


def executar_comando():
    executa = campo_Digite.get().strip().lower()

    if executa == "s":
        messagebox.showinfo('Executando', 'o Programa vai começar em alguns Segundo...')
        sleep(4)

        try:
            # script para clicar e colocar o usuário
            pyautogui.click(976,541,duration=3)
            pyautogui.write('jhonatan')
            pyautogui.click(964,574,)
            pyautogui.write('123456')
            pyautogui.click(851,611,duration=2)
            #abrir e ler o arquivo
            with open('produtos.txt','r') as arquivo:
                for linha in arquivo:
                    Produtos = linha.strip().split(',')
                    if len(Produtos) >= 3:
            #a cada virgula ele vai andar um pouco para frente 
                        produto=linha.split(',')[0]
                        quantidade=linha.split(',')[1]
                        preco=linha.split(',')[2]
            #parte 2 digitar os produtos
                        pyautogui.click(601,524,duration=2)
                        pyautogui.write(produto)

                        pyautogui.click(597,558,duration=2)
                        pyautogui.write(quantidade)
                                
                        pyautogui.click(638,593,duration=2)
                        pyautogui.write(preco)
                                
                        pyautogui.click(504,789,duration=1)
                        sleep(1)
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'produtos.txt' não encontrado.")
        else:
            messagebox.showinfo("Encerrando","Programa Encerrado")
    elif executa == "n":
        messagebox.showinfo("Encerrando", "Programa encerrado pelo usuário.")
        app.destroy()
    else:
        messagebox.showwarning("Aviso", "Resposta inválida! Digite 's' para sim ou 'n' para não.")
       


app=tk.CTk()
app.title("Automatizador de Estoque")
app.geometry('350x350')

campo_pergunta=tk.CTkLabel(app,text='Você quer executar o Programa\n Sim ou Não')
campo_pergunta.pack(pady=40)

campo_Digite=tk.CTkEntry(app,placeholder_text='Digite sua resposta')
campo_Digite.pack(pady=42)

campo_botao=tk.CTkButton(app,text="enviar",command=executar_comando)
campo_botao.pack(pady=43)
app.mainloop()