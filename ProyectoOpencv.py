import cv2
import mediapipe
import math
import time
import serial

ser = serial.Serial('COM4', 9600, timeout=2)

# Se configura el dispositivo que captura el video
captura = cv2.VideoCapture(1)
captura.set(3, 1280)  # Se define el ancho de la ventana
captura.set(4, 720)  # Se define el alto de la ventana

# Variables para conteo
parpadeo = False
conteo = 0
tiempo = 0
inicio = 0
final = 0
conteo_sue = 0
muestra = 0

# Invocamos las funciones para los dibujos
mediapipeDibujo = mediapipe.solutions.drawing_utils
mediapipeEstilos = mediapipe.solutions.drawing_styles
configDibujo = mediapipeDibujo.DrawingSpec(thickness=1, circle_radius=1)

mediapipeMallaFacial = mediapipe.solutions.face_mesh
mallaFacial = mediapipeMallaFacial.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

while captura.isOpened:

    ret, video = captura.read()

    cuadroRGB = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)

    resultados = mallaFacial.process(cuadroRGB)

    px = []
    py = []
    lista = []
    r = 5
    t = 3

    if resultados.multi_face_landmarks:
        for rostros in resultados.multi_face_landmarks:
            mediapipeDibujo.draw_landmarks(
                video,
                rostros,
                mediapipeMallaFacial.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mediapipeEstilos.get_default_face_mesh_tesselation_style(),
            )
 
            for id, puntos in enumerate(rostros.landmark):
                al, an, c = video.shape
                x, y = int(puntos.x * an), int(puntos.y * al)
                px.append(x)
                py.append(y)
                lista.append([id, x, y])
                if len(lista) == 468:
                    x1, y1 = lista[145][1:]
                    x2, y2 = lista[159][1:]
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    longitud1 = math.hypot(x2 - x1, y2 - y1)

                    x3, y3 = lista[145][1:]
                    x4, y4 = lista[159][1:]
                    cx2, cy2 = (x3 + x4) // 2, (y3 + y4) // 2
                    longitud2 = math.hypot(x4 - x3, y4 - y3)

                    cv2.putText(
                        video,
                        f"Parpadeos: {int(conteo)}",
                        (20, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

                    cv2.putText(
                        video,
                        f"Micro sueños: {int(conteo_sue)}",
                        (350, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

                    cv2.putText(
                        video,
                        f"Duracion: {int(muestra)}",
                        (160, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )
                    # es lo que muestra la longitud del ojo.//
                    # cv2.putText(
                    #     video,
                    #     f"longitud1: {int(longitud1)}",
                    #     (20, 180),
                    #     cv2.FONT_HERSHEY_SIMPLEX,
                    #     1,
                    #     (0, 255, 0),
                    #     2,
                    # )

                    # cv2.putText(
                    #     video,
                    #     f"longitud2: {int(longitud2)}",
                    #     (350, 180),
                    #     cv2.FONT_HERSHEY_SIMPLEX,
                    #     1,
                    #     (0, 255, 0),
                    #     2,
                    # )

                    if longitud1 <= 15 and longitud2 <= 15 and parpadeo == False:
                        conteo += 1
                        parpadeo = True
                        inicio = time.time()
                    elif longitud1 > 15 and longitud2 > 15 and parpadeo == True:
                        ser.write(b'b')
                        parpadeo = False
                        final = time.time()
                       
                        
                    
                    tiempo = round(final - inicio, 0)

                    if tiempo > 2:
                            ser.write(b'a')

                    
                    if tiempo >= 2:
                        #Aqui hiria la instruccion de enceder el arduino con la letra 'a'                        
                        conteo_sue += 1
                        muestra = tiempo
                        inicio = 0
                        final = 0 
    if ret:
        cv2.imshow("Detección de sueño", video)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
captura.release()
cv2.destroyAllWindows()
