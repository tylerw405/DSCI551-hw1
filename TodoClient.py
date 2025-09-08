import requests
import json

############ add codes here, if needed

class TodoClient:
  # this method simply remembers the given dburl
  def __init__(self, dburl):
    # fill in code
 
  # Remove all existing tasks from the todo list.
  # If the removal was successful, return "Success!".
  # otherwise, return the error message from the Firebase server.
  # The error message should be in a Python dictionary, e.g., 
  #        {'error': '404 Not Found'}
  # clear() method should be called first before any tasks are added to the 
  #    todo list.
  # You should assume that no other methods will be called on the todo list,
  # if the clear method failed.
  def clear(self):
    # fill in code


  # if the task exists in the todo list,, 
  #    return an error message in this format:
  #       Error in add_task: task "xyz" already exists!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    add the task to the todo list stored in Firebase, and
  #    return "Success!"
  def add_task(self, task):
    # fill in code

  # if the task does not exist in the list, 
  #    return an error message in this format:
  #        Error in delete_task: task "xyz" does not exist!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    remove the task from the list, and 
  #    return "Success!"
  def delete_task(self, task):
    # fill in code


  # if the task does not exist in the list, 
  #    return an error message in this format:
  #        Error in mark_completed: task "xyz" does not exist!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    change the status of the task to "completed", and 
  #    return "Success!"
  def mark_completed(self, task):
    # fill in code
 

  # return a list of tasks in the given status, 
  # and empty list if no such tasks
  def get_task_by_status(self, status):  # status is either completed or pending
    # fill in code
    
  # return a dictionary of task:status pairs, 
  # and None if no tasks in the todo list.
  def get_all_tasks(self):
    # fill in code

  ############ add codes here if needed