from Paasmer import *
import time

#Callback functions for subscribed feeds
def feed1_CB(name):
	print("This is in feed1")
	print(name)
def feed2_CB(name):
	print("This is in feed2")
	print(name)
def feed3_CB(name):
	print("This is in feed3")
	print(name)

###connecting to the Paasmer Edge docker device
test = Paasmer()
test.host = "localhost"   #IP address of the Paasmer Edge docker device.
test.connect()

#subscribing to the feeds with callback functions
test.subscribe("feed1",feed1_CB)
test.subscribe("feed2",feed2_CB)
test.subscribe("feed3",feed3_CB)

#loop start
test.loop_start()

while True:

	#publishing the feed details to Paasmer Edge docker device
	'''
	you can use the following analytics
	1.filter
	2.aggregate
	3.feedMonitoring
	4.average

	for filter, provide the analytics condition like "function(x) x < 5.0"

	for aggrgate, provide the number of values you want to do aggregate

	for average, provide the number of values you want to do average
	'''

	#publishing the feed details with filter analytics 
	test.publish("feed4",feedValue = 5,analytics = "filter",analyticsCondition="function(x) x > 3.0")
	time.sleep(2)

	
	#publishing the feed details without any analytics 
	test.publish("feed5",feedValue = 9,feedType = "sensor")
	time.sleep(2)

	
	#publishing the feed details with aggregate analytics
	test.publish("feed6",feedValue = 22,analytics = "aggregate",analyticsCondition = "10")
	time.sleep(2)
	
	
	#publishing the feed details with feedMonitoring
        test.publish("feed7",feedValue = 22,analytics = "feedMonitoring")
        time.sleep(2)

	#publishing the feed details with average analytics
        test.publish("feed8",feedValue = 28,analytics = "average",analyticsCondition = "10")
        time.sleep(2)

