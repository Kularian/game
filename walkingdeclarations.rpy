#Walking Definitions

transform naoyaloc:
    xpos naoyax
    ypos naoyay

transform nanjoloc:
    xpos nanjox
    ypos nanjoy

transform markloc:
    xpos markx
    ypos marky

transform brownloc:
    xpos brownx
    ypos browny

transform ellyloc:
    xpos ellyx
    ypos ellyy

transform ayaseloc:
    xpos ayasex
    ypos ayasey

transform yukinoloc:
    xpos yukinox
    ypos yukinoy

transform reijiloc:
    xpos reijix
    ypos reijiy

transform makiloc:
    xpos makix
    ypos makiy

transform npc1loc:
    xpos npc1x
    ypos npc1y

transform npc2loc:
    xpos npc2x
    ypos npc2y

transform npc3loc:
    xpos npc3x
    ypos npc3y

transform npc4loc:
    xpos npc4x
    ypos npc4y

transform npc5loc:
    xpos npc5x
    ypos npc5y

transform clerk1loc:
    xpos clerk1x
    ypos clerk1y

transform clerk2loc:
    xpos clerk2x
    ypos clerk2y

transform newloc:
    xpos newlocx
    ypos newlocy

#PC Standing Declarations

image naoyasprite downleft stand = "naoya/walking/DLStanding1.png"
image naoyasprite downright stand = "naoya/walking/DRStanding1.png"
image naoyasprite upleft stand = "naoya/walking/ULStanding1.png"
image naoyasprite upright stand = "naoya/walking/URStanding1.png"

image marksprite downleft stand = "mark/walking/DLStanding1.png"
image marksprite downright stand = "mark/walking/DRStanding1.png"
image marksprite upleft stand = "mark/walking/ULStanding1.png"
image marksprite upright stand = "mark/walking/URStanding1.png"

image nanjosprite downleft stand = "nanjo/walking/DLStanding1.png"
image nanjosprite downright stand = "nanjo/walking/DRStanding1.png"
image nanjosprite upleft stand = "nanjo/walking/ULStanding1.png"
image nanjosprite upright stand = "nanjo/walking/URStanding1.png"

image yukinosprite downleft stand = "yukino/walking/DLStanding1.png"
image yukinosprite downright stand = "yukino/walking/DRStanding1.png"
image yukinosprite upleft stand = "yukino/walking/ULStanding1.png"
image yukinosprite upright stand = "yukino/walking/URStanding1.png"

image brownsprite downleft stand = "brown/walking/DLStanding1.png"
image brownsprite downright stand = "brown/walking/DRStanding1.png"
image brownsprite upleft stand = "brown/walking/ULStanding1.png"
image brownsprite upright stand = "brown/walking/URStanding1.png"

image ayasesprite downleft stand = "ayase/walking/DLStanding1.png"
image ayasesprite downright stand = "ayase/walking/DRStanding1.png"
image ayasesprite upleft stand = "ayase/walking/ULStanding1.png"
image ayasesprite upright stand = "ayase/walking/URStanding1.png"

image makisprite downleft stand = "maki/walking/DLStanding1.png"
image makisprite downright stand = "maki/walking/DRStanding1.png"
image makisprite upleft stand = "maki/walking/ULStanding1.png"
image makisprite upright stand = "maki/walking/URStanding1.png"

image reijisprite downleft stand = "reiji/walking/DLStanding1.png"
image reijisprite downright stand = "reiji/walking/DRStanding1.png"
image reijisprite upleft stand = "reiji/walking/ULStanding1.png"
image reijisprite upright stand = "reiji/walking/URStanding1.png"

image ellysprite downleft stand = "elly/walking/DLStanding1.png"
image ellysprite downright stand = "elly/walking/DRStanding1.png"
image ellysprite upleft stand = "elly/walking/ULStanding1.png"
image ellysprite upright stand = "elly/walking/URStanding1.png"

#NPC Standing Declarations

image hanyasprite downleft stand = "hanya/walking/DLStanding1.png"
image hanyasprite downright stand = "hanya/walking/DRStanding1.png"
image hanyasprite upleft stand = "hanya/walking/ULStanding1.png"
image hanyasprite upright stand = "hanya/walking/URStanding1.png"

image natsumisprite downleft stand = "natsumi/walking/DLStanding1.png"
image natsumisprite downright stand = "natsumi/walking/DRStanding1.png"
image natsumisprite upleft stand = "natsumi/walking/ULStanding1.png"
image natsumisprite upright stand = "natsumi/walking/URStanding1.png"

image ooishisprite downleft stand = "ooishi/walking/DLStanding1.png"
image ooishisprite downright stand = "ooishi/walking/DRStanding1.png"
image ooishisprite upleft stand = "ooishi/walking/ULStanding1.png"
image ooishisprite upright stand = "ooishi/walking/URStanding1.png"

image saekosprite downleft stand = "saeko/walking/DLStanding1.png"
image saekosprite downright stand = "saeko/walking/DRStanding1.png"
image saekosprite upleft stand = "saeko/walking/ULStanding1.png"
image saekosprite upright stand = "saeko/walking/URStanding1.png"

image snowqueensprite downleft stand = "snowqueen/walking/DLStanding1.png"
image snowqueensprite downright stand = "snowqueen/walking/DRStanding1.png"
image snowqueensprite upleft stand = "snowqueen/walking/ULStanding1.png"
image snowqueensprite upright stand = "snowqueen/walking/URStanding1.png"

image tsutomusprite downleft stand = "tsutomu/walking/DLStanding1.png"
image tsutomusprite downright stand = "tsutomu/walking/DRStanding1.png"
image tsutomusprite upleft stand = "tsutomu/walking/ULStanding1.png"
image tsutomusprite upright stand = "tsutomu/walking/URStanding1.png"

#Emotion Indicators

image exclamation = "gui/talking/surprised.png"

#PC Moving-Standing Declarations
#Naoya
image naoyasprite downleft standmove:
    Image("naoya/walking/DLStanding1.png")
    pause 2.25
    Image("naoya/walking/DLStanding2.png")
    pause 1.75
    repeat

image naoyasprite downright standmove:
    Image("naoya/walking/DRStanding1.png")
    pause 2.25
    Image("naoya/walking/DRStanding2.png")
    pause 1.75
    repeat

image naoyasprite upleft standmove:
    Image("naoya/walking/ULStanding1.png")
    pause 2.25
    Image("naoya/walking/ULStanding2.png")
    pause 1.75
    repeat

image naoyasprite upright standmove:
    Image("naoya/walking/URStanding1.png")
    pause 2.25
    Image("naoya/walking/URStanding2.png")
    pause 1.75
    repeat

#Mark
image marksprite downleft standmove:
    Image("mark/walking/DLStanding1.png")
    pause 2.25
    Image("mark/walking/DLStanding2.png")
    pause 1.75
    repeat

image marksprite downright standmove:
    Image("mark/walking/DRStanding1.png")
    pause 2.25
    Image("mark/walking/DRStanding2.png")
    pause 1.75
    repeat

image marksprite upleft standmove:
    Image("mark/walking/ULStanding1.png")
    pause 2.25
    Image("mark/walking/ULStanding2.png")
    pause 1.75
    repeat

image marksprite upright standmove:
    Image("mark/walking/URStanding1.png")
    pause 2.25
    Image("mark/walking/URStanding2.png")
    pause 1.75
    repeat

#Nanjo
image nanjosprite downleft standmove:
    Image("nanjo/walking/DLStanding1.png")
    pause 2.25
    Image("nanjo/walking/DLStanding2.png")
    pause 1.75
    repeat

image nanjosprite downright standmove:
    Image("nanjo/walking/DRStanding1.png")
    pause 2.25
    Image("nanjo/walking/DRStanding2.png")
    pause 1.75
    repeat

image nanjosprite upleft standmove:
    Image("nanjo/walking/ULStanding1.png")
    pause 2.25
    Image("nanjo/walking/ULStanding2.png")
    pause 1.75
    repeat

image nanjosprite upright standmove:
    Image("nanjo/walking/URStanding1.png")
    pause 2.25
    Image("nanjo/walking/URStanding2.png")
    pause 1.75
    repeat

#yukino
image yukinosprite downleft standmove:
    Image("yukino/walking/DLStanding1.png")
    pause 2.25
    Image("yukino/walking/DLStanding2.png")
    pause 1.75
    repeat

image yukinosprite downright standmove:
    Image("yukino/walking/DRStanding1.png")
    pause 2.25
    Image("yukino/walking/DRStanding2.png")
    pause 1.75
    repeat

image yukinosprite upleft standmove:
    Image("yukino/walking/ULStanding1.png")
    pause 2.25
    Image("yukino/walking/ULStanding2.png")
    pause 1.75
    repeat

image yukinosprite upright standmove:
    Image("yukino/walking/URStanding1.png")
    pause 2.25
    Image("yukino/walking/URStanding2.png")
    pause 1.75
    repeat

#ayase
image ayasesprite downleft standmove:
    Image("ayase/walking/DLStanding1.png")
    pause 2.25
    Image("ayase/walking/DLStanding2.png")
    pause 1.75
    repeat

image ayasesprite downright standmove:
    Image("ayase/walking/DRStanding1.png")
    pause 2.25
    Image("ayase/walking/DRStanding2.png")
    pause 1.75
    repeat

image ayasesprite upleft standmove:
    Image("ayase/walking/ULStanding1.png")
    pause 2.25
    Image("ayase/walking/ULStanding2.png")
    pause 1.75
    repeat

image ayasesprite upright standmove:
    Image("ayase/walking/URStanding1.png")
    pause 2.25
    Image("ayase/walking/URStanding2.png")
    pause 1.75
    repeat

#brown
image brownsprite downleft standmove:
    Image("brown/walking/DLStanding1.png")
    pause 2.25
    Image("brown/walking/DLStanding2.png")
    pause 1.75
    repeat

image brownsprite downright standmove:
    Image("brown/walking/DRStanding1.png")
    pause 2.25
    Image("brown/walking/DRStanding2.png")
    pause 1.75
    repeat

image brownsprite upleft standmove:
    Image("brown/walking/ULStanding1.png")
    pause 2.25
    Image("brown/walking/ULStanding2.png")
    pause 1.75
    repeat

image brownsprite upright standmove:
    Image("brown/walking/URStanding1.png")
    pause 2.25
    Image("brown/walking/URStanding2.png")
    pause 1.75
    repeat

#elly
image ellysprite downleft standmove:
    Image("elly/walking/DLStanding1.png")
    pause 2.25
    Image("elly/walking/DLStanding2.png")
    pause 1.75
    repeat

image ellysprite downright standmove:
    Image("elly/walking/DRStanding1.png")
    pause 2.25
    Image("elly/walking/DRStanding2.png")
    pause 1.75
    repeat

image ellysprite upleft standmove:
    Image("elly/walking/ULStanding1.png")
    pause 2.25
    Image("elly/walking/ULStanding2.png")
    pause 1.75
    repeat

image ellysprite upright standmove:
    Image("elly/walking/URStanding1.png")
    pause 2.25
    Image("elly/walking/URStanding2.png")
    pause 1.75
    repeat

#reiji
image reijisprite downleft standmove:
    Image("reiji/walking/DLStanding1.png")
    pause 2.25
    Image("reiji/walking/DLStanding2.png")
    pause 1.75
    repeat

image reijisprite downright standmove:
    Image("reiji/walking/DRStanding1.png")
    pause 2.25
    Image("reiji/walking/DRStanding2.png")
    pause 1.75
    repeat

image reijisprite upleft standmove:
    Image("reiji/walking/ULStanding1.png")
    pause 2.25
    Image("reiji/walking/ULStanding2.png")
    pause 1.75
    repeat

image reijisprite upright standmove:
    Image("reiji/walking/URStanding1.png")
    pause 2.25
    Image("reiji/walking/URStanding2.png")
    pause 1.75
    repeat

#maki
image makisprite downleft standmove:
    Image("maki/walking/DLStanding1.png")
    pause 2.25
    Image("maki/walking/DLStanding2.png")
    pause 1.75
    repeat

image makisprite downright standmove:
    Image("maki/walking/DRStanding1.png")
    pause 2.25
    Image("maki/walking/DRStanding2.png")
    pause 1.75
    repeat

image makisprite upleft standmove:
    Image("maki/walking/ULStanding1.png")
    pause 2.25
    Image("maki/walking/ULStanding2.png")
    pause 1.75
    repeat

image makisprite upright standmove:
    Image("maki/walking/URStanding1.png")
    pause 2.25
    Image("maki/walking/URStanding2.png")
    pause 1.75
    repeat

#NPC Moving-Standing Declarations

#tsutomu
image tsutomusprite downleft standmove:
    Image("tsutomu/walking/DLStanding1.png")
    pause 2.25
    Image("tsutomu/walking/DLStanding2.png")
    pause 1.75
    repeat

image tsutomusprite downright standmove:
    Image("tsutomu/walking/DRStanding1.png")
    pause 2.25
    Image("tsutomu/walking/DRStanding2.png")
    pause 1.75
    repeat

image tsutomusprite upleft standmove:
    Image("tsutomu/walking/ULStanding1.png")
    pause 2.25
    Image("tsutomu/walking/ULStanding2.png")
    pause 1.75
    repeat

image tsutomusprite upright standmove:
    Image("tsutomu/walking/URStanding1.png")
    pause 2.25
    Image("tsutomu/walking/URStanding2.png")
    pause 1.75
    repeat

#Snowqueen
image snowqueensprite downleft standmove:
    Image("snowqueen/walking/DLStanding1.png")
    pause 2.25
    Image("snowqueen/walking/DLStanding2.png")
    pause 1.75
    repeat

image snowqueensprite downright standmove:
    Image("snowqueen/walking/DRStanding1.png")
    pause 2.25
    Image("snowqueen/walking/DRStanding2.png")
    pause 1.75
    repeat

image snowqueensprite upleft standmove:
    Image("snowqueen/walking/ULStanding1.png")
    pause 2.25
    Image("snowqueen/walking/ULStanding2.png")
    pause 1.75
    repeat

image snowqueensprite upright standmove:
    Image("snowqueen/walking/URStanding1.png")
    pause 2.25
    Image("snowqueen/walking/URStanding2.png")
    pause 1.75
    repeat

#Saeko
image saekosprite downleft standmove:
    Image("saeko/walking/DLStanding1.png")
    pause 2.25
    Image("saeko/walking/DLStanding2.png")
    pause 1.75
    repeat

image saekosprite downright standmove:
    Image("saeko/walking/DRStanding1.png")
    pause 2.25
    Image("saeko/walking/DRStanding2.png")
    pause 1.75
    repeat

image saekosprite upleft standmove:
    Image("saeko/walking/ULStanding1.png")
    pause 2.25
    Image("saeko/walking/ULStanding2.png")
    pause 1.75
    repeat

image saekosprite upright standmove:
    Image("saeko/walking/URStanding1.png")
    pause 2.25
    Image("saeko/walking/URStanding2.png")
    pause 1.75
    repeat

#Ooishi
image ooishisprite downleft standmove:
    Image("ooishi/walking/DLStanding1.png")
    pause 2.25
    Image("ooishi/walking/DLStanding2.png")
    pause 1.75
    repeat

image ooishisprite downright standmove:
    Image("ooishi/walking/DRStanding1.png")
    pause 2.25
    Image("ooishi/walking/DRStanding2.png")
    pause 1.75
    repeat

image ooishisprite upleft standmove:
    Image("ooishi/walking/ULStanding1.png")
    pause 2.25
    Image("ooishi/walking/ULStanding2.png")
    pause 1.75
    repeat

image ooishisprite upright standmove:
    Image("ooishi/walking/URStanding1.png")
    pause 2.25
    Image("ooishi/walking/URStanding2.png")
    pause 1.75
    repeat

#natsumi
image natsumisprite downleft standmove:
    Image("natsumi/walking/DLStanding1.png")
    pause 2.25
    Image("natsumi/walking/DLStanding2.png")
    pause 1.75
    repeat

image natsumisprite downright standmove:
    Image("natsumi/walking/DRStanding1.png")
    pause 2.25
    Image("natsumi/walking/DRStanding2.png")
    pause 1.75
    repeat

image natsumisprite upleft standmove:
    Image("natsumi/walking/ULStanding1.png")
    pause 2.25
    Image("natsumi/walking/ULStanding2.png")
    pause 1.75
    repeat

image natsumisprite upright standmove:
    Image("natsumi/walking/URStanding1.png")
    pause 2.25
    Image("natsumi/walking/URStanding2.png")
    pause 1.75
    repeat

#hanya
image hanyasprite downleft standmove:
    Image("hanya/walking/DLStanding1.png")
    pause 2.25
    Image("hanya/walking/DLStanding2.png")
    pause 1.75
    repeat

image hanyasprite downright standmove:
    Image("hanya/walking/DRStanding1.png")
    pause 2.25
    Image("hanya/walking/DRStanding2.png")
    pause 1.75
    repeat

image hanyasprite upleft standmove:
    Image("hanya/walking/ULStanding1.png")
    pause 2.25
    Image("hanya/walking/ULStanding2.png")
    pause 1.75
    repeat

image hanyasprite upright standmove:
    Image("hanya/walking/URStanding1.png")
    pause 2.25
    Image("hanya/walking/URStanding2.png")
    pause 1.75
    repeat

#Walking Declarations
#Naoya

image naoyasprite downleft walk:
    Image("naoya/walking/DLStanding1.png")
    pause 0.15
    Image("naoya/walking/DLWalkL1.png")
    pause 0.15
    Image("naoya/walking/DLWalkL2.png")
    pause 0.15
    Image("naoya/walking/DLWalkL1.png")
    pause 0.15
    Image("naoya/walking/DLStanding1.png")
    pause 0.15
    Image("naoya/walking/DLWalkR1.png")
    pause 0.15
    Image("naoya/walking/DLWalkR2.png")
    pause 0.15
    Image("naoya/walking/DLWalkR1.png")
    pause 0.15
    repeat

image naoyasprite downright walk:
    Image("naoya/walking/DRStanding1.png")
    pause 0.15
    Image("naoya/walking/DRWalkL1.png")
    pause 0.15
    Image("naoya/walking/DRWalkL2.png")
    pause 0.15
    Image("naoya/walking/DRWalkL1.png")
    pause 0.15
    Image("naoya/walking/DRStanding1.png")
    pause 0.15
    Image("naoya/walking/DRWalkR1.png")
    pause 0.15
    Image("naoya/walking/DRWalkR2.png")
    pause 0.15
    Image("naoya/walking/DRWalkR1.png")
    pause 0.15
    repeat

image naoyasprite upright walk:
    Image("naoya/walking/URStanding1.png")
    pause 0.15
    Image("naoya/walking/URWalkL1.png")
    pause 0.15
    Image("naoya/walking/URWalkL2.png")
    pause 0.15
    Image("naoya/walking/URWalkL1.png")
    pause 0.15
    Image("naoya/walking/URStanding1.png")
    pause 0.15
    Image("naoya/walking/URWalkR1.png")
    pause 0.15
    Image("naoya/walking/URWalkR2.png")
    pause 0.15
    Image("naoya/walking/URWalkR1.png")
    pause 0.15
    repeat

image naoyasprite upleft walk:
    Image("naoya/walking/ULStanding1.png")
    pause 0.15
    Image("naoya/walking/ULWalkL1.png")
    pause 0.15
    Image("naoya/walking/ULWalkL2.png")
    pause 0.15
    Image("naoya/walking/ULWalkL1.png")
    pause 0.15
    Image("naoya/walking/ULStanding1.png")
    pause 0.15
    Image("naoya/walking/ULWalkR1.png")
    pause 0.15
    Image("naoya/walking/ULWalkR2.png")
    pause 0.15
    Image("naoya/walking/ULWalkR1.png")
    pause 0.15
    repeat

#Ayase
image ayasesprite downleft walk:
    Image("ayase/walking/DLStanding1.png")
    pause 0.15
    Image("ayase/walking/DLWalkL1.png")
    pause 0.15
    Image("ayase/walking/DLWalkL2.png")
    pause 0.15
    Image("ayase/walking/DLWalkL1.png")
    pause 0.15
    Image("ayase/walking/DLStanding1.png")
    pause 0.15
    Image("ayase/walking/DLWalkR1.png")
    pause 0.15
    Image("ayase/walking/DLWalkR2.png")
    pause 0.15
    Image("ayase/walking/DLWalkR1.png")
    pause 0.15
    repeat

image ayasesprite downright walk:
    Image("ayase/walking/DRStanding1.png")
    pause 0.15
    Image("ayase/walking/DRWalkL1.png")
    pause 0.15
    Image("ayase/walking/DRWalkL2.png")
    pause 0.15
    Image("ayase/walking/DRWalkL1.png")
    pause 0.15
    Image("ayase/walking/DRStanding1.png")
    pause 0.15
    Image("ayase/walking/DRWalkR1.png")
    pause 0.15
    Image("ayase/walking/DRWalkR2.png")
    pause 0.15
    Image("ayase/walking/DRWalkR1.png")
    pause 0.15
    repeat

image ayasesprite upright walk:
    Image("ayase/walking/URStanding1.png")
    pause 0.15
    Image("ayase/walking/URWalkL1.png")
    pause 0.15
    Image("ayase/walking/URWalkL2.png")
    pause 0.15
    Image("ayase/walking/URWalkL1.png")
    pause 0.15
    Image("ayase/walking/URStanding1.png")
    pause 0.15
    Image("ayase/walking/URWalkR1.png")
    pause 0.15
    Image("ayase/walking/URWalkR2.png")
    pause 0.15
    Image("ayase/walking/URWalkR1.png")
    pause 0.15
    repeat

image ayasesprite upleft walk:
    Image("ayase/walking/ULStanding1.png")
    pause 0.15
    Image("ayase/walking/ULWalkL1.png")
    pause 0.15
    Image("ayase/walking/ULWalkL2.png")
    pause 0.15
    Image("ayase/walking/ULWalkL1.png")
    pause 0.15
    Image("ayase/walking/ULStanding1.png")
    pause 0.15
    Image("ayase/walking/ULWalkR1.png")
    pause 0.15
    Image("ayase/walking/ULWalkR2.png")
    pause 0.15
    Image("ayase/walking/ULWalkR1.png")
    pause 0.15
    repeat

#brown
image brownsprite downleft walk:
    Image("brown/walking/DLStanding1.png")
    pause 0.15
    Image("brown/walking/DLWalkL1.png")
    pause 0.15
    Image("brown/walking/DLWalkL2.png")
    pause 0.15
    Image("brown/walking/DLWalkL1.png")
    pause 0.15
    Image("brown/walking/DLStanding1.png")
    pause 0.15
    Image("brown/walking/DLWalkR1.png")
    pause 0.15
    Image("brown/walking/DLWalkR2.png")
    pause 0.15
    Image("brown/walking/DLWalkR1.png")
    pause 0.15
    repeat

image brownsprite downright walk:
    Image("brown/walking/DRStanding1.png")
    pause 0.15
    Image("brown/walking/DRWalkL1.png")
    pause 0.15
    Image("brown/walking/DRWalkL2.png")
    pause 0.15
    Image("brown/walking/DRWalkL1.png")
    pause 0.15
    Image("brown/walking/DRStanding1.png")
    pause 0.15
    Image("brown/walking/DRWalkR1.png")
    pause 0.15
    Image("brown/walking/DRWalkR2.png")
    pause 0.15
    Image("brown/walking/DRWalkR1.png")
    pause 0.15
    repeat

image brownsprite upright walk:
    Image("brown/walking/URStanding1.png")
    pause 0.15
    Image("brown/walking/URWalkL1.png")
    pause 0.15
    Image("brown/walking/URWalkL2.png")
    pause 0.15
    Image("brown/walking/URWalkL1.png")
    pause 0.15
    Image("brown/walking/URStanding1.png")
    pause 0.15
    Image("brown/walking/URWalkR1.png")
    pause 0.15
    Image("brown/walking/URWalkR2.png")
    pause 0.15
    Image("brown/walking/URWalkR1.png")
    pause 0.15
    repeat

image brownsprite upleft walk:
    Image("brown/walking/ULStanding1.png")
    pause 0.15
    Image("brown/walking/ULWalkL1.png")
    pause 0.15
    Image("brown/walking/ULWalkL2.png")
    pause 0.15
    Image("brown/walking/ULWalkL1.png")
    pause 0.15
    Image("brown/walking/ULStanding1.png")
    pause 0.15
    Image("brown/walking/ULWalkR1.png")
    pause 0.15
    Image("brown/walking/ULWalkR2.png")
    pause 0.15
    Image("brown/walking/ULWalkR1.png")
    pause 0.15
    repeat


#mark
image marksprite downleft walk:
    Image("mark/walking/DLStanding1.png")
    pause 0.15
    Image("mark/walking/DLWalkL1.png")
    pause 0.15
    Image("mark/walking/DLWalkL2.png")
    pause 0.15
    Image("mark/walking/DLWalkL1.png")
    pause 0.15
    Image("mark/walking/DLStanding1.png")
    pause 0.15
    Image("mark/walking/DLWalkR1.png")
    pause 0.15
    Image("mark/walking/DLWalkR2.png")
    pause 0.15
    Image("mark/walking/DLWalkR1.png")
    pause 0.15
    repeat

image marksprite downright walk:
    Image("mark/walking/DRStanding1.png")
    pause 0.15
    Image("mark/walking/DRWalkL1.png")
    pause 0.15
    Image("mark/walking/DRWalkL2.png")
    pause 0.15
    Image("mark/walking/DRWalkL1.png")
    pause 0.15
    Image("mark/walking/DRStanding1.png")
    pause 0.15
    Image("mark/walking/DRWalkR1.png")
    pause 0.15
    Image("mark/walking/DRWalkR2.png")
    pause 0.15
    Image("mark/walking/DRWalkR1.png")
    pause 0.15
    repeat

image marksprite upright walk:
    Image("mark/walking/URStanding1.png")
    pause 0.15
    Image("mark/walking/URWalkL1.png")
    pause 0.15
    Image("mark/walking/URWalkL2.png")
    pause 0.15
    Image("mark/walking/URWalkL1.png")
    pause 0.15
    Image("mark/walking/URStanding1.png")
    pause 0.15
    Image("mark/walking/URWalkR1.png")
    pause 0.15
    Image("mark/walking/URWalkR2.png")
    pause 0.15
    Image("mark/walking/URWalkR1.png")
    pause 0.15
    repeat

image marksprite upleft walk:
    Image("mark/walking/ULStanding1.png")
    pause 0.15
    Image("mark/walking/ULWalkL1.png")
    pause 0.15
    Image("mark/walking/ULWalkL2.png")
    pause 0.15
    Image("mark/walking/ULWalkL1.png")
    pause 0.15
    Image("mark/walking/ULStanding1.png")
    pause 0.15
    Image("mark/walking/ULWalkR1.png")
    pause 0.15
    Image("mark/walking/ULWalkR2.png")
    pause 0.15
    Image("mark/walking/ULWalkR1.png")
    pause 0.15
    repeat


#elly
image ellysprite downleft walk:
    Image("elly/walking/DLStanding1.png")
    pause 0.15
    Image("elly/walking/DLWalkL1.png")
    pause 0.15
    Image("elly/walking/DLWalkL2.png")
    pause 0.15
    Image("elly/walking/DLWalkL1.png")
    pause 0.15
    Image("elly/walking/DLStanding1.png")
    pause 0.15
    Image("elly/walking/DLWalkR1.png")
    pause 0.15
    Image("elly/walking/DLWalkR2.png")
    pause 0.15
    Image("elly/walking/DLWalkR1.png")
    pause 0.15
    repeat

image ellysprite downright walk:
    Image("elly/walking/DRStanding1.png")
    pause 0.15
    Image("elly/walking/DRWalkL1.png")
    pause 0.15
    Image("elly/walking/DRWalkL2.png")
    pause 0.15
    Image("elly/walking/DRWalkL1.png")
    pause 0.15
    Image("elly/walking/DRStanding1.png")
    pause 0.15
    Image("elly/walking/DRWalkR1.png")
    pause 0.15
    Image("elly/walking/DRWalkR2.png")
    pause 0.15
    Image("elly/walking/DRWalkR1.png")
    pause 0.15
    repeat

image ellysprite upright walk:
    Image("elly/walking/URStanding1.png")
    pause 0.15
    Image("elly/walking/URWalkL1.png")
    pause 0.15
    Image("elly/walking/URWalkL2.png")
    pause 0.15
    Image("elly/walking/URWalkL1.png")
    pause 0.15
    Image("elly/walking/URStanding1.png")
    pause 0.15
    Image("elly/walking/URWalkR1.png")
    pause 0.15
    Image("elly/walking/URWalkR2.png")
    pause 0.15
    Image("elly/walking/URWalkR1.png")
    pause 0.15
    repeat

image ellysprite upleft walk:
    Image("elly/walking/ULStanding1.png")
    pause 0.15
    Image("elly/walking/ULWalkL1.png")
    pause 0.15
    Image("elly/walking/ULWalkL2.png")
    pause 0.15
    Image("elly/walking/ULWalkL1.png")
    pause 0.15
    Image("elly/walking/ULStanding1.png")
    pause 0.15
    Image("elly/walking/ULWalkR1.png")
    pause 0.15
    Image("elly/walking/ULWalkR2.png")
    pause 0.15
    Image("elly/walking/ULWalkR1.png")
    pause 0.15
    repeat
