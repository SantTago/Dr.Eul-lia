from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_and_convert_audio(url):
    try:
        # Criar um objeto YouTube com base no link
        yt = YouTube(url)

        # Selecionar a melhor qualidade de áudio disponível
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Baixar o arquivo de áudio
        audio_path = audio_stream.download(output_path='.', filename='audio')

        # Carregar o arquivo de áudio baixado
        audio_clip = AudioFileClip(audio_path)

        # Salvar o arquivo de áudio no formato MP3
        mp3_filename = 'audio.mp3'
        audio_clip.write_audiofile(mp3_filename)

        print('Download e conversão do áudio concluídos com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# URL do vídeo do YouTube
url = 'https://youtu.be/yqp_8uqpU2k?si=B1YbBJJuiDgVXVB7'

# Chamada da função para baixar e converter o áudio
download_and_convert_audio(url)
