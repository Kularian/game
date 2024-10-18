#Switch declarations
label before_main_menu:
    play music "audio/Persona's Door.mp3"
    call screen pre_menu

label main_menu:
    call screen main_menu

label loadsave:
    call screen load

label preferences:
    call screen preferences

label extra:
    "Under Construction."
    jump battle

label Introcutscenes:
    if introcutscene == False:
        $ renpy.movie_cutscene("video/P1PSPOpening2.avi")
        $ introcutscene = True
    else:
        #$ renpy.movie_cutscene("video/P1PSXOpening.avi")
        $ introcutscene = False
    call screen pre_menu

label start2:
    define config.developer = True
    $ style.say_dialogue = style.say_dialogue
    default ooishiintro = False
    default hanyaintro = False
    default dramaclub = False
    default fencingclub = False
    default toro = False
    default Yuko = False
    default label026 = False
    default label029 = False
    default devilboy = False
    default studentcouncilprez = False
    default yamaoka = False
    default reijiflags = 0
    default reijifactory = False
    default reijimom = False
    default reijicasino = False
    default reijicheck = 0
    default location = "1F Empty Classroom"
    default ward = 1
    default floor = 1
    default yyyukino = False
    default yyyukino2 = False
    default rosacandidamark = False
    default Sebec1 = False
    default infirmarydialogue = 0
    default choice1 = ""
    default choice2 = ""
    default choicetext = ""
    default lines = 1
    default hospitalscene = 0
    default tbnarrator = 0
    default plotprogress = 0
    default reijisebec = False
    default ellycasino = 0
    default pddemon = False
    default tamakirapier = False
    default introcutscene = False
    default toroshards = False
    default thanatospersona = 0
    default marikoshard = False
    default jackfrostfriend = False

    scene bg black
    centered "Once, I dreamt I was a butterfly."
    centered "I forgot myself and knew only my happiness as a butterfly.\nSoon, I awoke, and I was myself again."
    centered "Did I dream that I was a butterfly?\n\nOr do I now dream that I am a man?"
    centered "Yet there is a distinction between myself and the butterfly.\nThis is the transformation of the physical.\n\n- Zhuangzi"
#    $ tbnarrator = "True"
#    n "There is an optional prologue, which provides additional exposition and insight."
#    n "This is not canon, and you may skip it if you prefer."
#    menu:
#        "Would you like to see the optional prologue?"
#        "Yes.":
#            window hide
#            jump prologue
#        "No.":
#            window hide
#            jump intro
    jump intro

label prologue:
    $ tbnarrator = "False"
    scene bg test with qdis
    $ location = "Maki's Room"
    show screen header with qdis
    show maki with qdis
    stu "I'm sorry if I worried all of you..."
    "{color=#ebffdb}>Maki Sonomura (Nickname: Maki)\nA chronically ill classmate who's just been hospitalized.{/color}"
    hide ma
    show mark animated neutral sad with qdis
    stu "Worried ain't the half of it.  You passed right out in Phys Ed!"
    show mark ns
    "{color=#ebffdb}>Masao Inaba (Nickname: Mark)\nThe spoiled son of Inaba Dry Cleaning's owners. Earnest and exciteable.{/color}"
    hide mark
    show maki with qdis
    ma "I'm not sure what happened...I was fine one minute and the next..."
    hide maki
    show mark animated neutral smirk with qdis
    mk "Hey, I'm just glad you're okay.  You'll be outta here soon."
    show mark ns
    hide screen header with qdis
    $ choicetext = "Right Naoya?"
    show nchoice at pright zorder 15 with easeinright
    show nchoice onlayer screens zorder 15 at pright
    show fadeblack onlayer screens zorder 3 with qdis
    $ choice1 = "Yeah, it won't be long."
    $ choice2 = "The doctors said..."
    call screen choices with qdis
    if _return == 1:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide mark
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show screen header with qdis
        show mark animated neutral smirk
        mk "See?  Even Naoya thinks so."
        hide mark
        show maki with qdis
        ma "I don't know... the doctors couldn't figure out what was wrong."
        hide maki
    if _return == 2:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide mark
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show screen header with qdis
        show mark animated neutral sad
        mk "Wait what?  What'd they say?"
        hide mark
        show maki with qdis
        ma "They said they're not sure what's wrong with me..."
        hide maki
    show mark animated neutral serious
    mk "What?  How the hell do they not know?  Aren't they doctors?  That's their whole job!"
    hide mark
    show maki with qdis
    ma "But if I can get my strength back, I'll definitely be coming back to school."
    hide maki
    show mark animated neutral smirk with qdis
    mk "Of course!  But until you do, I'll come visit you as much as I can."
    hide mark
    show maki with qdis
    ma "Thank you, Masao..."
    "Maki lets out a very long yawn, her eyes fluttering closed."
    ma "I think I'm going to take a little rest.  I'll see you later?"
    hide maki
    show mark animated neutral smirk with qdis
    mk "Yeah.  I'll try to come by tomorrow.  C'mon Naoya, we should let her rest."

    scene bghospital1 with qdis
    $ location = "Mikage Hospital"
    show screen header with qdis
    show mark animated neutral serious with qdis
    mk "Man.  I can't believe her mom didn't show up to help her."
    mk "I know she's busy working over at SEBEC, but c'mon.  What's more important than your kid?"
    hide mark with qdis
    pause 0.5
    show mark animated neutral serious with qdis
    mk "Anyway, we should get back to the school and tell Mrs. Ooishi the doctors got her on bed rest for awhile."
    show mark animated neutral sad
    mk "I figure they'll send something to the school, right?  Surprised Ooishi even let us first years go and check on her."
    mk "I guess she was worried when Maki's mom didn't answer any calls at work..."
    hide mark with qdis
    pause 0.5
    show mark animated neutral serious with qdis
    mk "C'mon.  Let's get outta here, Naoya."

    scene courtyard with qdis
    show mark animated neutral serious with qdis
    mk "...and that kind of explains all of that.  They dunno when she'll be out."
    hide mark
    show ooishi at pleft with qdis
    tea "I see...that poor girl.  We can all hope that she gets better soon."
    "{color=#ebffdb}>Principal Ooishi\nThe principal of St. Hermelin High.  She adores children and flowers.{/color}"
    oo "I'll get the teachers together and see if we can't do something for her."
    hide ooishi
    show mark animated neutral sad with qdis
    mk "Cool.  Me an' Naoya are gonna try to visit her when we can, too."
    hide mark
    show ooishi at pleft with qdis
    oo "I think that's wonderful!  Make sure to tell the other students about it too.  Let's get as many as we can to visit her and keep her spirits up!"
    oo "You two can head home for the day.  I'll talk to your teachers about it."
    hide ooishi
    show mmark animated neutral smirk with qdis
    mk "Even Hamya?"
    hide mark
    show ooishi at pleft with qdis
    oo "Masao, that's Mr. Hanya.  Please don't make me regret my decision here."
    oo "I know you've had some run-ins with the police..."
    hide ooishi
    show mark animated neutral serious with qdis
    mk "Hey, Old Baldy just got mad 'cause I tagged a few walls.  It wasn't like I did anything serious."
    hide mark
    show ooishi at pleft with qdis
    oo "That's the Chief of Police you're talking about, Masao.  And while I support your artistry...a less controversial outlet would be better, I feel."





label intro:
    scene bg black
    $ renpy.movie_cutscene("video/P1PSPOpening2.avi")
    $ naoyax = 1000
    $ naoyay = 400
    $ markx = 900
    $ marky = 450
    $ nanjox = 600
    $ nanjoy = 500
    $ brownx = 800
    $ browny = 300
    $ ayasex = 700
    $ ayasey = 350
    $ ellyx = 1100
    $ ellyy = 500
    $ yukinox = 700
    $ yukinoy = 550
    scene bg personagame
    show naoyasprite downleft stand at naoyaloc
    show nanjosprite upright stand at nanjoloc
    show marksprite downleft stand at markloc
    show yukinosprite upright stand at yukinoloc
    show brownsprite downright stand at brownloc
    show ayasesprite downright stand at ayaseloc
    show ellysprite upleft stand at ellyloc
    with qdis
    $ tbnarrator = 0
    play music opening2
    $ location = "1F Empty Classroom"
    show screen header with qdis
    show mark animated neutral serious with qleft
    show text1 at left with qright
    show text2 at bottom with qzoom
    hide text1
    hide text2
    show marksprite downleft standmove
    voice mark1
    stu "\"{color=#800000}Persona{/color}\"?"
    voice mark2
    stu "Dude if that really worked and I could see my future, I'd be on easy street."
    show mark animated neutral smirk
    voice mark3
    show marksprite upleft standmove
    stu "You sure you ain't got the brain rot, Hidehiko?"
    $ tbnarrator = 1
    show mark ns
    n "{color=#ebffdb}>Masao Inaba (Nickname: Mark)\nThe spoiled son of Inaba Dry Cleaning's owners. Earnest and exciteable.{/color}"
    $ tbnarrator = 0
    show marksprite upleft stand
    hide mark with qdis
    show brown animated neutral smirk with qleft
    show brownsprite downright standmove
    voice brown1
    stu "Hehehe...Turns out there's more to it than an easy joke!"
    voice brown2
    stu "Maybe not seeing the future, exactly, but weird stuff does happen!"
    voice brown3
    stu "I'm willing to put my money where my mouth is if you are, Mark."
    $ tbnarrator = 1
    show brown ns
    n "{color=#ebffdb}>Hidehiko Uesugi (Nickname: Brown)\nCraves attention and doesn't take things very seriously.{/color}"
    $ tbnarrator = 0
    hide brown with qdis
    show brownsprite downright stand
    show mark animated neutral smirk with qleft
    show marksprite upleft standmove
    voice mark4
    mk "Alright... You're on."
    voice mark5
    mk "I'll bet you an all-you-can-eat dinner at the Peace Diner on Joy Street."
    hide mark with qdis
    show marksprite upleft stand
    show ayase animated neutral smirk with qleft
    show ayasesprite downright standmove
    voice ayase1
    stu "Woooo!  I'm with Hidehiko!"
    $ tbnarrator = 1
    show ayase
    n "{color=#ebffdb}>Yuka Ayase (Nickname: Ayase)\nA troublemaking member of the suntanned, bleach-blonde \"kogal\" set.{/color}"
    $ tbnarrator = 0
    hide ayase with qdis
    show ayasesprite downright stand
    show elly animated neutral smirk with qdis
    show marksprite downright stand
    show ellysprite upleft standmove
    voice elly1
    stu "I'll throw my lot in with Brown, too."
    $ tbnarrator = 1
    show elly
    n "{color=#ebffdb}>Eriko Kirishima (Nickname: Elly)\nA ladylike student recently returned from abroad.  Beautiful and intelligent.{/color}"
    $ tbnarrator = 0
    hide elly with qdis
    show ellysprite upleft stand
    show mark animated neutral sad with qleft
    show marksprite downright standmove
    voice mark6
    mk "Are you guys serious?"
    show mark animated neutral smirk
    show marksprite downleft standmove
    voice mark7
    mk "Yo Kei, Yukino!  Who're you guys gonna side with?"
    hide mark with qdis
    show marksprite downleft stand
    show nanjo animated neutral serious with qleft
    show nanjosprite downleft standmove
    voice nanjo1
    stu "Hmph.  As if I cared one whit... It's absolute bunk."
    $ tbnarrator = 1
    show nanjo
    n "{color=#ebffdb}>Kei Nanjo (Nickname: Nanjo)\nHeir to the Nanjo Group.  An utter pragmatist and skeptic.{/color}"
    $ tbnarrator = 0
    hide nanjo with qdis
    show nanjosprite upright stand
    show yukino animated neutral serious with qleft
    show yukinosprite downright standmove
    voice yukino1
    stu "What he said... This is all you."
    $ tbnarrator = 1
    show yukino
    n "{color=#ebffdb}>Yukino Mayuzumi (Nickname: Yukino)\nTrusted by everyone, she's like an older sister to all the students.{/color}"
    $ tbnarrator = 0
    hide yukino with qdis
    show yukinosprite upright stand
    show mark animated neutral sad with qleft
    show marksprite downleft standmove
    voice mark8
    mk "Ugh!  You guys are so cold, y'know?"
    show marksprite upright standmove
    show mark animated neutral serious
    voice mark9
    mk "Hey, who're you with? It's gotta be me, right?  C'mon, what's it gonna be?"
    show mark ns
    hide screen header with qdis
    $ choicetext = "Will you bet on Mark or Brown?"
    show nchoice at pright zorder 15 with easeinright
    show nchoice onlayer screens zorder 15 at pright
    show fadeblack onlayer screens zorder 3 with qdis
    $ choice1 = "Bet on Mark"
    $ choice2 = "Bet on Brown"
    call screen choices with qdis
label label000: #mark/brown choice
    if _return == 1:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide mark
        show marksprite upright stand
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show screen header with qdis
        show ayase animated neutral smirk with qdis
        show ayasesprite downright standmove
        voice ayase2
        ay "Awww!  Just wait... you'll be sorry!"
    elif _return == 2:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show screen header with qdis
        show mark animated neutral sad with qleft
        voice mark10
        mk "Sheesh, you too?  All y'alls crazy."
    show ayasesprite downright stand
    show marksprite upright stand
    hide ayase with qdis
    hide mark with qdis
    show brown animated neutral smirk with qleft
    show brownsprite downright standmove
    show marksprite upleft stand
    voice brown4
    br "Heeheehee... This'll be fun!  Awright, let's get started!"
    scene bg black with qdis
    $ naoyax = 800
    $ naoyay = 450
    $ markx = 200
    $ marky = 500
    $ nanjox = 900
    $ nanjoy = 400
    $ brownx = 1000
    $ browny = 200
    $ ayasex = 1600
    $ ayasey = 400
    $ ellyx = 800
    $ ellyy = 700
    $ yukinox = 900
    $ yukinoy = 500
    $ tbnarrator = 1
    scene bg personagame
    show naoyasprite upright stand at naoyaloc
    show nanjosprite upright stand at nanjoloc
    show yukinosprite upright stand at yukinoloc
    show ayasesprite upleft stand at ayaseloc
    show brownsprite downright stand at brownloc
    show marksprite upright stand at markloc
    show ellysprite upright stand at ellyloc
    with qdis
    $ tbnarrator = 0
    show ayase animated neutral serious with qleft
    voice ayase3
    $ newlocx = 1060
    $ newlocy = 240
    ay "'Kay!  Here goes!  Umm.  Persona!  Persona!  Please come here!"
    hide ayase with moveoutleft
    window hide
    show ayasesprite upleft walk at newloc with MoveTransition(2.5)
    $ ayasex = 1060
    $ ayasey = 240
    show ayasesprite upleft stand at ayaseloc
    window show
    show brown animated neutral serious with qleft
    voice brown5
    $ newlocx = 275
    $ newlocy = 475
    br "My turn!  Persona!  Persona!  Come here!"
    hide brown with moveoutleft
    window hide
    show ayasesprite downleft stand
    show naoyasprite upleft stand
    show nanjosprite upleft stand
    show yukinosprite upleft stand
    show brownsprite downleft walk at newloc with MoveTransition(3.5)
    $ brownx = 275
    $ browny = 475
    show brownsprite downleft stand at brownloc
    show mark animated neutral sad with qleft
    window show
    show marksprite upright standmove
    voice mark11
    mk "Man, why I gotta do this...?"
    hide mark with qdis
    show marksprite upright stand
    show brown animated neutral smirk with qleft
    show brownsprite downleft standmove
    voice brown6
    br "Hurry it up!  All-you-can-eat!  All-you-can-eat!"
    hide brown with qdis
    show brownsprite downleft stand
    show mark animated neutral serious with qleft
    voice mark12
    $ newlocx = 750
    $ newlocy = 670
    mk "Okay, okay... Persona, Persona.  C'mere... I guess."
    hide mark with moveoutleft
    window hide
    show brownsprite downright stand
    show naoyasprite downleft stand
    show nanjosprite downleft stand
    show yukinosprite downleft stand
    show marksprite downright walk at newloc with MoveTransition(3.5)
    $ markx = 750
    $ marky = 670
    show marksprite downright stand at markloc
    show elly animated neutral serious with qleft
    window show
    voice elly2
    $ newlocx = 1600
    $ newlocy = 425
    el "Well, then... Persona, Persona!  Please come to us..."
    hide elly with moveoutleft
    window hide
    show ayasesprite downright stand
    show naoyasprite downright stand
    show nanjosprite downright stand
    show yukinosprite downright stand
    show marksprite upright stand
    show ellysprite upright walk at newloc with MoveTransition(3.5)
    $ ellyx = 1600
    $ ellyy = 425
    show ellysprite upleft stand at ellyloc
    show naoyasprite downleft stand
    show nanjosprite downleft stand
    show yukinosprite downleft stand
    show brown animated neutral smirk with qleft
    window show
    window auto
    show brownsprite upright standmove
    voice brown7
    br "Alright! Here it comes!"
    show brown ns
    voice brown8
    extend "\n{w=0.3}...{w=0.3}...{w=0.3}...{w=0.3}...{w=0.3}...{w=0.3}..."
    show brown animated neutral sad
    voice brown9
    extend "H-Huh?"
    scene bg black with qdis
    $ naoyax = 1000
    $ naoyay = 400
    $ markx = 900
    $ marky = 450
    $ nanjox = 600
    $ nanjoy = 500
    $ brownx = 800
    $ browny = 300
    $ ayasex = 700
    $ ayasey = 350
    $ ellyx = 1100
    $ ellyy = 500
    $ yukinox = 700
    $ yukinoy = 550
    scene bg personagame
    show naoyasprite upleft stand at naoyaloc
    show nanjosprite upright stand at nanjoloc
    show marksprite upleft stand at markloc
    show yukinosprite upright stand at yukinoloc
    show brownsprite downright stand at brownloc
    show ayasesprite downright stand at ayaseloc
    show ellysprite upleft stand at ellyloc
    with qdis
    show ayase animated neutral serious with qleft
    show ayasesprite downright standmove
    voice ayase4
    ay "Hidehiko!  You jerk!  Now I look like a total idiot!"
    hide ayase with qdis
    show ayasesprite downright stand
    show mark animated neutral smirk with qleft
    show marksprite upleft standmove
    voice mark13
    mk "See?  A fat load o' nothin'.  Hehe... Looks like I win."
    hide mark with qdis
    show marksprite upleft stand
    show yukino animated neutral serious with qleft
    show yukinosprite upright standmove
    voice yukino2
    yu "*Sigh* Happy now?  Hurry up and go get the teacher."
    hide yukino with qdis
    show yukinosprite upright stand
    show brown animated neutral sad with qdis
    show brownsprite downright standmove
    voice brown10
    br "W-Wait!  Hold up!  One more time!  Please!?  Mark screwed it up!"
    voice brown11
    br "C'mon, you gotta take it seriously when you do it."
    hide brown with qdis
    show brownsprite downright stand
    show mark animated neutral sad with qleft
    show marksprite upleft standmove
    voice mark14
    mk "Oh, you little...!  What a sore loser."
    play music opening2 fadeout 0.5
    show marksprite upleft stand
    hide screen header
    scene bg black with qdis
#    $ renpy.movie_cutscene("video/PSPCutscene1.avi")
#    scene bg weirdgirl with qdis
#    play music ohno fadein 0.5 fadeout 0.5
#    $ tbnarrator = 1
#    "Behind them, the figure of a young girl in white appears."
#    "Nanjo stares in bewilderment at the girl in white."
#    $ tbnarrator = 0
#    na "Wha...What is...?"
#    mk "Huh?  It's too late now to ask to--"
#    $ tbnarrator = 1
#    "Mark glances over his shoulders and, at the sight of the girl, turns to face her."
#    $ tbnarrator = 0
#    mk "Woah!"
#    $ tbnarrator = 1
#    "As everybody in the group stops and stares at her, the girl begins to cry."
#    $ tbnarrator = 0
#    mai "*Sob* Help me..." (name="Girl")
#    mk "Wha-What the...!?"
#    $ tbnarrator = 1
#    "Wind begins to whip through the room, and lightning crashes from the ceiling."
#    scene bg shocking with qdis
#    "Yukino is found laying on the floor."
#    $ tbnarrator = 0
#    na "Yukino!"
#    $ tbnarrator = 1
#    "Nanjo runs to help Yukino, but is stopped as lightning strikes Mark, you, and him."
#    "The remainder of the group stares at the four on the floor."
#
#    scene bg butterfly with qdis
#    play music philemon fadeout 0.5 fadein 0.5
#    "As unconsciousness sets in, a yellow butterfly flutters onto screen."
#    "It flies through a plethora of gears, buildings, and other objects."
#    "The screen stops at a large platform surrounded by four pillars."
#    scene bg philemon with qdis
#    n "A single man, clothed in a white suit and a mask with a butterfly motif, stands in the center of the platform and takes a bow."
#    $ tbnarrator = 0
#    ph "Welcome.  It's a pleasure to meet you."
#    ph "I am Philemon, a dweller between consciousness and unconsciousness."
#    ph "And now, a simple test: can you state your name?"
    show naoya at pleft2 with qdis
    mc "Naoya.  Naoya Toudou."
    ph "Splendid."
    ph "There aren't many who can remember their identity when in this domain."
    ph "It seems you passed that test."
    ph "Tell me this: are you aware of the many and varied selfs you harbor within you?"
    ph "The selves effused with divine love, and the self capable of demonic cruelty..."
    ph "People live by wearing different masks."
    ph "Your current self may be only one of those innumerable masks."
    ph "You, though... You have a very firm grip on your identity."
    ph "I respect your strong will, and in return I grant this power - \"Persona.\""
    ph "It is the power to summon the selves within you..."
    ph "...The gods and the demons you harbor."
    ph "The time is soon when you will need this power."
    ph "Now you must return to your proper time and place."
    play music "<silence .5>" fadeout 0.5
    scene bg black with qdis
    $ markx = 1000
    $ marky = 450
    $ nanjox = 925
    $ nanjoy = 425
    $ yukinox = 900
    $ yukinoy = 550
    $ npc1x = 700
    $ npc1y = 500
    "Voice" "So you guys had the same dream..."
    "Voice" "Indeed.  It's rather extraordinary."
    "Voice" "Think he's seeing it now too?"
    scene bg infirmary
    show marksprite downright stand at markloc
    show nanjosprite downright stand at nanjoloc
    show yukinosprite upright stand at yukinoloc
    show natsumisprite downright stand at npc1loc
    with qdis
    $ location = "Infirmary"
    play music schooldays volume 0.4 fadein 0.5
    show screen header with qdis
    show natsumisprite downright standmove
    show natsumi animated neutral serious with qdis
    nurse "Oh, Naoya, you've come around.  Ahaha, welcome to the infirmary."
    show natsumi animated neutral smirk
    nurse "You sure look cute when you're asleep."
    $ tbnarrator = 1
    show natsumi with qleft
    n "{color=#ebffdb}>Natsumi Yoshino\nSt. Hermelin High's nurse.  She doesn't seem to be a very good cook.{/color}"
    $ tbnarrator = 0
    hide natsumi with qdis
    show natsumisprite downright stand
    $ npc2x = 1200
    $ npc2y = 600
    show saekosprite upleft standmove at npc2loc with qdis
    show saeko animated neutral serious with qleft
    show saekosprite upright standmove with move
    sa "Naoya!  Are you all right!?  Thank goodness you're awake, Naoya!" (name="Teacher")
    show saeko animated neutral sad
    sa "I was so scared when I heard you'd collapsed!" (name="Teacher")
    show saeko
    $ tbnarrator = 1
    n "{color=#ebffdb}>Saeko Takami\nHomeroom teacher for Naoya and the others.  Very popular with the students.{/color}"
    $ tbnarrator = 0
    show saeko animated neutral smirk
    show saekosprite upleft standmove
    sa "I'm sorry you had to deal with my students, Natsumi."
    show saekosprite upleft stand
    hide saeko with qdis
    show mark animated neutral sad with qleft
    show marksprite downright standmove
    mk "C'mon, taking care of students is her whole job!  What's so bad about us...?"
    hide mark with qdis
    show marksprite downright stand
    show saeko animated neutral smirk with qleft
    show saekosprite upleft standmove
    sa "Now, now, Masao!  I want you to think about what you've done!"
    show saeko animated neutral serious
    sa "Anyway, Eriko and Ayase told me what happened."
    sa "No helping out for you today!"
    show saekosprite upright standmove
    sa "Instead, go get yourselves checked out at {color=#800000}Mikage Hospital{/color} and head home!"
    hide saeko with qdis
    show saekosprite upleft stand
    show yukino animated neutral smirk with qleft
    show yukinosprite downright standmove
    yu "So you think something's wrong with us, too?"
    hide yukino with qdis
    show yukinosprite downright stand
    show saeko animated neutral smirk with qleft
    show saekosprite upleft standmove
    sa "Oh, not like that.  I can tell by looking at you that you're perfectly sane."
    show saeko animated neutral sad
    show saekosprite upright standmove
    sa "But I'm worried you might have gotten hurt while collapsing, so go see the doc."
    hide saeko with qdis
    show saekosprite upleft stand
    show yukino animated neutral serious with qleft
    show yukinosprite downright standmove
    yu "So there is something that can faze you, Ms. Saeko... Alright, we'll go."
    hide yukino with qdis
    show yukinosprite downright stand
    show natsumi animated neutral serious with qleft
    show natsumisprite downright standmove
    show nanjosprite downleft stand
    show marksprite downleft stand
    show yukinosprite upleft stand
    nat "Speaking of Mikage Hospital, wasn't a student in your class staying there?"
    hide natsumi with qdis
    show natsumisprite downright stand
    show mark animated neutral serious with qleft
    show marksprite downleft standmove
    mk "You mean Maki, right...?"
    hide mark with qdis
    show nanjosprite downright stand
    show marksprite downright stand
    show yukinosprite downright stand
    show saeko animated neutral serious with qleft
    show saekosprite upleft standmove
    sa "Yes, that's right.  You should visit her while you're there."
    show saeko animated neutral sad
    sa "She's been laid up there for over a year now... I'm sure she's lonesome."
    hide saeko with qdis
    show saekosprite upleft stand
    $ tbnarrator = 1
    "You stand up, ready to go."
    $ tbnarrator = 0

label label001(location="Infirmary"):
    if plotprogress == 2:
        show screen header
        $ npc1x = 400
        $ npc1y = 400
        $ npc2x = 500
        $ npc2y = 400
        $ npc3x = 1200
        $ npc3y = 500
        scene bg black with qdis #update
        show saekosprite downright stand at npc2loc
        show natsumisprite downright stand at npc1loc
        show setsukosprite downleft stand at npc3loc
        #play appropriate music #update
        call screen Infirmaryb
        if _return == 1:
            $ naoyax = 450
            $ naoyay = 450
            show naoyasprite upleft stand at naoyaloc with qdis
            show natsumi animated neutral serious with qdis
            show natsumisprite downright standmove
            nat "Maki's mother isn't badly hurt.  You can relax."
            nat "What about you, Naoya?  Got any injuries?  Let me look..."
            show bg white
            pause 0.1
            hide bg white
            nat "There, all better.  Be careful out there."
        elif _return == 2:
            $ naoyax = 550
            $ naoyay = 450
            show naoyasprite upleft stand at naoyaloc with qdis
            show saeko animated neutral serious with qdis
            show saekosprite downright standmove
            sa "Masao and Kei know about the hole in the wall, right?"
            sa "The gates are sealed, so that's the only way they'll be able to get in."
        elif _return == 3:
            $ naoyax = 1150
            $ naoyay = 550
            show naoyasprite upright stand at naoyaloc with qdis
            show setsuko at pleft2 with qdis
            show setsukosprite downleft standmove
            set "I don't know what to say... I've caused so much trouble for everyone."
        elif _return == 4:
            $ naoyax = 800
            $ naoyay = 350
            show naoyasprite upright stand at naoyaloc with qdis
            ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
        elif _return == 5:
            jump callHermelinFloor1
        jump label001
    else:
        show screen header with qdis
        scene bg infirmary2
        $ markx = 1300
        $ marky = 500
        $ nanjox = 850
        $ nanjoy = 600
        $ yukinox = 1100
        $ yukinoy = 550
        $ npc1x = 700
        $ npc1y = 500
        $ npc2x = 800
        $ npc2y = 450
        with qdis
        play music schooldays volume 0.4 if_changed
        label label001TalkA:
            show screen Infirmary
            hide marksprite
            hide natsumisprite
            hide saekosprite
            hide nanjosprite
            hide yukinosprite
            call screen Infirmary
            if _return > 0:
                show yukinosprite downleft stand at yukinoloc
                show marksprite downright stand at markloc
                show nanjosprite upleft standmove at nanjoloc
                show saekosprite downright stand at npc2loc
                show natsumisprite downright stand at npc1loc
            if _return == 1:
                $ naoyax = 750
                $ naoyay = 530
                show natsumisprite downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                show natsumi animated neutral smirk with qleft
                nat "I put a new plant there.  What do you think?  Livens up the room, doesn't it?"
                nat "They say plants grow better if you talk to them.  Give it a try, Naoya."
                show natsumisprite downright stand
                hide natsumi
                hide naoyasprite
                with qdis
                $ label001natsumi = 1
            elif _return == 2:
                $ naoyax = 850
                $ naoyay = 480
                show saekosprite downright standmove at npc2loc
                show naoyasprite upleft stand behind nanjosprite at naoyaloc with qdis
                show saeko animated neutral serious with qleft
                sa "What were you doing, anyway?  I asked you to prepare for the sports festival."
                sa "We only have a month left and nothing's ready yet."
                show saeko animated neutral sad
                sa "Should we just cancel it this year...?"
                show saekosprite downright stand
                hide saeko
                hide naoyasprite
                with qdis
                $ label001saeko = 1
            elif _return == 3:
                $ naoyax = 800
                $ naoyay = 570
                show nanjosprite upleft standmove at nanjoloc
                show naoyasprite downright stand at naoyaloc
                show nanjo animated neutral serious with qleft
                na "It seems we have no choice in the matter.  Best to get it over with."
                show nanjosprite upleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label001nanjo = 1
            elif _return == 4:
                $ naoyax = 1050
                $ naoyay = 580
                show yukinosprite downleft standmove at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "I know I couldn't take being cooped up in the hospital for an entire year."
                show yukino animated neutral smirk
                yu "Let's go cheer her up!"
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label001yukino = 1
            elif _return == 5:
                $ naoyax = 1350
                $ naoyay = 530
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "Mikage Hospital, huh?  That's kind of a long walk from school."
                mk "It's way to the southeast.  You leave the school, take the subway..."
                mk "And go all the way to the 2nd ward."
                mk "Eh, if we just wander around, we'll get there sooner or later."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label001mark = 1
            elif _return == 6:
                ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
            elif _return == 7:
                jump callHermelinFloor1
            jump label001TalkA

label label002(location="Class 1-2"):
    if plotprogress >= 2:
        $ npc1x = 400
        $ npc1y = 400
        show student1sprite downleft stand at npc1loc
        scene bg black #update
        with qdis
        call screen Class12b
        if _return == 1:
            $ naoyax = 350
            $ naoyay = 450
            show naoyasprite upright stand at naoyaloc with qdis
            stu "See!?  I told you so!  SEBEC really was waging biological warfare!"
        elif _return == 2:
            jump callHermelinFloor1
        jump label002
    else:
        show screen header with qdis
        scene bg classroom with qdis
        $ yukinox = 420
        $ yukinoy = 400
        $ markx = 880
        $ marky = 350
        $ nanjox = 600
        $ nanjoy = 275
        $ npc1x = 750
        $ npc1y = 400
        play music schooldays volume 0.4 if_changed
        label label002TalkA:
            show screen Class12
            hide marksprite
            hide student7
            hide nanjosprite
            hide yukinosprite
            call screen Class12
            if _return > 0:
                show nanjosprite upleft stand at nanjoloc
                show yukinosprite downright stand at yukinoloc
                show student7 downleft stand at npc1loc
                show marksprite downright stand at markloc
            if _return == 1:
                $ naoyax = yukinox+60
                $ naoyay = yukinoy+25
                show yukinosprite downright standmove at yukinoloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show yukino animated neutral smirk with qleft
                yu "I didn't know you were this interested in rumors and gossip."
                show yukino animated neutral serious
                yu "Here's a hot tip: We need to get to the hospital!"
                show yukinosprite downright stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label002yukino = 1
            elif _return == 2:
                $ naoyax = npc1x-60
                $ naoyay = npc1y+25
                show student7 downleft standmove at npc1loc
                show naoyasprite upright stand at naoyaloc with qdis
                stu "This 'SEBEC curse' is a load of crap.  I bet they're making biological weapons."
                show student7 downleft stand
                hide naoyasprite with qdis
                $ label002astudent = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "Why's everyone so pissed at SEBEC?  It's just a regular company."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label002mark = 1
            elif _return == 4:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy+25
                show nanjosprite downleft standmove at nanjoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "I can't discount it.  Kandori is a man who wouldn't hesitate to do such things."
                show nanjosprite upleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label002nanjo = 1
            elif _return == 5:
                jump callHermelinFloor1
            jump label002TalkA

label label003(location="Class 1-3"):
    if plotprogress >= 2:
        $ npc1x = 400
        $ npc1y = 400
        scene bg black #update
        show student2sprite downleft stand at npc1loc
        with qdis
        #update music
        call screen Class13b
        if _return == 1:
            $ naoyax = 350
            $ naoyay = 450
            show naoyasprite upright stand at naoyaloc with qdis
            stu "Hey, isn't this the curse of the haunted mansion at work?"
            stu "I bet the spirits are angry that SEBEC built their HQ on top of it!"
            stu "It must be the ghost of a Sengoku-era general or something!"
        elif _return == 2:
            jump callHermelinFloor1
        jump label003
    else:
        show screen header with qdis
        scene bg classroom with qdis
        $ yukinox = 1380
        $ yukinoy = 350
        $ markx = 900
        $ marky = 660
        $ nanjox = 380
        $ nanjoy = 350
        $ npc1x = 775
        $ npc1y = 250
        play music schooldays volume 0.4 if_changed
        label label003TalkA:
            show screen Class13
            hide marksprite
            hide student8
            hide nanjosprite
            hide yukinosprite
            call screen Class13
            if _return > 0:
                show nanjosprite downright stand at nanjoloc
                show yukinosprite downleft stand at yukinoloc
                show student8 downleft stand at npc1loc
                show marksprite upright stand at markloc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy+25
                show yukinosprite downleft standmove at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious
                yu "Yeah, they tore that place down and put up the SEBEC building last year."
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label003yukino = 1
            elif _return == 2:
                $ naoyax = npc1x-60
                $ naoyay = npc1y+25
                show student8 downleft standmove at npc1loc
                show naoyasprite upright stand at naoyaloc with qdis
                stu "Did you ever hear any of those weird rumors about the SEBEC building?"
                stu "People have heard moaning and seen red eyes peering through windows..."
                stu "It's supposed to be cursed since they leveled the haunted mansion to built it."
                show student8 downleft
                hide naoyasprite with qdis
                $ label003astudent = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky-25
                show marksprite upright standmove at markloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show mark animated neutral smirk with qleft
                mk "The haunted mansion!  Man, that takes me back."
                show mark animated neutral serious
                mk "I used to go play there a lot and that old bat-- I mean my mom, got mad at me."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label003mark = 1
            elif _return == 4:
                $ naoyax = nanjox+60
                $ naoyay = nanjoy+25
                show nanjosprite downright standmove at nanjoloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "Stories about SEBEC tend to be unpleasant."
                na "That aside, we should head to the hospital."
                show nanjosprite downright stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label003nanjo = 1
            elif _return == 5:
                jump callHermelinFloor1
            jump label003TalkA

label label004(location="Class 1-4"):
    if plotprogress >= 2:
        scene bg black
        $ npc1x = 400
        $ npc1y = 400
        show student3sprite downleft stand at npc1loc
        with qdis #update
        #update music
        call screen Class14b
        if _return == 1:
            $ naoyax = 350
            $ naoyay = 450
            show naoyasprite upright stand at naoyaloc with qdis
            stu "Oh, hey!  It looks like Reiji went outside a minute ago!"
            stu "Aww... that was the perfect chance for me to talk to him!"
        elif _return == 2:
            jump callHermelinFloor1
        jump label004
    else:
        show screen header with qdis
        scene bg classroom with qdis
        $ yukinox = 875
        $ yukinoy = 575
        $ markx = 1075
        $ marky = 575
        $ nanjox = 1450
        $ nanjoy = 300
        $ npc1x = 275
        $ npc1y = 500
        play music schooldays volume 0.4 if_changed
        label label004TalkA:
            show screen Class14
            hide marksprite
            hide student6
            hide nanjosprite
            hide yukinosprite
            call screen Class14
            if _return > 0:
                show nanjosprite downright stand at nanjoloc
                show yukinosprite downright stand at yukinoloc
                show student6 downright stand at npc1loc
                show marksprite upright stand at markloc
            if _return == 1:
                $ naoyax = yukinox+60
                $ naoyay = yukinoy+25
                show yukinosprite downright standmove at yukinoloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show yukino animated neutral serious
                yu "We don't have time to deal with this nonsense.  Let's get to the hospital."
                show yukinosprite downright stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label004yukino = 1
            elif _return == 2:
                $ naoyax = npc1x+60
                $ naoyay = npc1y+25
                show student6 downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "Um, there's a guy named Reiji in your class, right?"
                stu "No matter how much I hang around your homeroom at break or after school..."
                stu "I never see him!"
                stu "How am I supposed to strike up a conversation?"
                stu "That romantic air of mystery he has... Ooooh!  But yeah..."
                show student6 downright stand
                hide naoyasprite with qdis
                $ label004astudent = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky-25
                show marksprite upright standmove at markloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show mark animated neutral serious
                mk "That girl's supposedly got a thing for Reiji... Not that I'm jealous or anything!"
                show marksprite upright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label004mark = 1
            elif _return == 4:
                $ naoyax = nanjox+60
                $ naoyay = nanjoy+25
                show nanjosprite downright standmove at nanjoloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "Reiji Kido, eh...?  He keeps to himself... I feel as though he does so deliberately."
                show nanjosprite downright stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label004nanjo = 1
            elif _return == 5:
                jump callHermelinFloor1
            jump label004TalkA

label label005(location="Class 1-6"):
    if plotprogress >= 2:
        scene bg black #update
        $ npc1x = 400
        $ npc1y = 400
        show student3sprite downleft stand at npc1loc
        with qdis
        #update music
        call screen Class16b
        if _return == 1:
            $ naoyax = 350
            $ naoyay = 450
            show naoyasprite upright stand at naoyaloc with qdis
            stu "Things have really gotten out of hand.  It's even put me off gambling."
            stu "I wonder when it'll all be over..."
            stu "Hey, wanna bet on when they'll fix it?"
        elif _return == 2:
            jump callHermelinFloor1
        jump label005
    else:
        show screen header with qdis
        scene bg classroom with qdis
        $ yukinox = 1700
        $ yukinoy = 400
        $ markx = 1350
        $ marky = 400
        $ nanjox = 1250
        $ nanjoy = 250
        $ npc1x = 700
        $ npc1y = 280
        play music schooldays volume 0.4 if_changed
        label label005TalkA:
            show screen Class16
            hide marksprite
            hide student9
            hide nanjosprite
            hide yukinosprite
            call screen Class16
            if _return > 0:
                show nanjosprite upleft stand at nanjoloc
                show yukinosprite downleft stand at yukinoloc
                show student9 downright stand at npc1loc
                show marksprite downright stand at markloc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy+25
                show yukinosprite downleft standmove at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "Let's ditch this gambling freak and go to the hospital before I lose it, okay?"
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label005yukino = 1
            elif _return == 2:
                $ naoyax = npc1x+60
                $ naoyay = npc1y+25
                show student9 downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "Gambling is a man's hobby.  And bunny-girls are a must for every casino!"
                stu "Slots, blackjack, Code Breaker..."
                stu "*sigh* I can't wait until I'm old enough to go."
                show student9 downright stand
                hide naoyasprite with qdis
                $ label005astudent = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral smirk with qleft
                mk "That dude got yelled at the other day for betting on Rich Man, Poor Man in class."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label005mark = 1
            elif _return == 4:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy-25
                show nanjosprite upleft standmove at nanjoloc
                show naoyasprite downright stand at naoyaloc with qdis
                show nanjo animated neutral smirk with qleft
                na "Code Breaker... Yes, I used to play that with Yamaoka when I was small."
                show nanjosprite upleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label005nanjo = 1
            elif _return == 5:
                jump callHermelinFloor1
            jump label005TalkA

label label006(location="Courtyard"):
    if plotprogress >=2:
        scene bg black #update courtyard bg later
        $ npc1x = 400
        $ npc1y = 400
        show student4sprite downleft stand at npc1loc
        with qdis
        #play applicable music #update
        call screen Courtyardb
        if _return == 1:
            $ naoyax = 350
            $ naoyay = 450
            show naoyasprite upright stand at naoyaloc with qdis
            stu "It's a madhouse outside, but it's so calm here... I wonder why the demons won't come here."
            stu "Could it be divine protection?"
        elif _return == 2:
            $ tbnarrator = 1
            n "{color=#ebffdb}>Hiremon Stone\nThis megalith was excavated when the school was first built in 1963."
            n "{color=#ebffdb}It's made of thamatite and possesses an abnormal magnetism.{/color}"
            n "{color=#ebffdb}Legend has it that a heavenly being known as Hiremon dropped it from the sky to be  Mikage-cho's guardian stone.{/color}"
            $ tbnarrator = 0
        elif _return == 3:
            jump callHermelinFloor1
        jump label006
    else:
        show screen header with qdis
        scene bg courtyard with qdis
        $ yukinox = 600
        $ yukinoy = 600
        $ markx = 830
        $ marky = 350
        $ nanjox = 1550
        $ nanjoy = 420
        $ npc1x = 700
        $ npc1y = 450
        $ npc2x = 1250
        $ npc2y = 460
        play music schooldays volume 0.4 if_changed
        label label006TalkA:
            show screen Courtyard
            hide marksprite
            hide student4
            hide nanjosprite
            hide yukinosprite
            call screen Courtyard
            if _return > 0:
                show nanjosprite upleft stand at nanjoloc
                show yukinosprite downleft stand at yukinoloc
                show student4 downright stand at npc1loc
                show marksprite downright stand at markloc
                show ooishisprite upright stand at npc2loc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy+25
                show yukinosprite downleft standmove at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "I have part-time work today.  Let's hurry to the hospital and get this over with."
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label006yukino = 1
            elif _return == 2:
                $ naoyax = npc1x+60
                $ naoyay = npc1y+25
                show student4 downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "Ms. Ooishi is so kind.  She loves flowers so much, she cares for them as if they were her children."
                show student4 downright stand
                hide naoyasprite with qdis
                $ label006astudent = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "Our principal's a cool lady... but she can be a little too lovey-dovey."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label006mark = 1
            elif _return == 4:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy+25
                show nanjosprite downleft standmove at nanjoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "This megalith shard... It's a very precious cultural artifact."
                na "Who built it?  For what purpose?  It never ceases to fascinate me."
                show nanjosprite upleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label006nanjo = 1
            elif _return == 5:
                $ naoyax = npc2x-60
                $ naoyay = npc2y+25
                show ooishisprite downleft standmove
                show naoyasprite upright stand at naoyaloc with qdis
                show ooishi at pleft2 with qleft
                oo "Well, hello, Naoya!  Are you all taking a walk, too?"
                oo "It's been part of my daily routine, ever since I was a girl..."
                oo "Praying to the guardian deity that everyone grows up into fine adults."
                if ooishiintro == False:
                    $ tbnarrator = 1
                    n "{color=#ebffdb}>Principal Ooishi\nThe principal of St. Hermelin High.  She adores children and flowers.{/color}"
                    $ tbnarrator = 0
                    $ ooishiintro = True
                show ooishisprite upright stand
                hide ooishi
                hide naoyasprite
                with qdis
                $ label006ooishi = 1
            elif _return == 6:
                $ naoyax = npc2x+60
                $ naoyay = npc2y+25
                show naoyasprite upright stand at naoyaloc with qdis
                $ tbnarrator = 1
                n "{color=#ebffdb}>Hiremon Stone\nThis megalith was excavated when the school was first built in 1963."
                n "{color=#ebffdb}It's made of thamatite and possesses an abnormal magnetism.{/color}"
                n "{color=#ebffdb}Legend has it that a heavenly being known as Hiremon dropped it from the sky to be  Mikage-cho's guardian stone.{/color}"
                $ tbnarrator = 0
                hide naoyasprite
                with qdis
                $ label006hiremon = 1
            elif _return == 7:
                jump callHermelinFloor1
            jump label006TalkA

label label007(location="Teacher's Lounge"):
    if plotprogress >= 2:
        scene bg black #Update with proper teacher lounge
        $ npc1x = 400
        $ npc1y = 400
        show teacher1sprite downright stand at npc1loc
        with qdis
        #play appropriate music #update
        call screen TeacherLoungeb
        if _return == 1:
            $ naoyax = 450
            $ naoyay = 450
            show naoyasprite upleft stand at naoyalock with qdis
            tea "Oh, it's you, Naoya.  Hey, go patrol around the school!"
            tea "Me? I-I can't leave this spot... I have to sort out all the reports I get!"
        elif _return == 2:
            jump callHermelinFloor1
        jump label007
    else:
        show screen header with qdis
        scene bg teacherlounge with qdis
        $ yukinox = 450
        $ yukinoy = 520
        $ markx = 840
        $ marky = 640
        $ nanjox = 1450
        $ nanjoy = 410
        $ npc1x = 670
        $ npc1y = 520
        $ ellyx = 1150
        $ ellyy = 320
        $ ayasex = 1000
        $ ayasey = 300
        play music schooldays volume 0.4 if_changed
        label label007TalkA:
            show screen TeacherLounge
            hide marksprite
            hide npcsprite
            hide nanjosprite
            hide yukinosprite
            hide ellysprite
            hide ayasesprite
            call screen TeacherLounge
            if _return > 0:
                show nanjosprite downleft stand at nanjoloc
                show yukinosprite downright stand at yukinoloc
                show npcsprite downleft stand at npc1loc
                show marksprite upright stand at markloc
                show ellysprite downleft stand at ellyloc
                show ayasesprite downright stand at ayaseloc
            if _return == 1:
                $ naoyax = yukinox+60
                $ naoyay = yukinoy+25
                show yukinosprite downright standmove at yukinoloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show yukino animated neutral sad with qleft
                yu "Eriko and Yuka didn't faint, so they don't need to go to the hospital. Why were we the only ones...?"
                show yukino animated neutral serious
                yu "Thinking about it, the ones who didn't faint had played 'Persona' before..."
                yu "Meaning Yuka, Eriko, and Hidehiko."
                show yukinosprite downright stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label007yukino = 1
            elif _return == 2:
                $ naoyax = npc1x-60
                $ naoyay = npc1y+25
                show npcsprite downleft stand at npc1loc
                show naoyasprite upright stand at naoyaloc with qdis
                tea "Oh, it's you, Naoya."
                tea "Hey, I hear someone keeps coming in and out of the open room on the second floor."
                tea "Are you the one doing it?  Hmm?"
                hide naoyasprite with qdis
                if reijiflags == 0:
                    $ reijiflags = 1
                    hide naoyasprite with qdis
                    $ label007ateacher = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky-25
                show marksprite upright standmove at markloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "A guy who keeps goin' into the open classroom on the second floor..."
                mk "You know anyone like that?"
                show marksprite upright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label007mark = 1
            elif _return == 4:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy+25
                show nanjosprite downleft standmove at nanjoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show nanjo animated neutral smirk with qleft
                na "It seems you're being mistaken for someone else, Naoya."
                show nanjosprite downleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label007nanjo = 1
            elif _return == 5:
                $ naoyax = ellyx-60
                $ naoyay = ellyy+20
                show ellysprite downleft standmove
                show naoyasprite upright stand at naoyaloc with qdis
                show elly animated neutral serious with qleft
                el "I told Ms. Saeko about what happened.  Brown seems to have already gone home..."
                show elly animated neutral smirk
                el "And I don't think Ayase could explain it coherently, do you?"
                show ellysprite downleft stand
                hide elly
                hide naoyasprite
                with qdis
                $ label007elly = 1
            elif _return == 6:
                $ naoyax = ayasex+60
                $ naoyay = ayasey+25
                show ayasesprite downright stand at ayaseloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show ayase animated neutral serious with qleft
                ay "Hidehiko took off, so me and Eriko explained everything to the teach!"
                show ayase animated neutral sad
                ay "Man, Hidehiko sure works fast at times like these."
                show ayasesprite downright stand
                hide ayase
                hide naoyasprite
                with qdis
                $ label007ayase = 1
            elif _return == 7:
                jump callHermelinFloor1
            jump label007TalkA

label label008(location="Principal's Office"):
    if plotprogress >= 2:
        scene bg black with qdis #Update Principal office here
        #play appropriate music #update
        if plotprogress == 5:
            show ooishi at pleft2 with qleft
            oo "I heard you've been looking into 'The Snow Queen.'  ...I'll tell you the whole story."
            oo "The actress portraying the Snow Queen here has traditionally worn a mask."
            oo "But there was always something unpleasant about that mask..."
            oo "Sooner or later, a rumor started that the Queen's mask was cursed."
            oo "I didn't believe it... until that day, eight years ago."
            oo "The last one to play the Snow Queen was Ms. Saeko."
            hide ooishi
            show hanya at pleft2 with qleft
            ha "M-Ma'am!  What're you saying!?"
            hide hanya
            show ooishi at pleft2 with qleft
            oo "Eight years ago... Ms. Saeko lost her best friend.  If only I'd realized it sooner..."
            oo "Had I forbidden the use of that mask, none of it would have happened."
            oo "...The mask was immediately purified and put into storage in the back room of the Gym."
            oo "But listen to me... you mustn't bring up Ms. Saeko's painful past."
            hide ooishi
            show hanya at pleft2 with qleft
            ha "H-Hey, the principal is just joking, okay?  Don't believe that junk...!"
            $ plotprogress = 6
        call screen PrincipalOfficeb
        if _return == 1:
            show ooishi at pleft2 with qleft
            if plotprogress != 6:
                oo "Naoya!  Thank goodness you're all right..."
                oo "When I think about something happening to one of my students, I worry so much."
            else:
                oo "I never want to lose another precious student. Take care of yourself, okay?"
            if ooishiintro == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Principal Ooishi\nThe principal of St. Hermelin High.  She adores children and flowers.{/color}"
                $ tbnarrator = 0
                $ ooishiintro = True
        elif _return == 2:
            show hanya at pleft2 with qleft
            if plotprogress != 6:
                ha "This is outrageous!  If something happens, they'll hold the school responsible..."
                ha "And we can kiss our careers goodbye!"
                ha "If this had just happened a little later, all the students would've gone home..."
                ha "Why is my luck so terrible!?"
            else:
                ha "Huh? You're still here? I'm busy! Get outta my sight already!"
            if hanyaintro == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Vice-Principal Hanya\nKnown as 'Hamya' among the students, who despise his extreme strictness.{/color}"
                $ tbnarrator = 0
                $ hanyaintro = True
        elif _return == 3:
            jump callHermelinFloor1
        jump label008
    else:
        show screen header with qdis
        scene bg principaloffice with qdis
        $ yukinox = 1110
        $ yukinoy = 420
        $ markx = 490
        $ marky = 440
        $ nanjox = 1410
        $ nanjoy = 500
        play music schooldays volume 0.4 if_changed
        label label008TalkA:
            show screen PrincipalOffice
            hide marksprite
            hide nanjosprite
            hide yukinosprite
            call screen PrincipalOffice
            if _return > 0:
                show nanjosprite downleft stand at nanjoloc
                show yukinosprite upright stand at yukinoloc
                show marksprite downright stand at markloc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy+25
                show yukinosprite downleft stand at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "Wow, these flowers are beautiful... So it's true about the principal, huh?"
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label008yukino = 1
            elif _return == 2:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "Looks like the principal isn't here.  She's probably in the courtyard again..."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label008mark = 1
            elif _return == 3:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy+25
                show nanjosprite downleft standmove at nanjoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "Snooping around is all well and good, but let's not forget the hospital."
                show nanjosprite downleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label008nanjo = 1
            elif _return == 4:
                jump callHermelinFloor1
            jump label008TalkA

label label009(location="1F Passageway"):
        show screen header with qdis
        scene bg 1FPassageway with qdis
        $ yukinox = 720
        $ yukinoy = 670
        $ markx = 540
        $ marky = 590
        $ nanjox = 980
        $ nanjoy = 620
        $ npc1x = 1200
        $ npc1y = 480
        play music schooldays volume 0.4 if_changed
        label label009TalkA:
            show screen Passageway1F
            hide marksprite
            hide npcsprite
            hide nanjosprite
            hide yukinosprite
            call screen Passageway1F
            if _return > 0:
                show nanjosprite upleft stand at nanjoloc
                show yukinosprite upright stand at yukinoloc
                show marksprite downright stand at markloc
                show hanyasprite upright stand at npc1loc
            if _return == 1:
                $ naoyax = yukinox+60
                $ naoyay = yukinoy-25
                show yukinosprite upright stand at yukinoloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "Tch... Isn't there one decent teacher here besides Ms. Saeko and the principal?"
                show yukinosprite upright stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label009yukino = 1
            elif _return == 2:
                $ naoyax = npc1x-60
                $ naoyay = npc1y+25
                show hanyasprite downleft standmove at npc1loc
                show naoyasprite upright stand at naoyaloc with qdis
                show hanya at pleft2 with qleft
                ha "Who told you kids that you could go through here?"
                ha "If you want to get outside, the school gates are there for a reason!"
                ha "Our school's swarming with degenerates like you!"
                ha "Ooishi is far too lenient!  Now get outta here!"
                ha "I'm going to call a specialist and have this blocked off!"
                if hanyaintro == False:
                            $ tbnarrator = 1
                            n "{color=#ebffdb}>Vice-Principal Hanya\nKnown as 'Hamya' among the students, who despise his extreme strictness.{/color}"
                            $ tbnarrator = 0
                            $ hanyaintro = True
                show hanyasprite downleft stand
                hide hanya
                hide naoyasprite
                with qdis
                $ label009hanya= 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral serious with qleft
                mk "Urgh, it's Hamya.  I hate that guy... Cheese it, Naoya!"
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label009mark = 1
            elif _return == 4:
                $ naoyax = nanjox-60
                $ naoyay = nanjoy-25
                show nanjosprite upleft standmove at nanjoloc
                show naoyasprite downright stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "What's the matter?  Are the school gates closed?"
                na "If we don't hurry, visiting hours at the hospital might end."
                show nanjosprite upleft stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label009nanjo = 1
            elif _return == 5:
                jump callHermelinFloor1
            elif _return == 6:
                jump callSportsBuilding
            jump label009TalkA

label label011(location="Gymnasium"):
    if plotprogress == 6:
        scene bg black with qdis #update
        call screen Gymnasiumc
        if _return == 1:
            stu "This fuss'll die down by the time the festival starts, right?"
            stu "It'd suck if the school festival was cancelled in all this chaos!"
        elif _return == 2:
            jump SnowQueenMask
        elif _return == 3:
            jump callSportsBuilding
    if plotprogress >= 2:
        if plotprogress =< 5:
            scene bg black with qdis #update
            #play appropriate music #update
            call screen Gymansiumb
            if _return == 1:
                stu "This fuss'll die down by the time the festival starts, right?"
                stu "It'd suck if the school festival was cancelled in all this chaos!"
            elif _return == 2:
                jump callSportsBuilding
            jump label011
    else:
        show screen header with qdis
        scene bg gym with qdis
        $ yukinox = 760
        $ yukinoy = 850
        $ markx = 810
        $ marky = 580
        $ nanjox = 600
        $ nanjoy = 770
        $ npc1x = 1500
        $ npc1y = 370
        $ npc2x = 550
        $ npc2y = 430
        play music schooldays volume 0.4 if_changed
        label label011TalkA:
            show screen Gymnasium
            hide marksprite
            hide student1
            hide student3
            hide nanjosprite
            hide yukinosprite
            call screen Gymnasium
            if _return > 0:
                show nanjosprite upright stand at nanjoloc
                show yukinosprite upright stand at yukinoloc
                show marksprite downright stand at markloc
                show student1 downleft stand at npc1loc
                show student3 downright stand at npc2loc
            if _return == 1:
                $ naoyax = yukinox+60
                $ naoyay = yukinoy-25
                show yukinosprite upright stand at yukinoloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "Can we hurry and get to the hospital yet?"
                show yukinosprite upright stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label011yukino = 1
            elif _return == 2:
                $ naoyax = npc2x+60
                $ naoyay = npc2y+25
                show student3 downright stand at npc2loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "I heard a second-year named Yosuke went missing along with his girlfriend..."
                stu "It's SEBEC's doing, if you ask me!\nHuh?  Proof...?  It's just male intuition!"
                show student3 downright stand
                hide naoyasprite
                with qdis
                $ label011astudent2 = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral smirk with qleft
                mk "This place would be great for practicin' dance moves if it had a big mirror."
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label011mark = 1
            elif _return == 4:
                $ naoyax = nanjox+60
                $ naoyay = nanjoy-25
                show nanjosprite upright standmove at nanjoloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "I don't have many ties with the gym, of course.  I suppose I can let it slide."
                show nanjosprite upright stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label011nanjo = 1
            elif _return == 5:
                $ naoyax = npc1x-60
                $ naoyay = npc1y+25
                show student1 downleft stand at npc1loc
                show naoyasprite upright stand at naoyaloc with qdis
                stu "The sound system's all good to go in the new gym!  The concert's gonna be bitchin'!"
                stu "I'm gonna skip Sports Day and hole up in the studio to practice!"
                show student1 downleft stand
                hide naoyasprite
                with qdis
                $ label011astudent1 = 1
            elif _return == 6:
                jump callSportsBuilding
            jump label011TalkA

label label012(location="Drama Club"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        if plotprogress == 3:
            stu "I told you, I don't know any play called 'The Snow Queen'!  Give it a rest!"
            pause 1.0
            stu "If there were any records left, you might be able to find something in them..."
            stu "You can check with the Student Council up on the third floor.  They should have them."
            $ plotprogress = 4
        call screen DramaClubb
        if _return == 1:
            if plotprogress != 4:
                stu "This is hardly the time to be thinking about the school festival."
            else:
                stu "I told you, I don't know any play called 'The Snow Queen'!  Give it a rest!"
        elif _return == 2:
            stu "Our president's the only one who knows about that play."
            stu "Huh?  What play?  Oh, uh... it's a secret."
        elif _return == 3:
            if plotprogress != 4:
                stu "Man, this sucks.  What's up with this?"
            else:
                stu "If there were any records left, you might be able to find something in them..."
                stu "You can check with the Student Council up on the third floor.  They should have them."
        elif _return == 4:
            jump callSportsBuilding
        jump label012
    if plotprogress == 2:
        scene bg black with qdis #update
        #play music #update
        call screen DramaClubb
        if _return == 1:
            stu "This is hardly the time to be thinking about the school festival."
        elif _return == 2:
            stu "Our president's the only one who knows about that play."
            stu "Huh?  What play?  Oh, uh... it's a secret."
        elif _return == 3:
            stu "Man, this sucks.  What's up with this?"
        elif _return == 4:
            jump callSportsBuilding
        jump label012
    else:
        $ yukinox = 1320
        $ yukinoy = 500
        $ markx = 550
        $ marky = 520
        $ nanjox = 880
        $ nanjoy = 640
        $ npc1x = 820
        $ npc1y = 450
        $ npc2x = 940
        $ npc2y = 460
        $ npc3x = 760
        $ npc3y = 520
        scene bg dramaclub with qdis
        play music schooldays volume 0.4 if_changed
        if dramaclub == False:
            show nanjosprite upright stand at nanjoloc
            show yukinosprite downleft stand at yukinoloc
            show marksprite downright stand at markloc
            show student4 downright stand at npc1loc
            show student6 downleft stand at npc2loc
            show student3 upright standmove at npc3loc
            stu "Hey, we haven't decided which play we're doing for the culture festival, have we?"
            stu "I heard there was a traditional play we used to perform... Why not do that?"
            stu "I think it was called The Snow--"
            show student3 upright stand
            show student4 downright standmove
            stu "Absolutely not!  That one's off limits.  I'll decide soon... Give me some time."
            $ dramaclub = True
        show screen header with qdis
        label label012TalkA:
            show screen DramaClub
            hide marksprite
            hide makisprite
            hide student4
            hide student6
            hide student3
            hide yukinosprite
            call screen DramaClub
            if _return > 0:
                show nanjosprite upright stand at nanjoloc
                show yukinosprite downleft stand at yukinoloc
                show marksprite downright stand at markloc
                show student4 downright stand at npc1loc
                show student6 downleft stand at npc2loc
                show student3 upright stand at npc3loc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy+25
                show yukinosprite downleft stand at yukinoloc
                show naoyasprite upright stand at naoyaloc with qdis
                show yukino animated neutral serious with qleft
                yu "The school has a traditional play?  News to me."
                show yukinosprite downleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label012yukino = 1
            elif _return == 2:
                $ naoyax = npc1x+60
                $ naoyay = npc1y+25
                show student4 downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "Hm?  Are you interested in joining the club?  If not, please leave.  You're in our eye lines."
                show student4 downright stand
                hide naoyasprite
                with qdis
                $ label012astudent1 = 1
            elif _return == 3:
                $ naoyax = markx+60
                $ naoyay = marky+25
                show marksprite downright standmove at markloc
                show naoyasprite upleft stand at naoyaloc with qdis
                show mark animated neutral smirk with qleft
                mk "Who needs a play?  Just lemme bust a move up on stage!"
                show marksprite downright stand
                hide mark
                hide naoyasprite
                with qdis
                $ label012mark = 1
            elif _return == 4:
                $ naoyax = nanjox+60
                $ naoyay = nanjoy-25
                show nanjosprite upright standmove at nanjoloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "Snow...?  Was he going to suggest The Snow Queen?"
                show nanjosprite upright stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label012nanjo = 1
            elif _return == 5:
                $ naoyax = npc2x-60
                $ naoyay = npc2y+25
                show student6 downleft standmove at npc2loc
                show naoyasprite upright stand at naoyaloc with qdis
                stu "St. Hermelin won the drama concours nine years ago, too... But the trophy from that year is missing."
                stu "I wonder what happened to it."
                show student6 downleft stand
                hide naoyasprite
                with qdis
                $ label012astudent2 = 1
            elif _return == 6:
                $ naoyax = npc3x+60
                $ naoyay = npc3y-25
                show student3 upright standmove at npc3loc
                show naoyasprite downleft stand at naoyaloc with qdis
                stu "The president seemed a little touchy... Why did she get so upset?"
                show student3 upright stand
                hide naoyasprite
                with qdis
                $ label012astudent3 = 1
            elif _return == 7:
                jump callSportsBuilding
            jump label012TalkA

label label013(location="Boxing Club"):
    if plotprogress >= 2:
        n "It appears to be empty.  Maybe they've all gone home?"
        jump callSportsBuilding
    else:
        $ yukinox = 1320
        $ yukinoy = 500
        $ markx = 1100
        $ marky = 400
        $ nanjox = 880
        $ nanjoy = 640
        $ npc1x = 950
        $ npc1y = 400
        scene bg boxingclub with qdis
        play music schooldays volume 0.4 if_changed
        show screen header with qdis
        label label013TalkA:
            show screen BoxingClub
            hide marksprite
            hide nanjosprite
            hide student7
            hide yukinosprite
            call screen BoxingClub
            if _return > 0:
                show nanjosprite upright stand at nanjoloc
                show yukinosprite upleft stand at yukinoloc
                show marksprite upright stand at markloc
                show student7 downright stand at npc1loc
            if _return == 1:
                $ naoyax = yukinox-60
                $ naoyay = yukinoy-25
                show yukinosprite upleft stand at yukinoloc
                show naoyasprite downright stand at naoyaloc with qdis
                show yukino animated neutral sad with qleft
                yu "...I could lose some weight myself..."
                show yukinosprite upleft stand
                hide yukino
                hide naoyasprite
                with qdis
                $ label013yukino = 1
            elif _return == 2:
                $ naoyax = npc1x+60
                $ naoyay = npc1y+25
                show student7 downright standmove at npc1loc
                show naoyasprite upleft stand at naoyaloc with qdis
                stu "I'm trying to lose weight.  Even the boxing gloves are starting to look like candy..."
                show student7 downright stand
                hide naoyasprite
                with qdis
                $ label013astudent1 = 1
            elif _return == 3:
                $ naoyax = markx-60
                $ naoyay = marky+25
                show marksprite downleft standmove at markloc
                show naoyasprite upright stand at naoyaloc with qdis
                show mark animated neutral smirk with qleft
                mk "Boxing is so cool!  It looks like it would hurt, though."
                show marksprite downleft stand
                hide mark
                hide naoyasprite
                with qdis
                $ label013mark = 1
            elif _return == 4:
                $ naoyax = nanjox+60
                $ naoyay = nanjoy-25
                show nanjosprite upright standmove at nanjoloc
                show naoyasprite downleft stand at naoyaloc with qdis
                show nanjo animated neutral serious with qleft
                na "You want to join the boxing club?  Well, let's get examined before that."
                show nanjosprite upright stand
                hide nanjo
                hide naoyasprite
                with qdis
                $ label013nanjo = 1
            elif _return == 5:
                jump callSportsBuilding
            jump label013TalkA

label label014(location="Archery Club"):
    if plotprogress >= 2:
        n "It appears to be empty.  Maybe they've all gone home?"
        jump callSportsBuilding
    else:
        scene bg archeryclub with qdis
        play music schooldays2 if_changed
        call screen ArcheryClub
        if _return == 1:
            show yukino animated neutral smirk with qleft
            yu "Bows and arrows aren't my thing.  I prefer razor blades."
        elif _return == 2:
            stu "Archery is an intelligent, mature sport!  Don't have a bow? We'll lend you one!"
        elif _return == 3:
            show mark animated neutral serious with qleft
            mk "I heard there's a bunch of bows here.  I think I'll borrow one and mess around with it next time."
        elif _return == 4:
            show nanjo animated neutral serious with qleft
            na "I agree, archery is interesting... But don't forget to go to the hospital."
        elif _return == 5:
            jump callSportsBuilding
        jump label014

label label015(location="Fencing Club"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #music #update
        if fencingclub == False:
            show tadashi at pleft2 with qleft
            td "Oh, hey Naoya!  How's it looking out there?  You went outside, right?"
            td "Is that cueball still running the shop?"
            hide tadashi
            show tamaki animated neutral serious with qleft
            tm "What's the matter, you scared?  Go see for yourself, fraidy cat!"
            hide tamaki
            show tadashi at pleft2 with qleft
            td "Wh-What the hell... I ain't s-scared of those demons!"
            td "You're scarier than they are, you muscley freak!"
            hide tadashi
            show tamaki animated neutral serious with qleft
            tm "What did you call me, fraidy cat!?  Fraidy cat, fraidy cat, fraidy cat!"
            hide tamaki
            show tadashi at pleft2 with qleft
            td "Argh!  Stupid muscley freak!  Muscley freak, mussel fr--damn, that's hard to say."
            hide tadashi with qdis
        call screen FencingClubb with qdis
        if _return == 1:
            if tamakirapier == True:
                show tamaki animated neutral smirk with qleft
                tm "Remember, Naoya.  Some demons are okay."
                tm "Defeating them isn't the only way to get things done."
            elif tamakirapier == False:
                show tamaki animated neutral serious with qleft
                tm "*pant* *pant* ...Hey, Naoya.  This is for you."
                show tamaki animated neutral sad
                tm "I used it at my last school for... stuff..."
                tm "I get the feeling this one's yours, not mine..."
                $ tamakirapier = True
        elif _return == 2:
            show tadashi at pleft2 with qleft
            td "*pant* *pant* She's seriously a piece of work, isn't she, Naoya?"
        elif _return == 3:
            stu "It felt like a usual day, with the usual argument..."
            stu "...but something's very wrong."
        elif _return == 4:
            stu "Tamaki's amazing.  She knew the names of every demon we saw out the window!"
            stu "She was going on about which ones were useful, and which ones were antisocial..."
            stu "Wait, does that mean demons can join our side?  Huh?"
        elif _return == 5:
            jump callSportsBuilding
        jump label015
    else:
        scene bg fencingclub with qdis
        play music schooldays2 if_changed
        if fencingclub == False:
            show tamaki animated neutral serious with qleft
            tm "Tadashi, you idiot! Why do you keep messing up the club room!?"
            show tamaki ns
            $ tbnarrator = 1
            n "{color=#ebffdb}>Tamaki\nA transfer student who joined the Fencing Club.  She's always arguing with Tadashi.{/color}"
            $ tbnarrator = 0
            hide tamaki
            show tadashi at pleft2 with qleft
            td "Laa la laa!  I'm not listeniiiiing!  We can do whatever we want."
            td "Sheesh, Tamaki, who pissed in your cornflakes this morning?"
            $ tbnarrator = 1
            n "{color=#ebffdb}>Tadashi\nA lazy member of the Fencing Club who quarrels with Tamaki every day.{/color}"
            $ tbnarrator = 0
            hide tadashi
            show tamaki animated neutral serious with qleft
            tm "What did you say!?  I'm gonna rip this trash off the walls right now!"
            hide tamaki
            show tadashi at pleft2 with qleft
            td "Hey!  What're you doing to my goddess!?"
            hide tadashi
            show tamaki animated neutral serious with qleft
            tm "'Goddess' my ass, you pervert!  You're the perviest pervert to ever perv!"
            hide tamaki
            show tadashi at pleft2 with qleft
            td "Arrrgh!  You hag!  You're a haggity hag who hags all hagging day!"
            $ fencingclub = True
            hide tadashi
            $ tbnarrator = 1
            ". . ."
            $ tbnarrator = 0
        call screen FencingClub with qdis
        if _return == 1:
            show yukino animated neutral smirk with qleft
            yu "Leave 'em alone.  You know how some people are.  They fight 'cause they care."
        elif _return == 2:
            show mark animated neutral serious with qleft
            mk "What a half-ass job... If you're gonna bomb a wall, you gotta do it with more style."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Honestly, the idiots populating our sports club... It's all a bit much."
        elif _return == 4:
            show tamaki animated neutral serious with qleft
            tm "*gasp* *gasp* What is it?  I'm a little busy here."
        elif _return == 5:
            show tadashi at pleft2 with qleft
            td "*gasp* *gasp* Yeah?  I'm kinda busy here."
        elif _return == 6:
            stu "Tamaki's a transfer student, but she's good enough to place in tournaments."
            stu "But she never wants to talk about her last school... Did something happen?."
        elif _return == 7:
            stu "*sigh* These two are like this every day.  I'm surprised they're not tired of it."
        elif _return == 8:
            jump callSportsBuilding
        jump label015

label label016(location="Ballet Club"):
    if plotprogress >= 2:
        n "It appears to be empty.  Maybe they've all gone home?"
        jump callSportsBuilding
    else:
        scene bg balletclub with qdis
        play music schooldays2 if_changed
        call screen BalletClub with qdis
        if _return == 1:
            show yukino animated neutral smirk with qleft
            yu "Ballet, huh...?  The Nutcracker is kinda neat, I always thought."
            yu "A fun dream world the girl saw on Christmas Eve...*dreamy sigh*"
            show yukino animated neutral serious
            yu "Hey, what's that look for!?  I happen to like ballet!  Something wrong with that!?"
        elif _return == 2:
            show mark animated neutral serious with qleft
            mk "I get fidgety around this stuff.  C'mon, let's go to the hospital!"
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "Yamaoka used to take me to the ballet when I was small..."
            na "I suppose he was trying to cultivate my aesthetic sensibilities."
        elif _return == 4:
            stu "It was nice when they rebuilt the gym and we finally got our own room."
            stu "Back when we had to change in the classrooms, someone could have seen us!"
            stu "Wait!  Were you one of the pervs doing that!?"
        elif _return == 5:
            stu "Did you know toe shoes are actually really hard?  I was pretty surprised the first time I put on a pair."
        elif _return == 6:
            jump callSportsBuilding
        jump label016

label label018(location = "Class 2-1"):
    if plotprogress >= 2:
        n "It appears to be locked."
        jump callHermelinFloor2
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        call screen Class21
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Hey Naoya, you gotta hear the stupid junk this guy is spouting."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "What's Masao's beef with that guy?  I don't see what the fuss is about."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Say, what about the hospital?  Weren't we going there for a checkup?"
        elif _return == 4:
            stu "Don't you think derelict buildings should be torn down? Places like that only attract hooligans--" (Name="Serious student")
            show mark animated neutral smirk with qleft
            mk "Haha!  'Hooligans'?  Seriously?  What a poindexter!"
            hide mark with qdis
            stu "Won't you pipe it down!?  As I was saying, wouldn't it attract hooligans?"
            stu "I'd certainly hate to see that happen." (Name="Serious student")
            $ reijifactory = True
        elif _return == 5:
            jump callHermelinFloor2
        jump label018

label label019(location="Class 2-2"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen Class22b
        if _return == 1:
            stu "So that dream was a sign..."
            stu "But the blue room doesn't seem to be related to this."
        elif _return == 2:
            jump callHermelinFloor2
        jump label019
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        call screen Class22
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "A blue room... Y'know, I feel like I had a dream like that too."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Remember, there's a girl at the hospital who wants to talk to you, too."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Dreams have no meaning.  They're dreams, nothing more."
        elif _return == 4:
            stu "I had a weird dream.  It's really been bothering me..."
            $ choicetext = "Do you want to hear about it?"
            show nchoice at pright zorder 15 with easeinright
            show nchoice onlayer screens zorder 15 at pright
            show fadeblack onlayer screens zorder 3 with qdis
            $ choice1 = "Yes"
            $ choice2 = "No"
            call screen choices with qdis
            if _return == 1:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                stu "It takes place in a blue room."
                stu "I can hear a piano and singing, and there's an odd old man sitting down..."
                stu "What do you think that means?"
                jump label019
            if _return == 2:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                stu "It was a really strange dream... like it was hinting at something that'll happen."
        elif _return == 5:
            jump callHermelinFloor2
        jump label019

label label020(location="Class 2-4"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen Class24b
        if _return == 1:
            stu "Devil-Boy says this town got all weird because of a curse on St. Hermelin."
            stu "I don't think now is the time for that... Though it's admirable in its own way."
        elif _return == 2:
            jump callHermelinFloor2
        jump label020
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        if Yuko == False:
            show yuko at pleft2 with qleft
            stu "Um...Naoya?  You're going to the hospital, right..?"
            $ tbnarrator = 1
            n "{color=#ebffdb}>Yuko Himeno\nMaki's friend.  She works part-time to support her family.{/color}"
            $ tbnarrator = 0
            yuko "Um, I hate to ask, but..."
            $ lines = 2
            $ choicetext = "Could you tell Maki I'll give back\nthat book next time I go visit her...?"
            show nchoice at pright zorder 15 with easeinright
            show nchoice onlayer screens zorder 15 at pright
            show fadeblack onlayer screens zorder 3 with qdis
            $ choice1 = "Sure"
            $ choice2 = "No way"
            call screen choices with qdis
            if _return == 1:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                yuko "U-um, thanks.  I'm sorry to ask you to go out of your way like that..."
            if _return == 2:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                yuko "O-Oh... Um, sorry I asked... It's okay, don't worry about it...!"
                hide yuko
                show yukino animated neutral serious with qleft
                yu "Naoya!  Don't be such an asshole!"
                hide yukino
            show yuko at pleft2 with qleft
            yuko "It was a really good book, so I wanted to read it again before I return it..."
            hide naoya
            hide yuko
            show mark animated neutral smirk with qleft
            mk "That good, huh?  What's it called?"
            hide mark
            show yuko at pleft2 with qleft
            yuko "U-Um, 'Gate to Paradise'..."
            hide yuko
            show mark animated neutral serious with qleft
            mk "Whoa, that's deep!  I didn't know Maki was into that kinda thing..."
            hide mark
            show nanjo animated neutral serious with qleft
            na "If you enjoyed it that much, why not simply buy your own copy?"
            hide nanjo
            show yuko at pleft2 with qleft
            yuko "W-Well... It's kind of expensive... and my brothers and sisters need new clothes."
            hide yuko
            show yukino animated neutral serious with qleft
            yu "Nanjo, you moron!  Don't you know she works part-time to help her family out?"
            hide yukino
            show mark animated neutral serious with qleft
            mk "Alright, well, we gotta get goin', but we'll be sure to pass on your message!"
            $ Yuko = True
            $ lines = 1
            hide mark with qdis
            jump callHermelinFloor2
        else:
            show yuko at pleft2 with qleft
            yuko "U-Um... Did you tell Maki...?"
            hide yuko
            show yukino animated neutral sad with qleft
            yu "Uh, sorry, not yet.  But we're going soon, promise."
            show yukino animated neutral serious
            yu "...Hey, Naoya! Let's get to the hospital already!"
            hide yukino with qdis
            jump callHermelinFloor2

label label021(location="Class 2-5"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #music #update
        call screen Class25b
        if _return == 1:
            stu "Hey, the principal was right after all about the guardian of this school!"
            stu "I mean, not a single demon has gotten in here yet, right?"
        if _return == 2:
            stu "Won't she shut up...?"
            stu "All that crap about guardians and demons...She's dreaming."
        if _return == 3:
            jump callHermelinFloor2
        jump label021
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        call screen Class25
        if _return == 1:
            show mark animated neutral sad with qleft
            mk "Hey Naoya, we're still going to the hospital, right?"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Yuka seems like an airhead, but I think sometimes she's working at it."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Does this woman never stop running her mouth...?"
        elif _return == 4:
            stu "Hey, where's Ayase?  Wasn't she with you?  She promised to go out, but she totally ditched."
            stu "I'm thinking I might like, just go ahead on my own."
            stu "It's really weird, though!  She seemed totally into it!  Ayase gets like this sometimes..."
            stu "She acts all, like, cynical and stuff.  I don't understand that girl."
        elif _return == 5:
            stu "Are you guys going to the hospital on the Second Ward?"
            stu "It's a pretty long walk... Good luck with that."
        elif _return == 6:
            jump callHermelinFloor2
        jump label021

label label022(location="Cafeteria"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen Cafeteriab
        if _return == 1:
            show toro at pleft2 with qleft
            tor "I'm scared of the demons, but I think this might be my chance!"
            tor "If I prove to Ayase how macho I am... She... she might l-like me... right?"
            if toro == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Kenta Yokouchi (Nickname: Toro)\nHis love of food has made him physically strong, but emotionally fragile.{/color}"
                $ tbnarrator = 0
                $ toro = True
        elif _return == 2:
            stu "Something's up with Toro.  You can see it in his eyes..."
            stu "Guess he's still hung up on Ayase.  His type is scary when they can't let go."
        elif _return == 3:
            jump callHermelinFloor2
        jump label022
    else:
        scene bg cafeteria with qdis
        play music schooldays2 if_changed
        call screen Cafeteria
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Toro's got balls, man!  I mean, asking out Ayase!?  Dude... I wouldn't go after her in a million years!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I hate guys who see someone who's serious about something and just make fun of it."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I believe I've asked this before, but shouldn't we be going to the hospital?"
        elif _return == 4:
            show toro at pleft2 with qleft
            tor "I-I had a weird dream!  There was his girl, and she was saying, 'Help me...'"
            tor "Was it a vision?  Is there really a girl waiting for me to rescue her?  W-Wow... that's awesome..."
            if toro == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Kenta Yokouchi (Nickname: Toro)\nHis love of food has made him physically strong, but emotionally fragile.{/color}"
                $ tbnarrator = 0
                $ toro = True
        elif _return == 5:
            stu "Dude, guess what I saw!  Toro asked out Ayase and got rejected on the spot!"
            stu "I hear he's still following her around, though."
        elif _return == 6:
            jump callHermelinFloor2
        jump label022

label label023(location="Home Ec Room"):
    if plotprogress >= 2:
        n "It seems to be locked."
        jump callHermelinFloor2
    else:
        scene bg homeecroom with qdis
        play music schooldays2 if_changed
        call screen HomeEcRoom
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Yosuke's handsome and a nice guy.  I hate to admit it, but he's hard to beat!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I was surprised too when Chisato started dating Yosuke.  It was so sudden..."
            show yukino animated neutral sad
            yu "Chisato never acted like she cared about him before.  Actually, I always thought Ma--"
            show yukino animated neutral serious
            yu "Hey, shouldn't we get going?"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "It's true that not even I think Chisato has an especially attractive personality."
            na "It seemed as if she was dating Yosuke to show off as much as anything."
        elif _return == 4:
            stu "Uh, isn't it time you gave up on Yosuke?  He obviously ran off with his girlfriend!"
            stu "C'mon, it's been two months already!"
            stu "That's a lie!  That Chisato bitch tricked him!  Everyone knows that girl's bad news!"
        elif _return == 5:
            jump callHermelinFloor2
        jump label023

label label024: #Empty Classroom (Reiji)
    if reijiflags != 1:
        "The door is locked..."
        jump callHermelinFloor2
        with pixellate
    if reijiflags == 1:
        scene bg emptyclassroom1 with qdis
        play music reiji fadeout 0.5 fadein 0.5
        $ location = "Empty Classroom"
        show yukino animated neutral serious with qleft
        yu "...Someone's there."
        hide yukino
        show mark animated neutral serious with qleft
        mk "Huh?  Reiji?  You're Reiji Kido!  What're you doin' here?"
        hide mark
        show reiji at pleft2 with qleft
        re "..."
        $ tbnarrator = 1
        n "{color=#ebffdb}>Reiji Kido (Nickname: Reiji)\nA quiet loner who transferred to St. Hermelin High six months ago.{/color}"
        "Reiji leaves without saying anything further."
        $ tbnarrator = 0
        scene bg emptyclassroom2 with qdis
        show nanjo animated neutral serious with qleft
        na "Hmph.  The standoffish sort, I see."
        hide nanjo
        show mark animated neutral sad with qleft
        mk "Look who's talking..."
        $ reijiflags = 2
        hide mark with qdis
label label017: #Reiji after convo
    call screen EmptyClass
    play music schooldays2 fadeout 0.5 fadein 0.5
    if _return == 1:
        show mark animated neutral smirk with qleft
        mk "What a gloomy Gus!  But hey, for all we know..."
        mk "Maybe he's the kinda guy who secretly practices magic tricks at home."
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "Reiji transferred here soon after the SEBEC Building was constructed..."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "I wonder what he was pondering at a place like this..."
    elif _return == 4:
        jump callHermelinFloor2
    jump label017

label label026 (location="Class 3-1"):
    if plotprogress >= 2:
        n "It seems to be locked."
        jump callHermelinFloor3
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        if label026 == False:
            stu "Nurse Natsumi is hot as hell!  I love that mature air she has..."
            stu "Oh, reaaaaally!?  Then why don't you have her pack your lunches from now on?"
            stu "Urk!  P-Please... not that... I'm sorry!  I shouldn't have said anything!"
            $ label026 = True
        call screen Class31
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Guys our age tend to go for older women."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Seriously, guys, the sun's going down.  Are we going to the hospital or not?"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I'm not interested in this sort of foolishness."
        elif _return == 4:
            stu "Even if she's a bad cook, you could just live off convenience store food."
        elif _return == 5:
            stu "That reminds me, I heard Nurse Natsumi just had a breakup. I wonder why?"
        elif _return == 6:
            jump callHermelinFloor3
        jump label026

label label027 (location="Class 3-3"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen Class33b
        if _return == 1:
            stu "This place is definitely cursed!  It must be the curse of the haunted mansion!"
            stu "It should've just affected SEBEC, but nooo... We had to get dragged in too."
            stu "Ugh, honestly!  What a pain!"
        elif _return == 2:
            stu "I know there are demons outside, but I'm getting really hungry..."
            stu "Maybe I could duck out for a bite using that secret shortcut."
            stu "...Nah, too scary."
        elif _return == 3:
            jump callHermelinFloor3
        jump label027
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        call screen Class33
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "A secret shortcut...?  Oh, he must mean the hole in the wall."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Looks like SEBEC's reputation is at an all-time low."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Stuff and nonsense.  Curses are nothing more than superstition."
        elif _return == 4:
            stu "Like, no way am I gonna walk by the SEBEC building at night."
            stu "That company's been cursed ever since they tore down the haunted mansion!"
        elif _return == 5:
            stu "I'm hungry... I'm gonna get a snack.  It'll be easy if I use the secret shortcut!"
            stu "You should give it a try, too!"
        elif _return == 6:
            jump callHermelinFloor3
        jump label027

label label028 (location="Class 3-6"):
    if plotprogress >= 2:
        n "It seems to be locked."
        jump callHermelinFloor3
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        call screen Class36
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "The police station's straight south from here, right?"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Huh.  There's other trees like that one in the infirmary...?"
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "You quite enjoy idling the time away with frivolity, don't you?"
            show nanjo animated neutral serious
            na "At this rate, the sun will have set before our examinations are through."
        elif _return == 4:
            stu "I saw a beautiful tree in the forest east of the station."
            stu "It looked exactly like the one Nurse Natsumi put in the infirmary."
            stu "I feel at peace when I look at that tree... It's the strangest thing."
        elif _return == 5:
            jump callHermelinFloor3
        jump label028

label label029 (location="Class 3-7"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen Class37b
        if _return == 1:
            stu "Awesome!  Now I don't have to go to cram school!"
            stu "Oh, but I can't go home, either..."
            stu "If there was an exit that wasn't guarded, I could just slip out quietly."
        elif _return == 2:
            stu "Doesn't that idiot get what kind of troublewe're in!?"
            stu "Forget the entrance exams!  We could die here!"
        elif _return == 3:
            jump callHermelinFloor3
        jump label029
    else:
        scene bg classroom with qdis
        play music schooldays volume 0.4 if_changed
        if label029 == False:
            stu "I don't wanna go to cram school.  I just wanna stay home and sleep."
            stu "You can't!  You need to study.  Let's go together, okay?"
            stu "Why don't we meet at the subway entrance?"
            stu "The subway... That's just due South from here, yeah?"
            $ label029 = True
        call screen Class37
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Hey, we're not supposed to be in here.  Let's just go to the hospital."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "You thought about what to do after grad?  College isn't in my plans."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "We'll be preparing for our college entrance exams soon."
            show nanjo animated neutral smirk
            na "Naturally, I plan to pass with top marks and enter the college of my choice."
        elif _return == 4:
            stu "You're supposed to be able to see your future self when you play 'Persona.'"
            stu "I wonder if I should try it... Will I be in college this time next year?"
        elif _return == 5:
            stu "Oh, give me a break!  If you have time to play that 'Persona' game, you have time to study!"
            stu "Moron... you promised we'd go to the same college together!"
        elif _return == 6:
            jump callHermelinFloor3
        jump label029

label label030 (location="Library"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #playmusic #update
        if plotprogress == 2:
            show devilboy animated neutral serious with qleft
            db "You know of 'The Snow Queen,' right?  Yes... the fairy tale."
            db "It's the traditional play performed by St. Hermelin's drama club.  Eeheehee..."
            show devilboy animated neutral smirk
            db "Don't be so hasty.  Listen to this... For some reason, The Snow Queen is usually performed while wearing a mask."
            show devilboy animated neutral sad
            db "Which brings me to my point.  In truth, that mask... is cursed."
            db "The students who wore it while playing the role all died unnatural deaths."
            show devilboy animated neutral smirk
            db "Isn't that interesting?  Supposedly, only one girl who played the part ever survived the curse..."
            show devilboy animated neutral serious
            db "No one knows who it is.  Maybe the Drama Club in the Club Building knows?"
            show devilboy animated neutral smirk
            db "If we could figure that out, it might unlock the mystery.  Eeeheehee..."
            $ plotprogress = 3
        call screen Libraryb
        if _return == 1:
            show devilboy animated neutral serious with qleft
            db "You know of 'The Snow Queen,' right?  Yes... the fairy tale."
            db "It's the traditional play performed by St. Hermelin's drama club.  Eeheehee..."
            show devilboy animated neutral smirk
            db "Don't be so hasty.  Listen to this... For some reason, The Snow Queen is usually performed while wearing a mask."
            show devilboy animated neutral sad
            db "Which brings me to my point.  In truth, that mask... is cursed."
            db "The students who wore it while playing the role all died unnatural deaths."
            show devilboy animated neutral smirk
            db "Isn't that interesting?  Supposedly, only one girl who played the part ever survived the curse..."
            show devilboy animated neutral serious
            db "No one knows who it is.  Maybe the Drama Club in the Club Building knows?"
            show devilboy animated neutral smirk
            db "If we could figure that out, it might unlock the mystery.  Eeeheehee..."
        elif _return == 2:
            stu "Hey, you!  You know something, don't you?  I'm begging you, help me out!"
        elif _return == 3:
            stu "You should be careful not to drive people into a corner."
            stu "Piss of a short-tempered guy, and who knows what he'll do?"
            stu "I bet the same is true for demons."
        elif _return == 4:
            jump callHermelinFloor3
        jump label030
    else:
        scene bg library with qdis
        play music schooldays2 if_changed
        call screen Library
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "What're we doin' at the library?  Let's hurry and see--I mean, get checked out!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Those two over there are making fun of Devil-Boy... But I prefer Devil-Boy to them."
            yu "At least he doesn't act all high and mighty."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "What a shabby collection... The library at home is much better stocked."
        elif _return == 4:
            show devilboy animated neutral serious with pleft
            db "...Oh, it's you, Naoya.  Eeeheehee... I'm investigating the seven mysteries of St. Hermelin High."
            show devilboy animated neutral smirk
            db "Want to know what I've learned?  Eeheehee...maybe some other time..."
            if devilboy == False:
                show devilboy ns
                $ tbnarrator = 1
                n "{color=#ebffdb}>Tsutomu Kurouri (Nickname: Devil-Boy)\nHe's an expert in the occult, but frequently has incorrect information.{/color}"
                $ tbnarrator = 0
                $ devilboy = True
        elif _return == 5:
            stu "They call him Devil-Boy, but the stuff he'll tell you is a load of crap.  I know much more about the occult."
            stu "Though, I could never tell the uninitiated."
        elif _return == 6:
            stu "The way I see it, there must be demons who get along well and those that don't."
            stu "If demons who hated each other met up, I'm sure it would be disastrous."
        elif _return == 7:
            stu "You see that guy over there?  The one they call Devil-Boy?"
            stu "He tripped and fell over again today during PE."
            stu "It was frickin' hilarious!  He can't even do a single push-up!  What a lamer!"
        elif _return == 8:
            jump callHermelinFloor3
        jump label030

label label031 (location="Student Council"):
    if plotprogress >=2:
        scene bg black with qdis #update
        #play music #update
        if plotprogress == 4:
            stu "The records?  I've already gone through and sorted them.  It was no small task, you know."
            stu "What?  You want me to show them to you?  Absolutely not!"
            stu "You have no idea what a pain it was to sort all those!"
            stu "If you want to know about the past, go ask someone who was there, like Principal Ooishi!"
            $ plotprogress = 5
        call screen StudentCouncilb
        if _return == 1:
            if plotprogress =< 4:
                stu "If I can get through this, I'll go down in student council history..."
                stu "Hey, if you want to be helpful, run along and solve this disaster, hmm?"
            elif plotprogress == 5:
                stu "The records?  I've already gone through and sorted them.  It was no small task, you know."
                stu "What?  You want me to show them to you?  Absolutely not!"
                stu "You have no idea what a pain it was to sort all those!"
                stu "If you want to know about the past, go ask someone who was there, like Principal Ooishi!"
            if studentcouncilprez == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Student council president\nLeader of St. Hermelin's student council.  Isn't wild about his job.{/color}"
                $ tbnarrator = 0
                $ studentcouncilprez = True
        elif _return == 2:
            stu "The other members and I were organizing a safety committee while HE sat back..."
            stu "We never should have elected that jerk!"
        elif _return == 3:
            jump callHermelinFloor3
        jump label031
    else:
        scene bg studentcouncil with qdis
        play music schooldays2 if_changed
        call screen StudentCouncil
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "I really hate this guy... Ugh!  Can't we go see Ma--I mean, go to the hospital?"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I bet we'd be better off with anyone but him as president."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "If he can't handle the meager power of the student council, he's no man at all."
        elif _return == 4:
            stu "Sorting old records is no task for a student council president!"
            stu "Kandori would have refused to do it as a point of pride..."
            stu "So I refuse too!  It's all part of my quest to be more like him!"
            if studentcouncilprez == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Student council president\nLeader of St. Hermelin's student council.  Isn't wild about his job.{/color}"
                $ tbnarrator = 0
                $ studentcouncilprez = True
        elif _return == 5:
            stu "He's trying to emulate Kandori, the 18th student council president."
            stu "Huh?  You haven't heard of that bigshot at SEBEC?"
            stu "He graduated from here... He's still young, but he's branch president of a big company now."
        elif _return == 6:
            stu "Those are his true colors, but he's no dummy.  He's got the faculty on his side."
            stu "I hear he's never even been reprimanded.  Talk about unfair!"
        elif _return == 7:
            stu "Our president does nothing but sit around and bark orders.  Who voted for this guy?"
            stu "If I was president, I would make a guy like him work 'til he keeled over!"
        elif _return == 8:
            jump callHermelinFloor3
        jump label031

label label032 (location = "Art Room"):
    if plotprogress >= 2:
        scene bg black with qdis #update
        #play music #update
        call screen ArtRoomb
        if _return == 1:
            stu "I thought the art club had it hard before, and now this!"
            stu "Guess it wasn't just the art club, through... the whole school was cursed."
            stu "Hahaha, what a relief!  ...Uh..."
        elif _return == 2:
            jump callHermelinFloor3
        jump label032
    else:
        scene bg artroom with qdis
        play music schooldays2 if_changed
        call screen ArtRoom
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Yeah, Maki's an awesome artist... C'mon, Naoya!  Let's go to the hospital!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I've seen one of Maki's paintings.  She won an award for her 'Gate to Paradise.'"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "The painting I saw of Maki's had a strong, raw sense of emotion to it."
        elif _return == 4:
            stu "We could really use more members... Maki's sick and Chisato's gone missing."
            $ choicetext = "Do you know those two?"
            show nchoice at pright zorder 15 with easeinright
            show nchoice onlayer screens zorder 15 at pright
            show fadeblack onlayer screens zorder 3 with qdis
            $ choice1 = "Yeah"
            $ choice2 = "No, I don't"
            call screen choices with qdis
            if _return == 1:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                stu "Well, Maki's pieces are incredible.  She's won several awards for them."
                stu "Her friend Chisato isn't very good, but she's had better luck with men."
            if _return == 2:
                hide screen choices with qdis
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with qdis
                stu "Ah, I see.  Well, the art club's going through a rough spot right now.  I dunno, maybe this club's cursed..."
        elif _return == 5:
            jump callHermelinFloor3
        jump label032

label label033 (location="Entrance Hall"):
    if plotprogress == 2:
        scene bg black #show new frontgate here
        #play appropriate music
        show elly animated neutral serious with qleft
        el "It's me, Eriko Kirishima.  We have an injured woman with us."
        show elly animated neutral sad
        el "Won't you open the gate?"
        hide elly with qdis
        stu "Not unless you say the password!"
        show elly animated neutral serious with qleft
        el "Ah, yes."
        el "'Roses are red, zombies are blue, I don't want brains, so you know I'm true.'"
        el "Now will you let us in?"
        hide elly with qdis
        stu "All right, come in!"
        n "The school gates open, and Yuki and Naoya carry Maki's mother inside."
        scene bg black #show new entrancehall here
        #play appropriate music
        show saeko animated neutral serious with qleft
        sa "Hey, Main!  You're all safe!?  Oh, I'm so glad..."
        show saeko animated neutral sad
        sa "Oh!  What happened to her!?"
        hide saeko
        show yukino animated neutral serious with qleft
        yu "We'll tell you later!  We need to get her to the infirmary, quick!"
        hide yukino
        show saeko animated neutral serious with qleft
        sa "You're right!  Main, come with me to the infirmary!"
        sa "Yukino, Eriko, I want you to head to the passageway to the gym."
        sa "Ayase and Yuko are there plugging up the hole in the wall.  Please help them out!"
        hide saeko
        show yukino animated neutral serious with qleft
        yu "Right... gotta keep the demons from getting in.  Will do!  C'mon, Eriko!"
        hide yukino with moveoutleft
        show elly animated neutral smirk with qleft
        el "Yes, let's go!"
        hide elly with moveoutleft
        n "Yukino and Elly have left."
        show saeko animated neutral serious with qleft
        sa "All right, then we should get going, too."
        scene bg black #show updated infirmary here #update
        #play appropriate music #update
        show setsuko at pleft2 with qleft
        set "...and that's what happened."
        hide setsuko
        show saeko animated neutral serious with qleft
        sa "So that's what SEBEC is up to, huh...?  I can't believe them!  Hey, Naoya?"
        sa "Sorry to ask, but...could you check in with some of the students?"
        show saeko animated neutral smirk
        sa "Tsutomu in the library says he knows what's going on and...you know how he can be."
        show saeko animated neutral serious
        sa "If you could check in with him, please?"
        jump label001
    else:
        scene bg entrancehall with qdis
        play music schooldays volume 0.4 if_changed
        show screen header
        if yamaoka == False:
            show nanjo animated neutral smirk with qleft
            na "You're all so slow... You must seize the moment, like myself!"
            show nanjo animated neutral serious
            na "There's a reason it's said that one's youth passes quickly."
            hide nanjo
            show mark animated neutral serious with qleft
            mk "That Nanjo pisses me off so bad... I'll find a chink in his armor someday."
            hide mark
            show yukino animated neutral serious with qleft
            yu "Masao and Kei are both such children."
            jump label034
        elif yamaoka == True:
            call screen Entryway
            if _return == 1:
                show mark animated neutral smirk with qleft
                mk "'Young Master'! Hah! Did you hear that? He's a young master!"
                mk "Teeheehee... This is perfect!"
            elif _return == 2:
                show yukino animated neutral serious with qleft
                yu "That Yamaoka guy must really love Nanjo."
            elif _return == 3:
                show nanjo animated neutral serious with qleft
                na "Yes, yes, what IS it, Naoya!? If you have nothing to say, away with you!"
            elif _return == 4:
                stu "Yo, Naoya!  I heard you collapsed!"
                stu "Are you studying too much, man?  Haha, like that'd happen..!"
            elif _return == 5:
                stu "Hey, isn't Nanjo kinda scary?  He's gone past 'cool' straight onto 'cold'."
            elif _return == 6:
                jump calloverworld
            elif _return == 7:
                jump callHermelinFloor1
            jump label033

label label034 (location="Front Gate"):
    scene bg frontgate with qdis
    play music nanjo if_changed
    show yamaoka animated neutral serious with qleft
    "Old Man" "Young Master!"
    show yamaoka
    $ tbnarrator = 1
    n "{color=#ebffdb}>Yamaoka, the Nanjo family butler\nHe's taken care of Nanjo since the heir was an infant.{/color}"
    $ tbnarrator = 0
    hide yamaoka
    show nanjo animated neutral serious with qleft
    na "Y...Yamaoka..!"
    hide nanjo
    show yamaoka animated neutral serious with qleft
    ya "Oh, my!  Master Kei is leaving the premises with a crowd of friends! I'm...I'm so happy to see this...!"
    hide  yamaoka
    show mark animated neutral smirk with qleft
    mk "Master...Kei?"
    hide mark
    show nanjo animated neutral serious with qleft
    na "Y-Yamaoka!  I've told you time and again never to call me that!  You dummy!"
    hide nanjo
    show mark animated neutral smirk with qleft
    mk "Did you just call him 'dummy'?  Hahaha!"
    hide mark
    show nanjo animated neutral serious with qleft
    na "N-No, I, ah... Oh, be silent, Masao!  Look, Yamaoka, I don't need a ride today!"
    na "Just... go back without me!"
    hide nanjo
    show yamaoka animated neutral serious with qleft
    ya "Oh, my!  Will you be going out on the town with your chums, young master?"
    hide yamaoka
    show nanjo animated neutral serious with qleft
    na "I'm only going to the hospital!  And stop calling me that!"
    hide nanjo
    show yamaoka animated neutral serious with qleft
    ya "The hospital!?  Heavens!  I do hope you haven't hurt yourself, young master!"
    hide yamaoka
    show yukino animated neutral smirk with qleft
    yu "Snrk... Ahahahahah!"
    hide yukino
    show nanjo animated neutral serious with qleft
    na "Enough!  Let's be on our way, Naoya!"
    na "Yamaoka... do NOT follow us!"
    hide nanjo with qdis
    $ yamaoka = True
    hide screen header
    jump calloverworld

label label035 (location="Kaneda Mansion"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        scene bg kanedamansion with qdis
        play music rich fadeout 0.5 fadein 0.5
        show screen header
        show kaneda at pleft2 with qleft
        kaneda "What are the police doing!?  I pay more taxes than anyone else!"
        if kaneda == False:
            "{color=#ebffdb}>Katsue Kaneda\nA resident of Mikage-cho who seems to be living the high life lately.{/color}"
            $ kaneda == True
        kaneda "Shouldn't they come protect me first at times like these?"
        kaneda "If anything happens to my treasure, I'll sue!"
        hide kaneda
        show elly animated neutral serious with qleft
        el "But everyone pays taxes.  There's no call to boast about it."
        hide elly
        show kaneda at pleft2 with qleft
        kaneda "Don't act like such a know-it-all, missy!  Ugh, hurry up and get off my property!"
        hide kaneda with qdis
        hide screen header
        jump calloverworld
    if plotprogress == 0:
        scene bg kanedamansion with qdis
        play music rich fadeout 0.5 fadein 0.5
        show screen header
        show kaneda at pleft2 with qleft
        kaneda "What do YOU children want?  You'd better not be here to steal my treasure!"
        if kaneda == False:
            "{color=#ebffdb}>Katsue Kaneda\nA resident of Mikage-cho who seems to be living the high life lately.{/color}"
            $ kaneda == True
        hide kaneda
        show nanjo animated neutral serious with qleft
        na "What nonsense!  To my eyes, this old woman's so-called 'treasure' is little more than rubbish."
        na "She purports to be an antique collector... But she'll buy anything that's priced high enough."
        show nanjo animated neutral smirk
        na "What could be more absurd?"
        hide nanjo
        show yukino animated neutral serious with qleft
        yu "That old biddy treats everyone like a thief.  Just ignore her."
        hide yukino
        show mark animated neutral serious with qleft
        mk "Can we leave yet, Naoya?  I'm sick of taking her crap!"
        hide mark
        show kaneda at pleft2 with qleft
        kaneda "Hmph!  Children like you can't grasp my treasure's true worth!  Now get out of my sight!"
        hide kaneda with qdis
        hide screen header
        jump calloverworld

label label036 (location="Himeno Residence"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        $ tbnarrator = 1
        "The Himeno Residence seems to be locked up..."
        $ tbnarrator = 0
        jump calloverworld
    elif plotprogress == 0:
        scene bg himenoresidence with qdis
        play music poor fadeout 0.5 fadein 0.5
        show screen header
        show nanjo animated neutral serious with qleft
        na "Is no one home?"
        na "Hmmm...what an extraordinarily small home."
        hide nanjo
        show mark animated neutral sad with qleft
        mk "Well, yeah, any place would look small next to yours!"
        show mark animated neutral serious
        mk "Tch, this is why I can't stand rich dudes like you..."
        hide mark
        show yukino animated neutral serious with qleft
        yu "I think this is where Yuko Himeno lives.  You know, Maki's friend."
        show yukino animated neutral sad with qleft
        yu "I work part-time for myself, but she's doing it for her family..."
        hide yukino
        show mark animated neutral sad with qleft
        mk "Man... talk about a sob story!"
        show mark animated neutral smirk
        mk "Yo, Nanjo, why don't you work part-time to pay Yamaoka's salary yourself!?"
        hide mark with qdis
        hide screen header
        jump calloverworld

label label037 (location="Yin & Yan"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        if yyyukino2 == False:
            scene bg yinyan with qdis
            play music yinyan fadeout 0.5 fadein 0.5 if_changed
            show screen header
            show yyclerk at pleft2 with qleft
            yyclerk "Y-Yukino!  Some monsters showed up!"
            yyclerk "Um, could you please stay with me here?"
            hide yyclerk
            show yukino animated neutral serious with qleft
            yu "I'm really sorry, but there's somewhere I need to go."
            yu "But I'm pretty sure you'll be fine as long as you stay in the store."
            hide yukino
            $ yyyukino2 = True
            jump label037
        if yyyukino == True:
            call screen YY1a
            if _return == 1:
                show mark animated neutral serious with qleft
                mk "Looks like the demons aren't comin' into the store.  That's a relief..."
            elif _return == 2:
                show yukino animated neutral serious with qleft
                yu "I wonder if I should've said that... I can't guarantee they won't come in."
            elif _return == 3:
                show nanjo animated neutral serious with qleft
                na "It's quite impressive that this place is still open in the midst of a demon attack."
            elif _return == 4:
                show yyclerk at pleft2 with qleft
                yyclerk "I'll be okay if I'm here... Gotta keep the store open..."
                yyclerk "We never close... Welcome!"
                $ tbnarrator = 1
                "Naoya perused the shop but ultimately bought nothing."
                $ tbnarrator = 0
                #shop here later
            elif _return == 5:
                show elly animated neutral serious with qleft
                el "What a curious feeling... It's as if everything is all a dream when I'm here."
            elif _return == 6:
                hide header
                jump calloverworld
            jump label037
    if plotprogress == 0:
        scene bg yinyan with qdis
        play music yinyan fadeout 0.5 fadein 0.5 if_changed
        show screen header
        if yyyukino == False:
            show yyclerk at pleft2 with qleft
            yyclerk "Oh you're here early, Yukino.  Doesn't your shift start later?"
            yyclerk "Do you need something?"
            hide yyclerk
            show yukino animated neutral serious with qleft
            yu "Something's come up so I'll be in late.  I'll work overtime to make it up."
            hide yukino
            show yyclerk at pleft2 with qleft
            yyclerk "Oh, okay.  You're a real go-getter, y'know that?"
            yyclerk "I guess you have a reason to work."
            hide yyclerk with qdis
            $ yyyukino = True
        call screen YY1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Yukino really does have a part-time job?  Uh... why?"
        elif _return == 2:
            show yukino animated neutral smirk with qleft
            yu "I want to study photography abroad, so I gotta save up."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I can't fathom Yukino wearing that uniform and smiling at customers."
        elif _return == 4:
            show yyclerk at pleft2 with qleft
            yyclerk "Welcome!  What would you like?"
            $ tbnarrator = 1
            "Naoya perused the shop but ultimately bought nothing."
            $ tbnarrator = 0
            #shop here later
        elif _return == 5:
            hide header
            jump calloverworld
        jump label037

label label038 (location="Alaya Shrine"):
    if plotprogress == 2:
        #show Alaya Shrine interior #update
        #play Alaya Shrine Music #update
        show screen header
        call screen AlayaShrineb
        if _return == 1:
            show elly animated neutral smirk with qleft
            el "What a fascinating butterfly..!"
            show elly animated neutral serious
            el "Don't you feel as thought it can see through to the depths of your soul?"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Huh... I wonder what this butterfly's deal really is."
            yu "Well, whatever.  Let's get back to school."
        elif _return == 3:
            bf "Close your eyes, wounded ones..."
            bf "If you are hurt on the way back to school, come here and I will heal you."
        elif _return == 4:
            show setsuko at pleft2 with qleft
            set "..."
            hide setsuko
            n "She seems to be unconscious."
            #shop here later
        elif _return == 5:
            hide header
            jump calloverworld
        jump label038
    if plotprogress == 1:
        #show Alaya Shrine interior #update
        #play Alaya Shrine Music #update
        show screen header
        show elly animated neutral serious with qleft
        el "Here we are.  "
        show elly animated neutral sad
        extend "Maki's mother should be here..."
        pause 0.3
        show elly animated neutral serious
        el "Oh, what an exquisite butterfly!"
        hide elly
        $ tbnarrator = 1
        "The yellow butterfly Elly mentions floats around the group."
        $ tbnarrator = 0
        show yukino animated neutral serious with qleft
        yu "Hey...Is it me, or is there something strange about that butterfly?"
        hide yukino
        show mark animated neutral serious with qleft
        mk "Wh...What's up with this thing!?"
        hide mark
        show bg black
        pause 0.3
        show bg white
        #show video here #update
        show yukino animated neutral serious with qleft
        yu "What {i}was{/i} that?  A dream?"
        hide yukino
        show nanjo animated neutral serious with qleft
        na "'Truth is stranger than fiction'...Evidently."
        hide nanjo
        show elly animated neutral serious with qleft
        el "To be present for another once-in-a-lifetime event..."
        show elly animated neutral smirk
        el "How magnificent!"
        hide elly
        show setsuko at pleft2 with qleft
        set "Nnh... Nrgh..."
        "{color=#ebffdb}>Setsuko Sonomura\nMaki's mother.  She works at SEBEC as an engineering specialist.{/color}"
        hide setsuko
        show mark animated neutral sad with qleft
        mk "H-Hey!  Did you forget about Maki's mom here?"
        hide mark
        n "Maki's mother gets to her feet."
        show yukino animated neutral sad with qleft
        yu "Lady?  You okay?"
        hide yukino
        show nanjo animated neutral serious with qleft
        na "This is a gunshot wound... who did this to you?"
        hide nanjo
        show setsuko at pleft2 with qleft
        set "Kandori's... goons..."
        hide setsuko
        show nanjo animated neutral serious with qleft
        na "Kandori!?  The president of SEBEC?"
        hide nanjo
        show setsuko at pleft2 with qleft
        set "The alterations to this town... Kandori's behind them all... "
        set "I...was involved in the development of a certain device..."
        hide setsuko
        show nanjo animated neutral serious with qleft
        na "A device... And you're saying this machine is causing the changes?"
        hide nanjo
        show setsuko at pleft2 with qleft
        set "It's the *Deva System*... It's engineered to affect reality."
        set "But I didn't think it could do this... Kandori said..."
        set "he doesn't care what happens to this town... I have to hurry and tell the police!"
        hide setsuko
        show elly animated neutral sad with qleft
        el "Oh dear... The police station is already overrun with demons."
        el "I just came from there."
        hide elly
        show setsuko at pleft2 with qleft
        set "My God... But Kandori has to be stopped...!"
        hide setsuko
        show mark animated neutral serious with qleft
        mk "...How did you escape, Ma'am?"
        hide mark
        show setsuko at pleft2 with qleft
        set "Through the abandoned factory... It has a secret freight entrance..."
        set "Use this... *security card*..."
        hide setsuko
        n "Maki's mother faints again."
        show yukino animated neutral sad with qleft
        yu "Lady!"
        show yukino animated neutral serious
        yu "Whew... she only passed out.  We have to get her to the school, quick!"
        hide yukino
        show mark animated neutral serious with qleft
        mk "You handle this, Naoya.  I got business to take care of."
        hide mark
        show nanjo animated neutral serious with qleft
        na "Wait, Masao.  'Nothing ventured, nothing gained...'  I'll come with you."
        na "Remember, you won't be able to get near Kandori without this card."
        hide nanjo with moveoutleft
        n "Mark and Nanjo leave."
        show yukino animated neutral serious with qleft
        yu "H-hey!  ...Tch, thanks, guys."
        yu "C'mon, let's go back to the school ourselves.  Honestly!"
        yu "Men never think about how the ones they leave behind feel."
        hide yukino
        show elly animated neutral smirk with qleft
        el "Those two do have a similarly reckless temperament."
        show elly animated neutral serious
        el "Well, I'm sure they'll give up and come back once they see the place."
        $ plotprogress = 2
        $ fencingclub = False
        jump label038
    elif plotprogress == 0:
        show yukino animated neutral serious with qleft
        yu "'The history of the Alaya Shrine'..."
        yu "It says, 'The god dwelling within people's souls is enshrined here.'"
        hide yukino
        jump calloverworld

label label039 (location="Esumi Clinic"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic1a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Maki's mom is at the shrine, right?"
            show mark animated neutral sad
            mk "We should hurry and go get her."
            jump label039
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Don't sweat it too much, Naoya."
            show yukino animated neutral smirk
            yu "We're here for you."
            jump label039
        elif _return == 3:
            show nanjo neutral sad with qleft
            na "..."
            show nanjo animated neutral serious
            extend "Oh sorry, Naoya."
            na "I was just lost in thought."
            jump label039
        elif _return == 4:
            show elly animated neutral with qleft
            el "This clinic's cheerful atmosphere is always relaxing, I find."
            jump label039
        elif _return == 5:
            show doctor at pleft2 with qleft
            doctor "Wish I could find a nurse who was less of a ditz."
            jump label039
        elif _return == 6:
            nurse "I hear things are going haywire outside."
            nurse "If I wasn't on the job, I'd go look!"
            jump label039
        elif _return == 7:
            hide screen header
            jump calloverworld
    elif plotprogress == 0:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "This is kind of a pain."
            jump label039
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Never been to the doctor before..."
            show yukino animated neutral smirk
            yu "Sent a couple people there, though."
            jump label039
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "True, we could get checked out here..."
            na "But aren't we on the way to the hospital?"
            jump label039
        elif _return == 4:
            show doctor at pleft2 with qleft
            doctor "You must go to St. Hermelin.  I heard they finished building the new gym."
            doctor "Must be easier to use than the old one, huh?"
            jump label039
        elif _return == 5:
            nurse "We just had the clinic remodeled, too!  Doesn't it look nice?"
            jump label039
        elif _return == 6:
            hide screen header
            jump calloverworld

label label040 (location="Mikage Sun Mall"): #MikageMall
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    else:
        scene bg white
        play music mikage fadeout 0.5 fadein 0.5
        call screen MikageSunMall with qdis

label label041 (location="Sennen Mannen-Do"): #Sennen Mannen-Do Mikage
    if plotprogress == 1:
        scene bg sennenmannendomikage with qdis
        play music sennen fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen SMD1a
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "I wish I could be as laid back as you, Naoya."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I'm worried about the school... For some reason, I'm real nervous about it."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "That clerk seems to be suspicious of us."
            na "But ARE we really still human now that we have this power?  What do you think?"
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "I'm rather surprised that some people can remain calm.  It's very impressive."
        elif _return == 5:
            show sennenmannendo 1 at pleft2 with qleft
            "Clerk" "Are you... truly human?"
            "Clerk" "Well, if you're a customer, I welcome you."
            $ tbnarrator = 1
            "Naoya persues the sweets, but ultimately decides against it."
            $ tbnarrator = 0
            #shop here later
        elif _return == 6:
            hide header
            jump label040
        jump label041
    if plotprogress == 0:
        scene bg sennenmannendomikage with qdis
        play music sennen fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen SMD1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "I wonder if kids still come to places like this nowadays."
            show mark animated neutral smirk
            mk "I used to come here every day to play the raffle!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Coming here once in a while is fine, but did you forget about the hospital?"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I've never eaten sweets before.  Yamaoka wouldn't allow it."
        elif _return == 4:
            show sennenmannendo 1 at pleft2 with qleft
            "Clerk" "One bite of Sennen Mannen-Do's sweets extends your life by 1,000 years..."
            "Clerk" "A second bite gives you 10,000 years.  Would you like one?"
            $ tbnarrator = 1
            "Naoya persues the sweets, but ultimately decides against it."
            $ tbnarrator = 0
            #shop here later
        elif _return == 5:
            hide header
            jump label040
        jump label041

label label042 (location="Peace Diner"): #Peace Diner Mikage
    if plotprogress == 1:
        $ tbnarrator = 1
        "The store seems to be closed..."
        $ tbnarrator = 0
        jump label040
    if plotprogress == 0:
        scene bg peacediner with qdis
        play music diner fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen PD1
        if _return == 1:
            show mark animated neutral sad with qleft
            mk "I wish I could leave my crappy home... I'm too embarrassed to have friends over."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "That girl's a friend of Yuka's.  They're a lot alike... neither ever shuts up."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I'd think life in Shibuya would be rather noisy.  This girl evidently has no idea..."
        elif _return == 4:
            "Girl" "I can't wait to live on my own!  I'm thinking I'll get a place by Shibuya... Sounds awesome."
            "Girl" "Ugh, I can't wait to ditch this boring place."
        elif _return == 5:
            show pdclerk at pleft2 with qleft
            pdclerk "Welcome to Peace Diner, where we always give you double meat!"
            hide pdclerk
            show yukino animated neutral serious with qleft
            yu "Hey!  Now's not the time to chow down on fast food!"
        elif _return == 6:
            hide header
            $ tbnarrator = 1
            "You head back out into the mall."
            $ tbnarrator = 0
            jump label040
        jump label042

label label043 (location="Rosa Candida"): #Rosa Candida Mikage
    if plotprogress == 1:
        scene bg rosacandida with qdis
        play music rosa fadeout 0.5 fadein 0.5
        show screen header
        show mark animated neutral sad with qleft
        mk "Hey... Is anyone here...?  You're hiding around here someplace, right?"
        mk "It's me, Masao, I'm not a demon."
        mk "It's safe... You can come out... We'll take you home."
        "{w=0.3}.{w=0.3}.{w=0.3}."
        mk "Mom...?"
        "{w=0.3}.{w=0.3}.{w=0.3}."
        show mark animated neutral serious
        mk "Eh, it's nothin', Naoya.  I'm fine."
        mk "The old bat must've gone home before it all went down."
        show mark animated neutral smirk
        mk "I bet she's bawlin' over her 'stories' on TV as we speak."
        mk "C'mon, let's go!"
    if plotprogress == 0:
        scene bg rosacandida with qdis
        play music rosa fadeout 0.5 fadein 0.5
        show screen header
        if rosacandidamark == False:
            "Mark's Mom" "Massie!"
            show mark animated neutral sad with qleft
            mk "Oh, crap!  It's my mom!"
            hide mark
            "Mark's Mom" "Hey, Massie!  You came just in time!"
            "Mark's Mom" "I'm doing some shopping, but the load's piling up.  Help me out, Massie!"
            show nanjo animated neutral smirk with qleft
            na "Hmmmm... This 'Massie' is you, is it, Masao Inaba...?"
            hide nanjo
            show mark animated neutral serious with qleft
            mk "Q-Quit it, you old bat!  I'm busy!  Leave me alone!"
            hide mark
            "Mark's Mom" "Massie!  You'd call your own mother an old bat!?"
            "Mark's Mom" "And just when I was thinking of buying you some t-shirts!"
            show yukino animated neutral smirk with qleft
            yu "'Massie'?  That's about as embarrassing as 'young master.'"
            hide yukino
            show mark animated neutral serious with qleft
            mk "No one asked you, Yukino!"
            hide mark
            "Mark's Mom" "Oh, are these your friends?"
            "Mark's Mom" "My, this store is expensive. Look at this one, Massie!"
            show mark animated neutral serious with qleft
            mk "What do I want with that!?  C'mon, Naoya, let's go!"
            hide mark
            $ tbnarrator = 1
            "Mark leaves the store."
            $ tbnarrator = 0
            "Mark's Mom" "Honestly, that boy... I hope you'll all stand by Massie, won't you?"
            $ rosacandidamark = True
            hide header
            jump label040
        if rosacandidamark == True:
            show mark animated neutral sad with qleft
            mk "She can't still be here... right...?"
            hide mark
            "Mark's Mom" "Oh, Massie, you're back!  Perfect timing!"
            show mark animated neutral serious with qleft
            mk "Crap!  She's still here!?  Let's ditch this place, Naoya!"
            hide header
            jump label040

label label044 (location="Satomi Tadashi"): #Satomi Tadashi Mikage
    if plotprogress == 1:
        scene bg satomitadashi with qdis
        play music satomi volume 0.4 fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen ST1a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "When I left my house this morning, I sure wasn't expecting this."
        elif _return == 2:
            show yukino animated neutral sad with qleft
            yu "I wonder how Maki's mom is doing... Hope she wasn't hurt too bad."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "A well-prepared man fears nothing!"
            show nanjo animated neutral sad
            na "...That's what Yamaoka always said."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "You get to the shrine by going west from here."
            el "It's in the northwestern part of Mikage-Cho."
        elif _return == 5:
            show stclerk at pleft2 with qleft
            stclerk "Ah, welcome!  Hey, have you seen Tamaki? I'm really worried about her..."
            stclerk "My son, on the other hand, can take a running jump!"
            stclerk "Hm...?  Oh, right, medicine.  Coming right up!"
            #store here eventually
        elif _return == 6:
            hide header
            jump label040
        jump label044
    if plotprogress == 0:
        scene bg satomitadashi with qdis
        play music satomi volume 0.4 fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen ST1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Don't tell me you're buying painkillers... We gotta go to the hospital!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "That lady sure seems to like getting into other people's business."
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "...paralyzed, then Dis-Para does the trick... Augh!"
            show nanjo animated neutral serious
            na "The song won't leave my brain!"
        elif _return == 4:
            "Lady" "Hey, don't you think it's weird, too?  I mean that Kaneda!"
            "Lady" "In the space of only a year, she's struck it rich somehow!"
            "Lady" "It's suspicious, if you ask me... Veeeery suspicious!"
        elif _return == 5:
            show stclerk at pleft2 with qleft
            stclerk "Oh, you go to St. Hermelin?  Do you know my son Tadashi?"
            stclerk "He's a hopeless slacker, but he's fallen in love with a real cutie!"
            stclerk "I'd be over the moon if a girl like that married my boy!"
            #store here eventually
        elif _return == 6:
            hide header
            jump label040
        jump label044

label label045 (location="Judgment 1999"): #Judgment 1999 Mikage
    if plotprogress == 1:
        scene bg judgment with qdis
        play music judgment fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen JD1a
        if ellycasino = 0:
            man "Hey, I've been looking for you.  You can't be out and about like this!"
            man "Aren't you scared with all the demons around?"
            man "C'mon, let me protect you!"
            show elly animated neutral serious with qleft
            el "Well, that's very generous of you."
            el "But given how much more extensive my knowledge of demons is than yours..."
            el "...Not to mention my ability to protect myself... Bother someone else."
            hide elly with qdis
            man "Uh... O-Okay..."
            $ ellycasino = 1
            jump label045
        elif ellycasino = 1:
            if _return == 1:
                show mark animated neutral serious with qleft
                mk "I like casinos too, but right now I just wanna hit up the shrine."
            elif _return == 2:
                show yukino animated neutral serious with qleft
                yu "I'm amazed at Eriko's guts.  But then, with her looks, she needs 'em."
            elif _return == 3:
                show nanjo animated neutral serious with qleft
                na "You don't seem to have a care in the world..."
                show nanjo animated neutral sad with qleft
                na "I'm rather envious of your composure at a time like this."
            elif _return == 4:
                show elly animated neutral serious
                el "Men like him are so tedious..."
            elif _return == 5:
                man "Well, that was a bust."
                man "But she'll need someone to protect her sooner or later!"
                man "I'll just keep trying until then!"
            elif _return == 6:
                show jclerk 1 at pleft2 with qleft
                jclerk "Hiiii!  SO nice to see you!"
                jclerk "If you're looking to exchange money for coins, I'm your man."
                jclerk "Won't you purchase some coins?  Hmmmm?"
                $ tbnarrator = 1
                "After some consideration, Naoya decided against it."
                $ tbnarrator = 0
                #coin purchase for gambling
            elif _return == 7:
                show jclerk 2 at pleft2 with qleft
                jclerk "I can exchange your coins for items, if that's what you're in the mood for..."
                jclerk "Wanna see what I've got?"
                $ tbnarrator = 1
                "After some consideration, Naoya decided against it."
                $ tbnarrator = 0
                #coin exchange for gambling
            elif _return == 8:
                hide screen header
                jump label040
            jump label045
    if plotprogress == 0:
        scene bg judgment with qdis
        play music judgment fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen JD1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Elly's pretty well-known, huh?  But then again, it's not that surprising."
            show mark animated neutral smirk
            mk "She's pretty awesome."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Do what you want, but can it wait until after we've been to the hospital?"
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "I wasn't aware you were a gambler.  Looks can be evidently be deceiving."
        elif _return == 4:
            "Man" "Hey, do you all go to St. Hermelin?  Then you must know that girl..."
            "Man" "She has long hair and a knockout figure.  I think her name's Sally or Mary..."
            "Man" "Whatever it is, she's gorgeous!"
            "Man" "C'mon, next time she's here, introduce us!"
        elif _return == 5:
            stu  "Aw, c'mon!  I lost all my coins again!"
            stu "I pumped in lots of coins, so whoever wins next will hit it big."
            stu "Hey, are you up next!?  Urgh... This ain't fair!"
        elif _return == 6:
            show jclerk 1 at pleft2 with qleft
            jclerk "Hiiii!  SO nice to see you!"
            jclerk "If you're looking to exchange money for coins, I'm your man."
            jclerk "Won't you purchase some coins?  Hmmmm?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin purchase for gambling
        elif _return == 7:
            show jclerk 2 at pleft2 with qleft
            jclerk "I can exchange your coins for items, if that's what ou're in the mood for..."
            jclerk "Wanna see what I've got?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin exchange for gambling
        elif _return == 8:
            hide screen header
            jump label040
        jump label045

label label046: #velvet room
    $ tbnarrator = 1
    "The store is closed..."
    window hide
    window auto
    $ tbnarrator = 0
    jump calloverworld

label label047: #agastya tree mikage mall
    scene bg agastyatree with qdis
    play music agastya fadeout 0.5 fadein 0.5 if_changed
    $ location = "Agastya Tree"
    show screen header
    ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
    hide screen header
    jump label040

label label048 (location="Historical Society"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        $ tbnarrator = 1
        "The Historical Society seems to be closed..."
        $ tbnarrator = 0
        jump calloverworld
    if plotprogress == 0:
        scene bg historicalsociety1 with qdis
        play music history fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen HistoricalSociety1
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Mmmm... receptionists."
            show mark animated neutral serious
            mk "Er, uh..."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "You're doing social studies research before we go to the hospital?"
            show yukino animated neutral smirk
            yu "Whatever, weirdo..."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "The historical society seems to be past here.  Are we going inside?"
        elif _return == 4:
            "Woman" "Welcome to the Mikage Historical Society!"
            "Woman" "We have many interesting exhibits here that shed light on the area's history."
        elif _return == 5:
            jump label049
        elif _return == 6:
            $ tbnarrator = 1
            "You go back out into Mikage-Cho."
            window hide
            window auto
            $ tbnarrator = 0
            hide screen header
            jump calloverworld
        jump label048

label label049: #Historical society inside
    scene bg historicalsociety2 with qdis
    play music history fadeout 0.5 fadein 0.5 if_changed
    show screen header
    call screen HistoricalSociety2
    if _return == 1:
        show mark animated neutral serious with qleft
        mk "You're awfully studious all of a sudden."
        show mark animated neutral smirk
        mk "Is Hell about to freeze over?"
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "It's musty in here, but kinda nice.  Maybe it's the mirror's influence."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "It's long been said that mirrors have mystical powers... Is this one of them?"
    elif _return == 4:
        "Man" "I came to see the {color=#800000}Expel Mirror{/color} display.  It's as divine as they say..."
    elif _return == 5:
        "Girl" "The Expel Mirror was all they found in the ruins six months ago."
        "Girl" "My teacher said it's boring in those ruins 'cause there's nothing else there."
    elif _return == 6:
        hide screen header
        $ tbnarrator = 1
        "You head back into the reception area."
        window hide
        window auto
        $ tbnarrator = 0
        jump label048
    jump label049

label label050: #police station
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    elif pddemon == True:
        show elly animated neutral serious
        el "Naoya, now is not the time."
        hide elly
        jump calloverworld
    elif plotprogress == 1:
        scene bg policestation with qdis
        play music police1 fadeout 0.5 fadein 0.5 if_changed
        $ location = "Police Station"
        show screen header
        show yukino animated neutral serious with qleft
        yu "'Scuse me!  There's demons in town!"
        yu "People are hurt.  Can you help them, um..."
        show yukino animated neutral sad
        extend "Officer?"
        hide yukino
        officer "Did you say...{w=0.7}demons?"
        show elly animated neutral serious with qleft
        el "Wait, Yukino!"
        el "Something's not right about him!"
        hide elly
        officer "The demons have been and gone."
        officer "Thanks to them, I ended up like this..."
        pause 1.0
        officer "Dammit...Lieutenant...{w=0.5}"
        extend "Please help me...{w=0.5}help..."
        show bg black
        pause 0.2
        hide bg black
        show elly animated neutral serious with qleft
        el "Just as I thought!  Run, everyone!"
        hide elly
        show yukino animated netural serious with qleft
        yu "Tch, looks like the police won't be any help either!"
        $ pddemon = True
        hide yukino with qdis
        hide screen header
        jump calloverworld
    elif plotprogress == 0:
        scene bg policestation with qdis
        play music police1 fadeout 0.5 fadein 0.5 if_changed
        $ location = "Police Station"
        show screen header
        "Lieutenant" "Well, if it isn't Masao.  You've been attending school, I hope?"
        "Lieutenant" "Not causing trouble for your teachers, are you?"
        "Officer" "That's a little harsh, Lieutenant.  You're no trouble anymore, right Masao?"
        show mark animated neutral sad with qleft
        mk "Yeah, well... sorta..."
        hide mark with qdis
        hide screen header
        jump calloverworld

label label051: #Mikage Ruins
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        show elly animated neutral smirk with qleft
        el "It's a pity to have such splendid ruins so close at hand, yet inacessibe."
        hide elly
        jump calloverworld
    if plotprogress == 0:
        show mark animated neutral serious with qleft
        mk "The ruins aren't open to the public, but people say there's nothin' here anyways."
        hide mark
        jump calloverworld

label label052 (location="Joy Street Mall"): #Joy Street Mall
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    else:
        scene bg white
        play music joystreet fadeout 0.5 fadein 0.5
        call screen JoyStreetMall with qdis

label label053 (location="Rosa Candida"): #Joy street
    if plotprogress == 1:
        $ tbnarrator = 1
        "The store seems to be closed."
        $ tbnarrator = 0
        jump label053
    if plotprogress == 0:
        scene bg rosacandida with qdis
        play music rosa fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen RC2
        if _return == 1:
            show mark animated neutral smirk with qleft
            mk "Speaking of clothes, what's with Nanjo's scarf?  He's always wearing that thing."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Tch, did Yuka ask you to go shopping for her?"
            yu "Well, once you're done here, we're going straight to the hospital!"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "The only clothing I require is this uniform... and my scarf, of course."
        elif _return == 4:
            show rcclerk at pleft2 with qleft
            rcclerk "The people in this town have such bad fashion sense!"
            rcclerk "The only one with a shred of taste is this brown-haired boy I see sometimes..."
            rcclerk "He's got these cool goggles on, and he's really cute!"
        elif _return == 5:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label053

label label054 (location = "Sennen Mannen-Do"): #Joy Street
    if plotprogress == 1:
        scene bg black with qdis
        play music sennen fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen SMD2a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Is it okay, these stores bein' open?  I ain't responsible if they get messed up by demons!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Haven't you had enough fooling around?  Can't we go to the Alaya Shrine next?"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "So he refuses to close his business even with the advent of demons..."
            show nanjo animated neutral smirk
            na "The common people can be stronger-willed than I had given them credit for."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "That reminds me, some people at school were saying something similar."
        elif _return == 5:
            show sennenmannendo 1 at pleft2 with qleft
            smd "My, I'm grateful you came all this way.  Things must be hard for all of you."
            hide sennenmannendo
            "Naoya perused the shop but ultimately bought nothing."
        elif _return == 6:
            man "That strange store in this mall will apparently be open soon."
            man "Don't ask me when, though."
        elif _return == 7:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label054
    elif plotprogress == 0:
        scene bg sennenmannendojoy with qdis
        play music sennen fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen SMD2
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Music...?  Like, pianos and singing?  Huh?  I think I've heard somethin' like that somewhere too..."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "A weird store?  What do you think's in it...?"
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Well then, where to next?  We can go anywhere you please..."
            show nanjo animated neutral smirk
            na "Just so long as the hospital is in our plans at some point."
        elif _return == 4:
            "Customer" "There's this one strange store in this here mall..."
            "Customer" "Whenever I go take a gander, it's closed, and I've never seen anyone go in or out."
            "Customer" "But every now and then, you can hear music from in there... It's a funny old world, isn't it?"
        elif _return == 5:
            show sennenmannendo 1 at pleft2 with qleft
            smd "My, I'm grateful you came all this way.  Well, feel free to look around."
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label054

label label055 (location = "Yin & Yan"): #Joy Street
    if plotprogress == 1:
        scene bg yinyan with qdis
        play music yinyan fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen YY2a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Is this the place Yukino works part-time?"
            mk "Oh, wait, that was another store."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Sure, it's a convenience store, but being able to buy weapons here is kinda..."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Hah... It's true, one can pick up daily necessities at the convenience store."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "Even if we don't buy them here, everyday objects can be useful as weapons."
        elif _return == 5:
            show yyclerk at pleft2 with qleft
            yyclerk "Our store doesn't carry weapons... Is that all right?"
            hide yyclerk
            "Naoya perused the shop but ultimately bought nothing."
        elif _return == 6:
            man "Convenience stores are supposed to stock everything!  Why wouldn't they have weapons, too!?"
            man "Don't you agree?  Yes!  Exactly!"
            man "Shouldn't this store be serving its customers' needs!?"
        elif _return == 7:
            man "Are these stores good for anything!?"
            man "Isn't it odd they don't have weapons?  Yeah!  You tell 'em!"
            man "A store's gotta serve its customers' needs!"
        elif _return == 8:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label054
    elif plotprogress == 0:
        scene bg yinyanjoy with qdis
        play music yinyan fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen YY2
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "So that's Reiji's mom... She seems so classy.  A pretty far cry from mine... Ugh."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "For all that Reiji Kido's an oddball, his mother seems nice."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Are you finished here?  Can we be on our way to the hospital now?"
        elif _return == 4:
            if reijimom == False:
                "Woman" "Oh, do you go to St. Hermelin?  That's the school my son attends..."
                $ reijimom = True
                $ choicetext = "His name's Reiji Kido.  Do you know him?"
                show nchoice at pright zorder 15 with easeinright
                show nchoice onlayer screens zorder 15 at pright
                show fadeblack onlayer screens zorder 3 with qdis
                $ choice1 = "Yeah"
                $ choice2 = "No, I don't"
                call screen choices with qdis
                if _return == 1:
                    hide screen choices with qdis
                    hide fadeblack onlayer screens
                    hide nchoice onlayer screens
                    hide nchoice
                    with qdis
                    "{size=-2}Reiji's Mom" "Oh, so you know him?  Ah, you're in the same class? I see..."
                    "{size=-2}Reiji's Mom" "Then you must know my son isn't very outgoing..."
                    $ lines = 2
                    $ choicetext = "It may be selfish of me to ask this, \nbut could you make friends with Reiji?"
                    show nchoice at pright zorder 15 with easeinright
                    show nchoice onlayer screens zorder 15 at pright
                    show fadeblack onlayer screens zorder 3 with qdis
                    $ choice1 = "Sure"
                    $ choice2 = "Nah"
                    call screen choices with qdis
                    if _return == 1:
                        hide screen choices with qdis
                        hide fadeblack onlayer screens
                        hide nchoice onlayer screens
                        hide nchoice
                        with qdis
                        "{size=-2}Reiji's Mom" "Ah, truly?  Thank you!  Please feel free to come visit him at home sometime!"
                    elif _return == 2:
                        hide screen choices with qdis
                        hide fadeblack onlayer screens
                        hide nchoice onlayer screens
                        hide nchoice
                        with qdis
                        "{size=-2}Reiji's Mom" "I see... I'm not surprised.  He does cultivate a bizarre image..."
                        "{size=-2}Reiji's Mom" "But deep down, he's really very sweet.  That reminds me... "
                        "{size=-2}Reiji's Mom" "It's not much, but please take this.  I hope you and my son can be friends."
                        "Received a Chewing Soul!  Or you will whenever there's an inventory!"
                    $ lines = 1
                elif _return == 2:
                    hide screen choices with qdis
                    hide fadeblack onlayer screens
                    hide nchoice onlayer screens
                    hide nchoice
                    with qdis
                    "{size=-2}Reiji's Mom" "Ah, I see... I'm sorry to have been so forward."
            elif reijimom == True:
                "{size=-2}Reiji's Mom" "Oh, you're a student at St. Hermelin... Please make friends with my son."
        elif _return == 5:
            show yyclerk at pleft2 with qleft
            yyclerk "Welcome!  What would you like?"
            $ tbnarrator = 1
            "Naoya perused the shop but ultimately bought nothing."
            window hide
            window auto
            $ tbnarrator = 0
            #shop here later
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label055

label label056 (location = "Peace Diner"): #Joy Street
    if plotprogress == 1:
        hide screen header
        $ tbnarrator = 1
        "The diner is closed..."
        window hide
        window auto
        $ tbnarrator = 0
        jump label052
    elif plotprogress == 0:
        scene bg peacediner with qdis
        play music diner fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen PD2
        if _return == 1:
            show mark animated neutral sad with qleft
            mk "Hidehiko's not here, is he?  Good... Dammit..."
            show mark animated neutral serious
            mk "I never shoulda said anything about all-you-can-eat!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Summnoning demons... I don't think it'd be anything to joke about if it actually happened."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "A card game?  Mm... I'll let it slide.  It sounds adult enough."
            na "Whereas Masao still gets excited over video games, even in high school."
            na "...Don't tell me you still play those things, too?"
        elif _return == 4:
            "Man" "Right now, I'm into this card game called 'Persona'..."
            "Man" "You use these things called 'Spell Cards' to summon demons."
            "Man" "Man, can you imagine if you could really do that?  Wouldn't that be wild?"
        elif _return == 5:
            show pdclerk at pleft2 with qleft
            pdclerk "Welcome-- oh wait hang on the register's on the fritz again."
            pdclerk "What do I do with this?  I don't know how to fix this thing!"
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label056

label label057 (location = "Satomi Tadashi"): #Joy Street
    if plotprogress == 1:
        scene bg satomitadashi with qdis
        play music satomi volume 0.4 fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen ST2a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Kids these days sure know what's what..."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I'm surprised Maki's mom made it to the shrine."
            show yukino animated neutral sad
            yu "If she'd collapsed before then... I don't like to think what might've happened."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "All one can trust is one's own strength.  It's the only way."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "I'm giving some thought to the mystery as well."
            show elly animated neutral smirk
            el "This is my chance to put into practice the things I've studied all this time."
        elif _return == 5:
            show stclerk at pleft2 with qleft
            stclerk "I'm not the least bit scared of demons.  I'm sure it was just a trick, or maybe I was seeing things."
            hide stclerk
            "Naoya perused the shop but ultimately bought nothing."
        elif _return == 6:
            student "The TV and radio don't work, and my parents are hiding under their futons."
            student "I guess in the end, you have to take matters into your own hands."
        elif _return == 7:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label054
    elif plotprogress == 0:
        scene bg satomitadashi with qdis
        play music satomi volume 0.4 fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen ST2
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "So this is Tadashi's uncle's store.  He said his dad owns the Sun Mall one?"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "I'm curious about this tree that wasn't there before."
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "...when you're feeling ill, then just take a Dis-Sick..."
            show nanjo animated neutral serious
            na "Gah, this insidious song!  I'm being brainwashed!"
        elif _return == 4:
            "Customer" "I went to the park and saw a tree that wasn't there before.  You should go look."
        elif _return == 5:
            show stclerk at pleft2 with qleft
            stclerk "Are you friends with my nephew?  Then I'll give you extra special service!"
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label057

label label058 (location = "Esumi Clinic"): #Esumi Clinic Joy Street
    if plotprogress == 1:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic2a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "It's so quiet here... I feel like nothin' ever happened."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Whatever's out there in town... It's not a bear, is it?"
        elif _return == 3:
            show nanjo animated neutral smirk with qleft
            na "It would be nice if I could someday cure my wounds through willpower alone."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "I wonder... what prompted the sudden appearance of these demons?"
        elif _return == 5:
            nurse "I heard a bear appeared.  Was it brown?  White?  Plump and hairy?"
        elif _return == 6:
            show doctor at pleft2 with qleft
            doctor "Do bears appear even in this town...?"
        elif _return == 7:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label058
    elif plotprogress == 0:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic2
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "The 'haunted mansion' was just some old, abandoned dump.  We liked it there, is all."
        elif _return == 2:
            show yukino animated neutral smirk with qleft
            yu "I'll admit, I played at the haunted mansion too."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I can't speak to what went on at the haunted mansion; I've never been."
        elif _return == 4:
            nurse "Did you play in the haunted mansion when you were little?  Lots of kids did."
        elif _return == 5:
            show doctor at pleft2 with qleft
            doctor "It's another nice day out."
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label058

label label059: #velvet room joy street
    $ tbnarrator = 1
    "The store is closed..."
    window hide
    window auto
    $ tbnarrator = 0
    jump calloverworld

label label060 (location = "Agastya Tree"): #joy street
    scene bg agastyatree with qdis
    play music agastya fadeout 0.5 fadein 0.5
    show screen header
    ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
    hide header
    jump label052

label label061 (location = "Judgment 1999"): # Joy Street
    if plotprogress == 1:
        scene bg judgment with qdis
        play music judgment fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen JD2a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "I feel sorry for the rest of the Tailors crew, but I got places to be."
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "The Alaya Shrine, guys.  I hate to nag, but you better not forget."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Is there a deeper plan underlying your actions, or...?"
            na "I'm completely unable to fathom your motivations for being here."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "The air's so unpleasant here."
        elif _return == 5:
            "Man" "Aw crap, what'm I gonna do?  I'm not cut out to fight demons."
            "Man" "And Mark ain't gonna be around, neither.  I gotta say, I'm scared."
            show mark animated neutral serious with qleft
            mk "Dude, don't go freakin' out over somethin' like this."
            mk "I'm leavin' the Tailors in your hands while I'm gone, y'know."
        elif _return == 6:
            "Man" "Heehee... Sho you guysh aren't demonsh..."
            "Man" "Tooo baaad... We woulda beat you up if you were!"
            "Man" "And then I woulda made you all work for me! Heee!"
        elif _return == 7:
            show jclerk 1 at pleft2 with qleft
            jclerk "Hiiii!  SO nice to see you!"
            jclerk "If you're looking to exchange money for coins, I'm your man."
            jclerk "Won't you purchase some coins?  Hmmmm?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin purchase for gambling
        elif _return == 8:
            show jclerk 2 at pleft2 with qleft
            jclerk "I can exchange your coins for items, if that's what you're in the mood for..."
            jclerk "Wanna see what I've got?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin exchange for gambling
        elif _return == 9:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label061
    elif plotprogress == 0:
        scene bg judgment with qdis
        play music judgment fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen JD2
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "You know, I like the slots too, but we should play after our checkup!"
        elif _return == 2:
            show yukino animated neutral serious with qleft
            yu "Masao's pals are weird as ever."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "What's the matter, Naoya?  Have you suddenly cottoned to gambling?"
        elif _return == 4:
            "Man" "Ya know, there's been this outsider lately hangin' around our place."
            "Man" "Dude supposedly has a scar on his head.  He shouldn't mess with the Tailors!"
            show mark animated neutral serious with qleft
            mk "Just ignore those guys.  They'll get bored and wander off before too long."
            $ reijicasino = True
        elif _return == 5:
            "Man" "Heehee... You guysh are Mark'sh friendsh?  Heeheeheeeeee!"
            "Man" "Looksh like you guysh ain't the onesh!"
        elif _return == 6:
            "Addict" "Dammit!  I'm broke again!  After all my losses, the next one who plays this machine oughtta win big..."
            "Addict" "Wait, are you up next?  Aww, this sucks!"
        elif _return == 7:
            show jclerk 1 at pleft2 with qleft
            jclerk "Hiiii!  SO nice to see you!"
            jclerk "If you're looking to exchange money for coins, I'm your man."
            jclerk "Won't you purchase some coins?  Hmmmm?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin purchase for gambling
        elif _return == 8:
            show jclerk 2 at pleft2 with qleft
            jclerk "I can exchange your coins for items, if that's what you're in the mood for..."
            jclerk "Wanna see what I've got?"
            $ tbnarrator = 1
            "After some consideration, Naoya decided against it."
            $ tbnarrator = 0
            #coin exchange for gambling
        elif _return == 9:
            hide screen header
            $ tbnarrator = 1
            "You head back into the mall."
            window hide
            window auto
            $ tbnarrator = 0
            jump label052
        jump label061

label label062 (location = "SEBEC Building"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        if reijisebec == False:
            #Play BGM: Appearance! (or similar)
            #Reiji outside Sebec building
            scene bg black with qdis
            show elly animated serious with qleft
            el "Mm? Isn't he that transfer student?"
            hide elly
            show mark animated serious with qleft
            mk "Huh?  Oh, hey, yeah, it's Reiji.  What's he doin' here?"
            hide mark
            show reiji animated neutral serious with qleft
            re "So you're not lettin' me through?  Fine... then be ready to die."
            hide reiji
            man "Don't make me tell ya twice.  Past here is SEBEC territory."
            man "You don't listen, maybe you get shot to death."
            show mark animated sad with qleft
            mk "That dumbass!  He's gonna get himself killed!"
            hide mark
            "Mark approaches Reiji and the guard."
            show mark animated smirk with qleft
            mk "Hahaha, sorry to butt in.  This guy's not all there upstairs, y'know?"
            mk "C'mon, blockhead, time to go."
            hide mark
            show reiji animated neutral serious with qleft
            re "Tch... You guys again."
            hide reiji
            "Reiji leaves."
            show mark animated sad with qleft
            mk "Sheesh... What is that dude up to?"
            hide mark
            show nanjo animated serious with qleft
            na "So even you'll lend a hand to others... Interesting.  I wouldn't have thought it."
            hide nanjo
            show mark animated serious with qleft
            mk "Idiot!  Even guys like him have moms..."
            show mark animated sad
            mk "She'd be sad if he got gunned down."
        elif reijisebec == True:
            man "Who're youse?"
            man "Past here is SEBEC territory.  No entry."
        label label062a:
            call screen Sebec2
            if _return == 1:
                show mark animated neutral serious with qleft
                mk "Hey, doesn't Maki's mom work for SEBEC?  What in the world's going on...?"
            elif _return == 2:
                show yukino animated neutral serious with qleft
                yu "I don't like this... This isn't how an ordinary company acts."
            elif _return == 3:
                show nanjo animated neutral serious with qleft
                na "SEBEC... What's Kandori's game?"
            elif _return == 4:
                show elly animated neutral serious with qleft
                el "What could this mean?  I heard SEBEC was a Fortuna 500 company..."
                show elly animated neutral sad
                el "But this may as well be a Mafia front operation."
            elif _return == 5:
                hide screen header
                $ tbnarrator = 1
                "You go back out into Mikage-Cho."
                window hide
                window auto
                $ tbnarrator = 0
                jump calloverworld
            jump label062a
    elif plotprogress == 0:
        play music sebec2 fadeout 0.5 fadein 0.5
        if Sebec1 == False:
            scene bg sebecreception with qdis
            show screen header
            show takeda at pleft2 with qleft
            "Man" "What do you kids want?  This ain't a playground for brats like you.  Hey, toss these kids out!"
            $ tbnarrator = 1
            n "{color=#0ff}>Takeda\nKandori's right-hand man who carries out SEBEC's illegal operations.{/color}"
            $ tbnarrator = 0
            hide takeda
            man "Takeda?  What's this disturbance about?"
            $ tbnarrator = 1
            "A well-dressed man steps into the room, and Nanjo confronts him immediately."
            $ tbnarrator = 0
            show nanjo animated neutral serious with qleft
            na "Kandori..."
            hide nanjo
            play music kandori0 fadeout 0.5 fadein 0.5
            show kandori animated neutral smirk with qleft
            kan "My, what a rare pleasure.  What business does the scion of the Nanjo family have with us?"
            show kandori
            $ tbnarrator = 1
            n "{color=#0ff}>Takahisa Kandori\nThe ambitious branch president of SEBEC.  Sinister rumors circulate abouthim...{/color}"
            $ tbnarrator = 0
            hide kandori
            show nanjo animated neutral serious with qleft
            na "I didn't come here for you.  I'm only tagging along with these people."
            hide nanjo
            show kandori animated neutral serious with qleft
            kan "Aha... Then these must be the young master's school friends."
            show kandori animated neutral smirk
            kan "You accompanied them to a sordid place like this?  Quite a friendship indeed..."
            hide kandori
            show nanjo animated neutral serious with qleft
            na "Cease calling me 'young master.'  I never gave you permission to use that name."
            hide nanjo
            show takeda at pleft2 with qleft
            tak "You little--!"
            hide takeda
            show kandori animated neutral serious with qleft
            kan "Stand down, Takeda.  It seems the Nanjo family lacks discipline...Well, I'll allow it."
            kan "But Nanjo... I will teach you the proper form of address to your betters."
            hide kandori
            show mark animated neutral serious with qleft
            mk "Nanjo's an insufferable dick, but you're a hell of a lot worse...!"
            hide mark
            show takeda at pleft2 with qleft
            tak "Tch... It's almost time, Mr. Kandori."
            hide takeda
            show kandori animated neutral serious with qleft
            kan "Yes, I'll be right there.  Now then, the time has come for me to ask you all to leave."
            hide kandori
            show mark animated neutral smirk with qleft
            mk "Heh!  Let's go, Naoya."
            hide mark with qdis
            $ tbnarrator = 1
            "You return back to the streets of Mikage-Cho."
            window hide
            window auto
            $ tbnarrator = 0
            $ Sebec1 = True
            hide screen header
            jump calloverworld
        if Sebec1 == True:
            scene bg sebecreception2 with qdis
            $ location = "SEBEC Building"
            man "Excuse me, do you have an appointment?"
            man "I'm sorry, but if you don't have one, I must ask you to leave."
            hide screen header
            jump calloverworld

label label063 (location = "Abandoned Factory"):
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        scene bg factoryreiji with qdis
        play music reiji fadeout 0.5 fadein 0.5
        $ location = "Abandoned Factory"
        show screen header
        show nanjo animated neutral smirk with qleft
        na "I don't recall having anything to do at such a shabby place."
        hide nanjo
        show mark animated neutral serious with qleft
        mk "Nanjo, you dick..."
    if plotprogress == 0:
        $ reijicheck = reijiflags
        if reijicasino == True:
            $ reijicheck += 1
        if reijifactory == True:
            $ reijicheck += 1
        if reijimom == True:
            $ reijicheck += 1
        if reijicheck == 5:
            scene bg factoryreiji with qdis
            play music reiji fadeout 0.5 fadein 0.5
            $ location = "Abandoned Factory"
            show screen header
            show nanjo animated neutral smirk with qleft
            na "I think simply 'shabby' would be more fitting for this place than 'antique.'"
            show nanjo animated neutral serious
            na "Hm...?  Masao, is he one of your 'crew' as well?"
            hide nanjo
            show mark animated neutral serious with qleft
            mk "Say what?"
            mk "Huh...?  So you're the dude with the scar on his head..."
            mk "What're you doin' here?"
            hide mark
            show reiji animated neutral serious with qleft
            re "You'd all better stay away from here.  Unless you want to die, of course..."
            hide reiji
            show mark animated neutral serious with qleft
            mk "What's that supposed to mean?  Hey, wait a sec!"
            hide mark
            "Reiji moves past the group and leaves without answering any of their questions."
            show yukino animated neutral serious with qleft
            yu "I wonder what he's wandering around for..."
            hide yukino with qdis
            hide screen header
            jump calloverworld
        else:
            play music mark fadeout 0.5 fadein 0.5
            scene bg factory with qdis
            show screen header
            show mark animated neutral serious with qleft
            mk "You got business at our studio today, man?"
            mk "Don't think anyone's here today..."
            hide mark with qdis
            hide screen header
            $ reijicheck = 0
            jump calloverworld
    jump calloverworld

label label064 (location = "Esumi Clinic"): #Ward 2 Clinic
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic3a
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "Damn, this is pissin' me off... We gotta hurry and go to the shrine."
        elif _return == 2:
            show yukino animated neutral sad with qleft
            yu "Y'think the woman that nurse saw was Maki's mom?"
        elif _return == 3:
            show nanjo animated neutral sad with qleft
            na "I'd like to refrain from seeing the doctor for a while..."
        elif _return == 4:
            show elly animated neutral serious with qleft
            el "Let's go to the Alaya Shrine once we're fixed up."
            el "It's just around the corner."
        elif _return == 5:
            show doctor at pleft2 with qleft
            doctor "Well, hello there.  Your friends are... interesting as always."
        elif _return == 6:
            nurse "I saw an injured woman walking around here."
            nurse "Did the demons get her...?"
        elif _return == 7:
            hide screen header
            $ tbnarrator = 1
            "You go back out into Mikage-Cho."
            window hide
            window auto
            $ tbnarrator = 0
            jump calloverworld
        jump label064
    elif plotprogress == 0:
        scene bg esumiclinic with qdis
        play music doctor fadeout 0.5 fadein 0.5 if_changed
        show screen header
        call screen Clinic3
        if _return == 1:
            show mark animated neutral sad with qleft
            mk "It doesn't bother you that we haven't been to the hospital yet?"
        elif _return == 2:
            show yukino animated neutral smirk with qleft
            yu "Ms. Saeko's technically our upperclassman.  She told me so once."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "I'm rather surprised that the townspeople know so much about St. Hermelin."
        elif _return == 4:
            nurse "My, does that uniform bring back memories!  I'm a St. Hermelin grad myself."
            nurse "One of my old classmates, Saeko Takami, teaches there now.  Do you know her?"
            nurse "Haha, that Saeko... I never pictured her as a teacher!"
        elif _return == 5:
            show doctor at pleft2 with qleft
            doctor "Well, hello there.  Your friends are... interesting as always."
        elif _return == 6:
            hide screen header
            $ tbnarrator = 1
            "You go back out into Mikage-Cho."
            window hide
            window auto
            $ tbnarrator = 0
            jump calloverworld
        jump label064

label label065: #Arcade
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        show elly animated neutral smirk with qleft
        el "Now is not the time to be playing games, Naoya."
        hide elly
        show yukino animated neutral serious with qleft
        yu "We need to get to the Alaya Shrine."
        hide yukino
        jump calloverworld
    if plotprogress == 0:
        show mark animated neutral smirk with qleft
        mk "Yo Naoya, I know you spend all your time here, but don't drag us along too!"
        hide mark
        jump calloverworld

label label066 (location = "Agastya Tree"): #Agastya Ward 2
    scene bg agastyatree with qdis
    play music agastya fadeout 0.5 fadein 0.5
    show screen header
    ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
    hide screen header
    jump calloverworld

label hospitalcheck:
    if plotprogress == 2:
        show elly animated neutral sad with qleft
        el "No, Naoya!"
        el "We must hurry and bring Maki's mother to the school!"
        hide elly with qdis
        jump calloverworld
    if plotprogress == 1:
        jump label083
    if plotprogress == 0:
        jump label067

label label067 (location = "Mikage Hospital"): #Reception
    scene bg hospital1 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    show screen header
    if hospitalscene == 0:
        show nanjo animated neutral serious with qleft
        na "There's some time until our examinations.  Let's visit Maki first, then."
        na "Best not be idle, after all."
        hide nanjo
        show mark animated neutral serious with qleft
        mk "Heh... Cold, man."
        mk "By the way, Maki's in {color=#800000}Room 302{/color}."
        hide mark
        show yukino animated neutral smirk with qleft
        yu "You're pretty well-informed, Masao."
        hide yukino
        show mark animated neutral serious with qleft
        mk "Uh... Shut up!  A friend of mine told me!"
        mk "Yo Naoya, let's just go already!"
        $ hospitalscene = 1
        jump label067
    else:
        call screen Hospital1
        if _return == 1:
            show mark animated neutral serious with qleft
            mk "What're you lookin' at me for?  Hurry and go!"
        elif _return == 2:
            show yukino animated neutral smirk with qleft
            yu "Huh.  Interesting that Masao knew which room Maki was in."
        elif _return == 3:
            show nanjo animated neutral serious with qleft
            na "Hospitals certainly enjoy keeping people waiting.  Don't they know time is money?"
        elif _return == 5:
            "Woman" "I'm sorry.  We're tied up right now, so please wait a little longer."
            "Woman" "Hm?  Maki Sonomura?  Oh, yes, her... She's in room 302."
        elif _return == 6:
            stu "Hoo boy... Know where the police station is?"
            stu "My boyfriend crashed his motorcycle."
            show mark animated neutral serious with qleft
            mk "What's this now?  The police?  You mean the place where Baldy works?"
            mk "Yeah, just head north after you leave the hospital."
            hide mark with qdis
            stu "Exit the hospital and head north... Thanks a bunch!"
        elif _return == 7:
            "Man" "Oww... Testifying about accidents is such a pain.  Talk about bad luck."
        elif _return == 8:
            "Man" "I'm going to work!  To hell with fake hallways and stairs!"
            "Man" "To hell with that little ghost girl!"
            "Man" "If you can't handle such things, you have no place at SEBEC!  Honestly!"
        elif _return == 9:
            "Woman" "I wonder if my honey's okay... Isn't seeing things a sign of overwork?"
        elif _return == 10:
            show yamaoka animated neutral serious with qleft
            ya "Oh dear, oh dear!  I've been spotted."
            ya "I would ask that you keep my presence a secret from the young master..."
        elif _return == 11:
            jump calloverworld
        elif _return == 12:
            jump HospitalNav
    jump label067

label label068: #Examination Room
    scene bg hospital2 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    nurse "Hey!  You have to wait your turn just like everyone else!"
    nurse "Now please leave!"
    jump HospitalNav

label label069: #2F Lobby
    scene bg hospital3 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    call screen Hospital3
    if _return == 1:
        show mark animated neutral serious with qleft
        mk "Man, what's with him calling you Hiroshi?"
    elif _return == 2:
        show yukino animated neutral sad with qleft
        yu "It must be rough on the nurse."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "Does that old man really believe such, or is he toying with us...?"
    elif _return == 4:
        "Old Man" "Look, Akiko, Hiroshi came to visit."
        nurse "That's right, Hiroshi's here..."
        "Old Man" "Thanks for coming all this way, Hiroshi."
        $ choicetext = "Listen to the Old Man?"
        show nchoice at pright zorder 15 with easeinright
        show nchoice onlayer screens zorder 15 at pright
        show fadeblack onlayer screens zorder 3 with qdis
        $ choice1 = "Don't Listen"
        $ choice2 = "Listen"
        call screen choices with qdis
        if _return == 1:
            hide screen choices with qdis
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with qdis
            "Old Man" "I see.  I'm glad to hear you're enjoying school."
        elif _return == 2:
            hide screen choices with qdis
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with qdis
            "Old Man" "Now you listen here, Hiroshi.  A man's soul is a complex thing."
            "Old Man" "The things a person shows to the outside world isn't necessarily what he thinks."
            "Old Man" "You have to dig deep to find out the truth they're hiding..."
    elif _return == 5:
        nurse "Hiroshi seems to be his grandson.  He mistakes me for his daughter, too..."
    elif _return == 6:
        jump HospitalNav
    jump label069

label label070: #2F Nurse's Station
    scene bg hospital4 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    nurse "Hm? Aren't you Maki Sonomura's friend?"
    show mark animated neutral serious with qleft
    mk "Uh..."
    hide mark with qdis
    nurse "You visited her last week too didn't you?  And the week before..."
    show nanjo animated neutral smirk with qleft
    na "Is that so...?  You're unexpectedly nice to her, I see."
    hide nanjo
    show yukino animated neutral smirk with qleft
    yu "Leave him alone, Nanjo."
    hide yukino with qdis
    jump HospitalNav

label label071: #3F Waiting Room
    scene bg hospital5 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    call screen Hospital5
    if _return == 1:
        show mark animated neutral smirk with qleft
        mk "Maki's room is the second one, straight down from here."
    elif _return == 2:
        show yukino animated neutral smirk with qleft
        yu "It was a good call, coming here.  I'm sure Maki will be glad to see us."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "There aren't many at this hospital whom Maki could converse with."
        na "Small wonder she doesn't feel like leaving her room, if that's the case..."
    elif _return == 4:
        "Old Man" "There's a girl on this floor who looked like she was in high school..."
        "Old Man" "But sometimes I hear a little girl's voice from her room."
        "Old Man" "There's only one bed in there... Does she have a sister or someone visiting her?"
    elif _return == 5:
        jump HospitalNav
    jump label071

label label072: #3F Nurse's Station
    scene bg hospital6 with qdis
    play music hospital0 fadeout 0.5 fadein 0.5 if_changed
    call screen Hospital6
    if _return == 1:
        show mark animated neutral sad with qleft
        mk "Oh, crap!  Y'think I should've brought flowers or something?  Well, too late now!"
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "C'mon, Maki's waiting."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "Why is Maki's mother working at THAT company, of all places!?"
    elif _return == 4:
        nurse "I can hardly believe it!  Her only daughter is in the hospital and she hasn't visited even once!"
        nurse "I don't care how busy she is at SEBEC!  She's a failure as a mother!  Poor Maki..."
    elif _return == 5:
        nurse "Are you Maki's friends?  I'm glad you came."
        nurse "You know she's been in and out of the hospital since she was a child, right?"
        nurse "I always worried about her keeping up her friendships..."
    elif _return == 6:
        jump HospitalNav
    jump label072

label label073: #Maki's Room
    scene bg hospitalmaki1 with qdis
    play music maki0 fadeout 0.5 fadein 0.5
    show doctor at pleft2 with qleft
    doctor "I have to go...but you should try to get some fresh air sometimes."
    doctor "It's good for you."
    hide doctor with qdis
    nurse "That's right, Maki.  Why don't we go for a walk tomorrow?"
    show maki with qleft
    ma "..."
    $ tbnarrator = 1
    n "{color=#ebffdb}>Maki Sonomura (Nickname: Maki)\nA chronically ill classmate who's been hospitalized for over a year now.{/color}"
    $ tbnarrator = 0
    hide maki
    show doctor at pleft2 with qleft
    doctor "Oho, it seems your real medication has arrived.  I'll leave you kids be."
    scene bg black with qdis
    scene bg hospitalmaki2 with qdis
    play music maki1 fadeout 0.5 fadein 0.5
    show maki animated sick smirk with qleft
    ma "Naoya... you all came... Thank you."
    ma "You're so thoughtful, Masao."
    hide maki
    show nanjo animated neutral serious with qleft
    na "What do you mean?"
    hide nanjo
    show maki animated sick serious with qleft
    ma "I told Masao I wanted to see everyone when he was here last time..."
    show maki animated sick smirk
    ma "Isn't that why you all came?"
    hide maki
    show yukino animated neutral smirk with qleft
    yu "...Yes it is."
    if Yuko == True:
        show yukino animated neutral serious
        extend "  Oh, and Yuko said she'll come by to return the book she borrowed."
        yu "\"Gate to Paradise,\" I think it was."
        hide yukino
        show maki animated with qleft
        ma "Ah... That's okay.  I've read it so many times, I practically have it memorized."
        hide maki
        show yukino animated neutral serious with qleft
        yu "Alright, I'll tell her next time I see her."
    show yukino animated neutral serious
    extend "  So how've you been?  You doing okay?"
    hide yukino
    show maki animated sick smirk with qleft
    ma "Uh-huh.  I'm doing much better.  I wonder if it's because of that good dream..."
    ma "It's hard to remember, but I keep dreaming of a really nice man... He's like a father..."
    hide maki
    show yukino animated neutral smirk with qleft
    yu "Like that doctor?  He seemed nice."
    hide yukino
    show maki animated sick sad with qleft
    ma "...I don't like him..."
    hide maki
    show mark animated neutral sad with qleft
    mk "Did he do somethin' to you!?"
    hide mark
    show maki animated sick sad with qleft
    ma "No, that's not it... I just...don't like doctors..."
    hide maki
    show mark animated neutral serious with qleft
    mk "Well, let's talk about other stuff, then.  Hey, how about your mom? How's she doin' at SEBEC?"
    hide mark
    show maki animated sick serious with qleft
    ma "She's not my mom!  She cares more about her job than me!  She doesn't care about me at all..."
    hide maki
    show mark animated neutral sad with qleft
    mk "S-Sorry..."
    hide mark
    show maki animated sick sad with qleft
    ma "Oh... it's all right."
    show maki animated sick serious
    ma "Ngh!"
    scene bg hospitalmaki3
    play music uhoh fadeout 0.5 fadein 0.5
    show maki animated sick sad with qleft
    ma "N-Noooo!"
    hide maki
    show mark animated neutral sad with qleft
    mk "Maki!? What's wrong? Hey!"
    hide mark
    show yukino animated neutral sad with qleft
    yu "This isn't good! Call a doctor!"
    hide screen header
    scene bg black with qdis
    scene bg icu1 with qdis
    play music maki0 fadeout 0.5 fadein 0.5
    $ tbnarrator = 1
    "The group waits outside the ICU, with Maki just inside after the doctors had taken her within."
    $ tbnarrator = 0
    na "I do hope it's nothing serious."
    mk "...Dammit..."
    $ tbnarrator = 1
    "As the group waits, the building starts to rumble."
    $ tbnarrator = 0
    scene bg icu2 with qdis
    na "Hm? An earthquake?"
    $ tbnarrator = 1
    "The benches shake and the items on the wall rattle before one falls to the ground, shattering."
    $ tbnarrator = 0
    scene bg icu3 with qdis
    play music uhoh fadeout 0.5 fadein 0.5
    mk "Woah! It's a big one!"
    yu "The hell!?  Hold on!"
    $ tbnarrator = 1
    "After a few moments, the rumbling stops."
    $ tbnarrator = 0
    na "It seems to have subsided."
    $ tbnarrator = 1
    "Fearing for Maki, Mark rushes to the ICU doors."
    $ tbnarrator = 0
    scene bg icu4 with qdis
    mk "Maki!"
    $ tbnarrator = 1
    "After pushing the door open, Mark finds there's just a wall behind the door."
    $ tbnarrator = 0
    mk "Whoa! Wh-what the hell!? Where'd the room go?"
    na "What...How is that...?  No, I was positive that was the ICU a moment ago!"
    scene bg icu5 with qdis
    $ tbnarrator = 1
    "In the distance, a woman screams, and everyone turns to face the source."
    $ tbnarrator = 0
    na "That scream...It came from downstairs!  Let's go!"
    $ tbnarrator = 1
    "Everyone darts downstairs after the source of the scream."
    $ tbnarrator = 0
    scene bg black with qdis
    scene bg awakening with qdis
    play music hospital1 fadeout 0.5 fadein 0.5
    show screen header
    $ location = "Mikage Hospital?"
    "Man" "F-Fresh meat... Meat is heeeeere!"
    show yukino animated neutral serious with qleft
    yu "Wh-What's with these guys?"
    hide yukino
    nurse "Th-The dead patients suddenly got up and walked..."
    nurse "That old man rescued me and...Nooooo!"
    $ tbnarrator = 1
    "The nurse panicks and runs off."
    $ tbnarrator = 0
#    scene bg awakening2 with qdis
    show mark animated neutral serious with qleft
    mk "What!?  These guys were dead?  Is this for real!?"
    hide mark
#    scene bg awakening3 with qdis
    show nanjo animated neutral sad with qleft
    na "Y...Yamaoka...?  Yamaoka!"
    show nanjo animated neutral serious
    na "You bastards...How DARE you!?"
    hide nanjo
    $ tbnarrator = 1
    "Filled with anger, Nanjo attacks the undead, and his friends come to support him."
    $ tbnarrator = 0
#    show awakening4 at pright with zoomin
    play music awakening fadeout 0.5 fadein 0.5
    show nanjo animated neutral serious with qleft
    na "I'll never forgive you bastards!"
    hide nanjo
    show yukino animated neutral serious with qleft
    yu "Careful, guys!"
    hide yukino
    show mark animated neutral serious with qleft
    mk "How the hell are we supposed to fight somethin' that's already dead!?"
    hide mark
    $ tbnarrator = 1
    "As one of the undead comes forward to attack Naoya, something incredible happens."
#    hide awakening4 with zoomout
#    show awakening5 at pright with zoominout
    "A ghostly presence emerges from Naoya."
    $ tbnarrator = 0
    "Persona" "Thou art I... and I am thou..."
    "Persona" "From the sea of thy soul, I cometh... I shall lend you my strength..."
    $ tbnarrator = 1
    "Somehow, the 'persona' attacks, striking and destroying one of the undead patients."
#    hide awakening5 with zoomout
#    show awakening6 at pright with zoominout
    "A similar-but-different presence emerges from Mark, and strikes down another of the undead."
#    hide awakening6 with zoomout
#    show awakening7 at pright with zoominout
    "From within Yukino, a new form emerges, energy emerging from it to destroy another."
#    hide awakening7 with zoomout
#    show awakening8 at pright with zoominout
    "Lastly, Nanjo himself summons one, reddish energy surrounding the last undead before it too, vanishes."
    $ tbnarrator = 0
#    hide awakening8 with zoomout
    scene bg nanjoyamaoka with qdis
    play music ohno fadeout 0.5 fadein 0.5
#    show nanjo animated neutral sad with qleft
    na "Yamaoka... Don't go... You wouldn't leave me behind, right? Right, Yamaoka?"
#    hide nanjo
#    show yamaoka animated bloody serious with qleft
    ya "Oh, young master... Don't be so sad... It spoils your handsome face..."
    ya "You're a fine Japanese man... And a man must stand on his own someday..."
    ya "It seems that this... will be the last service I can provide for you..."
#    hide yamaoka
#    show nanjo animated neutral sad with qleft
    na "No!  No no no!  I won't let you leave me!  Hang in there, Yamaoka!"
#    hide nanjo
#    show yamaoka animated bloody sad with qleft
    ya "It's time I said farewell... Just one last thing... Please promise me, young master..."
    ya "Promise to become the No. 1 man in the country and carry Japan on your back! *cough*"
#    hide yamaoka
#    show nanjo animated neutral sad with qleft
    na "...Of course... Of course I will.  When that time comes, you'll see. So, until then--"
#    hide nanjo
#    show yamaoka animated bloody sad with qleft
    ya "That's my young master... I will always be... in your heart..."
#    hide yamaoka
#    show nanjo animated neutral sad with qleft
    na "Yamaoka?  Hey!  Answer me... I'm begging you... Yamaoka!"
#    hide nanjo
    scene bg awakening with qdis
    show yukino animated neutral sad with qleft
    yu "Nanjo..."
    hide yukino
    show mark animated neutral sad with qleft
    mk "Let him be alone..."
    hide mark with qdis
    pause 1.5
    play music hospital1 fadeout 0.5 fadein 0.5
    show mark animated neutral serious with qleft
    mk "Hey Naoya... Could you hear their voices?  That thing said it was me."
    hide mark
    show yukino animated neutral serious with qleft
    yu "I heard it, too...Think it was that Persona thing?"
    hide yukino
    show mark animated neutral serious with qleft
    mk "It said it would lend us power, so I kinda doubt it's hostile."
    mk "If we're lucky, maybe it'll listen to what we tell it..."
    mk "I guess we might as well go on calling it '{color=#800000}Persona{/color}'."
    hide mark
    show yukino animated neutral serious with qleft
    yu "That's how it felt to me, too."
    yu "...I have a bad feeling about this. Let's go."

label label074: #Ideal 2F Waiting Room
    scene bg idealhospital0 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital0
    if _return == 1:
        show mark animated neutral sad with qleft
        mk "I didn't think he was gonna cry... He must've really loved that old guy."
    elif _return == 2:
        show yukino animated neutral sad with qleft
        yu "Nanjo seemed like a little boy in front of that old guy..."
        yu "Failing to protect the ones you love... Nothing hurts worse than that."
    elif _return == 3:
        show nanjo animated neutral sad with qleft
        na "Yamaoka... What should I do?  Without you, I'm all alone... No one is here to encourage me..."
        na "No one...will stand by me..."
    elif _return == 4:
        scene bg black
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        "Naoya and the others leave the room, with Yukino ensuring Nanjo stays moving."
        "They are attacked by more of the undead patients as they traverse the hallways."
        "Soon, they arrive at a door and let themselves inside, thankful for the slight reprieve."
        jump label075
    jump label074

label label075: #Ideal Hospital Room 1
    scene bg idealhospital1 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital1
    if _return == 1:
        show mark animated neutral smirk with qleft
        mk "With this power, we should be able to find out why this is happenin'!"
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "What is this bullshit!?  Whoever's doing this is gonna pay!  I'll get this place back to normal or die trying!"
    elif _return == 3:
        show nanjo animated neutral sad with qleft
        na "If only... if only I'd made certain he went home..."
    elif _return == 4:
        show doctor at pleft2 with qleft
        doctor "Dammit, why can't I get to the ICU!?  There's a patient in there! I have to treat the Sonomura girl...!"
    elif _return == 5:
        nurse "The TV's not working, and the phone's dead too!  What in the world is going on!?"
    elif _return == 6:
        nurse "I'd treat your wounds at the examination room, but... I can't find it!"
        nurse "Nothing in this hospital is where I remember it!"
    elif _return == 7:
        scene black with qdis
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        "After the stop in the nurse's office, Naoya and his allies move further into the Hospital."
        n "Surprisingly, they find themselves able to hold a few conversations with some of the demons, and Mark manages to get a 'Spell Card'."
        "However, they manage to find shelter within a room that, strangely, holds an Agastya Tree."
        $ tbnarrator = 0
        jump label076
    jump label075

label label076 (location = "Agastya Tree"):
    scene bg agastyatree with qdis
    play music agastya fadeout 0.5 fadein 0.5
    show screen header
    ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
    scene bg black with qleft
    $ location = "Mikage Hospital?"
    play music hospital1 fadeout 0.5 fadein 0.5
    $ tbnarrator = 1
    "Despite being on the second floor, the students cannot find a way down, and head back upstairs."
    "After fighting through a few more demons, they manage to make it to another nurse's station..."
    $ tbnarrator = 0
    jump label077

label label077 (location = "Mikage Hospital?"):
    scene bg idealhospital2 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital2
    if _return == 1:
        show mark animated neutral serious with qleft
        mk "Dammit!  If only we had a hint or something!"
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "It's like even the air's changed... I'm finding it hard to breathe."
    elif _return == 3:
        show nanjo animated neutral sad with qleft
        na "...I'm sorry, Naoya.  I'm not...thinking as quickly as usual."
    elif _return == 4:
        nurse "There's a strange haze I can see through the window... It's covering the town."
        nurse "You don't think we're trapped here like in the horror novels, do you?"
    elif _return == 5:
        "Old Man" "Oh, hello again, Hiroshi!  Did you come to listen to my stories?"
        "Old Man" "I have something to say that I think you may need to hear."
        "Old Man" "Stay calm, and think carefully before making a move."
        "Old Man" "If you do... you'll arrive at the truth come what may."
        "Old Man" "Say, Akiko?  Is lunch ready yet?"
    elif _return == 6:
        scene black with qdis
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        n "After leaving the room with the nurse and the old man, the group navigate the twisted hallways of the hospital."
        n "Dead ends abound, and nothing seems to lead anywhere that makes sense, but eventually they end up back where they started."
        "They come across Maki's now-empty room..."
        $ tbnarrator = 0
        jump label078
    jump label077

label label078: #Maki's Room (Ideal Hospital)
    scene bg idealhospital3 with qdis
    play music maki0 fadeout 0.5 fadein 0.5 if_changed
    call screen IHospital3
    if _return == 1:
        show mark animated neutral sad with qleft
        mk "I can still feel Maki here... Hang on, Maki.  We'll find you."
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "I'm worried about Maki too, but let's get to the streets.  I have a bad feeling..."
    elif _return == 3:
        show nanjo animated neutral sad with qleft
        na "...Yamaoka."
    elif _return == 4:
        $ tbnarrator = 1
        ">It's the painting called 'Gate To Paradise' that Maki won an award for."
        ">You can sense Maki's pain just by looking at it..."
        $ tbnarrator = 0
    elif _return == 5:
        scene black with qdis
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        n "Leaving Maki's room with heavy hearts, the group passes by a set of stairs down, and Nanjo seems to regain some of his usual airs as they walk."
        n "Still, the demons present a constant threat, reaching another dead end, they enter into another waiting room for a breather."
        $ tbnarrator = 0
        jump label079
    jump label078

label label079: #2nd Floor Waiting Room (Ideal Hospital)
    scene bg idealhospital4 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital4
    if _return == 1:
        show mark animated neutral serious with qleft
        mk "Hey, you think the other guys have this power too?"
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "This power's kinda unnerving, but it looks like it'll come in handy."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "I'll figure this out... There's nothing I can't do if I put my mind to it!"
    elif _return == 4:
        "Old Man" "I'm prepared for the worst, but I'm worried about my little grandson..."
        "Old Man" "He should be at school... I hope nothing's happened there."
    elif _return == 5:
        scene black with qdis
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        n "Now concerned about their school as well, the group sets back down the stairs they'd passed by before as there is no other path."
        n "Confronted with multiple dead ends, they finally manage to make their way into another room with yet another one of those strange trees."
        $ tbnarrator = 0
        jump label080
    jump label079

label label080 (location = "Agastya Tree"):
    scene bg agastyatree with qdis
    play music agastya fadeout 0.5 fadein 0.5
    show screen header
    ag "Young ones... Your presence is welcome. \nTake care on your journey, young ones..."
    scene bg black with qdis
    $ location = "Mikage Hospital?"
    play music hospital1 fadeout 0.5 fadein 0.5
    $ tbnarrator = 1
    n "After leaving the Agastya Tree, the four students make their way to another dead end, fighting demons as they come closer."
    n "They're starting to become uncomfortably used to wielding their personas, and another flight of stairs down yields another set of dead ends."
    n "Around one, the four of them manage to get into the very exam room they had signed in to access when they'd arrived here."
    $ tbnarrator = 0
    jump label081

label label081 (location = "Mikage Hospital?"):
    scene bg idealhospital5 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital5
    if _return == 1:
        show mark animated neutral serious with qleft
        mk "I wonder if there are other patients besides Maki in trouble right now..."
    elif _return == 2:
        show yukino animated neutral smirk with qleft
        yu "I always thought you were a pushover, Naoya... I'm surprised how calm you are."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "...Hm?  Yes, what is it?"
    elif _return == 4:
        nurse "I can't get in touch with the patients!  What am I supposed to do? Can't you do something!?"
        nurse "...I'm sorry.  I'm asking the impossible.  I'm just so confused."
    elif _return == 5:
        show doctor at pleft2 with qleft
        doctor "Are you all right?  Here, let me take a look... I want to save as many people as I can."
        $ tbnarrator = 1
        "HP, SP and Status restored!  Or at least they would be if you had those!"
        $ tbnarrator = 0
        doctor "Try not to push yourself too hard."
    elif _return == 6:
        scene black with qdis
        play music hospital1 fadeout 0.5 fadein 0.5
        $ tbnarrator = 1
        n "With only one path left to follow once they leave, the group makes their way through the twisted passages of the hospital."
        n "More demons rise up to stop them, but by now, the students are capable at dealing with the threats, and make their way to the exit."
        $ tbnarrator = 0
        jump label082
    jump label081

label label082 (location="Hospital Entrance"): #iHospital Entrance
    scene bg idealhospital6a with qdis
    play music uhoh fadeout 0.5 fadein 0.5
    show yukino animated neutral serious with qleft
    yu "Naoya! This one's still alive!  Gimme a hand here!"
    hide yukino
    show nanjo animated neutral serious with qleft
    na "We haven't time to waste here, Naoya!  It's too late for her, but not for us!"
    hide nanjo
    show mark animated neutral serious with qleft
    mk "Yo, Naoya!  The monsters are just around the corner!"
    hide mark with qdis
    nurse "I...I'm not going to make it... You kids... g-get out of here..."
    show yukino animated neutral sad with qleft
    yu "Don't give up!"
    show yukino
    $ choicetext = "I could really use a hand, Naoya!"
    show nchoice at pright zorder 15 with easeinright
    show nchoice onlayer screens zorder 15 at pright
    show fadeblack onlayer screens zorder 3 with qdis
    $ choice1 = "Help Her"
    $ choice2 = "Don't Help Her"
    call screen choices with qdis
    if _return == 1:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show yukino animated neutral smirk
        yu "Okay, you take that side!"
    elif _return == 2:
        hide screen choices with qdis
        hide fadeblack onlayer screens
        hide nchoice onlayer screens
        hide nchoice
        with qdis
        show yukino animated neutral serious
        yu "Are you serious!?  But she's still alive!"
        yu "You're telling me to abandon her!?"
        hide yukino
        show nanjo animated neutral sad with qleft
        na "...I don't want to leave Yamaoka behind, either.  But we don't have a choice!"
        show nanjo neutral
        $ choicetext = "We have to go!"
        show nchoice at pright zorder 15 with easeinright
        show nchoice onlayer screens zorder 15 at pright
        show fadeblack onlayer screens zorder 3 with qdis
        $ choice1 = "Don't Leave"
        $ choice2 = "Leave"
        call screen choices with qdis
        if _return == 1:
            hide screen choices with qdis
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with qdis
            show nanjo animated neutral serious
            na "Tsk... Don't blame me when you end up part of the problem instead of the solution."
        if _return == 2:
            hide screen choices with qdis
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with qdis
            show nanjo animated neutral serious
            na "Yukino!  Masao!  Let's go!"
    hide yukino
    hide nanjo
    show mark animated neutral serious with qleft
    mk "It's no good!  They're coming!"
    scene bg idealhospital6b with qdis
    play music elly fadeout 0.5 fadein 0.5
    show elly animated neutral smirk with qleft
    el "Oh, good day."
    show elly animated neutral serious
    el "Oh, my!  There are demons here too?"
    hide elly
    show nanjo animated neutral serious with qleft
    na "Eriko!  Get back!"
    hide nanjo
    show elly animated neutral serious with qleft
    el "No worries!  I may not look it, but I'm a rather capable fencer."
    hide elly
    show yukino animated neutral serious with qleft
    yu "Eriko!  This is no ordinary enemy!"
    hide yukino
    show mark animated neutral smirk with qleft
    mk "Sheesh, that girl's crazy!"
    hide mark with qdis
    play music awakening fadeout 0.5 fadein 0.5
    $ tbnarrator = 1
    n "Mark strikes one of the undead with his persona, knocking it down and into pieces, while the remaining one comes for Elly."
    "As it does, she feels a similar rush of energy to the rest."
    show idealhospital6c at pright with zoomin
    n "Her persona manifests, unleashing a wave of energy toward the remaining zombie, searing it with bright light and vanquishing it."
    $ tbnarrator = 0
    hide idealhospital6c with zoomout
    scene bg idealhospital6 with qdis
    play music hospital1 fadeout 0.5 fadein 0.5
    show elly animated neutral serious with qleft
    el "Was that Nike...?  The Greek goddess of victory... It's me... and I'm it..."
    hide elly
    show yukino animated neutral serious with qleft
    yu "Eriko?  Hey!  Are you okay?"
    hide yukino
    show elly animated neutral serious with qleft
    el "Nike... The archetypal portrayal of Christian angels... It's me... and I'm it..."
    hide elly
    show mark animated neutral serious with qleft
    mk "No good. She's completely gone."
    hide mark
    show yukino animated neutral serious with qleft
    yu "Eriko!  Snap out of it!"
    hide yukino
    show elly animated neutral serious with qleft
    el "*gasp* I-I'm sorry... I'm all right.  I am an angelic bringer of victory!"
    show elly animated neutral smirk
    el "From now on, you have my protection!"
    hide elly
    show mark animated neutral smirk with qleft
    mk "...You idiot.  We can do it too."
    hide mark
    show elly animated neutral serious with qleft
    el "R-Really...?  So I'm not the only one who was chosen..."
    hide elly
    show nanjo animated neutral serious with qleft
    na "Eriko... you dreamt of the butterfly, didn't you?"
    hide nanjo
    show elly animated neutral serious with qleft
    el "How do you know about that?  I've seen it quite often in my dreams..."
    show elly animated neutral sad
    el "Ever since I played the Persona game."
    hide elly
    show nanjo animated neutral serious with qleft
    na "Just as I thought.  That dream must be the cause of the phenomenon..."
    hide nanjo
    show mark animated neutral serious with qleft
    mk "That aside, why'd you come here?  Is it like this outside too?"
    hide mark
    show elly animated neutral sad with qleft
    el "Yes... There are demons everywhere.  And it's impossible to leave town."
    el "I looked everywhere, but it seems that the school is the only safe place."
    hide elly
    show yukino animated neutral serious with qleft
    yu "Oh?  The school's safe?  Let's go back there, Naoya."
    hide yukino
    show elly animated neutral serious with qleft
    el "Oh, but I nearly forgot!  We should go to the {color=#800000}Alaya Shrine{/color} first."
    show elly animated neutral sad
    el "Maki's mother is hurt.  She collapsed there..."
    hide elly
    show mark animated neutral serious with qleft
    mk "What!?  Dude, why didn't you say so before!?  C'mon Naoya, let's go!"

label label083: #Hospital Reception
    scene bg idealhospital6 with qdis
    play music hospital2 fadeout 0.5 fadein 0.5
    call screen IHospital6
    $ plotprogress = 1
    if _return == 1:
        show mark animated neutral sad with qleft
        mk "Maki... We'll come back for you, I swear..."
    elif _return == 2:
        show yukino animated neutral serious with qleft
        yu "All right, let's save Maki's mom and make a run for the school."
    elif _return == 3:
        show nanjo animated neutral serious with qleft
        na "You're all so softhearted... Anyway."
        na "The Personas, this change in town... It all seems too pat.  What could be causing all this?"
    elif _return == 4:
        show elly animated neutral serious with qleft
        el "Alaya Shrine isn't far from the school.  We should have no problems."
    elif _return == 5:
        jump calloverworld
        #scene black with qdis
        #"End of the demo~!"
        #$ MainMenu(confirm=False)()
        $ plotprogress = 1
    jump label083

####Navigation Labels######

label calloverworld:
    if ward == 1:
        play music overworld1 if_changed
        show bg wardone with qdis
        call screen OverworldMap1(_with_none=False) with qdis
    if ward == 2:
        play music overworld2 if_changed
        show bg wardtwo with qdis
        call screen OverworldMap2(_with_none=False) with qdis

label wardonetotwo:
    $ ward = 2
    show bg wardtwo
    call screen OverworldMap2 with pushup

label wardtwotoone:
    $ ward = 1
    show bg wardone
    call screen OverworldMap1 with pushdown

label callHermelinFloor1:
    hide hf1
    hide hf2
    hide hs
    play music schooldays volume 0.4 if_changed
    if floor == 2:
        $ tbnarrator = 1
        "You move to the first floor of the school"
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "First Floor"
        $ floor = 1
        show hf1 zorder 0 with moveinbottom
        $ tbnarrator = 0
        call screen HermelinFloor1(_with_none=False)
    elif floor == 4:
        $ tbnarrator = 1
        "You move to the first floor of the school"
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "First Floor"
        $ floor = 1
        show hf1 zorder 0 with moveinleft
        $ tbnarrator = 0
        call screen HermelinFloor1(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "First Floor"
        $ floor = 1
        show hf1 with qdis
        $ tbnarrator = 0
        call screen HermelinFloor1(_with_none=False) with qdis

label callSportsBuilding:
    hide hf1
    hide hs
    play music schooldays volume 0.4 if_changed
    if floor == 1:
        $ tbnarrator = 1
        "You move to the Sports Building of the school."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Sports Building"
        $ floor = 4
        show hs zorder 0 with moveinright
        $ tbnarrator = 0
        call screen HermelinSportsBuilding(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Sports Building"
        $ floor = 4
        show hs with qdis
        $ tbnarrator = 0
        call screen HermelinSportsBuilding(_with_none=False)
label callHermelinFloor2:
    hide hf1
    hide hf2
    hide hf3
    play music schooldays volume 0.4 if_changed
    if floor == 1:
        $ tbnarrator = 1
        "You move to the second floor of the school."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Second Floor"
        $ floor = 2
        show hf2 zorder 0 with moveintop
        $ tbnarrator = 0
        call screen HermelinFloor2(_with_none=False)
    elif floor == 3:
        $ tbnarrator = 1
        "You move to the second floor of the school."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Second Floor"
        $ floor = 2
        show hf2 zorder 0 with moveinbottom
        $ tbnarrator = 0
        call screen HermelinFloor2(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Second Floor"
        $ floor = 2
        show hf2 with qdis
        $ tbnarrator = 0
        call screen HermelinFloor2(_with_none=False)
label callHermelinFloor3:
    hide hf3
    hide hf2
    play music schooldays volume 0.4 if_changed
    if floor == 2:
        $ tbnarrator = 1
        "You move to the third floor of the school."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Third Floor"
        $ floor = 3
        show hf3 zorder 0 with moveintop
        $ tbnarrator = 0
        call screen HermelinFloor3(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        window auto
        hide screen header
        show fadeblack with qdis
        $ location = "Third Floor"
        $ floor = 3
        show hf3 zorder 0 with qdis
        $ tbnarrator = 0
        call screen HermelinFloor3(_with_none=False)

label HospitalNav:
    show fadeblack with qdis
    show hn with moveinleft
    call screen HospitalNav(_with_none=False)

return
