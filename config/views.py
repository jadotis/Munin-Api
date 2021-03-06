from django.shortcuts import render
from django.http import HttpResponse
import os
from os import walk, path
import json


def import_config(file):
    '''
    Returns the configuration file as a Json Object
    :param file: File Name (String)
    :return: Json
    '''
    with open(file) as config_file:
        data = json.load(config_file)
    return data


def return_config(request):
    '''
    Returns an HttpResponse Object that contains the configuration as noted
    :param request: HttpRequest Object
    :return: HttpResponse
    '''

    return HttpResponse(str(import_config('config.json')), content_type="text/json")

def modules(request):
    '''
    Returns a Set of files that are actively being used by the configured Munin Node
    :param request: HttpRequest Object
    :return: Array of Modules
    '''
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

    files = []
    for(dirpath, dirnames, filenames) in walk(finalized_Path):
        for file in filenames:
            if 'html' not in file:
                files.append(file.replace('.png', ''))

    return HttpResponse(str(set(files)), content_type="text/json")

