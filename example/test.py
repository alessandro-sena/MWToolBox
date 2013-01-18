#!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# Author: Carlos Alessandro Sena de Freitas  <veneinzuela@gmail.com>
# Created: Fri Jan 18 02:34:42 2013
# Last Update: Fri Jan 18 02:34:42 2013
# File: base
# Notes: Example file that loads the files in the files directory and submit the project to MobileWorks
#        Needs to set the username and password


if __name__ == '__main__':
    from implementation import *

    tweetProject = QuestionAvaliation()
    tweetProject.loadConfig('files')

    #use a properly login here
    tweetProject.setUsername('username')
    tweetProject.setPassword('password')

    #use production mode when necessary 
    tweetProject.sandbox()

    tweetProject.loadTasks('questions.json')
    tweetProject.loadTests('tests.csv')
    tweetProject.postProject()
