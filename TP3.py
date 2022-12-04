from Codigos2 import *
from tkinter import *
from tkinter import filedialog,END
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
class TelaPrincipal:
    def __init__(self):
        #Configuração da tela tkinter
        global Img
        Img = "Image.jpg"
        self.tela = ttk.Window(themename="journal")  
        self.tela.title("TP3")
        self.tela.geometry("250x250")

        #Butões
        self.ButtonAbrir = ttk.Button(self.tela, text="Clique para abrir a imagem", command=lambda: self.AbriImg(Img))
        self.ButtonAbrir.grid(padx=45, pady=85)
        self.tela.mainloop()
    
    def AbriImg(self,Img):
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
        
        self.t1 = Text(self.top,  height=4, width=13) # added one text box
        self.t1.place(x=640,y=250)

        #Imagem
        self.canv = Canvas(self.top, width=560, height=380, bg='black')
        self.canv.grid(row=2, column=2,padx=75,pady=25)
        Img = ImageTk.PhotoImage(Image.open(Img))  # PIL solution
        self.canv.create_image(5, 5, anchor=NW, image=Img)
        
        #MenuBar

        self.menubar = Menu(self.top)
        self.my_font1=('Times',12,'bold')
        menu_f = Menu(self.menubar,title='my title',tearoff=0) # file

        self.menubar.add_cascade(label="Arquivos", menu=menu_f) # Top Line

        menu_f.add_command(label="Nova Imagem", command=lambda:self.open_file())
        menu_f.add_command(label="Salvar Texto", command=lambda:self.save_file())
        menu_f.add_command(label="Salvar Texto Como..", command=lambda:self.save_as_file())
        menu_f.add_command(label="Exit", command=self.top.quit)
        self.top.config(menu=self.menubar) # adding menu to window
        
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
    def save_file(self):
        global file_name # collect the file name
        if(file_name=='untitle.txt'): # if default file name is still there
            self.save_as_file() # call the function
        else:
            fob=open(file_name,'w') # open in write mode
            my_str1=self.t1.get("1.0",END) # collect the data from text widget
            print(my_str1.split("\n"))
            my_str1 = [mystr+"\n" for mystr in my_str1.split("\n") if mystr != ""]
            fob.write("".join(my_str1))  # write to file
        
    def save_as_file(self):
        file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
        if file: # if user has not cancelled the dialog to save
            fob=open(file,'w') # open the file in write mode
            my_str1=self.t1.get("1.0",END) # collect the data from text widget
            fob.write(my_str1)  # write to file
    
    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("jpg file", ".jpg")],
            defaultextension=".jpg")
        global Img
        Img=file # set the file name
        Salvar(Img)
        self.AbriImg("Image.jpg")

tela = TelaPrincipal()