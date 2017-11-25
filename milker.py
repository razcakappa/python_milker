import urllib.request, json, sys, arrow
from pprint import pprint

# get data from URL
try:
    data = urllib.request.urlopen("https://api.rememberthemilk.com/services/rest/?method=rtm.tasks.getList&api_key=ea60fce7e89b013cb2e74f1977d4b8b5&format=json&list_id=42819726&filter=status:incomplete&auth_token=4116a69476f4ce0ff32a22caee4481147ed45c12&api_sig=3de4841e5418da923de8e82d8dced243").read().decode('utf-8')
except NameError:
    print ("Well, there's an error reaching URL")
    sys.exit()


#pprint(json.dumps(data))

# decoding json
if data is not None:
    output = json.loads(data)

# tasklist array, a list of tasks
if output is not None:
    taskseries = output['rsp']['tasks']['list'][0]['taskseries']

event = {}
date = {}
events = []
# task is a single task, can access task properties
if taskseries is not None:
	for task in taskseries:
		date['date'] = arrow.now().format('YYYY-MM-DD')
		event['summary']=task['name']
		event['end']=date
		event['start']=date
		events.append(event)

print (json.dumps(events));
