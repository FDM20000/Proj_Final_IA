# FERNANDO DIECKMANN MEDEIROS - PORTO ALEGRE - 632210070

# Visão Computacional para Monitoramento de Fechamento de Portão de Garagens em Condomínio

Este projeto utiliza técnicas de visão computacional para monitorar e identificar o acesso a um condomínio através do portão principal de garagens (acesso aos três andares).
Ele processa cada quadro do vídeo, identifica as regiões de interesse (portão e veículo) e destaca seu status (fechado, aberto com veículo, aberto sem veiculo depois de um determinado tempo e fechamento automático sem veículo).
Durante o processo armazena o frame com o veiculo passante e, caso não haja o fechamento do portão, salva as informações de data, hora e frame do veículo em um arquivo.

## Função `processa_frame`

A função `processa_frame` é responsável por processar uma imagem para destacar as áreas de interesse. Abaixo está uma descrição detalhada do que cada etapa da função faz.

```python
def processa_frame(img):
    """
    Processa a imagem para destacar as áreas de interesse.
    """
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_threshold = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    img_blur = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.int8)
    img_dil = cv2.dilate(img_blur, kernel)
    return img_dil
```

### Descrição das Etapas

1. **Conversão para Escala de Cinza (`cv2.cvtColor`)**:

   - A imagem colorida em formato BGR é convertida para uma imagem em escala de cinza. Isso facilita o processamento subsequente, pois reduz a complexidade dos dados (de 3 canais de cor para 1 canal de intensidade).

2. **Limiar Adaptativo (`cv2.adaptiveThreshold`)**:

   - Aplica um limiar adaptativo à imagem em escala de cinza para convertê-la em uma imagem binária (preto e branco), invertendo os valores. Isso ajuda a destacar as áreas de interesse, tornando-as brancas sobre um fundo preto.
   - Parâmetros:
     - `src`: imagem de entrada em escala de cinza.
     - `maxValue`: valor a ser dado aos pixels que atendem à condição (255 no caso de binário invertido).
     - `adaptiveMethod`: método para calcular o valor do limiar (cv2.ADAPTIVE_THRESH_GAUSSIAN_C usa a média ponderada de uma vizinhança gaussiana).
     - `thresholdType`: tipo de limiar (cv2.THRESH_BINARY_INV inverte os valores binários).
     - `blockSize`: tamanho da área local (25x25 pixels) para calcular o valor do limiar.
     - `C`: constante subtraída da média ou ponderação calculada (neste caso, 16).

3. **Desfocagem Mediana (`cv2.medianBlur`)**:

   - Aplica um filtro de mediana para reduzir o ruído na imagem binária. A mediana é eficaz na remoção de ruídos sal e pimenta, preservando as bordas.
   - Parâmetros:
     - `src`: imagem de entrada.
     - `ksize`: tamanho da janela do filtro (número ímpar, neste caso, 5x5).

4. **Criação do Kernel de Dilatação (`np.ones`)**:

   - Cria um kernel (matriz) de 3x3 preenchido com valores 1, que será usado na operação de dilatação.
   - Parâmetros:
     - `(3, 3)`: tamanho da matriz.
     - `np.int8`: tipo dos elementos da matriz.

5. **Dilatação da Imagem (`cv2.dilate`)**:
   - A dilatação aumenta as áreas brancas na imagem, ajudando a unir regiões próximas e preencher pequenos buracos nas áreas de interesse. Isso torna os objetos de interesse mais contínuos e destacados.
   - Parâmetros:
     - `src`: imagem de entrada.
     - `kernel`: kernel de convolução.

### Observações

- Certifique-se de que o vídeo (`parkinglot.mp4`) está no diretório correto.
- Adapte os parâmetros de processamento conforme necessário para seu cenário específico.

Claro! Aqui está um exemplo de um `README.md` curto e direto ao ponto para o seu projeto de seleção de múltiplas regiões de interesse (ROIs) em um vídeo:

# Seleção de Múltiplas Regiões de Interesse (ROIs)

Permite selecionar múltiplas regiões de interesse (ROIs) em um quadro específico de um vídeo. As ROIs selecionadas são exibidas e suas coordenadas são impressas no terminal.

### Executando o Script

1. **Defina o caminho para o seu vídeo e o número do quadro a ser capturado no script `roi.py`:**

```python
# Caminho para o vídeo
video_path = 'vagas/parkinglot.mp4'

# Número do quadro a ser capturado
frame_number = 100  # Altere para o número do quadro que você deseja capturar
```

2. **Execute o script `roi.py`:**

```bash
python roi.py
```

3. **Selecione as regiões de interesse:**

   - Uma janela será aberta com o quadro do vídeo.
   - Use o mouse para desenhar retângulos nas áreas de interesse.
   - Pressione `Enter` para confirmar cada seleção.
   - Para selecionar mais outra região, pressione `Enter` novamente.
   - Para sair do modo de seleção, pressione a tecla `q` para cada seleção feita.

### Exemplo de Saída

O script imprimirá as coordenadas das regiões de interesse selecionadas no terminal:

```
Região de interesse 1: x=124, y=81, w=123, h=223
Região de interesse 2: x=282, y=86, w=127, h=215
...
```
