from anvil import *
import anvil.server


class Hello():

  def __init__(self):

    anvil.server.connect("http://mk8.westus2.cloudapp.azure.com")  
    

    print(self.get_tasks())

  
  def get_tasks(self):
    tasks = anvil.server.call('get_tasks')
    self.tasks_panel.items = tasks


  def add_task(self, task):
      anvil.server.call('add_task', task)
      self.get_tasks()

  def delete_task(self, task):
      anvil.server.call('delete_task', task)
      self.get_tasks()

h = Hello()
