# https://pymotw.com/2/pprint/
from pprint import pprint

import anvil.server
from anvil.tables import app_tables


class Todo:

    def __init__(self):
        # anvil.server.connect("[uplink-key goes here]", url="ws://your-runtime-server:3030/_/uplink")
        key = "abcd"
        url = "ws://mk8.westus2.cloudapp.azure.com:3030/_/uplink"
        print("key", key)
        print("url", url)
        anvil.server.connect(key, url=url)

    def get_tasks(self):
        return anvil.server.call('get_tasks')

    def add_task(self, task):
        return anvil.server.call('add_task', task)

    def delete_task(self, task):
        return anvil.server.call('delete_task', task)


todo = Todo()

# todo.add_task({"name": "foo", "completed": True})
todo.add_task("foo")

task = app_tables.tasks.get(name="foo")
if task:
    print(task.get_id(), task['name'], task['complete'])
    todo.delete_task(task)

for task in app_tables.tasks.search():
    print(task.get_id(), task['name'], task['complete'])
    # todo.delete_task(task)


'''
https://anvil.works/docs/data-tables/data-tables-in-code#searching-querying-a-table

import anvil.tables.query as q

people_over_50 = app_tables.people.search(age=q.greater_than(50))

from datetime import date
late_projects = app_tables.projects.search(
  Complete=False,
  Due_Date=q.less_than(date.today())
)
'''