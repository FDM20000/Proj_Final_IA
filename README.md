# FERNANDO DIECKMANN MEDEIROS - PORTO ALEGRE - 632210070

# Visão Computacional para Monitoramento de Fechamento de Portão de Garagens em Condomínio

Este projeto utiliza técnicas de visão computacional para monitorar e identificar o acesso a um condomínio através do portão principal de garagens (acesso aos três andares).

Ele processa cada quadro do vídeo, identifica as regiões de interesse (portão e passagem de veículo) e analisa seu status (fechado, aberto sem veiculo depois de um determinado tempo e fechamento automático sem veículo).

Durante o processo armazena o frame e caso não haja o fechamento do portão, salva as informações de data, hora e frame inicial para verificação de possível infração a Convenção do Edifício.

O código foi desenvolvido em ETAPAS conforme as fases de análise e processamento das imagens, a saber:

# ETAPA 1: Definicao das áreas de interesse: 

Nesta etapa, foram definidas as regiões de interesse (ROIs) do vídeo que serão analisadas. 
Nela, `portao` é uma lista contendo as coordenadas (x, y, largura, altura) de duas áreas: a primeira ROI foca na região do portão e
a segunda ROI abrange uma área maior, incluindo a passagem onde o veículo deve passar após a abertura do portão.(ROIs);

# ETAPA 2: Carregamento do vídeo e inicio do loop de processamento:

O vídeo `entrada.mp4` é então carregado usando `cv2.VideoCapture` e um loop é iniciado para processar cada frame. 
Um método de subtração de fundo (Background Subtraction) é inicializado para identificar objetos em movimento. 
A variável `portao_fechado` é utilizada para rastrear o estado do portão e o `frames_desde_deteccao` controla o tempo desde a última detecção. 
A data e hora de início do vídeo são definidas para sincronizar os registros de infrações.

Ações:
   + Criado o objeto para background subtraction (MOG2)
   + Definição de variáveis para controlar o monitoramento do fechamento
   + Definiçâo do horário de início do vídeo - Para sincronizar o relógio neste exercício
   + Obtenção o FPS do vídeo
   + Inicialização do contador de frames processados
   + Leitura do frame atual do vídeo
   + Incremento do contador de frames processados

# ETAPA 3: Detectacao o veículo na área 1 (entrada):

Para cada frame, a subtração de fundo é aplicada para destacar objetos em movimento. 
Contornos são detectados na ROI do portão. 
Se a área de um contorno for maior que um limite (500 pixels), considera-se que um veículo entrou na área 1.

# ETAPA 4: Monitoramento o fechamento do portão:

Após a detecção de um veículo na área 1, o código monitora o fechamento do portão. 
Ele verifica se há mudanças significativas na ROI do portão nos frames subsequentes. 
Se a diferença entre os frames for superior a um limite, o portão é considerado fechado.

# ETAPA 5: Verificacao da saída da área 2 (veículo sai de "visão" e NÃO FECHA o portão):

Caso o portão não feche após a entrada do veículo, o código verifica se o veículo saiu da área 2 (passagem).
Se um contorno com área suficiente for detectado na ROI da área 2, 
assume-se que o veículo passou sem fechar o portão, configurando uma possível infração.

Ações:
   + Calculo do tempo decorrido (DESTE VÍDEO) e a data/hora da infração (SÍNCRONIA COM O VÍDEO)
   + Desenho das áreas de interesse no frame
   + Salvamento do frame como imagem

# ETAPA 6: Registro de infração:

Se uma infração é detectada, a data e hora da infração são registradas em um 
arquivo de texto (`provaveis_infracoes.txt`) e impressas no console. 
Uma imagem do primeiro frame com os dados iniciais da possível infração 
também é salva para verificação do registro no arquivo em txt.

Ações:
   + Salva em arquivo txt as prováveis infrações detectadas para posterior
     verificcação pela Administração e encaminhamento de Notificação ou Multa;

ETAPA 7: Libera os recursos do vídeo e fechar a janela

Após o processamento do vídeo, os recursos são liberados e
as janelas abertas pelo OpenCV são fechadas.

ETAPA 8: Publica resultados no Terminal e encerra análise.

# Considerações Finais

O video foi capturado pelo aplicativo ISIC Lite da Intelbras para efeitos deste trabalho.

Segundo orientações do Suporte Aplicativos <appsuporte@intelbras.com.br> para uso corrente do app como streaming "utilizar protocolo RTMP ou RTSP dependendo do modelo do gravador, porém terá que validar se sua aplicação é compatível com esses protocolos".

Como o app se mostra ser de grande utilidade na gestão dos riscos à segurança dos condomínios, pretendo aprimorar o app, provavelmente no Projeto Final da Graduação.




