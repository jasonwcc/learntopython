# Introduction
This tutorial shows how do we pass data to container image as we ran it . Like how we do it with shell script using positional parameters
./script $1 $2

<b>calc.py</b>  will perform multiplication of 2 numbers. By default no input given, it will multiply 10 by 20. 
User may input the numbers, and the script will calc based on that.

You may try it using python<br>
python calc.py <br>
10 * 20 = 200

python calc.py 25 5 <br>
25 * 5 = 125

<b>Dockerfile</b> will build it as container image. Lets try  it

# The steps 
<b> First we build it as docker container image </b><br>
podman build -t calc .

<b> Then we can run it but first we attempt without passing any number to it</b><br>
podman run -d calc

podman logs -l
10 * 20 = 200

podman rm -l

<b> Now we pass 2 numbers to it </b><br>
podman run -d calc 25 5

podman logs -l
25 * 5 = 125

