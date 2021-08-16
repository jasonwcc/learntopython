#!/bin/pythopen3
import sys

# Assuming content of fridge
myFridge= {'brocolli':5, 'cheese':10, 'pepper':10, 'egg':20, 'milk':4 }

#I ngredient to make Cheedar Omelete
c_omelet_ing = { 'milk':1 , 'egg':2 , 'cheese':2 }

# Ingredient to make Vege Omelete
v_omelet_ing = { 'milk':1 , 'egg':2 , 'brocolli':1 , 'pepper':1 }

# Function to make omelet
def get_omelet_ingredients(omeletname,noError):
        #common ingredients to get regardless of omelet type
        ingredients={'milk':1, 'egg':2}

        # Then depends on omelete type, we pick few more ingredients
        if (omeletname == 'cheedar'):
                ingredients['cheese']=20
        elif (omeletname == 'vege'):
                ingredients['brocolli']=1
                ingredients['pepper']=2
        else:
                noError[0]=1
                print('Sorry we do not make ',omeletname,' omelet')

        print()
        print("Currently executing get_omelet_ingredients",)
        print("You requested",omeletname,"omelet type")
        print()
        print("Dependent ingredients are:",ingredients)
        return ingredients

def remove_from_fridge(fridge,ingredients,noError):
    # Once ingredient is determined, then we need to find and remove those ingredients from fridge
    # But if specific ingredients not enough or missing, then report and break
    print()
    print("Following items is available in the fridge")

    for item in ingredients.keys():
      if( item in fridge and ingredients[item]<fridge[item] ):
        fridge[item] = fridge[item] - ingredients[item]
        print("-",item,":",fridge[item])
      else:
        print("Following items is not enough or not available")
        print("-",item,":",ingredients[item])
        noError[1]=1
        break
    return fridge

def make_omelet_q3(fridge, omeletname):
        noError=[0,0]  
        # first 0 for ingredient status, second for fridge status

        ingredients = get_omelet_ingredients(omeletname,noError)

        fridge = remove_from_fridge(fridge,ingredients,noError)

        if(noError[0] == 0 and noError[1] == 0):
           print("")
           print("Hooray we are able to make your %s omelete" % omeletname)
           print("Pls enjoy your %s omelete while it is hot" % omeletname)
        else:
           print("") 
           print("Sorry, we can't prepare your omelet")

print('Currently in the fridge:')
print(myFridge)

# Get input which type of omelet to make
print('Omelete of the day:')
print ('1 - Cheedar omelete')
print ('2 - Vegetable omelete')
choice = input("Enter choice (1/2): ")

if choice == "1":
   omeletename="cheedar"
elif choice == "2":
   omeletename="vege"
else:
   sys.exit("Invalid choice")

make_omelet_q3(myFridge, omeletename)



