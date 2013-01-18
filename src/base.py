#!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# Author: Carlos Alessandro Sena de Freitas  <veneinzuela@gmail.com>
# Created: Fri Jan 18 02:34:42 2013
# Last Update: Fri Jan 18 02:34:42 2013
# File: base
# Notes: Base classe to post a project into mobile works


# import the MobileWorks library 
import mobileworks as mw  
import cjson
import abc

class MWBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.username = None
        self.password = None
        self.tasksLoaded = False

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def loadConfig(self, baseDir, configFile="config.json", instructionsFile="instructions"):
        
        #default mode is sandbox
        self.sandbox()

        if (baseDir[-1] != '/'):
            baseDir+='/'
        self.baseDir = baseDir
        

        with open (baseDir+instructionsFile, "r") as myfile:
            instructions=myfile.read().replace('\n', ' ')

        self.project = mw.Project(instructions=instructions)  

        with open (baseDir+configFile, "r") as myfile:
            config=myfile.read().replace('\n', '')

        json = cjson.decode(config)


        #Set the fields of the project
        for field in json['fields']:
            l = []
            
            #Forcing the name, type order
            l.append("\"%s\"" % field['name'])
            l.append("\"%s\"" % field['type'])

            #Any other field later
            for item in field.iteritems():
                if item[0] not in ["name", "type"]:
                    l.append("%s=\"%s\"" % item)
                    

            args = ','.join(l)
            eval("self.project.add_field(%s)" % args)

        #Set the params of the project
        for param in json['params'].iteritems():
            eval("self.project.set_params(%s=%s)" % param)


    def postProject(self):
        if not self.tasksLoaded:
            print "Need to load some tasks"
            return



        if (self.username and self.password):

            #set the mode 
            if (self._production):
                mw.production()
            else:
                mw.sandbox()

            #set the user information
            mw.username = self.username
            mw.password = self.password

            self.project.post()
        else:
            print "Need to inform a username and password"

    def production(self):
        self._production = True

    def sandbox(self):
        self._production = False



    #Abstract methods


    @abc.abstractmethod
    def loadTests(self, filename):
        """Load the tests from a testfile."""
        return

    @abc.abstractmethod
    def loadTasks(self, filename):
        """Load the tasks from a testfile. Needs to set self.tasksLoaded to True"""
    
        return
    
    @abc.abstractmethod
    def renderSource(self, source):
        """Render the source for a task"""
        return

    




