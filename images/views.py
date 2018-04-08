from django.shortcuts import render
from django.http import HttpResponse
import os
from os import path, walk
import json



def import_config(file):
    '''
    Simple Configuration parser -- Non static

    :param file: Config.json
    :return: Json Data Array
    '''
    with open(file) as config_file:
        data = json.load(config_file)
    return data

def returnAbsolutePathIndex():
    '''
    Returns the absolute munin path --Linux Dirs only

    :return: plain path string
    '''
    #TODO: windows path string compatibility
    filePath = import_config('config.json')['config']['muninDir']
    file_Handle = open(filePath, "r")
    machine_Name = file_Handle.readline()
    try:
        while machine_Name != "" and machine_Name[0] != "[" and machine_Name[-1] != "]":
            machine_Name = file_Handle.readline()
    except IndexError:
            return HttpResponse("No name was able to be located in the file", content_type="text/json")

    machine = machine_Name.replace("[", "").replace("]", "")
    finalized_Path = path.join(path.join(import_config('config.json')['config']['imageDirectory'].replace("\n",""), machine.replace("\n",""), machine.replace("\n","")))
    return finalized_Path

def index(request):
    '''
    Returns the corresponding image for an HttpRequest -- With or without the file name extension(s)


    :param request: Request Http object --Contains Path String
    :return: Corresponding image of similar namef
    '''
    print("the requested path is: ", request.path)
    pathString = request.path.split('/')
    flag  = pathString[-4:]
    print("Flag is: ", flag)

    if flag != '.png':
        image_data = open(path.join(returnAbsolutePathIndex(), pathString[-1] + '.png'), "rb").read()
    else:
        image_data = open(path.join(returnAbsolutePathIndex(), pathString[-1]), "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")
    #Dynamically builds out the path

def returnImagesList(request):
    filePath = import_config('config.json')['config']['muninDir']
    file_Handle = open(filePath, "r")
    machine_Name = file_Handle.readline()
    while machine_Name != "" and machine_Name[0] != "[" and machine_Name[-1] != "]":
        machine_Name = file_Handle.readline()
    #TODO implement the error parsing here.
    machine = machine_Name.replace("[", "").replace("]", "")
    finalized_Path = path.join(path.join(import_config('config.json')['config']['imageDirectory'].replace("\n",""), machine.replace("\n",""), machine.replace("\n","")))


    files = []
    for(dirpath, dirnames, filenames) in walk(finalized_Path):
        for file in filenames:
            print(file)
            if 'html' not in file:
                files.append(file)
    return HttpResponse(str(files), content_type="text/json")