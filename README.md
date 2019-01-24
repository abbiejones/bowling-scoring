#Let's Go Bowling

Let's Go Bowling is a console application written in Python that allows a player to keep track of their bowling score at each frame as they play.

##Installation

Please clone the git repo to begin playing:

```
git@github.com:abbiejones/lets-go-bowling.git
```

#Usage

Step 1: Navigate into lets-go-bowling/src

Step 2: Start server
```
python server.py
```

To disconnect from server, type into STDIN:
```
/disconnect
```

Step 3: In a new terminal, start client

```
python client.py
```

Try allowing multiple clients to keep score at once 
(i.e. you can repeat step 3 multiple times)

#Tests

To run unit tests:

```
python testparseuserinput.py
python testupdatescore.py

```

