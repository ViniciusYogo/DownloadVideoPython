from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os

def baixar_video(url, diretorio, callback_progresso=None):
    yt = YouTube(url, on_progress_callback=callback_progresso)
    print(f"Baixando vídeo: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=diretorio)  # Salva no diretório especificado
    print("Download concluído!")

def baixar_audio(url, diretorio, callback_progresso=None):
    try:
        yt = YouTube(url, on_progress_callback=callback_progresso)
        print(f"Baixando áudio: {yt.title}")
        stream = yt.streams.get_audio_only()
        stream.download(output_path=diretorio)  # Salva no diretório especificado
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar áudio: {e}")

def sanitizar_nome_pasta(nome):
    caracteres_invalidos = r'<>:"/\|?*[]'
    for char in caracteres_invalidos:
        nome = nome.replace(char, '_')
    return nome

def baixar_playlist(url, diretorio, callback_progresso=None):
    try:
        pl = Playlist(url)
        print(f"Baixando playlist: {pl.title}")
        nome_playlist_sanitizado = sanitizar_nome_pasta(pl.title)
        pasta_playlist = os.path.join(diretorio, nome_playlist_sanitizado)  # Usa o diretório especificado
        
        if not os.path.exists(pasta_playlist):
            os.mkdir(pasta_playlist)
            print(f'Pasta da playlist "{pasta_playlist}" criada com sucesso.')
        
        total_videos = len(pl.videos)  # Número total de vídeos na playlist
        progresso_por_video = 100 / total_videos  # Progresso que cada vídeo contribui para a barra

        for i, video in enumerate(pl.videos):
            try:
                print(f"Baixando: {video.title} ({i + 1}/{total_videos})")

                # Função de callback para atualizar o progresso do vídeo atual
                def atualizar_progresso_video(stream, chunk, bytes_remaining):
                    if callback_progresso:
                        # Calcula o progresso do vídeo atual
                        tamanho_total = stream.filesize
                        bytes_baixados = tamanho_total - bytes_remaining
                        progresso_video = (bytes_baixados / tamanho_total) * progresso_por_video

                        # Calcula o progresso total da playlist
                        progresso_total = (i * progresso_por_video) + progresso_video
                        callback_progresso(progresso_total)  # Atualiza a barra de progresso

                video.register_on_progress_callback(atualizar_progresso_video)  # Registra o callback
                stream = video.streams.get_audio_only()
                stream.download(output_path=pasta_playlist)
                print(f"Concluído: {video.title}")
            except Exception as e:
                print(f"Erro ao baixar o vídeo {video.title}: {e}")
    except Exception as e:
        print(f"Erro ao processar a playlist: {e}")