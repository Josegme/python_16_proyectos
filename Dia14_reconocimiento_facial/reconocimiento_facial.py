"""
Paso 1: reconce facial
Paso 2: análisis facial - evalúa puntos de referencia del rostro
Paso 3: convertir imagen en datos HOG (huella digital del rostro)
es un cógigo numérico
Paso 4: Se compara con la BD de reconocimiento facial evaluando si
coiciden las métricas con alguno de los que tenemos dentro de nuestra BD
cmake - dlib - face-recognition - numpy - opencv-python
"""
from cv2 import cv2
import face_recognition as fr


# cargar imagenes
foto_control = fr.load_image_file(FotoA.jpg)
foto_prueba = fr.load_image_file(FotoB.jpg)

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar cara control
lugar_cara_A = fr.face_location(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# localizar cara control
lugar_cara_B = fr.face_location(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]), #ubicación
              (lugar_cara_A[1], lugar_cara_A[2]), #ubicación
              (0, 255, 0), # color
              2) #ancho de línea

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]), #ubicación
              (lugar_cara_B[1], lugar_cara_B[2]), #ubicación
              (0, 255, 0), # color
              2) #ancho de línea

# realizar comparación
resultado = fr.compare_faces([cara_codificada_A],
                             cara_codificada_B,
                             0.3) #cualquier valor superior a este -> no hay coincidencia
#entonces podemos manipular el límite de tolerancia

# medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# mostrar resultados
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (0,255,0),
            2)

# mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# mantener el programa abierto
cv2.waitKey(0)


