## Análise de Áudio Interativa
Este script Python permite a análise interativa de um arquivo de áudio utilizando a biblioteca Librosa. O usuário pode escolher entre três opções de análise: plotar a forma de onda do áudio, plotar o espectrograma ou plotar o espectro de frequência.

Requisitos:
- Python 3.x
- Bibliotecas: librosa, matplotlib

Uso:
1. Certifique-se de ter instalado as bibliotecas necessárias, executando `pip install librosa matplotlib` em seu ambiente Python.
2. Coloque o arquivo de áudio que deseja analisar no mesmo diretório do script.
3. Execute o script e siga as instruções no menu interativo para escolher a análise desejada.

Funções:
1. plot_waveform(audio, sr):
   - Plota a forma de onda do áudio.
   - Parâmetros:
     - audio: array unidimensional contendo os dados do áudio.
     - sr: taxa de amostragem do áudio.
   - ![image](https://github.com/jacksonlmp/dev_projetos_de_software/assets/45649262/c177fa25-de95-4beb-bfa9-5b3532f0f4ca)


2. plot_spectrogram(audio, sr):
   - Calcula e plota o espectrograma do áudio.
   - Parâmetros:
     - audio: array unidimensional contendo os dados do áudio.
     - sr: taxa de amostragem do áudio.
   - ![image](https://github.com/jacksonlmp/dev_projetos_de_software/assets/45649262/a07f2f97-515e-4531-8e95-bb046f382e8e)


3. plot_frequency_spectrum(audio, sr):
   - Calcula e plota o espectro de frequência do áudio.
   - Parâmetros:
     - audio: array unidimensional contendo os dados do áudio.
     - sr: taxa de amostragem do áudio.
   - ![image](https://github.com/jacksonlmp/dev_projetos_de_software/assets/45649262/68229be6-04d4-4e96-8c62-c59a7c436a3c)


4. interactive_menu():
   - Cria um menu interativo onde o usuário pode escolher a análise de áudio desejada.
   - Carrega o áudio e chama a função correspondente com base na escolha do usuário.

Fluxo de execução:
1. O usuário executa o script.
2. O menu interativo é exibido, apresentando as opções disponíveis.
3. O usuário escolhe uma opção digitando o número correspondente.
4. Com base na escolha do usuário, a função correspondente é chamada para realizar a análise de áudio e plotar o gráfico correspondente.
5. O gráfico é exibido.
6. O menu é exibido novamente, permitindo que o usuário escolha outra opção ou saia do programa.

Observações:
- O usuário precisa fornecer o caminho correto para o arquivo de áudio no código, substituindo "caminho/do/arquivo/audio.wav" pelo caminho real do arquivo de áudio que deseja analisar.
- Certifique-se de não ter arquivos ou pacotes com o nome "matplotlib" no mesmo diretório do script, pois pode causar conflito de nomes.
- Caso ocorram erros, verifique se as bibliotecas "librosa" e "matplotlib" estão instaladas corretamente em seu ambiente Python.
