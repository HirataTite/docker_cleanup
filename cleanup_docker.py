#!/usr/bin/python

import docker
import json
import os

client = docker.from_env()

# Clean Exited/Unused Containers
def cleanContainer():
    print "##### Containers #####"
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
'''
def stopContainer():
    for container in client.containers.list(all):
        data = container.attrs
        status_running = data['State']['Running']
        status_pause = data['State']['Paused']
        if (status_running == 'true'):
            if (status_pause == 'true'):
                print "Stopping Container"
                container.stop()
'''
print ""

# Clean Untagged Images
def cleanImages():
    print "##### Images #####"
    for image in client.images.list():
        data = image.attrs
        tag = data['RepoTags']
        print image
        print tag
        if (tag == None):
           #stopContainer()
           print "Image is Untagged"
           # client.images.remove(image)
           os.system('docker rmi -f %s' % image.id)
        if(tag == [u'<none>:<none>']):
           #stopContainer()
           print "Image is Untagged"
           # client.images.remove(image)
           os.system('docker rmi -f %s' % image.id)

cleanImages()
