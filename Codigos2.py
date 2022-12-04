from tkinter import *
from PIL import Image, ImageEnhance,ImageFilter, ImageTk
from tkinter import filedialog,END
from tkinter.filedialog import asksaveasfilename
global tela

def RodarImg(img,graus):
    img = Image.open(img)
    img = img.rotate(graus)
    img.save("Image.jpg")

def Brilho(img,br):
    img = Image.open(img)
    img = ImageEnhance.Brightness(img)
    img.enhance(int(br)).save("Image.jpg")

def Redimensionar(img):
    img = Image.open(img)
    img = img.resize((607, 369))
    img.save("Image.jpg")

def Borrar(img):
    img = Image.open(img)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.save("Image.jpg")

def Salvar(img):
    img = Image.open(img)
    img.save("Image.jpg")
