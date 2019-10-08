from tkinter import *

class Aplicacao:
  def __init__(self, master=None):
      self.widget1 = Frame(master)
      self.widget1.pack()
      self.msg = Label(self.widget1, text = "Calculadora")
      self.msg["font"] = ("verdana", "10","normal", "bold")
      self.msg.pack()
      self.sair = Button(self.widget1)
      self.sair["text"] = "Fechar"
      self.sair["font"] = ("Verdana","10")
      self.sair["width"] = 5
      self.sair["command"] = self.widget1.quit
      self.sair.pack(side = LEFT)
      self.adicao = Button(self.widget1)
      self.adicao["text"] = "+"
      self.adicao["font"] = ("Verdana","10")
      self.adicao["width"] = 5
      self.adicao["command"] = self.widget1.quit
      self.adicao.pack(side = RIGHT)
    

root = Tk()
Aplicacao(root)
root.mainloop()

