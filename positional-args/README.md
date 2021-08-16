# Introduction
We going to build a container using the python source code here.

This tutorial shows how do we pass data to container image as we start it . Like how we do it with shell script using positional parameters
./script $1 $2

<b>calc.py</b>  will perform multiplication of 2 numbers. By default no input given, it will multiply 10 by 20. 
User may input the numbers, and the script will calc based on that.

You may try it using python<br>
python calc.py <br>
10 * 20 = 200

python calc.py 25 5 <br>
25 * 5 = 125

<b>Dockerfile</b> will build it as container image. Lets try  it

# Try it
Copy this source code to your local system
```
git clone https://gitlab.com/jasonwcc.my/learntopython 
```

Build it as docker container image 
```
podman build -t calc .
```

First we attempt to start the container without passing any number to it
```
podman run -d calc
NOTE: the container started successfully. 

podman logs -l
10 * 20 = 200

podman rm -l

```

Now we pass two numbers to as we start the container
```
podman run -d calc 25 5
NOTE: the container started successfully. 

podman logs -l
25 * 5 = 125
```

Clean up
``` 
podman stop -af
podman rm -af
podman rmi -f calc
```

