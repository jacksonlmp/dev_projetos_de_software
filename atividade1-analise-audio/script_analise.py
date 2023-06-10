import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

def plot_waveform(audio, sr):
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(audio, sr=sr)
    plt.title('Forma de Onda')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.show()

def plot_spectrogram(audio, sr):
    hop_length = 512
    n_fft = 2048
    spectrogram = librosa.stft(audio, hop_length=hop_length, n_fft=n_fft)
    spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))
    plt.figure(figsize=(12, 6))
    librosa.display.specshow(spectrogram_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma (dB)')
    plt.show()

def plot_frequency_spectrum(audio, sr):
    fft = np.fft.fft(audio)
    magnitude = np.abs(fft)
    frequency = np.linspace(0, sr, len(magnitude))
    plt.figure(figsize=(12, 4))
    plt.plot(frequency[:len(frequency)//2], magnitude[:len(frequency)//2])
    plt.title('Espectro de Frequência')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.show()

def interactive_menu():
    audio_path = "sunflower.mp3"
    audio, sr = librosa.load(audio_path)

    while True:
        print("\nMenu de Análise de Áudio")
        print("1. Plotar Forma de Onda")
        print("2. Plotar Espectrograma")
        print("3. Plotar Espectro de Frequência")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            plot_waveform(audio, sr)
        elif choice == "2":
            plot_spectrogram(audio, sr)
        elif choice == "3":
            plot_frequency_spectrum(audio, sr)
        elif choice == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    interactive_menu()
