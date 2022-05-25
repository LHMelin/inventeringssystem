'''imports'''
import os
from tkinter import ALL
from unicodedata import category

'''classes'''
class Item:

    '''konstruktorn'''

    def __init__(self, category, name, colour, artnumb, amount):
        self.category = category
        self.name = name
        self.colour = colour
        self.artnumb = artnumb
        self.amount = amount

    '''strängmetoden'''

    def __str__(self):
        return f'Category: {self.category}\nName: {self.name}\nColour: {self.colour}\nArtnumb: {self.artnumb}\nAmount: {self.amount}'

    def get_all_attributes(self):
        return self.category, self.name, self.colour, self.artnumb, self.amount

    



'''functions'''


def clear_console():
    '''tömmer konsolen'''
    os.system('cls')


def save_item(items : list()):

    saved_items = []
    for item in items:
        category, name, colour, artnumb, amount = item.get_all_attributes()
        save_string = f"{category}/{name}/{colour}/{artnumb}/{amount}\n"
        saved_items.append(save_string)
        '''alla attribut i klassen sparas i en lista på en och samma värdeplats'''

    with open("item_file.txt", "w", encoding="utf8") as f:
        for item in saved_items:
            f.write(item)
        print(f"Your items have been successfully saved.")
        '''om ingen fil finns så skapas en fil och listan konverteras till en txt fil där varje plats i listan blir en rad i txt filen'''

def search_item():

    search = input("Search for a items by category, name, colour, artnumb or amount:  \n").lower()

    file1 = open("item_file.txt", "r")
    lines = file1.readlines()

    count = 0
    '''Används för att räkna ut hur många gånger if påståendet var sant'''

    for line in lines:
        if (search in line):
            '''om  ditt sökord matchar något ord eller någon siffra i txt filen'''
            line_list1 = line.split("/")
            line_list2 = [s.replace("\n", "") for s in line_list1] 
            '''txt filen öppnas och konverteras till en lista där \n tas bort och varje attribut får en värdeplats''' 

            category = line_list2[0]
            name = line_list2[1]
            colour = line_list2[2]
            artnumb = line_list2[3]
            amount = line_list2[4]
            '''attributen får varsin variabel'''

            return_item = Item(category, name, colour, artnumb, amount)
            print(f"{return_item}\n")
            '''attributen skickas till konstruktorn där stringmetoden används för att skriva ut varans attribut'''

            count += 1
        else:
            pass

    if count>=1:
        print(f"These {count} items were found.")
    else:
        print("No items were found.")

def remove_item():

    while True:

        delete_artnumb = input("Enter the artnumb of the item you want to remove:  ")

        file1 = open("item_file.txt", "r")
        lines = file1.readlines()
        found = False
        line_count = 0

        for line in lines:
            line_count +=1 
            line_list1 = line.split("/")
            line_list2 = [s.replace("\n", "") for s in line_list1] 
            '''samma metod som i skapa vara funktionen'''

            if (delete_artnumb) == line_list2[3]:
                '''om artikel nummeret finns på rätt plats i den skapade listan så finns produkten'''
                found = True
                file = open("item_file.txt", "r")
                lines1 = file.readlines()
                '''hela txt filen omvandlas till en lista där varje rad i txt filen blir en värdeplats'''
                file.close()

                del lines1[line_count-1]
                '''önskade raden/värdeplatsen tas bort'''

                new_file = open("item_file.txt", "w+")

                for line1 in lines1:
                    new_file.write(line1)
                '''den nya listan läggs in istället i samma txt fil'''

                new_file.close()

                print("Item has been succesfully removed.")
                
            else:
                pass

        if found == True:
            break
        
        else:
            print("That art numb does not exist.\n")
        




def load_item():

    with open("item_file.txt", "r", encoding="utf8") as f:
        items = []
        for line in f.readlines():
            attributes = line.split("/")
            this_item = Item(attributes[0], 
                             attributes[1], 
                             attributes[2], 
                             attributes[3], 
                             int(attributes[4]))
            items.append(this_item)
            '''lista med varje attribut på en värdeplats skapas för att kunna skickas till konstruktorn'''
        return items



def add_item():
        category = input("In what category do you want to add an item?\n").lower()
        name = input("What item do you want to add to the inventory?\n").lower()
        colour = input("What colour is the item?\n").lower()

        while True:
            artnumb = input("What article number does the item have?\n")

            file1 = open("item_file.txt", "r")
            lines = file1.readlines()
            found = False

            for line in lines:
                line_list1 = line.split("/")
                line_list2 = [s.replace("\n", "") for s in line_list1]

                if artnumb == line_list2[3]:
                    found = True
                    break
                else:
                    pass
                '''txt filen söks igen rad efter rad och görs om till listor per rad.
                I listorna så gämförs artnumb variabeln med alla existerande artnumb attribut.
                Om den nya variabeln är samma som något artnumb i listorna så börjar while loopen om'''
        
            if found == True:
                print("That artnumb does already exist. Please try again.\n")
            
            else:
                break

        
        while True:
            amount_str = input(f"How many {name}'s do you want to add?\n")

            numb_test = amount_str.isnumeric()

            '''numb_test blir true om input på amount_str är en siffra'''

            if numb_test == True:
                amount = int(amount_str)
                break
            
            elif numb_test == False:
                print("The amount has to be a number.\n")
                '''om en siffra inte skrivs in så loopas while loopen'''
            

        return_item = Item(category, name, colour, artnumb, amount)
        print("You have created the following item.")
        print(return_item)
        return return_item

'''main code'''

def main():

    items = load_item()

    print("Welcome to the inventory program.")

    while True:
        print("""
        Menu:

        1. Create a new item
        2. Search for items
        3. Remove item
        4. End program
        
        """)

        choice = input("-")

        if choice == "1":
            new = add_item()
            items.append(new)
            save_item(items)
        
        elif choice == "2":
            search_item()
            break

        elif choice == "3":
            remove_item()
            break

        elif choice == "4":
            clear_console()
            break

        else:
            print("You didn't choose one of the following:\n")

        '''funktioner blir kallade på'''

if __name__=="__main__":
    main()
