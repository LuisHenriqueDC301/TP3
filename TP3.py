from Codigos2 import *
from tkinter import *
from PIL import ImageTk, Image

class TelaPrincipal:
    def __init__(self):
        #Configuração da tela tkinter
        self.tela = Tk()  
        self.tela.title("TP3")
        self.tela.geometry("250x250")

        #Butões
        self.ButtonAbrir = Button(self.tela, text="Clique para abrir a imagem", height="3", command=lambda: self.AbriImg("Image.jpg"))
        self.ButtonAbrir.grid(padx=45, pady=85)
        self.tela.mainloop()
    
    def AbriImg(self,img):
        self.top = Toplevel() 
        self.top.geometry("750x520")  
    
        #Butões 
        self.ButtonRodar = Button(self.top, text="Rodar a Imagem", command=lambda:self.AtualizarImg("Rodar"))
        self.ButtonRodar.place(x=120,y=450)
        
        self.ButtonBorrar = Button(self.top, text="Borrar a Imagem", command=lambda:self.AtualizarImg("Borrar"))
        self.ButtonBorrar.place(x=250,y=450)
        
        self.ButtonRedimensionar = Button(self.top, text="Redimensionar", command=lambda:self.AtualizarImg("Redi"))
        self.ButtonRedimensionar.place(x=380,y=450)
        
        self.ButtonAumentar = Button(self.top, text="Aumentar o Brilho", command=lambda:self.AtualizarImg("Brilho"))
        self.ButtonAumentar.place(x=510,y=450)
        
        #Imagem
        self.canv = Canvas(self.top, width=560, height=380, bg='black')
        self.canv.grid(row=2, column=2,padx=75,pady=25)
        img = ImageTk.PhotoImage(Image.open(img))  # PIL solution
        self.canv.create_image(5, 5, anchor=NW, image=img)
        self.top.mainloop()

    def AtualizarImg(self,c):
        if c == 'Rodar':
            RodarImg("Image.jpg",90)
        elif c == "Brilho":
            Brilho("Image.jpg",5)
        elif c == "Redi":
            Redimensionar("Image.jpg")
        elif c == "Borrar":
            Borrar("Image.jpg")
        self.AbriImg("Image.jpg")

tela = TelaPrincipal()