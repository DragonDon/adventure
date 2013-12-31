""" DragonDon's Choose Your Own Adventure Core Module
    Version 2.2.1
    - 1.0 flavour text included in code
    - 2.0 flavour text moved to external file
    - 2.1 change function names to generic names
    - 2.2 change print formatting to a function call for flavour text
    - 2.2.1 minor text edits, opponent name change, removed "sample" from text name 
"""
from sys import exit
import textwrap

quest = 0

def printText(text):
    print(textwrap.fill((textwrap.dedent(text).strip()), width=60))


def event1(module):
    print ""
    printText(module.event1_description)
    opponent1_dead = False
    
    while True:
        print ""
        print module.event1_choice
        next = raw_input(module.event1_prompt)
        
        if next == module.event1_next1 and not opponent1_dead:
            print ""
            printText(module.event1_next1_text)
            print module.dead_why
            quest_complete(module)
        elif next == module.event1_next2 and not opponent1_dead:
            print ""
            printText(module.event1_next2_text)
            print module.dead_why
            quest_complete(module)
        elif next == module.event1_next3 and not opponent1_dead:
            print ""
            printText(module.event1_next3_text)
            opponent1_dead = True
            printText(module.area3_next5_text)
        elif next == module.event1_next4 and not opponent1_dead:
            print ""
            print module.event1_next4_text
        elif next == module.event1_next5 and opponent1_dead:
            visited_area2 = False
            area1(module, visited_area2)
        else:
            print ""
            print module.event1_next5_text

def event2(module):
    print ""
    printText(module.event2_description)
    opponent2_dead = False
    
    while True:
        print ""
        print module.event2_choice
        next = raw_input(module.event2_prompt)
        
        if next == module.event2_next1 and not opponent2_dead:
            print ""
            printText(module.event2_next1_text)
            print module.dead_why
            quest_complete(module)
        elif next == module.event2_next2 and not opponent2_dead:
            print ""
            printText(module.event2_next2_text)
            print module.dead_why
            quest_complete(module)
        elif next == module.event2_next3 and not opponent2_dead:
            print ""
            printText(module.event2_next3_text)
            opponent2_dead = True
            printText(module.area3_next5_text)
        elif next == module.event2_next4 and not opponent2_dead:
            print ""
            print module.event2_next4_text
        elif next == module.event2_next5 and opponent2_dead:
            visited_area2 = False
            quest_path(module)
        else:
            print ""
            print module.event2_next5_text
            
def area1(module, visited_area2):
    print ""
    printText(module.area1_description)

    while True:
        print ""
        print module.area1_choice
        next = raw_input(module.area1_prompt)
            
        if next == module.area1_next1:
            area2(module)
        elif next == module.area1_next2 and visited_area2 == False:
            print ""
            print (printText(module.area1_next2_text))
        elif next == module.area1_next2 and visited_area2 == True:
            event2(module)
        else:
            print ""
            print (printText(module.event1_next5_text))

def area2(module):
    print ""
    printText(module.area2_description)
    if quest == 1:
        printText(module.quest1_text)
        in_bar = True

        while True:
            print module.area2_choice
            next = raw_input(module.area2_prompt)
            if next == module.area2_next1 and in_bar:
                print ""
                print (printText(module.area2_next1_text))
            elif next == module.area2_next2:
                in_bar = False
                visited_area2 = True                
                area1(module, visited_area2)
            else:
                print ""
                print module.area2_next2_text

    if quest == 2:
        print module.area2_choice2
        in_bar = True

        while True:
            print module.area2_choice2
            next = raw_input(module.area2_prompt)
            if next == module.area2_next3:
                print ""
                print (printText(module.area2_next3_text))
            elif next == module.area2_next4 and in_bar:
                print ""
                print (printText(module.area2_next4_text))
            elif next == module.area2_next5:
                visited_area2 = True                
                area1(module, visited_area2)
            else:
                print ""
                print (printText(module.area2_next5_text))
 
    if quest == 3:
        print ""
        printText(module.quest3_text)
        in_bar = True

        while True:
            print ""
            print module.area2_choice3
            next = raw_input(module.area2_prompt)
            if next == module.area2_next6:
                print ""
                printText(module.area2_next6_text)
                next = module.area2_next7
            elif next == module.area2_next7:
                print ""
                printText(module.area2_next8_text)
            elif next == module.area2_next9:
                visited_area2 = True                
                area1(module, visited_area2)                
            else:
                print ""
                printText(module.area2_next10)

def area3(module):
    print ""
    printText(module.area3_description)
    player_dead = False

    while True:
        print ""
        print module.area3_choice
        next = raw_input(module.area3_prompt)
        
        if next == module.area3_next1:
            print ""
            printText(module.area3_next1_text)
            print module.dead_why
            player_dead = True
            print module.area3_next5_text
        elif next == module.area3_next2 and not player_dead:
            print ""
            printText(module.area3_next2_text)
            print module.dead_why
            player_dead = True
            print module.area3_next5_text
        elif next == module.area3_next3 and not player_dead:
            print ""
            printText(module.area3_next3_text)
            print module.dead_why
            player_dead = True
            print module.area3_next5_text
        elif next == module.area3_next4:
            print ""
            printText(module.area3_next4_text)
            print module.dead_why
            printText(module.area3_next5_text)
            player_dead = True
        elif next == module.area3_next6 and not player_dead:
            print ""
            printText(module.area3_next6_text)
        elif next == module.area3_next6 and player_dead:
            quest_complete(module)
        else:
            print ""
            printText(module.area3_next7)
                
def area4(module):
    print ""
    printText(module.area4_description)
    death_awaits = True

    while True:
        print module.area4_choice
        next = raw_input(module.area4_prompt)
        
        if next == module.area4_next1:
            print ""
            printText(module.area4_text1)
            print module.dead_why
        elif next == module.area4_next2 and death_awaits:
            print ""
            printText(module.area4_text2)
            print module.dead_why
        elif next == module.area4_next3:
            print ""
            printText(module.area4_text3)
            print module.dead_why
        elif next == module.area4_next4 and death_awaits:
            print ""
            printText(module.area4_text4)
            print module.dead_why
            death_awaits = False
            quest_complete(module)
        else:
            print ""
            print module.area4_text5

def area5(module):
    print ""
    printText(module.area5_description)
    death_cult = True

    while True:
        print ""
        print module.area5_choice

        next = raw_input(module.area5_prompt).lower();
        
        if next == module.area5_next1 and death_cult:
            print ""
            printText(module.area5_text1)
            print module.area5_continue_text
            death_cult = False
        elif next == module.area5_next2 and death_cult:
            print ""
            printText(module.area5_text2)
            print module.area5_continue_text
            death_cult = False
        elif next == module.area5_next3 and death_cult:
            print ""
            printText(module.area5_text3)
            print module.area5_continue_text
            death_cult = False
        elif next == module.area5_next4 and death_cult:
            print ""
            print module.area5_text4
        elif next == module.area5_next4 and not death_cult:
            quest_complete(module)
        else:
            print ""
            print module.area5_text5

def quest_path(module):
    print ""
    print module.quest_path
    if quest == 1:
        area3(module)
    if quest == 2:    
        area4(module)
    if quest == 3:       
        area5(module)

def quest_complete(module):
    print ""
    printText(module.quest_complete_text)
    if quest == 1:
        print ""
        printText(module.quest_complete_text1)
        play_again(module)
    if quest == 2:
        print ""
        printText(module.quest_complete_text2)
        play_again(module)
    if quest == 3:
        print ""
        print module.quest_complete_text3
        play_again(module)
    
def start():
    global quest

    print "Game Genres to choose from:"
    print "1/ Fantasy"
    print "2/ Sci-Fi (Placeholder only)"
    print "3/ Horror (Placeholder only)"
    print "or hit any other key + enter to quit"
    genre = raw_input("Choose your game genre: ")

    if genre == "1":
        import fantasy_text2
        module = fantasy_text2
    elif genre == "2":
        import sci_fi_text
        module = sci_fi_text
    elif genre == "3":
        import horror_text
        module = horror_text
    elif genre == "Q" or "q":
        exit(0)
    else:
        print "Please choose an option"

    print module.start_text
    next = raw_input(module.start_prompt)
    
    if next == module.start_next1:
        quest = 1
        event1(module)
        quest = 1
    elif next == module.start_next2:
        quest = 2
        event1(module)
    elif next == module.start_next3:
        quest = 3
        event1(module)     
    else:
        printText(module.start_dead)
        print module.dead_why

def play_again(module):
    print ""
    print module.play_again_separator

    while True:
        print ""
        next = raw_input(module.play_again_prompt)

        if next == module.play_again_next1:
            start()
        elif next == module.play_again_next2:
            print ""
            print module.play_again_next2_1
            exit(0)
        else:
            print ""
            printText(module.play_again_text)
            print module.quest_complete_text1

start()
