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
    scene bg ufficio with slowdissolve
    show normal bingus
    b "Hello there, my name is Bingus im going to be your new supervisor. May ask your name human?"

    $ povname = renpy.input("So... Whats your name?", length =32)

    y "My mane is [povname]."

    b "So glad to have you here [povname], here at 'Spedisco Nu Paccheeto' we are always happy to have new recruits in our big happy family!"

    y "Uh... ok I guess. So... how's the pay here ehm Pintus? "
    hide normal bingus
    show angry bingus

    b "The names is Bingus, I would like my name not to be confused ok?"
    hide angry bingus
    show normal bingus
    b "Before that I have to ask you a couple of question for an optional survery so we can improve the service and how we appoach new future recruits."
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
    jump Scelta_1

label Scelta_1:
    b "Very good."
    show happy bingus
    b "First question, how good of a team player are you?"
    hide happy bingus
    menu:
        "The best of the best":
            jump Scelta_3
        "Good enough for this position":
            jump Scelta_4
        "What's teamwork?":
            jump Scelta_5

label Scelta_5:
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
    show confused bingus
    b "Ok... love the spirit, really..."

    hide confused bingus
    show normal bingus
    b "Let's continue with the questionnaire."
    jump Scelta_0 

label Scelta_3:
    show happy bingus
    b "Wonderful! We are having so much fun, I cant wait to finish this very ''entertaining'' task before my lunch breack!"
    jump Scelta_0

label Scelta_0:
    hide happy bingus
    show confused bingus
    b "Whoa the next one must be one of the newer ones, first time ever seeing it here."
    hide confused bingus
    show normal bingus
    b "Soo next question, are you sextually active by any chanche?"
    menu:
        "Yes, why you ask?":
            jump Scelta_6
        "None of your buissness!":
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
    b "Aren't you having fun? Here at 'Spedisco Nu Paccheeto' every day is fun as your last!"
    hide happy bingus
    show seccato bingus
    b "Ugh.. this stupid gingle is still stuck in my mind, but you will get over it eventually."
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
    b "Well if you can see the importance of this question im not gonna elaborate further."

    y "If you say so... everybody knows hot tea from the vening machine in the gas station is the best."
    hide angry bingus
    show seccato bingus
    b "Ugh... what a zorping loser."

    y "Exuse me? I what did you said to me?"
    hide seccato bingus
    show normal bingus
    b "Ehm... nothing I was just.. clearing my voice and thats hehe."

    y "Can we hurry up?"

    b "Of course, let me see..."
    jump Scelta_12

label Scelta_10:
    
    show seccato bingus
    b "Well if you like drinking battery acid I guess its definetly a choice."

    y "Excuse me?"
    hide seccato bingus
    show normal bingus
    b "Let's continue, so I can end my misery soon."
    jump Scelta_12

label Scelta_9:
    b "Im my opinion green tea is the best, but if you still have the taste of a infant I guess we could make it work."

    y "I wonder whats the purpose of this survey."
    
    show seccato bingus
    b "Don't ask me, im just doing my job."
    
    b "'Wispering to himself' Just 23 years to retirement I can do it, oh my Zulone this headake is killing me."
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
    b "Ugh... two tablets of Zanaz are not gonna be enough fot this level of pain."

    b "You don't have many friends am I right?"

    y "Sorry I was just tryna to lights up the conversation."
    hide seccato bingus
    show normal bingus 
    b "I think you could do a better job simply by closing yout mouth, ok?"

    y "Yes sir."
    jump Scelta_16

label Scelta_14:
    show confused bingus
    b "But I still will be here five years from now."

    b "Was this some kind of human joke because it didn't make me laugh."

    y "Ok I get it, like you could have told me your funny bone was missing jeeze."
    hide confused bingus
    show normal bingus
    b "All my 230 bones are perfectly fine, you just aren't funny."
    jump Scelta_16

label Scelta_13:
    show seccato bingus
    b "Which one?"

    b "Regardless listen if you wanted so bad to be a comedian you should have just put a red nose on your face."

    b "The clown looks its already on point."

    y "....... that kinda hurts."
    hide seccato bingus
    show normal bingus
    b "Im glad to hear that bozo."
    jump Scelta_16

label Scelta_16:
    "Static sounds coming from Bingus radio"

    show normal bingus
    b "Do me a favor and stay quiet for a second I think the boss is trying to contact me."

    "Answers radio call"
    hide normal bingus
    show normal boss at right
    show feared bingus at left
    d "Supervisor Bingus, im calling for an update on the interview with the new recruit.........., over."

    b "Glad to hear you boss, always a pleasure. The recruit interview is going quite well, over."
    hide normal boss
    show angry boss at right
    
    d "I hope for you its not well as the last one who crashed 2 of our trucks inside the cafeteria, over."
    
    b "Yes sir, I din't forgot about the drivers licence, over."

    "Bingus looks at you with a glacial stare"
    
    b "You do have a driving licence am I right human?"
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
    b "Finally you said somehing smart and useful for once!"

    b " Still do not get near the cafeteria capisc?"

    y "Ok, thanks I guess?"
    hide happy bingus
    jump Scelta_19

label Scelta_19:
    hide angry boss
    show normal boss at right
    show feared bingus at left
    d "Supervisor Bingus do you hear me? Over."

    b "yes boss, the candate has a drivers licence, over."
    hide normal boss
    show happy boss at right

    d "Perfect,I just finished signing the new recruit documents. The human is officaly part of the 'Spedisco Nu Paccheeto' family. over."
    hide feared bingus
    show seccato bingus at left
    b "Hurray... im soo happy to hear that."
    
    d "Good, if you please can you direct the human to the Launching pad, so it can sart the shift, over."

    b "Sure thing boss, it'll be a pleasure for me. Over and out."
    hide happy boss
    hide seccato bingus
    show normal bingus
    b "You heard the boss, go to the Launching pad, follow the corridor and take the second door to the right."

    b "And remember do NOT enter or follow me into the cafeteria, now if you escuse me I have a tuna sadwich to eat."

    b "Oh, I almost forgot your truck its gonna be the first one on the left, my collegue will be waiting for you in the vehicle."
    hide normal bingus
    show seccato bingus
    b "Please don't screw up."
    hide seccato bingus
    "Walks away"

    y "Finally, the stupid survey its over, I hope I don't get fired on day one as my last job."

    y "Maybe mixing bleach and vinegar to clean the floors in a restaurant wasn't a good idea."

    y "I guess its time to start my shift."
    jump Scelta_20

label Scelta_20:
    scene bg camion with dissolve
    y "I think this one is the right truk, I wonder where is this collegue bingus told me about."

    "Door opens and slam close"
    show happy bingus
    y "Bingus what are you doing here?"

    P "Gleep gloop"
    "Hands over strange tablet"

    y "You want me to take it?"

    P "Zorp"
    
    "Tablets lighs up, illuminating the cabin"
    P "Very good friend, now you can hear me right?"

    y "Yes but you were talking to me fine like 5 minutes ago, whats the use of this strange machine."
    hide happy bingus
    show normal bingus
    P "Well its an itergalatic translator with over 5 gazillion language known in the universe."

    P "I still don't know how to speack properly the human dialect so Boss gave it to me just in case."

    B "Oh by the way i am not Bingus but his little brother Bingus Jr and im going to be your partner."

    y "Cool, finally someone who seems normal. Soo... what do we do now?"

    B "Well you should start first by turning on the truck with the key."

    y "Sure, ehm where is the keyhole?"
    hide normal bingus 
    show confused bingus
    B "Inside the steering weel, have you ever drove one of this truks before [povname]?"

    y "Yes, of course I have many hours driving trucks, even bigger than this one."

    y "This must be a new model I didn't had the chance tro try before ahah."
    hide confused bingus
    show normal bingus

    "Turns on the truck"
    y "Ok now what?"

    B "Well now you have to choose where to go first I have a couple of addess to go trough so choose."
 
    y "I get to choose?"
    hide normal bingus
    show happy bingus
    B "Yes silly, I usually pick a random address so I knewer know what my nect destination will be, wanna try?"

    y "I'd rather not, what are the addesses Jr?"

    B " Sure thing lets see..."
    hide happy bingus
    jump addresses

label addresses:
    menu:
        "77 Domina Ave Neptune Np 44756" if wanda ==0:
            jump wanda
        "03 Sapience Rd SW Saturn St 5689" if seneca ==0:
            jump seneca
        "404 Remsemen Street Jupiter Jp 3912" if quasar ==0:
            jump quasar
        "420 Hooters 6th Avenue Mars Mr 6996 " if adinolfo ==0:
            jump adino

label adino:
    scene bg space with dissolve
    show normal bingus
    y "Woah the space is so beautiful."
    hide normal bingus
    show happy bingus
    B "I know right, this is the best part of the job."

    B "Every day is full of possibilities."

    y "Really? I only thought we were just some delivery guys for a massive coporation."
    hide happy bingus
    show normal bingus
    B "Thas only a part of the job, I think its the journey the best part."

    B "Once I had to follow a comet in order to arrive to a very far far away planet in a different distict just outside of the Milky Way."
    hide normal bingus
    show happy bingus
    B "Best experience of my life, and you did you had similar experience ehm... can you remind me your name?"

    y "Don't worry, my name is [povname] and no I never had something like that in my life."

    y "The closest thing I had saw related to space is the bill board for the pizza place i used to work at with a space ship on it." 
    hide happy bingus
    show confused bingus
    B "Well its better than nothing I guess...oh I think we are close to our destination look on your left!"
    hide confused bingus

    scene bg adinolfoplanet with dissolve
    with Pause(2)
    scene bg aviale with dissolve
    with Pause(1)

    y "This dude must have tons of money, like look how rich and well kept is this patch of garden."

    y "Heck he got grass on Mars thats more impressive than every thing elese!"
    show normal bingus
    B "You are right but remember to be professional."

    y "Ok I will."

    B "Good luck!"
    hide normal bingus
    scene bg aporta with dissolve
    with Pause(1)
    menu:
        "Knock on the door.":
            jump adino_1
        "Leave the package and go back to the truck.":
            jump adino_2

label adino_2:
    y "Well, on a second thought I think its better if i leave the package here."

    y "Just wanna tke all precautions since the package is very heavy I guess its also fragile."
    show normal bingus
    B "Good, make sure to place it with the label facing the top."

    y "Done, let's go Jr!"
    hide normal bingus 
    show happy bingus
    B "So were are we going now captain?"
    $ adinolfo +=1
    hide happy bingus
    jump addresses