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
    file_Handle = open(filePath, "r")
    machine_Name = file_Handle.readline()
    print("initial value of machine_name: ", machine_Name)
    while machine_Name != "" and machine_Name[0] != "[" and machine_Name[-1] != "]":
        machine_Name = file_Handle.readline()
        print("machine_Name is: ", machine_Name)
    #TODO implement the error parsing here.
    machine = machine_Name.replace("[", "").replace("]", "")
    finalized_Path = path.join(path.join(import_config('config.json')['config']['imageDirectory'].replace("\n",""), machine.replace("\n",""), machine.replace("\n","")))

    print("finalized path is: ", finalized_Path)

    files = []
    for(dirpath, dirnames, filename) in walk(finalized_Path):
        print(filename)
        if filename[-4:] not in 'html':
            files.extend(filename)
    return HttpResponse(str(files), content_type="text/json")

