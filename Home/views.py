from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras_preprocessing import image
import json
from tensorflow import Graph
import pandas as pd
import numpy as np
import tensorflow as tf
from django.template import Context, Template


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def services(request):
    global predict
    predict= 0
    global labelInfo
    labelInfo= {}
    img_height, img_width = 240, 240
    with open(r'C:\Users\pranj\Desktop\django\brain_tumor\class_dictionary.json') as f:
        labelInfo = f.read()
        labelInfo = json.loads(labelInfo)

    model_graph = Graph()
    with model_graph.as_default():
        tf_session = tf.compat.v1.Session()
        with tf_session.as_default():
            model = load_model(r'C:\Users\pranj\Desktop\django\brain_tumor\model.h5')

    if request.method == 'POST':
        fileObj = request.FILES['filePath']
        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name, fileObj)
        filePathName=fs.url(filePathName)
        testimage='.'+filePathName
        img = image.load_img(testimage, target_size=(img_height, img_width))
        x = image.img_to_array(img)
        x=x/253
        x=x.reshape(-1,img_height, img_width,1)
        with model_graph.as_default():
            with tf_session.as_default():
                predict= model.predict(x).flatten()
                
    result= predict           
    result = np.argmax(predict)
    if result<0.5:
        result= labelInfo[str(0)]
    else:
        result= labelInfo[str(1)]
    context= {'result':result}
        # import numpy as np
        # predictedLabel=labelInfo[str(np.argmax(predict[0]))]
 
    
    return render(request,'services.html', context) 


    # return render(request,'services.html' )
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        contact = Contact(name= name, age= age)
        contact.save()
        messages.success(request, 'Successfully Submitted!')
    
    return render(request,'contact.html' )
    # return HttpResponse("This is contact page")



    """if request.method=='POST':    
        fileobj = request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName= fs.save(fileobj.name, fileobj)"""