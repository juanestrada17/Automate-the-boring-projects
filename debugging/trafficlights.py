market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'
assert 'red' in stoplight.values(), 'Neither light is red!' + str(spotlight)
#IT makes sure that one of the lights is red so that there won't be 
# an accident 
switchLights(market_2nd)

#To disable assertions you can pass the -0 option
