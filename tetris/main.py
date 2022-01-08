import tkinter as tk
import tetris

def main():
    win = tk.Tk()
    app = tetris.TETRIS(master = win)
    app.mainloop()

if __name__ == "__main__":
    main()