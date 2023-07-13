import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():

    #almacenar recognizer en una variable
    r = sr.Recognizer()

    #configurar el microfono

    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print('ya puedes hablar')

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language='es-ar')

            #prueba de que pudo ingresar
            print(f'Dijiste: {pedido}')

            #devolver pedido
            return pedido
        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print('ups, no entendi')

            #devolver error
            return 'sigo esperando'
        #en caso de no poder resolver el pedido
        except sr.RequestError:
            #prueba de que no comprendio el audio
            print('ups, no hay servicio')

            #devolver error
            return 'sigo esperando'

        # error inesperado

        except:
            #prueba de que no comprendio el audio
            print('ups, algo ha salido mal')

            #devolver error
            return 'sigo esperando'


# funcion para que el asistente piueda ser escuchado

def hablar(mensaje):


    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar el día de la semana

def pedir_dia():

    #crear variab le con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    hablar(f'Hoy es {calendario[dia_semana]}')

def pedir_hora():


    #crear variable con datos de hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} con {hora.minute} minutos y {hora.second} segndos'
    print(hora)

    #decir la hora
    hablar(hora)

# saludo inicial
def saludo_inicial():

    #crear variable con datos de hora

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    #decir el saludo
    hablar(f'{momento}, soy escarlet, tu asistente personal. Por favor, dime en qué te puedo ayudar')

# funcion central del asistente

def pedir_cosas():
    #activar el saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:


        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'podemos garchar' in pedido:
            hablar('Que chistoso eres Enzo, si no se entera Agustina me encantaría')
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo lo hago')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Genial, ya mismo lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'nos vemos' in pedido:
            hablar('Perfecto Enzo, me voy a descansar, cualquier cosa me chiflas')
            break

pedir_cosas()
