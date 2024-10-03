## Custom SQQ Screens ###############################################################

screen SQHermelinFloor1:
    imagemap:
        idle "maps/HermelinFloor1.png"
        hover "maps/HermelinFloor1b.png"
        ground "maps/HermelinFloor1.png"

        hotspot (162, 224, 513, 186) action Jump("label002") #Class 1-2
        hotspot (708, 227, 511, 180) action Jump("label003") #Class 1-3
        hotspot (1249, 224, 510, 184) action Jump("label004") #Class 1-4
        hotspot (160, 434, 514, 187) action Jump("label005") #Class 1-6
        hotspot (704, 435, 517, 184) action Jump("label006") #Courtyard
        hotspot (1246, 437, 514, 189) action Jump("label007") #Teacher's Lounge
        hotspot (157, 642, 521, 191) action Jump("label008") #Principal's Office
        hotspot (704, 641, 520, 192) action Jump("label001") #Infirmary
        hotspot (1248, 644, 517, 189) action Jump("label009") #1F Passageway
        imagebutton xpos 30 ypos 435 idle "maps/MoveLeft.png" hover "maps/MoveLeftb.png" action Jump("label033") #Entryway
    imagebutton xpos 1800 ypos 435 idle "maps/MoveRight.png" hover "maps/MoveRightb.png" action Jump("callSportsBuilding") #SportsBuilding
    imagebutton xpos 925 ypos 50 idle "maps/StairUp.png" hover "maps/StairUpb.png" action Jump("callHermelinFloor2") #2f

screen SQHermelinFloor2:
    imagemap:
        idle "maps/HermelinFloor2.png"
        hover "maps/HermelinFloor2b.png"
        ground "maps/HermelinFloor2.png"

        hotspot (165, 227, 506, 178) action Jump("label018") #Class 2-1
        hotspot (708, 229, 507, 179) action Jump("label019") #Class 2-2
        hotspot (1251, 226, 505, 182) action Jump("label020") #Class 2-4
        hotspot (165, 437, 506, 182) action Jump("label021") #Class 2-5
        hotspot (1249, 435, 511, 183) action Jump("label022") #Cafeteria
        hotspot (707, 435, 509, 178) action Jump("label023") #Home Ec Room
        hotspot (706, 646, 512, 180) action Jump("label024") #Empty Classroom | Reiji

    imagebutton xpos 925 ypos 50 idle "maps/StairUp.png" hover "maps/StairUpb.png" action Jump("callHermelinFloor3") #3f
    imagebutton xpos 925 ypos 850 idle "maps/StairDown.png" hover "maps/StairDownb.png" action Jump("callHermelinFloor1") #1f

screen SQHermelinFloor3:
    imagemap:
        idle "maps/HermelinFloor3.png"
        hover "maps/HermelinFloor3b.png"
        ground "maps/HermelinFloor3.png"

        hotspot (163, 226, 510, 178) action Jump("label026") #Class 3-1
        hotspot (707, 229, 509, 179) action Jump("label027") #Class 3-3
        hotspot (1251, 230, 508, 177) action Jump("label028") #Class 3-6
        hotspot (160, 438, 508, 178) action Jump("label029") #Class 3-7
        hotspot (704, 434, 514, 181) action Jump("label030") #Library
        hotspot (1251, 437, 503, 179) action Jump("label031") #Student Council
        hotspot (706, 645, 509, 182) action Jump("label032") #Art Room

    imagebutton xpos 925 ypos 850 idle "maps/StairDown.png" hover "maps/StairDownb.png" action Jump("callHermelinFloor2") #2f

screen SQHermelinSportsBuilding:
    imagemap:
        idle "maps/SportsBuilding.png"
        hover "maps/SportsBuildingb.png"
        ground "maps/SportsBuilding.png"

        hotspot (165, 227, 503, 181) action Jump("label009") #1F Passageway
        hotspot (708, 226, 507, 182) action Jump("label011") #Gymnasium
        hotspot (1252, 226, 507, 182) action Jump("label012") #Drama Club
        hotspot (163, 435, 507, 184) action Jump("label013") #Boxing Club
        hotspot (708, 435, 508, 181) action Jump("label014") #Archery Club
        hotspot (1249, 437, 510, 176) action Jump("label015") #Fencing Club
        hotspot (707, 645, 506, 180) action Jump("label016") #Ballet Club

    imagebutton xpos 30 ypos 435 idle "maps/MoveLeft.png" hover "maps/MoveLeftb.png" action Jump("callHermelinFloor1") #1F

########Ice Castle Rooms#########

screen SQClass23a:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(3) #Hanya
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(5) #Ooishi
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQClass23b:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(3) #Hanya
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(5) #Ooishi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(6) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQClass23c:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(3) #Hanya
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(5) #Ooishi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(6) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(7) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQClass23d:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(3) #Hanya
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(5) #Ooishi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(6) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(7) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(8) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQDramaCluba:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQDramaClubb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQDramaClubc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQDramaClubd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/StudentRight.png" action Return(4) #Student
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQFencingCluba:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(3) #Tamaki
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/TadashiRight.png" action Return(4) #Tadashi
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQFencingClubb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(3) #Tamaki
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/TadashiRight.png" action Return(4) #Tadashi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQFencingClubc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(3) #Tamaki
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/TadashiRight.png" action Return(4) #Tadashi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQFencingClubd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(3) #Tamaki
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/TadashiRight.png" action Return(4) #Tadashi
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave
    imagebutton xpos 300 ypos 150 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Hypnos Tower
    imagebutton xpos 1400 ypos 850 idle "text/GreyLeft.png" hover "text/PurpLeft.png" action Return(10) #Philemon

screen SQSMDa:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(3) #Teacher
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave
    imagebutton xpos 800 ypos 500 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(9) #Clerk

screen SQSMDb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(3) #Teacher
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave
    imagebutton xpos 800 ypos 500 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(9) #Clerk

screen SQSMDc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(3) #Teacher
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave
    imagebutton xpos 800 ypos 500 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(9) #Clerk

screen SQSMDd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(3) #Teacher
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave
    imagebutton xpos 800 ypos 500 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(9) #Clerk

screen SQSTa:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQSTb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQSTc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQSTd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQWeapona:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(9) #Teacher
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(5) #Leave

screen SQWeaponb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(9) #Teacher
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQWeaponc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(9) #Teacher
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQWeapond:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/TeacherLeft.png" action Return(9) #Teacher
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQArmora:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(9) #Yuko
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(5) #Leave

screen SQArmorb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(9) #Yuko
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQArmorc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(9) #Yuko
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQArmord:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 600 ypos 560 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(9) #Yuko
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/ClerkRight.png" action Return(4) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQLibrarya:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/DevilboyRight.png" action Return(4) #Devilboy
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQLibraryb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/DevilboyRight.png" action Return(4) #Devilboy
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQLibraryc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/DevilboyRight.png" action Return(4) #Devilboy
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 885 ypos 120 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQLibraryd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/DevilboyRight.png" action Return(4) #Devilboy
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 885 ypos 120 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave
    imagebutton xpos 500 ypos 300 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(8) #Butterfly
    imagebutton xpos 200 ypos 300 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Nemesis Door


screen SQInfirmarya:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(3) #Nanjo
    imagebutton xpos 700 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(4) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/NatsumiRight.png" action Return(5) #Natsumi
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/GirlLeft.png" action Return(6) #Setsuko
    imagebutton xpos 885 ypos 120 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(7) #Student
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQInfirmaryb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(3) #Nanjo
    imagebutton xpos 700 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(4) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/NatsumiRight.png" action Return(5) #Natsumi
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/GirlLeft.png" action Return(6) #Setsuko
    imagebutton xpos 885 ypos 120 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(7) #Student
    imagebutton xpos 885 ypos 120 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(8) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(9) #Leave

screen SQCafeteria1a:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Student
    imagebutton xpos 340 ypos 550 idle "text/GreyRight.png" hover "text/ToroRight.png" action Return(4) #Toro
    imagebutton xpos 240 ypos 350 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCafeteria1b:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Student
    imagebutton xpos 340 ypos 550 idle "text/GreyRight.png" hover "text/ToroRight.png" action Return(4) #Toro
    imagebutton xpos 240 ypos 350 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 725 ypos 600 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(6) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCafeteria2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Student
    imagebutton xpos 340 ypos 550 idle "text/GreyRight.png" hover "text/ToroRight.png" action Return(4) #Toro
    imagebutton xpos 240 ypos 350 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 725 ypos 600 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(6) #Elly
    imagebutton xpos 1100 ypos 600 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(7) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClass21:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/PurpLeft.png" action Return(3) #Butterfly
    imagebutton xpos 240 ypos 350 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 725 ypos 600 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1100 ypos 600 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave
    imagebutton xpos 300 ypos 350 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Thanatos

screen SQClassrooma:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(4) #Girl
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClassroomb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(4) #Girl
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClassroomc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(4) #Girl
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClassroomd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(4) #Girl
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQJDa:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GuyRight.png" action Return(4) #Guy
    imagebutton xpos 1620 ypos 150 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(5) #Clerk
    imagebutton xpos 1090 ypos -30 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(6) #Clerk
    imagebutton xpos 1780 ypos 650 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(10) #Leave

screen SQJDb:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GuyRight.png" action Return(4) #Guy
    imagebutton xpos 1620 ypos 150 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(5) #Clerk
    imagebutton xpos 1090 ypos -30 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(6) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(7) #Elly
    imagebutton xpos 1780 ypos 650 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(10) #Leave

screen SQJDc:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GuyRight.png" action Return(4) #Guy
    imagebutton xpos 1620 ypos 150 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(5) #Clerk
    imagebutton xpos 1090 ypos -30 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(6) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(7) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(8) #Nanjo
    imagebutton xpos 1780 ypos 650 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(10) #Leave

screen SQJDd:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/StudentLeft.png" action Return(3) #Student
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GuyRight.png" action Return(4) #Guy
    imagebutton xpos 1620 ypos 150 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(5) #Clerk
    imagebutton xpos 1090 ypos -30 idle "text/GreyLeft.png" hover "text/ClerkLeft.png" action Return(6) #Clerk
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(7) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(8) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(9) #Brown
    imagebutton xpos 1780 ypos 650 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(10) #Leave

screen SQClass11a:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Guy
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClass11b:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Guy
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClass11c:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Guy
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQClass11d:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(3) #Guy
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(5) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(6) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(7) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(8) #Leave

screen SQHypnos1:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/GirlLeft.png" action Return(7) #Mariko

screen SQHypnos2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/NatsumiLeft.png" action Return(7) #Natsumi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TadashiLeft.png" action Return(8) #Tadashi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(9) #Tamaki

screen SQHypnos3:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(7) #Ooishi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(8) #Hanya

screen SQHypnos4:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQHypnos5:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/GuyLeft.png" action Return(6) #Guy
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/NatsumiLeft.png" action Return(7) #Natsumi

screen SQHypnos6:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(6) #Ooishi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(7) #Hanya

screen SQHypnos7:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TadashiLeft.png" action Return(6) #Tadashi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(7) #Tamaki

screen SQHypnos8:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/PurpLeft.png" action Return(6) #Kumi

screen SQHypnos9:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/NatsumiLeft.png" action Return(7) #Natsumi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TadashiLeft.png" action Return(8) #Tadashi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/TamakiLeft.png" action Return(9) #Tamaki

screen SQHypnos10:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/OoishiLeft.png" action Return(7) #Ooishi
    imagebutton xpos 430 ypos 700 idle "text/GreyLeft.png" hover "text/HanyaLeft.png" action Return(8) #Hanya

screen SQHypnos11:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQNemesis1:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQNemesis2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(7) #Mariko

screen SQNemesis3:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(7) #Mr Devilish

screen SQNemesis4:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQNemesis5:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQNemesis6:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQNemesis7:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQThanatos1:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQTartarus1:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(7) #Cerberus

screen SQTartarus2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(7) #Mariko

screen SQTartarus3:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQTartarus4:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(7) #Mariko

screen SQTartarus5:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQTartarus6:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQTartarus7:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQTartarus8:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQThanatos2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQThanatos3:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQThanatos4:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCourtyard:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave
    imagebutton xpos 965 ypos 525 idle "text/GreyRight.png" hover "text/SaekoRight.png" action Return(7) #Saeko

screen SQCastle1:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1100 ypos 460 idle "text/GreyLeft.png" hover "text/EllyLeft.png" action Return(3) #Elly
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(4) #Brown
    imagebutton xpos 1430 ypos 500 idle "text/GreyLeft.png" hover "text/NanjoLeft.png" action Return(5) #Nanjo
    imagebutton xpos 430 ypos 700 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle2:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(3) #Jack Frosts
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(4) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(5) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCastle3:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle4:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle5:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle6:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/GirlRight.png" action Return(3) #Mariko
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(4) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(5) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCastle7:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(3) #Jack Frosts
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(4) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(5) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCastle8:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(3) #Jack Frosts
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(4) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(5) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown

screen SQCastle9:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1265 ypos 625 idle "text/GreyRight.png" hover "text/PurpRight.png" action Return(3) #Jack Frosts
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(4) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(5) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(6) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(7) #Leave

screen SQCastle10:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle11:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle12:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle13:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle14:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle15:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle16:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle17:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyMove.png" hover "text/PurpMove.png" action Return(6) #Leave

screen SQCastle18:
    imagebutton xpos 355 ypos 450 idle "text/GreyLeft.png" hover "text/YukinoLeft.png" action Return(1) #Yukino
    imagebutton xpos 725 ypos 440 idle "text/GreyRight.png" hover "text/AyaseRight.png" action Return(2) #Ayase
    imagebutton xpos 1115 ypos 120 idle "text/GreyRight.png" hover "text/EllyRight.png" action Return(3) #Elly
    imagebutton xpos 1115 ypos 420 idle "text/GreyRight.png" hover "text/NanjoRight.png" action Return(4) #Nanjo
    imagebutton xpos 1115 ypos 720 idle "text/GreyRight.png" hover "text/BrownRight.png" action Return(5) #Brown
    imagebutton xpos 1400 ypos 850 idle "text/GreyRight.png" hover "text/GuyRight.png" action Return(6) #Kandori
