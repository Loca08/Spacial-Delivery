#  Lo script di gioco va in questo file.
#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.
 
define B = Character("Bingus Jr", color="#1bee13ff", who_outlines=[(1, "#ffffff", 1, 1)])
define P = Character("Fake Bingus?", color="#1bee13ff", who_outlines=[(1, "#ffffff", 1, 1)])
define b = Character("Bingus", color="#1bee13ff", who_outlines=[(1, "#ffffff", 1, 1)])
define d = Character("Boss", color="#140c29ff", who_outlines=[(1, "#ffffff", 1, 1)]) 
define w = Character("Random Alien Girl", color="#e045f5", who_outlines=[(1, "#ffffff", 1, 1)])
define W = Character("Wanda", color="#e045f5", who_outlines=[(1, "#ffffff", 1, 1)])
define s = Character("Random Alien Boy", color="#f7b232", who_outlines=[(1, "#ffffff", 1, 1)])
define S = Character("Seneca", color="#f7b232",who_outlines=[(1, "#ffffff", 1, 1)])
define q = Character("Random Alien Entity", color="#a1f0f0",who_outlines=[(1, "#ffffff", 1, 1)])
define Q = Character("Quasar", color="#a1f0f0", who_outlines=[(1, "#ffffff", 1, 1)])
define y = Character("[povname]", color="#297f99", who_outlines=[(1, "#ffffff", 1, 1)])
define a = Character("Random Fishy Alien", color="#2c521a",who_outlines=[(1, "#ffffff", 1, 1)])
define A = Character("Adinolfo", color="#2c521a", who_outlines=[(1, "#ffffff", 1, 1)])

define slowfade = Fade(1.0, 0, 3.0)
define midfade = Fade(1.0, 0, 2.0)
define quickfade = Fade(1.0, 0, 1.0)
define slowerfade = Fade (3.0, 0, 3.0)
define moreslowerfade = Fade(5.0, 0, 5.0)
define fastdissolve = Dissolve(0.7)
define middissolve = Dissolve(1.3)
define slowdissolve = Dissolve(2.0)
define slowerdissolve = Dissolve(3.5)
define fadehold = Fade(3.0, 1.0, 3.0)
define slowerfadehold = Fade(10.0, 0, 10.0)

define splash = "splash.png"

default wanda = 0
default seneca = 0
default quasar = 0
default adinolfo = 0

default wandas = 0
default senecas = 0
default quasars = 0
default adinolfos = 0

default monicas = 0
default monica = 0

image movie1 = Movie(channel="movie_dp", play = "images/movies/movie1.webm")
image wanda = Movie(channel="movie_dp", play = "images/movies/wanda.webm")
image seneca = Movie(channel="movie_dp", play = "images/movies/seneca.webm")
image quasar = Movie(channel="movie_dp", play = "images/movies/quasar.webm")
image adinolfo = Movie(channel="movie_dp", play = "images/movies/adinolfo.webm")
image neutral = Movie(channel="movie_dp", play = "images/movies/neutral.webm")

# Il gioco comincia qui.R
# Inzia la scena post cutscene con bingus che ti fa il colloqui.
label splashscreen:
    scene black
    with Pause(1)

    show text "D(Elivery) Group presents..." with dissolve
    with Pause(2) 

    hide text with dissolve
    with Pause(1)

    play sound "ping.mp3"

    show splash with dissolve
    with Pause(2) 

    scene black with dissolve
    with Pause(1)
    return

label start:        
    show movie1 with dissolve
    with Pause(27)
    hide movie1
    
    scene bg ufficio with quickfade
    show normal bingus
    b "Hello there, my name is Bingus, i'm going to be your new supervisor. May I ask your name human?"

    $ povname = renpy.input("So... Whats your name?", length =32)

    y "My name is [povname]."

    b "So glad to have you here [povname], here at 'Spedisco Nu Paccheeto' we are always happy to have new recruits in our big happy family!"

    y "Uh... ok I guess. So... how's the pay here ehm, Pintus? "
    hide normal bingus
    show angry bingus

    b "The name's Bingus, I would like my name not to be confused ok?"
    hide angry bingus
    show normal bingus
    b "Before that I have to ask you a couple of question for an optional survey so we can improve the service and how we approach new future recruits."
    menu:
        "I guess so":
            jump Scelta_1
        "NO":
            jump Scelta_2

label Scelta_2:
    hide normal bingus
    show confused bingus
    b "Well im gonna make you fill this out anyway, I get a little bonus for every silly question I'll ask you."

    hide confused bingus
    show normal bingus
    
    b "Anyways im gonna check yes in the box."
    hide normal bingus
    jump Scelta_1

label Scelta_1:
    hide normal bingus
    show happy bingus

    b "Very good."

    b "First question, how good of a team player are you?"
    menu:
        "The best of the best":
            jump Scelta_3
        "Good enough for this position":
            jump Scelta_4
        "What's teamwork?":
            jump Scelta_5

label Scelta_5:
    hide happy bingus
    show normal bingus
    b "Listen, im here to help you making the right decision ok?"
    hide normal bingus
    show angry bingus
    b "My patience has a limit you know?"

    b "Everything clear? Good let's continue shall we?"
    hide angry bingus
    show normal bingus
    jump Scelta_0

label Scelta_4:
    hide happy bingus
    show confused bingus
    b "Ok... love the spirit, really..."

    hide confused bingus
    show normal bingus
    b "Let's continue with the questionnaire."
    jump Scelta_0 

label Scelta_3:
    hide happy bingus
    show happy bingus
    b "Wonderful! We are having so much fun, I can't wait to finish this very ''entertaining'' task before my lunch break!"
    jump Scelta_0

label Scelta_0:
    hide happy bingus
    show confused bingus
    b "Whoa the next one must be one of the newer ones, first time ever seeing it here."
    hide confused bingus
    show normal bingus
    b "Soo next question, are you sexually active by any chance?"
    menu:
        "Yes, why you ask?":
            jump Scelta_6
        "None of your business!":
            jump Scelta_7
        "No, can we change the subject? Like for real for real?":
            jump Scelta_8

label Scelta_8:
    show happy bingus
    b "Don't worry, this is just part of the protocol. We know you have no game."

    b "Let's jump to the next question."
    hide happy bingus
    jump Scelta_6

label Scelta_7:
    b "Well its just my job after all. We know you have no game silly goose."

    b "After this wake up call, let's continue."
    hide normal bingus
    jump Scelta_6

label Scelta_6:
    show normal bingus
    b "I was going to select none regardless."
    hide normal bingus
    show happy bingus
    b "♪ Aren't you having fun? Here at 'Spedisco Nu Paccheeto' every day is as fun as your last! ♪"
    hide happy bingus
    show seccato bingus
    b "Ugh.. this stupid jingle is still stuck in my mind, but you will get over it eventually."
    hide seccato bingus
    show normal bingus
    b " Next question, do you prefer peach or lemon tea?"
    menu:
        "Peach of course!":
            jump Scelta_9
        "Lemon obviously!":
            jump Scelta_10
        "Why is this important?":
            jump Scelta_11

label Scelta_11:
    show angry bingus
    b "Well if you can't see the importance of this question im not gonna elaborate further."

    y "If you say so... everybody knows hot tea from the vending machine in the gas station is the best."
    hide angry bingus
    show seccato bingus
    b "Ugh... what a zorping loser."

    y "Excuse me? I what did you said to me?"
    hide seccato bingus
    show normal bingus
    b "Ehm... nothing I was just.. clearing my voice and thats hehe."

    y "Can we hurry up?"

    b "Of course, let me see..."
    jump Scelta_12

label Scelta_10:
    
    show seccato bingus
    b "Well if you like drinking battery acid I guess its definitely a choice."

    y "Excuse me?"
    hide seccato bingus
    show normal bingus
    b "Let's continue, so I can end my misery soon."
    jump Scelta_12

label Scelta_9:
    b "Im my opinion green tea is the best, but if you still have the taste of an infant I guess we could make it work."

    y "I wonder whats the purpose of this survey."
    
    show seccato bingus
    b "Don't ask me, im just doing my job."
    
    b "'Whispering to himself' Just 23 years to retirement, I can do this, oh my Zulone this headache is killing me."
    hide seccato bingus
    show normal bingus
    jump Scelta_12

label Scelta_12:
    b "Final and last question, Where do you see yourself five years from on?"
    menu:
        "Doing your mum.":
            jump Scelta_13
        "Doing your job but better.":
            jump Scelta_14
        "Five years older.":
            jump Scelta_15

label Scelta_15:
    
    show seccato bingus
    b "Ugh... two tablets of Zanaz are not gonna be enough for this level of pain."

    b "You don't have many friends am I right?"

    y "Sorry I was just trying to light up the conversation."
    hide seccato bingus
    show normal bingus 
    b "I think you could do a better job simply by closing your mouth, ok?"

    y "Yes sir."
    jump Scelta_16

label Scelta_14:
    show confused bingus
    b "But I still will be here five years from now."

    b "Was this some kind of human joke because it didn't make me laugh."

    y "Ok I get it, like you could have told me your funny bone was missing jeez."
    hide confused bingus
    show normal bingus
    b "All my 230 bones are perfectly fine, you just aren't funny."
    jump Scelta_16

label Scelta_13:
    show seccato bingus
    b "Which one?"

    b "Regardless, listen, if you wanted so bad to be a comedian you should have just put a red nose on your face."

    b "The clown look is already on point."

    y "....... that kinda hurts."
    hide seccato bingus
    show normal bingus
    b "Im glad to hear that bozo."
    jump Scelta_16

label Scelta_16:
    "'Static sounds coming from Bingus radio'"

    show normal bingus
    b "Do me a favor and stay quiet for a second, I think the boss is trying to contact me."

    "'Answers radio call'"
    hide normal bingus
    show normal boss 
    d "Supervisor Bingus, im calling for an update on the interview with the new recruit.........., over."
    hide normal boss
    show normal bingus
    b "Glad to hear you boss, always a pleasure. The recruit interview is going quite well, over."
    hide normal bingus
    show angry boss
    
    d "I hope for you its not well as the last one who crashed 2 of our trucks inside the cafeteria, over."
    hide angry boss
    show feared bingus
    b "Yes sir, I didn't forget about the drivers license, over."

    "'Bingus looks at you with a glacial stare'"
    
    b "You do have a driving license am I right human?"
    menu:
        "Of course I know how to drive.":
            jump Scelta_17
        "I know how to ride a bike... with training wheels.":
            jump Scelta_18

label Scelta_18:
    hide feared bingus
    show seccato bingus at left 
    b "Of course you were gonna let me down."

    b "For the love of Zubsus, don't get near the cafeteria ok?"

    y "I don't know where the heck you have the cafeteria but ok dude."
    hide seccato bingus
    jump Scelta_19

label Scelta_17:
    hide feared bingus
    show happy bingus at left
    b "Finally you said something smart and useful for once!"

    b " Still do not get near the cafeteria capisc?"

    y "Ok, thanks I guess?"
    hide happy bingus
    jump Scelta_19

label Scelta_19:
    show normal boss
    d "Supervisor Bingus do you hear me? Over."
    hide normal boss
    show normal bingus
    b "yes boss, the candidate has a drivers license, over."
    hide normal bingus
    show happy boss

    d "Perfect,I just finished signing the new recruit documents. The human is officially part of the 'Spedisco Nu Paccheeto' family. over."
    hide happy boss
    show seccato bingus
    b "Hurray... im soo happy to hear that."
    hide seccato bingus
    show happy boss
    d "Good, if you please can you direct the human to the Launching pad, so they can start the shift, over."
    hide happy boss
    show seccato bingus
    b "Sure thing boss, it'll be a pleasure for me. Over and out."

    b "You heard the boss, go to the Launching pad, follow the corridor and take the second door to the right."
    hide seccato bingus
    show angry bingus
    b "And remember do NOT enter or follow me into the cafeteria, now if you excuse me I have a tuna sandwich to eat."
    hide angry bingus
    show normal bingus
    b "Oh, I almost forgot your truck is gonna be the first one on the left, my colleague will be waiting for you in the vehicle."
    hide normal bingus
    show seccato bingus
    b "Please don't screw up."
    hide seccato bingus with dissolve
    "'Walks away'"

    y "Finally, the stupid survey its over, I hope I don't get fired on day one as my last job."

    y "Maybe mixing bleach and vinegar to clean the floors in a restaurant wasn't a good idea."

    y "I guess its time to start my shift."
    jump Scelta_20

label Scelta_20:
    scene bg camion with quickfade
    y "I think this one is the right truck, I wonder where is this colleague bingus told me about."

    "'Door opens and slams shutting'"
    show happy bingus with dissolve
    y "Bingus what are you doing here?"

    P "Gleep gloop"
    "'Hands over strange tablet'"

    y "You want me to take it?"

    P "Zorp"
    
    "'Tablets turns on'"
    P "Very good friend, now you can hear me right?"

    y "Yes but you were talking to me fine like 5 minutes ago, what's the use of this strange machine."
    hide happy bingus
    show normal bingus
    P "Well it's an intergalactic translator with over 5 gazillion language known in the universe."

    P "I still don't know how to speak properly the human dialect so Boss gave it to me just in case."

    B "Oh by the way i am not Bingus but his little brother Bingus Jr and im going to be your partner."

    y "Cool, finally someone who seems normal. Soo... what do we do now?"

    B "Well you should start first by turning on the truck with the key."

    y "Sure, ehm where is the keyhole?"
    hide normal bingus 
    show confused bingus
    B "Inside the steering wheel, have you ever drove one of this trucks before?"

    y "Yes, of course, I spent many hours driving trucks, even bigger than this one."

    y "This must be a new model I didn't have the chance to try before ahah."
    hide confused bingus
    show normal bingus

    "'Turns on the truck'"
    y "Ok now what?"

    B "Well now you have to choose where to go first, I have a couple of addresses to go through so choose."
 
    y "I get to choose?"
    hide normal bingus
    show happy bingus
    B "Yes silly, I usually pick a random address so I never know what my next destination will be, wanna try?"

    y "I'd rather not, what are the addresses Jr?"

    B " Sure thing lets see..."
    hide happy bingus with dissolve
    jump addresses

label addresses:
    menu:
        "77 Domina Ave Neptune Np 44756" if wandas ==0:
            jump wanda
        "03 Sapience Rd SW Saturn St 5689" if senecas ==0:
            jump seneca
        "404 Remsemen Street Jupiter Jp 3912" if quasars ==0:
            jump quasar
        "420 Hooters 6th Avenue Mars Mr 6996 " if adinolfos ==0:
            jump adino
        "Go back to base." if monicas ==4:
            jump ACT2

label adino:
    scene bg space with quickfade
    show normal bingus with dissolve
    y "Woah the space is so beautiful."
    hide normal bingus
    show happy bingus
    B "I know right!"

    B "Every day is full of possibilities."

    y "Really? I only thought we were just some delivery guys for a massive corporation."
    hide happy bingus
    show normal bingus
    B "That's only a small fraction of the job, the journey is the best part I must say."

    B "Once I had to follow a comet in order to arrive to a very far far away planet in a different district just outside of the Milky Way."
    hide normal bingus
    show happy bingus
    B "Best experience of my life, and you said you had a similar experience ehm... can you remind me your name?"

    y "Don't worry, my name is [povname] and no I never had something like that in my life."

    y "The closest thing I had seen related to space is the bill board for the pizza place I used to work at with a space ship on it." 
    hide happy bingus
    show confused bingus
    B "Well it's better than nothing I guess...oh I think we are close to our destination, look on your left!"
    hide confused bingus with dissolve

    scene bg adinolfoplanet with dissolve
    with Pause(2)
    scene bg aviale with dissolve
    with Pause(1)

    y "This dude must have tons of money, like look how rich and well kept is this patch of garden."

    y "Heck he got grass on Mars, that's more impressive than everything else!"
    show normal bingus with dissolve
    B "You are right but remember to be professional."

    y "Ok I will."

    B "Good luck!"
    hide normal bingus with dissolve
    scene bg aporta with dissolve
    with Pause(1)
    menu:
        "Knock on the door.":
            jump adino_1
        "Leave the package and go back to the truck.":
            jump adino_2

label adino_2:
    y "Well, on a second thought I think it's better if I leave the package here."

    y "Just wanna take all the precautions, the package is very heavy so I guess it's also fragile."
    show normal bingus with dissolve
    B "Good, make sure to place it with the label facing the top."

    y "Ok everything set correctly, let's go Jr!"
    hide normal bingus with dissolve
    scene bg space with dissolve  
    show happy bingus
    B "So were are we going now captain?"
    $ adinolfos +=1
    $ monicas +=1
    hide happy bingus
    jump addresses

label adino_1:
    "'Knocks on the door'"
    scene bg aportaopen with dissolve
    "'Door opens'"
    show bonk cat with dissolve
    a "Well, hello there! Looks like someone's got a big packawge for me. ~"

    a "If it's too heavy I could give you a hand. ~"
    "'Winks playfully'"

    y "Yeah... sure, so if you can sign here on my clipboard it's all yours."
    hide bonk cat
    show normal cat
    a "Here you go.~"

    a "Hope to see ya soon sweetie. ~"

    "'Hands over a big tip'"
    y "Thanks, have a good one sir."
    hide normal cat with dissolve
    scene bg aporta with dissolve
    with Pause(1)

    scene bg space with dissolve
    show normal bingus with dissolve
    B "So, how did it go?"

    y "Good, he gave me a big tip also."

    hide normal bingus
    show happy bingus
    B "That's very nice."

    B "So were are we going now captain?"

    $ adinolfos +=1
    $ monicas +=1
    hide happy bingus
    jump addresses

label dayend:
    show normal bingus
    y "Back to the base Jr, that was our last delivery for the day."
    hide normal bingus
    show happy bingus
    B "Cool we were faster than the programmed schedule, wanna grab something to eat in the cafeteria when we arrive? I'm starving."

    y "I don't think it's a good idea since they told me I was prohibited to go in for some reason."
    hide happy bingus 
    show normal bingus
    B "Nah it's just my brother, he says this to all the new recruits. You are gonna be fine trust me."

    y "Well if you say so."
    hide happy bingus
    jump week2

label seneca:
    scene bg space
    show normal bingus with dissolve

    y "Hey Jr, can I ask you something?"

    B "Sure [povname], what's on your mind?"

    y "Is your brother always like that with the newcomers?"
    hide normal bingus
    show confused bingus
    B "Like what?"

    y "You know, rude and very sassy to say the least."
    hide confused bingus
    show happy bingus
    B "Oh, it's normal. He is just very serious about this job, that's it hehe."

    y "You sure?"

    B " Totally, trust me."
    
    hide happy bingus 
    show normal bingus
    B "Oh look! The next destination, you should keep an eye on the path so we don't deliver to the wrong house hehe."

    y "Sure..."
    hide normal bingus
    scene bg senecaplanet with dissolve
    with Pause(2)
    scene bg sviale with dissolve
    with Pause(1)

    y "Are you sure we are at the correct house?"
    show normal bingus with dissolve
    B "Yup"

    y "This dude's house sure look like a museum."

    B "I know, I know, now deliver the package if you don't mind."
    hide normal bingus with dissolve
    scene bg sporta with dissolve
    with Pause(1)
    menu:
        "Knock on the door.":
            jump seneca_1
        "Leave the package and go back to the truck.":
            jump seneca_2

label seneca_2:
    y "I feel the pressure of someone waiting."

    y "I really don't wanna face a possibly angry costumer."
    "'Places the package next to the door'"

    y "Good, now I gotta make sure to place it with the label facing the top."

    y "Ok everything is set correctly, let's go Jr!"
    
    scene bg space with dissolve
    show happy bingus with dissolve
    B "So were are we going now captain?"
    $ senecas +=1
    $ monicas +=1
    hide happy bingus with dissolve
    jump addresses

label seneca_1:
    "'Knocks on the door'"
    scene bg sportaopen with dissolve
    "'Door opens'"
    show sene 1 with dissolve
    s "'Cogito ergo sum', it doesn't matter how hard you doubt everything, the existence of the thinking ego will remain a truth."

    s "One of my favorite passages."

    y "Well I am more of a 'Live like there is no tomorrow guy' hehe."
    hide sene 1 
    show sene 3
    s "Strange philosophy from a guy who is delivering a package late."

    s "After all 'Errare Humanum est'... am I wrong ?"
    hide sene 3
    show sene 1
    y "Sorry for that sir, so if you can sign here on the clipboard i'll go."

    s "Be careful out there, the universe is not a place for those with a weak mind."

    y "Good day sir."
    
    scene bg sporta with dissolve
    with Pause(1)

    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how did it go?"

    y "Good I think."

    hide normal bingus
    show happy bingus
    B "Better than nothing."

    B "So were are we going now captain?"

    $ senecas +=1
    $ monicas +=1
    hide happy bingus with dissolve
    jump addresses 

label quasar:
    scene bg space with dissolve
    show happy bingus with dissolve
    
    B "♪ We are going on a trip on this big mail ship. Flying trough the sky! Jr and [povname] ♪"

    y "Hey little bud I didn't know you can sing."
    hide happy bingus
    show normal bingus

    B "Gnarpies are very sociable creatures, singing is one of the many way our species interacts with each others."

    y "That explains why your brother was so upset about the jingle."
    hide normal bingus
    show feared bingus
    B "Yeah we don't talk about that."

    B "The less we think about it, the higher the chances of forgetting it."
    hide feared bingus
    show normal bingus
    y "Yeah you are right."

    B "........."

    y "............"

    B "........."

    y "............"

    B "Turn right to that asteroid, the next house will be on the left."

    scene bg quasarplanet with dissolve
    with Pause(2)
    scene bg qviale with dissolve
    with Pause(1)

    y "Damn, this place smells horrible, or is the package i'm holding?"

    y "Either way better be quick."

    scene bg qporta with dissolve
    with Pause(1)
    menu:
        "Knock on the door.":
            jump quasar_1
        "Leave the package and go back to the truck.":
            jump quasar_2

label quasar_2:
    y "Label facing up and i'm out of here."

    "'Jumps back into the truck'"
    scene bg space with dissolve
    show happy bingus with dissolve
    B "So were are we going now captain?"

    $ quasars +=1
    $ monicas +=1
    hide happy bingus with dissolve
    jump addresses

label quasar_1:
    y "Please answer quick."

    scene bg qporta with dissolve
    with Pause(1)

    q "One second, i'm coming."

    y "Hi, here is you package and here is where you need to sign so I can leave."
    scene bg qportaopen with dissolve
    with Pause(1)
    "'A sticky gelatinous hand reaches out of the door leaving a drop on the place to sign.'"

    y "Yeah, that should count, I hope."

    q "Thanks..."

    "'You hear the voice whispering behind the door'"

    q "(wait a second is this delivery guy a human!?!?!?)"

    q "(a real human being, knocked on my door!)"

    q "(for... delivering me a package!?!?!?)"

    q "(ok quiet now take the parcel, thank you and say goodbye quietly)"

    q "TTTTT...TT...THANK YOU........HAVE GOOD DAY!!"
    scene bg sporta with dissolve
    with Pause(1)
    "'Door slams'"

    y "Have a nice day you too I guess..."

    "'Runs back to the truck'"

    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how did it go?"

    y "I'm gonna tell you after we leave, I can't stand the smell of this place."

    $ quasars +=1
    $ monicas +=1
    hide normal bingus with dissolve
    jump addresses

label wanda:
    show normal bingus with dissolve 
    y "Hey Jr, I found some freeze-dried sushi in the back, do you think it tastes better in space?"
    hide normal bingus 
    show feared bingus
    B "Is that even a question?"

    y "Im always open making new experience, pass me the water so I can taste this bad boy."

    B "Im gonna get a paper bag from the utility box in the bag, just in case."

    y "Nah, im gonna be fine trust me."

    scene bg wandaplanet with dissolve
    with Pause(2)
    scene bg wviale with dissolve
    with Pause(1)

    y "I was so wrong..."

    y "I'll never eat freeze-dried sushi again."

    y "The location is definitely not helping."
    scene bg wporta with dissolve
    with Pause(1)
    menu:
        "Knock on the door.":
            jump wanda_1
        "Leave the package and go back to the truck.":
            jump wanda_2

label wanda_2:
    y "Label facing up and i'm out of here."

    "'Runs back to the truck'"
    scene bg space with dissolve
    show happy bingus with dissolve
    B "So were are we going now captain?"

    $ wandas +=1
    $ monicas +=1
    hide happy bingus with dissolve 
    jump addresses

label wanda_1:
    scene bg wporta with dissolve
    with Pause(1)
    scene bg wportaopen with dissolve
    with Pause(1)
    show cami secc with dissolve 
    w "........"

    y "Uhm hi."
    "'Stares respectfully'"
    w "I think what you are holding is mine."
    hide cami secc
    show cami normal
    y "Ehm, yes I've got a package for a “Wanda.” Address is 77 Domina Ave, Neptune."  
    
    y "just sign here on my clipboard."

    y "Perfect, hey quick question are you always this welcoming?"
    hide cami normal
    show cami secc
    w "Are you always this annoying?"
    
    menu:
        "No, ma'am. Just wanted to confirm I'm delivering to the right person.":
            jump wanda_3
        " Well, your name is on the package… unless you're hiding from the law?":
            jump wanda_4
        "Stay silent":
            jump wanda_5

label wanda_3:
    hide cami secc
    show cami normal
    W "If you say so."
    hide cami normal
    jump wanda_6

label wanda_4:
    hide cami secc
    show cami normal
    W "And if I were? Would you rat me out?"

    y "Depends on how well you tip."
    hide cami normal 
    show cami secc
    W "You are so annoying."
    hide cami secc
    jump wanda_6

label wanda_5:
    W "Just as I thought."
    hide cami secc
    jump wanda_6

label wanda_6:
    show cami secc
    W "If you are waiting for a tip it's not happening."

    W "Now get lost ok?"
    hide cami secc with dissolve 
    "'Closes door'"
    scene bg wporta with dissolve
    with Pause(1)

    y "Well I tried."

    scene bg space with dissolve 
    show normal bingus with dissolve 
    B "So you feel good now?"

    y "Kinda, let's go."

    $ wandas +=1
    $ monicas +=1
    hide normal bingus with dissolve
    jump addresses

label ACT2:
    scene bg space
    show normal bingus with dissolve
    "'Static noises coming from the radio'"
    B "Boss is calling."
    "'Answers radio'"
    hide normal bingus
    show normal boss 
    d "Bingus Jr do you hear me? Over."
    hide normal boss 
    show normal bingus
    B "Yes Boss, over."
    hide normal bingus
    show normal boss 
    d "Perfect, i'm calling to inform you and the new recruit that your shift is over, over."
    hide normal boss
    show happy bingus
    B "Really? Over."
    hide happy bingus 
    show happy boss
    d "Yes, someone didn't load all the packages on your truck and since you are too far away it's better to end your shift early, but just this time ok? Don't get comfy, over."
    hide happy boss
    show normal bingus 
    B "Thanks sir, see ya tomorrow, over and out."
    
    hide normal boss
    show normal bingus
    y "Let's a go! First day and we get to end early."
    hide normal bingus
    show happy bingus
    B "Nice, wanna go get a drink on the way back? I know a place near the moon that is the end of the world."

    y "Sure, i'm kinda low on money tho..."   
    hide happy bingus
    show normal bingus
    B "Oh don't worry it's on me this time, next one is on you."
    hide normal bingus 
    show happy  bingus
    B "Now stop talking and let's get the party started!" 
    scene black with slowdissolve
    with Pause(1)

    show text "Bingus Jr and [povname] spent some great time together that evening." with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)

    show text "They became good friend since then..." with dissolve
    with Pause(2) 

    hide text with dissolve
    with Pause(1)

    show text "[povname] still owes Jr some money. " with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)


    show text "One week later" with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)

    scene bg camion with quickfade
    y "I think i'm starting to get used to this routine."
    show happy bingus with dissolve 
    B "Good morning [povname]"
    
    y "Morning Jr, how we doing today?"

    B "Very good, I had my big coffee this morning and im ready to go."

    y "Love the spirit, were are we going today partner?"
    hide happy bingus
    show normal bingus
    B "Let's see..."

    B "Oh I think you'll recognize them."
    hide normal bingus with dissolve
    jump addresses2

label addresses2:
    menu:
        "77 Domina Ave Neptune Np 44756" if wanda ==0:
            jump wando
        "03 Sapience Rd SW Saturn St 5689" if seneca ==0:
            jump seneco
        "404 Remsemen Street Jupiter Jp 3912" if quasar ==0:
            jump quasaro
        "420 Hooters 6th Avenue Mars Mr 6996 " if adinolfo ==0:
            jump adina
        "Go back to base." if monica ==4 :
            jump ACT3

label quasaro:
    scene bg space with dissolve
    show happy bingus with dissolve
    B "♪ Cruising on down main street You're relaxed and feeling good Next thing that you know you're seeing Bingus in the neighborhood! ♪"

    y "♪ Surfing on a sound wave Swinging through the stars Take a left at your intestine Take your second right past Mars ♪"
    hide happy bingus
    show normal bingus
    B "You are getting good, one note was right this time."

    y "Thanks Jr, but I decide to stay humble."

    B "Ok mr, now turn right at the next asteroid if you please."
    hide normal bingus
    scene bg quasarplanet with dissolve
    with Pause(2)
    scene bg qviale with dissolve
    with Pause(1)

    y "This place smells terrible like last time."
    scene bg qporta with dissolve
    with Pause(1)
    "'Knocks on the door'"
    scene bg qportaopen with dissolve
    with Pause(1)
    show qua embara with dissolve
    q "Oh! y..you are the same courier from last week."

    q "B...but surely you..forgot about me hehehe..."
    menu:
        "Of course I remember you.":
            jump q1 
        "Sorry I don't remember you.":
            jump q2 

label q2:
    hide qua embara
    show qua sad
    q "............."

    q "It's ok, maybe I overacted.... my bad."

    q "Im so dumb, I'll take the parcel and leave..."
    hide qua sad with dissolve
    scene bg qporta with dissolve
    with Pause(1)
    "'Slams door'"

    q "Stupid, why did I opened my mouth, I am so embarrassed right now!"

    y "Have a nice day I guess..."
    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "I think I said something wrong, better not think about it much."

    $ quasar +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label q1:
    hide qua embara
    show qua happy
    q "... whoa you remember (he remembers me im so exited right now!!!?!?)"

    y "Yeah, is everything ok?"

    q "YES, I mean yes everything is ok"
    hide qua happy
    show qua normal

    q "I have a question are you really a human? Like from Earth?"

    y "Yup im a real human."
    
    q "Wow, I never seen one of your species from this close."

    q "I thought you were more hairy and did't wore clothes tho..."

    y "I would like you to see going around naked with how cold the space is."
    hide qua normal
    show qua sad
    q "Im sorry, I didn't mean it to sound rude I was just curious."

    y "Oh nono, I was just joking I wasn't angry."
    hide qua sad
    show qua happy
    q "Oh, thanks the stars! For a second I thought I screw up everything hehe."

    y "By the way, those that you where referring to were monkeys."
    hide qua happy
    show qua normal
    q "Monkeys, never heard of them from my researches...oh! Im so rude I didn't introduced myself im Quasar "

    y "Nice yo meet you Quasar, my name is [povname]."
    
    Q "[povname] you say, a very peculiar name. Hey I have some takeaway inside, wanna share it with me?"

    menu:
        "Sure why not.":
            jump q3 
        "Sorry I have to go now.":
            jump q4

label q4:
    hide qua normal
    hide qua happy
    show qua sad
    Q "Oh don't worry, I hope to see you soon."

    hide qua sad 
    show qua normal
    y "Have a nice day Quasar"

    scene bg qporta with dissolve
    with Pause(1)
    "'Door closes'"
    Q "The human said my name yippee!!"

    y "What a strange individual.."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, a very interesting individual I have to say."

    $ quasar +=1
    $ monica +=1
    hide normal bingus with dissolve 
    jump addresses2

label q3:
    hide qua normal
    show qua happy
    Q "Please enter and have a seat [povname]"
    hide qua happy
    scene bg qsalotto with dissolve
    with Pause(1)
    
    "'The strange odor in the air fill you lungs'"
    show qua embara with dissolve
    Q "Yeah sorry for the mess, I moved out from my parents house in order to find a job and hadn't much time to tide up the place hehe.."

    Q "This is the best place I could afford with my savings while I wait for someone to respond at my countless e-mails with my CV."
    hide qua embara
    show qua normal
    Q "I don't usually have visitors, I can't remember the last time someone entered in this house except me."
    hide qua normal
    show qua sad
    Q "I don't have many friends, or friends at all hehe..."
    hide qua sad 
    show qua normal
    Q "But hey, thats enough talking about me how about you?"

    y "Nothing much, just a delivery man trying to get to the end of the month."

    Q "Very interesting... listen I have some question to ask you and so little time..."
    "'Alarm plays somewhere in the house.'"
    hide qua normal
    show qua embara
    Q "Oh no! My noodles! I have to go, please have a seat I'll be be in a minute."
    hide qua embara with dissolve 
    "'Runs away in a hurry'"

    y "I hope the food didn't burn up, damn this place is really a mess... like I am a messy person that always forget to to the laundry and stuff but this is on a next level."

    y "It looks like some houses I'll see on 'Home and Grass Tv'"

    y "Yuck I stepped on something moist..."

    Q "Don't worry [povname] everything is going alright here."
    "'Sounds of flames erupting in the distance'"

    Q "Everything is alright, give me like five minutes max ok?"

    y "That wasn't very promising "

    y "Ugh the moist thing is all over my show, maybe I can find some tissue around somewhere, preferable one that is not used..."
    menu :
        "Look around the house.":
            jump q5 
        "Stay where you are and wait.":
            jump q6 

label q5_2:
    scene bg qsalotto with dissolve
    y "Maybe that was the real bath-room, should I go back and take a deeper look?"
    jump q6

label q6:
    y "Nah its better if I stay in the living-room, don't wanna risk stepping on something worse..."
    "'Your eyes gaze on one of the many screen in the room'"

    y "This one is showing a strange planet, lets see... it's called Sblumbo."

    y "I guess this is where Quasar comes from, this explain the slimy looks."
    show qua normal
    Q "Hey im back, soo about the food... there is a possibility that is charred beyond saving..."

    y "Oh, don't worry I wasn't that hungry. (And looking at the room... im not even sure if anything coming from this house could be edible.)"

    Q "Im so sorry, im failure and I've ruined your appetite..."

    y "No don't be so hard on yourself, you tried at least."

    Q "'Tried', like its three months that im trying to find a job here..."
    "'Grabs phone with the picture of the planet'"
    hide qua normal 
    show qua sad
    Q "I've worked so hard on my home planet in order to save up enough to finally leave and be on my own while exploring the vastness of the great cosmos."

    Q "Sometimes I wonder if I made a good decision coming here..."

    Q "I miss Sblumbo, but now its too late to go back home."

    Q "This house, it's just like me... a big pile of trash."

    y "No don't say it! You have to keep up your spirit, if not for those back on Sblumbo do it for you."

    y "Listen I too was broke as heck a week ago but I took the risk working for this company and it tuned out to be one of the best decision I made in the last 2 month."

    y "What I am trying to say is, life is hard you have to be harder got it?"
    hide qua sad
    show qua embara
    with Pause(2)
    hide qua embara
    show qua normal

    Q "Nobody before told me something like that. You human, I mean [povname] are really something else."
    "'Phone starts ringing'"

    y "Sorry it's my colleague."

    B "Hey [povname], where are you it's 10 min im waiting!"

    y "Yeah sorry, I was talking with the customer and I lost track of time."

    B "Well move then! The boss can see our movements and sure know when we are not in track got it?"

    y "Crystal clear Jr."
    "'Closes the call'" 

    y "Sorry Quasar I think i have to go now."
    hide qua normal
    show qua sad
    Q "It's ok if you leave I won't take more of your time... it was fun knowing you."
    menu:
        "Stay for a few more minutes.":
            jump q7
        "Leave.":
            jump q8

label q8:
    hide qua sad
    show qua sad
    Q "Oh don't worry, I hope to see you soon."

    hide qua sad 
    show qua normal
    y "Have a nice day Quasar"

    scene bg qporta with dissolve
    with Pause(1)
    "'Door closes'"
    Q "I made a friend yippee!!"

    y "What a strange individual.."

    "'Goes back to the truck'"
    scene bg camion
    show normal bingus
    B "So how it went?"

    y "Good, a very interesting individual I have to say."

    $ quasar +=1
    $ monica +=1
    hide normal bingus
    jump addresses2  

label q7:
    y "Don't worry Jr I'll be back soon."
    "'Winks at Quasar and closes the call.'"
    hide qua sad 
    show qua embara

    y "So you told me before you had many things to ask me."
    hide qua embara
    show qua happy
    Q "I'll start immediately!"
    hide qua happy
    show qua normal
    Q "First follow me, I need to show you something."
    scene bg qdoio with dissolve
    hide qua normal 
    show qua happy
    Q "Ok prepare yourself, ready? Ok take a look."
    hide qua happy
    scene bg qspecial with dissolve
    with Pause(2)
    show qua happy
    Q "So, what do you think?"

    y "It's very...unique I must say."

    Q "I know! I am so, SOO intrigued by your culture and traditions."
    hide qua happy
    show qua normal
    Q "I once received in the mail a Journal called Dipiù and it was a game changer for me."

    Q "I saw all the things you humans saw on daily basis."

    y "(I've never seen so much gossip magazine in my life)"

    y "Well, let's say its not only spice and drama we know back there but it's pretty close hehe."

    Q "I kinds envy you humans, despite all your flaws you always try to came out on top of every obstacles life gives you without fear."
    hide qua normal
    show qua sad
    Q "My people don't have that kind of reputation."

    Q "We for most of the galaxy are just a bunch of parasites that fucks up everything in our way."

    Q "Sometimes I feel like a worthless Amoeboid like the one from some old  video-games from centuries ago."
    
    y "You are so much more than a Amoeboid trust me Quasar."
    hide qua sad
    show qua embara

    Q "That was very sweet I must say...thanks."
    hide qua embara
    show qua happy
    Q "I think now it's time to, I've wasted enough of your time already."

    y "I'ts not a big deal I enjoy you company Quasar."
    hide qua happy
    menu:
        "Exchange phone numbers.":
            jump q9 
        "Give Quasar a handshake.":
            jump q10

label q10:
    hide qua happy
    show qua normal
    Q "It was fun knowing you."

    y "It was a pleasure to meet you. Have a great day Quasar and  see you soon."

    y "Remember here at 'Spedisco Nu Paccheeto' we always give our best for the costumer."
    hide qua normal 
    show qua happy
    Q "You are so silly, see you soon and don't forget about me ok?"

    y "I will not, goodbye."
    hide qua happy
    scene bg qporta with dissolve
    with Pause(2)
    "'Door closes'"
    Q "I made a friend, yippee!!"

    y "What a strange individual.."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, a very interesting individual I have to say."

    $ quasar +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label q9:
    hide qua happy
    show qua embara
    Q "Oh..(The human enjoys my company I am soo happy I could explode right now!)."

    y "It was a pleasure to meet you. Hey why don't we exchange phone numbers so we can keep in touch if its ok for you."
    hide qua embara
    show qua happy
    Q "YES 'clears troat' yes I would like to."
    "'You exchanges numbers'"
    Q "You are special [povname], I hope you soon and don't forget about me ok?"

    y "I will not, now i have to go back work or Jr will kill me if you don't mind hehe."

    Q "Goodbye."
    hide qua happy with dissolve
    scene bg qporta with dissolve
    with Pause(2)
    "'Door closes'"
    Q "I made a friend, yippee!!"

    y "What a strange individual.."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, a very interesting individual I have to say."

    $ quasar +=2
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label q5:
    scene bg qdoio with dissolve
    y "Everywhere I go I see piles and piles of trash."

    y "I can't even walk straight!"

    y "Maybe behind this door there is a bathroom where I can clean myself."
    scene bg qspecial with dissolve
    y "I definitely wasn't expecting something like this to be in this place."
    menu:
        "Take a closer look.":
            jump q5_1
        "Go back to the living-room.":
            jump q5_2
        "Turn around and run back to the truck.":
            jump q5_3

label q5_3:
    scene bg qsalotto with dissolve
    show qua normal
    Q "Hey im back, soo about the food... there is a possibility that is charred beyond saving..."

    y "Oh, don't worry I wasn't that hungry. (And looking at the room... im not even sure if anything coming from this house could be edible.)"

    Q "Im so sorry, im failure and I've ruined your appetite..."

    y "No don't be so hard on yourself, you tried at least."

    y "I'm sorry but i have to go now or my colleague will kill me."
    hide qua normal
    show qua sad
    Q "Oh don't worry, I hope to see you soon."

    hide qua sad 
    show qua normal
    y "Have a nice day Quasar"

    scene bg qporta with dissolve
    with Pause(1)
    "'Door closes'"
    Q "Ugh, why I can't even turn on a stove, im so dumb..."

    y "What a strange individual.."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve 
    B "So how it went?"

    y "Good, a very strange individual I have to say."

    $ quasar +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2 

label q5_1:
    y "The image in the middle seems familiar but I don't remember why..."

    y "Maybe if I get closer I can see better."
    show qua normal with dissolve
    Q "Hey what are you doing? Snooping around?"

    y "Oh no, nothing of sorts I was just looking for something to clean myself."

    Q "Oh sorry, I always forgot this place is a mess, here take this pieces of cloth."

    Q "Don't worry it's clean (or at least I think it is)."

    y "Thanks Quasar."
    hide qua normal
    show qua sad
    Q "So you found it... my secret shrine."

    Q "I know it's very weird and creepy but I can explain!"
    hide qua sad
    show qua normal
    Q "I deeply admire the ones of your kind, su much in fact I got my hands on all this human magazine in order to know more."

    y "Well, let's say its not only spice and drama we know back there but it's pretty close hehe."

    Q "Humans are such an interesting species, full of wonder and despite your flaws you always came out on top of every challenge life gives you."
    hide qua normal
    show qua sad
    Q "My people don't have that kind of reputation."

    Q "We for most of the galaxy are just a bunch of parasites that fucks up everything in our way."

    Q "Sometimes I feel like a worthless Amoeboid like the one from some old  video-games from centuries ago."
    hide qua sad
    show qua normal
    Q "I've worked so hard on my home planet in order to save up enough to finally leave and be on my own while exploring the vastness of the great cosmos."
    hide qua normal
    show qua sad
    Q "I miss home, I miss Sblumbo..."

    Q "This house, it's just like me... a big pile of trash."

    y "No don't say it, you have to be strong if not for those back on Sblumbo do it for you."

    y "Listen I too was broke as heck a week ago but I took the risk working for this company and it tuned out to be one of the best decision I made in the last 2 month."

    y "What I am trying to say is, life is hard you have to be harder got it?"
    hide qua sad
    show qua embara
    with Pause(2)
    hide qua embara
    show qua normal

    Q "Nobody before told me something like that. You human, I mean [povname] are really something else."
    "'Phone starts ringing'"

    y "Sorry it's my colleague."

    B "Hey [povname], where are you it's 10 min im waiting!"

    y "Yeah sorry, I was talking with the customer and I lost track of time."

    B "Well move then! The boss can see our movements and sure know when we are not in track got it?"

    y "Crystal clear Jr."
    "'Closes the call'" 

    y "Sorry Quasar I think I have to go now."
    hide qua normal
    show qua sad
    Q "It's ok if you leave I won't take more of your time... it was fun knowing you."

    menu:
        "Stay for a few more minutes.":
            jump q8
        "Leave.":
            jump q5_4

label q5_4:
    hide qua sad
    show qua sad
    Q "I think now it's time to, I've wasted enough of your time already."

    y "I'ts not a big deal I enjoy you company Quasar."
    hide qua sad 
    show qua happy
    Q "Even tho I can't even boil some water without starting a fire?"

    y "You're all right Quasar, remember it ok? "

    Q "........."
    menu:
        "Exchange phone numbers.":
            jump q9 
        "Give Quasar a handshake.":
            jump q10

label seneco:
    scene bg space 
    show normal bingus with dissolve

    y "Hey Bingus, sorry if I ask but... does your brother hates me?"

    B "Nah, of course not. He is just silly in other ways hehe."

    y "Well, how do you explain his criminally offensive side eye he gives me every time we see each other?"
    hide normal bingus
    show confused bingus
    B "He's just keeping an eye on you let's say."

    y "Ok, but why?"
    hide confused bingus 
    show sad bingus
    B "He doesn't like you."
    y "Why is the fact that I like the gas station tea?"
    hide sad bingus 
    show angry bingus
    B "You what?!"

    y "Ehm its just a joke, I wasn't serious. (That was close)"
    hide angry bingus
    show sad bingus
    B "So the reason why he doesn't like you is due to the fact we spent too much time together."

    B "Since our parents pass away when I was little he always tried his best to give me a good life."

    B "Even now that we are both adults, in his eyes im still his little brother."

    y "Aww that's very sweet Jr."

    y "It also explains a lot about him, maybe one of this days we can go out together so we can know each others better what do you think?"
    hide sad bingus
    show happy bingus 

    B "I think its a wonderful idea [povname], but first before planning let's finish todays shift!"
    scene bg senecaplanet with dissolve
    with Pause(2)
    scene bg sviale with dissolve
    with Pause(1)

    y "I can still feel the spiritual pressure of this house owner waiting."
    show normal bingus

    B "Yup, me too. Now deliver the package if you don't mind."

    hide normal bingus with dissolve
    scene bg sporta with dissolve
    with Pause(1)
    "'Knocks on the door'"
    scene bg sportaopen
    "'Door opens'"
    show sene 1 with dissolve 
    s "Oh, my package has finally traveled all the way through the shape of the phenomenons of the external senses."

    y "The shape of what now? Sir I just need a signature on the parcel..."

    s "My dead human, im talking about the subjective condition that allows us to use our intuition, of corse this intuition is external thus the knowledge of those so called 'External senses'."

    s "Tell me, isn't this beautiful?"
    hide sene 1
    show sene 2
    y "I think so... is this all from the works of your mind?"

    s "Immanuel Kant actually, this his from your peoples work."
    hide sene 2
    show sene 5
    s "Are you implying as a human like you doesn't know this great philosopher?!?!"

    y "No, you got it all twisted, of course I know Kant hehe.."
    hide sene 5
    show sene 1

    s "Well if you say so, I guess my reaction was inappropriate."

    s "My name is Seneca, this is the nominative I would like to be called."

    S "My real name is composed by words only individuals from my planet can pronounce."

    y "Nice to meet you Seneca, my name is [povname] and philosophy is not really my thing but I respect those who study it tho."
    hide sene 1 
    show sene 2
    S "Such nice words to hear from one of your kind."

    S "Unfortunately your race is no longer filled with elevated minds like the ones who came before you centuries ago."

    y "Thanks, I guess..."
    hide sene 2
    show sene 4
    S "If you don't mind [povname], I would like to invite you inside, so we can continue our discussion."

    menu:
        "Sure why not.":
            jump s1 
        "Sorry I have to go now.":
            jump s2

label s2:
    show sene 4
    S "Don't worry, It was my mistake interfering with your work."

    S "I hope you have a good day."
    hide sene 4
    show sene 2
    y "Have a nice day sir."

    scene bg qporta with dissolve
    with Pause(1)
    "'Door closes'"

    y "I feel more conscious about myself now, very weird. "

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, a very interesting individual I have to say."

    $ seneca +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2    

label s1:
    show sene 1
    S "Please be my guest [povname]"
    hide sene 1
    scene bg ssalotto
    with Pause(1)
    show sene 3
    y "Woah, I like your interior design. I see you have many manuscripts impressive."

    S "Thanks for the compliment, I collect them in my free time so I can expand my knowledge."
    
    y "I imagine its very rewarding having this many books and the fact you probably read all of them at least once I guess."
    hide sene 3
    show sene 4
    S "My dream is to build in the future a new LIbrary of Alexandria so knowledge will be accessible to all who seek enlightenment."

    S "My mission is similar to those who recite Hippocrates oath."

    S "I can't turn my back to those who looks for knowledge without the resources."

    y "That's very honorable Seneca."
    hide sene 4
    show sene 2
    S "If you don't mind I have to take care of some business inside the library, I'll be back soon."

    S "You can wait for me in the living-room."
    hide sene 2 with dissolve

    y "This house is filled to the brim with cool stuff, maybe he wouldn't mind if i take a peek in his absence."
    menu:
        "Stay where you are.":
            jump s3 
        "Take a look around the house":
            jump s4 

label s3:
    y "No I have to be strong, Seneca told me to stay here so I will."

    y "I can wait while reading one of the books laying around here."

    y "This guy sure love also lifting, I bet all the other rooms are filled with books and weights."

    y "Knowledge must be a heavy burden to carry around hehe."
    show sene 1 with dissolve
    S "[povname] im back, forgive me what I had to to took more time than planned."

    S "If you don't mind I would like to show you something, since you proved yourself to be a thoughtful individual."
    hide sene 1
    show sene 4
    y "I'll be glad to Seneca, please show me the way."
    "'Phone starts ringing'"

    y "Sorry it's my colleague."

    B "Hey [povname], everything is alright?"

    B "You are taking longer than usual delivering the package, do you need some help?"

    y "Yeah sorry, I was talking with the customer and I lost track of time."

    B "Well move then! We don't have all day to complete the all deliveries ok?"

    y "Crystal clear Jr."
    "'Closes the call'" 

    y "Seneca I think I have to go now."
    hide sene 4
    show sene 1
    S "It's ok if you leave I won't take more of your time, it was delightful getting to know you."
    menu:
        "Stay for a few more minutes.":
            jump s5 
        "Leave.":
            jump s6 

label s6:
    hide sene 1
    show sene 2
    S "I hope to see you soon, maybe we can continue our conversation while training our bodies."

    S "Its 'Mens sana in corpore sano' after all."

    hide sene 2
    show sene 1
    y "Have a nice day Seneca"
    scene bg sportaopen with dissolve
    scene bg sporta with dissolve
    with Pause(1)
    "'Door closes'"

    y "I should come back, I really like his company."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, a very mindful individual I have to say."

    $ seneca +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2 

label s5:
    y "Don't worry Jr I'll be back soon."
    "'Winks at Seneca and closes the call.'"
    hide sene 1
    show sene 1

    S "Despite I do not condone lying I'll make and exception this time, please follow me."
    scene bg sdoio with dissolve 
    show sene 1
    S "Here, behind this door I can show you the product of my work."
    hide sene 1
    scene bg sspecial with dissolve
    with Pause(1)
    show sene 1 
    S "Here I present you Project Hermes, the biggest library the universe has ever seen."

    S "Despite time is internal and not external, I still have a long way before I can call it complete."

    y "Let me guess, it's Kant again right?"
    hide sene 1
    show sene 2
    S "For Kant time and space are parallel in concept despite one being exterior to the mind and the other interior."

    S "It's fascinating at the beginning it can seem troublesome, as Kant put it you can say what you want on pietism but the education and the intellectual discipline gain from that type of information was impeccable."

    y "Well, isn't it obvious due to his philosophical discoveries?"

    y "You know, sometimes I feel like despite the low knowledge I have that philosophy predated science."
    hide sene 2
    show sene 4
    S "Of course it did, after all science is philosophy and philosophy is also math. Can you see the link?"

    y "Uhm.. I think so, yes."

    S "Philosophy is a logical language, you cannot come to illogical or surreal conclusion if used correctly."
    hide sene 4
    show sene 3

    S "The same happens with math, since its based on axioms and logic."

    S "Think about Democritus and his atom. He lived during ancient greece, on your small planet and despite this he theorized the atom way before John Dalton in the nineteenth century."

    y "Now it kinda sounds like magic if you put it this way."

    S "Haha my child, you can call philosophy magic if you want but its just a simple and logic use of culture which contains every knowledge."

    y "Still, talking about the library its massive!"
    hide sene 3
    show sene 1 
    S "Be free to consult whichever book you find interesting. It's my personal library but it's open for everyone looking for knowledge."

    S "Im against entry fees, I only accept donations in order to expand this project."

    y "Project Hermes you said right? Can you tell me more about it?"
    hide sene 1
    show sene 5

    S "I called it after Hermes Trismegistus, for me it's like point in common between opposites."

    S "Usually on your planet, the more culture flourishes the more conflict arise and fights broke out between opposite ideologies even tho those should be the one to be in peace like it happened on my home planet."

    S "As within so without, like the smallest so is the biggest."

    y "Im starting to understand it now. You know we human are very emotional creatures, we lose our temper when we are under pressure and often we confuse our work with our identity."

    S "From where I came our people transcended emotion this is why I express myself using my body so that you can understand me better."

    y "(Ah, so that was the reason why he wouldn't stop flexing in front of me)"
    hide sene 5
    show sene 4
    y "Despite this, many humans live like they are on a different and lower plane of consciousness."

    S "That's because each one of you has freedom to do and think what they please, your specie don't 'force' a progressive way of thinking in fact it does the exact opposite in order to secure your survival."

    S "It's very peculiar how in modern times you still prefer to run away from knowledge and dialogue labeling those as a danger to your survival."
    hide sene 4 
    show sene 1
    y "Now I am very curious, since you are such an open minded individual can I ask what you bought?"

    S "I got some new weights for my home gym of course!"
    hide sene 1
    show sene 3
    with Pause(1)
    hide sene 3

    show sene 1
    y "Weights? I thought you were build like that by nature! So you are also a gym rat other than an erudite."

    S "Of course my friend!"
    hide sene 1
    show sene 3
    with Pause(1)
    hide sene 3
    show sene 1
    S "'Mens sana in corpore sano' am I right?"

    y "Your philosophy doesn't bat an eyelid."

    S "Training your body is a mental exercise as much as studying, despite not looking like it."

    S "Have you ever experienced while studying a flow state the same does the body during the workout."

    y "So consistency is the key."

    S "Exactly my disciples."
    hide sene 1
    show sene 3
    with Pause(1)
    hide sene 3

    show sene 1
    y "You are a really talented and intelligent individual, I would be honored to learn more with your guide."

    "'Seneca blushes softly'"

    S "Thanks for the kind words [povname], it's a pleasure for me helping the ones in need. I too have to thank you [povname]."

    y "For what?"

    S "It was fun talking to you, your identity and your intuitions. You are a really precious individual for me, never forget this."

    y "Thank you Seneca."
    hide sene 1
    show sene 3
    S "Remember to come back soon ok?"
    "'Winks playfully'"

    y "Hey why don't we exchange phone numbers so we can keep in touch if its ok for you."
    hide sene 3
    show sene 2
    S "Sure let's keep in touch."

    "'You exchanges numbers'"
    y "I guess it's time for me to go now before my colleague kills me hehe."

    S "Goodbye then [povname]."

    hide sene 2
    scene bg sportaopen with dissolve
    scene bg sporta with slowdissolve
    with Pause(2)
    "'Door closes'"

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, my mind feel more enlightened now hehe."

    $ seneca +=2
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label s4:
    y "Let's take a look."
    scene bg sdoio with dissolve

    y "This house looks like a museum both outside and inside."

    y "I wonder what inside this room."
    scene bg sspecial with dissolve
    with Pause(1)

    y "Woah, this place is massive."

    y "I wonder what this books can contain."
    "'The book you chose was heavier than expected an slip from your hands with a loud thud'"
    show sene 1
    S "STOP RIGHT THERE YOU CRIMINAL SCUM!"

    y "Oh gosh, im sorry I was curious I didn't mean it."

    S "HUMAN, HOW DARE YOU DESECRATE THE CRADLE OF KNOWLEDGE AND RESTORED WISDOM?"
    
    S "THE LEGITIMATE HEIR OF THE LIBRARY OF ALEXANDRIA?? HOW DARE YOU DEPRIVE OTHER FORMS OF LIFE OF MERCIFUL CULTURE?"

    S "FILTHY BEING, TRAITOR OF MY OWN TRUST "

    S "GET OUT!!"
    hide sene 1
    "'You silently exit the house without saying a word.'"

    scene sportaopen with dissolve
    scene sporta with dissolve
    with Pause(1)

    "'Door slams shut.'"

    "'Goes back silently to the truck.'"
    scene bg camion
    show normal bingus
    B "So how it went?"
    hide normal bingus

    show confused bingus
    y "Let's not talk about it ok? Im not in the mood."

    $ seneca +=1
    $ monica +=1
    hide confused bingus 
    jump addresses2

label adina:
    scene bg space
    show normal bingus with dissolve
    B "Hey, I remember this address. Isn't it the one where the rich guy lives that lent you the big tip the last time?"

    y "You are right Bingus, this is the guy with the grass on Mars!"

    y "How do I look? I wanna do a good impression so he's gonna tip me again."
    hide normal Bingus
    show confused bingus

    B "You look like someone who can't drink a cup of coffee without spilling it on his shirt."
    hide confused bingus 
    show normal bingus
    B "The rest is fine I guess."

    y "Crap, I didn't saw it, hope he's not gonna notice it."

    y "While I try to remove it can you take the wheel for a second please?"
    "'Leaves the steering wheel to grab a napkin'"

    hide normal bingus
    show feared bingus
    B "Wait im not ready."

    "'Grabs the steering wheel in a panic'"
    hide feared bingus
    show angry bingus
    B "Don't you ever try doing something stupid like that!"

    y "Chill little dude, I know what I was doing."

    y "Im gonna offer you some tea from the cafeteria to forgive me ok Jr?"
    hide angry bingus
    show normal bingus
    B "With the gold fish biscuits?"

    y "Yes with the biscuits."
    hide normal bingus
    show happy bingus
    B "Ok we are even now."
    hide happy bingus
    show angry bingus
    B "Try doing something like that again and im gonna launch out of the windshield the next time ok?"

    y "Got it."
    hide angry bingus
    show happy bingus 
    B "Good, I think we arrive at our destination look!"

    hide happy bingus
    scene bg adinolfoplanet with dissolve
    with Pause(2)
    scene bg aviale with dissolve
    with Pause(1)
    show normal bingus with dissolve 
    B "Remember calm and professional"

    y "Ok I will."

    B "Good luck!"
    hide normal bingus with dissolve
    scene bg aporta with dissolve
    with Pause(1)

    "'Knocks on the door'"
    scene bg aportaopen with dissolve 
    "'Door opens"
    show bonk cat with dissolve
    a "Well, hello there! Looks like someone's came back.~"

    y "Yes sir, if you can sign my parcel it's all yours."

    a "Sure thing sweetie"
    "'Signs the parcel'"

    y "You have a really nice house I must say. Seeing grass on Mars is really something I never thought I would see in my lifetime."

    a "It's nothing just my vacation house, I have like five other in this Solar system."

    y "(Six vacation houses, man this guys its astronomically rich!)"

    a "Yeah, I know its not much I would have liked to have one for each planet of this solar system."
    hide bonk cat
    show sad cat
    a "Unfortunately, there are not many houses to by on Neptune and Venus for sale."
    hide sad cat
    show silly cat

    a "So im trying to buy both planet hehe.~"
    "'You stares in shock'"

    a "Since you seem to have a taste for nice things, how about you come inside and take a look?~"

    menu:
        "Accept the invite.":
            jump a1 
        "Refuse in a polite way.":
            jump a2

label a2:
    hide silly cat
    show sad cat
    a "Don't worry, maybe another time."
    hide sad cat 
    show silly cat
    a "I hope you have a good day sweetie.~"
    
    y "Have a nice day sir."
    hide silly cat with dissolve
    scene bg qporta with dissolve
    with Pause(1)
    "'Door closes'"

    y "Oh, he didn't leave a tip this time."

    y "Well, better go back to work then."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Meh, no tip maybe another time Jr."

    $ adinolfo +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2 

label a1:
    hide silly cat
    show happy cat
    a "Oh my gosh, im so happy right now please follow me hehe"

    hide happy cat with dissolve
    scene bg asalotto with dissolve
    with Pause(1)
    
    show normal cat with dissolve
    a "So this is my martian vacation house, its my favorite of the six I have."
    hide normal cat
    show sad cat
    a "But first, im a terrible host I haven't introduced myself."
    hide sad cat
    show silly cat

    A "Nice to meet you my name is Adinolfo, what's yours?~"

    y "My names is [povname]."

    A "[povname]... I had a pet dodo named [povname] he was so cute with his big yellow nose."
    hide silly cat
    show sad cat
    A "It's a shame birds cannot stand intergalactic travel at hyperspeed..."

    y "Wait how did you had a pet dodo, weren't those extinct?"

    hide sad cat
    show normal cat
    A "Father got me one for my birthday, he is the best!"

    y "Can you remind me who your father is Adinolfo?"
    hide normal cat
    show silly cat
    A "Oh his name is Elon Adinolfo Senior Musk."

    y "(Elon!?!?! Elon Musk!?! Gosh I thought he was joking when he told me he's looking to buy Neptune and Venus but he is not kidding!)"

    y "That is soo cool, I would have never guessed."

    A "Yeah I get this a lot."
    hide silly cat
    show normal cat
    
    A "So now that we introduced each others, tell me do you like my place?"

    y "Yeah, it's very cozy."

    A "I know right! I really like the interior design of human houses ,so I asked my dad to hire a famous human designer to set up the place."

    y "And what was his name?"

    A "I think he was called Philippe Starck."

    y "(The more he talks, the more I can feel my poverty)"

    y "(My bank account is still red from last Xmas)" 

    y "That's very nice I love it."

    A "You haven't seen anything, I see you have a good eye why don't we talk more in front of a cup of cherry blossom and mango tea?"
    "'Adinolfo's phone starts ringing'"
    hide normal cat
    show silly cat
    A "Sorry is my dad calling, maybe he has some news on the planet transaction thingy hehe."

    A "Wait for me, I'll be back soon sweetie.~"
    hide silly cat with dissolve
    "'Walks away'"

    y "Man this dude is really a money printing machine."

    y "He is really humble tho I have to say."
    menu: 
        "Take a look around the house":
            jump a3
        "Stay where you are":
            jump a4
        
label a3:
    y "I wonder what other things this guy has."

    y "He probably wouldn't mine if i take a quick sneak peek."

    scene bg adoio with dissolve
    y "Oh whats that at the end of the corridor?"

    scene bg aspecial with dissolve
    y "Strange decor but I must say it's very demure."
    show happy cat with dissolve
    A "Im baaack!! Daddy finally bought me the planet I longed for sooo many years! I'm soooo happy!!"
    
    y "Wow! Glad to hear that! (this guy is DEFINITELY richer than the Rothschild family)"
    
    A "Now, where were w- AAAA"
    hide happy cat with dissolve
    "'Trips'"

    y "Oh! Hey! A-are you ok??"
    show normal cat with dissolve
    A "Ouch, don't worry, I just fell off, these carpets are the best to fall o-ooOOOOO NOOOOOOOO!!!!!"
    hide normal cat 
    show sad cat
    y "WHAT??? WHAT HAPPENED??"

    A "MY, MY, MY… MY NAAAAAAAAIIIIIL WAAAHHH"

    y "(oh my god how do you console someone who… simply broke a nail?)"

    y "Uhm… No Adinolfo, don't worry, it's just a nail!"

    A "JUST A NAIL??? JUST A NAIL YOU SAY?? DO YOU KNOW HOW MUCH WORK AND MONEY ARE BEHIND *MY* NAILS?????"

    y "(Oh shit)"

    A "HOW DARE YOU MINIMIZE THE IMPORTANCE OF MY NAILS YOU DUMB HUMAN!!!!"

    y "No really I didn't want to.."

    A "(sob sob) You're so mean, why are you saying such things… sniff sniff"

    y " No Adinolfo, I'm sorry, you're beautiful even if your nail is broken!"
    
    A "SHUT UP!! GO OUT!!! OR I WILL CALL MY FATHER OKKK???? WAAAAHH"

    y "(woah I think it's best for me to go out without saying anything)"  
    hide sad cat with dissolve
    "'You silently exit the house without saying a word.'"

    scene aportaopen with dissolve
    scene aporta with dissolve
    with Pause(1)

    "'Door slams shut.'"

    "'Goes back silently to the truck.'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"
    hide normal bingus

    show confused bingus
    y "Let's not talk about it ok? Im not in the mood."

    $ adinolfo +=1
    $ monica +=1
    hide confused bingus with dissolve
    jump addresses2

label a4:
    y "Looking around I can see many things from the twentieth century."

    y "I know this thing from my history class in highschool."

    y "Look! Its a library full of burned cds!"

    y "They are all neatly stored let's see."

    y "There are some David Bowie, Caparezza, Queens and Pavarotti."

    y "Never heard of those guys, I guess they are famous if Adinolfo has their music."
    show silly cat with dissolve

    A "Heeey, im back and I have some great news!"

    y "Woah tell me more."
    hide silly cat
    show normal cat
    A "So father told me he wasn't able to buy Venus but he get Neptune!"

    y "(I feel threatened in some way, if his dad can buy a planet what else can he do?)"

    y "Thats wonderful Adinolfo."

    A "I know right! Now I can live on the same planet as my favorite streamer xX.Gorgon_Nya.Xx she is suck an icon!"

    y "And what does she do exactly?"

    A "She talks about old and forgotten creepypastas from the twenty-first century like Smiling dog.jpeg and Ted the caver."

    y "Never heard of those but they sounds interesting."
    hide normal cat
    show silly cat
    A "Im gonna show you my creepypastas collection one of this days, I have some ancient texts from 2014 translated from Albus the white."
    "'Phone starts ringing'"

    y "Sorry it's my colleague."

    B "Hey [povname], everything is alright?"

    B "You are taking longer than usual again, are you stuck or something?"

    y "Yeah sorry, I was talking with the customer and I lost track of time."
    hide silly cat
    show normal cat
    A "Is he your colleague? He sound cute on the phone."

    B "Well move then! We don't have all day to complete the all deliveries ok?"

    y "Yes, I know no need to remind me."
    "'Closes the call'" 
    hide normal cat 
    show sad cat
    y "Sorry Adinolfo I have to go now."

    A "It's ok if you leave I won't take more of your time, it was nice getting to know you."

    menu:
        "Stay for a few more minutes.":
            jump a5 
        "Leave.":
            jump a6 
    
label a6:
    hide sad cat
    show normal cat
    A "Oh don't worry, I hope to see you soon."

    y "Have a nice day Adinolfo"
    hide normal cat 
    show silly cat
    A "Come back visiting soo sweetie."
    scene bg aportaopen with dissolve 
    scene bg aporta with dissolve
    with Pause(1)
    "'Door closes'"

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, big reality check but he's a nice guy."

    $ adinolfo +=1
    $ monica +=1
    hide normal bingus with dissolve 
    jump addresses2  

label a5:
    hide sad cat
    show normal cat
    y "Don't worry Jr I'll be back soon."
    "'Winks at Adinolfo and closes the call.'"
    hide normal cat
    show happy cat

    y "So you told me before you had to show me some things right?"

    A "Follow me!"
    hide happy cat
    show normal cat
    A "I know I promised you the creepypastas but I have something better to show you."

    scene bg adoio with dissolve
    hide normal cat
    show silly cat with dissolve 
    A "Ok prepare yourself, ready? Ok take a look."

    hide silly cat
    scene bg aspecial with dissolve
    with Pause(2)
    show happy cat with dissolve
    A "So, what do you think?"  
    
    y "Very unique, I have no words to describe it."

    A "It's my little oasis on Mars."

    y "You really have some good taste, I love the statue."
    hide happy cat 
    show silly cat
    
    A "Thanks, it was a gift I got after my last big charity event."

    y "I didn't know you are also a philanthropist."
    hide silly cat
    show normal cat

    A "I try doing my part, I was lucky to be born in a life of luxury so I try to share this gift with the ones in need."

    y "That's very deep, sorry to ask but what did you donate?"

    A "Well once I gifted three hundred thousand colorful thigh high socks to an orphanage."

    A "Oh and another time I gift four hundred thousand Fiji water bottles to a poor village in Kenya."
    hide normal cat
    show silly cat
    A "But my favorite one was building an internet cafe for the homeless in Downtown Boston."

    y "I have to admit you are kinda crazy, but I really love your spirit and ideas."

    y "Your dedication it's truly something I admire."

    A "Aww you are making me blush."
    hide silly cat 
    show sad cat

    A "You know, im not usually this talkative."
    hide sad cat 
    show happy cat
    A "But with you I feel safe in a way."

    A "You know I would really appreciate if you come visit me again."

    menu:
        "I will be glad to":
            jump a7
        "Sorry but I think you are going too fast":
            jump a8

label a8:
    hide happy cat
    show sad cat

    A "Oh, sorry I may have skipped some steps."

    A "Can we be friends?"

    y "Sure I'll be glad to Adinolfo"
    hide sad cat 
    show happy cat

    y "I have to go now or my colleague will kill me."
    hide happy cat
    show normal cat

    A "It was fun knowing you."

    y "I enjoyed you company. Have a great day Adinolfo."

    y "Remember here at 'Spedisco Nu Paccheeto' we always give our best for the costumer."

    A "You are so silly sweetie goodbye."

    y "Goodbye."
    hide normal cat
    scene bg aportaopen with dissolve
    scene bg aporta with dissolve
    with Pause(2)
    "'Door closes'"

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, it was an experience I have to say."

    $ adinolfo +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label a7:
    hide happy cat
    show happy cat 

    A ".......'Blushes'"

    A "Oh, sorry I may have skipped some steps."
    hide happy cat
    show normal cat
    A "So I guess we are friends now?"

    y "Sure I'll be glad to be Adinolfo"

    y "I have to go now or my colleague will kill me."
    hide normal cat
    show happy cat
    A "It was fun knowing you."

    y "I enjoyed you company. Have a great day Adinolfo."

    y "Remember here at 'Spedisco Nu Paccheeto' we always give our best for the costumer."

    A "You are so silly sweetie goodbye."

    y "Goodbye."
    hide normal cat
    scene bg aportaopen with dissolve
    scene bg aporta with dissolve
    with Pause(2)
    "'Door closes'"

    A "I got a friend!!!"

    A "And I didn't had to pay, this must be serious business yippee"

    y "Hehe , I like this guy."

    "'Goes back to the truck'"
    scene bg space with dissolve
    show normal bingus with dissolve
    B "So how it went?"

    y "Good, it was an experience I have to say."

    $ adinolfo +=2
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label wando:
    show normal bingus with dissolve 
    y "Hey Jr, I got some blue cheese and maize porridge for lunch wanna try?"
    hide normal bingus 
    show feared bingus
    B "Is that even a question?"

    y "You know im always open making new experience."

    B "Like the freeze dried sushi from last time?"

    y "That was on me I admit, I'll never try something like that again."

    B "Im gonna get a paper bag from the utility box in the bag, just in case."

    y "Nah, im gonna be fine trust me."

    y "This is some real Italian expertly crafted made delicacy."
    hide feared bingus
    show seccato bingus
    B "And where did you got this delicacy?"

    y "From the gas station."

    B "Im gonna get a bigger paper bag." 

    scene bg wandaplanet with dissolve
    with Pause(2)
    scene bg wviale with dissolve
    with Pause(1)

    y "I was so wrong...again!"
    scene bg wporta with dissolve
    with Pause(1)

    "'Knocks on the door'"

    "'Doors open'"
    scene bg wportaopen with dissolve
    with Pause(1)

    show cami normal with dissolve
    W "Oh, it's you again. Are you perhaps the only delivery guy on duty or are you coming here on purpose?"

    y "Just doing my job ma'am, I've got another package for you."

    y "Just sign here on the clipboard and I'll be on my way back ok?"

    W "Sure as long as you leave me alone."

    "'Signs parcel'"

    W "Now if you don't mind, would you min bring that heavy package inside."

    y "No problem ma'am"
    
    y "(Gosh this lady manners are tougher to stand than the food I had before)" 
    hide cami normal 
    show cami secc
    W "Good, don't make me regret asking for help."
    menu: 
        "Follow her inside.":
            jump w1 
        "Drop the package past the entrance.":
            jump w2 

label w2:
    W "You're not as helpful as I thought."

    y "Thanks, I guess..."

    W "Next time don't just drop my stuff and call it a day."

    y "Alright, I'll go then."
    hide cami secc with dissolve 
    scene bg wportaopen with dissolve
    scene bg wporta with dissolve
    "'Goes back to the truck'"
    
    with Pause(1)
    scene bg space with dissolve
    show normal bingus with dissolve
    B "Good you are back, so partner what's gonna be our next stop?"

    $ wanda +=1
    $ monica +=1
    hide normal bingus with dissolve
    jump addresses2

label w1:
    hide cami secc
    scene bg wsalotto with dissolve
    show cami normal with dissolve
    W "You can put it on the table there in the corner."

    y "No problem, I've got this."

    W "Thanks, I don't usually let people inside but, since you are not totally worthless, I'll make an exception."

    y "I can see from the decor that you are not lying."

    W "What did you say?"

    y "Ehm nothing, I said the decor its very unique hehe..."

    W "Unique you say, uh?"

    y "(Unique in the Addamns family way...)"

    W "I like dark and gloomy things, it reminds me of home."

    y "You know, I too have a similar style in my apartment."

    W "For real?"

    y "Yeah its probably because I haven't paid my eclectic bills in a while."
    hide cami normal 
    show cami secc

    W "........"

    y "My bad, what I wanted to say is I too know the feeling of needing a place you can call you own."
    hide cami secc
    show cami normal

    W "I came here for my job, I moved a lot since I became a famous streamer."

    W "Intergalactic doxing is getting really out of hand in the last years."

    y "Oh you are a streamer? I would have never guessed."

    W "Not to brag but im a internet celebrity with over three million followers, online I am known as xX.Gorgon_Nya.Xx."
    hide cami normal
    show cami happy
    y "Oh now I remember! I know you seemed familiar."
    hide cami happy 
    show cami normal
    W "Well since you seem to be a fan and you helped me with the package I guess you deserve an autograph."

    W "Wait for me here, I'll be back soon."
    hide cami normal 
    show cami secc

    W "Don't overstate your welcome ok?"

    y "Don't worry I'll stay put like a statue."
    hide cami secc with dissolve
    menu:
        "Stay where you are.":
            jump w3 
        "Take a look around the house.":
            jump w4 

label w3:
    y "Alright, I'll stay right here. No touching. No snooping. Just... a delivery guy standing awkwardly inside a house that could be a circus attraction."

    y "At least the furniture isn't growling at me... yet."

    y "I hope she is not like one of those Hello Kitty girls I heard about."

    y "My buddy Pierre once date one, he needed a year of physical and mental therapy to move over after what she did to him."
    show cami normal with dissolve
    W "Im back, wow you actually stayed put."

    W "You'll make a decent gargoyle not gonna lie."

    y "I'll take that as a compliment."
    hide cami normal
    show cami secc
    W "As you should."
    hide cami secc
    show cami normal
    W "Anyway, thanks for not wrecking anything while I was gone you're not as hopeless as I thought after all."

    W "But you'll need to shoot higher than to impress me."
    "'Phone starts ringing'"

    y "Sorry it's my colleague."

    B "Hey [povname], where are im waiting!"

    y "Yeah sorry, I was talking with the customer and I lost track of time."

    B "Well move then! The boss can see our movements remember."

    y "Crystal clear Jr."
    "'Closes the call'" 

    y "I think i have to go now."

    Q "It's ok if you leave I won't take more of your time... it was fun knowing you."
    menu:
        "Stay for a few more minutes.":
            jump w5
        "Leave.":
            jump w6

label w5:
    y "You know what? Work can wait. I'll stay a little longer."
    hide cami normal
    show cami happy
    W "Seriously?"
    hide cami happy
    show cami normal
    W "Well, don't think I'm impressed or anything. You probably just don't want to deal with your boss, right?"

    y "What can I say? I like your company and your place is very unique"
    
    y "Like you."
    hide cami normal
    show cami secc
    W "That was nauseatingly sweet, but thanks."
    hide cami secc
    show cami normal 

    W "But thanks..."

    W "Fine. What do you want to know?"

    y "Let's start with the obvious. Why all the plushies? I mean, they're cool but why so much of them?"

    W "I like them, okay? They're... comforting. They remind me of when things were simpler."

    y "That makes sense. You've got good taste, too. Especially Kuromi over there."

    W "You know who Kuromi is?"

    y "Of course I know who she is."

    W "Huh. Maybe you're not so bad after all."

    W "But don't get any ideas. You're still just a delivery guy."

    y "A delivery guy who is bold enough to talk to you though."

    W "...Yeah. I noticed."

    W "My job is very hard, I usually don't have enough time during the day to socialize or go outside."

    W "I have to stream, making video post on social media and keep up with my fanbase."

    W "Make more content every day in order to satisfy the masses."

    W "Sometimes it gets really overwhelming..."
    hide cami normal 
    show cami disgust
    W "The sheer amount of freaks I have to see on a daily basis should be illegal."
    hide cami disgust
    show cami normal
    W "But hey, if it wasn't for this I would have never being able to afford a house this big and spend money on my interests."

    y "I too struggle with my job sometimes and for a long time I didn't had one"

    y "But now things are finally starting to get better."

    y "I hope things will turn out better for you too."

    y "I have to go now or my colleague will kill me if im late again."

    hide cami normal
    show cami happy

    W "Thanks for the kind words."

    y "No problem im just doing my job."

    y "Hey wanna share numbers so we can keep in touch?"
    hide cami happy 
    show cami normal

    W "No need to, if I'll need you I'll find a way."

    y "Ok... soo have a nice day."

    scene bg wportaopen with dissolve
    scene bg wporta with dissolve
    with Pause(1)

    "'Door closes'"

    "'You silently go back to the truck.'"
    scene bg space with dissolve 
    show normal bingus with dissolve
    B "So how it went?"
    hide normal bingus

    show confused bingus
    y "It was an experience let's say."

    $ wanda +=1
    $ monica +=1
    hide confused bingus with dissolve
    jump addresses2

label w6:
    y "Hey, Wanda, I've got to go. Work's calling and im late on the schedule."
    hide cami normal
    show cami secc

    W "Tsk, as I could care less."

    W "Thanks again fro the help, here is your autograph now don't waste more of my precious time."

    y " Got it, see you around ok?"

    W "Good. Now go before I change my mind and lock you here."

    y "What did you say?"

    W "Nothing, now go."
    scene bg wportaopen with dissolve
    scene bg wporta with dissolve 
    with Pause(1)

    "'Door closes'"

    "'Goes back silently to the truck.'"
    scene bg space with dissolve
    show normal bingus with dissolve 
    B "So how it went?"
    hide normal bingus

    show confused bingus
    y "I have dodged a bullet, let's say."

    $ wanda +=1
    $ monica +=1
    hide confused bingus with dissolve
    jump addresses2

label w4:
    y "Well technically she didn't said I couldn't take a look while being respectful."

    y "Let's see what she's hiding."

    scene bg wdoio with dissolve
    y "This house is getting creepier the more time passes."

    y "......."

    y "I feel a cold breeze coming from the end of this corridor, wonder what it could possibly be."

    y "I should take a closer look."
    scene wspecial with dissolve

    y "Well, I should have expect that."

    y "This lady has a whole dungeon under her house, I am not taking a step down those crooked stairs."
    
    y "Never, NEVER date or approach a goth girl that is also a Sanrio fan."

    y "I bet down there she has all kind of torture device Hello Kitty themed."

    show cami disgust
    W "Are you out of your mind?"

    y "(Oh no, my time has come...)"

    y "Uhm... my pen ran out of ink and I was looking around to found one so I can sign the parcel too ehehe..."

    W "So you thought you'd just wander into my private rooms like you own the place?"

    W "I thought I made it clear, stay where you are and don't move!"

    W "Are you perhaps a messy puppy that cannot even understand a simple command?"

    y "I didn't mean to intrude, im sorry..."

    W "Now, get our of my house before I make you regret ever taking a step in it!"
    
    "'You silently exit the house without saying a word.'"

    scene wportaopen with dissolve
    scene wporta with dissolve
    with Pause(1)

    "'Door slams shut.'"

    "'Goes back silently to the truck.'"
    scene bg camion
    show normal bingus
    B "So how it went?"
    hide normal bingus

    show confused bingus
    y "I have dodged a bullet, let's say."

    $ wanda +=1
    $ monica +=1
    hide confused bingus 
    jump addresses2
    
label ACT3:
    scene bg space
    show normal bingus with dissolve
    "Static noises coming from the radio"
    B "Boss is calling."
    "'Answers radio'"
    hide normal bingus
    show normal boss
    d "Bingus Jr do you hear me? Over."
    hide normal boss
    show happy bingus
    B "Yes Boss, over."
    hide happy bingus
    show normal boss
    d "Perfect, im calling to inform you and the new recruit that your shift is over, over."
    hide normal boss
    show normal bingus
    B "Got it. Over."
    hide normal bingus 
    show happy boss
    d "Oh and remember tonight we are gonna have our company pizza party."

    d "Since we increased our profits by 400 times everyone its gonna receive a twentieth of a pizza slice and 3 milliliters of soda! Over."
    hide happy boss 
    show happy bingus

    B "That sounds wonderful, me and [povname] are thrilled to be there, see you soon boss! Over and out."
    "'Closes call'"
    hide happy bingus
    show normal bingus
    
    B "Another very productive day, isn't it wonderful [povname]?"

    y "Yeah im happy to work with you Jr."

    y "Come one now, let's go back to the base let's se how lit this company party can be."

    y "One whole twentieth of a pizza! Man working hard sure is rewarded."

    scene black with slowdissolve
    with Pause(1)

    show text "Bingus Jr and [povname] spent another great evening together" with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)

    show text "The party was fun, even Bingus's brother was there." with dissolve
    with Pause(2) 

    hide text with dissolve
    with Pause(1)

    show text "Bingus brother now tolerates [povname] a little more." with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)


    show text "One week later" with dissolve
    with Pause(3) 

    hide text with dissolve
    with Pause(1)
    
    scene bg camion with quickfade
    show happy bingus with dissolve
    B "Good morning [povname]"
    
    y "Morning Jr, how we doing today?"

    B "Very good, I tried some green tea you told me about and it was pretty decent I have to say."

    y "I know you would have like it, were are we going today partner?"
    hide happy bingus
    show normal bingus
    B "Let's see..."
    hide normal bingus
    show happy bingus
    B "Oh you have some new messages better check those out."
    if wanda ==2 and seneca ==2 and quasar ==2 and adinolfo ==2:
        jump secret
    else:
        jump messages

label secret:
    y "Nah it's nothing important, let's go Jr or else we will be late on the schedule."

    B "Aye aye captain!"
    scene black with quickfade
    with Pause(1)

    show text "[povname] and Jr went on with the shift like usual." with dissolve
    with Pause(2) 

    hide text with dissolve
    with Pause(1)

    show text "After the shift [povname] went back home...." with dissolve
    with Pause(2) 

    scene black with dissolve
    with Pause(1)

    show secret with dissolve
    with Pause(27)
    hide secret
    call credits
    return    

label messages:    
    menu:
        "Wanda invite." if wanda ==2:
            jump wande
        "Seneca invite" if seneca ==2:
            jump senece
        "Quasar invite" if quasar ==2:
            jump quasare
        "Adinolfo invite" if adinolfo ==2:
            jump adine
        "Ignore and let Bingus choose your next destination.":
            jump neutral_final

label wande:
    y "This one is from Wanda"
    hide happy bingus
    show confused bingus
    B "What does she needs? Did the package arrived damaged?"

    y "No nothing like that... if you don't mind can we go and check on him?"
    hide confused bingus
    show normal bingus
    B "Sure, I'll make a deviation."

    B "But you have to be quick, don't take too much time last time ok?"

    y "Don't worry I'll be back before you can Say 'Spedisco Nu Paccheeto'."

    B "If you say so..."
    hide normal bingus with dissolve
    scene bg wandaplanet with dissolve
    with Pause(1)
    scene bg wviale with dissolve

    y "I wonder what he needs my help for."

    scene bg wporta with dissolve
    "'Knocks on the door'"
    scene bg wportaopen with dissolve
    show cami normal with dissolve
    W "I told you I would find a way"
    
    W "I have to tell you something. "

    W "Follow me inside, I don't want anyone to see us together."

    y "Sure Wanda, whatever makes you more comfortable."
    hide cami normal with dissolve
    scene bg wsalotto with dissolve
    scene bg wdoio with dissolve

    scene wletto with dissolve
    show cami normal with dissolve
    A "This is my private room, here we should be alone away from prying eyes."

    y "Now tell me, what was on your mind that required my help?"
    hide cami normal
    show cami happy 
    A "I have some feelings for you dork."
    hide cami happy
    show cami secc
    A "Of all the people in this universe, you alone have impressed me "
    hide cami secc
    show cami normal
    A "When we talked last week you reminded me of how I was before fame and for the first time in a while i felt something..."

    y "Oh Wanda..."
    hide cami normal
    show cami happy
    A "Tell me do you feel the same?"

    y "I do...."
    hide cami happy
    show cami bonk
    A "Then we should make this serious and start dating."

    A "Maybe those losers who thirst so much will stop harassing me."

    y "How about I meet your parents first?"

    A "We can also do that too."

    play sound "music.mp3"
    show wanda with dissolve
    with Pause(27)
    hide wanda
    call credits
    return     

label adine:
    y "This one is from Adinolfo"
    hide happy bingus
    show confused bingus
    B "What does he needs? Did the package arrived damaged?"

    y "No nothing like that... if you don't mind can we go and check on him?"
    hide confused bingus
    show normal bingus
    B "Sure, I'll make a deviation."

    B "But you have to be quick, don't take too much time last time ok?"

    y "Don't worry I'll be back before you can Say 'Spedisco Nu Paccheeto'."

    B "If you say so..."
    hide normal bingus with dissolve
    scene bg adinolfoplanet with dissolve
    with Pause(1)
    scene bg aviale with dissolve

    y "I wonder what he needs my help for."

    scene bg aporta with dissolve
    "'Knocks on the door'"
    scene bg aportaopen with dissolve
    show happy cat with dissolve
    A "[povname] you saw my message!"
    hide happy cat
    show silly cat
    A "Sorry for sudden request, I know your job is very busy but I really need to tell you something. "
    hide silly cat
    show normal cat
    A "Please follow me inside, I don't want my father seeing us from the satellites"

    y "Sure Adinolfo, whatever makes you more comfortable."
    hide normal cat with dissolve 
    scene bg asalotto with dissolve
    scene bg adoio with dissolve

    scene aletto with dissolve
    show silly cat with dissolve
    A "This is my private room, here we should be alone away from hidden cameras"

    y "Now tell me, what was on your mind that required my help?"
    hide silly cat
    show bonk cat
    A "I have some feelings for you..."

    A "I thought I would never experience such silly things."
    hide bonk cat 
    show happy cat
    A "But when im with you [povname] I feel like I am more than the son of a intergalactic multi gazillionaire."

    y "Oh Adinolfo..."
    hide happy cat
    show normal cat
    A "Tell me [povname] do you feel the same?"

    y "I do Adinolfo."
    hide normal cat
    show bonk cat
    A "Then I think we should start dating if it's ok for you [povname]."

    A "Maybe we can have a romantic story like the ones I see in Brooklyn shows and travel across the galaxy on my private spaceship and and..."

    y "How about I meet your parents first?"

    A "We can also do that hehe.."

    play sound "music.mp3"
    show adinolfo with dissolve
    with Pause(27)
    hide adinolfo
    call credits
    return

label quasare:
    y "This one is from Quasar"
    hide happy bingus
    show confused bingus
    B "What do they needs? Did the package arrived damaged?"

    y "No nothing like that... if you don't mind can we go and check on him?"
    hide confused bingus
    show normal bingus
    B "Sure, I'll make a deviation."

    B "But you have to be quick, don't take too much time last time ok?"

    y "Don't worry I'll be back before you can Say 'Spedisco Nu Paccheeto'."

    B "If you say so..."
    hide normal bingus with dissolve
    scene bg quasarplanet with dissolve
    with Pause(1)
    scene bg qviale with dissolve

    y "I wonder what he needs my help for."

    scene bg qporta with dissolve
    "'Knocks on the door'"
    scene bg qportaopen with dissolve
    show qua happy with dissolve
    Q "[povname] you came!"
    hide qua happy
    show qua embara
    Q "Sorry for the abrupt message, I know you are a very busy person but I really need to tell you something. "
    hide qua embara
    show qua normal
    Q "Please follow me inside, Im not comfortable talking outside of such things."

    y "Sure Quasar, whatever makes you more comfortable."
    hide qua normal
    scene bg qsalotto with dissolve
    scene bg qdoio with dissolve

    scene qletto with dissolve
    show qua normal with dissolve
    Q "This is my private room, here we should be alone."

    y "Now tell me, what was on your mind that required my help?"
    hide qua normal
    show qua embara
    Q "I have some feelings for you..."

    Q "Im not used to express my feelings."
    hide qua embara 
    show qua happy
    Q "But when im with you [povname] I feel like I can do anything!"

    y "Oh Quasar..."
    hide qua happy
    show qua embara
    Q "Tell me [povname] do you feel the same?"

    y "I do Quasar"
    hide qua embara
    show qua horny
    Q "Then I think we should start dating if it's ok for you [povname]."

    Q "Maybe we can have a romantic story like the one I had read in those magazine."

    y "I'll be glad to..."

    play sound "music.mp3"
    show quasar with dissolve
    with Pause(27)
    hide quasar
    call credits
    return   

label senece:
    y "This one is from Seneca"
    hide happy bingus
    show confused bingus
    B "What does he needs? Did the package arrived damaged?"

    y "No nothing like that... if you don't mind can we go and check on him?"
    hide confused bingus
    show normal bingus
    B "Sure, I'll make a deviation."

    B "But you have to be quick, don't take too much time last time ok?"

    y "Don't worry I'll be back before you can Say 'Spedisco Nu Paccheeto'."

    B "If you say so..."
    hide normal bingus with dissolve
    scene bg senecaplanet with dissolve
    with Pause(1)
    scene bg sviale with dissolve

    y "I wonder what he needs my help for."

    scene bg sporta with dissolve
    "'Knocks on the door'"
    scene bg sportaopen with dissolve
    show sene 1 with dissolve
    S "Welcome back [povname]."

    S "Sorry for the abrupt message, but I have to tell you something that was on my mind since our last encounter."

    S "Please follow me inside, I prefer to talk of such topics in a more private location."

    y "Sure Seneca, whatever makes you more comfortable."
    hide sene 1
    scene bg ssalotto with dissolve
    scene bg sdoio with dissolve

    scene bg sletto with dissolve
    show sene 1 with dissolve
    S "This is my private room, here we should be alone."

    y "Now tell me, what was on your mind that required my help?"
    hide sene 1 
    show sene 2
    S "I have some feelings for you..."

    S "I know that emotions are something completely irrational opposite to rational thinking."
    hide sene 2 
    show sene 3
    S "But with you [povname] I feel something that not even words can describe."

    y "Oh Seneca..."
    hide sene 3
    show sene 1
    S "Tell me [povname] do you feel the same?"

    y "I do Seneca"

    S "Then I think we should start dating, this way we can really see if what we feel could be more than something irrational."

    play sound "music.mp3"
    show seneca with dissolve
    with Pause(27)
    hide seneca
    call credits
    return    

label neutral_final:
    hide happy bingus
    show normal bingus
    y "You know Jr how about you choose the destination this time."
    hide normal bingus 
    show happy bingus
    
    B "Really!?!?!"

    y "Of course bud, you deserve to have fun too."

    B "Yippee im so happy!!"

    y "So what are you waiting captain? Its time to go!"

    B "Aye aye [povname]!"
    hide happy bingus with dissolve
    play sound "music.mp3"
    show neutral with dissolve
    with Pause(27)

    call credits
    return    

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show group:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide group
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    show bg end with quickfade
    pause 
    return

init python:
    credits = ('Design', 'Locatelli Alessandro'), ('Design', 'Battaglia Niccolò'), ('Design', 'Consiglieri Leonardo'), ('Design', 'Melfa Altea'), ('Concept', 'Avanzi Nicole'), ('Concept', 'Betta Eleonora'), ('Concept', 'Bonfadini Noemi'), ('Concept', 'Pavan Sara'), ('Concept', 'Peralti Sara'), ('Concept', 'Rigolli Riccardo'), ('Concept', 'Tartaglia Giulia'), ('Concept', 'Zheng Xin'), ('Programmer', 'Locatelli Alessandro')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image group = Text("{size=80} Made by D(Elivery) Group", text_align=0.5)
    image thanks = Text("{size=80}Thank you for Playing!", text_align=0.5)