import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en una variable
    r = sr.Recognizer()

    # configuarar el microfono
    with sr.Microphone() as origen:

        print("Configurando el micrófono..")

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabación
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-AR")

            # prueba de que pudo ingresar
            print("Dijiste: "+ pedido)

            # devolver pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el
            print("Ups, no entendí.")

            # devolver error
            return  "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no hay servicio.")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"

# función para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar el día de la semana
def pedir_dia():

    # crear variable con datos
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábados',
                  6: 'Domingos'}

    # decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# informar que hora es
def pedir_hora():

    # crear una variable, con datos de la hora
    hora = datetime.datetime.now()
    hora = (f'En este momento son las {hora.hour}'
            f' horas con {hora.minute} minutos'
            f'y {hora.second} segundos')
    print(hora)

    # decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if 20 < hora.hour < 6:
        momento = 'Buenas noches!'
    elif  6 <= hora.hour < 13:
        momento = 'Buen día!'
    else:
        momento = 'Buenas tardes!'

    # decir el saludo
    hablar(f'{momento}, soy Vicky, tu asistente personal. Por favor, dime en que te puedo ayudar!')

# Funcion principal del asistente
def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto lindo, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro cariño, estoy en eso.')
            webbrowser.open('https://google.com')
            continue
        elif 'que día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia en este momento')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso.')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado: ')
            continue
        elif 'reproducir' in pedido:
            hablar('Genial, ya busco ese tema')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón, no la he encontrado')
                continue
        elif 'listo' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()






