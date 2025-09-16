import requests
import json


class TodoClient:
  # this method simply remembers the given dburl
  def __init__(self, dburl):
    self.dburl = dburl
 
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
    res = requests.delete(self.dburl)

    try:
      data = res.json()
    except ValueError:
      data = None

    if res.json() == None:
      msg = "Success!"
    else:
      msg = res.json()
    return msg


  # if the task exists in the todo list,, 
  #    return an error message in this format:
  #       Error in add_task: task "xyz" already exists!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    add the task to the todo list stored in Firebase, and
  #    return "Success!"
  def add_task(self, task):
    db = requests.get(self.dburl).json() or {}

    if task in db:
      return f'Error in add_task: task "{task}" already exists!'
    else:
      res = requests.patch(self.dburl, json={task: "pending"})
      res.json()
      return f'Success!'


  # if the task does not exist in the list, 
  #    return an error message in this format:
  #        Error in delete_task: task "xyz" does not exist!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    remove the task from the list, and 
  #    return "Success!"
  def delete_task(self, task):
    db = requests.get(self.dburl).json() or {}

    if task not in db:
      return f'Error in delete_task: task "{task}" does not exist!'
    else:
      delete_url = f"{self.dburl[:-5]}/{task}.json"
      res = requests.delete(delete_url)
      res.json()
      return 'Success!'


  # if the task does not exist in the list, 
  #    return an error message in this format:
  #        Error in mark_completed: task "xyz" does not exist!
  #         where xyz should be replaced with the actual task name
  # else, 
  #    change the status of the task to "completed", and 
  #    return "Success!"
  def mark_completed(self, task):
    db = requests.get(self.dburl).json() or {}

    if task not in db:
      return f'Error in mark_completed: task "{task}" does not exist!'
    else:
      url = f"{self.dburl[:-5]}/{task}.json"
      res = requests.put(url, json="completed")
      res.json()
      return f'Success!'
 

  # return a list of tasks in the given status, 
  # and empty list if no such tasks
  def get_task_by_status(self, status):  # status is either completed or pending
    db = requests.get(self.dburl).json() or {}
    task_list = [key for key,value in db.items() if value == status]
    return task_list
    
  # return a dictionary of task:status pairs, 
  # and None if no tasks in the todo list.
  def get_all_tasks(self):
    return requests.get(self.dburl).json()

  ############ add codes here if needed

  def response_check(self, res):
    try:
            data = res.json()
    except ValueError:
        data = None

    if res.status_code == 200:
        return data
    else:
        return {"error": f"{res.status_code} {res.reason}"}
