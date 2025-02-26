from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import funcoes as fc
import os
import sys
import ctypes

# Definir o ícone da barra de tarefas no Windows
def set_taskbar_icon(icon_path):
    if sys.platform == "win32":
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(icon_path)

# Diretório padrão: pasta "Downloads" do usuário
diretorio = os.path.join(os.path.expanduser('~'), "Downloads")

# Função para escolher o diretório de download
def escolher_diretorio():
    global diretorio
    novo_diretorio = filedialog.askdirectory()  # Pergunta qual vai ser o diretório da pasta
    if novo_diretorio:
        diretorio = novo_diretorio
        label_diretorio.config(text=f"Diretório: {diretorio}")

# Função para atualizar a barra de progresso
def atualizar_progresso(progresso_total):
    barra_progresso['value'] = progresso_total
    janela.update_idletasks()  # Atualiza a interface

    # Fecha a aba de progresso quando o download é concluído
    if progresso_total >= 100:
        messagebox.showinfo("Concluído", "Download da playlist concluído com sucesso!")
        notebook.hide(aba_progresso)  # Oculta a aba de progresso

# Função para baixar o vídeo/áudio/playlist
def baixar():
    url = entrada.get()
    if url:
        # Obtém o valor da seleção
        opcao_selecionado = var_opcao.get()
        if opcao_selecionado == "Escolha uma opção":
            messagebox.showwarning("Aviso", "Por favor, selecione uma opção válida.")
        else:
            # Reinicia a barra de progresso
            barra_progresso['value'] = 0
            notebook.add(aba_progresso, text="Progresso")  # Mostra a aba de progresso
            notebook.select(aba_progresso)  # Seleciona a aba de progresso

            # Executa a função de download com o diretório e callback de progresso
            funcao_selecionada = opcoes_funcoes[opcao_selecionado]
            funcao_selecionada(url, diretorio, atualizar_progresso)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL.")

# Cria a janela principal
janela = Tk()
janela.title("YogoTube")

# Definir o ícone da janela e da barra de tarefas
icone_path = "icone.ico"  # Substitua pelo caminho correto do seu ícone
janela.iconbitmap(icone_path)
set_taskbar_icon(icone_path)  # Define o ícone da barra de tarefas

janela.configure(bg="#f5f5f5")  # Cor de fundo suave

# Centralizar a janela no monitor
janela.update_idletasks()
largura_janela = janela.winfo_width()
altura_janela = janela.winfo_height()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura_janela // 2)
y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f'+{x}+{y}')

# Estilo personalizado para os widgets
style = ttk.Style()
style.theme_use("clam")  # Tema "clam" para um visual moderno

# Configurações de estilo
style.configure("TFrame", background="#ffffff", relief="solid", borderwidth=1)  # Fundo branco com borda
style.configure("TLabel", background="#ffffff", font=("Helvetica", 12), foreground="#333333")  # Texto escuro
style.configure("TButton", font=("Helvetica", 12), padding=5, background="#4caf50", foreground="#ffffff")  # Botão verde
style.configure("TEntry", font=("Helvetica", 12), padding=5, relief="flat", borderwidth=1)  # Campo de entrada simples
style.configure("TProgressbar", thickness=20, background="#4caf50")  # Barra de progresso verde

# Notebook (para abas)
notebook = ttk.Notebook(janela)
notebook.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

# Aba principal (formulário de download)
aba_principal = ttk.Frame(notebook)
notebook.add(aba_principal, text="Download")

# Centralizar os widgets na aba principal
aba_principal.grid_columnconfigure(0, weight=1)
aba_principal.grid_rowconfigure(0, weight=1)

# Texto de orientação
texto_orientacao = ttk.Label(aba_principal, text="Download de Vídeos e Músicas", style="TLabel")
texto_orientacao.grid(column=0, row=0, pady=5, columnspan=2)

# Campo de entrada para a URL
label_url = ttk.Label(aba_principal, text="URL do vídeo/playlist:", style="TLabel")
label_url.grid(column=0, row=1, pady=2, sticky="ew")
entrada = ttk.Entry(aba_principal, width=40, style="TEntry")
entrada.grid(column=0, row=2, pady=2, columnspan=2, sticky="ew")

# Opções de Downloads
opcoes = ["Escolha uma opção", "Baixar Vídeo (Unico)", "Baixar Áudio", "Baixar Playlist"]
opcoes_funcoes = {
    "Baixar Vídeo (Unico)": fc.baixar_video,
    "Baixar Áudio": fc.baixar_audio,
    "Baixar Playlist": fc.baixar_playlist
}

# Define qual vai ser a mensagem inicial das opções
var_opcao = StringVar()
var_opcao.set("Escolha uma opção")

# Define o menu de opções
menu_opcoes = ttk.OptionMenu(aba_principal, var_opcao, *opcoes)
menu_opcoes.grid(column=0, row=3, pady=5, columnspan=2, sticky="ew")

# Rótulo para exibir o diretório de download atual
label_diretorio = ttk.Label(aba_principal, text=f"Diretório: {diretorio}", style="TLabel")
label_diretorio.grid(column=0, row=4, pady=2, columnspan=2, sticky="ew")

# Botão para escolher o diretório de download
botao_escolher_diretorio = ttk.Button(aba_principal, text="Escolher Diretório", command=escolher_diretorio, style="TButton")
botao_escolher_diretorio.grid(column=0, row=5, pady=5, columnspan=2, sticky="ew")

# Botão de download
botao_download = ttk.Button(aba_principal, text="Download", command=baixar, style="TButton")
botao_download.grid(column=0, row=6, pady=5, columnspan=2, sticky="ew")

# Aba de progresso
aba_progresso = ttk.Frame(notebook)
notebook.add(aba_progresso, text="Progresso")
notebook.hide(aba_progresso)  # Oculta a aba de progresso inicialmente

# Barra de progresso
barra_progresso = ttk.Progressbar(aba_progresso, orient=HORIZONTAL, length=400, mode='determinate', style="TProgressbar")
barra_progresso.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()