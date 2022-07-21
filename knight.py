from random import choice

########################## Data for Program ######################################################################

# Knights for testing
knights = {'john': {'age': '23', 'weapon': 'mace', 'castle': 'london', 
                'adjs': ['trusty', 'foreboding', 'impoverished', 'whoremongering']}, 
           'james': {'age': '24', 'weapon': 'lance', 'castle': 'paris', 
               'adjs': ['venerable', 'decrepit', 'loyal', 'hunting']}}
#knights = {}

weapon_adjs = ['trusty', 'venerable', 'vicious', 'blood-thirsty',  'gleaming', 'rusty', 'notched']

castle_adjs = ['glorious', 'decrepit', 'impenetrable', 'foreboding', 'lavish', 'luxuriant', 'gargantuan']

# TODO change to dictionary to increase readability 
knight_activities = ['taxing the peasants', 'feasting', 'training for war', 'raping and pillaging',
                     'deep in prayer', 'entertaining nobles', 'seducing the ladies of the court',
                     'drunkenly brawling', 'drunkenly reveling', 'plotting and scheming', 
                     'scheming and plotting', 'jousting', 'hunting', 'whoremongering', 
                     'overtaxing the peasants', 'deep in thought', 'consumed in reading',
                     'dispensing justice', 'dispensing injustice']

# Used to generate list comprehensions of activities which are compatible with knight_adjs
def select_activities(*args):
    return [activity for x, activity in enumerate(knight_activities) if x in args]

# The following could be simplified by creating a few select groups to go with 
# particular attributes, but I decided to maintain granular control of exactly which 
# activities are compatible with which attributes
knight_adjs = {'noble' :        select_activities(0,1,2,4,5,9,10,11,12,15,16,17),
               'righteous' :    select_activities(0,1,2,4,5,9,10,11,12,15,16,17),
               'loyal' :        select_activities(0,1,2,3,4,5,7,8,9,10,11,12,14,15,16,17,18),
               'ferocious' :    select_activities(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
               'vengeful' :     select_activities(0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18),
               'heroic' :       select_activities(0,1,2,4,5,8,9,10,11,12,15,16,17),
               'dissolute' :    select_activities(0,1,2,3,5,6,7,8,9,10,11,12,13,14,18),
               'pious' :        select_activities(0,1,2,4,5,9,10,11,12,15,16,17),
               'perfidious' :   select_activities(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18),
               'wise' :         select_activities(0,1,2,4,5,9,10,11,12,15,16,17),
               'learned' :      select_activities(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
               'virtuous' :     select_activities(0,1,2,4,5,9,10,11,12,15,16,17),
               'impoverished' : select_activities(0,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18),
               'indomitable' :  select_activities(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
               'indolent' :     select_activities(0,1,3,5,6,7,8,9,10,11,12,13,14,18),
               'foolish' :      select_activities(0,1,3,5,6,7,8,9,10,11,12,13,14,18),
               'cowardly' :     select_activities(0,1,3,5,6,8,9,10,13,14,15,16,18),
               'niggardly' :    select_activities(0,2,3,4,6,7,8,9,10,12,14,15,16,17,18),
               'halfwitted' :   select_activities(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,18),
               'circumspect' :  select_activities(0,1,2,4,5,6,8,9,10,13,14,15,16,17,18)
               }


knight_descriptions = {}
glorious_scrolls = []

################################################ Text helper functions #########################################

# used to prompt the user to input
def prompt(message):
    print(message)
    return input(">> ")

# Used to set either an 'a' or 'an' before an adjective
def set_article(adjective):
    if adjective[0] in 'aeiou':
        return f"an {adjective}"
    else:
        return f"a {adjective}"

####################################### Decorator Functions ###################################################

# A number of functions need to check whether or not knights or some other dict or list is empty
# and whether or not they have been passed 'exit' as input by the user, the decorator below 
# keeps that code out of those functions
def should_i_exit(objects):
    def func_wrapper(function):
        def wrapper(*args, **kwargs):
            if not objects or 'exit' in *args:
                return
            else:
                return function(*args, **kwargs)
        return wrapper        
    return func_wrapper

############################################ Menu Presentation and Selection #################################

# Used to retrieve the first string from a menu option presented to the user. This string is then checked
# against the user input to see what option they have chosen. Use of the first word allows a longer option
# description to be presented to the user, whilst they only have to type in the first key word e.g
# if 'Create a knight' is presented, the can simply type 'create' (or the integer presented before the string)
def first_word(string):
    return string.split(' ', 1)[0]

# Used to transform an entire list of options selected by the user according to first_word() 
def first_words(options):
    return [first_word(option) for option in options]

# Used to generate a dict using ints cast to strings as keys, so that there is no need to convert 
# the user input to an integer
def gen_options_dict(range_of_dict, options):
    string_range = [str(num) for num in range_of_dict]

    return dict(zip(string_range, options))

# takes a list of menu options and returns a dictionary of the form returned by gen_options_dict
# also adds the 'all' and 'exit' option to all menus by default
def gen_options(options_list, object_name, action_name, every=True, esc=True):
    if not options_list:
        print(f"There are no {object_name}'s to {action_name}.")
        return False 

    if every:
        options_list = options_list +  ['all']
    if esc:
        options_list = options_list +  ['exit']

    return gen_options_dict(range(1, 1 + len(options_list)), options_list)

# Prints the menu options in a numbered list and returns options_dict to pass to select_options
def print_options(options_dict):
    if not options_dict:
        return False

    for x, option in options_dict.items():
        print(f"{x}: {option.capitalize()}")

    print()
    return options_dict

def format_input(selection_string):
    """ Takes any string given by the user, removes extraneous spaces, splits the string
        on the commas and generates a selection list to return"""
    new_str = ''  
    prev_char = ''
      
    for char in selection_string:
     if char != ' ':
         new_str = new_str + char
         prev_char = char
     elif char == ' ' and prev_char != ' ':
         new_str = new_str  + char
         prev_char = char
     elif char == ' ' and prev_char == ' ':
         prev_char = char
         
    new_str = new_str.split(',')
    new_str = [option.strip().lower() for option in new_str]
    return new_str

# TODO Review the use of first_words and first_word, I have bodged it to work for now
# But it may not be necessary
# Select_options takes a dictionary of the form returned by gen_options, asks the user to choose an option
# or options using either the name of the option or its list number, it then returns a list containing
# all of the options selected in their word form e.g. if the options are {'1':'a','2':'b','3':'c'}
# and the user gives 1 b 3 as input, select_options will return ['a', 'b', 'c']
def select_options(options_to_select, object_name, action_name):
    # Check if there are any options to select from
    if not options_to_select: 
        return False 

    selection = prompt(f"Which {object_name} would you like to {action_name}? (Please seperate options with commas.)")
    selection = format_input(selection)
    options_to_return = []
#    print(f"Options to select: {options_to_select}")
#    print(f"Selection: {selection}")

    # If the user selects 'all' we return a list containg every available option
    # except for 'all' and 'exit'
    all_key = str(len(options_to_select) - 1)
    if options_to_select[all_key] == 'all' and ('all' in selection or all_key in selection):
        # Removes 'exit' and 'all' from the return list
        options_to_return = list(options_to_select.values())
        del options_to_return[-2:]
        return options_to_return

    # returns a list with every option selected by the user in its word form
    # as the words are used as keys later on
    for option in selection:
        if option in options_to_select.keys():
            options_to_return.append(options_to_select[option])
        elif option in options_to_select.values():
            options_to_return.append(option)
        else:
            print("Bad input.")
            return select_options(options_to_select, object_name, action_name)
#    print(f"Options to return: {options_to_return}")
    return options_to_return

# so_wrap is a wrapper for select_options(print_options(gen_options etc))
# go_n and ga_n are usuually the same as so_n and sa_n respectively, but on rare
# occassions (such as update_knight) they are different.
def so_wrap(options, so_n, sa_n, go_n= '', ga_n = '', every = True, esc = True):
    if not go_n:
        go_n = so_n
    if not ga_n:
        ga_n = sa_n
    return select_options(print_options(gen_options(options, go_n, ga_n, every, esc)),
                          so_n, sa_n)

def select_knight(action):
    return so_wrap(list(knights.keys()), 'knight(s)', action, 'knight')
        
####################################### Knight Options #######################################################

# Collects the basic details and generates the description of a knight
def knight_details(name):

    knights[name] = {}

    age = prompt(f'How old is {name.capitalize()}?')
    try:
        int(age)
        knights[name]['age'] = age
    except:
        print("Please enter an integer for the age.")
        return knight_details(name)

    weapon = prompt(f'What weapon does {name.capitalize()} favour?').lower()
    knights[name]['weapon'] = weapon

    castle = prompt(f"What is the name of {name.capitalize()}'s castle?")
    knights[name]['castle'] = castle

    # sets an unchanging group of adjectives used to enliven the descriptions of the knight
    knights[name]['adjs'] = [choice(weapon_adjs), choice(castle_adjs),
                             choice(list(knight_adjs.keys()))]

    # The knight activity is added after the other character attributes have been chosen
    # because the possible activity is dependant on the chosen character attribute.
    # knights[name]['adjs'][2] references the character attribute chosen above
    knights[name]['adjs'].append(choice(knight_adjs[knights[name]['adjs'][2]]))

    knight_descriptions[name] = gen_knight_desc(name)

# TODO Maintain the capitalization of names such as Albert the Great
def create_knight():
    # Create a new entry in the 'knights' dict
    print("Let's make a knight")
    # Names are stored in lowercase
    name = prompt("Please enter the knights name:").lower()

    if name in knights:
        print(f"{name.capitalize()} is already a knight.")
        selection = so_wrap([f'overwrite {name.capitalize()}', f'update {name.capitalize()}'], 'action', 'take', every=False)
        if 'overwrite' in selection:
            knights[name] = {}
            knight_details(name)

        elif 'update' in selection:
            update_knight(name)
        else:
            return
    else:
        knight_details(name)

# Updates an individual knight, and geenrates a new description,
# if the name is changed the knights and knight_descriptions dictionaries are modified 
def update_knight(knight):
    print(f"Updating {knight.capitalize()}.")
    attrs = so_wrap(['name', 'age', 'weapon', 'castle'], 'attributes', 'update', 'knight')

    if 'exit' in attrs:
        return

    if 'name' in attrs:
        new_name = prompt(f"What would you like {knight.capitalize()}'s new name to be?")
        knights[new_name] = knights[knight]
        knights.pop(knight)
        knight_descriptions.pop(knight)
        knight = new_name

    for attr in attrs:
        if attr == 'name':
            continue
        new_val = prompt(f"What would you like {knight.capitalize()}'s new {attr} to be?")

        knights[knight][attr] = new_val

    knight_descriptions[knight] = gen_knight_desc(knight)
    return knight

# Updates multiple knights 
@should_i_exit(knights)
def update_knights(selection):

    for knight in selection:
        new_knight = update_knight(knight)

# Deletes an arbitrary selection of knights
@should_i_exit(knights)
def delete_knights(selection):
    erase_knights(selection)

    for kn in selection:
        print(f"Executing {kn.capitalize()}.")
        knights.pop(kn)
        knight_to_file('dead_knights.txt', knight_descriptions.pop(kn))
        if kn in glorious_scrolls: glorious_scrolls.pop(kn)

######################################## Knight Describing Functions ########################################

# Used to generate the description dictionary for an individual knight
def gen_knight_desc(k_name):
    info = knights[k_name]
    adjs = info['adjs']
    desc_dict = {}
    name = k_name.capitalize()

    desc_dict['character'] = f"{name} is {set_article(adjs[2])} {info['age']} year old knight."
    desc_dict['weapon'] = f"In battle he favours his {adjs[0]} {info['weapon']}."
    # TODO Add another activity to each knight
    desc_dict['activities'] = f"{name} can usually be found waging war or {adjs[3]}."
    # TODO Add random adjectives to replace 'grand' in the castle string
    desc_dict['castle'] = (f"{name} resides in the {adjs[1]} castle known as " 
                          f"{info['castle'].capitalize()}. Its furnishings are as grand as he is {adjs[2]}.")

    return desc_dict

# by default prints the format string, pass False to return the string
def format_k_desc(k_desc, prn=True):
    format_string = ""
    for attr in k_desc.values():
        format_string += attr + "\n"
    if prn:
        print(format_string)
    else:
        return format_string

def access_attribute(k_desc, attribute, prn=True):
    if prn:
        print(k_desc[attribute])
        print() 
    else:   
        return k_desc[attribute]

def prnKD(k_desc):
    format_k_desc(k_desc)

def describe_knight(knight):
    print(f"Describing: {knight.capitalize()}")
    attributes = so_wrap(['character', 'weapon', 'activities', 'castle'], 'attributes', 'describe')
    if 'exit' in attributes:
        return
    if {'character', 'weapon', 'activities', 'castle'} == set(attributes):
        return prnKD(knight_descriptions[knight])
    else:
        for attr in attributes:
            print(f"{knight.capitalize()}'s {attr}:")
            access_attribute(knight_descriptions[knight], attr)



# Prints the description string for an arbitrary selection of knights
#describe_knights = should_i_exit(
@should_i_exit(knight_descriptions)
def describe_knights(selection):

    for knight in selection:
        describe_knight(knight)
#        prnKD(knight_descriptions[knight])

# Only used for testing, in practice the descriptions will be generated when the knight is created
# Used to collect the description lists for all or some of the knights
def gen_knights_descs():
    for knight in knights.keys():
        knight_descriptions[knight] = gen_knight_desc(knight)
    return knight_descriptions

####################################### Writing Knights to File ###############################################

# Used to save the descriptions of a knight to a file. 
def knight_to_file(file, k_desc):
    
    with open(file, 'a') as f:
        f.write(format_k_desc(k_desc, False))
        f.write('\n')

# Writes an arbitrary selection of knights to a file
@should_i_exit(knights)
def knights_to_file(selection, file):

    for kn in selection:
        knight_to_file(file, knight_descriptions[kn])
        if not kn in glorious_scrolls: glorious_scrolls.append(kn)

##################################### Removing Knights from File ##############################################

# erases the descriptions of the knights in the knights.txt file
@should_i_exit(glorious_scrolls)
def erase_knights(selection):
    
    global glorious_scrolls
    # The check below uses sets because [1,2,3] != [2,3,1], but {1,2,3} == {2,3,1} and selection
    # and glorious_scrolls might contain the same elements but no be in the same order
    if set(selection) == set(glorious_scrolls):
        with open('knights.txt', 'w') as f:
            f.truncate(0)
        glorious_scrolls = []
    else:
        glorious_scrolls = [knight for knight in glorious_scrolls if not knight in selection]
        with open('knights.txt', 'w') as f:
            f.truncate(0)
        gs_copy = glorious_scrolls.copy()
        return knights_to_file(gs_copy, 'knights.txt')

########################################## Import Knights from TXT Description File ############################

# TODO allow for the selection of particular knights from the file rather than just grabbing all of them

# Used to allow for retrieval of items made up of two or more words i.e 'battle axe'
def list_to_string(list):
    string = ""
    for item in list:
        string += (item.strip() + ' ')
    return string.strip()[:-1]


# Reads in the entire file ('knights.txt') and returns the list
def read_knights(file):
    with open(file, 'r') as f:
        kns = f.readlines()
    return kns

# Takes the list from read_knights() and returns a list whose elements are lists containing the 
# 4 line descriptions of the knights
def get_knights(lines):
    kns = []
    knight = []

    for line in lines:
        if len(knight) == 4:
            kns.append(knight)
            knight = []
        elif line == '\n':
            continue
        else:
            knight.append(line)
    return kns

# TODO allow for names with multiple words in them
# TODO Add error handling for files with incorrect formatting
def retrieve_details(kn):
    kn = [line.split() for line in kn]

    name = kn[0][0]
    age = kn[0][4]
    castle = list_to_string(kn[3][8:-9])
    weapon = list_to_string(kn[1][6:])
    char_adj = kn[0][3]
    weapon_adj = kn[1][5]
    activity = list_to_string(kn[2][8:])
    castle_adj = kn[3][4]

    knights[name] = {'age': age, 'weapon' : weapon, 'castle' : castle, 
                     'adjs' : [weapon_adj, castle_adj, char_adj, activity]}
    knight_descriptions[name] = gen_knight_desc(name)

# Takes the list from get_knights and extracts the details needed to generate entries for 'knights',
# and 'knight_descriptions' by using retrieve_details as above
def retrieve_knights(kns):
    for knight in kns:
        retrieve_details(knight)
    return knights
        
# Takes a file and returns all the knight entries from that file (which by default is 'dead_knights.txt')
# Also truncates the given file
def ressurect_knights(file):
    retrieve_knights(get_knights(read_knights(file)))
    with open(file, 'w') as f:
        f.truncate()


#################################################### Main Menu #################################################

def menu():
    menu_ops = ['create a knight','update some knights','describe some knights',
                'execute some knights', 'record some grand knights in the scrolls', 
                'erase some troublesome knights from the scrolls', 'ressurect knights from the dead']
    print()
    print('########## MAIN MENU ##########')
    print()
   
    options = print_options(gen_options(menu_ops, 'action', 'take', every=False))
    for key, val in options.items():
        options[key] = first_word(val)

    action = select_options(options, 'action', 'take')

    if action[0] == 'create':
        create_knight()
        menu()
    elif action[0] == 'update':
        update_knights(select_knight('update'))
        menu()
    elif action[0] == 'describe':
        describe_knights(select_knight('describe'))
        menu()
    elif action[0] == 'execute':
        delete_knights(select_knight('execute'))
        menu()
    elif action[0] == 'record':
        knights_to_file(so_wrap([knight for knight in knights if not knight in glorious_scrolls], 'knight', 'record in the scrolls'), 'knights.txt')
        menu()
    elif action[0] == 'erase':
        erase_knights(so_wrap(glorious_scrolls, 'knight', 'erase from the scrolls' ))
        menu()
    elif action[0] == 'ressurect':
        ressurect_knights('dead_knights.txt')
        menu()
    elif action[0] == 'exit':
        print("Goodbye.")
    else:
        print("Bad input.")
        menu()

gen_knights_descs()
menu()

