from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os

pasta_base_musica = 'Musicas'
pasta_base_video = 'Videos'
    
    

            


def baixar_video(url):
    
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download()

    print("Download concluí do!")



def baixar_audio(url):
    try:    
        yt = YouTube(url,on_progress_callback=on_progress)
        
        if not os.path.exists(pasta_base_musica):
            os.mkdir(pasta_base_musica)
            print(f'Pasta {pasta_base_musica} Criada com sucesso')
        else:
            print(f'Pasta {pasta_base_musica} Já existe')
        
        ys = yt.streams.get_audio_only()
        ys.download(output_path=pasta_base_video)

        print("Download concluí do!")
    except Exception as e:
        print("Deu erro")



                  

def sanitizar_nome_pasta(nome):
    caracteres_invalidos = r'<>:"/\|?*[]'
    for char in caracteres_invalidos:
        nome = nome.replace(char, '_')
    return nome

def baixar_playlist(url):
    try:
        # Carrega a playlist
        pl = Playlist(url)
        print(f"Playlist carregada: {pl.title}")

        # Sanitiza o nome da playlist para garantir que seja válido como nome de pasta
        nome_playlist_sanitizado = sanitizar_nome_pasta(pl.title)
        print(f"Nome da playlist sanitizado: {nome_playlist_sanitizado}")

        # Define a pasta base onde as playlists serão salvas
        pasta_base_musica = "Musicas"
        
        # Cria a pasta base se ela não existir
        if not os.path.exists(pasta_base_musica):
            os.mkdir(pasta_base_musica)
            print(f'Pasta base "{pasta_base_musica}" criada com sucesso.')
        else:
            print(f'Pasta base "{pasta_base_musica}" já existe.')

        # Cria o caminho completo para a pasta da playlist
        pasta_playlist = os.path.join(pasta_base_musica, nome_playlist_sanitizado)
        
        # Cria a pasta da playlist se ela não existir
        if not os.path.exists(pasta_playlist):
            os.mkdir(pasta_playlist)
            print(f'Pasta da playlist "{pasta_playlist}" criada com sucesso.')
        else:
            print(f'Pasta da playlist "{pasta_playlist}" já existe.')

        # Baixa cada vídeo da playlist como áudio
        for video in pl.videos:
            try:
                print(f"Baixando: {video.title}")
                ys = video.streams.get_audio_only()
                ys.download(output_path=pasta_playlist)
                print(f"Concluído: {video.title}")
            except Exception as e:
                print(f"Erro ao baixar o vídeo {video.title}: {e}")

    except Exception as e:
        print(f"Erro ao processar a playlist: {e}")
        
        
        
        

#teste("https://www.youtube.com/watch?v=nRe3xFeyhVY&list=PLdSUTU0oamrwC0PY7uUc0EJMKlWCiku43")
