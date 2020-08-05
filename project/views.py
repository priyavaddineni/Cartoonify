import requests
import sys
import shutil, os
from django.shortcuts import render
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
from cv2 import cv2

def button(request):
    return render(request,'index.html')


def external(request):
    
    image = request.FILES['image']
    print(image)
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    fileurl=fs.open(filename)
    templateurl=fs.url(filename)
    print("rawurl",filename)
    print("fullurl",fileurl)
    print("tempurl",templateurl)

    
    image = run([sys.executable,'C://Users//saipr//Desktop/project//project//scr.py',str(fileurl),str(filename)],shell=False,stdout=PIPE)
    
    print(image.stdout)
    
    stri=str(image.stdout, 'utf-8')
    shutil.copy('C://Users//saipr//Desktop//project//project//media//temp.png', 'C://Users//saipr//Desktop//project//project//static//media')

    
    return render(request,'index.html',{'raw_url':templateurl,'edit_url':stri})

def take_picture(request):
    
    if request.method == 'POST':
        image = run([sys.executable,'C://Users//saipr//Desktop/project//project//take.py'],shell=False,stdout=PIPE)
        print(image.stdout)
        stri=str(image.stdout, 'utf-8')
        print(stri)

        shutil.copy('C://Users//saipr//Desktop//project//project//media//temp.png', 'C://Users//saipr//Desktop//project//project//static//media')
        
        

    return render(request,'index.html',{'edit_url':stri})