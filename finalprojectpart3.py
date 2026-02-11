#Student Name: Matt Gesner
#Program Title: Final Project Part 3
#Description: Final submission for final project

import csv
import os

from finalprojectfunctions import read_data, get_fighter_summary, search_fighters_by_weight_class, search_fight_urls_by_method

#Creating a function to return the summary of the fighter for display
def get_fighter_summary_for_display(summary):
    return f"\nFighter Summary:\n-----------------------------------------------------\nTotal Wins: {summary['total_wins']}\n\nWins by Method of Victory:\n" + "\n".join([f"  {method.title()}: {count}" for method, count in summary['wins_by_method'].items()]) + f"\n\nAdditional Details:\n  Height: {summary['height']}\n  Reach: {summary['reach']}\n  Weight Class: {summary['division']}\n-----------------------------------------------------"

#Creating a function to return fighter names for display
def get_fighter_names_for_display(fighters):
    return f"\nFighters in the specified weight class:\n-----------------------------------------------------\n" + "\n".join(fighters) + f"\n-----------------------------------------------------"

#Creating a function to return fight URLs for display
def get_fight_urls_for_display(urls):
    return f"\nFight URLs for the specified method of victory:\n-----------------------------------------------------\n" + "\n".join(urls) + f"\n-----------------------------------------------------"

#Creating a function to save the output to a text file
def save_to_txt(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"\nResults saved to {filename}")

#Main function to run the program
def main():
    print("Welcome to the UFC Stat Finder!\n")
    
#Loading the data from CSV 
    file_path = "masterdataframe.csv"
    data = read_data(file_path)
    
    if not data:
        print("Error: No data loaded. Please check the file path or file contents.")
        return
    
#Creating a list to store filtered results
    filtered_data = []  


#Printing the main program
    while True:
        print("\nPlease choose one of the following search filters:")
        print("1 - Search by Fighter Name and Show Stats")
        print("2 - Search Fighter List by Weight Class")
        print("3 - Search for Fight URLs via Method of Victory")
        print("4 - Exit Program")

#Creating and setting the value for choice
        choice = input("\nEnter your choice (1-4): ").strip()

#Option 1 is searching fighters stats by name
        if choice == "1":
            fighter_name = input("Enter the fighter's name: ").strip()
            results = get_fighter_summary(fighter_name, data)
            if not results:
                print("No results found for the specified fighter.")
            else:
                result_display = get_fighter_summary_for_display(results)
                print(result_display)
#Saving results to text file
                save_to_txt(result_display, f"{fighter_name}_summary.txt")

#Option 2 is searching for list of fighters by weight class
        elif choice == "2":
            weight_class = input("Enter the weight class: ").strip()
            fighters = search_fighters_by_weight_class(weight_class, data)
            if not fighters:
                print("No fighters found in the specified weight class.")
            else:
                result_display = get_fighter_names_for_display(fighters)
                print(result_display)

                save_to_txt(result_display, f"{weight_class}_fighters.txt")

#Option 3 is searching for links based on the method of victory
        elif choice == "3":
            victory_method = input("Enter the method of victory (e.g., KO/TKO, Submission): ").strip()
            urls = search_fight_urls_by_method(victory_method, data)
            if not urls:
                print("No fight URLs found for the specified method of victory.")
            else:
                result_display = get_fight_urls_for_display(urls)
                print(result_display)

                save_to_txt(result_display, f"{victory_method}_fight_urls.txt")

#Option 4 to exit
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

#Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()
