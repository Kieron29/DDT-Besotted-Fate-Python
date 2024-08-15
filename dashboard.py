import tkinter as tk
from PIL import Image, ImageTk

#new window for content game
class BesottedFate:
    def __init__(self, root):
        self.root = root #shortens
        root.title("Besotted Fate") #creates title Besotted Fate
        root.attributes('-fullscreen', True) #makes fullscreen

        #adjust app to user's screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        #add background image
        self.bg_img = Image.open("bfcell.jpg")
        self.bg_img = self.bg_img.resize((screen_width, screen_height))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(root, image=self.bg_img)
        self.bg_label.place(relwidth=1, relheight=1)

        #font and sizes
        label_font = ("MS Gothic", 24)
        dialogue_font = ("MS Gothic", 24)
        button_font = ("MS Gothic", 18)

        #title for day
        self.title_label = tk.Label(root, text="Day One", font=label_font, bg='white')
        self.title_label.place(relx=0.5, rely=0.01, anchor='n')

        #dialogue box and positioning
        self.dialogue_frame = tk.Frame(root, bd=2, relief="solid", bg='white')
        self.dialogue_frame.place(relx=0.025, rely=0.1, relwidth=0.65, relheight=0.6) 
        self.dialogue_label = tk.Label(self.dialogue_frame, font=dialogue_font, anchor='nw', justify='left', bg='white', wraplength=screen_width * 0.6)
        self.dialogue_label.pack(fill="both", expand=True, padx=10, pady=10)

        #hint box 
        self.hints_frame = tk.Frame(root, bd=2, relief="solid", bg='white')
        self.hints_frame.place(relx=0.025, rely=0.75, relwidth=0.65, relheight=0.15)
        #hint label config
        self.hints_label = tk.Label(self.hints_frame, font=label_font, bg='white')
        self.hints_label.pack(padx=10, pady=5, anchor='nw')
        #create new label (nav=navigation) as it will change
        self.nav_label = tk.Label(self.hints_frame, text="Press spacebar or arrow keys to navigate around the text", font=("MS Gothic", 20), bg='white')
        self.nav_label.pack(padx=10, pady=(10, 5), anchor='nw') 

        #placeholder button (first choice)
        self.choices_frame = tk.Frame(root, bd=2, relief="solid")
        self.choices_frame.place(relx=0.7, rely=0.55, relwidth=0.275, relheight=0.35) 
        self.c1 = tk.Button(self.choices_frame, text="Look outside your cell", font=button_font, height=3, command=lambda: self.choice('c1p1'))
        self.c1.pack(fill="x", padx=10, pady=(10, 5))
        self.c2 = tk.Button(self.choices_frame, text="Pretend to sleep", font=button_font, height=3, command=lambda: self.choice('c2p1'))
        self.c2.pack(fill="x", padx=10, pady=5)
        self.c3 = tk.Button(self.choices_frame, text="Eat the food on the tray", font=button_font, height=3, command=lambda: self.choice('c3p1'))
        self.c3.pack(fill="x", padx=10, pady=(5, 10))
        self.disable_choices()

        #settings and help buttons (set=settings)
        self.set_help_frame = tk.Frame(root, bd=2, relief="solid", bg='white')
        self.set_help_frame.place(relx=0.7, rely=0.1, relwidth=0.275, relheight=0.15) 
        self.set_button = tk.Button(self.set_help_frame, text="Settings", font=button_font, command=self.settings)
        self.set_button.pack(side="top", fill="x", padx=10, pady=(10, 5))
        self.help_button = tk.Button(self.set_help_frame, text="Help", font=button_font, command=self.help)
        self.help_button.pack(side="top", fill="x", padx=10, pady=(5, 10))

        #content - dialogue box
        self.text_part1 = (
            "Droplets of water fall into your drowsy eyes. You wake up, seemingly unnerved but completely confused. "
            "‘This isn't where I should be’, you think, as your eyes adjust to the bright beam of light from a slit of welded steel. "
            "The dark concrete floor is mouldy and the air is damp. You are in a 4x4 prison cell, it seems. "
            "The only thing keeping you from the rats and cockroaches feeding on your flesh is a rugged tarp, suspended on a chain-linked bench on which you lie. "
            "Whatever happened to your cosy bed with cold pillows and the air conditioner?")
        self.text_part2 = (
            "Sitting next to your feet is a tray with bread with lumps on it, clearly unidentified substances that are supposedly edible. "
            "On your right is the hallway, separated by iron bars and an iron door that looks aged but well fitted that not even a truck could budge. "
            "And towards your left, a toilet with a pungent stench, which you probably should not inspect. "
            "Directly opposite is… well nothing. Just a wall and the etched tallies of a previous tenant that you replaced. "
            "Lastly, behind you. A concrete wall separating you from a neighbour that soon may very well be part of your life. "
            "Yet for now, you have no idea where you are, what time it is and why you're here. "
            "All you know is that this place is ominous and you need to escape.")
        #changed to use \n instead
        self.text_part3 = ("A trudging of heavy iron-clad boots can be heard in the distance, growing louder with every step. It seems you are not the only one in a cell either, as you can hear the panting and groaning of similar state victims in cells surrounding you. You…")
        self.text_part4 = ("After that little anxiety episode, you notice that there is a piece of shredded paper underneath the bench, just barely concealed by the hole-ridden tarp. Your curiosity results in you reading this note. “I'm Melissa, I'm here to try to help but I'm really just in your same situation. Write back and slip it under the crack of the slab next to you”. You…")
        self.text_part5 = ("A few minutes later, a shuffling occurs and the crinkled paper is lodged back into your possession. ‘I'm a nobody from a small town Amarillo, Texas. I don’t know why we’re here, but I have a wild guess. We were drugged and kidnapped, forced to create contraband for an organisation. Regarding the language the guards speak, I assume it's Russian. I've been here for around 5 days, but I don't have the best sense of time.’ You…")
        self.text_part6 = ("The note was replaced with a new sheet of paper with reasonably sized text.  ‘You don't know this yet, but the guards are sensitive to hearing and smelling.  Their eyesight is faulty but they can make out a man is not where he is supposed to be.  Here is the bright side, I have a plan to escape.  In an hour, we will be released to work in the factory and it seems we will have a good chance of smuggling some metals/chemicals and other elements to help us escape.  Are you in?’  ")
        self.text_part7 = ("Her information gathered seems valuable. Moments later, the bell rings and you see the vault-like door move outwards.  You see everybody stand up and make their way outside the cell where they stand still.  ‘I should probably do that’ you think, as you attempt to muster the strength to step outside from the cell for the first time. You...")
        self.text_part8 = ("All prisoners suddenly turn to their left and start following the guards down the hallway.  You copy every move of the unknown soul in front of you until you reach a small chair with your name on it.  \n‘What the hell am I supposed to do with this?’ You think, as you see the taskboard and quota that is expected of you, lying on the wooden stool you would sit on.  As you read the procedure, a singular tap on your shoulder from a being behind you is felt.  You...")
        self.text_part9 = ("You sit down in your 'workspace' and see an instruction manual.  Your first task on this list is a very interesting one.  A machine requires adjustments and there are three different colour coded wires.  You look up and pull out a metal crate that resembles a voltage box.  ‘I guess I have to fix this darn thing’, you say to yourself.  There are 3 wires in this voltage box with the colour code - Red, Blue and Green.  On the taskbar, there are the following clues; \n The blue wire is not next to the wire you need to cut. \n The green wire is not on the far right. \n The red wire is to the left of the blue wire. \nYou need to cut the wire that will safely disable the voltage box from experiencing a high current fault.  If you cut the wrong wire, this could mean death.  What do you choose?")
        self.text_part10 = ("A crucial oil-filled machine lays in front of you, dire for repair.  The machine has a compartment with a sensitive cable underneath that in no circumstance should have any oil dripping on it.  You need to replace the bottom of the compartment and screw it on without letting any oil drip onto the cable.  You have 3 different screws available to you.  What do you use to tighten the bottom without letting oil leak onto the cable?")
        self.text_part11 = ("You finished your tasks for the time being, and the bell rings.  You notice in the corner of your eye that guards are entering the facility to assess the workplace.  \n“Well, I've finished the machine and it should be functioning.” \nBut wait? \n“Which button do I press to show the guards I have completed the task?” You question, as you see a controller with 3 different coloured buttons.  Before you can even think, a guard approaches and waits for the Quod Erat Demonstrandum.  You have a feeling that you have to press the right button or you will be dead on the spot.")
        self.text_part12 = ("You pass the inspection and Melissa approaches you.  \n“Well done.  You know, I wouldn't have teamed up with you if you didn't have problem-solving skills”  She said.   \n“Uhm thanks?” You reply and she giggles. \n“Oh, we are making our way to the ‘rest’ cell.  Here is our only chance to pass the chem lab, the steelworks and the guard's locker area.  Today the Chem Lab is open-but it will close tomorrow and the steelworks will open.” She dictates.  \n“We should try get something from the chem lab.  But it's your decision.”")
        self.text_part13 = ("You close your eyes, harden your resolve and mentally prepare yourself. Nothing should go south, and if it does, Melissa is definitely becoming the sacrifice. You both walk towards the Chem lab and see trolleys lined up outside that seem to contain several pocketable items.  You decide to grab…")
        self.text_part14 = ("You step into the rest zone and the guards close the barb-wired cage doors.  There are about 50 prisoners in the area which all sit on the damp, yellow grass.  You look up and see a glimmer of the outside sun discretely waving back at you. It's not much, but you feel a sense of relief.  Your eyes wonder to Melissa, finally seeing her directly and you admire her expression as she tilts her head confused on why you are staring so intently.  Melissa whispers on how she is happy with your choice and you start talking about life as it was before. You mention...")
        self.text_part15 = ("Time passes, and you find yourself separated from Melissa and in your respective cell. It is night time and you are placed into the cell you started in.  A long day of labour has proved fruitful as you carry the bottle of Hydrochloric Acid.  Melissa slips a note under the same crack which you open up quietly.   \n‘We can escape whenever you want.  We can even do it tonight.  You make the call.’ \nYou think about it meticulously.  You can attempt it tonight and be free faster, or you can bide your time, exploring the large factory.")

        #outcomes
        self.c1o1 = ("You look outside your cell to see who is causing the loud footstep noises. The figure walking down notices you and shouts in a foreign language. It is best not to stand there any longer as he does not seem pleased. You sit back down on the bench.")
        self.c2o1 = ("Lying on your bed, you peer with one eye open and the guard stares into your cell. He wields a thunderlance and strikes the metal bars in an immense rage. You jolt up and he shouts in a foreign language.")
        self.c3o1 = ("You figure that you need some energy, hauling the sludge into your mouth and swallowing. It reminds you of clumped sour milk. You wince at the taste and nervously avoid making eye contact with the passing guard, and he reciprocates.")
        self.c1o2 = ("You discreetly slip it under the crack and you can hear the motions of the unknown sender collecting your writing.")
        self.c2o2 = ("Your boredom exceeds you. You decide to write back.")
        self.c3o2 = ("You discreetly slip it under the crack and you can hear the motions of the unknown sender collecting your writing.")
        self.c1o3 = ("How suspicious, you think.  You are not one to trust anyone who appears out of nowhere. It doesn't stop you from writing back, you are just highly on guard.")
        self.c2o3 = ("You slip back the note and it is received a few seconds later.")
        self.c3o3 = ("In an attempt to attract her attention, you whisper 'HEY!' A guard notices this and rushes to your cell before you can even react. " "A back-breaking blow of electricity and hard wire is jabbed between the iron bars and into your neck.")
        self.c1o4 = ("You question her and she replies, ‘I'm a quick learner.  I've seen many people who talk too much and get beheaded.  However, they could not spot me slipping a metal wire into my pocket.  Do you trust me or not?’")
        self.c2o4 = ("You relay the good news of her new found companionship and she replies, “Great. I promise I won't let you down  When you hear the dull ringing of a bell, the doors release and we make our way to the assembly line.”")
        self.c3o4 = ("You start overthinking - I'm not ready for this.  What if we get caught? How can I trust her?  Too many possibilities for error I might get a heart attack. \nBut there's no point. \nI have to join her if I want a better chance at survival.")
        self.c1o5 = ("A squad of guards march across the hallway, with a laser gun scanning the forehead of every prisoner.  Not a word was exchanged, not a look either.")
        self.c2o5 = ("Lo and Behold, a girl stands with chestnut brown hair and a large white lab coat.  It is dirty and torn but emanates a bright aura of freedom and hope.  She does not dare look back, so you turn your attention back to the cell opposite where you stand.  The guards approach and they proceed to scan your forehead.")
        self.c3o5 = ("You sit and wait.  The dull metal helmet stacked on a guard's obscured face menacingly turns to you.  The baton is raised and your heart leaps.  Clenching your fists and planting your feet to the ground you decide action is better than reaction.  A full swing to his helmet with your bare knuckles misses, but the guard doesn’t.  The baton smashes your skull into fragments simultaneously frying your insides until you are nothing more than a statistic.")
        self.c1o6 = ("It's the girl on the cell to your right, who speaks in a hushed but clear voice.  “Hey.  We should be in the clear as the guards rely on CCTVs to monitor us.  However, after a few hours, they arrived to check and simultaneously the CCTV seemed to turn off.   Anyways, I’ll help you with your work but you seem to have the easiest of the lot.”")
        self.c2o6 = ("In a hushed tone and without moving your head, you reply with “yes?”\n“Turn around idiot, we are safe here.” and so you do.  It's the girl on the cell to your right, who speaks in a hushed but clear voice.  “Hey.  We should be in the clear as the guards rely on CCTVs to monitor us.  However, in a few hours, they will arrive to check and simultaneously the CCTVs seem to turn off.   Anyways, I’ll help you with your work but you seem to have the easiest of the lot.”")
        self.c3o6 = ("The tap is harder this time, and you should probably turn around. \n“Turn around idiot, we are safe here.” and so you do.  \nIt's the girl on the cell to your right, who speaks in a hushed but clear voice.  “Hey.  We should be in the clear as the guards rely on CCTVs to monitor us.  However, in a few hours, they will arrive to check and simultaneously the CCTVs seem to turn off.   Anyways, I’ll help you with your work but you seem to have the easiest of the lot.”")
        self.c1o7 = ("You sigh in relief as nothing bad happens, and the voltage box is disabled.  \n“Woah, you're learning quickly.” says Melissa.  “I suppose the next task would be trickier so you would need some of my help.  I'm not sure on exactly what to do but I've seen people get electrocuted for fixing it incorrectly.  Maybe something resistant to leakage will help with your task.”")
        self.c2o7 = ("And you close your eyes as you grab the plier, snapping the blue cord in half.  Everything blurs and all your nerves seem to rejoice at once.  Your eyes widen and roll back as you scream out in utter fear.  But nothing comes out.  Just an endless spasm of volts lift you into the horizon and you can’t help but wish you thought it through just a little more closely.")
        self.c3o7 = ("The voltage box explodes as you cut the green cord in half.  You look to your right - Melissa stares in shock.  You look to your left - workers have weary but widened eyes.  ‘I cut the wrong one.’ you thought, as you felt something on your chest.  As you look down, you see a large chunk of blasted, sizzling metal jutting out your ribs.  At that moment, your body’s adrenaline runs out and you fall into the depths of your abyss.")
        self.c1o8 = ("You fasten the bottom of the compartment with screws and rubber gaskets, then fill the container with oil. The machine seems to be slightly sturdier now, and you feel slightly accomplished. “Not bad for a first time huh?” Melissa commented. As long as it’s been, we have a small 30-minute break inside a large prison cell.”")
        self.c2o8 = ("You fasten the bottom of the compartment with screws and washers. You fill up the compartment with oil and you do not notice beads of oil forming next to the screws underneath.  Every second you fill the container with oil, the drips increase and fly millimetres away from the exposed cable.  You notice it too late—the oil has dripped and an incredible crackling rages throughout the factory.  The cable short circuits and acrid smoke possess the space.  A fire ruptures as smoke, oil and plastic fill your lungs.  The gravity of the situation did not register until guards rushed over with fire extinguishers and grabbed you out of the burning wreck.  But It doesn’t matter.  You are already dead.")
        self.c3o8 = ("You fasten the bottom of the compartment with screws and a nylon coating, then fill the container with oil. The machine seems to be slightly sturdier now, and you feel slightly accomplished. “Not bad for a first time huh?” Melissa commented.  As long as it’s been, we have a small 30-minute break inside a large prison cell.”")
        self.c1o9 = ("A quiet for 5 seconds and you begin to shake.  Was this the wrong button?  Suddenly, the machine splurts to life and electricity is channelled through the cables.  The guard ticks something off his clipboard, exhales, and leaves.")
        self.c2o9 = ("You wait and pray the machine splurts to life.  But it never does.  You realise the red button is connected to the red wire - but you have severed that wire. The guard grins behind his masked helmet.  The baton is raised and your heart leaps.  Clenching your fists and planting your feet to the ground you decide action is better than reaction.  A full swing to his helmet with your bare knuckles misses, but the guard doesn’t.  The baton smashes your skull into fragments simultaneously frying your insides until you are nothing more than a statistic.")
        self.c3o9 = ("Smoke pours out of the metal crate that you fiddled with.  Did I press the wrong button?  Indeed you have - it explodes in your face but you managed to avoid getting hurt.  You can’t cheat death twice, as the guard whips out his weapon from the holster.  ‘It’s so over.’ You say to yourself.  The baton is raised and your heart leaps.  Clenching your fists and planting your feet to the ground you decide action is better than reaction.  A full swing to his helmet with your bare knuckles misses, but the guard doesn’t.  The baton smashes your skull into fragments simultaneously frying your insides until you are nothing more than a statistic.")
        self.c1o10 = ("She smiles and looks around quickly.  \n“Okay, right over there is an unguarded trolley.  We really gotta be careful though.  I'll try to cover you as you grab something - but make it quick.”")
        self.c2o10 = ("“Snap out of it. Don't they say you miss 100 percent of the shots you don't take?” She remarked.  \n“Yeah well, I don't want to get shot. Are you sure we won't get caught?”  You replied, nervously.  \n“Ugh, that trolley over there is unguarded.  I’ll cover you as you grab something - just make it quick.”")
        self.c3o10 = ("“Right.  You should stop saying things like this or we’ll actually get killed in the dumbest way possible.” Melissa glared.  \n“Anyways.  I'll cover you as you grab something from that unguarded trolley - but make it quick!”")
        self.c1o11 = ("Perfect.  This should erode metal locks very easily.  Melissa is satisfied with your choice and you slip it in your pants.  Nonchalantly, you both make your way towards the rest area.")
        self.c2o11 = ("The tweezers are of such a bad quality that you place them back.  Guess you're going to go for the small bottle of Hydrochloric Acid.")
        self.c3o11 = ("You grab the sulfuric acid and nonchalantly walk towards the rest area.  As you walk, you trip on an unseen cord leading to you dropping the beaker.  It shatters and you fall right on it.  This loud noise attracts the guards as your tissues and flesh are vaporised and the fumes burn your insides.  The guard towers over you as you struggle to survive, and he fires a singular shot to finish you off.")
        self.c1o12 = ("“Hey Melissa, you know I got a dog named Rocco?  He ALWAYS drools everywhere but I still love him.  I can't help but wonder where he is now.  Or if he even knows I'm gone.”  \nMelissa giggles and replies, “He sounds cute and I’m sure he’s fine. I have a cat named Stef but I’m sure she’s fine too. Knowing her, she’s probably having a good time eating rats behind the garbage in Arby’s.”")
        self.c2o12 = ("“Bro, I like cheese.  I want to eat some cheese right now.” You exclaim randomly.  \n“That is so random,” Melissa replied. “But relatable.” \n”I know right? Like I could go for a cheesy mozzarella pizza or a bowl of cheesy ramen or a-” \n“SHHH! Don’t make me hungry!” She jokingly interrupted.")
        self.c3o12 = ("“In my free time, I love to invest in stocks.  I invested about $7,500 in AAMD and I got about a 55% profit.  Like, I can’t believe no one saw how AAMD's new release completely crushes BPMR's product.” You gloated. \n“Oh, that’s good for you!” She replied, invested in your speech on investments.  \n“Yeah, and I went ALL into AAMD which was nerve-wracking.”")
        self.c1o13 = ("To be Continued.")
        self.c2o13 = ("To be Continued.")
        self.c3o13 = ("To be Continued.")
        self.current_part = 1
        self.button()
        
        #controls for users
        root.bind('<space>', self.next_part) #user presses spacebar, goes to next part
        root.bind('<Right>', self.next_part) #user presses right arrow key, goes to next part
        root.bind('<Left>', self.previous_part) #user presses left arrow key, goes to previous part

    #enables keybind navigation
    def enable_movement(self):
        root.bind('<space>', self.next_part) 
        root.bind('<Right>', self.next_part) 
        root.bind('<Left>', self.previous_part) 
    
    #disables keybind navigation
    def disable_movement(self):
        root.unbind('<space>')
        root.unbind('<Right>')
        root.unbind('<Left>')

    #placeholder buttons - disabled state
    def disable_choices(self):
        self.c1.config(state="disabled")
        self.c2.config(state="disabled")
        self.c3.config(state="disabled")

    #placeholder buttons - enabled state
    def enable_choices(self):
        self.c1.config(state="normal")
        self.c2.config(state="normal")
        self.c3.config(state="normal")  

    #button and hint text according to parts
    def button(self):
        if self.current_part == 1: #if displayed part is 1...
            self.dialogue_label.config(text=self.text_part1) #...show text_part1
            self.hints_label.config(text="Hint: Assess your surroundings.") #uses hint label customisation and adds the text
            self.enable_movement() #keybinds are enable to navigate
        elif self.current_part == 2:
            self.dialogue_label.config(text=self.text_part2)
            self.hints_label.config(text="Hint: Assess your surroundings.")
            self.enable_movement()
        elif self.current_part == 3:
            self.dialogue_label.config(text=self.text_part3)
            self.hints_label.config(text="Hint: Be careful in what you choose to do.")
            self.enable_choices() #makes button choices clickable   
            self.disable_movement() #disables keybind as choice is presented
            self.c1.config(text="Look outside your cell", command=lambda: [self.choice('c1p1'), self.enable_movement()]) #first option, labelled c1p1
            self.c2.config(text="Pretend to sleep", command=lambda: [self.choice('c2p1'), self.enable_movement()])
            self.c3.config(text="Eat the food on the tray", command=lambda: [self.choice('c3p1'), self.enable_movement()])
        elif self.current_part == 4:
            self.dialogue_label.config(text=self.text_part4)
            self.hints_label.config(text="Hint: Carefully consider your response.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Write back with “What’s going on?”", command=lambda: [self.choice('c1p2'), self.enable_movement()])
            self.c2.config(text="Leave the paper alone", command=lambda: [self.choice('c2p2'), self.enable_movement()])
            self.c3.config(text="Write back with “Who are you?”", command=lambda: [self.choice('c3p2'), self.enable_movement()])
        elif self.current_part == 5:
            self.dialogue_label.config(text=self.text_part5)
            self.hints_label.config(text="Hint: Be wary.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Very suspicious.", command=lambda: [self.choice('c1p3'), self.enable_movement()])
            self.c2.config(text="Ask, ‘How do we get out of here?’", command=lambda: [self.choice('c2p3'), self.enable_movement()])
            self.c3.config(text="Whisper loudly to get her attention", command=lambda: self.choice('c3p3')) #death choice so no need for enabling movement
        elif self.current_part == 6:
            self.dialogue_label.config(text=self.text_part6)
            self.hints_label.config(text="Hint: Two is better than one.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Question her on why she knows so much", command=lambda: [self.choice('c1p4'), self.enable_movement()])
            self.c2.config(text="I'm in.", command=lambda: [self.choice('c2p4'), self.enable_movement()])
            self.c3.config(text="Change your mind.", command=lambda: [self.choice('c3p4'), self.enable_movement()])
        elif self.current_part == 7:
            self.dialogue_label.config(text=self.text_part7)
            self.hints_label.config(text="Hint: Two is better than one.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Imitate the cell prisoners.", command=lambda: [self.choice('c1p5'), self.enable_movement()])
            self.c2.config(text="Peer to see who you've talked to", command=lambda: [self.choice('c2p5'), self.enable_movement()])
            self.c3.config(text="Stay seated. I'm not playing games.", command=lambda: [self.choice('c3p5'), self.enable_movement()])
        elif self.current_part == 8:
            self.dialogue_label.config(text=self.text_part8)
            self.hints_label.config(text="Hint: Maybe look behind you.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Look behind you, of course.", command=lambda: [self.choice('c1p6'), self.enable_movement()])
            self.c2.config(text="In a hushed tone, reply with “Yes?”", command=lambda: [self.choice('c2p6'), self.enable_movement()])
            self.c3.config(text="Pretend you didn't feel it.", command=lambda: [self.choice('c3p6'), self.enable_movement()])
        elif self.current_part == 9:
            self.dialogue_label.config(text=self.text_part9)
            self.hints_label.config(text="Hint: Read the clues carefully.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Red Wire", command=lambda: [self.choice('c1p7'), self.enable_movement()])
            self.c2.config(text="Blue Wire", command=lambda: [self.choice('c2p7'), self.enable_movement()])
            self.c3.config(text="Green Wire", command=lambda: [self.choice('c3p7'), self.enable_movement()])
        elif self.current_part == 10:   
            self.dialogue_label.config(text=self.text_part10)
            self.hints_label.config(text="Hint: Pick the screws with liquid resistance.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Screws with a rubber gasket", command=lambda: [self.choice('c1p8'), self.enable_movement()])
            self.c2.config(text="Screws with a washer", command=lambda: [self.choice('c2p8'), self.enable_movement()])
            self.c3.config(text="Screws with a nylon coating", command=lambda: [self.choice('c3p8'), self.enable_movement()])
        elif self.current_part == 11:
            self.dialogue_label.config(text=self.text_part11)
            self.hints_label.config(text="Hint: Think back to the coloured wires.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Press the ‘Blue’ Button", command=lambda: [self.choice('c1p9'), self.enable_movement()])
            self.c2.config(text="Press the ‘Red’ Button", command=lambda: [self.choice('c2p9'), self.enable_movement()])
            self.c3.config(text="Press the ‘Yellow’ Button", command=lambda: [self.choice('c3p9'), self.enable_movement()])
        elif self.current_part == 12:
            self.dialogue_label.config(text=self.text_part12)
            self.hints_label.config(text="Hint: Choose what you think will work.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Let's do it!", command=lambda: [self.choice('c1p10'), self.enable_movement()])
            self.c2.config(text="I don't know if we should.", command=lambda: [self.choice('c2p10'), self.enable_movement()])
            self.c3.config(text="What can go wrong?", command=lambda: [self.choice('c3p10'), self.enable_movement()])
        elif self.current_part == 13:
            self.dialogue_label.config(text=self.text_part13)
            self.hints_label.config(text="Hint: Choose what you think will work.")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Small bottle of Hydrochloric Acid", command=lambda: [self.choice('c1p11'), self.enable_movement()])
            self.c2.config(text="Tweezers", command=lambda: [self.choice('c2p11'), self.enable_movement()])
            self.c3.config(text="Beaker of Sulfuric Acid", command=lambda: [self.choice('c3p11'), self.enable_movement()])
        elif self.current_part == 14:
            self.dialogue_label.config(text=self.text_part14)
            self.hints_label.config(text="Hint: Tell more about yourself!")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Your pet dog, Rocco", command=lambda: [self.choice('c1p12'), self.enable_movement()])
            self.c2.config(text="That you like cheese", command=lambda: [self.choice('c2p12'), self.enable_movement()])
            self.c3.config(text="That you're investing in AAMD", command=lambda: [self.choice('c3p12'), self.enable_movement()])
        elif self.current_part == 15:
            self.dialogue_label.config(text=self.text_part15)
            self.hints_label.config(text="Hint: Should you escape now, or later?")
            self.enable_choices()
            self.disable_movement()
            self.c1.config(text="Escape now.", command=lambda: [self.choice('c1p13'), self.enable_movement()])
            self.c2.config(text="Escape later.", command=lambda: [self.choice('c2p13'), self.enable_movement()])
            self.c3.config(text="Flip a coin. Heads is now.", command=lambda: [self.choice('c3p13'), self.enable_movement()])

    #update for next part
    def next_part(self, event=None):
        if self.current_part < 15:
            self.current_part += 1 
            self.button()

    #update for previous part
    def previous_part(self, event=None):
        if self.current_part > 1:
            self.current_part -= 1
            self.button()

    #choices and the outcomes that follow
    def choice(self, choice):
        self.disable_choices()
        if choice == 'c1p1': #if user picks, show linked outcome
            self.dialogue_label.config(text=self.c1o1) #outcome
        elif choice == 'c2p1':
            self.dialogue_label.config(text=self.c2o1)
        elif choice == 'c3p1':
            self.dialogue_label.config(text=self.c3o1)
        elif choice == 'c1p2':
            self.dialogue_label.config(text=self.c1o2)
        elif choice == 'c2p2':
            self.dialogue_label.config(text=self.c2o2)
        elif choice == 'c3p2':
            self.dialogue_label.config(text=self.c3o2)
        elif choice == 'c1p3':
            self.dialogue_label.config(text=self.c1o3)
        elif choice == 'c2p3':
            self.dialogue_label.config(text=self.c2o3)
        elif choice == 'c3p3':
            self.dialogue_label.config(text=self.c3o3)
            self.dead() #shows deathscreen
        elif choice == 'c1p4':
            self.dialogue_label.config(text=self.c1o4)
        elif choice == 'c2p4':
            self.dialogue_label.config(text=self.c2o4)
        elif choice == 'c3p4':
            self.dialogue_label.config(text=self.c3o4)
        elif choice == 'c1p5':
            self.dialogue_label.config(text=self.c1o5)
        elif choice == 'c2p5':
            self.dialogue_label.config(text=self.c2o5)
        elif choice == 'c3p5':
            self.dialogue_label.config(text=self.c3o5)
            self.dead()
        elif choice == 'c1p6':
            self.dialogue_label.config(text=self.c1o6)
        elif choice == 'c2p6':
            self.dialogue_label.config(text=self.c2o6)
        elif choice == 'c3p6':
            self.dialogue_label.config(text=self.c3o6)
        elif choice == "c1p7":
            self.dialogue_label.config(text=self.c1o7)
        elif choice == "c2p7":
            self.dialogue_label.config(text=self.c2o7)
            self.dead()
        elif choice == "c3p7":
            self.dialogue_label.config(text=self.c2o7)
            self.dead()
        elif choice == "c1p8":
            self.dialogue_label.config(text=self.c1o8)
        elif choice == "c2p8":
            self.dialogue_label.config(text=self.c2o8)
            self.dead()
        elif choice == "c3p8":
            self.dialogue_label.config(text=self.c3o8)
        elif choice == "c1p9":
            self.dialogue_label.config(text=self.c1o9)
        elif choice == "c2p9":
            self.dialogue_label.config(text=self.c2o9)
            self.dead()
        elif choice == "c3p9":
            self.dialogue_label.config(text=self.c3o9)
            self.dead()
        elif choice == "c1p10":
            self.dialogue_label.config(text=self.c1o10)
        elif choice == "c2p10":
            self.dialogue_label.config(text=self.c2o10)
        elif choice == "c3p10":
            self.dialogue_label.config(text=self.c3o10)
        elif choice == "c1p11":
            self.dialogue_label.config(text=self.c1o11)
        elif choice == "c2p11":
            self.dialogue_label.config(text=self.c2o11)
        elif choice == "c3p11":
            self.dialogue_label.config(text=self.c3o11)
            self.dead()
        elif choice == "c1p12":
            self.dialogue_label.config(text=self.c1o12)
        elif choice == "c2p12":
            self.dialogue_label.config(text=self.c2o12)
        elif choice == "c3p12":
            self.dialogue_label.config(text=self.c3o12)
        elif choice == "c1p13":
            self.dialogue_label.config(text=self.c1o13)
        elif choice == "c2p13":
            self.dialogue_label.config(text=self.c2o13)
        elif choice == "c3p13":
            self.dialogue_label.config(text=self.c3o13)

    #help page and fullscreen
    def help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.attributes('-fullscreen', True)
        help_frame = tk.Frame(help_window, bg='white')
        help_frame.place(relwidth=1, relheight=1)

        #background image
        help_img= Image.open("bfgarage.jpg")
        help_img = help_img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        help_img = ImageTk.PhotoImage(help_img)

        #help and title label
        help_label = tk.Label(help_frame, image=help_img)
        help_label.place(relwidth=1, relheight=1)
        title_label = tk.Label(help_frame, text="Help", font=("MS Gothic", 50), bg='white')
        title_label.pack(pady=20)

        help_text = """
        How to Play:

        Besotted Fate is a story decision-based game where you wake up in a factory in an unknown location. 
        Your mission is to survive and escape, preferably shutting down this criminal enterprise.

        Press spacebar or arrow keys to continue with dialogue.
        Read through the dialogue and choose one out of three choices that you think is best. 
        This will lead you through an adventure that can lead to multiple different endings. 
        Every day is a checkpoint. If you die, you will be redirected to your latest day.

        To reset your progress, you can do this by going to play > settings > reset progress.

        Note that there is no audio within the game.

        Credits:
        KO. - Writer and Developer
        StableDiffusionWeb - AI Art Generator
        KD, KC - Assistance with Grammar and Storyline
        """

        text_label = tk.Label(help_frame, text=help_text, font=("MS Gothic", 18), bg='white', wraplength=help_window.winfo_screenwidth())
        text_label.pack(pady=20)

        #return button and customisation
        return_button = tk.Button(help_frame, text="Return", font=("MS Gothic", 18), command=help_window.destroy)
        return_button.pack(pady=20)
        help_label.img = help_img

    #setting page
    def settings(self): 
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.attributes('-fullscreen', True)
    
        #frame
        settings_frame = tk.Frame(settings_window)
        settings_frame.place(relwidth=1, relheight=1)

        #display background img
        settings_img = Image.open("bffire.jpg")
        settings_img = settings_img.resize((settings_window.winfo_screenwidth(), settings_window.winfo_screenheight()))
        settings_img = ImageTk.PhotoImage(settings_img)

        #label for bg img
        bg_label = tk.Label(settings_frame, image=settings_img)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.img = settings_img 

        #title
        title_label = tk.Label(settings_frame, text="Settings", font=("MS Gothic", 50), bg='white')
        title_label.pack(pady=20)
    
        #settings text
        settings_text = "Settings"
        text_label = tk.Label(settings_frame, text=settings_text, font=("MS Gothic", 18), bg='white', wraplength=settings_window.winfo_screenwidth())
        text_label.pack(pady=20)
    
        #additional help text
        help_text = "For help and additional information; \nContact Us - 20035@student.macleans.school.nz\n\nTo play again or restart, click button underneath.\n"
        help_label = tk.Label(settings_frame, text=help_text, font=("MS Gothic", 18), bg='white', wraplength=settings_window.winfo_screenwidth())
        help_label.pack(pady=10)

        #restart and exit button
        restart_button = tk.Button(settings_frame, text="Restart", font=("MS Gothic", 18), command=lambda:[self.restart_game(),settings_window.destroy()])
        restart_button.pack(pady=10)
        exit_button = tk.Button(settings_frame, text="Exit", font=("MS Gothic", 18), command=self.root.quit)
        exit_button.pack(pady=10)
    
        
    #death screen
    def dead(self):
        death_window = tk.Toplevel(self.root)
        death_window.title("Game Over")
        death_window.attributes('-fullscreen', True) 
        death_frame = tk.Frame(death_window, bg='white')
        death_frame.place(relwidth=1, relheight=1)

        #background image
        death_img = Image.open("bfdeath.jpg")
        death_img = death_img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        death_img = ImageTk.PhotoImage(death_img)

        #death and title labels
        death_label = tk.Label(death_frame, image=death_img)
        death_label.place(relwidth=1, relheight=1)
        title_label = tk.Label(death_frame, text="Game Over", font=("MS Gothic", 50), bg='white')
        title_label.pack(pady=20)
        death_text_label = tk.Label(death_frame, text=" \n At long last, you have met your fate.  \n  You have died, and your body is incinerated in a blast furnace.  \n You are now but a statistic in the evil world of Dr. Galhass who takes profit over people.  \n \n If you wish to revisit your options, click the restart button.  \n \n " , font=("MS Gothic", 24), bg='white')
        death_text_label.pack(pady=(5, 20)) 

        #restart and exit button
        restart_button = tk.Button(death_frame, text="Restart", font=("MS Gothic", 18), command=lambda:[self.restart_game(),death_window.destroy()])
        restart_button.pack(pady=10)
        exit_button = tk.Button(death_frame, text="Exit", font=("MS Gothic", 18), command=self.root.quit)
        exit_button.pack(pady=10)
        death_label.img = death_img

#restart function
    def restart_game(self):
        self.current_text = self.text_part1 #sets it to beginning text
        self.dialogue_label.config(text=self.current_text)
        self.current_part = 1
        self.c1.config(text="Look outside your cell", command=lambda: self.choice('c1p1')) #use placeholder button
        self.c2.config(text="Pretend to sleep", command=lambda: self.choice('c2p1'))
        self.c3.config(text="Eat the food on the tray", command=lambda: self.choice('c3p1'))
        self.disable_choices() #do not allow choices to be clicked
        self.enable_movement() #enables keybind navigation
        
if __name__ == "__main__":
    root = tk.Tk()
    app = BesottedFate(root)
    root.mainloop()
