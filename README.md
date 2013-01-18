MWToolBox
=========

Mobile Works ToolBox

Mobile Works API Documentation: http://www.mobileworks.com/developers/

Dependencies:

    -Mobile Works API

    -cjson

    -abc

How to use:

    ->Create a subclass of the class MWBase and implement the following methods:

        loadTests: Function to load the tests file into the mobileworks api

        loadTask: Function to load the task file into the mobileworks api, this method needs to set self.tasksLoaded to True

        renderResource: Function to render properly the resource of each task

    ->All the files needs to be in the same files directory
   

Necessary Files:

    ->Instructions: Instructions in text format or in HTML format

    ->Config: File this file must contain the fields and the params of the project

    ->TasksFile: File that contains the tasks of the project

    ->TestsFile (Optional): File that contains the tests of the project
        



