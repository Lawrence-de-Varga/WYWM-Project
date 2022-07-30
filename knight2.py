from random import choice
from decorators import *

########################## Data for Program ######################################################################

# Knights for testing
knights = {'john': {'age': '23', 'weapon': 'mace', 'castle': 'london',
                    'adjs': ['trusty', 'foreboding', 'impoverished', 'whoremongering']},
           'james': {'age': '24', 'weapon': 'lance', 'castle': 'paris',
                     'adjs': ['venerable', 'decrepit', 'loyal', 'hunting']}}
#knights = {}

weapon_adjs = ['trusty', 'venerable', 'vicious', 'blood-thirsty', 'gleaming', 'rusty', 'notched']

castle_adjs = ['glorious', 'decrepit', 'impenetrable', 'foreboding', 'lavish', 'luxuriant', 'gargantuan']

knight_activities = ['taxing the peasants', 'feasting', 'training for war', 'raping and pillaging',
                     'deep in prayer', 'entertaining nobles', 'seducing the ladies of the court',
                     'drunkenly brawling', 'drunkenly reveling', 'plotting and scheming',
                     'scheming and plotting', 'jousting', 'hunting', 'whoremongering',
                     'overtaxing the peasants', 'deep in thought', 'consumed in reading',
                     'dispensing justice', 'dispensing injustice']


def select_activities(*args):
    """Used to generate lists of activities which are compatible with particular knight_adjs"""
    return [activity for x, activity in enumerate(knight_activities) if x in args]


# The following could be simplified by creating a few select groups to go with
# particular attributes, but I decided to maintain granular control of exactly which 
# activities are compatible with which attributes
knight_adjs = {'noble': select_activities(0, 1, 2, 4, 5, 9, 10, 11, 12, 15, 16, 17),
               'righteous': select_activities(0, 1, 2, 4, 5, 9, 10, 11, 12, 15, 16, 17),
               'loyal': select_activities(0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18),
               'ferocious': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18),
               'vengeful': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18),
               'heroic': select_activities(0, 1, 2, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17),
               'dissolute': select_activities(0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18),
               'pious': select_activities(0, 1, 2, 4, 5, 9, 10, 11, 12, 15, 16, 17),
               'perfidious': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18),
               'wise': select_activities(0, 1, 2, 4, 5, 9, 10, 11, 12, 15, 16, 17),
               'learned': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18),
               'virtuous': select_activities(0, 1, 2, 4, 5, 9, 10, 11, 12, 15, 16, 17),
               'impoverished': select_activities(0, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18),
               'indomitable': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18),
               'indolent': select_activities(0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18),
               'foolish': select_activities(0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18),
               'cowardly': select_activities(0, 1, 3, 5, 6, 8, 9, 10, 13, 14, 15, 16, 18),
               'niggardly': select_activities(0, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18),
               'half-witted': select_activities(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18),
               'circumspect': select_activities(0, 1, 2, 4, 5, 6, 8, 9, 10, 13, 14, 15, 16, 17, 18)
               }

knight_descriptions = {}
glorious_scrolls = []


################################################ Text helper functions #########################################

def prompt(message):
    """ Used to prompt the user to input"""
    print(message)
    return input(">> ")


def set_article(adjective):
    """ Used to set either an 'a' or 'an' before an adjective"""
    if adjective[0] in 'aeiou':
        return f"an {adjective}"
    else:
        return f"a {adjective}"


# Takes a name like 'albert the great' and returns 'Albert the Great'
# NOTE articles_and_others is not necessarily complete  
articles_and_others = ['the', 'a', 'an', 'and', 'on', 'in', 'of', 'some', 'from']


def format_name(name):
    """ Takes a name and capitalizes every word not in articules_and_others. E.g.
        'albert the great' is returned as 'Albert the Great'."""
    name = name.split()
    new_name = []
    for word in name:
        if word in articles_and_others:
            new_name.append(word)
        else:
            new_name.append(word.capitalize())
    return ' '.join(new_name)


############################################ Menu Presentation and Selection #################################

def first_word(string):
     """ Used to retrieve the first string from a menu option presented to the user. This string is then checked
         against the user input to see what option they have chosen."""
     return string.split(' ', 1)[0]


def first_words(options):
    """ Used to transform an entire list of options selected by the user according to first_word()"""
    return [first_word(option) for option in options]


def gen_options_dict(range_of_dict, options):
    """ Used to generate a dict using ints cast to strings as keys, so that there is no need to convert
         the user input to an integer"""
    string_range = [str(num) for num in range_of_dict]

    return dict(zip(string_range, options))


def gen_options(options_list, object_name, action_name, every=True, esc=True):
    """  Takes a list of menu options and returns a dictionary of the form returned by gen_options_dict
         also adds the 'all' and 'exit' option to all menus by default"""
    if not options_list:
        print(f"There are no {object_name}'s to {action_name}.")
        return False

    if every:
        options_list = options_list + ['all']
    if esc:
        options_list = options_list + ['exit']

    return gen_options_dict(range(1, 1 + len(options_list)), options_list)


def print_options(options_dict):
    """ Prints the menu options in a numbered list and returns options_dict to pass to select_options"""
    if not options_dict:
        return False

    for x, option in options_dict.items():
        print(f"{x}: {format_name(option)}")

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
            new_str = new_str + char
            prev_char = char
        elif char == ' ' and prev_char == ' ':
            prev_char = char

    new_str = new_str.split(',')
    new_str = [option.strip().lower() for option in new_str]
    return new_str


def select_options(options_to_select, object_name, action_name):
    """ Select_options takes a dictionary of the form returned by print_options, asks the user to choose an option
     or options using either the name of the option or its list number, it then returns a list containing
     all of the options selected in their word form e.g. if the options are {'1':'a','2':'b','3':'c'}
     and the user gives 1 b 3 as input, select_options will return ['a', 'b', 'c'] """
    # Check if there are any options to select from
    if not options_to_select:
        return False

    selection = prompt(f"Which {object_name} would you like to {action_name}? (Please separate options with commas.)")
    selection = format_input(selection)
    options_to_return = []

    # If the user selects 'all' we return a list containing every available option
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

    return options_to_return


def select_options_wrap(options, so_object_name, so_action_name, go_object_name='', 
                       go_action_name='', every=True, esc=True):
    """  select_options_wrap is a wrapper for select_options(print_options(gen_options etc.))
         go_object_name and go_action_name are usually the same as so_object_name and so_action_name
         respectively, but on rare occasions (such as update_knight) they are different."""
    if not go_object_name:
        go_object_name = so_object_name
    if not go_action_name:
        go_action_name = so_action_name
    return select_options(print_options(gen_options(options, go_object_name, go_action_name, every, esc)),
                          so_object_name, so_action_name)


def select_knight(action):
    """select_knights uses select_options_wrap to allow for the selection of knights"""
    return select_options_wrap(list(knights.keys()), 'knight(s)', action, 'knight')


####################################### Knight Options #######################################################

def set_knight_name():
    return prompt("Please enter a name for the knight:").lower()


def set_knight_age(name):
    age = prompt(f"How old is {format_name(name)}?")

    try:
        int(age)
    except ValueError:
        print("Please enter a positive integer for the age.")
        return get_knight_age(name)
    return str(abs(int(age)))

def set_knight_weapon(name):
    return prompt(f"What weapon does {format_name(name)} favour?")


def set_knight_castle(name):
    return prompt(f"What is the name of {format_name(name)}'s castle?")


def set_knight_adjs(name):
    knights[name]['adjs'] = [choice(weapon_adjs), choice(castle_adjs), choice(list(knight_adjs.keys()))]
    return knights[name]['adjs'] + [choice(knight_adjs[knights[name]['adjs'][2]])]

set_attr_func_dict = {'age': set_knight_age, 'weapon' : set_knight_weapon,
                      'castle' : set_knight_castle, 'adjs' : set_knight_adjs}


def set_knight_attrs(selection, name):
    
    for attr in selection:
        knights[name][attr] = (set_attr_func_dict[attr])(name)
    knight_descriptions[name] = gen_knight_desc(name)


def create_knight():
    """ Create a new entry in the 'knights' dict"""

    print("Let's make a knight")
    name = set_knight_name()

    if name in knights:
        print(f"{format_name(name)} is already a knight.")
        selection = select_options_wrap(['overwrite', 'update'], 'action', 'take',
                            every=False)
        print(selection)
        if 'overwrite' in selection:
            knights[name] = {}
            set_knight_attrs(list(set_attr_func_dict.keys()), name)
        elif 'update' in selection:
            update_knight(name)
        else:
            return
    else:
        knights[name] = {}
        set_knight_attrs(list(set_attr_func_dict.keys()), name)


def update_knight(name):

    """ Updates an individual knight, and generates a new description,"""
    print(f"Updating {format_name(name)}.")
    attrs = select_options_wrap(['name', 'age', 'weapon', 'castle'], 'attributes', 'update', 'knight')

    if 'exit' in attrs:
        return

    if 'name' in attrs:
        new_name = set_knight_name() 
        knights[new_name] = knights[name]
        knights.pop(name)
        knight_descriptions.pop(name)
        set_knight_attrs([attr for attr in attrs if attr != 'name'], new_name)
    else:
        set_knight_attrs(attrs, name)
    

@should_i_exit(knights)
def update_knights(selection):
    """ Updates multiple knights"""
    for name in selection:
        update_knight(name)


@should_i_exit(knights)
def delete_knights(selection):
    """ Deletes an arbitrary selection of knights."""
    erase_knights(selection)

    for name in selection:
        print(f"Executing {format_name(name)}.")
        knights.pop(name)
        knight_to_file('dead_knights.txt', knight_descriptions.pop(name))
        if name in glorious_scrolls:
            glorious_scrolls.pop(name)


######################################## Knight Describing Functions ########################################

def gen_knight_desc(name):
    """Used to generate the description dictionary for an individual knight."""
    info = knights[name]
    adjs = info['adjs']
    desc_dict = {}
    name = format_name(name)

    desc_dict['character'] = f"{name} is {set_article(adjs[2])} {info['age']} year old knight."
    desc_dict['weapon'] = f"In battle he favours his {adjs[0]} {info['weapon']}."
    desc_dict['activities'] = f"{name} can usually be found waging war or {adjs[3]}."
    # TODO Add random adjectives to replace 'grand' in the castle string
    desc_dict['castle'] = (f"{name} resides in the {adjs[1]} castle known as "
                           f"{format_name(info['castle'])}. Its furnishings are as grand as he is {adjs[2]}.")

    return desc_dict


def access_attributes(knight_description, attributes):
    """ Takes a knight-Description and a list of attributes and returns a string comprised of the 
        values of those attributes from the knight_description dict."""
    description = ''

    for attr in attributes:
        description = description + knight_description[attr] + '\n' 
    return description


def select_attrs_to_describe(name):
    """ Allows the user to select which attributes of a knight to describe."""
    print(f"what would you like to know about {format_name(name)}?")
    attributes = select_options_wrap(['character', 'weapon', 'activities', 'castle'], 'attributes', 'describe')

    return access_attributes(knight_descriptions[name], attributes)

@should_i_exit(knight_descriptions)
def describe_knights(selection):
    """ Glues together the description strings returned for each knight by select_attrs_to_describe
        and prints this larger string once finished."""
    description = ''
    
    for name in selection:
        description = description + f"Let me tell you about {format_name(name)}:\n" +  select_attrs_to_describe(name) + '\n'
    print(description)


# Only used for testing, in practice the descriptions will be generated when the knight is created
def gen_knights_descs():
    """ Used to generate the description lists for all of the knights. """
    for name in knights.keys():
        knight_descriptions[name] = gen_knight_desc(name)
    return knight_descriptions


####################################### Writing Knights to File ###############################################

def knight_to_file(file, knight_description):
    """ Used to save the descriptions of a knight to a file. """
    with open(file, 'a') as f:
        for string in knight_description.values():
            f.write(string)
            f.write('\n')
        f.write('\n')


@should_i_exit(knights)
def knights_to_file(selection, file):
    """ Writes an arbitrary selection of knights to a file"""
    for name in selection:
        glorious_scrolls.append(name)
        knight_to_file(file, knight_descriptions[name])


##################################### Removing Knights from File ##############################################

@should_i_exit(glorious_scrolls)
def erase_knights(selection):
    """ Erases the descriptions of the selected knights in the knights.txt file."""
    global glorious_scrolls
    # The check below uses sets because [1,2,3] != [2,3,1], but {1,2,3} == {2,3,1} and selection
    # and glorious_scrolls might contain the same elements but not be in the same order
    if set(selection) == set(glorious_scrolls):
        with open('knights.txt', 'w') as f:
            f.truncate(0)
        glorious_scrolls = []
    else:
        glorious_scrolls = [name for name in glorious_scrolls if name not in selection]
        with open('knights.txt', 'w') as f:
            f.truncate(0)
        gs_copy = glorious_scrolls.copy()
        return knights_to_file(gs_copy, 'knights.txt')


########################################## Import Knights from TXT Description File ############################

# TODO allow for the selection of particular knights from the file rather than just grabbing all of them

def read_knights(file):
    """ Reads in the entire file ('knights.txt') and returns the list."""
    with open(file, 'r') as f:
        return f.readlines()
#    return kns


def get_knights(lines):
    """ Takes the list from read_knights() and returns a list whose elements are lists containing the
         4 line descriptions of the knights."""
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


def retrieve_details(kn):
    """ Takes the 4 string lists from which are returned as elements of a list from get_knights
         and extracts the info necessary to rebuild the description for further use."""
    kn = [line.split() for line in kn]

    name = ' '.join(kn[0][:-7])
    age = kn[0][-4]
    weapon = ' '.join(kn[1][6:])[:-1]
    castle = ' '.join(kn[3][8 + len(name.split()) - 1:]).split('.')[0]

    weapon_adj = kn[1][5]
    if weapon_adj not in weapon_adjs:
        return False

    castle_adj = kn[3][4 + len(name.split()) - 1]
    if castle_adj not in castle_adjs:
        return False

    char_adj = kn[0][-5]
    if char_adj not in knight_adjs:
        return False

    activity = ' '.join(kn[2][7 + len(name.split()):])[:-1]
    if activity not in knight_activities:
        return False

    return [name, age, weapon, castle, weapon_adj, castle_adj, char_adj, activity] 


def retrieve_knights(kns):
    """ Takes the list from get_knights and extracts the details needed to generate entries for 'knights',
         and 'knight_descriptions' by using retrieve_details as above."""
    for name in kns:
        result = retrieve_details(name)
        if result:
            knights[result[0]] = {'age': result[1], 'weapon': result[2], 'castle': result[3],
                             'adjs': [result[4], result[5], result[6], result[7]]}
            knight_descriptions[result[0]] = gen_knight_desc(result[0])
        else:
            print("Corrupt Input File.")
            return False
            


def resurrect_knights(file):
    """ Takes a file and returns all the knight entries from that file (which by default is 'dead_knights.txt')
         Also truncates the given file."""
    if retrieve_knights(get_knights(read_knights(file))):
        with open(file, 'w') as f:
            f.truncate()


#################################################### Main Menu #################################################

def menu():
    """ Present the main menu to the user."""
    menu_ops = ['create a knight', 'update some knights', 'describe some knights',
                'execute some knights', 'record some grand knights in the scrolls',
                'erase some troublesome knights from the scrolls', 'resurrect knights from the dead']
    print()
    print('########## MAIN MENU ##########')
    print()

    # select_options_wrap is not used as we need to modify the presented options before
    # they select one.
    options = print_options(gen_options(menu_ops, 'action', 'take', every=False))
    for num, option in options.items():
        options[num] = first_word(option)

    action = select_options(options, 'action', 'take')

    # action[0] is used to prevent multiple options being selected as in other menus.
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
        knights_to_file(select_options_wrap([knight for knight in knights if knight not in glorious_scrolls], 'knight',
                                'record in the scrolls'), 'knights.txt')
        menu()
    elif action[0] == 'erase':
        erase_knights(select_options_wrap(glorious_scrolls, 'knight', 'erase from the scrolls'))
        menu()
    elif action[0] == 'resurrect':
        resurrect_knights('dead_knights.txt')
        menu()
    elif action[0] == 'exit':
        print("Goodbye.")
    else:
        print("Bad input.")
        menu()


# gen_knights_descs() is only for testing
gen_knights_descs()
menu()
