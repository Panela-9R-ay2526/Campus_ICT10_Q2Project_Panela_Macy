# Working with Lists
from pyscript import document
# Variables
country = ["China", "Japan", "South Korea", "North Korea", "Mongolia", "Taiwan", "Hong Kong","Macau"]
nickname = ["The Red Dragon","Land of the Rising Sun", "Land of the Morning Calm", "The Hermit Kingdom","Land of the Eternal Blue Sky","The Beautiful Island", "Asia's World City","Las Vegas of Asia"]
# Function
def show_name(e):
    selected_country = document.getElementById("country").value

    index = country.index(selected_country)
    selected_nickname = nickname[index]

    document.getElementById("result").innerText = selected_nickname


def get_name (e):
    grade_7 = {'Aki Hayakawa', 'Hikaru Indo','Yoshiki Tsujinaka','Angel Devil'}
    grade_8 = {'Yuji Itadori', 'Megumi Fushiguro','Gojo Satoru','Geto Suguru'}
    grade_9 = {'Maki Zenin', 'Yuta Okkotsu','Kirara Hoshi','Nobara Kugisaki'}
    grade_10 = {'Katsuki Bakugo', 'Izuku Midoriya','Ochako Uraraka','Toga Himiko'}



    document.getElementById('output').innerHTML = ' '
    f_name = document.getElementById('fname').value.title().strip()
    l_name = document.getElementById('lname').value.title().strip()

    members = (grade_7 | grade_8 | grade_9 | grade_10)
    members.add(f'{f_name} {l_name}')

    display(f'Congratulations, {f_name} {l_name}! You are now part of the OBMC Marching Band!', target='output')
    display(f'List of Members: {members} {f_name} {l_name}, amount of members: {len(members)}', target='output')

#working with dictionaries
from pyscript import display, document

# Defining Variables
def nonmetal_value(e):
    document.getElementById('result').innerHTML = " "
    nonmetal_v = document.getElementById('dictionary').value   

    nonmetal = {
        'C':'Symbol: C  Element: Carbon Atomic Number: 6 Atomic Mass: 12.011',
        'Xe': 'Symbol: Xe Element: Xenon Atomic Number: 54 Atomic Mass: 131.293',
        'H':'Symbol: H Element: Hydrogen Atomic Number: 1 Atomic Mass: 1.008',
        'N':'Symbol: N Element: Nitrogen Atomic Number: 7  Atomic Mass: 14.007',
        'Ne':'Symbol: Ne Element: Neon  Atomic Number: 10 Atomic Mass: 20.1797',
        'I':'Symbol: I Element: Iodine  Atomic Number: 53 Atomic Mass: 126.90447',
        'Ar':'Symbol: Ar Element: Argon  Atomic Number: 18 Atomic Mass: 39.948',
        'Kr':'Symbol: Kr Element: Krypton  Atomic Number: 36 Atomic Mass: 39.948',
        'F':'Symbol: F Element: Fluorine  Atomic Number: 9 Atomic Mass: 18.998403162',
        'Rn':'Symbol: Rn Element: Radon  Atomic Number: 86 Atomic Mass: 222222.01758'
        }
  
    
    game_checker = nonmetal_v in nonmetal
    
# Displaying result   
    display_message = nonmetal.get(nonmetal_v, 'Sorry, please type a valid element')
    display(display_message, target="result")

