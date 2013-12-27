""" DragonDon's Choose Your Own Adventure Core Module
    Version 1.0
"""
from sys import exit
import textwrap

quest = 0

def event1(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.event1_description).strip()), width=60)
    kobolds_dead = False
    
    while True:
        print ""
        print module.event1_choice
        next = raw_input(module.event1_prompt)
        
        if next == module.event1_next1 and not kobolds_dead:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.event1_next1_sample_text).strip()), width=60))
        elif next == module.event1_next2 and not kobolds_dead:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.event1_next2_sample_text).strip()), width=60))
        elif next == module.event1_next3 and not kobolds_dead:
            print ""
            print textwrap.fill((textwrap.dedent(module.event1_next3_sample_text).strip()), width=60)
            kobolds_dead = True
        elif next == module.event1_next4 and not kobolds_dead:
            print ""
            print module.event1_next4_sample_text
        elif next == module.event1_next5 and kobolds_dead:
            visited_area2 = False
            area1(module, visited_area2)
        else:
            print ""
            print module.event1_next5_text

def event2(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.event2_description).strip()), width=60)
    kobolds_dead = False
    
    while True:
        print ""
        print module.event2_choice
        next = raw_input(module.event2_prompt)
        
        if next == module.event2_next1 and not kobolds_dead:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.event2_next1_sample_text).strip()), width=60))
        elif next == module.event2_next2 and not kobolds_dead:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.event2_next2_sample_text).strip()), width=60))
        elif next == module.event2_next3 and not kobolds_dead:
            print ""
            print textwrap.fill((textwrap.dedent(module.event2_next3_sample_text).strip()), width=60)
            kobolds_dead = True
        elif next == module.event2_next4 and not kobolds_dead:
            print ""
            print module.event2_next4_sample_text
        elif next == module.event2_next5 and kobolds_dead:
            visited_area2 = False
            quest_path(module)
        else:
            print ""
            print module.event2_next5_text
            
def area1(module, visited_area2):
    print ""
    print textwrap.fill((textwrap.dedent(module.area1_description).strip()), width=60)

    while True:
        print ""
        print module.area1_choice
        next = raw_input(module.area1_prompt)
            
        if next == module.area1_next1:
            area2(module)
        elif next == module.area1_next2 and visited_area2 == False:
            print ""
            print textwrap.fill((textwrap.dedent(module.area1_next2_text).strip()), width=60)
        elif next == module.area1_next2 and visited_area2 == True:
            event2(module)
        else:
            print ""
            print module.event1_next5_text   

def area2(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.area2_description).strip()), width=60)
    if quest == 1:
        print textwrap.fill((textwrap.dedent(module.quest1_sample_text).strip()), width=60)
        in_bar = True

        while True:
            print module.area2_choice
            next = raw_input(module.area2_prompt)
            if next == module.area2_next1 and in_bar:
                print ""
                print textwrap.fill((textwrap.dedent(module.area2_next1_sample_text).strip()), width=60)
            elif next == module.area2_next2:
                in_bar = False
                visited_area2 = True                
                area1(module, visited_area2)
            else:
                print ""
                print module.area2_next2_sample_text

    if quest == 2:
        print textwrap.fill((textwrap.dedent(module.area2_choice2).strip()), width=60)
        in_bar = True

        while True:
            print module.area2_choice2
            next = raw_input(module.area2_prompt)
            if next == module.area2_next3:
                print ""
                print textwrap.fill((textwrap.dedent(module.area2_next3_sample_text).strip()), width=60)
            elif next == module.area2_next4 and in_bar:
                print ""
                print textwrap.fill((textwrap.dedent(module.area2_next4_sample_text).strip()), width=60)
            elif next == module.area2_next5:
                visited_area2 = True                
                area1(module, visited_area2)
            else:
                print ""
                print module.area2_next5_sample_text
 
    if quest == 3:
        print ""
        print textwrap.fill((textwrap.dedent(module.quest3_sample_text).strip()), width=60)
        in_bar = True

        while True:
            print ""
            print module.area2_choice3
            next = raw_input(module.area2_prompt)
            if next == module.area2_next6:
                print ""
                print textwrap.fill((textwrap.dedent(module.area2_next6_sample_text).strip()), width=60)
                next = module.area2_next7
            elif next == module.area2_next7:
                print ""
                print textwrap.fill((textwrap.dedent(module.area2_next8_sample_text).strip()), width=60)
            elif next == module.area2_next9:
                visited_area2 = True                
                area1(module, visited_area2)                
            else:
                print ""
                print module.area2_next10


def event3(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.event3_description).strip()), width=60)
    player_dead = False

    while True:
        print ""
        print module.event3_choice
        next = raw_input(module.event3_prompt)
        
        if next == module.event3_next1:
            print ""
            dead((textwrap.fill((textwrap.dedent(module.event3_next1_sample_text).strip()), width=60)), module)
            player_dead = True
            print module.event3_next5_sample_text
        elif next == module.event3_next2 and not player_dead:
            print ""
            dead(textwrap.fill((textwrap.dedent(module.event3_next2_sample_text).strip()), width=60), module)
            player_dead = True
            print module.event3_next5_sample_text
        elif next == module.event3_next3 and not player_dead:
            print ""
            dead(textwrap.fill((textwrap.dedent(module.event3_next3_sample_text).strip()), width=60), module)
            player_dead = True
            print module.event3_next5_sample_text
        elif next == module.event3_next4:
            print ""
            dead(textwrap.fill((textwrap.dedent(module.event3_next4_sample_text).strip()), width=60), module)
            print module.event3_next5_sample_text
            player_dead = True
            print module.event3_next5_sample_text
        elif next == module.event3_next6 and not player_dead:
            print ""
            print module.event3_next6_sample_text
        elif next == module.event3_next6 and player_dead:
            quest_complete(module)
        else:
            print ""
            print module.event3_next7
                
def ruins(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.ruins_description).strip()), width=60)
    death_awaits = True

    while True:
        print module.ruins_choice
        next = raw_input(module.ruins_prompt)
        
        if next == module.ruins_next1:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.ruins_sample_text1).strip()), width=60))
        elif next == module.ruins_next2 and death_awaits:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.ruins_sample_text2).strip()), width=60))
        elif next == module.ruins_next3:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.ruins_sample_text3).strip()), width=60))
        elif next == module.ruins_next4 and death_awaits:
            print ""
            print dead(textwrap.fill((textwrap.dedent(module.ruins_sample_text4).strip()), width=60))
            death_awaits = False
            quest_complete(module)
        else:
            print ""
            print module.ruins_sample_text5

def cult(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.cult_description).strip()), width=60)
    death_cult = True

    while True:
        print ""
        print module.cult_choice

        next = raw_input(module.cult_prompt)
        
        if next == module.cult_next1 and death_cult:
            print ""
            print textwrap.fill((textwrap.dedent(module.cult_sample_text1).strip()), width=60)
            print module.cult_continue_text
            death_cult = False
        elif next == module.cult_next2 and death_cult:
            print ""
            print textwrap.fill((textwrap.dedent(module.cult_sample_text2).strip()), width=60)
            print module.cult_continue_text
            death_cult = False
        elif next == module.cult_next3 and death_cult:
            print ""
            print textwrap.fill((textwrap.dedent(module.cult_sample_text3).strip()), width=60)
            print module.cult_continue_text
            death_cult = False
        elif next == module.cult_next4 and death_cult:
            print ""
            print module.cult_sample_text4
        elif next == module.cult_next4 and not death_cult:
            quest_complete(module)
        else:
            print ""
            print module.cult_sample_text5

def quest_path(module):
    print ""
    print module.quest_path
    if quest == 1:
        event3(module)
    if quest == 2:    
        ruins(module)
    if quest == 3:       
        cult(module)

def quest_complete(module):
    print ""
    print textwrap.fill((textwrap.dedent(module.quest_complete_sample_text).strip()), width=60)
    if quest == 1:
        print ""
        print textwrap.fill((textwrap.dedent(module.quest_complete_sample_text1).strip()), width=60)
        play_again(module)
    if quest == 2:
        print ""
        print textwrap.fill((textwrap.dedent(module.quest_complete_sample_text2).strip()), width=60)
        play_again(module)
    if quest == 3:
        print ""
        print module.quest_complete_sample_text3
        play_again(module)

def dead(why, module):
    print ""
    print why, module.dead_why
    
def start():
    global quest

    print "Game Genres to choose from:"
    print "1/ Fantasy"
    print "2/ Sci-Fi"
    print "3/ Horror"
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
    else:
        print "Please choose a number"

    print module.start_text
    next = raw_input(module.start_prompt)
    
    if next == module.start_next1:
        quest = 1
        event1(module)
        quest = 1
    elif next == module.start_next2:
        quest = 2
        event1()
    elif next == module.start_next3:
        quest = 3
        event1()     
    else:
        dead(module.start_dead, module)

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
            print textwrap.fill((textwrap.dedent(module.play_again_sample_text).strip()), width=60)
            modulequest_complete_sample_text1

start()