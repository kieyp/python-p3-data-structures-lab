spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 39,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list=[ food['name'] for food in spicy_foods]
    return list
result=get_names(spicy_foods)



def get_spiciest_foods(spicy_foods):
    data=[n for n in spicy_foods if n["heat_level"] > 5]
    return data
result=get_spiciest_foods(spicy_foods)
print(result)

def print_spicy_foods(spicy_foods):
    for food_data in spicy_foods:
        print (food_data['name'],'('+food_data['cuisine']+')', '|', 'Heat Level:',food_data['heat_level'] *'🌶')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods,"American"))



def print_spiciest_foods(spicy_foods):
    for food_data in spicy_foods:
        if food_data['heat_level'] > 5:
            print (food_data['name'],'('+food_data['cuisine']+')', '|', 'Heat Level:',food_data['heat_level'] *'🌶')
            
print_spiciest_foods(spicy_foods)
    
    

def get_average_heat_level(spicy_foods):
    #avg= total/no of items
    #total /len(items)
    #sum
    total_hlevel=sum([n['heat_level'] for n in spicy_foods]) 
    avg=total_hlevel/len(spicy_foods)
    return avg
result=get_average_heat_level(spicy_foods)
print(result)

def create_spicy_food(spicy_foods, spicy_food):
    
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods,"spicy_food"))


