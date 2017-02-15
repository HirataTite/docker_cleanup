#!/usr/bin/python

import docker
import json
import os

# Clean Exited/Unused Containers


def cleanContainer():
    print "##### Containers #####"
    client = docker.from_env()
    for container in client.containers.list(all):
        data = container.attrs
        print container.short_id
        # print container.attrs
        status = data['State']['Status']
        print status
        if (status == 'exited'):
            print "Removing Exited Container"
            container.stop()
            container.remove()
        # captura e atribui a data de inicio de fim do container
        initdate_container = data['State']['StartedAt']
        enddate_container = data['State']['FinishedAt']
        #print initdate_container
        #print enddate_container

cleanContainer()


def stopContainer():
    client = docker.from_env()
    for container in client.containers.list(all):
        data = container.attrs
        status_running = data['State']['Running']
        status_pause = data['State']['Paused']
        if (status_running == 'true'):
            if (status_pause == true):
                print "Stopping Container"
                container.stop()

print ""

# Clean Untagged Images


def cleanImages():
    print "##### Images #####"
    client = docker.from_env()
    for image in client.images.list():
        data = image.attrs
        image_name = image
        tag = data['RepoTags']
        print image_name
        print tag
        if (tag == None):
            stopContainer()
            print "Image is Untagged"
            # client.images.remove(image)
            os.system('docker rmi %s' % image.id)
        #else:
        #    print "Image Ok"


cleanImages()
