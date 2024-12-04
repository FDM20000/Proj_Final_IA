

import cv2
import datetime

# ETAPA 1: Definir as áreas de interesse (ROIs)

portao = [
    [1077, 193, 42, 34],  # Área 1: Região do portão (x, y, largura, altura)
    [516, 435, 339, 249]   # Área 2: Região maior englobando a passagem (x, y, largura, altura)
]

# ETAPA 2: Carregar o vídeo e iniciar o loop de processamento

video = cv2.VideoCapture('entrada.mp4')

# Criar o objeto para background subtraction (MOG2)

fgbg = cv2.createBackgroundSubtractorMOG2()

# Variáveis para controlar o monitoramento do fechamento

portao_fechado = False
frames_desde_deteccao = 0

# Definir o horário de início do vídeo - Para sincronizar o relógio neste exercício

horario_inicio_video = datetime.datetime(2024, 11, 28, 17, 52, 22)

# Obter o FPS do vídeo

fps = video.get(cv2.CAP_PROP_FPS)

# Inicializar o contador de frames processados

frames_processados = 0

while video.isOpened():

    # Ler o frame atual do vídeo

    ret, frame = video.read()
    if not ret:
        break

    # Incrementar o contador de frames processados

    frames_processados += 1

# ETAPA 3: Detectar o veículo na área 1 (entrada)

    fgmask = fgbg.apply(frame)
    roi_portao = fgmask[portao[0][1]:portao[0][1] + portao[0][3],
                        portao[0][0]:portao[0][0] + portao[0][2]]
    contornos, _ = cv2.findContours(roi_portao, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        if cv2.contourArea(contorno) > 500:

# ETAPA 4: Monitorar o fechamento do portão

            portao_fechado = False
            frames_desde_deteccao = 0
            while not portao_fechado and frames_desde_deteccao < 30:
                ret, frame_atual = video.read()
                if not ret:
                    break
                fgmask_atual = fgbg.apply(frame_atual)
                roi_portao_atual = fgmask_atual[portao[0][1]:portao[0][1] + portao[0][3],
                                                portao[0][0]:portao[0][0] + portao[0][2]]
                diferenca = cv2.absdiff(roi_portao, roi_portao_atual)
                if cv2.countNonZero(diferenca) > 100:
                    portao_fechado = True
                frames_desde_deteccao += 1

# ETAPA 5: Verificar saída da área 2 (veículo sai de visão e NÃO FECHA o portão)

            if not portao_fechado:
                roi_area2 = fgmask_atual[portao[1][1]:portao[1][1] + portao[1][3],
                                        portao[1][0]:portao[1][0] + portao[1][2]]
                contornos_area2, _ = cv2.findContours(roi_area2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for contorno_area2 in contornos_area2:
                    if cv2.contourArea(contorno_area2) > 500:

            # Calcular o tempo decorrido (DESTE VÍDEO) e a data/hora da infração (TORNAR SÍNCRONA COM O VÍDEO):

                        tempo_decorrido = datetime.timedelta(seconds=frames_processados / fps)
                        data_hora = (horario_inicio_video + tempo_decorrido).strftime("%Y-%m-%d %H:%M:%S")

            # Desenhar as áreas de interesse no frame

                        cv2.rectangle(frame_atual, (portao[0][0], portao[0][1]), (portao[0][0] + portao[0][2], portao[0][1] + portao[0][3]), (0, 255, 0), 2)
                        cv2.rectangle(frame_atual, (portao[1][0], portao[1][1]), (portao[1][0] + portao[1][2], portao[1][1] + portao[1][3]), (0, 255, 0), 2)

            # Salvar o frame como imagem

                        nome_arquivo = f"infracao_{data_hora}.jpg"
                        cv2.imwrite(nome_arquivo, frame_atual)


# ETAPA 6: Registrar infração

                        with open("provaveis_infracoes.txt", "a") as arquivo_infracoes:
                            arquivo_infracoes.write(f"Provavel infracao detectada com inicio em: {data_hora}\n")
                        print(f"Provavel infracao detectada com inicio em: {data_hora}")
                        break

# ETAPA 7: Liberar os recursos do vídeo e fechar a janela

video.release()
cv2.destroyAllWindows()