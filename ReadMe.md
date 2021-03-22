#Components
1.  Redis
2.  Tensorflow
3.  Numpy


##Scripts
1. **npBusUtil:** this script will handle sending a numpy array and reading it from redis server
2. **tfBusUtil:** this script will handle sending tensorflow object to redis
3. **pdBusUtils:** this script will send pandas dataframe and reading from redis.
4. **BusUtil:** this is the base class that all BusUtill will drive from

##BusUtil
This is the base class all bus utils will drive from. It contains

- ***Properties***
1.  host
2.  port
3.  access name
4.  access password
5.  address

-   ***Methods***
1.  ```Send(msg,timestamp)```
2.  ```Read()```
3.  ```Run()``` Run Send and Read in an infinite loop on a separate thread

-   ***Abstract Method***
1.  ```toBase64String(data)```
2.  ```data = fromBase64String()```

-   ***Emitter***
1.  ```NewMessageReceived(msg,timestamp)``` # will be triggered and handled by a custom method or a class when a message is found

##The Run Cycle
