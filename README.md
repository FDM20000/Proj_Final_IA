# FERNANDO DIECKMANN MEDEIROS - PORTO ALEGRE - 632210070

# Visão Computacional para Monitoramento de Fechamento de Portão de Garagens em Condomínio

Este projeto utiliza técnicas de visão computacional para monitorar e identificar o acesso a um condomínio através do portão principal de garagens (acesso aos três andares).

Ele processa cada quadro do vídeo, identifica as regiões de interesse (portão e passagem de veículo) e analisa seu status (fechado, aberto sem veiculo depois de um determinado tempo e fechamento automático sem veículo).

Durante o processo armazena o frame e caso não haja o fechamento do portão, salva as informações de data, hora e frame inicial para verificação de possível infração a Convenção do Edifício.

O código foi desenvolvido em ETAPAS conforme as fases de análise e processamento das imagens, a saber:

ETAPA 1: Definicao das áreas de interesse (ROIs);

ETAPA 2: Carregamento do vídeo e inicio do loop de processamento;

   + Criado o objeto para background subtraction (MOG2)
   + Definição de variáveis para controlar o monitoramento do fechamento
   + Definiçâo do horário de início do vídeo - Para sincronizar o relógio neste exercício
   + Obtenção o FPS do vídeo
   + Inicialização do contador de frames processados
   + Leitura do frame atual do vídeo
   + Incremento do contador de frames processados

ETAPA 3: Detectacao o veículo na área 1 (entrada);

ETAPA 4: Monitoramento o fechamento do portão;

ETAPA 5: Verificacao da saída da área 2 (veículo sai de visão e NÃO FECHA o portão);

   + Calculo do tempo decorrido (DESTE VÍDEO) e a data/hora da infração (SÍNCRONIA COM O VÍDEO)
   + Desenho das áreas de interesse no frame
   + Salvamento do frame como imagem

ETAPA 6: Registro de infração;
   + Salva em arquivo txt as prováveis infrações detectadas para posterior verificcação pela Administração e encaminhamento de Notificação ou Multa;

ETAPA 7: Libera os recursos do vídeo e fechar a janela

ETAPA 8: Publica resultados no Terminal e encerra análise.

# Considerações Finais

O video foi capturado pelo aplicativo ISIC Lite da Intelbras para efeitos deste trabalho.

Segundo orientações do Suporte Aplicativos <appsuporte@intelbras.com.br> para uso corrente do app como streaming "utilizar protocolo RTMP ou RTSP dependendo do modelo do gravador, porém terá que validar se sua aplicação é compatível com esses protocolos".

Como o app se mostra ser de grande utilidade na gestão dos riscos à segurança dos condomínios, pretendo aprimorar o app, provavelmente no Projeto Final da Graduação.




