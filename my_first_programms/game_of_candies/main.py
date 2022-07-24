from tkinter import *


def demo_f():
    root = Tk()
    root.title('Game of Candies!')
    root.geometry('600x600+300+100')
    root.mainloop()


window = Tk()
window.title('Game of Candies!')
window.geometry('360x150+300+100')
icon = PhotoImage(file='src/icon.png')
window.iconphoto(False, icon)
window.config(bg='#49423d')
# window_image = PhotoImage(file='src/throne.png')
# bg_image = Label(window, image=window_image, )
# bg_image.place(x=0, y=0, relwidth=1, relheight=1)
window.resizable(False, False)
logo_image = PhotoImage(file='src/game_logo.png')
Label(window, image=logo_image, bg='#49423d', height=50).pack()

play_btn = Button(window, text="Let's play", font='Calibri, 16', command=demo_f)
play_btn.pack(anchor='s')
window.mainloop()


def main():
    pass


if __name__ == "__main__":
    main()
