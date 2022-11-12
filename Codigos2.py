from tkinter import *
from PIL import Image, ImageEnhance,ImageFilter, ImageTk
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
    img = img.resize((round(img.size[0]*1.5), round(img.size[1]*3.5)))
    img.save("Image.jpg")

def Borrar(img):
    img = Image.open(img)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img.save("Image.jpg")

