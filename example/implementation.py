#!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# Author: Carlos Alessandro Sena de Freitas  <veneinzuela@gmail.com>
# Created: Fri Jan 18 02:34:42 2013
# Last Update: Fri Jan 18 02:34:42 2013
# File: base
# Notes: 
# Class used to submit a project on Mobile Works, in wich the workers label a set of tweets as: 
#   -Question
#   -Not a Question
#   -Invalid Tweet

import abc
from base import MWBase
import csv
import mobileworks as mw  
import cjson


class QuestionAvaliation(MWBase):
    

    def renderSource(self, source):
        return """  <div style=\"background: none repeat scroll 0% 0% rgb(255, 255, 255); color: rgb(51, 51, 51); font-size: 22px; line-height: 28px; font-family: Georgia,&quot;Times New Roman&quot;,serif; word-wrap: break-word; padding: 25px 50px; border-radius: 5px 5px 5px 5px; width: 400px; margin-left: 30px; border: 1px solid rgb(221, 221, 221);\">
                <span>"""+source+"""</span>
            </div>"""


    def loadTests(self, filename):

        #load tests from a csv file
        tests = []
        fin = open(self.baseDir+filename, 'r') 
        reader = csv.reader(fin,delimiter=',')
        for [test_id, tweet, l1,l2,l3,l4] in reader:
            t = (test_id.strip(), tweet.strip(), l1.strip())
            tests.append(t)
        fin.close() 


        for test_id, tweet, label in tests:  
            # create the test task
            test =  mw.Task( resource=self.renderSource(tweet))
            test.add_field("Valid Question", "m", choices="Question,Not a Question,Invalid Tweet", answers=[label]) 
            # add the test to the project 
            self.project.add_test_task(test) 



    def loadTasks(self, filename):

        #load tasks from a json file
        questions = []
        fin = open(self.baseDir+filename, 'r')
        for line in fin:
            line = cjson.decode(line)
            question = line['question']
            t = (question['tweet_id'], question['tweet_text'])
            questions.append(t)
        fin.close()

        for tweet_id, text in questions:
            task =  mw.Task(resource=self.renderSource(text)) 
            self.project.add_task(task) 

        self.tasksLoaded = True




