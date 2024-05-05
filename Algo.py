
import random


def alt_path(stages ,table , start , end ,cities,d) :#O(n)
    path = []
    path.append(start)
    str_path = start
    if get_index(cities,stages[len(stages)-1][0]) > get_index(cities,end) :
        stages.pop()
    # print("stages after pop : " , stages)
    for i in range(len(stages)):
        random_index = random.randint(0, len(stages[i]) - 1)
        random_city = stages[i][random_index]
        str_path += " -> " + random_city
        path.append(random_city)
    path.append(end)
    # print(path)
    cost = calculate_cost(path,table,cities,d)
    str_path += "--->" + end
    return str_path,cost

def calculate_cost(path ,table,cities,d) :#O(n)
    cost =0
    for i in range(len(path)-1):
        j = get_index(cities,path[i])-d 
        k = get_index(cities,path[i+1])-d      
        cost += table[j][k]
    return cost
    

def get_index(cities, city_name):#O(n)
    for i, city in enumerate(cities):
        if city == city_name:
            return i
    return -1
def contain(arr, sub_arr):#O(n)
    for i, subarray in enumerate(arr):
        if subarray == sub_arr:
            return i
    return -1

def print_path(next,toCity,fromCity,d,cities,destination,start_city, last ): # O(n*m)
    path  = ""
    size = toCity
    difference = 0

    while get_index(cities,last) != get_index(cities,start_city) :

        for i in range(size, fromCity,-1) :
            if(i == fromCity) :
                break
            if(cities[i+d] == last) :
                difference = size - i
                path = cities[i+d] + " -> " + path
                last = next[0][toCity - difference]
            # print(get_index(cities,last),get_index(cities,start_city) )

            
    return start_city + " -> " + path +destination
                

            
        
    
        
    

def apply_algorithm(start_combo, end_combo, cities,input_data): # O(n^3)
    numOfCities =0
    fromCity = 0
    toCity = 0
    startingCity=""
    destination =""
    table=[]
    next=[]
    stages = []    
    d=0

    startingCity = start_combo
    destination = end_combo

    fromCity = get_index(cities, startingCity) # O(n)
    toCity = get_index(cities, destination)# O(n)



    d = fromCity
    numOfCities = toCity - fromCity + 1

    table = [[0 for i in range(numOfCities)] for j in range(numOfCities)]
    next = [[0 for i in range(numOfCities)] for j in range(numOfCities)]
    for i in range(numOfCities):  # fill the table with initial values
        for j in range(numOfCities):
            if i == j:
                table[i][j] = 0
            else:
                table[i][j] = float('inf')  # integer max value 
            next[i][j] = "X"

    lines = input_data.split("\n")
    for i in range(numOfCities - 1):
        parts = lines[i + fromCity].split(", ")#split  lines by , : Start, [A,22,70], [B,8,80], [C,12,80]
        stage = [] 
        end_in_sub = False # check if the end point in sub arrays
        city1 = i  # city1 0 --> numOfCities - 1
        for j in range(1, len(parts)):  # Start from index 1
            city_and_costs = parts[j].replace("[", "").replace("]", "").split(",")#split the info :[A,22,70] by ,
            item = city_and_costs[0].strip()
            if len(parts) != 2: #scheck if its the end point
                    stage.append(item)
            if item == destination : #chack if the subarray contain the end point
                end_in_sub = True
                
            city2 = 0
            # Find the index of the city in the array 
            for k, city_name in enumerate(cities[fromCity:], start=fromCity):  # Start the enumeration from fromCity
                if city_name == item:
                    city2 = k
                    break
            city2 = city2 -fromCity
            if city2 >= numOfCities :
                break


            petrol_cost = int(city_and_costs[1])
            hotel_cost = int(city_and_costs[2])

            table[city1][city2] = petrol_cost + hotel_cost
        if len(stage)!= 0 and contain(stages,stage) == -1 and end_in_sub == False:  #if sub array is empty and if the sub array is already existed and if the sub array is contain the end point
                stages.append(stage)
    # print(stages)    
    #O(n^2)
    for i in range(numOfCities):  #O(n)
        for j in range(numOfCities):#O(n)
            if j < i :
                table[i][j] = float('inf') # Set values in the lower triangle of the table to Integer.MAX_VALUE
            if j == i:
                table[i][j] = 0 # Set values when i = j to 0 because the cost is zero
    
    
    # O(n^3)
    for i in range(numOfCities): # O(n) 
        for j in range(numOfCities):# O(n)
            for k in range(numOfCities):# O(n) 
                if table[j][i] == float('inf') or table[i][k] == float('inf'):#skip the calculation 
                    continue
                if table[j][k] > table[j][i] + table[i][k]: #choose the minimun optimal solution
                    table[j][k] = table[j][i] + table[i][k]
                    next[j][k] = cities[i + d]
               
               
                    
   
                          

    for i in range(1, numOfCities):
        if next[0][i] == "X":
            next[0][i] = startingCity
        else:
            break


    for i in range(len(next)):
        if table[0][i] == 0 or table[0][i] == float('inf'):
            next[0][i] = "X"
    fromCity = fromCity -d        
    toCity = toCity - d

    return  fromCity, toCity, startingCity, destination, table, next, d,stages


