from functools import partial
from tkinter import *
import tkinter.ttk as ttk

from glossary import *
from vocab import Record

lexems =[]
dictList = None


def processText(txtEntry):
    print(txtEntry.get('1.0', END))



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
        searchEntry.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

        searchBtn = Button(searchFrame, text="Найти")
        searchBtn.pack(side=RIGHT)

        Label(frame1, text="Словарь").pack(padx=5, pady=5)
        global dictList
        dictList = Listbox(frame1, width=40)
        dictList.pack(fill=Y, expand=True, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=Y, padx=5, pady=5)

        Label(frame2, text="Bвод текста").pack()

        txtEntry = Text(frame2)
        txtEntry.pack(fill=BOTH, expand=True)

        textSubmitBtn = Button(frame2, text="Обработать текст", command=partial(processText, txtEntry))
        textSubmitBtn.pack()

        lexemLbl = Label(frame2, text="Лексема")
        lexemLbl.pack()

        newLexemBtn = Button(frame2, text="Добавить", command=partial(lexemaModal, self.parent))
        newLexemBtn.pack()


def getEndingsArray(entries=[]):
    endings =[]
    for entry in entries:
        str = entry.get()
        arr = str.split(' ')
        for ending in arr:
            ending.replace('-', '')
            endings.append(ending)
    return endings


def openMutableModal(root):
    top = Toplevel(root)

    tabParent = ttk.Notebook(top)
    nounTab = ttk.Frame(tabParent)  # существительное
    adjTab = ttk.Frame(tabParent)  # прилагательное
    verbTab = ttk.Frame(tabParent)  # глаголы
    ptrTab = ttk.Frame(tabParent)  # причастие
    numrTab = ttk.Frame(tabParent)  # числительное
    nproTab = ttk.Frame(tabParent)  # местоимение

    tabParent.add(nounTab, text="сущ")
    tabParent.add(adjTab, text="прил")
    tabParent.add(verbTab, text="глагол")
    tabParent.add(ptrTab, text="прич")
    tabParent.add(numrTab, text="числ")
    tabParent.add(nproTab, text="мест")

    ##вкладка для существительного
    Label(nounTab, text="Основа").pack()
    baseEntryNoun = Entry(nounTab)
    baseEntryNoun.pack()
    Label(nounTab, text="Окончания").pack()
    Label(nounTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч (6шт)").pack()
    singNounEntry = Entry(nounTab)
    singNounEntry.pack()
    Label(nounTab, text="введите окончания падежей в формате -<окончание> через пробел для мн.ч (6шт)").pack()
    plurNounEntry = Entry(nounTab)
    plurNounEntry.pack()
    Button(nounTab, text="Добавить", command=partial(saveMutableLexem,
                                                     NOUN,
                                                     baseEntryNoun.get(),
                                                     partial(getEndingsArray,[singNounEntry, plurNounEntry]))).pack()
    ##вкладка для прилагательного
    Label(adjTab, text="Основа").pack()
    baseEntryAdj = Entry(adjTab)
    baseEntryAdj.pack()
    Label(adjTab, text="Окончания").pack()
    Label(adjTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч м.р (6шт)").pack()
    singAdjEntryM = Entry(adjTab)
    singAdjEntryM.pack()
    Label(adjTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч ж.р (6шт)").pack()
    singAdjEntryF = Entry(adjTab)
    singAdjEntryF.pack()
    Label(adjTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч ср.р (6шт)").pack()
    singAdjEntryN = Entry(adjTab)
    singAdjEntryN.pack()
    Label(adjTab, text="введите окончания падежей в формате -<окончание> через пробел для мн.ч (6шт)").pack()
    plurAdjEntry = Entry(adjTab)
    plurAdjEntry.pack()
    Button(adjTab, text="Добавить", command=partial(saveMutableLexem,
                                                    ADJS,
                                                    baseEntryAdj,
                                                    partial(getEndingsArray,[singAdjEntryM,
                                                                      singAdjEntryF,
                                                                      singAdjEntryN,
                                                                      plurAdjEntry]))).pack()

    #вкладка для глаголов
    Label(verbTab, text="Основа").pack()
    baseEntryVerb = Entry(verbTab)
    baseEntryVerb.pack()
    Label(verbTab, text="Окончания").pack()
    Label(verbTab, text="введите окончания для лиц в формате -<окончание> через пробел для ед.ч (3шт)").pack()
    singVerbEntry = Entry(verbTab)
    singVerbEntry.pack()
    Label(verbTab, text="введите окончания для лиц в формате -<окончание> через пробел для мн.ч (3шт)").pack()
    plurVerbEntry = Entry(verbTab)
    plurVerbEntry.pack()
    Button(verbTab, text="Добавить", command=partial(saveMutableLexem,
                                                     VERB,
                                                     baseEntryVerb,
                                                     partial(getEndingsArray,
                                                         [singVerbEntry, plurVerbEntry]))).pack()

    # вкладка для причастий
    Label(ptrTab, text="Основа").pack()
    baseEntryPrtf = Entry(ptrTab)
    baseEntryPrtf.pack()
    Label(ptrTab, text="Окончания").pack()
    Label(ptrTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч м.р (6шт)").pack()
    singPrtfEntryM = Entry(ptrTab)
    singPrtfEntryM.pack()
    Label(ptrTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч ж.р (6шт)").pack()
    singPrtfEntryF = Entry(ptrTab)
    singPrtfEntryF.pack()
    Label(ptrTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч ср.р (6шт)").pack()
    singPrtfEntryN = Entry(ptrTab)
    singPrtfEntryN.pack()
    Label(ptrTab, text="введите окончания падежей в формате -<окончание> через пробел для мн.ч (6шт)").pack()
    plurPrtfEntry = Entry(ptrTab)
    plurPrtfEntry.pack()
    Button(ptrTab, text="Добавить", command=partial(saveMutableLexem,
                                                    PRTF,
                                                    baseEntryPrtf,
                                                    partial(getEndingsArray,[singPrtfEntryM,
                                                                     singPrtfEntryF,
                                                                     singPrtfEntryN,
                                                                     plurPrtfEntry]))).pack()

    #вкладка для числительных
    Label(numrTab, text="Основа").pack()
    baseEntryNumr = Entry(numrTab)
    baseEntryNumr.pack()
    Label(numrTab, text="Окончания").pack()
    Label(numrTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч (6шт)").pack()
    singnumrEntry = Entry(numrTab)
    singnumrEntry.pack()
    Label(numrTab, text="введите окончания падежей в формате -<окончание> через пробел для мн.ч (6шт)").pack()
    plurnumrEntry = Entry(numrTab)
    plurnumrEntry.pack()
    Button(numrTab, text="Добавить", command=partial(saveMutableLexem,
                                                     NUMR,
                                                     baseEntryNumr,
                                                     partial(getEndingsArray,
                                                         [singnumrEntry, plurnumrEntry]))).pack()
    #вкладка для местоимений
    Label(nproTab, text="Основа").pack()
    baseEntrynpro = Entry(nproTab)
    baseEntrynpro.pack()
    Label(nproTab, text="Окончания").pack()
    Label(nproTab, text="введите окончания падежей в формате -<окончание> через пробел для ед.ч (6шт)").pack()
    singnproEntry = Entry(nproTab)
    singnproEntry.pack()
    Label(nproTab, text="введите окончания падежей в формате -<окончание> через пробел для мн.ч (6шт)").pack()
    plurnproEntry = Entry(nproTab)
    plurnproEntry.pack()
    Button(nproTab, text="Добавить", command=partial(saveMutableLexem,
                                                     NPRO,
                                                     baseEntrynpro,
                                                     partial(getEndingsArray,
                                                         [singnproEntry, plurnproEntry]))).pack()

    tabParent.pack(expand=1, fill=BOTH)
    top.grab_set()
    top.focus_set()
    top.wait_window()


def getCasesEntriesList(root):
    casesFrame = Frame(root)
    casesFrame.grid()
    for case in CASES:
        caseFrame = Frame(casesFrame)
        caseFrame.grid()
        Label(caseFrame, text=CASES[case]).grid()
        Entry(casesFrame).grid()
    return casesFrame


def updateDict():
    dictList.delete(0,END)
    for lex in lexems:
        dictList.insert(0, lex.base)
    dictList.pack()


def saveMutableLexem(pos, baseEntry, entriesF):
    entries = entriesF()
    rec = Record(pos, baseEntry.get(), entries)
    global lexems
    lexems.append(rec)
    lexems = sorted(lexems, key=lambda l:l.base)
    updateDict()

def saveImmutableLexem(posSelect, baseEntry, entries=[]):
    rec = Record(posSelect.curselection(), baseEntry.get(), entries)
    global lexems
    lexems.append(rec)
    lexems = sorted(lexems, key=lambda l:l.base)
    updateDict()

def openImmutableModal(root):
    top = Toplevel(root)
    posListBox = Listbox(top)

    for immutable in IMMUTABLES:
        posListBox.insert(0, POS[immutable])
    posListBox.pack()

    Label(top, text="Основа").pack()
    baseEntry = Entry(top)
    baseEntry.pack()

    submitBtn = Button(top, text="Сохранить", command=partial(saveImmutableLexem,
                                                              posListBox,
                                                              baseEntry))
    submitBtn.pack()
    top.grab_set()
    top.focus_set()
    top.wait_window()


def lexemaModal(root):
    top = Toplevel(root)

    lbl = Label(top, text="Выберите какая ваша часть речи")
    lbl.pack()
    mutableBtn = Button(top, text="Изменяемая", command=partial(openMutableModal, top))
    mutableBtn.pack()

    immutableBtn = Button(top, text="Неизменяемая", command=partial(openImmutableModal, top))
    immutableBtn.pack()

    top.grab_set()
    top.focus_set()
    top.wait_window()


def main():
    root = Tk()
    app = AppUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
