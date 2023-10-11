import re
import random

from langcodes import best_match

bot_name = "Corvex"


def get_response(user_input):
    split_message = re.split(r'\s|[,.;:?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


print("Hola soy " + bot_name + ", te ayudaré en lo que necesites. Dime que necesitas? Por favor solo usar de manera formal y recuerda que soy solamente un bot.")
print("Recuerda que de igual manera si no entiendes algo puedes ver directamente el ClassRoom: https://classroom.google.com/c/MzE5MjI0NDU3OTk0")


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability( 
            message, list_of_words, single_response, required_words)

    response('Para hacer una sede, tienes que ir a nuevo contenido de envio y llenar los parametros que se te solicitan. Recuerda que el nombre siempre empieza con el tipo de envio, luego la sede y por último el área y programa. Por ejemplo: Mail Info - AR - CI - IPMII', [
             'como', 'hacer', 'crea', 'sedes', 'donde', 'sede', 'registro'], single_response=True)
    response('Se tienen que configurar 29 sedes. 23 sedes de habla hispana y 6 de habla portuguesa. Las abreviaturas de las sedes se encuentran en: https://drive.google.com/file/d/1Oj28DuNTTHpS9kOm8TkHk2aaxuHqzehT/view', [
             'cuantas', 'sedes', 'tienen', 'configuran', 'hacer', 'crear', 'generar', 'abreviaturas'], single_response=True)
    response('Para adjuntar archivos en local se tienen que subir desde el apartado de "archivos adjuntos" y darle a "nuevo". Luego se sube un archivo desde la computadora. Para adjuntar archivos en producción, se tienen que encadenar del contenido general de la misma área.', [
             'como', 'archivos', 'local', 'produccion', 'adjuntar'], single_response=True)
    response('El link del sistema de gestion en local es: http://esec-team.ctdesarrollo.org/team-sublime/sirius-app/Escritorio/login , y el de produccion es: https://sg.funiber.org/si/Escritorio/login', [
             'cual', 'sistema de gestion', 'link', 'produccion', 'local', 'sistema', 'gestion'], single_response=True)
    response('Para generar una prueba de carta te puedes apoyar en este video: https://www.youtube.com/watch?v=OCnKJVw83Es&t=31s', [
             'como', 'generar', 'pruebas', 'carta', 'cartas', 'envios', 'crear', 'hacer'], single_response=True)
    response('Me puedes consultar: creación de sedes, cantidad de sedes a configurar, adjuntar archivos, sistema de gestión, generar cartas, drive de plantillas...', [
             'que', 'puedo', 'preguntar', 'consultar', 'ayuda', 'ayudar', 'como', 'puedes', 'ayudarme', 'ayudame'], single_response=True)
    response('El drive de las plantillas HTML de las sedes se encuentra en: https://drive.google.com/drive/folders/12-7Esk7mTBNXW0rPoswLFy_bej-1kC0n?usp=sharing', [
             'donde', 'HTML', 'sedes', 'plantilla', 'esta', 'encuentro', 'encuentra', 'drive', 'html', 'cuales', 'plantillas', 'usar'], single_response=True)
    response('Los pasos para generar un Mail Info es: ir al sistema de gestion -> personalizar envios -> buscar area solicitada, programa solicitado', [
             'como', 'pasos', 'hacer', 'mail', 'info', 'peticion', 'informacion', 'que', 'generar', 'crear'], single_response=True)
    response('Los parametros que debes utilizar en LOCAL son: Para:"correopersonal@ct"; Bcc:"#SEDE_COPIA_OCULTA#"; de:"#SEDE_MAIL#"; Nombre Remitente:"BECA FUNIBER #SEDE_NOMBRE#"; Asunto:""BECA FUNIBER- #PROGRAMA_NOMBRE#', [
             'cuales', 'parametros', 'requeridos', 'tienen', 'parametro', 'que'], single_response=True)
    response('Los archivos adjuntos los tienes que sacar de producción directamente, esto para no tener problemas a la hora de tener algún archivo mal actualizado', [
             'cuales', 'archivos', 'requeridos', 'tienen', 'catalogos', 'adjuntos', 'adjuntar', 'adjuntos'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['Puedes decirlo otra vez?',
                'No te entendi bien', 'No te pude ayudar, pero le puedes decir a tu SL'][random.randrange(3)]


while True:
    print("Corvex: " + get_response(input('Tu: ')))
