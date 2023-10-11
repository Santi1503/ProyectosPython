from tkinter import *
from Proyectos.BOTS.ChatBot1 import get_response, bot_name

bg_gray = "#ABB2B9"
bg_color="#17202A"
text_color="#EAECEE"

FONT = "Arial 12"
FONT_BOLD = "Arial 10 bold"

class ChatBot:
    def __init__(self):
        self.window =Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("chat")
        self.window.resizable(width= False, height=False)
        self.window.configure(width=450, height=525, bg=bg_color)

if __name__=="__main__":
    app = ChatBot()
    app.run()
