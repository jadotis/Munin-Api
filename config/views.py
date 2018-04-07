from django.shortcuts import render
from django.http import HttpResponse
import os
from os import walk, path
import json


def import_config(file):
    with open(file) as config_file:
        data = json.load(config_file)
    return data


def return_config(request):

    return HttpResponse(str(import_config('config.json')), content_type="text/json")

def modules(request):
    filePath = import_config('config.json')['config']['muninDir']
    #mockFilePath = "C:\\Users\\jadotis\\Documents\\Vuze Downloads"
    #Must build the filepath from the real config file.
    file_Handle = open(filePath, "r")
    machine_Name = ""
    while machine_Name[0] != "[":
        machine_Name = file_Handle.readLine()
    #TODO implement the error parsing here.
    machine = machine_Name.replace("[", "").replace("]", "")
    print(machine)
    finalized_Path = path.join(filePath, machine, machine)
    print("finalized path is: ", finalized_Path)







    files = []
    for(dirpath, dirnames, filenames) in walk(finalized_Path):
        files.extend(filenames)
    return HttpResponse(str(files), content_type="text/json")

