from tkinter import *
import funcoes as fc




# Função para baixar o vídeo (exemplo)
def baixar():
    url = entrada.get()  # Obtém o conteúdo do campo de entrada
    fc.baixar_video(url)  # Chama a função de download passando a URL

# Cria a janela principal
janela = Tk()
janela.geometry("500x400")
janela.title("ViniDownloads")

# Texto de orientação
texto_orientacao = Label(janela, text="Download de Vídeos e músicas")
texto_orientacao.grid(column=0, row=0, pady=10)

# Campo de entrada para a URL
entrada = Entry(janela, width=40)
entrada.grid(column=0, row=1, pady=10)

# Opções de Downloads
opcoes = ["Escolha uma opção" , "Baixar Vídeo (Unico)", "Baixar Áudio" , "Baixar Playlist"]
opcoes_valores = [None, fc.baixar_video, fc.baixar_audio, fc.baixar_playlist]

var_opcao=IntVar()

# Botão de download
botao = Button(janela, text="Download", command=baixar)
botao.grid(column=0, row=2, pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
