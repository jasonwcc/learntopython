# This is my sample python code
# 1. calc2.py : will perform add, substract, divide and multiplication by getting 2 numbers from user
# 2. scalc.py : will perform simple seismic calculation
# 3. hpcalc.py : will perform massive hpc calculation

# Run it from any kubernetes platform
# Example from Openshift v4.7
oc new-app --name calc python~https://github.com/jasonwcc/python.git

