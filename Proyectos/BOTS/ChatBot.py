import sys
import re
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

bot_name = "Rodulfo Domingo"


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


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    response('Para hacer una sede, tienes que...', [
             'como', 'hacer', 'crea', 'sedes', 'donde', 'sede', 'registro'], single_response=True)
    response('Se tienen que configurar ... se encuentran en: https://github.com/Santi1503', [
             'cuantas', 'sedes', 'tienen', 'configuran', 'hacer', 'crear', 'generar', 'abreviaturas'], single_response=True)
    response('Para adjuntar archivos ...', [
             'como', 'archivos', 'local', 'produccion', 'adjuntar'], single_response=True)
    response('El link... es: https://github.com/Santi1503 , y ... https://github.com/Santi1503', [
             'cual', 'sistema de gestion', 'link', 'produccion', 'local', 'sistema', 'gestion'], single_response=True)
    response('Para generar ...: https://github.com/Santi1503', [
             'como', 'generar', 'pruebas', 'carta', 'cartas', 'envios', 'crear', 'hacer'], single_response=True)
    response('Me puedes consultar: ...', [
             'que', 'puedo', 'preguntar', 'consultar', 'ayuda', 'ayudar', 'como', 'puedes', 'ayudarme', 'ayudame'], single_response=True)
    response('El drive ...: https://github.com/Santi1503', [
             'donde', 'HTML', 'sedes', 'plantilla', 'esta', 'encuentro', 'encuentra', 'drive', 'html', 'cuales', 'plantillas', 'usar'], single_response=True)
    response('Los pasos ...', [
             'como', 'pasos', 'hacer', 'mail', 'info', 'peticion', 'informacion', 'que', 'generar', 'crear'], single_response=True)
    response('Los parametros que ...', [
             'cuales', 'parametros', 'requeridos', 'tienen', 'parametro', 'que'], single_response=True)
    response('Los ...', [
             'cuales', 'archivos', 'requeridos', 'tienen', 'catalogos', 'adjuntos', 'adjuntar', 'adjuntos'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['Puedes decirlo otra vez?',
                'No te entendi bien', 'No te pude ayudar, pero le puedes decir a tu SL'][random.randrange(3)]
    return response


class ChatbotGUI(QWidget):
    def __init__(self):
        print("iniciando chat...")
        super().__init__()
        self.init_ui()
        self.append_message("Hola soy " + bot_name + ", te ayudaré en lo que necesites. Dime que necesitas? Por favor solo usar de manera formal y recuerda que soy solamente un bot.", QColor("#1617FE"))
        self.append_message("", QColor("#1617FE"))
        self.append_message("", QColor("#1617FE"))

    def init_ui(self):
        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: #F4EDE8;")

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        
        font = QFont("Arial", 12)
        
        self.text_edit.setFont(font)

        self.input_line = QLineEdit()
        self.input_line.returnPressed.connect(self.send_message)

        send_button = QPushButton("Send")
        send_button.setStyleSheet("background-color: #00007A; color: white;")
        send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_line)
        input_layout.addWidget(send_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

    def send_message(self):
        user_input = self.input_line.text()
        self.append_message("You: " + user_input, QColor("#1617FE"))
        response = get_response(user_input)
        self.append_message(bot_name + " :" + response, QColor("#007FFE"))
        self.input_line.clear()

    def append_message(self, message, color):
        self.text_edit.setTextColor(color)
        self.text_edit.append(message)
        self.text_edit.setTextColor(Qt.black)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotGUI()
    window.show()
    sys.exit(app.exec_())