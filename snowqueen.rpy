label SnowQueenMask:
    scene bg black with dissolve #update with the Gym Storage room
    #play music #update
    "It's a box sealed with talismans."
    hide screen header with dissolve
    $ choicetext = "Open it?"
    show nchoice at pright zorder 15 with easeinright
    show nchoice onlayer screens zorder 15 at pright
    show fadeblack onlayer screens zorder 3 with dissolve
    $ choice1 = "What can it hurt?"
    $ choice2 = "Might not be a good idea."
    call screen choices with dissolve
    if _return == 1:
        hide screen choices with dissolve
        hide fadeblack onlayer screens
        hide nchoice onlayer screens
        hide nchoice
        with dissolve
        show screen header with dissolve
        "Obtained the Snow Queen Mask!"
        $ plotprogress = 7
        scene bg black with dissolve #update with Gymnasium and 1 teacher
        #play music #update
        tea "Oh, Naoya!  You're still here!?  I'm closing off the gym."
        tea "You should head to the main building."
        tea "I haven't heard of any demons getting in, yet, but who knows when they will?"
        tea "Hey... where did you get that mask...?  ...Nah, it can't be the same one."
        tea "Anyway, you should get out of here."
        scene bg black with dissolve
        n "Naoya makes his way back to the school from the Club Building..."
    if _return == 2:
        n "Naoya leaves the box alone."
        jump label011

label label084: #Snow Queen full start
    scene bg black with dissolve #update with Passageway and Maki/Mark leaving
    #play music #update
    n "As Naoya enters the passageway back to the main part of the school, he sees several of his friends by the hole in the wall."
    show yukino animated neutral serious with dissolve
    yu "Hey Masao!  Wait!"
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "You don't even know if that's really Maki!"
    hide ayase with dissolve
    n "Mark and Maki leave through the hole in the wall without another word."
    n "Ayase runs over to Naoya."
    show ayase animated neutral sad with dissolve
    ay "Omigod, Naoya!  Mark's in big trouble!"
    hide ayase with dissolve
    n "Yukino moves closer to Naoya as well."
    show yukino animated neutral serious with dissolve
    yu "Kei was hurt, so Masao, Hidehiko, and Eriko brought him back here."
    show yukino animated neutral sad
    yu "But then..."
    hide yukino
    show ayase animated neutral serious with dissolve
    ay "Maki showed up out of nowhere!  Isn't she supposed to be in the hospital!?"
    ay "Something's seriously wrong here!"
    hide ayase with dissolve
    n "Ms. Saeko enters the passageway from the school."
    show saeko animated neutral serious with dissolve
    sa "I heard Masao came back!"
    hide saeko
    show yukino animated neutral sad with dissolve
    yu "Y-yeah, but..."
    hide yukino with dissolve
    show fadeblack onlayer screens zorder 3 with dissolve
    n "Yukino explains the situation to Ms. Saeko."
    hide fadeblack onlayer screens
    show saeko animated neutral sad with dissolve
    sa "So he and Maki went outside together?  Oh, I have to bring them back!"
    hide saeko
    show yukino animated neutral serious with dissolve
    yu "Wait, Ms. Saeko!  If something happens to you, what'll the people here do?  Let us go instead!"
    hide yukino
    show saeko animated neutral smirk with dissolve
    sa "Oh, good point, Yukino!  Thanks...  Hm?"
    show saeko animated neutral serious
    sa "What's that you have there, Naoya...?  That... that mask...!"
    sa "Goodness... I didn't think it was still lying around here..."
    hide saeko
    n "Ms. Saeko takes the mask from you."
    show saeko animated neutral serious with dissolve
    sa "It reminds me of my high school days... I wore this mask when I was in a play called, 'The Snow Queen'."
    scene bg SQ1 with dissolve
    #play music #update
    n "Once upon a time, there was an evil demon.  And one day, this demon made a mirror..."
    n "The mirror blurred out the beautiful things of the world and made the ugly things clear."
    n "The demon climbed to heaven, intending to do mischief to God with the mirror, but the mirror broke on the way up."
    n "The countless splinters it broke into rained down upon the earth.  And that is how it all began."
    scene bg SQ2 with pushleft
    n "There lived a boy named Kay and a girl named Gerda, and the two were close friends."
    n "But one day, tiny splinters of the mirror got into Kay's eyes and heart."
    n "The splinters caused Kay's heart to grow cold and his eyes to see only ugly things."
    n "He even began to tease Gerda, whom he cared so much for."
    scene bg SQ3 with pushleft
    n "On a snowy winter day... A big, white sleigh appeared in front of Kay, who was playing with his sled at the market square."
    n "And the beautiful woman on that white sleigh took him away."
    n "Little did he know that the woman was the Snow Queen!"
    n "That was how Kay came to the Snow Queen's Ice Castle, far to the north."
    scene bg SQ4 with pushleft
    n "Gerda learned of Kay's disappearance, and despite her sorrow, she decided to embark on a journey to find him."
    n "Along the way, she overcame many hardships and obstacles with the warm help of the people she met."
    n "At last, Gerda's love for Kay and her unwavering courage led her to the Ice Castle."
    scene bg SQ5 with pushleft
    n "What Gerda saw at the end of her journey was the half-frozen Kay, who had forgotten her completely."
    n "Gerda's warm tears gently covered him, melting his heart."
    n "Upon regaining himself, Kay burst into tears, washing away the splinter of the mirror in his eye."
    n "Hand in hand, the two left Ice Castle... And lived at home happlily ever after."
    scene bg black with dissolve #update with Passageway and Maki/Mark leaving
    #play music #update
    show ayase animated neutral serious with dissolve
    ay "It's a neat-looking mask."
    hide ayase
    show saeko animated neutral serious with dissolve
    sa "Yes, but some say it's cursed.  ...I guess I can see why."
    show saeko animated neutral sad
    sa "It's because of this that my friend was..."
    hide saeko
    show ayase animated neutral sad with dissolve
    ay "C-C'mon, Ms. Saeko!  Cut it out!  We've got enough to be scared of..."
    ay "That mask gives me the creeps!  Why don't you just throw it away?"
    hide ayase
    show saeko animated neutral smirk with dissolve
    sa "Oh, sorry about that!  It's just a silly school legend.  'Whoever wears it, dies'?  Ha!"
    sa "I wore it, and I'm okay, aren't I?  See?  So it's better if I went looking for those two!"
    hide saeko
    n "Ms. Saeko, to illustrate the point, dons the mask."
    show saeko animated neutral smirk with dissolve #update with mask
    sa "I've got Lady Luck on my side."
    pause 0.3
    sa "......?"
    pause 0.3
    #play updated scary music
    n "Ms. Saeko suddenly gasps, reaching her hands up toward the mask."
    show saeko animated neutral sad with dissolve #update with mask
    sa "Aaaaaaaaaaaaagh!"
    hide saeko
    show yukino animated neutral sad with dissolve
    yu "Ms. Saeko!?  What's wrong!?"
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Wh-What's going on!?"
    #update with Snow Queen Cutscene
    scene bg black #update with frozen courtyard
    #play creepy music
    show ayase animated neutral sad with dissolve
    ay "Owww... Huh?  Uh... where am I?"
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "Hey... This is the courtyard!  What the hell's going on here!?"
    hide yukino
    show ayase animated neutral serious with dissolve
    ay "Whoa!  Look!"
    hide ayase
    #update with showing Ms. Saeko as the Snow queen again
    show yukino animated neutral sad with dissolve
    yu "Ms. Saeko!"
    hide yukino
    n "Yukino attempts to approach Ms. Saeko, but large pillars of ice prevent her from getting closer."
    show yukino animated neutral serious with dissolve
    yu "What the--!?"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sa "Hahaha... Finally!  I've been waiting so long!"
    hide saeko
    show yukino animated neutral sad with dissolve
    yu "Ms. Saeko...?"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sa "Saeko?  Oh... I see what's happening.  Poor Saeko... Hahahah."
    hide saeko
    show yukino animated neutral sad with dissolve
    yu "Huh?  But you are Saeko!  Are you okay!?"
    show yukino animated neutral serious
    yu "Did you trip and hit your head or something?"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sa "Hahaha... 'I wore it, and I'm okay,' eh?  Teeheehee... Ahahaha!"
    sa "That's the Saeko I remember so well.  Self-confident... self-centered..."
    sa "She'd step on anyone to get to be the center of attention."
    hide saeko
    show yukino animated neutral serious with dissolve
    yu "What's wrong with you!?  Stop with the jokes, 'cause they aren't funny!"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sa "Jokes?  Look around you.  Hahaha... you think this is a joke?"
    sa "Beautiful, isn't it?  A peaceful, perfectly still landscape."
    sa "You'll all be dressed in ice and stay beautiful forever.  So come on over..."
    hide saeko
    show ayase animated neutral sad with dissolve
    ay "What are you saying!?  You're our teacher!  This is just..."
    hide ayase
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sa "Oh, what a lovely girl.  Hahaha... Come closer, girl, and I'll give you ageless beauty."
    hide saeko
    show yukino animated neutral serious with dissolve
    yu "Don't do it, Ayase!  It's the mask... It must have taken her over!"
    yu "Okay, monster, you lay one finger on Ms. Saeko and your ass is grass!"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    msk "'Taken her over'?  That's not very nice.  Tell me, who was it who undid the seal on the mask?"
    msk "Who put it on without thinking twice?  Not to mention...isn't it rude to go around calling people monsters?"
    msk "I think I'd prefer... the Snow Queen.  Very fitting for this mask, isn't it?"
    sq "Hahaha..."
    hide saeko
    show yukino animated neutral serious with dissolve
    yu "Can it!  What do you want with Ms. Saeko!?"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sq "What a reckless young lady.  Your teacher is going to be... a sacrfice."
    hide saeko
    show ayase animated neutral sad with dissolve
    ay "A... A sacrifice?"
    hide ayase
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sq "Yes, that's right.  Saeko is so full of hope.  If I offer her as a sacrifice..."
    sq "The stillness of despair--the Eternal Night--is sure to descend."
    hide saeko
    show ayase animated neutral serious with dissolve
    ay "Huh...?  Does that mean everyone's gonna get frozen?  I hate being cold!"
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "That's not gonna happen!  I'm taking back Ms. Saeko, right now!"
    hide yukino
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sq "Well, aren't you brave?  Fine... you can have her.  But Saeko will stay frozen as long as she has this mask on."
    sq "So will the school.  And don't think you can leave.  You'll see what I mean if you walk around a little."
    sq "There's no escape.  You only have two choices... Welcome the Eternal Night, or take the mask off Saeko."
    hide saeko
    show ayase animated neutral sad with dissolve
    ay "Okay, but like, how do we do that?"
    hide ayase
    show saeko animated neutral serious with dissolve #update with Snow Queen
    sq "Hahaha, keep fighting it.  Nothing's more beautiful than despair after a struggle."
    sq "I can't wait to bask in your beautiful despair..."
    hide saeko
    show ayase animated neutral serious with dissolve
    ay "Hey!  I asked you a question!"
    hide ayase
    n "Saeko becomes fully encased in ice."
    show yukino animated neutral sad with dissolve
    yu "*gasp* Ms. Saeko!"
    hide yukino
    n "The Snow Queen's voice echoes around the area."
    sq "Hahaha... Watch it, or Saeko and the mask will both shatter into smithereens."
    sq "I have a few rituals to perform, so there is still time before the Eternal Night."
    sq "Why don't we pass the time with a game?"
    show yukino animated neutral serious with dissolve
    yu "A game!?"
    hide yukino
    sq "This school is now a castle of ice.  There are three towers, each with a guardian."
    sq "If you can defeat them before I've finished my rituals... I'll turn Saeko and the school back to normal."
    sq "I must leave this mask now and prepare to call down the Eternal Night."
    sq "I hope you enjoy yourselves while I'm gone.  Hahaha... I'll see you later."
    n "The presence of the Snow Queen fades away..."
    show ayase animated neutral sad with dissolve
    ay "Hey, wait!  Don't leave...!  Omigod... Wh-What're we gonna do!?"
    show ayase animated neutral serious
    ay "This is all your fault, Naoya!  If you never found that stupid mask, this wouldn't have happened!"
    ay "You better own up!  Are you a man or not!?  Say something!"
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "Stop it, Ayase!  Pointing fingers won't help the situation any.  It's not like Naoya knew what was gonna happen."
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "But Yukino..."
    hide ayase
    show bg black
    pause 0.1
    hide bg black
    show ayase animated neutral serious with dissolve
    ay "Whoa!  What was that!?"
    hide ayase
    n "A golden butterfly appears in the courtyard."
    show yukino animated neutral serious with dissolve
    yu "That thing again..."
    hide yukino
    show ayase animated neutral serious with dissolve
    ay "Huh...?  What do you mean 'Again'?"
    hide ayase
    n "Philemon cutscene shows up here."
    #Update with philemon cutscene
    n "Obtained 'Mirror Frame'."
    show yukino animated neutral serious with dissolve
    yu "So our job's to find the Mirror Shards and put them in this frame, huh?"
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Umm, Yukino?  You know the towers are guarded by demons, right?"
    ay "Aren't we a little, y'know, shorthanded?"
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "You can stay here if you want.  We don't force you to come, not when we don't know what we're up against."
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Uh, no, I meant... It's just..."
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "I'll do whatever it takes to save Ms. Saeko.  I used to be a lousy delinquent."
    yu "Even my parents gave up on me... but not her.  "
    show yukino animated neutral sad
    extend "She never gave up on me.  Ever."
    show yukino animated neutral serious
    yu "Now it's my turn to help her, and my... expertise can be put to a good cause."
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Hey, Yukino... You're not planning on leaving me here all alone, are you...?"
    show ayase animated neutral serious
    ay "'Cause I'm going with you!  I feel much safer around you and Naoya."
    hide ayase
    show yukino animated neutral smirk with dissolve
    yu "Haha, sure... whatever floats your boat."
    yu "If we get stuck in a bad situation, I'm sure you'll help lighten the mood."
    hide yukino with dissolve
    n "Yukino finally notices the weapon that Ayase is carrying."
    show yukino animated neutral serious with dissolve
    yu "Hey!  Holy crap, Ayase, where did you get a gun!?"
    hide yukino
    show ayase animated neutral smirk with dissolve
    ay "Kei gave it to me.  Him and Masao went tot he police station for some weapons."
    show ayase animated neutral sad
    ay "But Kei got hurt, so they came back to school."
    show ayase animated neutral serious
    ay "He handed me some guns and said to hold on to them while he went to the nurse..."
    show ayase animated neutral smirk
    ay "So I kept one for myself!  Hehehe... I always wanted to try shooting one of these things!"
    hide ayase
    show yukino with dissolve
    yu "......"
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Gah!  The wind's picking up!  Brrrr, it's cooooooooold... My ears hurt!"
    ay "C'mon, let's go inside, quick!"
    hide ayase
    show yukino animated neutral serious with dissolve
    yu "Yeah, standing here won't do anyone any good."
    yu "Y'think the three of us can handle the demons and get those *Mirror Shards*...?"
    yu "I dunno, maybe we should grab a couple of more people, like Ayase said."
    show yukino animated neutral smirk
    yu "I bet Elly would have some information.  We should check the library."
    hide yukino
    show ayase animated neutral sad with dissolve
    ay "Good, let's get inside!  I'm freezing to death here!"
    hide ayase
    n "You and Ayase go into the school, seeking some warmth."
    show yukino animated neutral sad with dissolve
    yu "Ms. Saeko... We'll be back for you."
    jump callSQHermelinFloor1

label label085 (location = "Class 1-1"):
    scene bg black with dissolve #update with Frozen Classroom
    #play music classroom #update
    if plotprogress < 8:
        call screen SQClass11a
    elif plotprogress == 8:
        call screen SQClass11b
    elif plotprogress == 9:
        call screen SQClass11c
    elif plotprogress >= 10:
        call screen SQClass11d
    if _return == 1:
        if plotprogress != 14:
            show yukino animated neutral serious with qleft
            yu "Who the hell built snowmen here!?"
        else:
            show yukino animated neutral serious with qleft
            yu "My toes are getting numb.  Stupid Drama Club!  Why'd the Snow Queen have to be their traditional play?"
            yu "Why not A Midsummer Night's Dream?  I hate the cold..."
    elif _return == 2:
        if plotprogress != 14:
            show ayase animated neutral smirk with qleft
            ay "Omigosh!  Look at those dolls!  They're, like, sooooo cute!"
        else:
            show ayase animated neutral serious with qleft
            ay "We're not done here yet?"
    elif _return == 3:
        if plotprogress != 14:
            raiho "Hee-ho!  We transferred to this hee-school from Devil's Peak-ho behind that door."
            reiho "Hee-ho!  It's hee-so cool and comfy-ho over here."
            raiho "School is pretty fun, isn't it, Reiho?"
            reiho "Yeah... it's all right, ho."
            raiho "Think we'll make a hee-hundred friends?"
            reiho "I doubt it..."
            raiho "Hee-huh...?  Human girls aren't cold like that, ho!"
            reiho "They aren't?  Sounds hee-hard..."
        else:
            reiho "Hee... Nothing cool has happened lately."
            raiho "Hee-ho!  Wanna light the school on fire, ho?  Burn, baby, burn!"
            reiho "Hey, hee-don't be so reckless.  That'll make this place too hee-hot."
    elif _return == 5:
        if plotprogress != 14:
            show elly animated neutral smirk with qleft
            el "Oh!  Jack Frosts!"
            show elly animated neutral serious
            el "Careful... Their outwardly adorable appearance is a ruse to lure people in."
            show elly animated neutral smirk
            el "Then, they use their icy breath to freeze their unsuspecting prey!"
        else:
            show elly animated neutral serious with qleft
            el "Innocence and cruelty are two sides of the same coin.  Be careful!"
    elif _return == 6:
        if plotprogress != 14:
            show nanjo animated neutral serious with qleft
            na "As the saying goes, 'Discretion is the better part of valor.'"
        else:
            show nanjo animated neutral serious with qleft
            na "It's not my business, but those children look pale.  They need more iron."
    elif _return == 7:
        if plotprogress != 14:
            show brown animated neutral smirk with qleft
            br "Hey, check out those weirdos!  They keep saying, 'Hee-ho, hee-ho.'"
        else:
            show brown animated neutral serious with qleft
            br "I talked to 'em a little... Man, they've been through some hard times."
            show brown animated neutral sad
            br "And they're still so young!  It's enough to bring me to tears... *sniff*"
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    jump label085

label label086 (location = "Weapon Shop 1-2"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    if plotprogress < 8:
        call screen SQWeapona
    elif plotprogress == 8:
        call screen SQWeaponb
    elif plotprogress == 9:
        call screen SQWeaponc
    elif plotprogress >= 10:
        call screen SQWeapond
    if _return == 1:
        if plotprogress < 13:
            show yukino animated neutral serious with qleft
            yu "From Devil's Peak, huh?  Then is that kid a demon too...?"
        else:
            show yukino animated neutrals serious with qleft
            yu "It's making money off humans fighting demons.  "
            show yukino animated neutral smirk
            extend "That's one ballsy kid...!"
    elif _return == 2:
        if plotprogress < 13:
            show ayase animated neutral smirk with qleft
            ay "Hey, are these, like, real?"
        else:
            show ayase animated neutral serious with qleft
            ay "I wonder where that kid's from."
    elif _return == 3:
        if plotprogress < 13:
            stu "Ah, so you're here too, Naoya.  Check it out!"
            stu "With all this, we can stand up to the demons whenever they appear!"
        else:
            stu "Huh?  He's selling different stuff now... It looks even more dangerous."
    elif _return == 4:
        #show froggyboy clerk
        yyclerk "Welcoooooome.... I from Devil's Peak.  Bring very good things."
        yyclerk "Mister need this.  I sell at low price, you buy."
    elif _return == 5:
        if plotprogress < 13:
            show elly animated neutral smirk with qleft
            el "That child is supposedly a merchant of death from the demon world."
        else:
            show elly animated neutral serious with qleft
            el "Does that child care at all who wins between us and the Queen?"
    elif _return == 6:
        if plotprogress < 13:
            show nanjo animated neutral smirk with qleft
            na "Amazing!  All of these could prove useful for us."
        else:
            show nanjo animated neutral serious with qleft
            na "I wonder how many times we survived as a result of that child."
            na "We should express our thanks, even if its prices are a bit exorbitant."
    elif _return == 7:
        if plotprogress < 13:
            show brown animated neutral sad with qleft
            br "Yikes, what's with the little arms dealer at school?"
            show brown animated neutral smirk
            br "...Well, I guess it's part of that small stuff you're not supposed to sweat."
        else:
            show brown animated neutral sad with qleft
            br "WHOA!  Has it gotten even crazier here?"
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    elif _return == 9:
        tea "What is the matter with that child!?  This is a school!"
        tea "He can't open a store here without permission!"
    jump label086

label label087 (location = "Armor Shop 1-3"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    if plotprogress < 8:
        call screen SQArmora
    elif plotprogress == 8:
        call screen SQArmorb
    elif plotprogress == 9:
        call screen SQArmorc
    elif plotprogress >= 10:
        call screen SQArmord
    if _return == 1:
        if plotprogress < 13:
            show yukino animated neutral serious with qleft
            yu "All these clothes have some practical use.  They're more like armor than clothes."
        else:
            show yukino animated neutral serious with qleft
            yu "Think this shopkeeper came from Devil's Peak like the one across the hall?"
    elif _return == 2:
        if plotprogress < 13:
            show ayase animated neutral smirk with qleft
            ay "Oh man, this is soooo cool!"
        else:
            show ayase animated neutrals sad with qleft
            ay "Yikes... I wonder if I've gained weight."
    elif _return == 3:
        if plotprogress < 13:
            stu "Squee!  Look, look!  This dress is soooo cute!"
        else:
            stu "Squee!  Look, look!  This skirt is soooo cheap!"
    elif _return == 4:
        #show gasmask clerk update
        yyclerk "Wel... come..."
    elif _return == 5:
        if plotprogress < 13:
            show elly animated neutral serious with qleft
            el "Could this be armor?  I must say, it's better than no protection whatsoever."
        else:
            show elly animatd neutral serious with qleft
            el "No wonder they stock high-quality goods.  If we died, they'd have no customers."
    elif _return == 6:
        if plotprogress < 13:
            show nanjo animated neutral serious with qleft
            na "The higher an item's price, the sturdier it seems."
        else:
            show nanjo animated neutral serious with qleft
            na "I wonder how often this armor has saved our lives... It's expensive, but I'm not complaining."
    elif _return == 7:
        if plotprogress < 13:
            show brown animated neutral sad with qleft
            br "Hey, what's with this store selling these crazy clothes at school?"
            show brown animated neutral smirk
            br "...Eh, whatever.  It's not like the school regulations mean anything anymore."
        else:
            show brown animated neutral smirk with qleft
            br " Even if the school goes back to normal, I'm gonna keep wearing stuff from here."
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    elif _return == 9:
        if plotprogress < 13:
            show yuko at pleft2 with qleft
            yuko "Oh... such cute clothes... so expensive, though..."
        else:
            show yuko at pleft2 with qleft
            yuko "U-Um... Do you think this place will buy uniforms...?"
    jump label087

label label088 (location = "Class 2-1"):
    if plotprogress < 12: #update with actual plot progress
        "The door is frozen shut and will not open."
    else:
        scene bg black with dissolve #update with frozen cafeteria
        #play music cafeteria #update
        call screen SQClass21
        if _return == 1:
            if plotprogress == 12:
                show yukino animated neutral sad with qleft
                yu "What an awful feeling... The air here is as bad as the hospital basement."
            else:
                show yukino animated neutral sad with qleft
                yu "Even with Yuriko gone, the air here is still cold."
        elif _return == 2:
            if plotprogress == 12:
                show ayase animated neutral sad with qleft
                ay "It's soooo cooooold... Ow, my lower back..."
            else:
                show ayase animated neutral sad with qleft
                ay "I'm hungry... how much longer is this gonna take?"
        elif _return == 3:
            if plotprogress == 12:
                ph "This door leads to 'Thanatos Tower', one of the three towers surrounding this school."
                ph "This tower is filled with immensely powerful demons. Gathering the Mirror Shards here will be a formidable task indeed."
                ph "I must warn you of this, as well... Once you enter a tower, you cannot leave until you defeat its master."
                ph "Be sure of yourself before entering one."
            else:
                ph "Yuriko's spirit is at peace, now.  Well done."
        elif _return == 4:
            if plotprogress == 12:
                show brown animated neutral serious with qleft
                br "Wow, it's FREEZING here!  I think it's even colder than the other classrooms!"
            else:
                show brown animated neutral serious with qleft
                br "Ah... ah... ACHOO!  Argh!  We really need to get rid of all this stupid ice!"
        elif _return == 5:
            if plotprogress == 12:
                show elly animated neutral serious with qleft
                el "Hm... Thanatos Tower... Thanatos is the Greek god of death."
                show elly animated neutral smirk
                el "Not someone you'd want as your friend..."
            else:
                show elly animated neutral sad with qleft
                el "The desire to remain beautiful... I can somewhat understand how Yuriko felt."
        elif _return == 6:
            if plotprogress == 12:
                show nanjo animated neutral serious with qleft
                na "Hm.  Better weapons would be nice."
            else:
                show nanjo animated neutral serious with qleft
                na "A god of death... That's one Persona I'd as soon not assume."
        elif _return == 7:
            "update for new SQ navigation"
            #jump #update with new SQ navigation:
        elif _return == 8:
            $ tbnarrator = 1
            n "A heavy, cold draft can be felt from beyond the door as you force it open."
            $ tbnarrator = 0
            jump label121
        jump label088

label label089 (location = "Classroom"):
    scene bg black with dissolve #update with Frozen Classroom
    #play music classroom #update
    if plotprogress < 8:
        call screen SQClassrooma
    elif plotprogress == 8:
        call screen SQClassroomb
    elif plotprogress == 9:
        call screen SQClassroomc
    elif plotprogress >= 10:
        call screen SQClassroomd
    if _return == 1:
        if plotprogress != 14:
            show yukino animated neutral smirk with qleft
            yu "A casino?  Sounds tempting."
        else:
            show yukino animated neutral serious with qleft
            yu "Huh, since we've been fighting for a while, the prize might have increased."
    elif _return == 2:
        if plotprogress != 14:
            show ayase animated neutral sad with qleft
            ay "I'm hunnnngryyyy!  That reminds me, where did the home ec room go?"
            show ayase animated neutral serious
            ay "I had ingredients left over after I made sweets this morning, so I left 'em there."
        else:
            show ayase animated neutral sad with qleft
            ay "I'm hunnngryyyy."
    elif _return == 3:
        if plotprogress != 14:
            stu "Naoya!  The room in front of the library turned into a casino!  I'm so frickin' excited!"
            stu "You should check it out, too!"
        else:
            stu "While you guys were gone, I, uh, blew the club's whole budget on poker..."
            stu "Whoever's playing next is one lucky skunk.  The prize bonus must be through the roof!"
    elif _return == 4:
        if plotprogress <= 10:
            stu "Heh... We're done for.  We were always going to die someday..."
            stu "It's just been sped up a bit.  Yep... That's all there is to it."
            stu "I get to go out while I'm still beautiful, so I thank the Snow Queen for that."
        elif plotprogress <= 13:
            stu "Heh... A blue room and a blue piano.  Blue curtains and a blue carpet..."
            stu "I wonder what goes on in that room.  It's the room just to our left.  Heh..."
        else:
            stu "Heh... There's a light floating in a dark room.  The light takes me to another world."
            stu "It's wonderful... Leave here and turn left at the cross-roads, then keep going straight."
            stu "That's how you get there.  Heh..."
    elif _return == 5:
        if plotprogress != 14:
            show elly animated neutral sad with qleft
            el "That girl by the window... She's been muttering something for some time..."
        else:
            show elly animated neutral sad with qleft
            el "That girl by the window... She's still muttering to herself..."
    elif _return == 6:
        if plotprogress != 14:
            show nanjo animated neutral serious with qleft
            na "A casino?  We'll need to pry you away from there if you get involved with such things."
        else:
            show nanjo animated neutral serious with qleft
            na "The fool... He brought it on himself."
    elif _return == 7:
        if plotprogress != 14:
            show brown animated neutral smirk with qleft
            br "Hey, that sounds like fun.  We should try this casino ourselves!"
        else:
            show brown animated neutral serious with qleft
            br "I wanna just kick back and have fun at a casino or somewhere for once."
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    jump label089

label label090 (location = "Class 2-3"):
    scene bg black with dissolve #update with Frozen Classroom
    #play music classroom #update
    if plotprogress < 8:
        call screen SQClass23a
    elif plotprogress == 8:
        call screen SQClass23b
    elif plotprogress == 9:
        call screen SQClass23c
    elif plotprogress >= 10:
        call screen SQClass23d
    if _return == 1:
        if plotprogress != 14:
            show yukino animated neutral serious with qleft
            yu "I can't stand it.  That bald bastard's throwing his weight around again."
        else:
            show yukino animated neutral serious with qleft
            yu "That Kiichi's still writing lines?"
    elif _return == 2:
        if plotprogress != 14:
            show ayase animated neutral serious with qleft
            ay "Kiichi didn't do anything wrong, either.  I saw it before the school froze..."
            ay "He couldn't take any more of that student council president sitting on his ass..."
            show ayase animated neutral smirk
            ay "So he just gave him, like, a little warning is all."
        else:
            show ayase animated neutral smirk with qleft
            ay "Hey, doesn't that bald head make you wanna, like, punch it?"
    elif _return == 3:
        if plotprogress <= 10:
            show hanya at pleft2 with qleft
            ha "How dare he give me lip that way!  I'm not listening to his excuses!"
            ha "They're only lies, anyway.  As punishment, he must clean windows, write lines, and polish my shoes!"
        elif plotprogress <= 13:
            show hanya at pleft2 with qleft
            ha "Oh, if only it had been real...  Hm?  No, it's nothing.  Don't interfere with his punishment."
        else:
            show hanya at pleft2 with qleft
            ha "Hey!  Don't interfere with his punishment!  Unless you want to join him?"
    elif _return == 4:
        if plotprogress <= 10:
            stu "To hell with this!  Why am I the only one getting lectured here?"
            stu "It's just as much the student council president's fault!"
            stu "Is yelling at students without listening to them a teacher's job or what!?"
        elif plotprogress <= 13:
            stu "Don't talk to me, dammit!  Why am I the only one who has to write lines!?  I will not do..."
        else:
            stu "Don't talk to me, dammit!  I'm a little busy here!  I promise not to..."
    elif _return == 5:
        if plotprogress <= 10:
            show ooishi at pleft2 with qleft
            oo "Honestly, that man... The student must have had a reason for starting the fight."
            oo "Teachers must hear all sides before making a decision..."
        elif plotprogress <= 13:
            show ooishi at pleft2 with qleft
            oo "I had the most awful dream.  Ugh, my head..."
        else:
            show ooishi at pleft2 with qleft
            oo "Punishing students isn't the only way to educate them."
    elif _return == 6:
        if plotprogress != 14:
            show elly animated neutral serious with qleft
            el "A proper adult acting that way is rather unsightly in itself."
        else:
            show elly animated neutral serious with qleft
            el "Where could the Night Queen have gone?"
    elif _return == 7:
        if plotprogress != 14:
            show nanjo animated neutral serious with qleft
            na "Both parties in a quarrel are culpable.  They should both have to write lines."
        else:
            show nanjo animated neutral serious with qleft
            na "Nothing will happen if we remain here."
    elif _return == 8:
        if plotprogress != 14:
            show brown animated neutral serious with qleft
            br "I hate getting attacked with cold logic, but I wish people wouldn't get so angry."
        else:
            show brown animated neutral serious with qleft
            br "Let's hurry and go somewhere else."
    elif _return == 9:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    jump label090

label label091 (location = "Drama Club"):
    scene bg black with dissolve #update with Frozen Drama Club
    #play music classroom #update
    if plotprogress < 8:
        call screen SQDramaCluba
    elif plotprogress == 8:
        call screen SQDramaClubb
    elif plotprogress == 9:
        call screen SQDramaClubc
    elif plotprogress >= 10:
        call screen SQDramaClubd
    if _return == 1:
        if plotprogress != 14:
            show yukino animated neutral smirk with qleft
            yu "So our drama club's good enough that it can win competitions?"
        else:
            show yukino animated neutral serious with qleft
            yu "Let's beat that Night Queen for the sake of the three tower guardians."
    elif _return == 2:
        if plotprogress != 14:
            show ayase animated neutral smirk with qleft
            ay "What a teeny-tiny room!"
            show ayase animated neutral sad
            ay "I feel like I'm in one big fridge..."
        else:
            show ayase animated neutral serious with qleft
            ay "Student council president?  More like STUPID council president!"
            ay "It really pisses me off that a guy like him ended up in charge!"
    elif _return == 3:
        if plotprogress != 14:
            stu "I heard a story about when Ms. Saeko was in the drama club..."
            stu "They say she fought with her best friend over who would play the Snow Queen."
            stu "I forgot her last name, but I think her first name was Tomomi."
            stu "There were tears in Ms. Saeko's eyes when she told me about that..."
        else:
            stu "It seems like there's a tragic legacy behind the Snow Queen's mask."
            stu "Maybe I should write a play about it once the town's back to normal."
    elif _return == 4:
        if plotprogress != 14:
            stu "Whew... that was close.  See, I got in a fight."
            stu "The Vice-Principal almost caught me, which would have been bad."
            stu "But I bet he won't find me here."
        else:
            stu "You guys really do work hard."
            stu "Leave everything to your ol' student council president and run along, okay?"
    elif _return == 5:
        if plotprogress != 14:
            show elly animated neutral sad with qleft
            el "Nothing but sheets and sheets of ice... It's not beautiful at all; only cold."
        else:
            show elly animated neutral serious with qleft
            el "Where could the other club members be?"
    elif _return == 6:
        if plotprogress != 14:
            show nanjo animated neutral serious with qleft
            na "Where did the other club rooms go?"
        else:
            show nanjo animated neutral serious with qleft
            na "There doesn't seem to be anything useful here."
    elif _return == 7:
        if plotprogress != 14:
            show brown animated neutral sad with qleft
            br "Here one may find the sweat and tears of maidens who devoted their youth to acting."
            show brown animated neutral serious
            br "Hey, what should we do!?"
        else:
            show brown animated neutral serious with qleft
            br "I wonder if TV studios are like this backstage... I so want to see one."
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    jump label091

label label092 (location = "Fencing Club"):
    scene bg black with dissolve #update with Frozen Drama Club
    #play music classroom #update
    if plotprogress < 8:
        call screen SQFencingCluba
    elif plotprogress == 8:
        call screen SQFencingClubb
    elif plotprogress == 9:
        call screen SQFencingClubc
    elif plotprogress >= 10:
        call screen SQFencingClubd
    if _return == 1:
        if plotprogress <= 10:
            show yukino animated neutral serious with qleft
            yu "There they go again.  Don't those two ever get tired of fighting with each other?"
        else:
            show yukino animated neutral sad with qleft
            yu "Ugh!  Quit being all lovey-dovey!"
    elif _return == 2:
        if plotprogress <= 10:
            show ayase animated neutral smirk with qleft
            ay "Tamaki is pretty cute.  Hey, maybe I should get my hair cut short, too!"
        else:
            show ayase animated neutral smirk with qleft
            ay "Awwww... that's so sweet!  Two kids in a cold room, their hearts burning with love... a pair of jailbirds."
    elif _return == 3:
        if plotprogress <= 10:
            show tamaki animated neutral serious with qleft
            tm "Tadashi is such a jerk!  I TOLD him those sports drinks were for everyone, and he drank them all!"
        else:
            show tamaki animated neutral smirk with qleft
            tm "I had a wonderful dream, and it made me realize my true feelings. Starting today... I'll always be with Tadashi!"
    elif _return == 4:
        if plotprogress <= 10:
            show tadashi at pleft2 with qleft
            td "C'mon, it's not THAT big a deal, is it!?  You tightwad!"
            td "Oh, uh, sorry.  That was meant for this loudmouth over here."
        else:
            show tadashi at pleft2 with qleft
            td "Two people, seeing the same dream at the same time... It can't be a coincidence!"
            td "Clearly, we were meant for each other."
    elif _return == 5:
        if plotprogress <= 10:
            show elly animated neutral serious with qleft
            el "Hm... Hypnos Tower... Hypnos is the Greek god of sleep."
            show elly animated neutral smirk
            el "That doesn't sound so scary, does it?"
        else:
            show elly animated neutral serious with qleft
            el "Jailbirds...?  Not lovebirds?  Was Ayase joking when she said that?  Or did she really...?"
            show elly animated neutral sad
            el "*sigh* Honestly, I don't understand her sometimes."
    elif _return == 6:
        if plotprogress <= 10:
            show nanjo animated neutral serious with qleft
            na "The temperature is enervating me... No, no, that's not good."
        else:
            show nanjo animated neutral sad with qleft
            na "What's Ayase trying to say?"
    elif _return == 7:
        if plotprogress <= 10:
            show brown animated neutral sad with qleft
            br "At least he has someone to argue with. *sigh* Being single is a drag..."
            show brown animated neutral serious
            br "Brrrr!"
        else:
            show brown animated neutral smirk with qleft
            br "I see my handsome face in your eyes..."
            show brown animated neutral sad
            br "Wait, does that mean you...!?"
    elif _return == 8:
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    elif _return == 9:
        jump label101
    elif _return == 10:
        bf "I've been waiting for you.  The Snow Queen's power seems to be weakened after you saved Toro from his Persona."
        bf "This door that was previously frozen shut is now open to you."
        bf "This is the entrance to 'Hypnos Tower'.  Of the three, this tower has the simplest structure."
        bf "I believe it will be comparatively easy to find the Mirror Shards there."
        bf "This may also weaken the Snow Queen's power further and thaw other doors."
        bf "Remember: once you enter the tower, you cannot leave until you defeat its master."
    jump label092

label label093 (location = "Infirmary"):
    if plotprogress == 7:
        scene bg black with dissolve #update with Infirmary
        #play  music infirmary #update
        show natsumi animated neutral serious with qleft
        nat "Kei, you need to hold still so I can treat your wounds!"
        hide natsumi with qdis
        show nanjo animated neutral serious with qleft
        na "Perhaps you had best learn first how to dress injuries before tending to others."
        hide nanjo with qdis
        show yukino animated neutral smirk with qleft
        yu "I don't think Kei's in any mood to talk right now."
        hide yukino with qdis
        show ayase animated neutral serious with qleft
        ay "C'mon, Naoya.  Let's go check in the library to find Elly."
        "update for new SQ navigation"
        #jump #update with new SQ navigation:
    elif plotprogress == 8:
        scene bg black with dissolve #update with Infirmary
        #play  music infirmary #update
        show natsumi animated neutral serious with qleft
        nat "Don't you take off that bandage, Kei!  Your wound will reopen!"
        hide natsumi with qdis
        show nanjo animated neutral serious with qleft
        na "Not to worry.  The way that bandage was applied, it served no purpose anyway."
        hide nanjo with qdis
        show natsumi animated neutral serious with qleft
        nat "Hmph... Excuse me for being a little bit of a butterfingers."
        hide natsumi with qdis
        show nanjo animated neutral serious with qleft
        nanjo "Well then, if you'll excuse me..."
        hide nanjo with qdis
        show natsumi animated neutral serious with qleft
        nat "Wait, what are you doing?  Don't tell me you're going outside...!"
        hide natsumi with qdis
        stu "Yeah, c'mon, Kei.  You're just gonna get hurt again.  Besides..."
        stu "We've been all over campus and we couldn't find any way out."
        stu "We can't leave the school!"
        show nanjo animated neutral serious with qleft
        na "Hm?  What are you babbling about?  This isn't the time to share your day dreams."
        hide nanjo with qdis
        show ayase animated neutral serious with qleft
        ay "She's not!  It's totally true!  The Snow Queen trapped us all in here."
        hide ayase with qdis
        show nanjo animated neutral serious with qleft
        na "The Snow Queen?  Do you take me for a fool?  You can devise a better lie that that."
        na "I haven't time to waste on the daft.  Now, kindly step aside."
        hide nanjo with qdis
        show yukino animated neutral serious with qleft
        yu "She's right, Kei.  There's no exit."
        hide yukino with qdis
        show nanjo animated neutral serious with qleft
        na "Yukino, not you too-- Wait..."
        na "Has the phenomenon we saw at the hospital reoccurred here!?"
        hide nanjo with qdis
        show elly animated neutral serious with qleft
        el "I'm afraid so.  With one important difference... There are no demons here, but no way out either."
        hide elly with qdis
        show yukino animated neutral smirk with qleft
        yu "You got it.  On the bright side, it's not swarming with demons..."
        show yukino animated neutral serious
        yu "But the bad news is there's no way out."
        hide yukino with qdis
        show nanjo animated neutral sad with qleft
        na "...I'm concerned for Masao and Maki.  I must get outside at any cost."
        hide nanjo with qdis
        show setsuko at pleft2 with qleft
        set "Maki... Is there really no exit?  I wonder if there's something we can do..."
        hide setsuko with qdis
        show yukino animated neutral serious with qleft
        yu "Turns out, there is.  But we need help."
        hide yukino with qdis
        show nanjo animated neutral serious with qleft
        na "What do you mean?"
        hide nanjo with qdis
        show ayase animated neutral serious with qleft
        ay "Okay, here goes..."
        hide ayase with qdis
        show fadeblack with dissolve
        n "The four of you explain the situation to Nanjo."
        hide fadeblack with dissolve
        show nanjo animated neutral serious with qleft
        na "Hm.  I see.  If we save Ms. Saeko from this so-called Snow Queen, the school will be restored."
        na "And you're expecting my help?"
        hide nanjo with qdis
        n "You nod affirmatively."
        show nanjo animated neutral serious with qleft
        na "Very well.  If you insist, I suppose I can lend a hand.  We'll take care of this, then Maki."
        $ plotprogress = 9
        jump label093
    else:
        scene bg black #update with frozen infirmary
        #play music library fadeout 0.5 fadein 0.5 #update
        if plotprogress < 10:
            call screen SQInfirmarya
        else:
            call screen SQInfirmaryb
        if _return == 1:
            if plotprogress != 14:
                show yukino animated neutral serious with qleft
                yu "I hate doctors... but if we get hurt, we should go see Nurse Natsumi."
                show yukino animated neutral smirk
                yu "Better that than force ourselves to keep going while we're injured."
            else:
                show yukino animated neutral serious with qleft
                yu "Everyone doing okay?"
        elif _return == 2:
            if plotprogress != 14:
                show ayase animated neutral serious with qleft
                ay "Is this that Agastya thing?  I've heard it has, like, weird powers."
            else:
                show ayase animated neutral serious with qleft
                ay "This place is freezing, too.  It's time we ditched all this cold stuff."
        elif _return == 3:
            if plotprogress != 14:
                show nanjo animated neutral sad with qleft
                na "I worry about Masao and Maki out there.  We must hurry and defeat the Snow Queen."
            else:
                show nanjo animated neutral serious with qleft
                na "Masao, Maki, wait for us.  Once we defeat the Snow Queen, we'll come for you!"
        elif _return == 4:
            if plotprogress != 14:
                show elly animated neutral smirk with qleft
                el "Thank goodness the infirmary is still intact."
            else:
                show elly animated neutral serious with qleft
                el "We must hurry and bring the school back to normal so we can find Maki."
        elif _return == 5:
            if plotprogress <= 10:
                show natsumi animated neutral serious with qleft
                nat "Why are you staring at me?  Wait, let me guess..."
                show natsumi animated neutral smirk
                nat "Have you fallen for me?  Speaking of falling for people... "
                show natsumi animated neutral serious
                nat "Ayase!  Did I hear that Kenta confessed his love for you?  What did you say to him!?"
                nat "That boy's been acting very strange lately."
                nat "You should take people's feelings into consideration before you say something!"
                hide natsumi with qdis
                show ayase animated neutral serious with qleft
                ay "Well said!  And like, you would know, with all your experience getting rejected."
                hide ayase with qdis
                show natsumi animated neutral serious with qleft
                nat "...Well, back to work for me."
            elif plotprogress <= 13:
                show natsumi animated neutral serious with qleft
                nat "I'm still so tired....but I was having such a nice dream."
                nat "I wonder if anyone would notice if I took a snooze in one of the beds here..."
            else:
                show natsumi animated neutral serious with qleft
                nat "You're looking more mature, Naoya."
                show natsumi animated neutral smirk
                nat "Really, all of you seem more grown up than when I last saw you."
        elif _return == 6:
            if plotprogress != 14:
                show setsuko at pleft2 with qleft
                set "I can't believe the phenomenon has spread to the school..."
            else:
                show setsuko at pleft2 with qleft
                set "I keep thinking I can hear Maki.  But if she's here, then..."
        elif _return == 7:
            if plotprogress != 14:
                stu "Oww... I fell and landed on my butt.  Why's the hall so slippery!?"
            else:
                stu "Like, did you hear?  Y'know the market they're holding next door that sells those kickass clothes?"
                stu "Apparently their stock is, like, completely different now."
        elif _return == 8:
            if plotprogress != 14:
                show brown animated neutral smirk with qleft
                br "I wonder if there are any love potions around here."
            else:
                show brown animated neutral serious with qleft
                br "I wonder if there are any smart drugs around here."
        elif _return == 9:
            "update for new SQ navigation"
            #jump #update with new SQ navigation:
        jump label093

label label094 (location = "Cafeteria"):
    if plotprogress < 9:
        scene bg black with dissolve #update with frozen cafeteria
        #play music cafeteria #update
        if plotprogress < 8:
            call screen SQCafeteria1a
        else:
            call screen SQCafeteria1b
        if _return == 1:
            show yukino animated neutral serious with qleft
            yu "We can't waste our time here!  Let's go find someone we can rely on!"
        elif _return == 2:
            show ayase animated neutral serious with qleft
            ay "Even the inside of the school's frozen!  How could that monster do this to us!?"
        elif _return == 3:
            stu "Everything froze over all of a sudden.  Did demons do that, too?"
            stu "I just took a look and we're starting to run low on food... No surprise that Toro's panicking."
        elif _return == 4:
            show toro at pleft2 with qleft
            tor "No way... All that's left is milk and cheese?  I can't even eat my sorrow away?"
            if toro == False:
                $ tbnarrator = 1
                n "{color=#ebffdb}>Kenta Yokouchi (Nickname: Toro)\nHis love of food has made him physically strong, but emotionally fragile.{/color}"
                $ tbnarrator = 0
                $ toro = True
            tor "I'm lactose intolerant... This is a conspiracy by someone who knows!"
            tor "Yeah, that's gotta be it!  Everyone in the world is laughing at my bad luck!"
            tor "*sob* Dammit..."
        elif _return == 5:
            show brown eyes at pleft2 with qleft
            br "Aaaaaaaa-choooo!"
            show brown animated neutral smirk
            br "Oh, sorry.  Did that get on your clothes?"
            show brown animated neutral sad
            br "I seriously feel like some wilted lettuce stuck in the fridge.  It's depressing."
            show brown animated neutral serious
            br "I thought about having some hot ramen, but I can't boil any water.  Plus, Toro's freaking out."
            br "Says he's gonna eat all the food to get over being dumped."
            show brown animated neutral smirk
            br "That's why I hurried to hide everything except the dairy stuff."
            br "I mean, who knows what'll happen, y'know?  I'm like, so on top of things!"
        elif _return == 6:
            show elly animated neutral sad with qleft
            el "I had assumed Kenta was upset due to the Snow Queen, but it's over a rejection?"
            show elly animated neutral serious with qleft
            el "I wonder who had rejected him..?"
        elif _return == 7:
            "update for new SQ navigation"
            #jump #update with new SQ navigation:
        jump label094
    elif plotprogress == 9:
        scene bg black with dissolve #update with frozen cafeteria
        #play music hospital2 fadeout 0.5 fadein 0.5 #update
        show brown animated neutral sad with qleft
        br "H-Hey, Toro!  I'm sorry for hiding the food from you..."
        br "Just please don't eat any more!  You're gonna waste it all!"
        hide brown with qdis
        stu "I'm sorry, man.  I thought if you found it, you'd gobble it all up."
        stu "The whole school's in trouble!  We have to ration the food!  You gotta understand..."
        show toro at pleft2 with qleft
        tor "Sh-Shut up!  Why's everyone make fun of me!?"
        tor "I know you were sharing the food without telling me!  That's it, this food's mine!"
        hide toro with qdis
        show brown animated neutral sad with qleft
        br "Nooo!  Our precious, precious food!"
        br "One guy goes crazy from rejection and we all starve to death now?"
        br "How can my charmed life end this way!? Croaking alongside a fatso..."
        hide brown with qdis
        show toro at pleft2 with qleft
        tor "AAAAAAAAAAHHHHHHH!  Y-Y-Y-Y-YOU SAID THE F-WORD!  DON'T CALL ME FAT!"
        tor "DAMN YOU ALL!  I'm gonna eat and eat and eat before I die!  I'll stuff myself!"
        tor "Then I'll watch the rest of you collapse one by one!  Ahahahahahahahahaha!"
        hide toro with qdis
        stu "H-Hey, Brown... he's completely lost it.  What do we do?"
        show brown animated neutral sad with qleft
        br "D-Don't ask me!  "
        show brown animanted neutral serious
        extend "Man, Yuka, this is all your fault for rejecting him!"
        hide brown with qdis
        show ayase animated neutral serious with qleft
        ay "Excuse me!?  What's with blaming me for this all of a sudden!?"
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "Only one thing to do... knock the poor bastard out cold."
        hide yukino with qdis
        show toro at pleft2 with qleft
        tor "Hahahahahahaha... No way!  Not gonna happen!  Wanna know why?"
        tor "'Cause the butterfly gave me a demon!"
        tor "I'm not just a butterball anymore, Ayase! Ahahahahahahaha!"
        hide toro with qdis
        show brown animated neutral smirk with qleft
        br "Uh... a demon?  Wow, sounds like his mind snapped along with his heart."
        hide brown with qdis
        show elly animated neutral serious with qleft
        el "What!?  Does he mean a Persona...?"
        hide elly with qdis
        stu "I'll grab a teacher!  Keep an eye on him, I'll be right back!"
        show brown animated neutral serious with qleft
        br "Hey, Boss!  I don't think he'll come to his senses without a swift kick in the butt."
        hide brown with qdis
        show yukino animated neutral smirk with qleft
        yu "Who're you calling 'Boss'!?  Tch, you're such a clown..."
        show yukino animated neutral serious
        yu "Sure, I'll try that if nothing else works.  For now, let's buy us some time until the teacher gets here!"
        yu "Hey Hidehiko, you listening?  Quit standing around and give us a hand!"
        hide yukino with qdis
        show brown animated neutral smirk with qleft
        br "Mwahahaha... I'll follow you to the ends of the earth!"
        hide brown with qdis
        show toro at pleft2 with qleft
        tor "Ahahahahahahaha!  No one can stop me now!"
        hide toro with qdis
        show nanjo animated neutral serious with qleft
        na "Kenta!  You must calm down!"
        na "Once the city returns to normal, I'll treat you to our chef's special dishes!"
        hide nanjo with qdis
        show toro at pleft2 with qleft
        tor "Aaaah, my darling Yuka!  I'll save you, and only you..."
        tor "...If you promise to go out with me.  I'll even save you some food!  Ahahahahahaha!"
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "Uh-uh.  No way.  Not in a million years."
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "AAAAAAAAAAAHHHHHHHHH...!  DAMMIT!  DAMMIT, DAMMIT, DAMMIT!  I'M... I'M... AAAAAAAAAHHHHHH...!"
        hide toro with qdis
        show yukino animated neutral sad with qleft
        yu "D-Don't get him mad!  You're too blunt, Ayase..."
        yu "I bet you were just as cold to him when he said he loved you!"
        hide yukino with qdis
        show ayase animated neutral serious with qleft
        ay "Eh, not really.  I just told him the truth.  All I said was, like..."
        scene bg black with dissolve
        n "Just a few hours ago..."
        scene bg black with dissolve #update with flashback cafeteria
        show ayase animated neutral serious with qleft
        ay "Okay, what's this super important thing you had to tell me?  I'm, like, busy!"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "A-A-Ayase... Um... um... I'm, um, I'm sorry for, um, asking you to meet me here."
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "Geez, speak up already!  If you're not saying anything, I'm out. Seeya!"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "W-Wait!  There is something! I'll tell you right now.  ...Are you ready?"
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "GLike, spit it out already!  I got people waiting on me!"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "...Ayase... I... I I-I-I-I..."
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "You... what?"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "I LOVE YOOOOOOOOOOU!  I... I LOVE YOU SOOOOOO MUUUUUCH!"
        tor "P-P-P-P-Please go out with me!  I p-p-p-promise I'll make you hippy..."
        tor "I, I mean, happy. *pant* *pant*"
        hide toro with qdis
        show ayase animated neutral smirk with qleft
        ay "......No.  Way.  Like, have you even seen yourself in a mirror?"
        show ayase animated neutral serious
        ay "Alright, I'm out.  Laters."
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "W-Wait!  Please!  Why not?  What's so bad about me?"
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "Let's see, you're fat, slow, wear the same clothes every day, laugh at everything..."
        ay "And I've never seen you do anything but eat, sleep, and read manga."
        ay "I like, don't get what keeps you going.  Everything about you sucks!"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "H-How can you be so mean...?  Well... what do YOU like, Ayase?"
        tor "You laugh when you aren't happy, you hang out with people you think are stupid..."
        tor "Are you scared to be alone?"
        hide toro with qdis
        show ayase animated neutral serious with qleft
        ay "Sh-Shut up!  Stop acting like you got it all figured out, butterball!"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "B... Butterball...?"
        scene bg black with dissolve #update with frozen cafeteria
        show nanjo animated neutral serious with qleft
        na "Small wonder Kenta was furious.  As they say, 'All evil comes from the mouth'..."
        na "You went too far, Ayase.  Apologize to him!"
        hide nanjo with qdis
        show brown animated neutral sad with qleft
        br "Oh man... What have you done!?  Quick, apologize!  It's not too late! Say you're sorry!"
        hide brown with qdis
        show ayase animated neutral sad with qleft
        ay "I did?  Really!?  Uh, did the truth really hurt that bad, Toro?"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "*sob* My darling Yuka... How could you...?  You'll pay for stomping all over my pure, innocent heart..."
        tor "Mr. Demon... Oh, Mr. Demon!  Come out!  Come out and punish the people who keep making fun of me!"
        tor "Bimble... Bumble... Bambob-bun..."
        hide tor with qdis
        show ayase animated neutral sad with qleft
        ay "Huh?  What's with the chanting?  You're in high school!  Stop dreaming about Mr. Demon and..."
        hide ayase with qdis
        show brown animated neutral sad with qleft
        br "Whoa whoa whoa, what's the chanting about?  This isn't some manga..."
        hide brown with qdis
        show toro at pleft2 with qleft
        tor "Unh... Uuuuuuuuunnnnggggghhh!  It's coming out!"
        #update with battle imagery
        show yukino animated neutral sad with qleft
        yu "Whoa!  What's with him!?"
        hide yukino with qdis
        show ayase animated neutral sad with qleft
        ay "Haha... ha... S-Sorry, Kenta.  Is, uh, it too late to apologize?"
        hide ayase with qdis
        show toro at pleft2 with qleft
        tor "Ahahahahahahahahaha... It's much, much, much, much, much too laaaaate!"
        tor "Eat THIS!"
        hide toro with qdis
        #update with Toro attacking the party
        show yukino animated neutral serious with qleft
        yu "Agh!  Dammit... How dare you!?"
        hide yukino with qdis
        #update with Ayase's persona
        show ayase animated neutral serious with qleft
        ay "Yikes!  Huh?  What the--!?  What NOW!?"
        hide ayase with qdis
        show brown animated neutral serious with qleft
        br "Whoa whoa whoa... What IS this thing!?"
        br "I didn't give it permission to come out of me like that!"
        hide brown with qdis
        #update with battle finishing
        show brown animated neutral serious with qleft
        br "Whaaa...?  Something just came outta me to say hi."
        hide brown with qdis
        show ayase animated neutral sad with qleft
        ay "What in the world was that...?"
        hide ayase with qdis
        show nanjo animated neutral serious with qleft
        na "Those things?  I decided to call them Personas."
        hide nanjo with qdis
        show elly animated neutral smirk with qleft
        el "They don't seem to be hostile; at least, not for now."
        hide elly with qdis
        show yukino animated neutral smirk with qleft
        yu "Looks like our little squad's getting bigger."
        hide yukino with qdis
        show brown animated neutral sad with qleft
        br "Uh... squad?"
        hide brown with qdis
        show ayase animated neutral serious with qleft
        ay "Huh?  You mean you and Naoya are like, you know... and stuff?"
        hide ayase with qdis
        show nanjo animated neutral sad with qleft
        na "I'm... not sure what you're trying to say, but..."
        show nanjo animated neutral serious
        na "There's definitely a commonality between us."
        hide nanjo with qdis
        show yukino animated neutral serious with qleft
        yu "Yeah, after we had those weird dreams, we can summon... Personas, Kei said?"
        hide yukino with qdis
        show elly animated neutral serious with qleft
        el "For some reason, only those who dreamed of the butterfly acquired the power."
        show elly animated neutral sad
        el "It also seems related to the demon invasion somehow..."
        hide elly with qdis
        show ayase animated neutral serious with qleft
        ay "Wait a sec, Toro was using a Persona, right?  Did he have that dream, too?"
        hide ayase with qdis
        show nanjo animated neutral serious with qleft
        na "If he could summon his Persona, then one assumes so."
        hide nanjo with qdis
        show elly animated neutral serious with qleft
        el "Yes, I agree.  That's the most likely explanation."
        hide elly with qdis
        show ayase animated neutral sad with qleft
        ay "Omigod!  I don't believe it!  No... no, it can't be!"
        ay "That thing's gonna come out of my tummy, and I'll go berserk!?"
        hide ayase with qdis
        show elly animated neutral sad with qleft
        el "Er... I don't think so.  It's all in how you use it."
        show elly animated neutral serious
        el "Take a knife, for example.  It can be a valuable tool in the kitchen, or a weapon on the battlefield."
        show elly animated neutral smirk
        el "What it does is determined by its user."
        hide elly with qdis
        show nanjo animated neutral serious with qleft
        na "Exactly. If you use this power for personal gain, you'll reap what you sow."
        hide nanjo with qdis
        show brown animated neutral smirk with qleft
        br "Alright... I should be fine, then.  Oh, duh!  I know exactly what that butterfly wants me to do!"
        br "It made me a hero so I could save the school--and the city!  Haha, alright..."
        br "If you guys really need me thaaaat much... I guess I can pitch in.  Follow my lead!"
        hide brown with qdis
        show nanjo animated neutral serious with qleft
        na "How naive..."
        hide nanjo with qdis
        show yukino animated neutral serious with qleft
        yu "Well, if he wants to come, fine with us.  Right, Naoya?"
        hide yukino with qdis
        show ayase animated neutral sad with qleft
        ay "Naoya, you really, actually want Hidehiko along?"
        hide ayase with qdis
        show brown animated neutral smirk with qleft
        br "C'mon, be real!  Miz Yukino here begged me to join!  How can I say no to that?"
        br "Plus, I heard it's your fault the school is in this mess."
        br "With me as leader, we can't lose!  Trust me!  Mwahahahahaha..."
        hide brown with qdis
        show yukino animated neutral serious with qleft
        yu "What are you doing?  Quit horsing around!  We're leaving!"
        hide yukino with qdis
        show brown animated neutral serious with qleft
        br "Y-Yes, Boss!"
        $ plotprogress = 10
        jump label094
    elif plotprogress >= 10:
        scene bg black with dissolve #update with frozen cafeteria
        #play music cafeteria #update
        call screen SQCafeteria2
        if _return == 1:
            if plotprogress != 14:
                show yukino animated neutral serious with qleft
                yu "Well then, let's make our way to the towers."
                show yukino animated neutral sad
                yu "We have to help Ms. Saeko."
            else:
                show yukino animated neutral serious with qleft
                yu "Doesn't it seem like it's gotten a little warmer?"
        elif _return == 2:
            if plotprogress != 14:
                show ayase animated neutral sad with qleft
                ay "I wonder if Toro's okay."
                show ayase animated neutral serious
                ay "I mean, like, not that I care or anything."
            else:
                show ayase animated neutral serious with qleft
                ay "Let's hurry out of here."
        elif _return == 3:
            if plotprogress < 12:
                stu "Huh?  You're asking why I didn't go get the teacher?  I did!"
                stu "But she wouldn't give me the time of day.  She said she was busy, and that it'd heal on its own."
                stu "Anyway, I'm just glad our food is safe."
            elif plotprogress == 13:
                stu "Man, this just isn't Toro's day. First he gets dumped by his crush and now he has to drink milk..."
                stu "Though some days are like that, I guess."
            else:
                stu "That classroom wasn't open until now... You know, the one to our left."
                stu "I heard the ice thawed a little and you can get inside now."
                stu "Rumor is there's this beautiful sphere inside.  But should we go near it...?"
        elif _return == 4:
            if plotprogress < 12:
                show toro at pleft2 with qleft
                tor "Huh?  Huhhh?  Why was I sleeping here?  Oh... hi everyone."
                tor "Don't look at me like that, it's embarrassing..."
            elif plotprogress == 13:
                show toro at pleft2 with qleft
                tor "Why do these things always happen to me...?"
                if toroshards == False:
                    tor "Oh, I almost forgot.  Tsutomu told me to give this to you."
                    tor "When me and him were coming back from the tower, we found this shiny thing..."
                    tor "But his muscles hurt so bad that he couldn't hold it.  So I'm giving it to you in his place."
                    $ toroshards = True
            else:
                show toro at pleft2 with qleft
                tor "I'm not the only one going through hard times, huh?  You and Ayase and everyone are all trying as hard as you can."
                tor "Alright, then!  I'm gonna try as hard as I can... to drink milk!"
        elif _return == 5:
            if plotprogress != 14:
                show brown animated neutral serious with qleft
                br "Persona, huh...?  Well, depending how you use it, anything might be possible."
            else:
                show brown animated neutral serious with qleft
                br "Personas are pretty scary."
                show brown animated neutral smirk
                br "Then again, I have no flaws, so there's nothing for me to worry about."
        elif _return == 6:
            if plotprogress != 14:
                show elly animated neutral sad with qleft
                el "We went through hell, no thanks to Ayase."
                show elly animated neutral serious with qleft
                el "Honestly, that girl..."
            else:
                show elly animated neutral serious with qleft
                el "A room with a beautiful sphere?  This sounds well worth investigating."
        elif _return == 7:
            if plotprogress != 14:
                show nanjo animated neutral serious with qleft
                na "That gluttonous pig had something coming out of his stomach."
                show nanjo animated neutral sad
                na "Is he... well?"
            else:
                show nanjo animated neutral serious with qleft
                na "It seems that he's matured.  Somewhat."
        elif _return == 8:
            "update for new SQ navigation"
            #jump #update with new SQ navigation:
        jump label094

label label095 (location = "Library"):
    if plotprogress == 7:
        scene bg black with dissolve #update with frozen library
        #play music hospital2 fadeout 0.5 fadein 0.5 #update
        show elly animated neutral serious with qleft
        el "How goes it, Tsutomu?  Did you discover anything?"
        hide elly with qdis
        show devilboy animated neutral serious with qleft
        db "Eeheehee... Of course, Eriko.  This temperature......."
        db "is not due to a cold front!"
        show devilboy animated neutral smirk
        db "I'm 90% sure."
        hide tsutomu with qdis
        show elly at pleft2
        el "......"
        hide elly with qdis
        show devilboy animated neutral sad with qleft
        db "I'm sorry... But I came up empty.  None of the books mention this kind of thing at all."
        hide tsutomu with qdis
        show elly animated neutral sad with qleft
        el "Oh... is that so?"
        show elly animated neutral smirk
        el "Then I'll keep up my own search.  I'm very intrigued by this door..."
        el "That writing is Greek for 'Nemesis Tower'."
        hide elly with qdis
        show devilboy animated neutral smirk with qleft
        db "Nemesis?  Hmm... Greek, you say?  Iiiiiiinteresting..."
        hide tsutomu with qdis
        show elly animated neutral serious with qleft
        el "Nemesis is the Greek goddess of retribution."
        hide elly with qdis
        n "Yukino turns to you and Ayase."
        show yukino animated neutral serious with qleft
        yu "See what I mean?  Elly knows all about this kinda stuff."
        hide yukino with qdis
        show ayase animated neutral smirk with qleft
        ay "Yeah!  She can help translate if we meet foreign demons."
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "Hey, Tsutomu knows tons about the occult and demons and stuff, too."
        yu "Wouldn't he be pretty useful?  Someone like him would be a big plus, I think."
        hide yukino with qdis
        show ayase animated neutral serious with qleft
        ay "Whaaaat!?  I don't wanna sound mean, but... he's not my type.  I say no."
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "That's your idea of 'not being mean'?  Who cares whether he's your type!?"
        yu "Though I gotta admit... He looks more than a little flaky..."
        hide yukino with qdis
        n "While you were talking amongst yourselves, Elly had approachd your group."
        show elly animated neutral serious with qleft
        el "Excuse me, but... what were you talking about just now?"
        el "I didn't mean to eavesdrop, but I heard my name come up."
        hide elly with qdis
        show yukino animated neutral serious with qleft
        yu "Oh, we were just saying you probably know a lot about demons."
        yu "Here's what's going on..."
        hide yukino with qdis
        show fadeblack with dissolve
        n "You, Yukino and Ayase catch Eriko up to speed."
        hide fadeblack with dissolve
        show elly animated neutral serious with qleft
        el "Ahh, so that's how the school became encased in ice.  Fascinating..."
        show elly animated neutral smirk
        el "I love stories of monsters and ghosts, but this..."
        el "I never imagined I'd witness multiple supernatural events, one after another."
        show elly animated nuetral serious
        el "Something must be done before it's too late."
        hide elly with qdis
        n "You agree and welcome Elly into your group."
        show elly animated neutral smirk with qleft
        el "All right!  Let's search for the 'Mirror Shards' and save Ms. Saeko."
        hide elly with qdis
        show ayase animated neutral serious with qleft
        ay "Okay, so we got Elly on board.  Who else would be useful?"
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "If Nanjo still has some guns, we should at least go and talk with him."
        hide yukino with qdis
        show elly animated neutral serious with qleft
        el "I believe he is still in the Infirmary.  Shall we?"
        $ plotprogress = 8
        jump label095
    else:
        scene bg black #update with frozen library
        #play music library fadeout 0.5 fadein 0.5 #update
        if plotprogress == 8:
            call screen SQLibrarya
        elif plotprogress == 9:
            call screen SQLibraryb
        elif plotprogress == 10:
            call screen SQLibraryc
        elif plotprogress >= 11:
            call screen SQLibraryd
        if _return == 1:
            if plotprogress < 12:
                show yukino animated neutral serious with qleft
                yu "Hey, lots of paper here.  "
                show yukino animated neutral smirk
                extend "Wanna make a bonfire?"
            else:
                show yukino animated neutral serious with qleft
                yu "Ugh!  If I never see Michiko again, it'll be too soon."
        elif _return == 2:
            if plotprogress < 12:
                show ayase animated neutral sad with qleft
                ay "The hospital was all messed up inside, just like the school, right?"
                ay "You think my house is okay?"
                show ayase animated neutral serious
                ay "I don't wanna see some demon kickin' it in the den."
            else:
                show ayase animated neutral serious with qleft
                ay "Michiko was really something.  I'm gonna be seeing her in my nightmares..."
        elif _return == 3:
            if plotprogress < 12:
                show elly animated neutral serious with qleft
                el "Hm... Nemesis Tower... Nemesis is the Greek goddess of retribution."
                show elly animated neutral sad
                el "I'm uneasy about this..."
            elif plotprogress < 14:
                show elly animated neutral sad with qleft
                el "I hope Toro is all right.  He was forced to drink quite a lot of milk..."
            else:
                show elly animated neutral serious with qleft
                el "Did you hear what Tsutomu said?  Let's go investigate!"
        elif _return == 4:
            if plotprogress < 12:
                show devilboy animated neutral serious with qleft
                db "Oh yeah, my uncle's a detective, and he once told me saw a demon."
                show devilboy animated neutral smirk
                db "I wonder if Yarai-ku is okay.  Eeeheehee..."
            elif plotprogress < 14:
                show devilboy animated neutral sad with qleft
                db "Owwww... My arms are so sore, I can't even lift them.  Eeehee...hee..."
                if toroshards = False:
                    show devilboy animated neutral serious
                    db "Oh... Toro and I found something on our way back from the tower."
                    show devilboy animated neutral sad
                    db "I left them with Toro... I wasn't able to lift them either eeehee...hee..."
            else:
                show devilboy animated neutral serious with qleft
                db "You know the classroom that's all frozen?  Eeeheehee... The isolated one."
                show devilboy animated neutral smirk
                db "They say the door opens now.  Eeeheehee..."
        elif _return == 5:
            if plotprogress < 12:
                show nanjo animated neutral serious with qleft
                na "Frozen books as far as the eye can see... How dismal."
            else:
                show nanjo animated neutral serious with qleft
                na "Hm?  My scarf's on crooked?  Ah, thanks for that."
        elif _return == 6:
            if plotprogress < 12:
                show brown animated neutral smrik with qleft
                br "There's no need to worry as long as you follow me!"
            else:
                show brown animated neutral sad with qleft
                br "Hey, uh, how about we stop talking about Nemesis Tower, huh?  Sound good?"
        elif _return == 7:
            "update for new SQ navigation"
            #update with new SQ navigation
        elif _return == 8:
            if plotprogress < 12:
                bf "This is the entrance to Nemesis Tower.  This tower has a complex structure as well as a cruel, calculating master."
                bf "Now that you've beaten Hypnos tower, it is the next path to take."
                bf "Remember: once you enter a tower, you cannot leave until you defeat its master."
                bf "Be sure of yourself before entering one."
            else:
                bf "It seems that the Nemesis Tower has been defeated, well done."
                bf "The Snow Queen's power continues to weaken.  Soon you maybe able to confront it directly."
        elif _return == 9:
            if plotprogress < 12:
                $ tbnarrator = 1
                n "A deep, resounding howl can be heard from beyond the door before you enter into Nemesis Tower."
                $ tbnarrator = 0
                jump label113
            else:
                $ tbnarrator = 1
                n "The door will not open."
                $ tbnarrator = 0
        jump label095

label label096 (location = "Sennen Mannen-Do"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    if plotprogress < 8:
        call screen SQSMDa
    elif plotprogress == 8:
        call screen SQSMDb
    elif plotprogress == 9:
        call screen SQSMDc
    elif plotprogress >= 10:
        call screen SQSMDd
    if _return == 1:
        if plotprogress < 13:
            show yukino animated neutral serious with qleft
            yu "Wasn't Sennen Mannen-Do a sweet shop?"
        else:
            show yukino animated neutral serious with qleft
            yu "This place has some weird stuff for a sweets shop."
    elif _return == 2:
        if plotprogress < 13:
            show ayase animated neutral smirk with qleft
            ay "Wow!  What beautiful gems... Hey, buy me some!  Pleeeeease!"
        else:
            show ayase animated neutral smirk with qleft
            ay "I could stare at this shiny stuff all day...!"
    elif _return == 3:
        if plotprogress < 13:
            tea "This is pretty elaborate for a Culture Festival stall. I'm impressed."
        else:
            tea "This place sells some pretty expensive stuff for a Culture Festival stall."
            tea "And those are two old-looking students..."
    elif _return == 4:
        show sennenmannendo 2 with qleft
        smd "Hohohoho... I love gems more than anything else in this world."
        smd "I'll exchange my special treasures for your gems. Would you like to trade?"
        hide sennenmannendo with qdis
        n "Naoya perused the items but ultimately decided not to trade."
    elif _return == 5:
        if plotprogress < 13:
            show elly animated neutral serious with qleft
            el "Hm?  This place isn't frozen... Now why is that?"
        else:
            show elly animated neutral serious with qleft
            el "The stores here seem as if they exist in another world.  They're not cold at all."
    elif _return == 6:
        if plotprogress < 13:
            show nanjo animated neutral serious with qleft
            na "What is this store?  A sweets shop...?  Ahhh... a sweatshop.  Yes, of course."
        else:
            show nanjo animated neutral serious with qleft
            na "This 'sweets shop' is rather bizarre."
    elif _return == 7:
        if plotprogress < 13:
            show brown animated neutral sad with qleft
            br "Hey, why's there a sweets shop at school?"
        else:
            show brown animated neutral smirk with qleft
            br "That reminds me... it's not cold in here!"
    elif _return == 8:
        "update for new SQ navigation"
        #update with new SQ navigation
    elif _return == 9:
        show sennenmannendo 2 with qleft
        smd "Hohohoho... Welcome. What manner of goods do you require?"
        hide sennenmannendo with qdis
        n "Naoya perused the items but ultimately decided not to trade."
    jump label096

label label097 (location = "Satomi Tadashi"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    if plotprogress < 8:
        call screen SQSTa
    elif plotprogress == 8:
        call screen SQSTb
    elif plotprogress == 9:
        call screen SQSTc
    elif plotprogress >= 10:
        call screen SQSTd
    if _return == 1:
        if plotprogress < 13:
            show yukino animated neutral serious with qleft
            yu "What's with the old guy?  And what does he mean by 'up above'?"
            show yukino animated neutral sad
            yu "And never mind that--why's there a pharmacy here at school!?"
        else:
            show yukino animated neutral serious with qleft
            yu "Where'd this store pop up from, anyway?"
    elif _return == 2:
        if plotprogress < 13:
            show ayase animated neutral smirk with qleft
            ay "Ooooooooooh!  A frog!  Soooooo cuuuute!"
        else:
            show ayase animated neutral smirk with qleft
            ay "I want this frog.  Buy it for me, Daddy!"
    elif _return == 3:
        if plotprogress < 13:
            stu "Huh?  What's with this song!?"
        else:
            stu "It's all going to hell outside, but it's hard to be nervous with this store around."
    elif _return == 4:
        #show Satomi Tadashi older here
        stclerk "Hello.  Thanks for always being nice to my great-grandson."
        stclerk "I'm always watching from up above.  Heeheehee!"
    elif _return == 5:
        if plotprogress < 13:
            show elly animated neutral serious with qleft
            el "So many suspicious medicines... I hope they aren't harmful to one's health."
        else:
            show elly animated neutral sad with qleft
            el "Aren't there more ordinary medicines, for everyday use?"
    elif _return == 6:
        if plotprogress < 13:
            show nanjo animated neutral sad with qleft
            na "Why is there a pharmacy here...?"
        else:
            show nanjo animated neutral serious with qleft
            na "Is this a legitimate place of business?"
    elif _return == 7:
        if plotprogress < 13:
            show brown animated neutral smirk with qleft
            br "No's-Bleed Z... Sounds like that'll do the trick, all right."
        else:
            show brown animated neutral serious with qleft
            br "Maybe I should buy up all the No's-Bleed Z before things go back to normal..."
    elif _return == 8:
        "update for new SQ navigation"
        #update with new SQ navigation
    jump label097

label label098 (location = "Judgment 1999"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    if plotprogress < 8:
        call screen SQJDa
    elif plotprogress == 8:
        call screen SQJDb
    elif plotprogress == 9:
        call screen SQJDc
    elif plotprogress >= 10:
        call screen SQJDd
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Why a casino?  Is the idea to forget about reality and waste away?"
        show yukino animated neutral smirk
        yu "Oh well, no sense sweating the details.  Might as well take a short break."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "A casino, huh?  A club would have been, like, way cooler."
    elif _return == 3:
        stu "Woo-ha!  I'm on a roll today!"
    elif _return == 4:
        man "Fro-Man: Yyyeah!  Shoobee da ba da, oh yeah!"
        man "While I was puzzlin' out future jive, my mama was workin' a nine to five."
        man "While I was cleaning the toilet stall, the Man set up my daddy to fall."
        man "Ya dig?  Da ba shoobee bop, oh yeah!"
    elif _return == 5:
        show jclerk 1 at pleft2 with qleft
        jclerk "Hiiii!  SO nice to see you!"
        jclerk "If you're looking to exchange money for coins, I'm your man."
        jclerk "Won't you purchase some coins?  Hmmmm?"
        $ tbnarrator = 1
        "After some consideration, Naoya decided against it."
        $ tbnarrator = 0
        #coin purchase for gambling
    elif _return == 6:
        show jclerk 2 at pleft2 with qleft
        jclerk "I can exchange your coins for items, if that's what you're in the mood for..."
        jclerk "Wanna see what I've got?"
        $ tbnarrator = 1
        "After some consideration, Naoya decided against it."
        $ tbnarrator = 0
        #coin exchange for gambling
    elif _return == 7:
        show elly animated neutral sad with qleft
        el "This is still our school, right...?"
    elif _return == 8:
        show nanjo animated neutral sad with qleft
        na "What IS this place!?"
    elif _return == 9:
        show brown animated neutral smirk with qleft
        br "Hehehehe... I could spend all day here!"
    elif _return == 10:
        "update for new SQ navigation"
        #update with new SQ navigation
    jump label098

label label099 (location = "Courtyard"):
    if plotprogress < 13:
        "The door is frozen shut and will not open."
    elif plotprogress == 13:
        scene bg black #update with courtyard
        #play music courtyard update
        $ tbnarrator = 1
        n "With the mirror shards assembled into the mirror frame, you return to the Courtyard to confront the Snow Queen."
        n "Ms. Saeko still stands frozen in place, and there's no signs of any change."
        $ tbnarrator = 0
        show yukino animated neutral serious with qleft
        yu "Naoya!  Hold up the mirror!"
        hide yukino with qdis
        $ tbnarrator = 1
        n "Naoya lifts the mirror, which causes the ice pillars in the area to shatter, and the ice around Ms. Saeko to melt."
        $ tbnarrator = 0
        #scene update with ice pillars and shiz all broken
        show saeko animated neutral serious with qleft #update with Snow Queen
        sq "Guh... aaah..."
        hide saeko with qdis
        show yukino animated neutral serious with qleft
        yu "Is it working!?"
        hide yukino with qdis
        show saeko animated neutral serious with qleft #update with Snow Queen
        sq "Gyaaaaaaah!  My face... it's buuurniiiiiing!"
        hide saeko with qdis
        $ tbnarrator = 1
        n "The mask separates from Saeko, and the image of a burned student appears just before the group."
        $ tbnarrator = 0
        show tomomi burned at pleft2 with qleft
        stu "Hoooow daaaare youuuuu... Whyyyy... Whyyy doooooes everyyyyone taaaake... Saekoooo's siiiiide...?"
        hide tomomi with qdis
        show ayase animated neutral sad with qleft
        ay "Eeeeeeek!"
        hide ayase with qdis
        show elly animated neutral sad with qleft
        el "Good heavens..."
        hide elly with qdis
        show brown animated neutral sad with qleft
        br "Holy son of a--Wh-Wh-Wh-Wh-What the hell!?"
        hide brown with qdis
        $ tbnarrator = 1
        n "The figure of the ghostly, burned student attacks, and the party retaliates in order to defeat her."
        n "After a difficult battle, they manage to defeat the spectral visage, emerging victorious."
        $ tbnarrator = 0
        show ayase animated neutral smirk with qleft
        ay "We did it!"
        hide ayase with qdis
        show yukino animated neutral sad with qleft
        yu "Ms. Saeko!"
        hide yukino with qdis
        $ tbnarrator = 1
        n "Ms. Saeko unsteadily rises to her feet, looking a little pale."
        $ tbnarrator = 0
        show yukino animated neutral sad with qleft
        yu "You okay?  You must've been so cold... Are you hurt?"
        hide yukino with qdis
        show saeko animated neutral sad with qleft
        sa "I'm all right, thank you.  But... "
        show saeko animated neutral serious
        extend "where is Tomomi?"
        hide saeko with qdis
        show nanjo animated neutral serious with qleft
        na "Tomomi..?"
        hide nanjo with qdis
        show brown animated neutral serious with qleft
        br "Tomomi?  Who?"
        hide brown with qdis
        show saeko animated neutral serious with qleft
        sa "Tomomi is the spirit who was possessing that mask... She's one of the students who fell under the Snow Queen's thrall."
        show saeko animated neutral sad
        sa "She's... also my best friend, from when I used to be in the drama club."
        hide saeko with qdis
        show yukino animated neutral sad with qleft
        yu "Th-Then... the Snow Queen possessing you was your friend...?"
        hide yukino with qdis
        show elly animated neutral serious with qleft
        el "So that's why the Queen seemed to be so familiar with you... But whyever would your best friend possess you?"
        hide elly with qdis
        show saeko animated neutral sad with qleft
        sa "I had no idea she thought of me that way... I guess... sometimes you hurt people without realizing it..."
        hide saeko with qdis
        scene bg black #update with drama club
        show saeko animated neutral smirk with qleft #update with younger version
        sa "Congrats on landing the Snow Queen part!  Our last year here, and you finally beat me out."
        hide saeko with qdis
        show tomomi at pleft2 with qleft
        tomomi "Thanks.  I'll put on a good show for you, Saeko!  But I'm nervous about the mask..."
        tomomi "Is it true everyone who's played the Snow Queen's role has been cursed?"
        hide tomomi with qdis
        show saeko animated neutral smirk with qleft #update with younger version
        sa "Whaaat?  Hey, I'm sure that's just some superstition?"
        sa "Just keep up that cheerful attitude and I bet any curse wouldn't dare touch you!"
        sa "That tendency of yours to believe whatever you hear is the one flaw you have!"
        hide saeko with qdis
        show tomomi at pleft2 with qleft
        tomomi "I wish... I wish I could be strong as you, Saeko."
        hide tomomi with qdis
        show saeko animated neutral smirk with qleft #update with younger version
        sa "C'mon, don't talk like that!  Cheer up!  You won the title role!"
        sa "What am I supposed to think if you're not happier about it?"
        hide saeko with qdis
        show tomomi at pleft2 with qleft
        tomomi "Y-You're right."
        hide tomomi with qdis
        scene black #update with drama club with saeko gone
        $ tbnarrator = 1
        n "As Saeko leaves, another student comes into the room to talk to Tomomi."
        $ tbnarrator = 0
        stu "Whaaaat!?  Tomomi, can't you see Saeko is pulling the wool over your eyes?"
        show tomomi at pleft2 with qleft
        tomomi "Huh!?  She tricked me?"
        hide tomomi with qdis
        stu "You didn't know!?  Saeko bowed out of contention for the Snow Queen part.  Everyone's been talking about it."
        stu "They say she forced the part on you 'cause she's scared of the mask's curse."
        show tomomi at pleft2 with qleft
        tomomi "She withdrew... because she's scared of the curse...?  No way!"
        tomomi "Even if she did bow out, I'm sure she was just being considerate!"
        tomomi "We're in the same year, but I've never gotten better role than her, so..."
        hide tomomi with qdis
        stu "So she's letting you take this last chance?  You're so naive, Tomomi.  The Snow Queen is the title role!"
        stu "No one would give it up without a damn good reason."
        show tomomi at pleft2 with qleft
        tomomi "......"
        hide tomomi with qdis
        scene black #update with drama club room with Saeko/Tomomi
        show saeko animated neutral sad with qleft #update with younger version
        sa "Tomomi?  Did you call for me?  Is something the matter...?  Why are you hiding?"
        show saeko animated neutral smirk
        sa "Well... break a leg tomorrow!  I'll be looking forward to it."
        hide saeko with qdis
        tomomi "...Your... ...ault..."
        show saeko animated neutral serious with qleft #update with younger version
        sa "What was that?  I can't hear you!"
        hide saeko with qdis
        tomomi "It'ssss... your... faaaaaault!  Yours, yours, yours!  It'ssss all your faaaaaault!"
        show saeko animated neutral sad with qleft #update with younger version
        sa "Huh!?  Tomomi, what's gotten into you!?  Calm down!"
        hide saeko with qdis
        tomomi "You... you forced the masssk onto meee..."
        show saeko animated neutral sad with qleft #update with younger version
        sa "Tomomi... are you all right?  What's this about the mask?"
        hide saeko with qdis
        tomomi "The mask... the mask... suddenly wouldn't come... off... it got so hot... hot!"
        tomomi "My face started... it started sizzzzzling... And it's all... all... ALL!  "
        show tomomi burned at pleft2 with qleft
        extend "YOUR!  FAAAAAAULT!"
        hide tomomi with qdis
        show saeko animated neutral sad with qleft #update with younger version
        sa "Eeeeeeeeeek!"
        hide saeko with qdis
        scene bg black with dissolve #update with courtyard
        show ayase animated neutral serious with qleft
        ay "But that's, like, totally not your fault.  You didn't force it on her, right?"
        ay "So it's all Tomomi's misunderstanding!"
        hide ayase with qdis
        show saeko animated neutral sad with qleft
        sa "Maybe so.  But... I can't say with absolute confidence that that's true."
        sa "Maybe some part of me really was gloating over how much better I was."
        sa "Maybe I was just acting like Tomomi's best friend, when I never really cared."
        sa "Maybe I was too in love with the idea of being 'considerate Saeko'... And I only ended up hurting her."
        hide saeko with qdis
        show yukino animated neutral sad with qleft
        yu "Ms. Saeko..."
        hide yukino with qdis
        show saeko animated neutral sad with qleft
        sa "It's not the mask's curse!  What really made her that way is--"
        hide saeko with qdis
        show yukino animated neutral serious with qleft
        yu "Enough!"
        hide yukino with qdis
        pause 0.7
        show ayase animated neutral sad with qleft
        ay "Yeesh... It's so cold..."
        hide ayase with qdis
        show nanjo animated neutral serious with qleft
        na "......!  How could this be...?"
        hide nanjo with qdis
        show yukino animated neutral serious with qleft
        yu "What's up?"
        hide yukino with qdis
        show elly animated neutral serious with qleft
        el "We've defeated the Snow Queen and saved Ms. Saeko, but the school's still frozen!"
        hide elly with qdis
        show ayase animated neutral serious with qleft
        ay "Huh.  Come to think of it, the sky's still a weird color..."
        hide ayase with qdis
        unknown "Hmhmhm... You all must be so very cold.  Ahahahahah..."
        scene bg black with dissolve #update to show the snow queen
        $ tbnarrator = 1
        n "A woman appears behind the group, and with a flash of ice, freezes the ground beneath their feet."
        $ tbnarrator = 0
        show saeko animated neutral sad with qleft
        sa "Wh-What's going on!?"
        hide saeko with qdis
        show brown animated neutral sad with qleft
        br "Oh crap... oh crap...!  Not cool!  We just defeated it!"
        hide brown with qdis
        sq "The Tomomi inside me... The Tomomi with human weakness is dead.  I am grateful."
        sq "No longer tied to my host or the mask I was bound to, I am finally free.  Now I can be complete!"
        sq "I will become the Night Queen in full! I shall enshroud this world in black and white; void and sorrow."
        show yukino animated neutral serious with qleft
        yu "What!?"
        hide yukino with qdis
        nq "Foolish mortals who cling to hope... I shall teach you a lesson! I have not yet given up on the Eternal Night."
        nq "From the heights of this Ice Castle, I shall unleash the snows of despair.  Hmhmhm... Ahahahahahaha..."
        #update with the Night Queen vanishing
        show ayase animated neutral sad with qleft
        ay "Huh!?"
        #update music change
        extend "  What was that about?"
        hide ayase with qdis
        show nanjo animated neutral serious with qleft
        na "The Snow Queen symbolizes the darkness within Tomomi's heart."
        na "Thus, by holding up the Demon's Mirror which reflects all evil, Tomomi..."
        show nanjo animated neutral sad
        na "Sorry, the Snow Queen, "
        show nanjo animated neutral serious
        extend "saw how vile her heart had become."
        hide nanjo with qdis
        show yukino animated neutral serious with qleft
        yu "I get it!  Tomomi saw what she had become in the mirror and came to her senses."
        yu "Then her Persona, the Night Queen, had nowhere to go and went berserk."
        hide yukino with qdis
        show elly animated neutral serious with qleft
        el "That's the most likely scenario."
        hide elly with qdis
        show ayase animated neutral sad with qleft
        ay "Huh... So that means we like, have to defeat that Night thing too?"
        hide ayase with qdis
        show brown animated neutral smirk with qleft
        br "Thanks for the explanation.  I think I'm finally starting to get what's going on here."
        show brown animated neutral serious
        br "So if we don't defeat that Queen, we can't go home or take a hot bath!"
        hide brown with qdis
        show saeko animated neutral smirk with qleft
        sa "It hasn't been long since this started, and look how much you've all grown."
        hide saeko with qdis
        show ayase animated neutral smirk with qleft
        ay "Aww, well, I only made it this far 'cause I had everyone backing me up."
        ay "There's, like, no way I would've made it by myself..."
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "Yeah, thanks to these guys, well... I don't know how to say this, but..."
        show yukino animated neutral smirk
        yu "It's like I understand for the first time why I'm alive."
        hide yukino with qdis
        show ayase animated neutral smirk with qleft
        ay "Whoa, that sounds REALLY cool!"
        hide ayase with qdis
        show yukino animated neutral sad with qleft
        yu "Sh-Shut up!  Let's go, Naoya!"
        show yukino animated neutral smirk
        yu "Night Queen or Snow Queen or whatever, this team has nothing to be afraid of!"
        hide yukino with qdis
        show saeko animated neutral smirk with qleft
        sa "Haha... I'm leaving everyone in your hands, Naoya!"
        hide saeko with qdis
        $ tbnarrator = 1
        n "Ready to face onto your next challenge, you and your group ready up to move to take on the Night Queen."
        n "However, before you can depart, the room darkens once more."
        $ tbnarrator = 0
        show yukino animated neutral serious with qleft
        yu "Wh...what the!?"
        hide yukino with qdis
        #update with Tomomi appearing in the room again
        show ayase animated neutral serious with qleft
        ay "Whoa!  Is that...?"
        hide ayase with qdis
        show saeko animated neutral sad with qleft
        sa "Tomomi!"
        hide saeko with qdis
        show tomomi at pleft2 with qleft
        tomomi "Saeko... everyone... thank you.  It's because of you that I was able to return to myself."
        tomomi "That reflection... My heart was so awful that I couldn't look straight at it..."
        hide tomomi with qdis
        show yukino animated neutral serious with qleft
        yu "It's not just you, Ms. Tomomi.  I'm sure anyone's reflection would be horrible in that mirror."
        yu "Not very many people in the world with a truly pure heart..."
        hide yukino with qdis
        show brown animated neutral smirk with qleft
        br "Speak for yourself!  I'm innocent as a young girl, pure as an angel, and... "
        show brown animated neutral serious
        extend "Never mind."
        hide brown with qdis
        show ayase animated neutral smirk with qleft
        ay "I bet I'd look like some kinda monster."
        hide ayase with qdis
        show tomomi at pleft2 with qleft
        tomomi "If you looked right now, I know you wouldn't see a monster... I know!"
        tomomi "You should keep carrying the Demon's Mirror with you.  I bet it would protect you from misfortune."
        tomomi "Though it won't be easy to carry around in the form of a mirror, so..."
        hide tomomi with qdis
        $ tbnarrator = 1
        n "Tomomi reaches out a hand toward your mirror, and it changes shape, becoming a shield!"
        n ">Obtained Spiegel Shield."
        $ tbnarrator = 0
        show tomomi at pleft2 with qleft
        tomomi "And I don't know if you'll find a use for it or not, but..."
        tomomi "The hero's costume from 'The Snow Queen' should be in storage at the gym."
        tomomi "It was kept near the box with Snow Queen mask, to keep the seal strong."
        hide tomomi with qdis
        show yukino animated neutral smirk with qleft
        yu "Well, that's one piece of good news.  No idea where the storage room is in this Ice Castle..."
        yu "But it sounds like it's worth hunting for."
        hide yukino with qdis
        show tomomi at pleft2 with qleft
        tomomi "Ah... If only I'd met you all sooner..."
        tomomi "I'll be watching from above with the past Queens so no one else ends up like us.  Thank you."
        hide tomomi with qdis
        show ayase animated neutral serious with qleft
        ay "No way!  I'm the one who should be thanking you!  I've been hurting a lot of people and I never even knew before!"
        show ayase animated neutral sad
        ay "It's people like me that make it hard for others to trust the ones around them..."
        hide ayase with qdis
        show tomomi at pleft2 with qleft
        tomomi "Hahaha...you all keep growing..."
        hide tomomi with qdis
        $ tbnarrator = 1
        n "Tomomi's spirit fades away, finally at peace."
        $ tbnarrator = 0
        $ plotprogress = 14
        jump label099
    elif plotprogress == 14:
        scene bg black #update with frozen courtyard
        #play music library fadeout 0.5 fadein 0.5 #update
        call screen SQCourtyard
        if _return == 1:
            show yukino animated neutral serious with qleft
            yu "The Night Queen, huh...?  The bitch said she'd 'unleash the snows of despair from the heights of the castle.'"
            yu "Maybe there's a passage or something the Queen used to get up top.  Let's find it!"
        elif _return == 2:
            show ayase animated neutral serious with qleft
            ay "Does it feel a little warmer to you?  Y'think the Queen's losing her power?  Oh, yeah!"
            ay "Maybe that door that was frozen shut up to now is open!?"
        elif _return == 3:
            show elly animated neutral serious with qleft
            el "In order to sever the mask's curse, we absolutely must defeat the Night Queen."
        elif _return == 4:
            show brown animated neutral smirk with qleft
            br "Night Queen?  Sounds like some hostess at a Ginza club.  How strong could she be?  You guys'll do just fine without me."
            br "...I'm joking!  C'mon, let's go!"
        elif _return == 5:
            show nanjo animated neutral serious with qleft
            na "It's been quite some time since Masao and Maki left the school."
            na "I fear for those two if we don't make haste and put an end to this..."
        elif _return == 6:
            "jump to the navigation for SQQ"
            #update to jump to SQQ navigation
        elif _return == 7:
            show saeko animated neutral smirk with qleft
            sa "You've all become so strong in such a short time.  You have a look in your eye that says there's nothing you can't do."
            show saeko animated neutral serious
            sa "I have a feeling you'recapable of taking care of the rest.  Please sever the curse of the mask!"
            show saeko animated neutral sad
            sa "It's brought pain to so many students!  I'm counting on you..."
        jump label099


label label100 (location = "Velvet Room"):

#####Hypnos Tower######

label label101 (location = "Hypnos Tower"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The group enters into the Hypnos Tower.  The feeling within it is light and airy, almost comfortable."
    n "Still, the group does not let down their guard as they traverse the first floor of the tower."
    n "The demons are easily dispatched, and the group makes their way up to the second floor landing."
    n "Within, they find a girl who seemingly has wandered inside as well."
    $ tbnarrator = 0
    stu "Oh, hello!  Nice to meet you.  I'm Mariko Yabe from Yamakumo High's Paranormal Watchers Club!  Nice to meet you!"
    mariko "It's an unofficial club, and I'm the president and only member!"
    mariko "My homeroom teach refuses to recognize my club, just 'cause he thinks it's lame!"
    mariko "So I came to visit Tsutomu, my fellow devotee, but... I... this is... This is GREAT!"
    mariko "I'm SO lucky I get to see an awesome paranormal event like this!  I was just exploring those three freaky towers that popped up around campus!"
    mariko "They're chock-full of demons!  You wouldn't believe the photos I got!"
    mariko "I'm gonna submit these babies to some national magazines!"
    mariko "If the media admits they're real, maybe my teach will recognize my club!  Here goes nothin'!"
label label101a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos1
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "So we have until the hour hand points to 12 o'clock... This won't be easy."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "I've been feeling totally sleepy ever since we came to this tower!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "I support Mariko's love for the occult, but she should not be in a dangerous place such as this."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "I've seen that girl hanging around Devil-boy before.  She's a cutie!"
        show brown animated neutral serious
        br "But man...this tower has got me feeling tired.  Maybe I'll talk with her on the way back down."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "That Snow Queen... I'm sure it's sneering as it watches us gather 'mirror shards'."
    elif _return == 6:
        $ tbnarrator = 1
        n "You and your companions venture further within."
        $ tbnarrator = 0
        jump label102
    elif _return == 7:
        stu "Huh?  I'm out of film... Ugh!  Of all the rotten luck!"
    jump label101a

label label102 (location = "Hypnos Tower"):
    $ tbnarrator = 1
    n "The group makes it further within the tower, and soon finds themselves traveling upwards once more."
    n "Demons lurk around every corner, but the six of you are able to keep one another safe as you continue."
    n "However, as you enter into another room, you find a strange sight..."
    $ tbnarrator = 0
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "What the... Who's that on the floor?  Tadashi and Tamaki!?  And Nurse Natsumi!"
    show yukino animated neutral sad
    yu  "What are they doing here?  Weren't they back at school?  No way...!"
    hide yukino with qdis
    show nanjo animated neutral serious with qleft
    na "It took some time, but regular students are being claimed as victims..."
    show nanjo animated neutral sad
    na "I pity them, but there isn't time to waste.  We could be next."
    hide nanjo with qdis
    show brown animated neutral sad with qleft
    br "Tadashi... Tamaki... Nurse Natsumi...  How could this happen...!?"
    show brown animated neutral serious
    br "Damn that Snow Queen!  I'll avenge their deaths if it's the last thing I do!"
    hide brown with qdis
    show tadashi at pleft2 with qleft
    td "Tadashi: Zzzz... hrnk... lo... you... Tamaki...!  Zzzz..."
    hide tadashi with qdis
    show yukino animated neutral sad with qleft
    yu "T-Tamaki!?  Is he talking in his sleep?  Wait... they're all just sleeping!?"
    show yukino animated neutral serious
    yu "Tch... well, that was a lot of panic over nothing."
    hide yukino with qdis
    show nanjo animated neutral serious with qleft
    na "Hold it, Yukino.  Even if they are only sleeping, it's odd they should be here and not at school."
    na "It could be a trap of the Snow Queen's.  I advise keeping your guard up."
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "Hypnos Tower...  Hypnos is the god of sleep..! I agree with Kei- these three may have been forced into sleep by the Snow Queen!"
    hide elly with qdis
    show tamaki animated neutral smirk with qleft
    tm "Zzzz... Mmmm... I love you... da... shi... Zzzz..."
    hide tamaki with qdis
    show ayase animated neutral smirk with qleft
    ay "Look at those faces, though... they seem so happy!  I dunno if the Snow Queen really has anything to do with this."
    hide ayase with qdis
    show natsumi animated neutral smirk with qleft
    nat "Zzzz... Hahaha... Now be a good boy... Clean your plate..."
    hide natsumi with qdis
    show ayase animated neutral serious with qleft
    ay "Ugh... like, what's she dreaming about?  It makes me wanna pinch her nose."
    hide ayase with qdis
label label102a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos2
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Even if they are just sleeping, we can't leave them here surrounded by demons.  Let's wake them up before we move on."
        show yukino animated neutral sad
        yu "What?  They won't wake up?  Hm..."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Y'know what?  Tadashi acts up a lot, but he's not that bad-looking when he's asleep."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "If Hypnos is, in fact, tied to their strange slumber...  I doubt they'll wake up no matter how long we wait here."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "What, so they're just sleeping?  I got all anxious over nothing..."
        show brown animated neutral smirk
        br "Then again, I suspected from the start that was what was happening.  Really!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "If they're not in mortal peril, it should be fine to leave them.  We don't have time."
        na "Time is money, as they say.  Let's proceed."
    elif _return == 6:
        $ tbnarrator = 1
        n "You and your companions, unable to rouse the sleeping individuals, decide to continue onward."
        n "Yukino and Elly seem uncertain about leaving them behind, but Nanjo presses onward, and you all follow suit."
        $ tbnarrator = 0
        jump label103
    elif _return == 7:
        show natsumi animated neutral smirk with qleft
        nat "Zzzz... Mmmm... You won't escape this time... Now eat up..."
    elif _return == 8:
        show tadashi at pleft2 with qleft
        td "Zzzz... *hrnk*... I'll always hold you close to me..."
    elif _return == 9:
        show tamaki animated neutral smirk with qleft
        tm "Zzzz... I'll always be with you..."
    jump label102a

label label103:
    $ tbnarrator = 1
    n "Yukino seems to quietly bicker with Nanjo about leaving the others, but admits that it was the best choice."
    n "However, as another door is opened, you and your companions find a similar situation in this room."
    $ tbnarrator = 0
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "Great, more of them... ......!?  Wait a sec!  It's the principal and VP!"
    show yukino animated neutral smirk
    yu "Geez... Not setting a very good example."
    hide yukino with qdis
    show nanjo animated neutral sad with qleft
    na "Hmm.  The situation is more serious than I had thought."
    show nanjo animated neutral serious
    na "It's clear now that something is causing people in the school to fall asleep.  We must locate the cause."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "This is deplorable!  I work my ass off as a student, and what do the teachers do?  Lie back and doze off!  Get real!"
    hide brown with qdis
    show hanya at pleft2 with qleft
    ha "Zzzz... Heh heh heh... Hehe... hee..."
    hide hanya with qdis
    show ayase animated neutral sad with qleft
    ay "Ewww!  Baldy's sneering in his sleep... Gross!"
    hide ayase with qdis
    show nanjo animated neutral serious with qleft
    na "This is repulsive... I can't bear to look for another moment."
    na "That sort of man in a teaching position... What is this world coming to?"
    show nanjo animated neutral sad
    na "Is the principal all right, though?  She seems to be in distress."
    hide nanjo with qdis
    show elly animated neutral sad with qleft
    el "Oh no, Ms. Ooishi!  She must be having a nightmare.  Look, she's sweating so profusely... Did the Snow Queen cause this?"
    hide elly with qdis
    show ooishi at pleft2 with qleft
    oo "Zzzz... But... that's...!"
    hide ooishi with qdis
    show yukino animated neutral serious with qleft
    yu "They're just like the people in the other room.  None of them show any signs of waking up anytime soon."
    show yukino animated neutral sad
    yu "What should we do?"
label label103a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos3
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "We're not just gonna leave 'em here, are we?"
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Hey, like, now's our chance!  Let's draw stuff on Baldy's head!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "We're letting precious time go to waste in our indecision..."
        el "Whether we awaken the sleepers or climb the tower, we must make a choice."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Hmmmmm... Alright!  Listen to your leader's decision!  We're moving on!"
        show brown animated neutral serious
        br "Although... Wait a minute.  If we save them, they'll owe us one."
        show brown animated neutral smirk
        extend "  Whaddaya think?"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Oh, for crying out loud...!  Remind me why we entered the tower... To escape the school, correct?"
        na "Then we should ignore any distractions from that end!"
        na "You people allow yourselves too many unnecessary diversions."
    elif _return == 6:
        $ tbnarrator = 1
        n "Unable to rouse the principal or vice principal either, you and the others leave these ones behind as well."
        n "Yukino seems determined to find a way to wake them, and presses onward with a renewed vigor."
        jump label104
    elif _return == 7:
        show ooishi at pleft2 with qleft
        oo "Zzzz... Ugh... Unhhh... Mmmm... No..."
    elif _return == 8:
        show hanya at pleft2 with qleft
        ha "Zzzz... Prepare... for dictation... Shine... shoes... hehehe..."
    jump label103a

label label104:
    $ tbnarrator = 1
    n "The mood is heavy as you traverse the Hypnos Tower.  Brown and Ayase make jokes to try to lighten the mood, but Yukino is stubbornly quiet."
    n "However, soon the search rewards you with a large door that stands in your way, with an eerie feeling about it."
    $ tbnarrator = 0
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "What the hell is this place?"
    hide yukino with qdis
    show nanjo animated neutral sad with qleft
    na "Urgh... the drowsiness is practically palpable.  Almost overpowering..."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "Huh?  Ahhhh... I get it!  The boss has to be around here!  Stay on your toes, guys!"
    show brown animted neutral smirk
    br "Oooh, I always wanted to say that."
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Hey, uh, this door is kinda weird-looking.  Wanna go in?"
    hide ayase with qdis
    show nanjo animated neutral serious with qleft
    na "A blatantly suspicious door like that?  It would be madness to go near it."
    show nanjo animated neutral sad
    na "Though idle speculation won't help, either... What should we do?"
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "The door does look suspicious, but I don't get the sense that it's dangerous."
    show elly animated neutral smirk
    el "Perhaps we should consider Ayase's suggestion and go through."
    hide elly with qdis
    show yukino animated neutral serious with qleft
    yu "Alright!  No use talking and talking without doing anything.  Let's see what's on the other side!"
    hide yukino with qdis
    $ tbnarrator = 1
    n "The golden butterfly appears as you all talk amongst yourselves."
    $ tbnarrator = 0
    bf "Hahaha, still energetic, I see."
    #update with cutscene
    ph "How are you doing, friends?  This is a world of dreams, ruled by the Persona Hypnos of this tower's master."
    ph "Hypnos is currently trapping people'ssouls and confining them in the dream world."
    ph "Thus, this is a crossroadbetween the dream world and reality."
    ph "Either go to the dream world and awaken the people there or continue forth and defeat Hypnos - the choice is yours."
    ph "But remember: there is a limit to the time you are given."
label label104a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos4
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "I feel icky, watching someone else's dream... Like I'm some Peeping Tom."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I wonder if I end up in the Dream World when I go to sleep, too."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "The Dream World... Does that make me Elly in Slumberland, then?"
        show elly animated neutral smirk
        el "Hahah..."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "I'm interested in other people's dreams.  Looks like fun, huh?  Heh heh heh..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "We have no business here.  Let's press on."
    elif _return == 6:
        $ tbnarrator = 1
        n "A cloying breeze is blowing from beyond the door.  With your support, Yukino opens the door."
        n "There is no hesitation as the group moves within to see what awaits them."
        $ tbnarrator = 0
        jump label105
    jump label104a

label label105 (location = "Dreamworld"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As the group enters, they find themselves amidst a Yin & Yan convenience store."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Huh?  Who has dreams about a convenience store?"
    yu "I mean, I've had one or two about work, but this is different."
    hide yukino with qdis
    show natsumi animated neutral smirk with qleft
    nat "So, what do you want for dinner tonight?"
    hide natsumi with qdis
    man "Anything's fine, as long as I have it with you... How was that?  Hahaha!"
    show nanjo animated neutral serious with qleft
    na "Ah, this must be Nurse Natsumi's dream.  Then I assume that's her recent ex."
    na "He's not bad, if not quite at my own level.  None too bright, either."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "Huh?  Is that the guy Nurse Natsumi just broke up with?  He's pretty handsome."
    show brown animated neutral smirk
    br "Not like me of course, but not bad."
    hide brown with qdis
    show ayase animated neutral smirk with qleft
    ay "Whoa!  Nurse Natsumi's boyfriend is, like, smoking hot!  I SO wish I had an awesome guy like him."
    hide ayase with qdis
    show natsumi animated neutral smirk with qleft
    nat "Oh, you're so funny!  Come on, what are you in the mood for?"
    nat "Let's decide quick and check out, so we can go back home and eat."
    hide natsumi with qdis
    man "Uh, what?  Didn't you tell me you were gonna cook for me today, hon?"
    show nanjo animated neutral serious with qleft
    na "Wait, is she going to feed him the corner store's ready-made meal?"
    show nanjo animated neutral sad
    na "Correct me if I'm wrong, but I don't believe that counts as 'cooking'..."
    hide nanjo with qdis
    show elly animated neutral sad with qleft
    el "Oh, Nurse Natsumi... Don't tell me she's acting as though she cooks the store's pre-made lunches..."
    el "I feel sorry for him..."
    hide elly with qdis
    show natsumi animated neutral smirk with qleft
    nat "Yeah, and I will!  I'll warm it up for you in the microwave once we get to my place."
    nat "Oh, how about this 'Surprise Cutlet Combo'?  It says it's their latest item!"
    nat "Sounds delicious, doesn't it?  Let's get two of these, honey!"
    hide natsumi with qdis
    man "Uh... Y-Yeah, anything's fine.  I can't wait to dig in... Haha...ha..."
    show yukino animated neutral sad with qleft
    yu "This... is painful to watch, in so many ways.  Let's wake her up and move on."
label label105a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos5
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "Big surprise she got dumped, huh?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Hey, you think eating the food in a dream is bad for you?"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "This is fantastic!  To think that the human subconscious can create such a realistic environment!"
        el "This convenience store looks authentic in every respect!"
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "I wonder if we can bring any of this food back to the real world...  Man, what a waste."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "No clerk, no other shoppers... This place is more unsettling than a convenience store late at night."
    elif _return == 6:
        man "What the hell do you want from us!?  Huh!?"
    elif _return == 7:
        show natsumi animated neutral serious with qleft
        nat "What do you want!?  Try anything funny and I'll call for the police!"
        hide natsumi with qdis
        $ tbnarrator = 1
        n "Naoya, at Yukino's behest, pinches Natsumi to awaken her from this dream."
        $ tbnarrator = 0
        show natsumi animated neutral serious with qleft
        nat "Wh-What's happening?"
        hide natsumi with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "As Natsumi awakens, the dream ends.  The darkness surrounds your group for a moment before a new dream appears..."
        $ tbnarrator = 0
        jump label106
    jump label105a

label label106:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As the dream comes into focus, they find themselves in the principal's office at their very own school."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Huh?  We're... in the principal's office?  What the hell...?"
    hide yukino with qdis
    show hanya at pleft2 with qleft
    ha "Vice-Principal Ooishi.  You presume to tell your principal that his education policies are wrong?"
    ha "Is that what you're getting at, Ooishi?"
    hide hanya with qdis
    show ooishi at pleft2 with qleft
    oo "No, Mr. Hanya, I didn't mean it that way."
    oo "I just think punishing students for being tardy three times with either expulsion or having to shine the principal's shoes until graduation is a bit... harsh."
    hide ooishi with qdis
    show nanjo animated neutral serious with qleft
    na "It seems we're witnessing a shared dream of the principal and vice-principal.  But here, the roles are reversed..."
    na "I'd wager our principal was dragged into that arrogant vice-principal's dream."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "What the... Hanya is the principal and Ooishi is the vice-principal!? What's going on here...?"
    show brown animated neutral smirk
    br "Ohhh, I get it!  This is what they're dreaming."
    hide brown with qdis
    show ayase animated neutral sad with qleft
    ay "Whaaaaat!?  Baldy's our principal here?  That's like, SUPER wrong!"
    hide ayase with qdis
    show hanya at pleft2 with qleft
    ha "Excuse me, Ooishi!?  Did I just hear your criticize the eminently fair rules I came up with?"
    ha "Hmm... I think this calls for a new rule.  Anyone who criticizes the principal's decisions is fired!"
    ha "Do you hear me?  Fired!"
    hide hanya with qdis
    show ooishi at pleft2 with qleft
    oo "'Came up with'!?  Do you often 'come up' with regulations without putting any thought into them!?"
    hide ooshi with qdis
    show nanjo animated neutral serious with qleft
    na "This is utterly ridiculous.  I can't bear to watch anymore.  Should a real educator be saying this sort of thing?"
    hide nanjo with qdis
    show elly animated neutral sad with qleft
    el "Vice-Principal Hanya's desire for power must be very strong..."
    el "Not only does his dream reflect them, it pulled in Ms. Ooishi..."
    hide elly with qdis
    show hanya at pleft2 with qleft
    ha "S-Silence!  What's wrong with coming up with school rules!?  I'm the most important person in this school!"
    ha "Why, I'm essentially a god!  My word is god's word, the will of the universe!  Don't you see!?"
    hide hanya with qdis
    show ooshi at pleft2 with qleft
    oo "Mr. Hanya!  What do you think the purpose of education is!?  To begin with..."
    hide ooshi with qdis
    show yukino animated neutral serious with qleft
    yu "Let's hurry and wake 'em up.  I can't stand listening to this."
label label106a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos6
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "I gotta say, this is a realistic-looking principal's office."
        show yukino animated neutral serious
        yu "If you hadn't told me I was in a dream, I wouldn't have suspected a thing."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "C'monnnnn... Let's get back to school.  I'm sooooo tired!"
    elif _return == 3:
        show elly animated neutral sad with qleft
        el "I'd thought the Dream World would be more... romantic."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Whoa, nice couch!  Wanna take a little breather?  Heheh... just kidding."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Perhaps I shouldn't say this, since we're encroaching on the dreams of others..."
        show nanjo animated neutral sad
        na "But I find that seeing a person's naked desires leaves a bad taste in my mouth."
    elif _return == 6:
        show ooishi at pleft2 with qleft
        oo "Not now, please.  I must get the principal to reconsider."
        hide ooishi with qdis
        $ tbnarrator = 1
        n "Naoya follows the same action as before, pinching Ooishi to wake her from this dream."
        $ tbnarrator = 0
        show ooishi at pleft2 with qleft
        oo "Oh!"
        hide ooishi with qdis
        show hanya at pleft2 with qleft
        ha "Wh-What the!?"
        hide hanya with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "Once the two start to wake, this dream ends as well, leaving you in a dark void."
        n "But the dreams do not end as another begins to take shape."
        $ tbnarrator = 0
        jump label107
    elif _return == 7:
        show hanya at pleft2 with qleft
        ha "Pipe down!  Don't bother me right now!"
        $ tbnarrator = 1
        n "Naoya follows the same action as before, pinching Hanya to wake him from this dream."
        $ tbnarrator = 0
        show hanya at pleft2 with qleft
        ha "Wh-What the!?"
        hide hanya with qdis
        show ooishi at pleft2 with qleft
        oo "Oh!"
        hide ooishi with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "Once the two start to wake, this dream ends as well, leaving you in a dark void."
        n "But the dreams do not end as another begins to take shape."
        $ tbnarrator = 0
        jump label107
    jump label106a

label label107:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The familiar sights of the Fencing Club room take shape around them, as do the voices of its two main residents."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "This is... the fencing club room.  Which means..."
    hide yukino with qdis
    show tadashi at pleft2 with qleft
    td "T-Ta-Ta-Tamaki!  I love you!  I love you with every fiber of my being!"
    hide tadashi with qdis
    show tamaki animated neutral smirk with qleft
    tm "Tadashi... I love you too..."
    hide tamaki with qdis
    show nanjo animated neutral serious with qleft
    na "So we're inside their dream... In the real world, they argue  incessantly.  But I see now."
    na "It's a classic example of 'fighting because they care.'"
    hide nanjo with qdis
    show brown animated neutral sad with qleft
    br "Nooooo!  Oh, the humanity!  I refuse to believe Tamaki likes Tadashi!"
    br "Someone, please tell me it's all a dream!  Wait... it IS a dream!"
    show brown animated neutral serious
    br "Or is this reality and the other side is the dream...?"
    hide brown with qdis
    show ayase animated neutral smirk with qleft
    ay "Omigawd!  I knew it!"
    hide ayase with qdis
    show tadashi at pleft2 with qleft
    td "Honey... look into my eyes...!"
    hide tadashi with qdis
    show tamaki animated neutral smirk with qleft
    tm "I am, darling...!"
    hide tamaki with qdis
    show nanjo animated neutral serious with qleft
    na "Far be it from me to cast aspersions, but this is unbearable to watch... In more ways than one."
    hide nanjo with qdis
    show elly animated neutral smirk with qleft
    el "Th-They seem awfully happy... Haha... I'd rather not interfere."
    hide elly with qdis
    show tadashi at pleft2 with qleft
    td "Look me in the eyes... Do you see yourself?  I see myself in your eyes... Ah!  We're united as one!"
    hide tadashi with qdis
    show tamaki animated neutral smirk with qleft
    tm "Yes... Yes!  I see myself in your eyes!  And you see yourself in mine? This is wonderful... You and I are one!"
    hide tamaki with qdis
    show yukino animated neutral serious with qleft
    yu "...Okay, they can keep at this once they're awake.  Let's wake them up already."
    hide yukino with qdis
label label107a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos7
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "Being in someone else's dream feels kinda awkward, you know?"
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Awww... Those two are like a pair of jailbirds.  I wish I could be like them."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "One wouldn't think to look at this room that we were in the Dream World."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "I'm begging you, man!  Leave a poor, broken man alone for a while... Ahh... Tamaki...!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "It's often difficult to convey one's true feelings to another... Especially between a man and a woman.  Interesting, no?"
    elif _return == 6:
        show tadashi at pleft2 with qleft
        td "Argh!  Stop bothering us!  Can't you see we're in the middle ofsomething!?"
        td "You're really rude, you know that?"
        hide tadashi with qdis
        $ tbnarrator = 1
        n "Having come to understand the process, Naoya pinches Tadashi to wake him up."
        $ tbnarrator = 0
        show tadashi at pleft2 with qleft
        td "Huh?  Wh-What?"
        hide tadashi with qdis
        show tamaki animated neutral sad with qleft
        tm "Huh?  Wh-Why?"
        hide tamaki with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "Tamaki and Tadashi fade away, and so does their dream world.  You believe that you will return to the real world."
        n "But as another dream starts to manifest, you have to wonder just who's dream you're in now..."
        $ tbnarrator = 0
        jump label108
    elif _return == 7:
        show tamaki animated neutral serious with qleft
        tm "Stop getting in our way!  If you ruin this moment..!"
        hide tamaki with qdis
        $ tbnarrator = 1
        n "Having come to understand the process, Naoya pinches Tamaki to wake her up."
        $ tbnarrator = 0
        show tamaki animated neutral sad with qleft
        tm "Huh?  Wh-Why?"
        hide tamaki with qdis
        show tadashi at pleft2 with qleft
        td "Huh?  Wh-What?"
        hide tadashi with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "Tamaki and Tadashi fade away, and so does their dream world.  You believe that you will return to the real world."
        n "But as another dream starts to manifest, you have to wonder just who's dream you're in now..."
        $ tbnarrator = 0
        jump label108
    jump label107a

label label108 (location = "Dreamworld?"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The room that takes shape almost appears to be someone's room, as a large bed rests in the back."
    n "Unlike the previous dreams, however, this one is completely foreign to you and your friends."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "What the...?  This doesn't feel like the other rooms.  Is this someone else's dream?"
    yu "...Huh?  Someone's back there!"
    hide yukino with qdis
    #show kumi at pleft2 with qleft
    stu "Oh... We have company... What a surprise."
    #hide kumi with qdis
    man "Indeed it is.  Shall we entertain our guests?"
    show nanjo animated neutral serious with qleft
    na "What's going on?  She's wearing our school's uniform.  Is this her dream, then?"
    hide nanjo with qdis
    show brown animated neutral smirk with qleft
    br "Woooow! She's a cutie!  Hm...?  Wait a sec, Nanjo's right!  She's got our school uniform on!"
    br "How the heck did I never notice a girl like her before!?"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Hey, what's your name?  Which homeroom are you in?  Are you trapped here too?"
    hide ayase with qdis
    #show kumi at pleft2 with qleft
    stu "Heehee... Why are you people here?  This dream is for myself alone."
    stu "The Snow Queen entrusted me with guarding this Hypnos Tower..."
    stu "But it would be rude not to introduce myself.  My name is Kumi Hirose."
    kumi "It's very rude of you to barge into someone else's dream.  Isn't it,  Sir Hypnos?"
    #hide kumi with qdis
    hypnos "Indeed it is.  And not just anyone's dream, Kumi, but yours.  They don't know their place."
    hypnos "What would you have me do, Kumi?  If it's all right with you, I can teach them a lesson."
    show nanjo animated neutral serious with qleft
    na "The guardian of this tower... Then you're the ones responsible for confining people in the Dream World."
    na "But why go about it in such a roundabout way rather than simply kill them?"
    na "What do you intend to do with the souls trapped in the Dream World!?"
    hide nanjo with qdis
    #show kumi at pleft2 with qleft
    kumi "Heehee... You came all this way to ask me that?  But I guess it can't be helped."
    kumi "You're forced to live in the real world, just like the rest."
    kumi "But isn't it clear that people are happiest living inside their dreams?"
    #hide kumi with qdis
    show elly animated neutral serious with qleft
    el "Surely you are mistaken.  Dreams are wonderful to be sure, but these dreams you've given people are false."
    el "You must let them come back to the real world so they can pursue these dreams in reality!"
    hide elly with qdis
    #show kumi at pleft2 with qleft
    kumi "They can never be happy in the real world... I'm just helping them see that."
    kumi "Isn't that right, Sir Hypnos?"
    #hide kumi with qdis
    hypnos "Indeed it is, Kumi.  You've done nothing wrong.  It's they who are the villains."
    hypnos "But it's inevitable that they don't understand you.  They have no idea what you went through in the real world..."
    hypnos "And the joy that filled your heart as you came to this world of dreams."
    hypnos "Now, let us show them the cruelty you faced in the real world... And teach them the splendor of dreams!"
    show yukino animated neutral sad with qleft
    yu "Huh...?  Wh-What's going on!?"
    hide yukino with qdis
    scene bg black with dissolve
    $ tbnarrator = 1
    n "The world around you goes dark, and you can hear the sounds of St. Hermelin once more as you find yourselves in the Drama Club room."
    $ tbnarrator = 0
    scene bg black with dissolve #update to Drama club
    #play music library fadeout 0.5 fadein 0.5 #update
    pres "Kumi, I've noticed you haven't been showing up to rehearsal lately."
    pres "You have the title role in 'The Snow Queen' and you're not evenrehearsing?"
    pres "What's the matter with you!?  Everyone else is working hard!  Do you feel even remotely guilty?"
    pres "Don't you realize how important your part is!?"
    stu "Yeah, Kumi!  You can't act like that when you won the Snow Queen part over our president."
    stu "Aren't you getting a little full of yourself?"
    stu "Really, though, we do need you to come to rehearsals.  We can only do so much with your understudy."
    stu "Talk to us, Kumi..."
    #show kumi at pleft2 with qleft
    kumi "Um... I've had to... s-study...  My grades went down, and... my p-parents said to forget the club... and study..."
    #hide kumi with qdis
    stu "Oh, geez!  Here we go with the class genius's parents!"
    stu "What a load of crap.  You were third in our grade for that last test, right?"
    stu "How can you call that bad!?"
    #show kumi at pleft2 with qleft
    kumi "Um... I wasn't... n-number one..."
    #hide kumi with qdis
    stu "Oh, give me a break!  What, is that sarcasm or something?"
    stu "Just 'cause you're smarter than most doesn't mean you can act all stuck up!"
    stu "If studying's so important, then go ahead and quit the club!"
    stu "I'm not gonna mince any more words... You've been a real pain in the ass!"
    #show kumi at pleft2 with qleft
    kumi "I... I didn't mean to..."
    #hide kumi with qdis
    pres "Alright, so you've told us why you haven't been coming."
    pres "But listen, Kumi... are you taking this club seriously?  Do you understand how many people it affects when you don't show up?"
    pres "Do you know how much trouble it causes when you focus on your own business?"
    pres "Kumi... can you tell me what your role is in this club?  Because if you don't know, I have to ask you to leave."
    stu "Yeah, she's absolutely right!  You heard her!  Get outta here!  Stupid, stuck-up dork..."
    stu "Having a depressing loner like you around brings us all down!"
    stu "I'm sorry, but the president has a point.  You should think carefully, Kumi."
    stu "What's more important: your life or your grades?"
    #show kumi at pleft2 with qleft
    kumi "......"
    #hide kumi with qdis
    scene bg black with dissolve
    $ tbnarrator = 1
    n "The nature of the dream changes again, into the interior of a home.  Kumi stands facing her father."
    $ tbnarrator = 0
    scene bg black with dissolve #update to Kumi's house
    #play music library fadeout 0.5 fadein 0.5 #update
    father "...Are you still fooling around with that script, Kumi?"
    father "Refresh my memory, what are you doing to school for again?  To study?  Or to fool around?"
    #show kumi at pleft2 with qleft
    kumi "U-Um... it's just... the 'Snow Queen,' see... I was chos--"
    #hide kumi with qdis
    father "Yes, your mother told me.  Apparently you scored in the 70s on some tests lately?"
    father "You get those low scores because you don't study.  You just fool around all the time."
    #show kumi at pleft2 with qleft
    kumi "But-- My average was eighty-"
    #hide kumi with qdis
    father "I gave up drinking and smoking, as much as I loved them..."
    father "And I quit playing golf on weekends so I could make more money.  Who do you think that's for!?"
    father "I'm providing for you and your mother, aren't I?"
    father "You're attending that school now because your father's working himself to death."
    #show kumi at pleft2 with qleft
    kumi "...I know, Father."
    #hide kumi with qdis
    father "But you still don't even think about what I'm going through..."
    father "Instead, you get lost in some club and never spend a moment studying."
    father "You're in the wrong here, Kumi."
    #show kumi at pleft2 with qleft
    kumi "......"
    #hide kumi with qdis
    scene bg black with dissolve
    $ tbnarrator = 1
    n "Things fade away, this time showing the interior of a bedroom."
    $ tbnarrator = 0
    scene bg black with dissolve #update to Kumi's room
    #play music library fadeout 0.5 fadein 0.5 #update
    #show kumi at pleft2 with qleft
    kumi "...Why is everyone cross at me?  What did I do?  Whether I do or don't do anything, it's always like that..."
    kumi "All of them... The world around me. The people around me.  Everyone's so... full of hostility..."
    kumi "I feel like I don't have any freedom... Do I have to exist in this reality with all these other people...?"
    kumi "If only there was a gentle world... filled with gentle people...  A whole world full of kindness and generosity..."
    kumi "Where I could be free...  Some dream, huh...?  Hah... Yeah, a dream... that only happens when I'm asleep in this bed..."
    kumi "It's the only free world I have left, where no one complains about me...  The world of dreams..."
    kumi "I wish I could just live there... In my dream world, made only for me..."
    #hide kumi with qdis
    scene bg black with dissolve
    $ tbnarrator = 1
    n "Kumi's memory comes to an end, and around you, the room with the bed appears once more."
    $ tbnarrator = 0
    scene bg black with dissolve #update to Hypnos Tower
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral sad with qleft
    yu "Huh... That's what made you shut yourself up in the Dream World."
    show yukino animated neutral serious
    yu "...And?"
    hide yukino with qdis
    #show kumi at pleft2 with qleft
    kumi "Th-That's all you can say, even after seeing what happened?  H-How dare you!?"
    kumi "The Snow Queen... the mask immediately understood my pain and anguish...!"
    kumi "Y-You're just like my father and the others in the drama club! You don't even try to understand me!"
    #hide kumi with qdis
    hypnos "K-Kumi!  You must calm yourself!"
    show nanjo animated neutral serious with qleft
    na "Oh, for heaven's sake!  You fled to the Dream World for such absurd, trivial reasons?"
    na "That's so appalling that I'm speechless.  You're making a mockery of your own life."
    hide nanjo with qdis
    show brown animated neutral smirk with qleft
    br "C'mon, Kumi, aren't you taking it all a little too seriously?  I mean, life's full of fun stuff!"
    br "You gotta take it easy!  Live a little!  Like me!"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Gimme a break!  You just did that so you could brag about your awesome grades!"
    ay "So what if I'm stupid!?  Ohhh, I cannot BELIEVE this!  I'm like, SO pissed!"
    hide ayase with qdis
    #show kumi at pleft2 with qleft
    kumi "But... but...!  What could I do?  No matter what I did or didn't do, no one gave me a hint of praise!"
    kumi "I tried my best, really I did!  But everyone around me just..."
    kumi "Right, Sir Hypnos!?  None of it was my fault, right!?"
    #hide kumi with qdis
    hypnos "Indeed, Kumi.  You've done nothing wrong!  It's clear who's at fault..."
    show elly animated neutral serious with qleft
    el "'The others,' right?  Your life seems very easy..."
    el "Any problem of yours is solved by blaming someone else from a safe distance."
    el "Are you that afraid of dealing honestly with other people?  I must say, you seem rather weak and selfish to me."
    hide elly with qdis
    #show kumi at pleft2 with qleft
    kumi "Wh-Who do you think you are!?  I'm happy now!  I've never been happier!"
    kumi "It was the Snow Queen's mask and Sir Hypnos who saved me, no one else!"
    kumi "For the first time in my life, I'm free, here in the Dream World!"
    kumi "It may not be real, but the happiness I feel inside is!"
    #hide kumi with qdis
    show yukino animated neutral serious with qleft
    yu "Yyyeah... I'm gonna call that bluff.  This is the Dream World, right?"
    yu "Then both of you are just part of Kumi Hirose's dream.  I'm guessing the real Kumi is somewhere else in the tower."
    yu "And that means if we pinch her and wake her up, you're history.  So that's exactly what we'll do!"
    show yukino animated neutral smirk
    yu "Shake off those cobwebs and wait for us, 'cause we're on our way!"
label label108a (location = "Dreamworld"):
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos8
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "So Kumi's the boss of this tower..."
        show yukino animated neutral smirk
        yu "Bet she has a 'Mirror Shard' or two."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Ooooooh!  She SO gets on my nerves!  Let's go kick her ass!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "That Hypnos character who stood beside Kumi... I hope he's nothing more than the ideal 'Prince' of her dreams..."
        el "A mere figment of her imagination."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Hmm... life is tough... I'm smart and I still got problems, so I kinda get how Kumi feels."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "What is the matter with that girl!?  Her entire outlook on life is a joke."
        na "I'm most irked by her idea of herself as "
        show nanjo animated neutral sad
        extend "the only sufferer in the world."
    elif _return == 6:
        #show kumi at pleft2 with qleft
        kumi "Wh-What do you want!?  If you lay even a finger on me, Sir Hypnos will punish you!"
        #hide kumi with qdis
        hypnos "Insolent fool!  Don't you dare touch Kumi!"
        $ tbnarrator = 1
        n "Naoya confidently moves up to Kumi and pinches her, even as she tries to flinch away."
        $ tbnarrator = 0
        #show kumi at pleft2 with qleft
        kumi "Rrgh... You...!  I'll remember this!"
        #hide kumi with qdis
        scene bg black with dissolve
        $ tbnarrator = 1
        n "The dream world begins to falter, breaking apart around you and your group."
        n "Soon it dissolves entirely...and you find yourselves back at the doorway, now sealed shut."
        $ tbnarrator = 0
        jump label109
    jump label108a

label label109 (location = "Hypnos Tower"):
    scene bg black with dissolve
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Eager to make sure their friends were now all right following the insight into their dreams, Yukino heads back to check on them."
    n "She makes a beeline for Tadashi and Tamaki, and enters the room with the rest of the group close behind."
    $ tbnarrator = 0
    scene bg black with dissolve #update with SQ Room for Tadashi/Tamaki
    #play music library fadeout 0.5 fadein 0.5 #update
    show tadashi at pleft2 with qleft
    td "Don't worry... No matter what happens, I'll protect you.  Tamaki... I want you to trust me!  I love you!"
    hide tadashi with qdis
    show tamaki animated neutral sad with qleft
    tm "We fought a lot, but that was because I worried about you, Tadashi. You're always so reckless..."
    show tamaki animated neutral smirk
    tm "You probably had no idea how I felt.  But thanks to that dream, I can admit my feelings... I love you, Tadashi!"
    hide tamaki with qdis
    show yukino animated neutral smirk with qleft
    yu "Oh, here it comes... I dunno how they can keep at it.  On the plus side, all three of you are awake."
    show yukino animated neutral serious
    yu "Anyone feel sick or anything?"
    hide yukino with qdis
    show tadashi at pleft2 with qleft
    td "Argh!  It was just getting good!  Why'd you have to butt in!?  Right, Tamaki?"
    hide tadashi with qdis
    show tamaki animated neutral serious with qleft
    tm "Yukino...?  You guys... what are you doing here?"
    hide tamaki with qdis
    show nanjo animated neutral serious with qleft
    na "They don't seem to remember anything.  Ignorance is bliss, as they say."
    na "...I'm certainly glad we wasted our time and effort saving them."
    hide nanjo with qdis
    show brown animated neutral sad with qleft
    br "Whaaaaat!?  Get real, Tamaki!  I went through allllll that trouble to save you, and you don't remember a thing!?"
    br "Now that hurts... This sucks."
    hide brown with qdis
    show tadashi at pleft2 with qleft
    td "Remember?  What the heck are you talking about?  We were... Huh?  Why are we here?"
    td "I was having a nice dream, and when I woke up... Tamaki was there... Looking right at me..."
    hide tadashi with qdis
    show yukino animated neutral smirk with qleft
    yu "Alright, alright!  We get it!  Congrats, both of you.  Just keep the lovey-dovey crap to yourselves!"
    show yukino animated neutral serious
    yu "I'll get out of your hair if you just tell me one thing... Do either of you have a 'Mirror Shard'?"
    show yukino animated neutral sad
    yu "It's really important."
    hide yukino with qdis
    show tamaki animated neutral sad with qleft
    tm "I'm not sure...sorry, I'm still trying to wake up a little here..."
    show nanjo animated neutral serious with qleft
    na "Hmph.  As I expected.  As Yukino stated, we're searching for 'Mirror Shards'. Do either of you have one?"
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "We need those shards to save the school."
    show elly animated neutral smirk
    el "Do you have any idea what we're talking about?"
    hide elly with qdis
    show tadashi at pleft2 with qleft
    td "...Nope!  All I have is my hand mirror for fixing my hair.  Is that good enough?"
    hide tadashi with qdis
    show tamaki animated neutral serious with qleft
    tm "Of course not, dummy!"
    tm "......!  Is this what you meant...?"
    show tamaki animated neutral sad
    tm "I don't know how it got there, but this was in my pocket..."
    hide tamaki with qdis
    show tadashi at pleft2 with qleft
    td "Wh... What!?  Tamaki!  Y-You never told me you had that!"
    td "No... We pledged ourselves to each other... And you kept a secret from me!"
    td "Oh, the pain!"
    hide tadashi with qdis
    show tamaki animated neutral serious with qleft
    tm "Hey!  I only just noticed, okay!?  Quit being stupid!  Just... let me talk!"
    show tamaki animated neutral smirk
    tm "Here you go, Main.  Hope this helps.  "
    show tamaki animated neutral sad
    extend "Sorry... I wish I could do more to help..."
    tm "I mean, I guess Tadashi and me could go with you, but... I think we'd only hold you guys back."
    show tamaki animated neutral smirk with qleft
    tm "Thanks for saving us.  Best of luck!"
    hide tamaki with qdis
    $ tbnarrator = 1
    n ">Obtained a Mirror Shard."
    $ tbnarrator = 0
    show tadashi at pleft2 with qleft
    td "Uhh... I don't really understand what's going on, but good luck, guys!"
    td "Leave Tamaki to me!"
    hide tadashi with qdis
    show ayase animated neutral smirk with qleft
    ay "Wow!  Talk about good luck!  We got ourselves a Mirror Shard!"
    ay "Good thing we took a little side trip to the Dream World.  Oh, hey!"
    ay "If Tamaki and Tadashi had a shard... Maybe Nurse Natsumi has one, too!  Let's ask her!"
    show ayase animated neutral serious
    ay "Nurse Natsumi?  Do you have a Mirror Shard?  Nurse Natsumi...?  Helllooooo!"
    ay "Earth to nurse!  Caaaan youuuu heaaaar meeeee?  Weee neeeed aaaa shaaaard!"
    ay "Are you even awake!?"
    hide ayase with qdis
    show natsumi animated neutral serious with qleft
    nat "...Stop yelling... I have low blood pressure... Ow ow ow... my head..."
    nat "A mirror...?  Don't have one of those... Good night... Zzzz..."
    hide natsumi with qdis
    show ayase animated neutral serious with qleft
    ay "Aww, she doesn't have one?  Guess we woke her up for nothing. Bleaaaaah!"
label label109a:
    scene bg black #update with frozen library
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos9
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "Well then, wanna go beat up the boss?"
        show yukino animated neutral sad
        yu "Actually, we should go and check on Principal Ooishi."
        show yukino animated neutral serious
        yu "And Hamya, I guess."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Oooooh, I wish I could be in a totally hot relationship too!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "It was purely a coincidence..."
        show elly animated neutral smirk
        el "But ultimately, Hypnos played Cupid for Tadashi and Tamaki."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Thanks to my incredible work, all three of them are just dandy."
        show brown animated neutral smirk
        br "Mwahahahaha!  I'm a natural-born leader!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Well, there goes a good deal of our precious time.  No more complaints, I hope?  Good.  Then let's move on."
        show nanjo animated neutral sad
        na "Though... I admit, I'm glad to see the three of them safe."
    elif _return == 6:
        $ tbnarrator = 1
        n "You agree with Yukino's suggestion, and lead the group into checking on the Principal and Vice-Principal."
        $ tbnarrator = 0
        jump label110
    elif _return == 7:
        show natsumi animated neutral serious with qleft
        nat "Aaaaargh!  I'm wide awake now, but I've got a whopper of a headache."
        show natsumi animated neutral smirk
        nat "I had a nice dream, though... Too bad it got interrupted right at the best part..."
    elif _return == 8:
        show tadashi at pleft2 with qleft
        td "You're done, right?  Then can you give us some privacy?  Please?"
    elif _return == 9:
        show tamaki animated neutral serious with qleft
        tm "I'm sorry, but Tadashi's all I can think about right now."
    jump label109a

label label110:
    scene bg black
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The six of your make your way back through the tower, fending off demons as you return to the room with Ooishi and Hanya."
    $ tbnarrator = 0
    scene bg black with dissolve #update with SQ Room for Ooishi/Hanya
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "Ms. Ooishi!  Mr. Hanya!  You're finally awake!  How are you feeling?"
    hide yukino with qdis
    show hanya at pleft2 with qleft
    ha "Y-Yukino!  Just what's going on here!?  Where in blazes am I?  ...This is all your doing, isn't it!?"
    ha "You pack of delinquents!  What are you up to, locking us in here!?"
    ha "Dammit, I was having such a nice dream, and now I can't remember any of it!  Arrrgh!"
    ha "Will someone please explain to me what's going on!?"
    ha "Urrrgh, you ask them, Ms. Ooishi!  They'll listen to you!"
    hide hanya with qdis
    show ooishi at pleft2 with qleft
    oo "Have you calmed down yet, Mr. Hanya?  First off, are any of you hurt?  That's the most important thing."
    hide ooishi with qdis
    show ayase animated neutral smirk with qleft
    ay "No way!  We're like, totally fine."
    hide ayase with qdis
    show ooishi at pleft2 with qleft
    oo "Good, good.  Now then... where are we?  I had the most awful dream, and..."
    hide ooishi with qdis
    show nanjo animated neutral serious with qleft
    na "This may be difficult for you to grasp, but we saved both of your lives."
    na "We aren't asking for your thanks, and we certainly don't deserve your anger.  I'm sure you understand, mm?"
    na "That aside... do either of you know anything about the Mirror Shards?  They're of the utmost importance to us."
    hide nanjo with qdis
    show hanya at pleft2 with qleft
    ha "I don't have anything to say to you delinquents!  Nanjo, are you leading this group of misfits?"
    hide hanya with qdis
    show brown animated neutral sad with qleft
    br "Oh, come ON, Mr. Hanya!  How can you call us delinquents!?"
    show brown animated neutral serious
    br "With a little support from these guys, I was risking my neck out there!  All to save you and Ms. Ooishi!"
    br "Wouldn't you say I deserve at least a little thank-you for that?  Then again... I guess it's all right."
    show brown animated neutral smirk
    br "What's done is done!  What's more important now is these Mirror Shards.  Do either of you know anything?"
    br "They're super important if me and these guys are gonna save the school.  Any ideas?  Any at all...?"
    hide brown with qdis
    show hanya at pleft2 with qleft
    ha "Mirror Shards!?  Oh, you mean this?  I don't know how it got there, but that was in my suit pocket."
    ha "It ripped a hole in the inside!  My daughter starts her job soon!  I can't ask her to mend my clothes anymore..."
    ha "*ahem* Th-That wasn't relevant.  Forget what I just said!  Anyway, just what are you kids planning to do with this!?"
    ha "Nothing good, I'll bet!  Absolutely not!  Out of the question!"
    ha "Something tells me if I give you this, the situation will get even worse!"
    hide hanya with qdis
    show ayase animated neutral serious with qleft
    ay "Seriously!?  Are you for real!?  What's wrong with you, cueball!?"
    ay "You didn't even let us explain, and you're gonna say no just like that!?"
    ay "Ooooooh, you're the worst!  This is why everyone likes the principal and NO ONE likes you!"
    ay "Now gimme that shard, chromedome!  Hand it over, baldo!  GIVE IT, damn you!  You assface!"
    hide ayase with qdis
    show ooishi at pleft2 with qleft
    oo "Now, now, Ayase.  Ladies shouldn't use such language."
    oo "Mr. Hanya, please refrain from scolding the students before hearing them out."
    oo "I'd like you to make an effort to put yourself on their level.  It should be clear to you then whether the students are lying or not."
    oo "You can decide whether to scold them after that.  Now I ask that you please give them this Mirror Shard."
    oo "I can see in their eyes that they haven't done anything wrong."
    hide ooshi with qdis
    show hanya at pleft2 with qleft
    ha "......Okay.  Here you go."
    hide hanya with qdis
    $ tbnarrator = 1
    n "Obtained a Mirror Shard."
    $ tbnarrator = 0
    show elly animated neutral serious with qleft
    el "I'm sorry... But we need this, not just for ourselves, but to save the entire school."
    hide elly with qdis
    show nanjo animated neutral serious with qleft
    na "Indeed. We're the only ones at this school with a clear understanding of what must be done."
    hide nanjo with qdis
    show ooishi at pleft2 with qleft
    oo "I won't ask for an explanation... not at the moment, anyway.  I can see that you're doing what you believe to be right."
    oo "But don't push yourselves too hard.  And whatever you do, don't disappoint those who have you in their hearts."
    oo "Now, go, and do what you must.  Luck be with you."
    hide ooishi with qdis
    show hanya at pleft2 with qleft
    ha "Hmph!  I won't bother trying to stop you.  Go on!  Do whatever you please!  ......But listen up!"
    ha "If... When the school is back to normal... see me in the office!  I have a special lecture in mind..."
    ha "After which I'll demand a full explanation!  So come prepared!  The Principal and I will be waiting!"
    ha "I want all of you there, understood?  Not one missing!"
    hide hanya with qdis
    show yukino animated neutral serious with qleft
    yu "Ms. Ooishi... Mr. Hanya..."
    show yukino animated neutral smirk
    yu "Heh... Don't worry, you can hold us to it! All of us!  See you later!"
    hide yukino with qdis
label label110a:
    scene bg black #update with frozen ooishi/hanya room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos10
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "I don't think there's anything left to do here.  We should move on and find Kumi."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Heheh!  The vice-principal is gonna love us now!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "At any rate, I'm glad the two of them are safe."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Cool!  Now the vice-principal owes me one!  Heheheh... I won't let him walk over me anymore, that's for sure!"
        show brown animated neutral sad
        br "...On second thought... I take it back. He's still a scary guy..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "He may not have earned our respect, but he is still our teacher.  It's good that everything turned out well in the end."
    elif _return == 6:
        $ tbnarrator = 1
        n "With your classmates and teachers secured, you make the call to head up to the top of the tower."
        n "You have already met Kumi in the dreamworld, but now it's time to meet her in the real world."
        n "Yukino and Nanjo bolster the others and you begin the climb to the top of the Hypnos Tower."
        $ tbnarrator = 0
        jump label111
    elif _return == 7:
        show ooishi at pleft2 with qleft
        oo "I had the worst dream... I'm glad I can't remember anything about it."
    elif _return == 8:
        show hanya at pleft2 with qleft
        ha "Mmm... It was such an amazing dream... Ugh, I can almost remember it! What was it about...?"
    jump label110a

label label111:
    scene bg black
    $ tbnarrator = 1
    n "With your classmates and teachers secured, you make the call to head up to the top of the tower."
    n "You have already met Kumi in the dreamworld, but now it's time to meet her in the real world."
    n "Yukino and Nanjo bolster the others and you begin the climb to the top of the Hypnos Tower."
    n "After some time, battling through the demons of the tower, you find an area to rest just before confronting Kumi."
    $ tbnarrator = 0
label label111a:
    scene bg black #update with frozen ooishi/hanya room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQHypnos11
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "We've come pretty far up.  I think we're near the end."
        show yukino animated neutral smirk
        yu "I better get psyched for what's coming!"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "Urgh, I'm soooo tired!  Sheesh!  Isn't there like, an elevator around!?"
    elif _return == 3:
        show elly animatd neutral smirk with qleft
        el "Fortunately, we didn't fall asleep.  Let's stay cautious and press onward."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Gaaaah!  I'm so tired!  For crying out loud, can't we take a little rest?"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Even if we pick up high-quality equipment, it's useless unless we put it on."
        na "Be sure to check what you're using from time to time."
    elif _return == 6:
        $ tbnarrator = 1
        n "Ready to move onward, you and your group continue climbing the tower to find its master."
        $ tbnarrator = 0
        jump label112
    jump label111a

label label112:
    scene bg black with dissolve
    $ tbnarrator = 1
    n "Before long, you've reached the top of the tower, and as you open the doors, you and your group can see Kumi within."
    $ tbnarrator = 0
    scene bg black with dissolve #update with Tower room
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "Well, here we are... Right, Kumi!?  Sorry to keep you waiting..."
    show yukino animated neutral smirk
    yu "But we're here now to straighten you out!"
    hide yukino with qdis
    show kumi at pleft2 with qleft
    kumi "So you came...  You fools.  You can't see outside the bounds of reality... You can't grasp or accept the paradise of dreams!"
    hide kumi with qdis
    show nanjo animated neutral serious with qleft
    na "Excuse me, but who's calling who a fool?  You're the coward who lived her life constantly fleeing from her problems..."
    na "And now you flee even from that life!  What more is there to say?  Prepare yourself to face us!"
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "Kumi... I dunno what to say... It really tears me up having to fight a cutie like you... But I gotta.  But I gotta!"
    show brown animated neutral smirk
    br "For truth, justice, and the St. Hermelin way!  Plus I gotta show off all these wicked skills I know!"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Like, whatever!  Us five can take a nerd like you any day!  Now's the time to apologize if you're gonna!"
    hide ayase with qdis
    show kumi at pleft2 with qleft
    kumi "Judging others by their appearance only proves how foolish you are... Sir Hypnos!  Help me!  Defeat them, please!"
    #show hypnos appearing in front of the party.
    show elly animated neutral serious with qleft
    el "Could that be... Kumi's Persona!?  Then the Hypnos we met in the Dream World wasn't a product of her dream!"
    hide elly with qdis
    show kumi at pleft2 with qleft
    kumi "Sir Hypnos!  They've invaded my dream to bully me!  Please, crush them!"
    hide kumi with qdis
    show yukino animated neutral serious with qleft
    yu "Hmph! If she's a Persona-user, there's no need to pull our punches! Alright guys, here we go!"
    hide yukino with qdis
    scene bg black with dissolve #update with hypnos battle
    #play music library fadeout 0.5 fadein 0.5 #update
    hypnos "Allow me to teach you the wonders of the Dream World... An eternal slumber from whence there is no awakening..."
    show yukino animated neutral serious with qleft
    yu "Yeah, right... in your dreams, pal!"
    hide yukino with qdis
    $ tbnarrator = 1
    n "With difficulty, you and your allies overcome and overpower Hypnos, leaving you all victorious."
    $ tbnarrator = 0
    scene bg black with dissolve #update with hypnos room
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "You're done.  That precious prince of yours... The Persona your heart made is gone."
    yu "You wanna keep going at it?  Suits me either way..."
    hide yukino with qdis
    show kumi at pleft2 with qleft
    kumi "...So this is it... There's no place for me anywhere... Not in the real world or the dream world..."
    kumi "Haha... I have to flee my own dream.  Ahahaha..."
    hide kumi with qdis
    show nanjo animated neutral serious with qleft
    na "Those who lack dreams are generally shallow and tedious. But those who focus solely on chasing their dreams lack substance."
    na "Don't lose sight of your dream, but don't allow it to overtake you, either."
    na "A dream is not a goal to chase... Nor is it a place to hide... A dream is that which sustains your soul."
    na "But it will never be yours if you do nothing but wait for it to come to you.  Dreams are not given.  You must reach out and take them!"
    show nanjo animated neutral sad
    na "...So Yamaoka often told me."
    hide nanjo with qdis
    show brown animated neutral smirk with qleft
    br "An easy win, thanks to me!  Although..."
    show brown animated neutral sad
    extend "  It kinda left a bad taste in my mouth..."
    hide brown with qdis
    show ayase animated neutral smirk with qleft
    ay "Whoo!  We won!  Hah!  In your face!  Well?  Had enough yet?  Hmmm?"
    hide ayase with qdis
    show kumi at pleft2 with qleft
    kumi "You're all so strong.  If only I was like you... I might have ignored the Snow Queen mask and went on with my life..."
    kumi "But I just blamed everyone else.  I went to my safe place and nursed my grudge."
    kumi "I... I acted just like the people that I blamed for everything..."
    hide kumi with qdis
    show elly animated neutral smirk with qleft
    el "Kumi... Now that you acknowledge your weakness, you're no longer weak."
    el "A dream is like an oasis in one's soul... It quenches the thirst of travelers exhausted from life's journey."
    show elly animated neutral serious
    el "But pleasant though the oasis may be... The travelers must continue the journey."
    el "We must all cross the desert of reality, no matter how harsh it becomes..."
    hide elly with qdis
    show kumi at pleft2 with qdis
    kumi "Thank you, everyone... I wish friends like you were there for me back then..."
    kumi "I'll always remember you... Thank you... and goodbye."
    hide kumi with qdis
    #show Kumi disappearing here
    $ tbnarrator = 1
    n "Obtained Mirror Shard."
    $ tbnarrator = 0
    show yukino animated neutral sad with qleft
    yu "Kumi Hirose wasn't so bad, really.  She was a victim of the mask... It twisted her."
    show yukino animated neutral serious
    yu "...Well, let's go back!  We gotta save Ms. Saeko!"
    $ tbnarrator = 1
    n "You have conquered Hypnos Tower!"
    $ tbnarrator = 0
    $ plotprogress = 11
    # update jump to SQQ navigation

label label113 (location = "Nemesis Tower"): #Nemesis Tower
    scene bg black with dissolve
    $ tbnarrator = 1
    n "As you come into the Nemesis Tower, there is a strange sensation that washes over you."
    n "Unlike the Hypnos Tower, this feels more targeted and malicious."
    $ tbnarrator = 0
    scene bg black with dissolve #update with nemesis room
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral sad with qleft
    yu "It feels weird in here... like someone's giving me a nasty look..."
    hide yukino with qdis
    unknown "Ohohohoho!  Good day to you all.  It's a delight to see you here in this tower."
    unknown "Allow me to extend a warm welcome.  Ohohohohohohohohoho!"
    show elly animated neutral serious with qleft
    el "Who are you?  Show yourself!  I assume you're the guardian of this tower..?"
    hide elly with qdis
    show nanjo animated neutral smirk with qleft
    na "Ha... Some guardian this is.  You're merely an ass in lionskin, hiding behind the Snow Queen!"
    hide nanjo with qdis
    show ayase animated neutral smirk with qleft
    ay "Yeah, you hear that?  You're scared of us, aren't you?  Hahaha!"
    ay "Hey guys!  This tower's boss seems, like, totally weak, huh?  Lucky us! Hahahahaha!"
    hide ayase with qdis
    #update with Michiko appearing
    show michiko at pleft2 with qleft
    stu "Ohohohohohoho!  What a litter of witless, yapping whelps you are!  But it's all to the good..."
    stu "I think you can keep me entertained for a while.  Weak playmates fall so easily I rarely get to enjoy my sport!"
    stu "Ohohoho... I haven't introduced myself, have I?  My deepest apologies. I am the Snow Queen's faithful servant..."
    stu "The guardian of Nemesis Tower... Michiko Matsudaira."
    michiko "I hope you grasp the honor of dying by my hand.  Incidentally...... Hm?  You... Yes, you!"
    michiko "Oh, what a pleasant surprise!  Such a fine, handsome gentleman!  I'll spare your life if you become my pet.  What say you?"
    hide michiko with qdis
    show brown animated neutral sad with qleft
    br "Uh... what!?  Me!?  W-W-Wait a second!  "
    show brown animated neutral serious
    extend "What the hell!?  Who do you think you are, Ugly!?"
    br "Comin' outta nowhere and saying that stuff... You think that I, the magnificent Brown, would stoop to be your pet!?"
    br "'Cause that ain't funny, dammit!  I don't serve anyone- I'm the hero!"
    hide brown with qdis
    show michiko at pleft2 with qleft
    michiko "What? Th-This is outrageous!  I take pity on you... and you bite back in response!?  H-Hmph!"
    michiko "I suppose you commoners could never understand my greatness.  Very well... Then I'll execute each of you whelps myself..."
    michiko "The time restriction on this tower is hereby lifted!  Take all the time you want!"
    michiko "Come to me, no matter what it takes!  Once more... take as much time as you want!"
    michiko "I look forward to seeing you!  Until then... farewell!"
    hide michiko with qdis
    #update with Michiko disappearing
    show yukino animated neutral serious with qleft
    yu "Michiko Matsudaira... Looks like she won't go down easy."
label label113a:
    scene bg black #update with frozen Nemesis tower room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis1
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "No time limit?  From the way she was acting, there's gotta be a catch. Don'tcha think?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Hmm... That Michiko girl totally reminds me of someone.  You know how she's like, super arrogant?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "No time restriction...?  I wonder what that's all about."
        el "Is it her way of saying even without a handicap, we're no match for her?  Or... is it something else?"
        el "Whatever the truth, it's clear that she's hiding something."
        el "It may be best for us to hurry, even without a strict time limit to observe."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "She's so egotistical, it's like she was born that way..."
        br "And she acts like she's better than everyone in the whole world!"
        show brown animated neutral smirk
        br "Just between you and me, she's a lot like our very own Mr. Nanjo!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "What an insolent girl!  Ugh, did you see how she looked down on us!?"
        na "Does she think she's the greatest woman on Earth or something?"
        na "Well, I'm very much offended!  Not to put too fine a point on it, I'm infuriated!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Filled with some trepidation about the lack of a time limit, you and the others agree to continue onward."
        n "You lead the others further into the tower, dealing with the demons as they approach."
        $ tbnarrator = 0
        jump label114
    jump label113a

label label114:
    scene bg black with dissolve

    $ tbnarrator = 1
    n "The tower holds many stronger demons than the Hypnos Tower, requiring more effort from you and your team."
    n "Brown suggests a quick break, finding an unused side room in the Tower and you step inside."
    n "Within, you once again find Mariko, who has gotten into this tower as well."
    $ tbnarrator = 0
label label114a:
    scene bg black #update with frozen Nemesis tower room w/ Mariko
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis2
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "There's no time limit here, right?  So let's take our time and prepare."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "That girl totally, like, reminds me of Devil-boy."
        show ayase animated neutral smirk
        ay "Omigosh, do you think they're dating?"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "She has much to learn if she cannot yet distinguish between aliens and demons."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Man, who knew being a hero was so much work?"
        show brown animated neutral smirk
        br "It's almost as much work as my look in the morning!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "That girl, honestly.  Does she not realize the danger she's in?"
    elif _return == 6:
        $ tbnarrator = 1
        n "After the break finishes (and ignoring Brown's complaints) you return to the tower climb."
        $ tbnarrator = 0
        jump label115
    elif _return == 7:
        mariko "According to my investigation, aliens are behind this school-freezing phenomenon!"
        mariko "Have you been abducted by any UFOs in the last two or three days?"
    jump label114a

label label115:
    $ tbnarrator = 1
    n "As you enter the room, you see both Tsutomu and Toro being tortured by a demon-like entity."
    $ tbnarrator = 0
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    devil "Hey!  Who said you were allowed to spill the milk!?  That milk is good for you!"
    devil "And you get to drink all you want... You should be happy, you gluttonous little porker!"
    devil "Now go on!  Drink, drink, and drink some more! Hahahahahaha!"
    show toro at pleft2 with qleft
    tor "*gulp* *glug* *gulp* *ulp* Ugh... Uuuuuuurgh!  Bluuuuugh! *cough* *gag* *puke*"
    tor "S-Stop...!  H-Help me!  P-Please, n-no more milk...!  I'm lactose-intolerant!"
    hide toro with qdis
    devil "And you, four-eyes!  What're you sticking your ass in the air like that for?"
    devil "It only counts as a push-up if your whole body is close to the ground!"
    devil "If you keep doing it wrong, I'll have to give you more reps again! Hahahahaha!"
    show devilboy animated neutral sad with qleft
    db "*gasp* *gasp* Aaaarrrrgh!  Ugh...!  I... I can't do this...!  I... I'm a thinking man..."
    db "My brain is my strongest... muscle...  My arms... simply aren't made... to do... push-ups...!"
    hide devilboy with qdis
    show yukino animated neutral serious
    yu "Toro!?  And Tsutomu!  What're you guys doing here!?  I thought you were both back at school!"
    hide yukino with qdis
    show toro at pleft2 with qleft
    tor "Please... stop!  I beg you!  B-Bluuuuuuurrrgh!  I... I'm gonna die... Ugh..."
    hide toro with qdis
    devil "Hey!  Don't pass out, porky!  You have to keep drinking!"
    devil "Think of yourself as a machine... An automation made to consume milk!"
    show devilboy animated neutral sad with qleft
    db "I... *pant* can't move... anymore...  "
    show devilboy animated neutral smirk
    extend "Ha... Hahaha... Ahahahaha... haha..."
    hide devilboy with qdis
    devil "Keep it up, dork!  Don't lose it yet!  It's Lady Michiko who'll deal with you two in the end!"
    devil "If you break now, she'll definitely punish me for it!"
    show nanjo animated neutral serious with qleft
    na "It seems it's as I suspected... Michiko is behind all this."
    na "Though I must say, her methods of torture are very well-planned... very effective."
    na "She's exploiting their weaknesses in the most efficient manner."
    na "But as near as I can tell, though, there's no purpose to it."
    show nanjo animated neutral sad
    na "Torture simply for the sake of it... frightening indeed."
    hide nanjo with qdis
    show elly animated neutral sad with qleft
    el "Oh, no!  They can't hold out much longer!  We must do something about it now, before it becomes too late!"
    hide elly with qdis
    show devilboy animated neutral smirk with qleft
    db "Hahaha!  Wow!  A fairy!  Haha... hahaha... I really saw it, Mom! Hahahaha..."
    hide devilboy with qdis
    show toro at pleft2 with qleft
    tor "*puke* *cough* *hack* ...!  Huh...?  A-Ayase!  You guys!  P-P-P-Please save me!"
    hide toro with qdis
    show ayase animated neutral sad with qleft
    ay "Uhhhh... Save these two goons...?  I wanna say, 'No way!'  But like, why's Michiko doing this?"
    ay "Is there some point I'm not getting?"
    hide ayase with qdis
    #update with Michiko appearing
    show michiko at pleft2 with qleft
    michiko "Ohohohoho!  It's because they're hideous!  And ugliness is unforgivable!"
    michiko "Therefore I, the acme of attractiveness, am punishing these sinners!"
    michiko "Do you understand, whelps?  Ohohohohoho!"
    hide michiko with qdis
    show brown animated neutral serious with qleft
    br "Who the HELL do you think you are!?  You stuck-up bitch!  How dare you do this to Toro and Devil-Boy!?"
    br "Oh, there was a line there, and you just crossed it!  Cut this out and get those chains off them right now!"
    hide brown with qdis
    show michiko at pleft2 with qleft
    michiko "Oh, you care deeply for your friends, mm?  What a beautiful friendship, yes?  Ohohohohoho!  How splendid!"
    michiko "Hah!  'Friendship!'  Then in honor of your admirable friendship..."
    michiko "I'll tell you where the key is so you can free these ugly fellows from their chains!"
    michiko "It can be found on the topmost floor of this tower... That's right--it's in my care!  Ohohoho!"
    michiko "If you wish to save yourprecious friends, come to me without delay!  Ohohoho!"
    michiko "Exit the door on your left and follow the path to reach my room in no time...  Ohohohohoho!"
    michiko "However... Those Mirror Shards you so eagerly seek... You may find one through the door behind me."
    michiko "The Mirror Shard is kept within a large chest there... Along with a hint to defeat me.  Ohohohohohohoho!"
    michiko "Remember, there's no timerestriction in this tower!  Spend as much time as you like searching!"
    michiko "You only have to ask that your friends endure the torture a while longer. Ohohohohohoho!"
    michiko "The choice is yours!  I'll see you soon!  Ohohoho!  Ohohohohohohoho!"
    hide michiko with qdis
    #update with Michiko disappearing
    show toro at pleft2 with qleft
    tor "Help me, please!  Get that key quick!  Blurrrrgh... T-The key... please...!"
    hide toro with qdis
    show devilboy animated neutral sad with qleft
    db "Ugh... Uuuuuugh... Where... oh where... is the key... to unchain my heart...? *gasp* *pant*"
    hide devilboy with qdis
    devil "What are you doing!?  Stop slacking!  Hahahahaha!  Gulp that milk!  Work those muscles!"
    show yukino animated neutral sad with qleft
    yu "We gotta help them, but we need that Mirror Shard, too.  What should we do?"
    hide yukino with qdis
label label115a:
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis3
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Michiko... We'll get you for this...!"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "It's a good lesson for those two, though, don'tcha think?  I mean, they're kinda lame..."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Gah, I can't stand that Michiko!"
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "They get on my nerves sometimes, but they're not that bad.  I wanna help 'em out!"
    elif _return == 5:
        show nanjo aniamted neutral serious with qleft
        na "It's immaterial to me whether we aim for the Mirror Shard or save these two..."
        na "My primary concern is beating some manners into that Michiko!"
    elif _return == 6:
        $ tbnarrator = 1
        n "The group seems torn on whether or not to help their friends or go after the Mirror Shard to help everyone."
        n "Eventually, Nanjo and Yukino convince Ayase to go up to put Michiko in her place first and foremost."
        n "Resolved to do so, the group begins to long tower climb to rescue their friends...but also deal with Michiko."
        $ tbnarrator = 0
        jump label116
    elif _return == 7:
        devil "I'm only doing what Lady Michiko ordered.  If you have a problem, take it up with her."
    jump label115a

label label116:
    scene bg black with dissolve
    $ tbnarrator = 1
    n "Climbing upward, you find yourselves at a door on the fourth floor.  Entering within reveals a small, safe area to rest."
    $ tbnarrator = 0
label label116a:
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis4
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Having no time limit is even more ominous, in a way."
        show yukino animated neutral sad
        yu "I think we should hurry on ahead."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "This tower is, like, totally creepy, y'know?  Let's hurry and get through it."
    elif _return == 3:
        show elly animated neutral sad with qleft
        el "Can we hurry ahead with all possible haste?  I can't shake this feeling..."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Hey, c'mon!  There's no time limit on this tower, right?"
        br "So let's take a break!  We can kick back a bit and then get right to it!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Gah, that Michiko woman gets on my nerves!  She's infuritating!  Truly infuriating!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Unwilling to wait, you all-but pull Brown along through the door to the next set of stairs."
        $ tbnarrator = 0
        jump label117
    jump label116a

label label117:
    scene bg black with dissolve
    $ tbnarrator = 1
    n "Fighting through the next floor, the winding tower once again ends at an ornate door to continue further."
    $ tbnarrator = 0
label label117a:
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis5
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "What a gaudy door.  Just the kind of thing Michiko would use... It makes me sick!"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I wonder if that Michiko girl ever, like, played the part of the 'Snow Queen,' too."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Er... If this door is meant to be a trap, it's a rather obvious one."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "I wish I could take this door back to my room!  It's one kickass door..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Hmph!  The woman's door is as infuriating as she is!"
        na "All show on the outside, lacking any substance within!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Frustrated, tired and annoyed, you and your allies continue the seemingly endless climb up the tower."
        $ tbnarrator = 0
        jump label118
    jump label117a

label label118:
    scene bg black with dissolve
    $ tbnarrator = 1
    n "A room, eerily similar to the one you had just come, stands at the end of the next floor."
    $ tbnarrator = 0
label label118a:
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis6
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Oh, for the love of... not again.  What's with these hideous doors!?"
        yu "Wasn't there one like it earlier, too?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "It's like, we walk and walk and we never get to the top!  I!  AM!  TIRED!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "I feel that this tower is much higher than it appears from outside.  Is it just me?"
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Yukino's right!  There was a room like this downstairs, too!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Dammit... I can sense Michiko's malice in the air itself!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Eriko proposes that this is perhaps part of Michiko's plan, to wear them out before you encounter her."
        n "It seems likely, and that only makes Nanjo more vocal about defeating her now, leading the group onwards."
        $ tbnarrator = 0
        jump label119
    jump label118a

label label119:
    scene bg black with dissolve
    $ tbnarrator = 1
    n "The tower continues to ascend, and yet another floor lays behind you."
    n "Another door stands in your way at the end, but this seems to be the end of the climb, or so you hope."
    $ tbnarrator = 0
label label119a:
    scene bg black #update with frozen Nemesis tower room w/ Toro/Tsutomu
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQNemesis7
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Ugh!  I can't stand this claustrophobic feeling this tower gives me!"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "I wonder if Toro and Tsutomu are okay..."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Whew... this is tiring, both mentally and physically.  I still believe it's Michiko's doing."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Alright!  Looks like Michiko's room is coming up soon!"
        br "Might as well check our equipment, huh?"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "This is one time I won't be holding back!  What that Michiko did is unforgivable!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Despite their exhaustion of climbing and battling demons, everyone is ready to continue."
        n "Whether to save Tsutomu and Toro, or simply to unleash their frustration on Michiko, all are in agreement."
        n "With everyone on the same page, you lead the group through the final door, to the top of the tower."
        $ tbnarrator = 0
        jump label120
    jump label119a

label label120:
    scene bg black #update with frozen Nemesis tower room w/ Michiko
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As you enter the final room, the door closes behind you.  Michiko looks surprised to see you present so early."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Michiko Matsudaira!  We're here for you!  Give us the key to free Toro and Tsutomu!"
    yu "We can take it by force, if that's the way you want to play it!  "
    show yukino animated neutral smirk
    extend "That's my plan, anyway."
    yu "I have a feeling you won't give up that easily, huh?"
    hide yukino with qdis
    show michiko at pleft2 with qleft
    michiko "I-Impossible!  You're here so soon!?  Wh-What about the Mirror Shard?  Didn't... Didn't you go get it?"
    michiko "Oh... Oh...!  How can this be!?  The source of my strength... the power of negative emotion...!"
    michiko "The hatred and anger is too weak!  This won't be enough at all!  Not only that, but..."
    michiko "What are these disgusting feelings that flow into me?  Gratitude...? Friendship...!?"
    michiko "THIS is what those two are thinking as they're being tortured?  No... You couldn't have...!"
    michiko "You figured out how this tower works!?  No!  Simply impossible!  My plans were flawless!"
    hide michiko with qdis
    show nanjo animated neutral serious with qleft
    na "Frankly, I'd normally be happy to leave those two and retrieve the Mirror Shard.  Hmph!"
    na "As if I gave a damn what that empty head of yours was scheming.  But you made one fatal error..."
    na "You have angered me."
    hide nanjo with qdis
    show michiko at pleft2 with qleft
    michiko "Without exception, humans think, 'As long as I'm okay, others don't matter.'"
    michiko "This mindset... no, it's even more atavistic than that!  It's instinct!"
    michiko "My plans revolve around the basic human instict for self-preservation!  So why?  Why!?"
    michiko "Why would you try to help others with the expectation of no reward? I can't understand at all!"
    michiko "My strength... This level of power is FAR from adequate!  What am I supposed to do?"
    hide michiko with qdis
    show brown animated neutral serious with qleft
    br "I'd never turn my back on my friends!  It's bad for my rep, man!  And I'd DEFINITELY never forgive a bitch like you!"
    br "This is for torturing Toro and Tsutomu!  For calling us all 'whelps'!  But most of all... "
    br "For saying I'm your pet!  You're gonna pay royally for that one!  Now let's get this showdown started!"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "And you know what?  We don't even need all twelve Mirror Shards!  Eight or so should do the job just fine!"
    ay "I like, don't care too much about what happens to Toro or Tsutomu."
    ay "But seeing a jerk like you act like some stuck-up celeb... Now that totally pisses me off!  Get it?"
    hide ayase with qdis
    show michiko at pleft2 with qleft
    michiko "Silence!  Silence!  SILENCE!  Let me be clear on this... You're saying that I am inferior to that hideous pair?"
    michiko "I, the lovely Michiko?  Oh... Oh...!  This is outrageous!"
    michiko "My magnificent plans were simply too sophisticated for you mangy curs!  Oh... Oh...!"
    michiko "I knew I should have slain you all as soon as you entered this tower!  Ohhhhh!"
    hide michiko with qdis
    show elly animated neutral serious with qleft
    el "Give in, Michiko.  The more you squall, the more prominent your unsightliness becomes..."
    show elly animated neutral smirk
    el "You should see yourself in a mirror.  Ahaha... I, for one, would be ashamed to look that way in public."
    show elly animated neutral serious
    el "Ayase is right.  A failure to acquire a couple of Mirror Shards in this tower won't hurt a bit."
    el "Let's draw a line under this conversation, shall we?  However much we explain it..."
    el "You'll never understand our reasons for coming directly here. Now, en garde!"
    hide elly with qdis
    scene bg black #update with Nemesis battle
    #play music library fadeout 0.5 fadein 0.5 #update
    nemesis "Aaaaaaahahahaha!  THIS is my true form!  Soooo lovely... and soooo elegant!"
    show yukino animated neutral serious with qleft
    yu "...You gotta be joking!  I've had enough with the fun and games already!  I'm so disgusted I can barely speak."
    hide yukino with qdis
    show ayase animated neutral serious with qleft
    ay "Like, have you ever even SEEN a mirror!?  You don't look like that at ALL!"
    hide ayase with qdis
    nemesis "ScreeeeeeeeEEEEE!  Silence!  Silence!  SILENCE!   I'll slice those insolent faces right off!"
    $ tbnarrator = 1
    n "Weakened by the lack of negative emotions, Nemesis is unable to overcome you and your allies."
    n "Driven by his frustrations, Nanjo deals a mortal blow, before Elly and Brown assist to finish her off."
    $ tbnarrator = 0
    scene bg black #update with frozen Nemesis tower room w/ Michiko
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral smirk with qleft
    yu "Hmph... game, set, and match!  Or do you wanna go another few rounds?"
    hide yukino with qdis
    show michiko at pleft2 with qleft
    michiko "I... I lost!?  Unbelievable... Inconceivable!  And to a pack of crude delinquents, no less!"
    michiko "Oh!  How can this be?  Oh...!  Ohhhhh!"
    hide michiko with qdis
    show nanjo animated neutral serious with qleft
    na "You are so tiresome.  You lost, and we won.  That's an indisputable fact."
    na "It won't change no matter how much you squall and twist that unsightly face."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "Yeah! You got a beatdown from me, the always-amazing Brown, and his gang!"
    br "Is that getting through to you!?  So stop honking like a seal and get out of our sight!  PLEASE!?"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Yup, that's right!  You're like, totally, hopelessly stupid.  I'm sick of looking at your stupid face."
    ay "Will you just get outta here?  Like, now?"
    hide ayase with qdis
    show michiko at pleft2 with qleft
    michiko "Aaaaaaaaaaaaaaaaaagh!  What manner of egotistic, abhorrent monsters are you!?"
    michiko "I've done nothing, yet the five of you gang up on me, then gloat in triumph!  People are always like that!"
    michiko "You lot are no exception! And neither are those ugly faces on the walls who once senselessly bullied me!"
    michiko "Don't you understand!?  All I did was leverage my vast wealth to land the role of the Snow Queen!"
    michiko "And also have that floozy hanging around my beau in the drama club expelled!"
    michiko "And bribe the teachers to lift my grades slightly more towards acceptability!  But those morons in my class..."
    michiko "They called me names!They talked behind my back!  They gave me the cold shoulder!"
    michiko "Only the SnowQueen mask ever extended a helping hand to me!  That's right... it and no one else!"
    michiko "Only the mask understood my profound sorrow!  My wretched circumstances!"
    michiko "Tell me, what right does anyone have to pick on poor, little me!?  I certainly can't understand!"
    hide michiko with qdis
    show elly animated neutral serious with qleft
    el "What?  But it's entirely your fault!"
    el "Is this really why you abandoned the real world to be a minion of the Snow Queen?"
    el "Unbelievable... You've completely lost the plot...!"
    hide elly with qdis
    show michiko at pleft2 with qleft
    michiko "Aaaaaaagh!  You continue to mock me, even after knowing my heartrending past?"
    michiko "I can't believe this!  I've had enough!  I suppose it was entirely too much to ask..."
    michiko "How could you, the poor in spirit, understand my sorrow!?  Hmph! Fine!  I'll give you a win, this once!"
    michiko "But I warn you... In due time, the thirst for revenge churning in me will be denied no more!"
    michiko "And on that day, I shall once again give you hell!  Remember that!  I'll stand in your way, again and again!"
    michiko "Do look forward to it!  Until then... Farewell!  Ohohohohohoho!  Ohohohohohohohohoho!"
    hide michiko with qdis
    #update with michiko disappearing
    $ tbnarrator = 1
    n "Obtained Mirror Shard."
    $ tbnarrator = 0
    show brown animated neutral smirk with qleft
    br "At least Kumi had it rough.  Bitchiko here deserved what she got for standing up to the Great Brown!"
    hide brown with qdis
    show yukino animated neutral serious with qleft
    yu "Michiko Matsudaira... If I never see her again, it'll be too soon."
    show yukino animated neutral smirk
    yu "Oh, hey!  I wonder if Toro and Tsutomu are okay..."
    show yukino animated neutral serious
    extend "That stupid Michiko!"
    yu "She didn't even give us the key!  We should check on 'em once we get back to school.  C'mon, let's go."
    $ tbnarrator = 1
    n "You have conquered Nemesis Tower!"
    $ tbnarrator = 0
    $ plotprogress = 12
    # update jump to SQQ navigation

label label121 (location = "Thanatos Tower"):
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The oppressive aura of the tower is only seen further as you step into the main entrance to the tower."
    n "Unsightly, dark decor with skulls lining the walls adds to the unsettling atmosphere."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Whoa, a creepy room right off the bat.  What're these skulls about?"
    hide yukino with qdis
    #update with Yuriko appearing
    show yuriko at pleft2 with qleft
    stu "Hi, everyone!  Welcome to good old Thanatos Tower! How're you all doing today?"
    stu "I'm your host, everyone's favorite idol, Yuriko Yamamoto!"
    hide yuriko with qdis
    show nanjo animated neutral serious with qleft
    na "What nonsense is this!?  Perhaps it's none of my business..."
    na "But isn't it a bit conceited to claim you're everyone's favorite idol?"
    hide nanjo with qdis
    show brown animatd neutral smirk with qleft
    br "Yeaaaaah!  Y!  U!  R!  I!  K!  O!  Yurikoooo! ...Uh, oh crap!  I got carried away... Who the heck are you!?"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Oh.  My.  God.  You look, like, SO dumb.  Who do you think you are, weirdo?"
    hide ayase with qdis
    show yuriko at pleft2 with qleft
    yuriko "Uh, hello?  Who's calling who a weirdo?  Ohh!  Are you jealous 'cause I'm so cutesy-wutesy?"
    yuriko "Ah man ...Being too pretty is a sin, isn't it?  Sorry 'bout that!  Ahahaha!"
    hide yuriko with qdis
    show elly animated neutral serious with qleft
    el "Er... so... why are you here?  Is it a battle you seek?  We'd have no objections to that."
    hide elly with qdis
    show yuriko at pleft2 with qleft
    yuriko "Awww, don't talk like that, guys!  I'm just here to tell you how to open the door back there."
    yuriko "So put your listening hats on!  Reaaaady?  Then here goes!  You see those two candles?"
    yuriko "One to the right of the door, one to the left?  Good!  All you have to do is blow one out, and poof!"
    yuriko "Door's open! Okey-dokey!  I hope you try 200% to get to me!  Bye-bye!"
    hide yuriko with qdis
    #update with Yuriko disappearing
    show yukino animated neutral serious with qleft
    yu "Well, uh... this is definitely a trap.  But that girl... Yuriko, right?"
    yu "I get the feeling she's tougher than she looks."
label label121a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQThanatos1
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "It's hard to describe how, but... this tower has an eerie feel to it."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I can't believe that girl!  What a loser!  What does she think life's all about?"
        ay "Who does she think she is!?  Oooooh, she's so aggravating!  Right?"
    elif _return == 3:
        show elly animated neutral sad with qleft
        el "What frightens me is that I can't tell what Yuriko is thinking... It seems as if she enjoyed this confrontation..."
        el "And this is certainly a trap.  It's as Yukino says... this won't be easy."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Psst!  Hey!  Yuriko's a cutie, huh?"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Good grief... Our hands are already full with Yuka's incessant yapping."
        na "And now we face a tower guardian exactly like her... I've got to get out of here."
    elif _return == 6:
        $ choicetext = "Which candle will you blow out?"
        show nchoice at pright zorder 15 with easeinright
        show nchoice onlayer screens zorder 15 at pright
        show fadeblack onlayer screens zorder 3 with dissolve
        $ choice1 = "Left"
        $ choice2 = "Right"
        call screen choices with dissolve
        if _return == 1:
            hide screen choices with dissolve
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with dissolve
            $ tbnarrator = 1
            n "You blow out the candle on the left, and as you do, you feel a deep clawing deep in your soul."
            n "Icy fingers grasp something within you and rip it forth, forcing you to a knee in agony as a grunt escapes your lips."
            $ tbnarrator = 0
            $ thanatospersona = 1
        else:
            hide screen choices with dissolve
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with dissolve
            $ tbnarrator = 1
            n "You blow out the candle on the right, and as you do, you hear Yukino cry out."
            $ tbnarrator = 0
            show yukino animated neutral sad with qleft
            yu "Huh!?  Wh-What's happening...?  S-Something's being yanked out of me... Aagh!  AAAAAAAHHHHHH!"
            hide yukino with qdis
            $ thanatospersona = 2
        #update with Yuriko reappearing
        show yuriko at pleft2 with qleft
        yuriko "Teeheehee!  Gotcha!  Teeheeheeheeheehee!  Did you really think you could get past here for free?  Silly billies!"
        yuriko "Tit for tat's the name of the game!  If you want anything in this tower, you gotta give something up in return!"
        yuriko "Life is hard, huh?  Well, I'll be taking your other life... Per-so-na! Thanks!  Teeheeheeheehee!  See ya!"
        hide yuriko with qdis
        #update with Yuriko disappearing
        show yukino animated neutral sad with qleft
        yu "Dammit!  What's up with that twit!?  What was that all about, anyway? 'I'll be taking your other life'?"
        yu "What did she mean?  "
        show yukino animated neutral serious
        extend "Damn that Yuriko!  She acts like an airhead, but she's a hardcore con artist!"
        hide yukino with qdis
        if thanatospersona == 1:
            $ tbnarrator = 1
            n "Your persona has been pulled from your soul, but you can feel it calling from somewhere."
            n "You lead the others forward further into the tower, determined to recover the power of your persona."
            $ tbnarrator = 0
            jump label122
        else:
            show yukino animated neutral sad with qleft
            yu "Hey... I think she did take my persona.  I can't feel Vesta anymore."
            show yukino animated neutral serious
            yu "But I think I can feel it.  Come on.  Let's go, Naoya."
            hide yukino with qdis
            $ tbnarrator = 1
            n "You nod and move with Yukino and the others into the tower."
            $ tbnarrator = 0
            jump label122
    jump label121a

label label122 (location = "Tartarus Entrance"):
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    if thanatospersona == 1:
        $ tbnarrator = 1
        n "While there are stairs that lead up, you can feel your Persona calling you from deep below you."
        n "The others follow, despite their own uncertainty, as you lead them to a large room with stairs leading underground."
        $ tbnarrator = 0
    else:
        $ tbnarrator = 1
        n "While there are stairs that lead up, Yukino leads the group elsewhere, feeling her Persona calling to her."
        n "The others follow, despite their own uncertainty, as you and she lead them to a large room with stairs leading underground."
        $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "What's this?  It looks different from the rest of the tower."
    hide yukino with qdis
    beast "HUMANS, WHY ARE YOU HERE?  BE AWARE THAT THIS IS THE ENTRANCE TO THE UNDERWORLD... AND I AM ITS GUARDIAN, CERBERUS."
    show nanjo animated neutral serious with qleft
    na "Don't stand in our way.  We won't hesitate to do away with you, beast!"
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "This animal's trying to stop me?  He does look strong, though... I know!  I'll strike up a little conversation."
    br "Umm... 'ME MAD.  YOU MOVE.'"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Look, we don't wanna fight you, okay?  We just wanna see what's through there.  Pretty please?"
    hide ayase with qdis
    cerberus "BEYOND HERE IS THE LAND OF THE DEAD, WHERE DECEASED SOULS GATHER.  I DOUBT YOU HAVE ANY BUSINESS THERE."
    show nanjo animated neutral serious with qleft
    na "The land of the dead, eh?  Mmm... Interesting.  With demons running rampant, this tower itself is much like Hell already."
    na "There is nothing left for us to fear."
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "Ahaha... The key to the mystery of our lost Persona power may be here. When Yuriko said, 'I'll take your other life'..."
    el "What she meant was that that she'd taken away the Persona.  Taking life means death, after all."
    el "And this is apparently where the souls of the deceased gather... Where else could our missing 'other soul' be?"
    el "Excuse me, Cerberus?  Am I correct in thinking you've been set here by Yuriko to keep us out?  You must let us through!  Or else..."
    hide elly with qdis
    cerberus "VERY PERCEPTIVE.  YOUR DEDUCTIONS ARE LARGELY CORRECT.  YES, YOUR SO-CALLED 'PERSONA' IS HERE."
    cerberus "BUT I HAVE NO DEALINGS WITH YURIKO.  I GUARD THIS PLACE OF MY OWN WILL."
    cerberus "THE LAND OF THE DEAD NEEDS NO INCOMPLETE SOULS. TAKE WHAT IS YOURS."
    show yukino animated neutral smirk with qleft
    yu "Sounds good.  Then we'll be on our way.  No need to bother you."
label label122a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus1
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "The land of the dead, huh?  Never thought I'd go there while I was still alive."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "Oooooh, the afterlife!  Freaky!"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "Wow!  I get to visit the underworld while I'm still alive!  I'm the luckiest girl on Earth!"
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Whoa, the land of the dead!  Cooool!  Maybe we can get on TV after all this!"
        "'A Student in the Afterlife', starring Hidehiko Uesugi!  Mwahahahaha!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "I'd prefer to avoid it, but I suppose I have business there at the moment."
    elif _return == 6:
        $ tbnarrator = 1
        n "With the door down into Tartarus in front of you, the six of you steel yourselves and begin to head down into its depths."
        $ tbnarrator = 0
        jump label123
    elif _return == 7:
        cerberus "THE DEMONS OF TARTARUS ARE STRONGER THAN THOSE OF THE TOWER.  THEIR HATRED OF LIVING IS FIERCE.  BE CAREFUL."
    jump label122a

label label123 (location = "Tartarus"):
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    if thanatospersona == 1:
        $ tbnarrator = 1
        n "The demons down here are certainly fierce, but you lead the others to a room along the path."
        n "Within, your persona waits, and as you approach, it moves to you, like a mirror.  A warmth washes over you."
        n "You have regained your Persona!"
        $ tbnarrator = 0
    else:
        $ tbnarrator = 1
        n "The demons down here are certainly fierce, but Yukino leads you and the others to a room along the path."
        n "Within, herr persona waits, and as she approaches, it moves to her, like a mirror."
        $ tbnarrator = 0
        show yukino animated neutral smirk with qleft
        yu "All right!  Vesta and I are back in business!"
label label123a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus2
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Seeing my own Persona like this drives home how mysterious a Persona really is."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I thought this place would be, like, way scarier, but this isn't so bad."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "This place is very different from our common perception of the underworld."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "If I die, I'm going straight to heaven for sure!  So this is the last time I'm gonna be seeing the underworld!  Yep."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "The world that's home to the souls of the deceased..."
        na "It's certainly not a comfortable place to be, but it has a certain solemn air.  It puts me in a contemplative mood."
    elif _return == 6:
        $ tbnarrator = 1
        n "With the Persona recovered, you are ready to head back up to deal with Yuriko, but Nanjo hesitates a bit."
        n "He suggests looking further through Tartarus to ensure no Mirror Shards are missed."
        n "The logic is sound, but you can't help but to wonder if there's an ulterior motive as you continue."
        $ tbnarrator = 0
        jump label124
    elif _return == 7:
        mariko "This'll knock your socks off... Sometimes these images appear on the walls here, and they look like you guys!"
        mariko "I took a few snaps.  I'll give you a print once the film's developed!"
        mariko "Not many people have photos of their own ghosts!"
    jump label123a

label label124:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Everyone seems on-edge, but Nanjo's request keeps everyone focused, although entering into another room proves interesting."
    n "The floor has several chest-like objects, and opening them reveals several items, including a Mirror Shard."
    $ tbnarrator = 0
label label124a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus3
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "There's no end to this.  The clock's ticking.  If we don't stop this at some point, we might be in trouble."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Just being around treasure boxes makes me, like, totally happy!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Please do keep our time limitations in mind."
    elif _return == 4:
        show brown animated neutral smirk with qleft
        br "Treasure boxes!  What could be greater!?  Man!  Treasure boxes!"
        br "Everyone knows what they are, but how many have actually touched a real one!?"
    elif _return == 5:
        show nanjo animated neutral smirk with qleft
        na "After so many battles together, I have a higher opinion of you.  You're strong."
        show nanjo animated neutral serious
        na "Anyway... I'm only putting out feelers, but once we defeat the Snow Queen..."
        na "Would you mind coming along to rescue Masao?  More manpower can hardly hurt."
        na "I won't force you... just consider it."
    elif _return == 6:
        $ tbnarrator = 1
        n "While a shard has been found, Nanjo seems intent on looking further."
        n "Yukino and Elly are worried about the time, but Ayase and Brown are happily along to look for more chests."
        $ tbnarrator = 0
        jump label125
    jump label124a

label label125:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Despite the dangers, Mariko seems to have gotten ahead of you, and has already looked through some of the contents of the room."
    n "She seems to be unharmed, so far, but danger lurks around every corner, down here."
    $ tbnarrator = 0
label label125a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus4
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "That Mariko girl's a real weirdo.  Same goes for Tsutomu.  I just don't get these guys who're into the occult."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Her pink uniform's cute, huh?"
    elif _return == 3:
        show elly animated neutral sad with qleft
        el "She may be even more of a danger to herself than Tsutomu..."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Maybe I should explore this tower with Mariko..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "That Mariko... She certainly is enjoying this situation."
    elif _return == 6:
        $ tbnarrator = 1
        n "A second shard down, and yet Nanjo insists on checking further within the depths."
        n "He seems to also want to find equipment to use against Yuriko, a logic no one can find fault with."
        $ tbnarrator = 0
        jump label126
    elif _return == 7:
        if marikoshard == False:
            mariko "Huh?  You wanna know if anything used to be in that chest over there? Yeah, sure!  This broken mirror piece!"
            mariko "I can feel strong spiritual energy in it.  It's gotta be some kinda powerful supernatural object.  Huh?"
            mariko "You want it...?  Hmmmm... How 'bout this?  I'll sell it for 5,000 yen!"
            mariko "I found it first, after all... It's not such a bad price, is it?"
            hide screen header with dissolve
            $ choicetext = "Buy it?"
            show nchoice at pright zorder 15 with easeinright
            show nchoice onlayer screens zorder 15 at pright
            show fadeblack onlayer screens zorder 3 with dissolve
            $ choice1 = "Buy Mirror Shard"
            $ choice2 = "Don't Buy Mirror Shard"
            call screen choices with dissolve
            if _return == 1:
                hide screen choices with dissolve
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with dissolve
                show screen header with dissolve
                mariko "Thanks!  I've been taking roll after roll of pics here, so I'm nearly out of film.  Now I can buy some more!"
                $ tbnarrator = 1
                n "Obtained a Mirror Shard!"
                $ tbnarrator = 0
                $ marikoshard = True
            else:
                hide screen choices with dissolve
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with dissolve
                show screen header with dissolve
                mariko "Oh, so you don't want it?  That's cool.  I'll just send it to the Atlantis News and have 'em appraise it!"
        elif marikoshard == True:
            mariko "Thanks!  I've been taking roll after roll of pics here, so I'm nearly out of film.  Now I can buy some more!"
    jump label125a


label label126:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The winding paths of Tartarus take you further within, heading deeper into the dungeon."
    n "A look at Nanjo shows him giving appraising glances this way and that, and it seems he's looking for...something."
    $ tbnarrator = 0
label label126a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus5
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "It sounds strange saying this in the world after death, but..."
        show yukino animated neutral sad
        yu "I hope we all make it back alive."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Hey, hey, some of these treasure boxes might have mirror shards in them."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Checking every single treasure box may strain our time limitations."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Cerberus was right... this Tartarus place sure is exhausting..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "The enemies here are strong.  If we don't equip ourselves well, we won't have a prayer against Yuriko."
    elif _return == 6:
        $ tbnarrator = 1
        n "Despite Brown's exhaustion, the others convince him to move onward as you've already found some mirror shards here."
        n "Nanjo is conspicuously quiet, and Yukino seems to have taken note of it as well."
        $ tbnarrator = 0
        jump label127
    jump label126a

label label127:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The deeper you go into Tartarus, the more it becomes apparent that Nanjo hasn't come across what he's looking for."
    n "Whether that's good or not, you aren't certain."
    $ tbnarrator = 0
label label127a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus6
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "I wonder if this Tartarus is Yuriko's treasure hoard.  There sure are a lot of boxes here."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Hey, if we beat the Snow Queen and rescue Ms. Saeko... that's it, right?"
        ay "Everyone will go back to normal, and we can, like, go home, right?"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "Haha... it's really rather amusing.  We give never knew each other well, yet here we are on an adventure together..."
        el "And not only that... part of me takes a real delight in this situation.  It really is amazing..."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Ughhhh!  This is supposedly the world after death, but there's nothing here.  Boooooriiiiiing!"
        show brown animated neutral smirk
        br "Hey!  Let's start heading back up the tower and go see Yuriko!"
    elif _return == 5:
        show nanjo animated neutral sad with qleft
        na "I'm worried about Ms. Saeko, of course, but that Masao... I wonder if he's all right.  He isn't very smart, after all."
        show nanjo animated neutral serious
        na "Damn and blast!"
    elif _return == 6:
        $ tbnarrator = 1
        n "You are nearing the end of Tartarus, and yet you all press on to its very end."
        n "Nanjo is even more subdued, and offers little in explanation to the others when asked what he's seeking."
        $ tbnarrator = 0
        jump label127
    jump label127a

label label128:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Yet another room appears before you, and yet it seems there is very little remaining to search."
    n "Nanjo, and by extension the rest of you, are steadily growing more on edge as you near the end."
    $ tbnarrator = 0
label label128a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus7
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Even now, our time keeps slipping away.  It's frustrating."
        show yukino animated neutral sad
        yu "Makes me think I might be powerless after all."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "It's kinda nice, having everyone work together toward something like this."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Thanatos Tower and Tartarus... It's all like something from Greek mythology."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "It sucks that this happened to our school, no doubt about that..."
        show brown animated neutral smirk
        br "But then again, it's a break from our boring everyday lives!  That's kinda cool!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "It's always so unsightly to witness one rummaging through treasure boxes."
        show nanjo animated neutral sad
        na "Oh, no, I didn't mean you in particular.  Just... in the general sense.  "
        show nanjo animatd neutral serious
        extend "Yes."
    elif _return == 6:
        $ tbnarrator = 1
        n "Brown and Ayase lag behind a bit, but Nanjo and Yukino encourage them onward."
        n "Despite the time uncertainty, Elly also is enjoying seeing just what there is to see down here."
        $ tbnarrator = 0
        jump label129
    jump label128a

label label129:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Entering into the last room, Nanjo lets out a quiet breath.  Both relief and sadness wash over his features."
    $ tbnarrator = 0
label label129a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQTartarus8
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "So mirror shards can be in treasure boxes, too!"
        yu "Let's try and check as many treasure boxes as we can, time permitting."
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "I always get goosebumps when we're about to open up a treasure box!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "I admit, my opinion of you has slightly improved.  You haven't uttered a word of complaint, even in a situation like this..."
        el "You've been a real unifying force.  "
        show elly animated neutral smirk
        extend "I never knew you had such a brave heart."
    elif _return == 4:
        show brown animated neutral serious with qleft
        br "Hey, to tell you the truth, you're so quiet, I always thought you were weird..."
        br "But after fighting along with you, I get it now!"
        show brown animated neutral smirk
        br "You're one hip, happenin' dude!  You're like, the next strongest and second most reliable, after me!"
        br "I gotta give you props!  Seriously."
    elif _return == 5:
        show nanjo animated neutral sad with qleft
        na "I am of mixed emotion.  I had hoped to see Yamaoka, here."
        na "Though I would not wish him to be confined to Tartarus, and not finding him here means he has gone onto heaven."
        show nanjo animated neutral serious
        na "Good.  I feel as if a weight has been lifted from my shoulders."
    elif _return == 6:
        $ tbnarrator = 1
        n "With Nanjo now seeming at ease, and with the entirety of Tartarus now explored, you return back to climb the tower."
        n "Three more mirror shards are in hand from the exploration, and now you move to deal with Yuriko."
        $ tbnarrator = 0
        jump label130
    jump label129a

label label130:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The climb up the tower was perilous, and in-turn, each of you had lost a fight."
    n "Rather than the loss of your life, it was the loss of your persona that had taken place, forcing you to return to Tartarus."
    n "Eventually, the six of you reach the fourth floor landing, confidence shaken."
    $ tbnarrator = 0
label label130a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQThanatos2
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "I hope Ms. Saeko's okay...  "
        show yukino animatd neutral serious
        extend "Dammit... We need to hurry this up."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "This totally sucks!  What am I gonna do without a Persona!?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "It seems that if you transgress in some way while in this tower..."
        el "There is a rule that you will pay with your 'life.'"
        show elly animated neutral sad
        el "But in our case, it seems we'll lose our Personas instead of our lives."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Damn!  Fighting without a Persona?  This tower has really strong monsters in it, too!  This is no joke!"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "We never previously realized the existence of Personas..."
        na "But I now realize how taxing it can be when one suddenly loses it."
    elif _return == 6:
        $ tbnarrator = 1
        n "The demons are very dangerous, but knowing that your persona's life is on the line, you cover one another on the way up."
        n "Teamwork becomes key, and your group grows stronger as a result as you climb up the Thanatos Tower."
        $ tbnarrator = 0
        jump label131
    jump label130a

label label131:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The quiet of the climb is occasionally broken by Eriko inquiring about the Eternal Night."
    n "Yukino and Nanjo seem focused on the goal of Yuriko, but Brown and Ayase indulge her in conversation."
    $ tbnarrator = 0
label label131a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQThanatos3
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "Not that it matters, but the treasure boxes in this tower are shaped funny."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "I'm hungry... Do any of these treasure boxes have, like, food in 'em?"
    elif _return == 3:
        show elly animated neutral sad with qleft
        el "Eternal Night... What would that world be like?  Despite my curiosity, I dread it..."
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Even if we had more time, it still wouldn't be enough.  This 'Eternal Night' thingy could happen any second... What a drag."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Supplies are only meaningful if you put them to use."
        na "We must take care to ensure that they don't end up being useless."
    elif _return == 6:
        $ tbnarrator = 1
        n "The steps continue upward and while the demons grow more and more dangerous, you and your team manage to stay safe."
        n "But the next floor ends at a large, ornate door.  As you all step inside, there are two treasure chests in the back."
        $ tbnarrator = 0
        jump label132
    jump label131a

label label132:
    scene bg black #update with frozen Thanatos tower entrance
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The situation with the chests seems like a trap, and no one is willing to move forward to check on them."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "This is a trap if I ever saw one.  Two chests in the back, and nothing else."
    yu "It's bad news, like that room with the candles.  You know how they say to let sleeping dogs lie?"
    yu "We should leave these be."
    hide yukino with qdis
    #update with Yuriko appearing
    show yuriko at pleft2 with qleft
    yuriko "Awww, you big meanie.  I put together a present just 'cause you guys were trying soooo hard."
    yuriko "And you're gonna walk away just like that?  I'm gonna cry... *sniffle*..."
    hide yuriko with qdis
    show nanjo animated neutral serious with qleft
    na "Hmph, as if we'd fall for that."
    hide nanjo with qdis
    show brown animated neutral smirk with qleft
    br "A present!?  L-Let's take it, Yukino!  No one that pretty can be a crook.  True fact!"
    br "C'mon, we can trust Yuriko!"
    hide brown with qdis
    show ayase animated neutral serious with qleft
    ay "Huh.  Sure, it looks like a trap, but it sounds kinda fun!  I don't wanna chicken out..."
    show ayase animated neutral smirk
    ay "Okay, go ahead and tell us what's up!"
    hide ayase with qdis
    show yuriko at pleft2 with qleft
    yuriko "Woo-hoo!  I knew you'd get it!  I think you and me could be best friends forever!  Oh, I'm so happy!"
    hide yuriko with qdis
    show elly animated neutral serious with qleft
    el "I'm sure you're up to no good with this so-called 'gift.'  It's a waste of time."
    hide elly with qdis
    show nanjo animated neutral serious with qleft
    na "Indeed. Stop blathering and get to the point.  Your mannerisms give me a migraine."
    hide nanjo with qdis
    show yuriko at pleft2 with qleft
    yuriko "Awww, why can't you be more positive?  I know you're all thrilled!  Oh well, I'll go ahead and explain the gift!"
    yuriko "Put your listening hats on!  One of these two chests has a Mirror Shard!  We all like those, don't we?"
    yuriko "And I'm feeling super-duper-generous today, so you can try your luck for free!  But! You only get one try!"
    yuriko "And of course, something bad will happen if you open the wrong one.  Uh-oh!"
    yuriko "Whee!  Sounds fun, huh?  Good luck!  Teeheeheehee!"
    hide yuriko with qdis
    #update with yuriko vanishing
    show ayase animated neutral serious with qleft
    ay "Oh, so it IS a trap?  Hmm... well, it's a good chance anyways!  We should like, give it a shot!"
    ay "I have a feeling she's not lying.  C'mon, it's not big deal, right?"
    show ayase animated neutral smirk
    ay "I take full responsibility if anything happens!  So let's crack one open!"
    hide ayase with qdis
label label132a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQThanatos4
    if _return == 1:
        show yukino animated neutral serious with qdis
        yu "Yuriko's toying with our lives and loving every minute of it! *sigh*"
        yu "I hate her frickin' guts."
    elif _return == 2:
        show ayase animated neutral sad with qdis
        ay "I dunno why, but it seems like Yuriko is forcing herself to be like this."
        show ayase animated neutral serious
        ay "That's just how it feels to me."
    elif _return == 3:
        show elly animated neutral serious with qdis
        el "These traps in the tower... It's all a game to her.  Each time we make progress, she torments us just enough so as not to kill anyone."
        el "She's even prepared a gift to entice us.  Everything's been meticulously planned so that she can kill us herself at the endgame."
    elif _return == 4:
        show brown animated neutral sad with qdis
        br "Man, the traps here are evil!  This tower's packed with danger for an honest joe like me!"
        show brown animated neutral serious
        br "No, seriously."
    elif _return == 5:
        $ tbnarrator = 1
        n "You need to pick a chest to proceed.  Which one will you open?"
        $ tbnarrator = 0
        $ choicetext = "Which chest will you open?"
        show nchoice at pright zorder 15 with easeinright
        show nchoice onlayer screens zorder 15 at pright
        show fadeblack onlayer screens zorder 3 with dissolve
        $ choice1 = "Left"
        $ choice2 = "Right"
        call screen choices with dissolve
        if _return == 1:
            hide screen choices with dissolve
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with dissolve
            show ayase animated neutral sad with qleft
            ay "Yeeeeek!  S-Something's coming out of me!"
            hide ayase with qdis
            yuriko "Teeheeheehee!  Too bad!  I'm taking your other self as a forfeit!  Okey-dokey!  Bye-bye!"
            show ayase animated neutral serious with qleft
            ay "Gaaah!  I can't believe that little sneak!  Argh... I can't use my Persona anymore!  What am I gonna do!?"
            ay "Gahhh!  That Yuriko is such a backstabber!  I'm like, SO pissed right now!"
            hide ayase with qdis
            $ thanatospersona = 3
        else:
            hide screen choices with dissolve
            hide fadeblack onlayer screens
            hide nchoice onlayer screens
            hide nchoice
            with dissolve
            show ayase animated neutral smirk with qleft
            ay "Bingo!  We got the right one!  This rules!  See?  I toldja we should open a chest!  Am I right or am I right?"
            hide ayase with qdis
            yuriko "Huh... Looks like Lady Luck's on your side.  Okey-dokey!  You win this game!  Congrats!"
            yuriko "It's just a little further to my room, so don't give up now, 'kay?"
            yuriko "I'll give each of you the bestest death ever!  I'll be waiting!"
            $ tbnarrator = 1
            n "Obtained a Mirror Shard."
            $ tbnarrator = 0
            $ thanatospersona = 4
        if thanatospersona == 3:
            $ tbnarrator = 1
            n "Your group decides that trying to take on Yuriko while Ayase doesn't have her persona available is not a good plan."
            n "Despite the complaints from Brown, the six of you make the trek all the way back down the tower to Tartarus once more."
            n "The demons are still dangerous but you protect Ayase on the way down, and restore her persona."
            n "Unwilling to take a break due to the time limit, Yukino spurs everyone onward back up the stairs, knowing Yuriko will be close."
            $ tbnarrator = 0
        elif thanatospersona == 4:
            $ tbnarrator = 1
            n "With another Mirror Shard in your possession, you ready yourselves for the final trek to deal with Yuriko."
            n "Everyone is exhausted, but with the end in sight, you all push onward to the final floor to confront the tower's master."
            $ tbnarrator = 0
        jump label133
    jump label132a

label label133:
    scene bg black #update with frozen Thanatos Yuriko Room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The room belonging to Yuriko doesn't match her bright demeanor, being dismal and dark."
    n "Still, the lingering scent and presence of death covers every inch of the top of the Thanatos tower."
    $ tbnarrator = 0
    show yukino animated neutral serious
    yu "Looks like we've reached Yuriko's room.  But this isn't what I was expecting from her cutesy attitude..."
    yu "Hey, Yuriko!  You know we're here, right?  Hurry up and come on out!  Or are you up to something again?"
    hide yukino with qdis
    #update with Yuriko appearing
    show yuriko at pleft2 with qleft
    yuriko "Geez Louise!  You don't have to wake the dead, y'know!  I can hear you just fine!  Anyway..."
    yuriko "You have a really nice face!  How 'bout you die here? That way you can keep your looks forever!"
    yuriko "If you keep on living, you'll get older and end up all wrinkly and ugly!"
    yuriko "So c'mon, why not die right now, when you're most beautiful, like I did?"
    yuriko "Then we can live in this tower together, looking gorgeous!  Does that sound great or what?  C'mon, we totally should!"
    yuriko "It'll be soooo much fun!  I'm super glad I came to this tower, like the Snow Queen's mask said!"
    yuriko "I'll stay young and pretty forever and ever!  But I was getting a little bored, being here all by my lonesome."
    yuriko "And I don't wanna fight you guys, so... Whaddya say?"
    hide yuriko with qdis
    show nanjo animated neutral serious with qleft
    na "Do you understand the substance of what you're saying?  What you obtained through death and the power of the mask..."
    hide nanjo with qdis
    show brown animated neutral seriou with qleft
    br "Yuriko... what're you saying?  The Snow Queen's mask killed you and now you're the guardian of this tower, huh?"
    br "Well, if you're dead now, I guess you won't get any older, but... That's not worth throwing away our lives, our futures, in the real world."
    br "Sorry, but I'm gonna have to pass on this 'eternal beauty' gig!"
    hide brown with qdis
    show nanjo animated neutral serious with qleft
    na "Well said.  The choice you made is merely the end of your existence, the real world without you..."
    na "Absolute, unending solitude within this tower.  This is not the eternal beauty you wished for!"
    hide nanjo with qdis
    #update with Yuriko appearing in front of Ayase
    show yuriko at pleft2 with qleft
    yuriko "Sh-Shut up!  You guys just don't understand how it is to be a girl! H-How about you?"
    yuriko "You're totally the cutest one of the bunch.  You get what I'm saying, right?"
    yuriko "You can have eternal beauty, right here!  We'll stay pretty... and..."
    hide yuriko with qdis
    show ayase animated neutral serious with qleft
    ay "Not one more word!  Don't think for a second that you and me are the same type!  You really, and I mean REALLY, piss me off!"
    ay "I would never die just to stay pretty!  You know what?  You gave up on dying!  And growing older!"
    ay "And living your life like a normal person! You gave up on everything you had!"
    ay "Yeah, you heard me!  You're a loser who threw away all her responsibilities!"
    hide ayase with qdis
    show elly animated neutral smirk with qleft
    el "Spot on! That was so cool!  I couldn't have said it better myself, Ayase!  You blew me away!"
    show elly animated neutral serious
    el "Now then, Yuriko... Since you've been rejected by Ayase, the one who could identify with you most..."
    el "I doubt anyone else here would have time for you!  What will you do now?"
    hide elly with qdis
    #update with Yuriko teleporting away from the group
    show yuriko at pleft2 with qleft
    yuriko "But... I... I was only trying to help you guys out!  I just wanted to have some laughs with everyone!"
    yuriko "What about that don't you get!?  That's it! No more Ms. Nice Yuriko!  You have no idea how strong I am!"
    yuriko "Beg for your life if you want--I won't listen!  I'll crush you so hard there'll be nothing left!"
    yuriko "Not even your soul!"
    hide yuriko with qdis
    show yukino animated neutral smirk with qleft
    yu "Heh... As Kei would probably say, 'Only death can cure a fool!'  Too bad death doesn't seem to have helped in your case!"
    show yukino animated neutral serious
    yu "Come on, then!  We'll kill all the stupid out of you!  Here we go!"
    hide yukino with qdis
    scene bg black #update with frozen Thanatos Battle
    #play music library fadeout 0.5 fadein 0.5 #update
    thanatos "Transformation complete!  Here comes Yuriko!  All righty, time to beat everyone up.  Hope you're ready!"
    show ayase animated neutral smirk with qleft
    ay "Pbbbbt!  You're uglier than death warmed over!"
    hide ayase with qdis
    thanatos "Excuse me!?  Oh, I have HAD it!  I'm SO not forgiving you for that!"
    show ayase animated neutral serious with qleft
    ay "Urgh... she's not the only one who's had it...!"
    hide ayase with qdis
    $ tbnarrator = 1
    n "Despite her words, Yuriko seems to be almost holding back during the fight as you and your allies overpower her."
    n "Ayase is clearly motivated and frustrated, leading the attack as Yuriko is steadily defeated."
    $ tbnarrator = 0
    scene bg black #update with frozen Thanatos Yuriko Room
    #play music library fadeout 0.5 fadein 0.5 #update
    show yukino animated neutral serious with qleft
    yu "It's the end of the line for you, Yuriko!  Be a good girl and accept it."
    yu "Or are you gonna go cry to the nice Snow Queen who gave you eternal beauty?  What's it gonna be, huh!?"
    hide yukino with qdis
    show yuriko at pleft2 with qleft
    yuriko "......I... I don't... I don't like the Snow Queen... I really don't."
    yuriko "I'm glad... it ended like this... I had fun with you guys.  I got to talk to you... have a nice battle..."
    yuriko "And now... I got beaten... It's a good thing. That's right... I'm... human.  And humans have to die..."
    yuriko "I was so stupid... Why didn't I understand something so easy...?"
    show nanjo animated neutral serious with qleft
    na "What?  Are you crying...?  Hmph.  Stop your charade.  What's your scheme this time?"
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "I admit I've got a soft spot for a cute girl in tears, but I know you're faking.  You've gotta be up to no good again."
    br "Well, it's not gonna work this time!  Sure, maybe you coulda fooled someone else... But not me!  Nnnnope!"
    br "I mean, you were all about the Snow Queen, and now you're saying you don't like her?  Hah!"
    hide brown with qdis
    show nanjo animated neutral serious with qleft
    na "Did you think you could fool us that easily?  I've had enough of your mockery."
    hide nanjo with qdis
    show ayase animated neutral serious with qleft
    ay "You idiot!  She's crying for reals!  Can't you tell?  Ugh, no wonder you still don't have a girlfriend!"
    ay "You don't understand girls at all!  And c'mon, Yukino, don't be so hard on her!  Give her a chance."
    ay "I don't think she's all that bad.  I... I can't explain it, but..."
    hide ayase with qdis
    show yuriko at pleft2 with qleft
    yuriko "...Thank you.  You're... Ayase, right?  I wish we'd met and become friends... while I was still alive."
    yuriko "To tell you the truth... I was scared. I used to hang out with my friends, and we'd go out and have fun..."
    yuriko "I had a lot of friends and a lot of guys who said they liked me.  Plus, my mom and dad were really sweet."
    yuriko "Every day was fun, and I was so happy... I thought, 'It just doesn't get better than this!'"
    yuriko "But then... I got scared..."
    yuriko "If it doesn't get better than this... Is it all downhill from here?"
    yuriko "For the rest of my life... Will I ever be happier than I am now?  Am I just gonna grow up, get old, turn ugly... and die...?"
    yuriko "I couldn't shake those questions.  I got so scared, I couldn't sleep at night..."
    yuriko "That's when the Snow Queen's mask I wore in the play spoke to me."
    yuriko "It said, 'I can help you live forever, exactly as you are now.'"
    yuriko "Before I knew it, I was in this tower... And I've been here ever since... all by myself..."
    yuriko "Mom... Dad... My friends... All gone.  Just me... I was so selfish!  I was stupid for not wanting to die or grow old!"
    yuriko "Every human has to!  That's why I fell for the Snow Queen's offer... I was such an idiot! I felt empty, being on my own for so long...!"
    yuriko "I wanted to just end it all! I couldn't stand it anymore!"
    yuriko "That's why... when you guys showed up... I was really happy!  I'd finally be able to put an end to this..."
    yuriko "...one way or another... I wouldn't have to be alone anymore!  That's why I... I...!"
    hide yuriko with qdis
    show elly animated neutral sad with qleft
    el "So that overhwelming power that seemed almost unnatural... It came from your unfathomable sadness..."
    el "The utter loneliness and bottomless grief you felt... That gave rise to despair far stronger than any of your prior feelings."
    show elly animated neutral serious
    el "Combined with your sadness, that was the root of both your peculiar attitude and the frightening power of your Persona, Thanatos."
    show elly animated neutral sad
    el "I see now, Yuriko, that you too were a victim of the Snow Queen."
    hide elly with qdis
    show yuriko at pleft2 with qleft
    yuriko "But it's finally over... I can't thank you enough.  Thanks to all of you... I can die... feeling like a human..."
    yuriko "I... I have to go now... Thank you so much.  Goodbye..."
    hide yuriko with qdis
    #update with Yuriko disappearing
    $ tbnarrator = 1
    n "Obtained a Mirror Shard."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Damn you, Snow Queen... I'll make you pay for toying with people's lives!"
    yu "Yuriko... We're doing this for you now, too!  So don't worry... rest well..."
    hide yukino with qdis
    $ tbnarrator = 1
    n "You have conquered Thanatos Tower!"
    $ tbnarrator = 0
    $ plotprogress = 13
    jump label088

label label134 (location = "Spare Room"):
    scene bg black #update with room with orb
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As you and your allies enter into the room, all of your attention is drawn to the glowing orb in the center of it."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "What's this..?"
    hide yukino with qdis
    show ayase animated neutral smirk with qleft
    ay "It's like, so pretty..."
    hide ayase with qdis
    show elly animated neutral serious with qleft
    el "Could it be plasma?"
    hide elly with qdis
    show brown animated neutral serious with qleft
    br "It feels like if I keep starting at it, I'll get sucked inside."
    hide brown with qdis
    show nanjo animated neutral serious with qleft
    na "Watch yourself.  They say that every rose has its thorn."
    hide nanjo with qdis
    $ tbnarrator = 1
    n "Despite the concerns and worry, you find yourself drawn to the orb."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "Naoya!  Be careful!"
    hide yukino with qdis
    $ tbnarrator = 1
    n "Seemingly drawn in by something you can't understand, you lift a hand up to touch the sphere."
    $ tbnarrator = 0
    show ayase animated neutral serious with qleft
    ay "Hey! What did you do, Naoya?"
    hide ayase with qdis
    show yukino animated neutral serious with qleft
    yu "Woah!"
    hide yukino with qdis
    $ tbnarrator = 1
    n "The ball, as if it were a tiny star, pulls everyone within, and a blinding white light overcomes your vision."
    n "When it fades, you are in a similar, though different, room."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "What just happened?"
    hide yukino with qdis
    show elly animated neutral serious with qleft
    el "Has anything changed?  Let's have a look outside this room!"
    hide elly with qdis
    show ayase animated neutral sad with qleft
    ay "Huh?  I feel like we're missing someone..."
    hide ayase with qdis
    show brown animated neutral serious with qleft
    br "Huhhh!?  What was that?"
    hide brown with qdis
    show nanjo animated neutral serious with qleft
    na "Is everyone all right?"
    hide nanjo with qdis
    show yukino animated neutral serious with qleft
    yu "I say we go with Elly's idea.  Let's take it slow and be careful- we don't know what's out there."
    hide yukino with qdis
label label134a:
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQCastle1
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "Are we going through it again?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "It's glowing, but it's cold."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Could this be something like a wormhole?"
    elif _return == 4:
        show brown animated neutral sad with qleft
        br "Staring at it hurts my eyes..."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "It seems that we can be teleported elsewhere by touching this."
    elif _return == 6:
        $ tbnarrator = 1
        n "You and the others leave the room, heading outside to see what lays beyond."
        $ tbnarrator = 0
        jump label135
    jump label134a

label label135 (location = "Boxing Club"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "You find that you're still somehow within the school, but something seems off as you traverse it."
    $ tbnarrator = 0
    scene bg black #update with frozen boxing club
    call screen SQCastle2
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "These guys again..."
    elif _return == 2:
        show ayase aniamted neutral smirk with qleft
        ay "It's nice they get along so well."
    elif _return == 3:
        reiho "Jab!  Jab!  Hee-ho!"
        raiho "There's no sumo club hee-here, so we're gonna join the boxing club, ho."
        reiho "Hey!  A sandbag can't move like that!"
        raiho "Hee-ho?  Are you talking about me?"
        reiho "Don't you hee-member?  How the boy at the fencing club was beaten up by a girl?"
        raiho "Hee-ho!  I see... so girls are strong, ho.  ...Please... Be gentle... okay?  Hee-ho!"
    elif _return == 4:
        show elly animated neutral serious with qleft
        el "I wonder if Jack Frosts actually have distinct genders."
    elif _return == 6:
        show brown animated neutral smirk with qleft
        br "Watching them really warms my heart."
    elif _return == 5:
        show nanjo animated neutral smirk with qleft
        na "They always act as though they're in the middle of a stand-up routine."
    elif _return == 7:
        $ tbnarrator = 1
        n "Leaving the Jack Frosts behind, you and the others look to explore the rest of the eerie frozen school."
        $ tbnarrator = 0
        jump label136
    jump label135

label label136 (location = "Ballet Club"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "You seem to be in the Club Room area as you move next into the Ballet Club room."
    n "Inside are several students, frozen solid."
    $ tbnarrator = 0
    scene bg black #update with frozen ballet club
    call screen SQCastle3
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "I'd wondered where some of the students had gone.  Now I've got my answer..."
        show yukino animated neutral serious
        yu "Just wait for us, guys.  We'll rescue you all soon!"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "How awful... Who does stuff like this for fun?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "They appear to still be alive."
        show elly animated neutral sad
        el "Eternal Night... so this is what it means."
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "Mm.  It seems the enemy is resorting to force now."
    elif _return == 5:
        show brown animated neutral sad with qleft
        br "Oh crap... oh crap...!"
    elif _return == 6:
        $ tbnarrator = 1
        n "With a heavy heart, you leave the frozen students and wander further into what was once your school."
        n "Demons run amok and they seem to grow stronger with each passing step, but you continue on to put an end to this."
        $ tbnarrator = 0
        jump label137
    jump label136

label label137 (location = "3F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Eventually you find stairs up, and climb higher into the school.  An empty classroom serves as a temporary safe room."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle4
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Any wounds, Naoya?"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "My hands are going numb."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Both the demons and the building's structure are becoming more formidable."
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "How on earth is this building laid out?"
        show nanjo animated neutral sad
        na "It's hard to believe it was once our school..."
    elif _return == 5:
        show brown animated neutral serious with qleft
        br "Whew, let's take a breather.  I feel like my legs are gonna fall off."
    elif _return == 6:
        $ tbnarrator = 1
        n "After a brief rest, you and the others continue your trek through the frozen school."
        $ tbnarrator = 0
        jump label138
    jump label137

label label138 (location = "3F Warehouse"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Coming into another room, you find more students frozen solid, and a rush of indignant anger moves through your group."
    $ tbnarrator = 0
    show elly animated neutral sad with qleft
    el "Good heavens... here, too...?"
    hide elly with qdis
    show brown animated neutral serious with qleft
    br "Dammit!  Night Queen or no, I'm not letting whoever did this off the hook!"
    hide brown with qdis
    show yukino animated neutral serious with qleft
    yu "This girl looks like she wants to say something..."
    hide yukino with qdis
    show ayase animated neutral serious with qleft
    ay "Y'think they'd melt if I cast Agi on 'em?"
    hide ayase with qdis
    show nanjo animated neutral serious with qleft
    na "'Set your mind at ease that even the fire may seem cool and refreshing.'"
    show nanjo animated neutral sad
    na "Wait... That makes it feel even colder."
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "Hunh?  H-Hey!  Look... There's something on the floor.  I-I-Is it a 10,000-yen bill?"
    br "'Cause if it is, dibs!  Dibs, you hear me!?  I saw it first!"
    hide brown with qdis
    show yukino animated neutral serious with qleft
    yu "Do you ever stop being such a greedy bastard!?"
    hide yukino with qdis
    show brown animated neutral serious with qleft
    br "Oh, Yukino, please.  I would never steal money like that.  In fact, I'll offer it to you.  No, no, seriously."
    hide brown with qdis
    show yukino animated neutral smirk with qleft
    yu "You moron.  What I'm saying is, that's not a 10,000-yen bill!"
    hide yukino with qdis
    show brown animated neutral sad with qleft
    br "Huh?  O-Ohhh... you're right.  Awwww..."
    hide brown with qdis
    show ayase animated neutral smirk with qleft
    ay "Totally stupid.  There's no doubt you'll pay the piper."
    hide ayase with qdis
    show brown animated neutral sad with qleft
    br "U-Urgh!  Why's Ayase saying that now!?"
    hide brown with qdis
    show elly animated neutral serious with qleft
    el "It appears to be a message of some kind.  Brown, I don't know how you confused that with a 10,000-yen bill..."
    hide elly with qdis
    show nanjo animated neutral serious with qleft
    na "Well then, Naoya.  Will you do the honors?  Perhaps it holds a clue to our current predicament."
    hide nanjo with qleft
    $ tbnarrator = 1
    n "You kneel down to read the note.  It seems stuck fast to the frozen floor and can't be moved, though still read."
    "'Get rid of the main character's old costume from the 'Snow Queen.'  It's dirty, and bad luck to boot.'"
    "'It's to the right of the vaulting horse.  I'm counting on you, first-club!'"
    "'- Drama club president & star'"
    $ tbnarrator = 0
    show brown animated neutral serious with qleft
    br "Hey, didn't that hottie friend of Ms. Saeko's say that the costume was important?"
    hide brown with qdis
    $ tbnarrator = 1
    n "You and the others move to examine the location mentioned in the note, and you find an antique costume amongst the junk."
    ">Obtained Spiegel Mask, Spiegel Mail, Spiegel Beine, and Spiegel Blade!"
    $ tbnarrator = 0
label label138a:
    scene bg black #update with frozen warehouse
    #play music library fadeout 0.5 fadein 0.5 #update
    call screen SQCastle5
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "We gotta do all we can for these guys."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "Actually, melting them might, like, do more harm than good, y'know?"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "What an incredible find!"
    elif _return == 4:
        show nanjo animated neutral smirk with qleft
        na "That was quite a windfall.  One hardly expects such an amazing find."
    elif _return == 5:
        show brown animated neutral smirk with qleft
        br "A main character's costume?  It should go to me, naturally!  ...Oh, man... It doesn't fit!"
        show brown animated neutral sad
        br "Aw well... Much as it breaks my heart to do this... I guess I'll give it to you, Main.  "
        show brown animated neutral smirk
        extend "Just kidding!"
    elif _return == 6:
        $ tbnarrator = 1
        n "Fortified with new equipment, you and the others continue your trek through the frozen school."
        $ tbnarrator = 0
        jump label139
    jump label138a

label label139 (location = "3F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As you come to check another room, you are both surprised, and also not, to find Mariko there as well."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle6
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "How'd that girl get all the way up here?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Hey, look!  His eyelashes are frozen."
    elif _return == 3:
        mariko "I'm pretty much done exploring the towers, so I came back this way... But just like I thought, I'm pretty bushed now."
        mariko "This is so exciting, though!"
        mariko "'A Mysteriously Frozen School'!  'The Revival of Demons'!  'The Bizarre Towers and the School that Became a Labyrinth'!"
        mariko "So what do you think?  Me, I say it's all a secret conspiracy to take over the world by sorcery..."
    elif _return == 4:
        show elly animated neutral sad with qleft
        el "The same scenery, wherever we go... Are we really moving forward?"
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "Under normal circumstances, I find Ayase barely tolerable..."
        na "But it's something of a relief to have her around at a time like this."
    elif _return == 6:
        show brown animated neutral sad with qleft
        br "I'm starting to get sleepy..."
    elif _return == 7:
        $ tbnarrator = 1
        n "Trusting Mariko to be able to protect herself, given how far she seems to have traveled, you and the others move on."
        $ tbnarrator = 0
        jump label140
    jump label139

label label140 (location = "Ice Castle Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The Jack Frost pair seem to have settled in here as well, but they provide a small bit of levity, if nothing else."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle7
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Are they following us or something?"
    elif _return == 2:
        show ayase animated neutral smirk with qleft
        ay "Whoa, she's got him totally under her thumb."
    elif _return == 3:
        reiho "Going up?  Well, hee-have fun."
        raiho "Hee, you know what?  We saw a girl wearing a funky mask upstairs."
        reiho "She-ho was saying crazy stuff, like 'I'll hee-stroy this schoo!', ho."
        raiho "Nooo!  What are we-ho gonna do if the hee-school gets destroyed?"
        reiho "Work!  Work your hee-hiney off and support me for life!"
        raiho "So cold..."
    elif _return == 4:
        show elly animated neutral smirk with qleft
        el "These demons don't seem hostile."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "It appears that he's having his own difficulties..."
    elif _return == 6:
        show brown animated neutral sad with qleft
        br "Poor dude... I can totally sympathize."
    elif _return == 7:
        $ tbnarrator = 1
        n "As you turn to leave, the two Jack Frosts scamper on ahead of you, heading further into the ice castle."
        n "Elly suggests that you follow them and without a better plan, your group trails the two hee ho-kesters deeper within."
        $ tbnarrator = 0
        jump label141
    jump label140

label label141 (location = "4F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "You follow the pair upstairs to another room, where they seem to be waiting for you"
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle8
    if _return == 1:
        show yukino animated neutral smirk with qleft
        yu "It's those snowmen again.  What are they up to this time?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I think they like, want us to talk to them."
    elif _return == 3:
        if jackfrostfriend == False:
            raiho "Hee-ho!  Hey, you guys!  Will you be friends with me?"
            show ayase animated neutral smirk with qleft
            ay "Why not?  They're like, totally cute."
            hide ayase with qdis
            show elly animated neutral serious with qleft
            el "They don't seem to be dangerous.  I think it's in our best interest."
            hide elly with qdis
            hide screen header with dissolve
            $ choicetext = "Befriend the Jack Frosts?"
            show nchoice at pright zorder 15 with easeinright
            show nchoice onlayer screens zorder 15 at pright
            show fadeblack onlayer screens zorder 3 with dissolve
            $ choice1 = "Sure."
            $ choice2 = "Can't trust a demon."
            call screen choices with dissolve
            if _return == 1:
                hide screen choices with dissolve
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with dissolve
                show screen header with dissolve
                raiho "Hee-hoo!  Just 94 more people until I make 100 friends!"
                raiho "Just let me know if you'd like to go upstairs!  Friends hee-help each other out, ho!"
                $ jackfrostfriend = True
            elif _return == 2:
                hide screen choices with dissolve
                hide fadeblack onlayer screens
                hide nchoice onlayer screens
                hide nchoice
                with dissolve
                show screen header with dissolve
                reiho "Tch."
        else:
            raiho "Well, friends?  Is there anything I can do for you, ho?  I hee-know!  Want me-ho to take you upstairs?"
            show brown animated neutral smirk with pleft
            br "C'mon Naoya, what are you waiting for?  Let's go!"
            hide brown with qdis
            show yukino animated neutral serious with pleft
            yu "We've got a lot of people waiting on us.  Let's go."
            hide yukino with qdis
            $ tbnarrator = 1
            n "With everyone in agreement, you agree to Raiho's proposal to take everyone upstairs."
            $ tbnarrator = 0
            raiho "Raiho: Hee-ho!  Well then, hee-close your eyes for a minute, ho..."
            jump label142
    elif _return == 4:
        show elly animated neutral serious with qleft
        el "It seems some demons are amicable and naturally curious as well."
    elif _return == 5:
        show nanjo animated neutral sad with qleft
        na "Are they lonesome?"
    elif _return == 6:
        show brown animated neutral smirk with qleft
        br "I was looking at their mouths, and I got this craving for watermelon."
    jump label141

label label142 (location = "5F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "When you open your eyes, you find yourself in another classroom- a different one than you've been so far."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle9
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "What kind of magic trick is this snowman using?"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "Whoa... this is like, kinda creepy..."
    elif _return == 3:
        reiho "Hee-ho! This is the Fifth Floor!"
        raiho "Good luck, hee-friends-ho!"
    elif _return == 4:
        show elly animated neutral serious with qleft
        el "This place...wait."
        show elly animated neutral sad with qleft
        el "Fifth foor?  Our school doesn't have a fifth floor."
    elif _return == 5:
        show nanjo animated neutral serious with qleft
        na "It's a wooden building now, I see."
        show nanjo animated neutral smirk
        na "Did the Night Queen run out of funds to complete the castle's construction?"
    elif _return == 6:
        show brown animated neutral sad with qleft
        br "Oh, hell no!  This place is even colder!"
    elif _return == 7:
        $ tbnarrator = 1
        n "Now in a completely new area of the Snow Queen's castle, you and your allies move forward to put an end to her."
        $ tbnarrator = 0
        jump label143
    jump label142

label label143 (location = "8F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "However, the castle proves larger than expected, and three flights of stairs later, you seem to be no closer to your goal."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle10
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Yuka's acting like a child again.  Though this time, I can see why."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Seriously!  Isn't there some cool spell that'll warp us right to the Queen!?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "I've wondered for some time now... What do you fight for, Naoya?"
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "This place is as spacious as my own home.  I'm impressed."
    elif _return == 5:
        show brown animated neutral smirk with qleft
        br "Whew!  As the leader, I say let's take five."
    elif _return == 6:
        $ tbnarrator = 1
        n "Eventually, the rest break ends and despite grumblings from Ayase and Brown, you continue further into the castle."
        $ tbnarrator = 0
        jump label144
    jump label143

label label144 (location = "5F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The path winds up and down stairs, and soon you enter a classroom with an unexpected occupant."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    #update with Mai
    girl "I can't waste time like this... Excuse me.  Have you seen me?"
    show ayase animated neutral serious with qleft
    ay "Huh?  What's she trying to say?  Hey, little girl, what are you doing here?"
    ay "You should go home.  It's, like, really dangerous here."
    hide ayase with qdis
    show nanjo animated neutral serious with qleft
    na "Ayase!  It shouldn't even be possible for a small girl like her to be here!"
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "Look out, she may not even be human!"
    hide elly with qdis
    show ayase animated neutral sad with qleft
    ay "Sh-Shut up!  Get off my case!  I thought she was in trouble, so I talked to her, that's all!"
    ay "I'm not mean like you."
    hide ayase with qdis
    #update with Mai
    girl "I'm Mai.  I'm not lost, and I'm not a demon, either."
    girl "Anyway, have you seen me?  I'm wearing clothes like yours, and I have a white mask on."
    show yukino animated neutral serious with qleft
    yu "You're looking for a student from this school?  Sorry, but I don't know anyone who wears a mask."
    hide yukino with qdis
    #update with Mai
    mai "Oh.  Okay."
    #update with Mai disappearing
    show ayase animated neutral sad with qleft
    ay "H-hey!"
label label144a:
    scene bg black #update with frozen classroom
    call screen SQCastle11
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "What was that all about?"
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "I don't think she's a bad kid..."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "A little girl alone, here of all places... It has to be a monster!"
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "I remember seeing that girl around somewhere.  Who was she...?"
    elif _return == 5:
        show brown animated neutral smirk with qleft
        br "Wow, she's a cutie!  Give her ten years or so, and you'll have to hold me back!"
    elif _return == 6:
        $ tbnarrator = 1
        n "A little shaken by your encounter with the girl, you and your allies take a moment to ready yourselves."
        n "But before long, you and the others continue onward."
        $ tbnarrator = 0
        jump label145
    jump label144a

label label145 (location = "7F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The path winds back up the stairs, and within you find another little girl, this one garbed in black."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    show elly animated neutral serious with qleft
    el "Another little girl?  This continues to get stranger and stranger..."
    hide elly with qdis
    #update with Aki
    girl "I can't waste time like this!  Hey, have you seen my Daddy?"
    show ayase animated neutral serious with qleft
    ay "Your Daddy?  Huh, maybe she's lost.  Hey, little girl, what are you doing here?"
    ay "You should go home with that other little girl.  It's, like, really dangerous here."
    hide ayase with qdis
    show nanjo animated neutral serious with qleft
    na "Honestly! Won't you please try to be more cautious?"
    na "I'd appreciate if you made more of an effort to learn from your mistakes."
    hide nanjo with qdis
    show ayase animated neutral sad with qleft
    ay "Sh-Shut up!  Get off my case!  What if she's really looking for her dad?"
    show ayase animated neutral serious
    ay "Are you gonna leave her by herself!?"
    hide ayase with qdis
    #update with Aki
    girl "Um, don't you understand what I'm saying?  I'm asking if you saw my Daddy or not!"
    girl "He's wearing clothes like yours and a black mask."
    show yukino animated neutral serious with qleft
    yu "Sorry, but nobody I know wears a mask."
    hide yukino with qdis
    #update with Aki
    girl "Oh.  Okay then."
    #update with Aki disappearing
label label145a:
    scene bg black #update with frozen classroom
    call screen SQCastle12
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "What was that all about...?  Both of those little girls..."
    elif _return == 2:
        show ayase animated neutral sad with qleft
        ay "What's a little girl doing here?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "She has to be a monster!  How else could either of them be here?"
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "I'm certain I've seen those two around somewhere.  But where?  Where was it..?"
    elif _return == 5:
        show brown animated neutral sad with qleft
        br "Sassy girls like that... I'm not too good at dealing with them."
    elif _return == 6:
        $ tbnarrator = 1
        n "The back-to-back encounters with the two little girls have left everyone confused, especially Ayase."
        n "But Elly is now incensed to find the answers, leading the rest along further into the castle."
        $ tbnarrator = 0
        jump label146
    jump label145a

label label146 (location = "8F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "More stairs lead higher into the castle, and the seemingly endless maze is starting to sap away what remains of the good cheer."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle13
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "That Night Queen was calling the frozen school an Ice Castle... And yeah, it's a castle, all right."
        show yukino animated neutral sad
        yu "Going forward is a real pain."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I've always been bad at stuff like mazes and funhouses.  Grrrr!  This, like, sucks!"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "Two girls...one in white, one in black... what does it mean?"
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "I'm considering implementing a labyrinth to enhance my home security.  "
        show nanjo animated neutral smirk
        extend "Well?"
    elif _return == 5:
        show brown animated neutral serious with qleft
        br "Why's this place so huge!?  Does it actually end...?"
    elif _return == 6:
        $ tbnarrator = 1
        n "A growing feeling in your stomach that you're getting closer pushes you onward."
        $ tbnarrator = 0
        jump label147
    jump label146

label label147 (location = "5F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "As the group finds the next room to rest in... they come face-to-face with an unexpected individual."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom w/ Maki
    show yukino animated neutral sad with qleft
    yu "Maki..?"
    hide yukino with qdis
    show ayase animated neutral serious with qleft
    ay "Check out that painting... It's all black.  "
    show ayase animated neutral sad
    extend "Freaky..."
    hide ayase with qdis
    show elly animated neutral serious with qleft
    el "Is this an illusion, or some kind of trap?"
    hide elly with qdis
    show brown animated neutral smirk with qleft
    br "Maki, what's up with the mask?  You don't need to hide that cute face."
    hide brown with qdis
    #update with masked maki
    mma "I'm painting over your future with blackness.  Do you know why? Why must you get in my way?"
    mma "How can you withstand the pain?  You have each other... Ms. Saeko... your family... People you can rely on."
    mma "But I'm always alone.  I can only watch the happiness of others."
    show yukino animated neutral sad with qleft
    yu "Wait a sec, are you...?"
    hide yukino with qdis
    #update with masked maki
    mma "You can never understand how I feel!  I'll destroy this place... I'll destroy the whole school!"
    #update with maki vanishing
    show nanjo animated neutral sad with qleft
    na "Maki, wait! ..."
    hide nanjo with qdis
label label147a:
    scene bg black #update with frozen classroom
    call screen SQCastle14
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "Maki..."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Hey, didn't that one little girl ask about someone in a mask?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "But Maki can't possibly be here.  A demon, perhaps...?"
    elif _return == 4:
        show nanjo animated neutral sad with qleft
        na "It can't be... Maki was outside the school grounds."
    elif _return == 5:
        show brown animated neutral smirk with qleft
        br "Wow, Maki has some weird fashion sense.  You see that mask of hers?"
    elif _return == 6:
        $ tbnarrator = 1
        n "Confusion grips the group as you continue forward, trying to come to terms with having seen Maki."
        n "But there was no option but to move forward..."
        $ tbnarrator = 0
        jump label148
    jump label147a

label label148 (location = "5F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The walls of the school seem to have regressed back into old, wooden buildings as you climb further."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle15
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Did the building change because the past Snow Queens attended class in this one?"
        yu "...That would mean the demons have gotten even stronger."
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "You know, Yukino... Hey!  "
        show ayase animated neutral smirk
        extend "'You know' and 'Yukino' kinda sound alike!"
        hide ayase with qdis
        show yukino animated neutral serious with qleft
        yu "...This isn't the time to be fooling around, Ayase."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "It's said many generations of memories are ingrained into old schools."
        el "I only hope that doesn't mean evil things are in store for us."
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "Mayuzumi is right.  From this point on, we should brace for the worst."
    elif _return == 5:
        show brown animated neutral sad with qleft
        br "This place creeps me out.  It's bad enough that it's an old building..."
        br "But it's all frozen over, and our footsteps echo way too loud."
    elif _return == 6:
        $ tbnarrator = 1
        n "The creaky wooden walls add a new level of discontent to your group, but all of you can feel the end drawing close."
        $ tbnarrator = 0
        jump label149
    jump label148

label label149 (location = "Student Council Room 6F"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "Briefly, it seems you return to the more 'normal' school, but the Student Council room seems to hold another secret..."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom w/ Kandori
    #update with masked Kandori
    man "I didn't expect you'd take this long.  Have you seen her already?"
    show yukino animated neutral serious with qleft
    yu "You mean that girl in the art room...?  The one with the white mask?"
    hide yukino with qdis
    #update with masked kandori
    man "What did she say?"
    show elly animated neutral serious with qleft
    el "She had stated she wished to 'destroy the school'."
    hide elly with qdis
    #update with masked kandori
    man "I see.  Yes, that does sound like her.  This iced-over school is a byproduct of her heart."
    man "But it won't affect my plans."
    show ayase animated neutral serious with qleft
    ay "Huh?"
    hide ayase with qdis
    #update with masked kandori
    man "I've always believed the public school system served no purpose. Education should be reserved for society's chosen."
    man "If she wishes for its destruction, I see no harm in humoring her."
    show nanjo animated neutral serious with qleft
    na "You're Kandori, aren't you!?"
    hide nanjo with qdis
    #update with masked kandori
    man "Perhaps.  See if you can figure it out with that subpar brain of yours."
    #update with kandori disappearing
label label149a:
    scene bg black #update with frozen student council room
    call screen SQCastle16
    if _return == 1:
        show yukino animated neutral sad with qleft
        yu "Who's the weird guy in a mask...?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "So like, this is the old Student Council room?"
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "He isn't frozen?  Who is he...?"
    elif _return == 4:
        show nanjo at pleft2 with qleft
        na "......"
    elif _return == 5:
        show brown animated neutral serious with qleft
        br "I feel like I've seen this guy before."
    elif _return == 6:
        $ tbnarrator = 1
        n "With everyone now rattled further by the appearance of the masked man, it takes several moments to recover."
        n "But now Nanjo seems to be ready to solve this mystery as well with the new appearance, and urges everyone onward."
        $ tbnarrator = 0
        jump label150
    jump label149a

label label150 (location = "5F Classroom"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The school returns to the older, wooden visage as you reach another safe room."
    $ tbnarrator = 0
    scene bg black #update with frozen classroom
    call screen SQCastle17
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "What {i}is{/i} this floor?"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "Heyyyy, I've seen this room before... in an old framed photo in the principal's office."
        ay "It's the wooden school building that was here before they built the one we have."
    elif _return == 3:
        show elly animated neutral serious with qleft
        el "This certainly is an antique building.  "
        show elly animated neutral smirk
        extend "If we weren't in our current situation, I'd have enjoyed looking around."
    elif _return == 4:
        show nanjo animated neutral serious with qleft
        na "I'd expect Ayase to know.  She's certainly been to the principal's office enough."
    elif _return == 5:
        show brown animated neutral sad with qleft
        br "Warmth of handmade wooden buildings, my ass!"
        br "The wind blows through the cracks in the walls and it smells all musty... Makes me want a hot bath."
    elif _return == 6:
        $ tbnarrator = 1
        n "The hallway outside leads in only one direction, and you all can tell you're at the end of this long journey."
        n "Ready to put an end to things, you lead your group onward."
        $ tbnarrator = 0
        jump label151
    jump label150

label label151 (location = "Stage"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The door opens to reveal a stage, and the Night Queen stands upon it, all on her own."
    $ tbnarrator = 0
    scene bg black #update with frozen stage
    #update with night queen
    nq "Hmhm... You came all the way up here?  It would have been easier if you'd just waited for the Eternal Night to fall."
    nq "But if you insist... I shall grant your wish with despair.  You won't find me as easy as Tomomi. Hmhmhmhmhm..."
    #update with masked maki
    mma "Why are you trying so hard to protect this place?  I hate school... I wish it would disappear from the face of the earth!"
    #update with masked kandori
    man "Allow us to assist you, Night Queen.  Though it's a bit crowded here for the three of us to combine our strength..."
    man "I invite you all to the uppermost floor.  You may take your time in coming to us."
    #update with the Night Queen and Masked Maki disappearing
label label151a:
    scene bg black #update with frozen student council room
    call screen SQCastle18
    if _return == 1:
        show yukino animated neutral serious with qleft
        yu "Let's go!"
    elif _return == 2:
        show ayase animated neutral serious with qleft
        ay "I'm all set!"
    elif _return == 3:
        show elly animated neutral smirk with qleft
        el "I'm glad this freezing cold won't last much longer."
    elif _return == 4:
        show nanjo at pleft2 with qleft
        na "......"
    elif _return == 5:
        show brown animated neutral smirk with qleft
        br "All right team! I'll lead you to victory!"
    elif _return == 6:
        #update with masked kandori
        man "Are you ready?  Have you made your preparations to advance to the final floor?"
        $ tbnarrator = 1
        n "With you and your allies all ready, you nod."
        $ tbnarrator = 0
        #update with masked kandori
        man "Very well."
        jump label152
    jump label151a

label label152 (location = "Summit"):
    scene bg black #update with frozen Thanatos Tower entry room
    #play music library fadeout 0.5 fadein 0.5 #update
    $ tbnarrator = 1
    n "The Night Queen stands atop the summit of the castle, her body fused with the masked girl and masked man."
    $ tbnarrator = 0
    scene bg black #update with frozen stage
    #update with night queen
    nq "I've been waiting for you."
    #update with masked maki
    mma "No more school!  Ever!"
    #update with masked kandori
    man "Let's see what you can do."
    scene bg black #update with battle scene
    $ tbnarrator = 1
    n "The Night Queen's power is tremendous, and at first it seems that there's no chance that you and your allies will win."
    n "But patience and teamwork steadily begin to win out as each of you continue to stand up again and again."
    n "The Eternal Night is resisted by the six of you, and every time one of you goes down, another steps forward."
    n "Eventually, the Night Queen begins to weaken, and before long, her power wanes entirely, leaving you victorious."
    $ tbnarrator = 0
    #update with snow queen
    sq "Urgh... I failed... against these youths?  How distressing... But heed my words..."
    sq "Eternal night will fall again so long as people seek to turn hope to despair..."
    #update with masked maki
    mma "No... How could this happen!?  This is my world...!"
    #update with masked kandori
    man "As I thought.  Improvising didn't suffice, and we must take matters into our own hands."
    man "Your name was Toudou, yes?  I have a feeling we'll see each other again."
    #update with the masked figures all disappearing
    #update with the snow queen movie of the ice melting
    scene bg black #update with entrance hall
    #play music schooldays fadeout 0.5 fadein 0.5 #update
    show saeko animated neutral serious with qleft
    sa "You're really going?"
    hide saeko with qdis
    show nanjo animated neutral serious with qleft
    na "Yes.  I'm worried about Maki and Masao.  And something else, too..."
    hide nanjo with qdis
    show elly animated neutral serious with qleft
    el "Yes, that girl with the white mask looked just like Maki..."
    hide elly with qdis
    show yukino animated neutral smirk with qleft
    yu "Yeah, there's still some business we gotta take care of.  Right, Naoya?"
    hide yukino with qdis
    $ tbnarrator = 1
    n "You nod in agreement."
    $ tbnarrator = 0
    show yukino animated neutral serious with qleft
    yu "We gotta find Maki... She looked like she was in pain to me."
    hide yukino with qdis
    show saeko animated netural serious with qleft
    sa "...Alright.  Then you go do what you gotta do!  You're adults now, setting out on your own."
    sa "I won't stop you.  But promise me this..."
    hide saeko with qdis
    show ayase animated neutral serious with qleft
    ay "Huh?  Promise what?"
    hide ayase with qdis
    show saeko animated neutral smirk with qleft
    sa "Come back and see me before you get all old and wrinkled!  And come back to report in when it's all over with!"
    hide saeko with qdis
    show yukino animated neutral smirk with qleft
    yu "Oh, we will, don't worry about that!  We're your best students, remember?"
    hide yukino with qdis
    show saeko animated neutral smirk with qleft
    sa "She says, while wearing an outfit that's against the dress code."
    sa "You should try being in my shoes, getting yelled at every day by the vice principal!"
    sa "Haha... it looks like this incident has given him second thoughts, though.  He asked me to thank you guys."
    sa "Maybe now he won't be so strict... for a while, at least."
    hide saeko with qdis
    show ayase animated neutral smirk with qleft
    ay "Hah!  That cueball?  As if!"
    hide ayase with qdis
    show saeko animated neutral serious with qleft
    sa "Oh, he's not really all that bad.  But anyway!  You should stop chitchatting and get going before it's too late!"
    hide saeko with qdis
    show yukino animated neutral smirk with qleft
    yu "Right!"
    hide yukino with qdis
    show brown animated neutral smirk with qleft
    br "C'mon, what's there to worry about?  I'll be with them!  C'mon, honey... Don't spoil that pretty face with tears."
    br "Mwahahahaha!"
    hide brown with qdis
    show elly animated neutral serious with qleft
    el "The school's returned to normal... But that's only the beginning.  Our true battle comes later."
    el "First, we must restore peace to our city.  We're still young... there's a lot of life yet to fight through."
    el "I'll rise to the challenge!"
    hide elly with qdis
    show nanjo animated neutral serious with qleft
    na "When there's a will, there's a way... That's how I feel with friends like these."
    na "Rest assured, Ms. Saeko, we'll find Masao and Maki!  Let's go, Naoya!"
    hide nanjo with qdis
    show ayase animated neutral serious with qleft
    ay "Y'know, up to now, I've just been doing whatever I feel like..."
    ay "But when I see Yukino and the others try so hard, I feel like I can do way better."
    ay "I dunno how exactly, but that can wait until after we save the town."
    show ayase animated neutral smirk
    ay "Catch you later, Ms. Saeko!"
    hide ayase with qdis
    show yukino animated neutral smirk with qleft
    yu "Once the town's back to normal, I'm going to hit the books.  Just you watch!"
    yu "I'll be just as awesome a teacher as you, Ms. Saeko!  Haha... I'll see you later, yeah?"
    hide yukino with qdis
    show saeko animated neutral smirk with qleft
    sa "Thanks for everything, Naoya!  Looks like they have ideas for their future."
    sa "How about you?  Do you have a future in mind?"
    hide saeko with qdis
    $ tbnarrator = 1
    n "You glance over your friends, feeling their wishes for the future, before you turn to look at Ms. Saeko, nodding."
    $ tbnarrator = 0
    show saeko animated neutral smirk with qleft
    sa "Great!  You've done something amazing here.  Savor that feeling and give it your all!"
    hide saeko with qdis
    #update with all the students leaving
    show saeko animated neutral serious with qleft
    sa "Phew.  Now then..."
    hide saeko with qdis
    show bg white
    hide bg white with dissolve
    #update with butterfly appearing
    show saeko animated neutral smirk with qleft
    sa "Hm?  Hey there, little guy.  Where did you come from?  Are you here to wish them luck, too?  Haha..."
    hide saeko
    scene bg black with dissolve
    $ tbnarrator = 1
    n "The castle of ice returned to its familiar form of St. Hermelin High, thanks to the students' courage."
    n "With the mask's curse dispelled, one of the school's enigmas came to a close."
    n "'Eternal night will fall again so long as people seek to turn hope to despair.'"
    n "Having banished the darkness in their souls, the students take the Queen's words to heart as they start taking steps towards their futures..."
    $ tbnarrator = 0
    scene bg black with dissolve #update with courtyard w/ Mark
    show nanjo animated neutral serious with qleft
    na "Masao!"
    hide nanjo with qdis
    show brown animated neutral serious with qleft
    br "M-Mark?"
    hide brown with qdis
    show ayase animated neutral sad with qleft
    ay "Huh?  Hey, where's Maki?"
    hide ayase with qdis
    show mark animated neutral sad with qleft
    mk "Oh man... Guys, I need your help!"
    hide mark with qdis
    show yukino animated neutral serious with qleft
    yu "Did something happen to Maki?"
    hide yukino with qdis
    show mark animated neutral serious with qleft
    mk "I'm sorry... I never shoulda let it happen... We went to the SEBEC building, but the demons inside got her."
    mk "They're pretty tough, and I don't think I can handle 'em on my own."
    hide mark with qdis
    show yukino animated neutral sad with qleft
    yu "What!?"
    hide yukino with qdis
    show elly animated neutral serious with qleft
    el "We must rescue her, quickly!"
    hide elly with qdis
    show brown animated neutral serious with qleft
    br "Alright!"
    everyone "Let's go!"
    scene bg black with dissolve
    $ tbnarrator = 1
    n "This story will continue.  Thank you for playing through the first part of Persona: Metamorphosis!"
    $ tbnarrator = 0
    $ MainMenu(confirm=False)()

#####SQQ Navigation Labels####

label callSQHermelinFloor1:
    hide hf1
    hide hf2
    hide hs
    play music schooldays volume 0.4 if_changed
    if floor == 2:
        $ tbnarrator = 1
        "You move to the first floor of the school"
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "First Floor"
        $ floor = 1
        show hf1 zorder 0 with moveinbottom
        $ tbnarrator = 0
        call screen SQHermelinFloor1(_with_none=False)
    elif floor == 4:
        $ tbnarrator = 1
        "You move to the first floor of the school"
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "First Floor"
        $ floor = 1
        show hf1 zorder 0 with moveinleft
        $ tbnarrator = 0
        call screen SQHermelinFloor1(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "First Floor"
        $ floor = 1
        show hf1 with dissolve
        $ tbnarrator = 0
        call screen SQHermelinFloor1(_with_none=False) with dissolve

label callSQSportsBuilding:
    hide hf1
    hide hs
    play music schooldays volume 0.4 if_changed
    if floor == 1:
        $ tbnarrator = 1
        "You move to the Sports Building of the school"
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Sports Building"
        $ floor = 4
        show hs zorder 0 with moveinright
        $ tbnarrator = 0
        call screen SQHermelinSportsBuilding(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Sports Building"
        $ floor = 4
        show hs with dissolve
        $ tbnarrator = 0
        call screen SQHermelinSportsBuilding(_with_none=False)
label callSQHermelinFloor2:
    hide hf1
    hide hf2
    hide hf3
    play music schooldays volume 0.4 if_changed
    if floor == 1:
        $ tbnarrator = 1
        "You move to the second floor of the school."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Second Floor"
        $ floor = 2
        show hf2 zorder 0 with moveintop
        $ tbnarrator = 0
        call screen SQHermelinFloor2(_with_none=False)
    elif floor == 3:
        $ tbnarrator = 1
        "You move to the second floor of the school."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Second Floor"
        $ floor = 2
        show hf2 zorder 0 with moveinbottom
        $ tbnarrator = 0
        call screen SQHermelinFloor2(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Second Floor"
        $ floor = 2
        show hf2 with dissolve
        $ tbnarrator = 0
        call screen SQHermelinFloor2(_with_none=False)
label callSQHermelinFloor3:
    hide hf3
    hide hf2
    play music schooldays volume 0.4 if_changed
    if floor == 2:
        $ tbnarrator = 1
        "You move to the third floor of the school."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Third Floor"
        $ floor = 3
        show hf3 zorder 0 with moveintop
        $ tbnarrator = 0
        call screen SQHermelinFloor3(_with_none=False)
    else:
        $ tbnarrator = 1
        "You move back into the hallway."
        window hide
        hide screen header
        show fadeblack with dissolve
        $ location = "Third Floor"
        $ floor = 3
        show hf3 zorder 0 with dissolve
        $ tbnarrator = 0
        call screen SQHermelinFloor3(_with_none=False)
