#!/bin/python3
# Answer to Q3
# Assuming content of fridge
myFridge= {'brocolli':5, 'cheese':10, 'pepper':10, 'egg':20, 'milk':4 }

#I ngredient to make Cheese Omelete
c_omelet_ing = { 'milk':1 , 'egg':2 , 'cheese':2 }

# Ingredient to make Vege Omelete
v_omelet_ing = { 'milk':1 , 'egg':2 , 'brocolli':1 , 'pepper':1 }

# Function to make omelet
def get_omelet_ingredients(omeletname,noError):
        #common ingredients to get regardless of omelet type
        ingredients={'milk':1, 'egg':2}

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
           print("Omelet %s is ready" % omeletname)
        else:
           print("") 
           print("Sorry, we can't prepare your omelet")

print('Currently in the fridge:')
print(myFridge)

make_omelet_q3(myFridge, 'cheedar')



