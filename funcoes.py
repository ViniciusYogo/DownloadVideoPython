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
    yt = YouTube(url,on_progress_callback=on_progress)
    
    if not os.path.exists(pasta_base_musica):
        os.mkdir(pasta_base_musica)
        print(f'Pasta {pasta_base_musica} Criada com sucesso')
    else:
        print(f'Pasta {pasta_base_musica} Já existe')
    
    ys = yt.streams.get_audio_only()
    ys.download(output_path=pasta_base_video)

    print("Download concluí do!")


def baixar_playlist(url):

    pl = Playlist(url)

    pasta_playlist =  pl.title

    if not os.path.exists(pasta_base_musica):
        os.mkdir(pasta_base_musica)
        print(f'Pasta {pasta_base_musica} Criada com sucesso')
    else:
        print(f'Pasta {pasta_base_musica} Já existe')
        
    pasta_playlist= os.path.join(pasta_base_musica, pl.title)   
    
    if not os.path.exists(pasta_playlist):
        os.mkdir(pasta_playlist)
        print(f'Pasta {pasta_playlist} Criada com sucesso')
    else:
        print(f'Pasta {pasta_playlist} Já existe')

    
    for video in pl.videos:
        ys = video.streams.get_audio_only()
        ys.download(output_path=pasta_playlist)


baixar_playlist("https://www.youtube.com/watch?v=H6Dbnk511FI&list=PLKVSwOHMv7b6WOb9xAkkB71XFedmhUSPH")

