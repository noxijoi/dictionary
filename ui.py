from tkinter import *
import tkinter.ttk as  ttk

class AppUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Lab1")
        self.pack(fill=X, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=Y, side=LEFT)

        searchLbl = Label(frame1, text="Поиск")
        searchLbl.pack()

        searchFrame = Frame(frame1)
        searchFrame.pack(fill=X)

        searchEntry = Entry(searchFrame)
        searchEntry.pack(side=LEFT, fill=X, expand= True, padx=5, pady=5 )

        searchBtn = Button(searchFrame, text="Найти")
        searchBtn.pack(side=RIGHT)

        dictLbl = Label(frame1, text="Словарь")
        dictLbl.pack( padx=5, pady=5)

        dictList = Listbox(frame1, width=40)
        dictList.pack(fill=Y, expand=True, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=Y, padx=5, pady=5)

        txtLbl = Label(frame2, text="Bвод текста")
        txtLbl.pack()

        txtEntry = Text(frame2)
        txtEntry.pack(fill=BOTH, expand=True)

        textSubmitBtn = Button(frame2, text="Обработать")
        textSubmitBtn.pack()

        lexemLbl = Label(frame2, text="Лексема")
        lexemLbl.pack()

        newLexemBtn = Button(frame2, text="Добавить", command=lexemaModal)
        newLexemBtn.pack()

def lexemaModal(root, lexema):
    top = Toplevel(root)





def main():
    root = Tk()
    app = AppUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
