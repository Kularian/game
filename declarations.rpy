#Character Definitions

define full = Character(_('nar'), color="#ebffbd")
define n = Character(_(' '), what_ypos=-54)
define mc = Character(_('Naoya'), color="#ebffbd", image="naoya")
define ma = Character(_('Maki'), color="#ebffbd", image="maki")
define mk = Character(_('Mark'), color="#ebffbd", image="masao")
define na = Character(_('Nanjo'), color="#ebffbd", image="nanjo")
define yu = Character(_('Yukino'), color="#ebffbd", image="yukino")
define ay = Character(_('Ayase'), color="#ebffbd", image="ayase")
define el = Character(_('Elly'), color="#ebffbd", image="elly")
define br = Character(_('Brown'), color="#ebffbd", image="brown")
define re = Character(_('Reiji'), color="#ebffbd", image="reiji")
define mai = Character(_('Mai'), color="#ebffbd", image="mai")
define aki = Character(_('Aki'), color="#ebffbd", image="aki")
define ph = Character(_('Philemon'), color="#ebffbd")
define nat = Character(_('Natsumi'), color="#ebffbd", image="natsumi")
define sa = Character(_('Ms. Saeko'), color="#ebffbd", image="saeko")
define ag = Character(_('Agastya Tree'), color="#ebffbd")
define oo = Character(_('Mrs. Ooishi'), color="#ebffbd", image="ooishi")
define ha = Character(_('Mr. Hanya'), color="#ebffbd", image="hanya")
define tm = Character(_('Tamaki'), color="ebffbd", image="tamaki")
define td = Character(_('Tadashi'), color="ebffbd", image="tadashi")
define yuko = Character(_('Yuko'), color="ebffbd", image="yuko")
define tor = Character(_('Toro'), color="ebffbd", image="toro")
define db = Character(_('Tsutomu'), color="ebffbd", image="devilboy")
define ya = Character(_('Yamaoka'), color="ebffbd", image="yamaoka")
define yao = Character(_('Old Man'), color="ebffbd", image="yamaoka")
define stu = Character(_('Student'), color="ebffdb")
define pres = Character(_('President'), color="ebffdb")
define tea = Character(_('Teacher'), color="ebffdb")
define kaneda = Character(_('Kaneda'), color="ebffdb", image="kaneda")
define yyclerk = Character(_('Clerk'), color="ebffdb", image="yyclerk")
define doctor = Character(_('Doctor'), color="ebffdb", image="doctor")
define nurse = Character(_('Nurse'), color="ebffdb")
define sec = Character(_('Secretary'), color="ebffdb")
define smd = Character(_('Shopkeeper'), color="ebffdb", image="sennenmannendo")
define pdclerk = Character(_('Clerk'), color="ebffdb", image="pdclerk")
define stclerk = Character(_('Clerk'), color="ebffdb", image="stclerk")
define jclerk = Character(_('Clerk'), color="ebffdb", image="jclerk")
define rcclerk = Character(_('Clerk'), color="ebffdb", image="rcclerk")
define tak = Character(_('Takeda'), color="ebffdb", image="takeda")
define kan = Character(_('Kandori'), color="ebffdb", image="kandori")
define set = Character(_("Maki's Mom"), color="ebffdb", image="setsuko")
define mmom = Character(_("Mark's Mom"), color="ebffdb")
define man = Character(_('Man'), color="ebffdb")
define woman = Character(_('Woman'), color="ebffdb")
define girl = Character(_('Girl'), color="ebffdb")
define lieu = Character(_('Lieutenant'), color="ebffdb")
define officer = Character(_('Officer'), color="ebffdb")
define bf = Character(_('Butterfly'), color="ebffdb")
define msk = Character(_('Mask'), color="ebffdb")
define sq = Character(_('Snow Queen'), color="ebffdb")
define reiho = Character(_('Reiho'), color="ebffdb")
define raiho = Character(_('Raiho'), color="ebffdb")
define kumi = Character(_('Kumi'), color="ebffdb")
define hypnos = Character(_('Hypnos'), color="ebffdb")
define father = Character(_('Father'), color="ebffdb")
define unknown = Character(_('Unknown Voice'), color="ebffdb")
define michiko = Character(_('Michiko'), color="ebffdb")
define mariko = Character(_('Mariko'), color="ebffdb")
define devil = Character(_('Mr. Devilish'), color="ebffdb")
define nemesis = Character(_('Nemesis'), color="ebffdb")
define yuriko = Character(_('Yuriko'), color="ebffdb")
define beast = Character(_('Large Beast'), color="ebffdb")
define cerberus = Character(_('Cerberus'), color="ebffdb")
define thanatos = Character(_('Thanatos'), color="ebffdb")
define tomomi = Character(_('Tomomi'), color="ebffdb")
define nq = Character(_('Night Queen'), color="ebffdb")
define girl = Character(_('Girl'), color="ebffdb")
define mma = Character(_('Maki?'), color="ebffdb")
define everyone = Character(_('Everyone'), color="ebffdb")


transform loc:
    xalign 0.06
    yalign 0.067

transform phase1:
    xalign 0.955
    yalign 0.105

transform phase2:
    xalign 0.919
    yalign 0.15

transform pleft:
    xalign -1.00
    yalign 1.0

transform pleft2:
    xalign 0
    yalign 1.0

transform pright:
    xalign 1.0
    yalign 0.2

transform choice1:
    xpos 700
    ypos 325

transform choice2:
    xpos 700
    ypos 500

transform choicetext:
    xpos 752
    ypos 880

transform choicetext2:
    xpos 752
    ypos 882

transform anybuttonfade:
    xalign 0.5
    yalign 0.80
    ease 1.5 alpha 0.0
    ease 1.5 alpha 1.0
    repeat

transform bottom:
    xalign 0.5
    yalign 1.0

define qdis = Dissolve(0.2)
define qleft = MoveTransition(0.2, enter=offscreenleft, enter_time_warp=_warper.easein)
define qright = MoveTransition(0.2, enter=offscreenright, enter_time_warp=_warper.easein)
define qzoom = OldMoveTransition(0.2, enter_factory=ZoomInOut(0.01, 1.0))

#define qleft2  = MultipleTransition([
#    False, Dissolve(0.2),
#    False, MoveTransition(0.0, leave=offscreenleft, enter_time_warp=_warper.easein),
#    False, MoveTransition(0.2, enter=offscreenleft, enter_time_warp=_warper.easein),
#    True])

#UI Declarations
image location = "location.png"
image location2 = "location2.png"
image phase = "phase.png"
image tp = "textprompt.png"
image text1 = "gui/textpart1.png"
image text2 = "gui/textpart2.png"

#Character Declarations
image naoya = "old/naoya.png"
image maki:
    Image ("maki/sick/serious e.png", xalign=0, yalign=1.0)

image mark ns = "mark/neutral/smirk.png"
image mark ns1 = "mark/neutral/serious t1.png"
image mark ns2 = "mark/neutral/serious t2.png"
image mark nse = "mark/neutral/serious e.png"
image mark nse1 = "mark/neutral/serious et1.png"
image mark nse2 = "mark/neutral/serious et2.png"

image nanjo = "nanjo/neutral/serious.png"
image nanjo sad = "nanjo/neutral/sad.png"
image yukino = "yukino/neutral/serious.png"
image ayase = "ayase/neutral/serious.png"
image ayase base = "ayase/neutral/base.png"
image brown ns = "brown/neutral/smirk.png"
image brown eyes = "brown/neutral/serious e.png"
image brown base = "brown/neutral/base.png"
image elly = "elly/neutral/serious.png"
image elly base = "elly/neutral/base.png"
image reiji ns = "reiji/neutral/serious.png"
image natsumi = "natsumi/neutral/smirk.png"
image saeko = "saeko/neutral/serious.png"
image ooishi = "ooishi.png"
image hanya ns = "hanya/neutrtal/serious.png"
image tamaki ns = "tamaki/neutral/smirk.png"
image tadashi = "tadashi.png"
image yuko = "yuko.png"
image toro ns = "toro/neutral/serious.png"
image devilboy ns = "tsutomu/neutral/smirk.png"
image yamaoka ns = "yamaoka/neutral/serious.png"
image kaneda = "kaneda.png"
image yyclerk = "yinyanworker.png"
image doctor = "doctor.png"
image sennenmannendo 1 = "sennenmannendo1.png"
image sennenmannendo 2 = "sennenmannendo2.png"
image pdclerk = "peacedinerclerk.png"
image stclerk = "satomi.png"
image jclerk 1 = "judgmentclerk1.png"
image jclerk 2 = "judgmentclerk2.png"
image rcclerk = "rosacandidaworker.png"
image takeda = "takeda.png"
image kandori = "kandori/neutral/serious.png"
image flair = "flair.png"
image setsuko = "setsuko.png"

#Animated Declarations
#naoya
image nchoice:
    Image("naoya/naoya choice 1.png")
    pause 1.6
    Image("naoya/naoya choice 2.png")
    pause 0.2
    repeat

#Mark
image mark animated neutral serious:
    Image("mark/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/serious et1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/serious et2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    repeat

image mark animated neutral smirk:
    Image("mark/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk et1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk e.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    repeat

image mark animated neutral sad:
    Image("mark/neutral/sad.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/sad t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad et2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/sad t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/sad et1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("mark/neutral/sad.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("mark/neutral/sad t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    repeat

#nanjo
image nanjo animated neutral serious:
    Image("nanjo/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image nanjo animated neutral smirk:
    Image("nanjo/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image nanjo animated neutral sad:
    Image("nanjo/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("nanjo/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("nanjo/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#yukino
image yukino animated neutral serious:
    Image("yukino/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/serious e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image yukino animated neutral smirk:
    Image("yukino/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image yukino animated neutral sad:
    Image("yukino/neutral/sad e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yukino/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yukino/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#ayase
image ayase animated neutral serious:
    Image("ayase/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image ayase animated neutral smirk:
    Image("ayase/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image ayase animated neutral sad:
    Image("ayase/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("ayase/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("ayase/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#brown
image brown animated neutral serious:
    Image("brown/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image brown animated neutral smirk:
    Image("brown/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image brown animated neutral sad:
    Image("brown/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("brown/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("brown/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#elly
image elly animated neutral serious:
    Image("elly/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image elly animated neutral smirk:
    Image("elly/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image elly animated neutral sad:
    Image("elly/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("elly/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("elly/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#maki
image maki animated neutral serious:
    Image("maki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image maki animated neutral smirk:
    Image("maki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image maki animated neutral sad:
    Image("maki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image maki animated sick serious:
    Image("maki/sick/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image maki animated sick smirk:
    Image("maki/sick/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image maki animated sick sad:
    Image("maki/sick/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("maki/sick/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("maki/sick/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#Reiji

image reiji animated neutral serious:
    Image("reiji/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image reiji animated neutral smirk:
    Image("reiji/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image reiji animated neutral sad:
    Image("reiji/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("reiji/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("reiji/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#NPCS

#Saeko

image saeko animated neutral serious:
    Image("saeko/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image saeko animated neutral smirk:
    Image("saeko/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image saeko animated neutral sad:
    Image("saeko/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("saeko/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("saeko/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#Kandori

image kandori animated neutral serious:
    Image("kandori/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image kandori animated neutral smirk:
    Image("kandori/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("kandori/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("kandori/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    repeat

#Yamaoka

image yamaoka animated neutral serious:
    Image("yamaoka/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image yamaoka animated bloody serious:
    Image("yamaoka/bloody/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/serious et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/serious e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image yamaoka animated bloody sad:
    Image("yamaoka/bloody/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("yamaoka/bloody/sad e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("yamaoka/bloody/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#natsumi
image natsumi animated neutral serious:
    Image("natsumi/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/serious et1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/serious et2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/serious t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/serious.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/serious t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    repeat

image natsumi animated neutral smirk:
    Image("natsumi/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk et1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk e.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/smirk t1.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    Image("natsumi/neutral/smirk.png", xalign=-0.02, yalign=1.0)
    pause 0.27
    Image("natsumi/neutral/smirk t2.png", xalign=-0.02, yalign=1.0)
    pause 0.16
    repeat

#Tamaki
image tamaki animated neutral serious:
    Image("tamaki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image tamaki animated neutral smirk:
    Image("tamaki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image tamaki animated neutral sad:
    Image("tamaki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/sad et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tamaki/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tamaki/neutral/sad t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#tsutomu

image devilboy animated neutral serious:
    Image("tsutomu/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image devilboy animated neutral smirk:
    Image("tsutomu/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image devilboy animated neutral sad:
    Image("tsutomu/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("tsutomu/neutral/sad.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("tsutomu/neutral/t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#toro

image toro animated neutral serious:
    Image("toro/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image toro animated neutral smirk:
    Image("toro/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image toro animated neutral angry:
    Image("toro/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/angry et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("toro/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("toro/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

#hanya

image hanya animated neutral serious:
    Image("hanya/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/serious t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/serious.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/serious t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image hanya animated neutral smirk:
    Image("hanya/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk et2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/smirk et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/smirk.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/smirk t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat

image hanya animated neutral angry:
    Image("hanya/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry e.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry t1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/angry et1.png", xalign=0, yalign=1.0)
    pause 0.16
    Image("hanya/neutral/angry.png", xalign=0, yalign=1.0)
    pause 0.27
    Image("hanya/neutral/angry t2.png", xalign=0, yalign=1.0)
    pause 0.16
    repeat
