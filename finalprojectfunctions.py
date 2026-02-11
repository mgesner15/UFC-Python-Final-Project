import csv
import os

#Creating a function to read data from a file
def read_data(file_path):
    data = []
    if not os.path.exists(file_path):
        return data
    
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            data.append(row)
    return data

#Creating a function to search fighter summary by name
def get_fighter_summary(fighter_name, data):
    fighter_data = []
    for row in data:
        if fighter_name.lower() in row[4].lower():  
            fighter_data.append(row)

    if not fighter_data:
        return None

#Creating a function to get wins by method of victory
    wins = [row for row in fighter_data if row[3] == "1"]  
    
    unique_methods = []
    for row in wins:
        method = row[9].lower()  
        if method not in unique_methods:
            unique_methods.append(method)

    methods = {method: sum(1 for row in wins if row[9].lower() == method) for method in unique_methods}

#Collecting the data from rows for height, reach, and division
    if len(fighter_data[0]) > 18:
        height = fighter_data[0][18] 
    else:
        height = "N/A"

    if len(fighter_data[0]) > 17:
        reach = fighter_data[0][17]  
    else:
        reach = "N/A"

    if len(fighter_data[0]) > 6:
        division = fighter_data[0][6] 
    else:
        division = "N/A"

    return {
        "total_wins": len(wins),
        "wins_by_method": methods,
        "height": height,
        "reach": reach,
        "division": division
    }

#Creating a function to search for fighters by weight class
def search_fighters_by_weight_class(weight_class, data):
    fighters = []
    for row in data:
        if weight_class.lower() in row[6].lower():
            fighters.append(row[4]) 
    return fighters

#Creating a function to search for fight URLs based on method of victory
def search_fight_urls_by_method(victory_method, data):
    urls = []
    for row in data:
        if victory_method.lower() in row[9].lower(): 
            urls.append(row[1])  
    return urls  
