"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Metodos de segmentación - TEST

@author: David Felipe Cuellar Diaz
"""


import os
import segGrabCut

directory = os.getcwd()

folderin = directory + "/"

tipo=["GRE","NIR","RGB"]

form=[".TIF",".JPG"]

imagein=["","IMG_170805_165709_0138_"]
	
image= folderin + imagein[1] + tipo[2] + form[1]
folder = folderin + "/results/"

skm=segGrabCut.segmentacion(image=image,folder=folder,rgb=True, resize=True, scalefactor=1/5)

skm.grabcut()
    
