# Paasmer-Python-library-V-1
The official release of the Generic Python library (Beta version) to work with the **Paasmer IoT** Platform

This library works with both Python 2 and 3.

### Prerequisites:
* Install the Paho-Mqtt package. If you have pip installed, you can do this by writing `pip install paho-mqtt` in your command line interface.

## Paasmer Python Library
**Paasmer Python Library** is set of functions that can be used to connect, subscribe and publish to the Paasmer gateway easily and more efficiently in a single function call. It can also support Edge Analytics on any feed while publishing. It has separate CallBack for each feed and thus making the connection simple.

## Getting started with Paasmer Python Library
Here is a very simple example that connects to the Paasmer Gateway, subscribes and Publishes to Paasmer platform enabling the user to access and read the feeds.

### Importing Paasmer Library
Open `paasmer-python-library` directory and start building the script.

```
from Paasmer import *
```
### Connecting to the Paasmer Edge docker device
```
test = Paasmer()
test.host = "localhost"   #IP address of the Paasmer Edge docker device.
test.connect()
```


### Subscribing 
```
#Callback functions for subscribed feeds
def feed1_CB(name):
    print("This is in feed1")
    print(name)

#subscribing to the feeds with callback functions
test.subscribe("feed1",feed1_CB)

```
The Subscribe functions need the following as parameters,
```
subscribe(feedname,callback function name)
```
- Feedname
- Call back Function name 

### Loop start
```
test.loop_start()
```

### Publishing the feed details 
The Publish functions need the following as parameters,
```
    test.publish("feed2",feedValue = 9,feedType = "sensor")

```
- Feedname
- Feedvalue
- Feedtype (The Feedtype is to be sensor or actuator)
```

You can use the Analytics in the following way,
- Filter - provide the analytics condition like "function(x) x < 5.0"
- Aggregate - provide the number of values you want to do aggregate
- FeedMonitoring
- Average - provide the number of values you want to do average

To syntax for Publishing Analytics are,
```
#publishing the feed details with filter analytics 
    test.publish("feed4",feedValue = 5,analytics = "filter",analyticsCondition="function(x) x > 3.0")

#publishing the feed details with aggregate analytics
    test.publish("feed6",feedValue = 22,analytics = "aggregate",analyticsCondition = "10")

#publishing the feed details with average analytics
    test.publish("feed8",feedValue = 28,analytics = "average",analyticsCondition = "10")

#publishing the feed details with feedMonitoring
    test.publish("feed7",feedValue = 22,analytics = "feedMonitoring")
```
** Note - A sample code is provided in `paasmer-python-library` directory **


## Support
The support forum is hosted on the GitHub, issues can be identified by users and the Team from Paasmer would be taking up requests and resolving them. You could also send a mail to support@paasmer.co with the issue details for a quick resolution.

## Note

* The Paasmer Library is a simple library that allows you to connects to the Paasmer Gateway, subscribes and Publishes to Paasmer platform. Future enhancements may be arriving shortly.


