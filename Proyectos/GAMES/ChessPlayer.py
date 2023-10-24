import chess
import tkinter as tk
from tkinter import messagebox
import random

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajedrez")

        self.board = chess.Board()
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onSquareClick)

        self.drawBoard()

    def drawBoard(self):
        self.canvas.delete("all")
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 * 50, y0 * 50
                self.canvas.create_rectangle(x0,y0,x1,y1, fill=color)
                piece = self.board.piece_at(chess.square(col, 7 - row))
                if piece:
                    self.canvas.create_text(x0 + 25, y0 + 25, text=str(piece), font=("Arial", 24), fill="black" if piece.color == chess.WHITE else "white")

    def onSquareClick(self, event):
        col = event.x // 50
        row = 7- event.y // 50
        square = chess.square(col,row)
        legal_moves = list(self.board.legal_moves)
        if self.board.turn == chess.WHITE and square in legal_moves:
            move = chess.Move.null()
            for m in legal_moves:
                if m.from_square == square:
                    move = m
                    break
            self.board.push(move)
            self.drawBoard()
            self.play_ai_move()
        elif self.board.turn == chess.BLACK:
            messagebox.showinfo("Espera", "Espera tu turno")

    def playAiMove(self):
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
            self.board.push(move)
            self.drawBoard()
        if self.board.is_checkmate():
            messagebox.showinfo("Fin de juego", "¡Juego terminado! Has ganado.")
        elif self.board.is_stalemate():
            messagebox.showinfo("Fin del juego", "Tablas por ahogado.")
        elif self.board.is_insufficient_material():
            messagebox.showinfo("Fin del juego", "Tablas por material insuficiente.")
        elif self.board.is_seventyfive_moves():
            messagebox.showinfo("Fin del juego", "Tablas por regla de los 75 movimientos.")
        elif self.board.is_fivefold_repetition():
            messagebox.showinfo("Fin del juego", "Tablas por repetición de posición.")

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()