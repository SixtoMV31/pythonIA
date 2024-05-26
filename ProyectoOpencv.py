import cv2
import mediapipe
import math
import time

# Se configura el dispositivo que captura el video
captura=cv2.VideoCapture(1)
cap.set(3, 1280)    # Se define el ancho de la ventana
cap.set(4, 720)     # Se define el alto de la ventana

# Variables para conteo
parpadeo = False
conteo = 0
tiempo = 0
inicio = 0
final = 0
conteo_sue = 0
muestra = 0

# Invocamos las funciones para los dibujos
mediapipeDibujo = mediapipe.drawing_utils
configDibujo = mediapipeDibujo.DrawingSpec(thickness = 1, circle_radius = 1)

mediapipeMallaFacial = mediapipe.solutions.face_mesh
mallaFacial = mediapipeMallaFacial.FaceMesh(max_num_faces = 1)

while (captura.isOpened):
    
    ret, video = captura.read()
    
    cuadroRGB =  cv2.cvtColor(video, cv2.BGR2RGB )
    
    resultados = mallaFacial.proccess(cuadroRGB)
    
    px = []
    py = []
    lista = []
    r = 5
    t = 3
    
    if resultados.multi_face_landmarks:
        for rostros in resultados.multi_face_landmarks:
            mediapipeDibujo.draw_landmarks(video, rostros, mediapipeMallaFacial.FACE_CONNECTIONS, configDibujo)
            
            for id, puntos in enumerate(rostros.landmark):
                al, an, c = video.shape
                x, y = int(puntos.x * an), int(puntos.y * al)
                px.append(x)
                py.append(y)
                lista.append([id, x, y])
                if len(lista) == 468:
                    
    if (ret):
        video=cv2.flip(video,1)
        cv2.imshow("frame",video)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
captura.release()
cv2.destroyAllWindows()