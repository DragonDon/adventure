""" DragonDon's Choose Your Own Adventure Fantasy Module
    Version 2.0
    v1 - name for each area
    v2 - generic name for each area

    event1 = ambush1
    event2 = ambush2 
    area1 = Snowhold 
    area2 = inn
    area3 = burial_mound
    area4 = area4_area
    area5 = area5_area
    opponent1 = kobolds 
    opponent2 =  avenging kobolds 
    quest1 = mentor 
    quest2 = ruins 
    quest3 = cult

    from core module:
    - visited_inn = visited_area2
"""

event1_description = "\nYou travel to the town of Snowhold. The King's Road turns from a reasonable path to one much less maintained. You see the remnants of broken carts at various points. \nSuddenly you are ambushed by Kobolds!  What do you do?"
event1_choice = "Choose: \n*(P)lead for your life \n*(R)un for the hills \n*(K)ill the vermin or \n*(c)ontinue your quest"
event1_prompt = "Ambush > "
event1_next1 = "p"
event1_next1_text = "\nThe Kobolds look at you funny and shuffle aimlessly about as if waiting for you to actually do something. You, feeling a sudden gush of depression for being a failed adventure, sit down and wither away into future.\n"
event1_next2 = "r"
event1_next2_text = "\nYou make a break for the hills at top speed. The Kobolds, and their tiny little legs, can't keep up to your muscular thighs! You feel the wind in your hair, the sun on your face and completely forget to stop for a break. Within minutes you have run out of breath and drop dead from a heart attack.\n"
event1_next3 = "k"
event1_next3_text = "\nThe Kobolds charge at you, you charge back and with one fell swing of your mighty sword, you have slain 5 Kobolds!"
event1_next4 = "c"
event1_next4_text = "\nNice try buddy.  Choose something else first you cheater!\n"
event1_next5 = "c"
event1_next5_text = "I've got no idea what that means. Maybe try reading what's in the brackets?"


event2_description = "\nYou travel around the town of Snowhold. The King's Road takes you a different way but still not maintained at all. \nSuddenly you are ambushed by Avenging Kobolds! They scream 'THIS IS FOR OUR FALLEN COMRADES!!!'"
event2_choice = "Choose: \n*(D)rop your weapons and cry \n*(R)un for the hills \n*(K)ill the vermin \n*(c)ontinue your quest"
event2_prompt = "Ambush2 > "
event2_next1 = "d"
event2_next1_text = "\nThe Kobolds run you through and every which way but loose.  Your last thoughts, as your consciousness ebbs away, are 'boy, this road needs some maintenance.' \n"
event2_next2 = "r"
event2_next2_text = "\nYou make a break for the hills at top speed. The Kobolds, and their tiny little legs, can't keep up to your muscular thighs! You feel the wind in your hair, the sun on your face and completely forget to stop for a break. Within minutes you have run out of breath and drop dead from a heart attack.\n"
event2_next3 = "k"
event2_next3_text = "\nThe Kobolds charge at you, you brandish your shiny(and very sharp) sword and they stop in their tracks.  You obviously mean business and they know they can't win, so they all commit suicide with their own weapons."
event2_next4 = "c"
event2_next4_text = "\nNice try buddy.  Choose something else first you cheater!\n"
event2_next5 = "c"
event2_next5_text = "I've got no idea what that means. Maybe try reading what's in the brackets?"

area1_description = "\nYou enter the town of Snowhold.  It was once one of the most important places in the North but is now all but forgotten. You hear the sounds of a small city around you and see a nominal amount of people going about their business as you would expect. \nWhere would you like to visit?"
area1_choice = "Choose: \n*Visit the (I)nn \n*(L)eave town."
area1_prompt = "Snowhold > "
area1_next1 = "i"
area1_next2 = "l"
area1_next2_text = "What?  You come to town and decide to blow before even getting details about your quest?  Sorry, this if loop won't break till you visit the Inn"

area2_description = "\nYou make your way to the Inn and going inside you see patrons here drinking ale, sitting by the fire and generally talking to themselves."
quest1_text = "\nSuddenly, one patron, an old fellow, shouts 'Not one of you lot cares about anything.  My friend and mentor to many, has dissapeared and no one cares!'\nWhat do you do?"
area2_choice =  "\nChoose: \n*(S)peak to old fellow \n*(L)eave Inn."
area2_prompt = "Inn > "
area2_next1 = "s"
area2_next1_text = "\nEh?  You willing to help me find my friend?  Maybe he was a mentor of yours? You will need to go to the Old Burial Mount outside of town.  That's where he told me he was going."
area2_next2 = "l"
area2_next2_text = "I've got not idea what that means. Maybe try reading what's in the brackets?"
quest2_text = "\nYou spy a man sitting at a table by himself.  He looks well weathered, dusty and seemingly carrying exploring equiment fit for ruins.\nWhat do you do?"
area2_choice2 = "\nChoose: \n*(Speak) to Obviously Experienced Traveller<tm>.\n*(Find) a barwench to explore in 'other' ways.\n*(Leave) Inn."
area2_next3 = "s"
area2_next3_text = "\n'Sigh. Another group looking for Ruins I suppose.  Yes I found them but I couldn't find any treasure.  Maybe you can. Here, take the damned map.  Search it and IF by chance you find something, at least buy me a drink!'"
area2_next4 = "f"
area2_next4_text = "\nMan...you ARE desparate to be thinking such stuff in THIS game.  It's ASCII text for crying out loud!  Go look for treasure or something!"
area2_next5 = "l"
area2_next5_text = "I've got not idea what that means. Maybe try reading what's in the brackets?"
quest3_text = "You walk into the Inn (what a redundant thing to say really) and look around.  Everything seems like you would expect except the creepy looking fellow who looked at you with wide eyes and made a dash for the back door. \nWhat do you do?\n"
area2_choice3 = "Choose: \n*(C)hase after him \n*(A)sk some locals who was that guy \n*(L)eave Inn."
area2_next6 = "chase"
area2_next6_text = "\nYou pounce off after the Blatantly Suspicious Man<tm>.  Out the back, through the kitchen, out the door.  You catch a glimpse of him climbing a tree and bounding over the city wall.  Drats.  He got away. You head back to the Inn to find out about that Blatantly Suspicious Man<tm>."
area2_next7 = "a" #reused, instead of using area2_next8 as the same
area2_next8_text = "Some drunken guy at the bar mummers 'Those cult boys gonna have a new sacrafice tonight it seems' as he eyes you blearily.  You grab him by the collar and demand to know what he meant by that.  Quite Drunk Guy<tm> squeals and says the fellahs in the Keep, north of Winerhaven, don't like newcomers to town. You drop him and decided to deal with those 'fellahs'" 
area2_next9 = "l"
area2_next10 = "I've got no idea what that means. Maybe try reading what's in the brackets?"

area3_description = "\nNormally some descriptive text of the area you have approached is put here but the guy who coded this program couldn't be bothered so you are outta luck.  Just get ready to fight some minor creatures, slighlty tougher than those weekling Kobolds.  OH, and some sort of ghostly apparition too. The two Gnomes, 2 guard drakes and 4 human rabble immediately start towards you.  The ghostly apparition floats menacingly behind them taunting you with words like 'doom', 'death' and 'destruction'\nWhat do you do?"
area3_choice = "Choose: \n*Take on the two (G)nomes because they are short and easy to deal with\n*Stare boldly at the (H)umans with the idea that you can simply intimidate them into submission.\n*Pick up a rock and with your deft skill, take out two (D)rakes with one stone \n*Taunt the (A)pparition with a few choice words of your own! \n*(c)ontinue your quest"
area3_prompt = "Burial Mound > "
area3_next1 = "g"
area3_next1_text = "\nYou advance on the Gnomes whom simply scatter into the nearby woods. Pff, Gnomes are a cowardly bunch. Your victory is shortlived as the human rabble pile on you and the Drakes pull your arms out of the sockets then you feel the cold touch of the Apparition.  Your heart stops. \n"
area3_next2 = "h"
area3_next2_text = "\nYou stare at the Human Rabble and being the cowardly group and possessing low self-esteem,  they are done for by the sheer force of your personality.  You suddenly feel severe pain in your legs as you then notice the two Gnomes gnawing at your hamstrings, which snap and you fall to the ground.  The Carniverous Gnomes are followed by the Drakes as they feast on your body then in swoops the Apparition which feasts on your soul.\n"
area3_next3 = "a"
area3_next3_text = "\nYou have a few choice words your self and you speak them proudly. 'I am a human being. My spirit will never die because I am not really playing this game but simply typing at a keyboard.  You cannot harm me!' The Apparition stops, looks completely crestfallen but suddenly perks up as the Gnomes, Drakes and Human Rabble nail your ass to the ground because you weren't paying attention to them.\n"
area3_next4 = "d"
area3_next4_text = "\nYou heft a decent size rock at one of the Drakes.  It nails it square in the temple which causes it to collapse.  The first Drake falls into the second one and in one lump they plummet from the air into the midst of the Human Rabble.  Now, being Human Rabble, that means they are severely malnurished.  They seize this opportunity for prime Drake-meat and immeditely begin to gnaw on the hapless creatures.  The Gnomes, being a rare breed of Carniverous Gnomes, go wild at the smell of blood and join in on the feeding frenzy.  The Apparition, seeing how he has utterly lost control of the situation vanishes in a puff of ether never to be heard of again."
area3_next5_text = "\nYou may (c)ontinue your quest"
area3_next6 = "c"
area3_next6_text = "\nNice try buddy.  Choose something else first you cheater!\n"            
area3_next7 = "I've got no idea what that means. Maybe try reading what's in the brackets?"

area4_description = "You follow the map the Obviously Experienced Traveller<tm> gave you.  It is surprisingly easy to do.  He's obviously been there quite a few times. As you wander off the King's Road onto a path, then down by a river, across it, pass Grandmother's House and onto another path again, just as you pass a large boulder or two you turn the corner and a rather LARGE giant blocks your way. Thinking that mayyyyybe you'll leave this one alone, you turn around and see a second GIANT blocking your retreat.  Trapped! That damned Obviously Experienced Traveller<tm> tricked you.  This is what you think the moment he walks out from behind one of the GIANTS. 'I know what you are thinking' he says. 'Do I feel lucky? Well I can tell you this. No matter what option you choose from the menu, you are going to die. I'll be taking your equipment, need to replace the crap I got from the last guy who came through here. What do you do?"
area4_choice = "Choose: \n*(G)ive up and let the Obviously Experienced Traveller<tm> take whatever he wants. [heh, like you have a choice really] \n*G(r)ip your sword tightly and prepare for a fight! \n*G(a)sp loudly as you notice a disturbing bulge in the GIANT'S loincloth but choose to 'take it like a man' and brace for the worst. \n*(C)urse the guy who made this program and put you in such a dilema in the first place!"
area4_prompt ="Ruins > "
area4_next1 = "g"
area4_text1 = "\nYou start to take all your equipment off and all 3 of your opponents smile broadly.  'You know, I heard a saying once' the Obviously Experienced Traveller<tm> said. 'Stealing is the gift that keeps on giving. You look like a nice, strong young traveller.  I think we'll keep you.' you are so stunned that you don't even notice the GIANT behind you grab and pin both your arms and proceeds to carry you off. \n"
area4_next2 = "r"
area4_text2 = "\nYou grip your trusty sword and grit your teeth while sneering contemptuously at the Obviously Experienced Traveller<tm> in front of you when suddenly you feel a blow from behind.  As the light fades from your eyes and sounds become muffled you hear something about 'trophy' and 'toy' before you black out. \n"
area4_next3 = "a"
area4_text3 = "\nYou gasp in shock as to the implications of such a bulge!  The GIANT looks pleased as your shock.  You feel 'something' large poke you from behind and your world goes black.\n"
area4_next4 = "c"
area4_text4 = "You curse loudly but in reality, nothing comes out of the computer as you realize that the Obviously Experienced Traveller<tm> was right.  This ends badly regardless of your choices.\n"
area4_text5 = "I've got no idea what that means. Maybe try reading what's in the brackets?"

area5_description  = "A cult?!  Now there is something any worthy adventurer will tackle to rid the world of! You march on over to this Keep with purpose of mind and strength of soul, plus your shiny sword doesn't hurt either. You feel alive.  You feel you can take on anything!  You march right up to the broad front door and kick that fucker down like it was some diseased waif begging for food and/or money.  Nothing is going to stop this reckoning from happening.  NOTHING! Nothing except that huge fucking undead Dragon sitting in the middle of the room maybe! \nWhat do you do?"
area5_choice = "Choose:\n*(S)cream 'LEEEEEEEEROYYYYYY JEEENKINS!!' And rush the room. \n*(Q)uiver in fear, piss your armor[which would be a shame since you just had it dry-cleaned last tuesday].\n*(A)sk them if they have a moment to talk about Jesus. \n*(c)ontinue your quest."
area5_prompt = "Cult > "
area5_next1 = "s"
area5_text1 = "\nHoping to catch them off guard by your brash actions, your vocal chords strain with mighty effort as you rush the Undead Dragon. But since it's ears rotted off thousands of years ago it can't hear a damn thing and with one chomp, your body becomes two pieces and your soul is theirs for the bidding.  You are manipulated into servitude and your first order of business is to oversee an excavation at some burial mound, in case of trouble.\n"
area5_continue_text = "You may (c)ontinue your quest" #reused
area5_next2 = "q"
area5_text2 = "\nYou were hoping to fall upon your own sword before they get to you. The cultists surrounding the Undead Dragon puke at the smell of your urine.  The Undread Dragon pucks because the cultists puke.  You puke now because everyone else is puking then you really do slip and fall right onto your own sword because that spicy lamb curry you picked up in the market earlier was a bit greasy.  Before yor completely die, the Undread Dragon snatches your soul.  You are manipulated into servitude and your first order of business is to oversee an excavation at some burial mound, in case of trouble.\n"
area5_next3 = "a"
area5_text3 = "\nThe cultists surrounding the Undread Dragon and even the Dragon himself, give you THE most disgusted look.  They slam the door in your face while saying 'if you come here again, I'll have you charged with trespassing!'  This sudden act of agression stuns you and you stumble back a few feet and activate an old pit trap.  You fall down and find a nice place to rest on a few spikes at the bottom.  Your soul is snagged by the cultists as it leaves your body.  You are manipulated into servitude and your first order of business is to oversee an excavation at some burial mound, in case of trouble.\n"
area5_next4 = "c"
area5_text4 = "\nNice try buddy.  Choose something else first you cheater!\n"            
area5_text5 ="I've got no idea what that means. Maybe try reading what's in the brackets?"

quest_complete_text = "\n** You have your quest is done!  Listen!  Can you hear the trumpets blaring?  If you can, better get that hearing check, ain't no sound in this game bucko!"
quest_complete_text1 = "\nYou hear the faint whisper of a sound that could be your missing Mentor, passing you a weak-voiced appreciation before dying due to age, malnutrition and severe beating from his captors."
quest_complete_text2 = "\nAs the GIANT takes you.........\naway...geeze, did you think I'd really get graphic here?  That's what Google is for.  Search for something equally disgusting and you can pretend that happened to you.  Try searching 'Angry Pirate' on urbandictionary.com(definition #2) but only with GIANTS."
quest_complete_text3 = "\nWell fuck, that didn't go as planned did it?  Maybe better luck next time?"

quest_path = "Having dispatched the Avenging Kobolds, you continue your journey."

dead_why = "Good Job!\n"

start_text = "\n **** Welcome to the Hinterlands....you might not survive... ****\nWhat is your quest? \n1/ I'm seeking my missing mentor! \n2/ I wish to search the ruins of a lost empire! \n3/ I have been warned with Ominus Signs of a Death Cult.  They must be stopped!"
start_prompt = "(Choose 1, 2, or 3) > "
start_next1 = "1"
start_next2 = "2"
start_next3 = "3"
start_dead = "Having not chosen any purpose in life, you die a lonely and bitter shade of a human being."

play_again_separator = " ************** "
play_again_prompt = "Would you like to try again? (y/n) >"
play_again_next1 = "y"
play_again_next2 = "n"
play_again_next2_1 = "pussy."
play_again_text = "I've got no idea what that means. Have you just not been following directions?  This help section has been printed ALL game long!!!"