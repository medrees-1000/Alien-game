from sys import exit
from random import randint
from textwrap import dedent


class Scene:

    def enter(self):
        print("this Scene has not been configured yet")
        print("Subclass it and implement enter()" )
        exit(1)
    def combat(self):
        print("This is the combat system")
        exit(1)
class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
       current_scene = self.scene_map.opening_scene()
       last_scene = self.scene_map.next_scene("finished")
       
       while current_scene != last_scene:
           next_scene_name = current_scene.enter()
           current_scene = self.scene_map.next_scene(next_scene_name)

       current_scene.enter()
       
class Death(Scene):

    quip = ["""
            you lost, 
            such a loser, 
            you can do better
                         """
 ]


    def enter(self):
        print(Death.quip[randint(0, len(self.quip)-1)])
        exit(1)
    

    def combat(self):
        print("You Suck man learn some fighting ")
        exit(1)



class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

             You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
"""))
        action = input("> ")

        if action == "tell a joke":
            print(dedent("""Quick on the draw you yank out your blaster and fire
  it at the Gothon. His clown costume is flowing and
    moving around his body, which throws off your aim.
  Your laser hits his costume but misses him entirely.
   This completely ruins his brand new costume his mother
 bought him, which makes him fly into an insane rage
  and blast you repeatedly in the face until you are
   dead. Then he eats you."""))
            
            return "death"
        elif action == "doge":
            print(dedent("""
 Like a world class boxer you dodge, weave, slip and
 slide right as the Gothon's blaster cranks a laser
  past your head. In the middle of your artful dodge
  your foot slips and you bang your head on the metal
    wall and pass out. You wake up shortly after only to
 die as the Gothon stomps on your head and eats you.

                          """))
            return "death"
        
        elif action == "shoot":
            print(dedent("""
  Lucky for you they made you learn Gothon insults in
  the academy. You tell the one Gothon joke you know:
  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
   fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
   not to laugh, then busts out laughing and can't move.
 While he's laughing you run up and shoot him square in
   the head putting him down, then jump through the
 Weapon Armory door.
   """))
            return "laser_weapon_armory"
        else:
            print("Does not compute")
            return "central_corridor"
        


    def combat(self):
        print("to do these actions you need to combat and these are your options ")
        print("1. shoot ")
        print("2, tell a joke , if your chose this you seriously need to consider your life choices ")
        print("3, dodge ")

        choice = input("So tell me what do you do and hurry up not enought time: ")

        if choice == "2":
            print("You tell a joke but the gothon is not entartained ")
            return "death"
        elif choice == "3":
            print("How can you dodge such a big creature")
            return "death"
        elif choice == "1":
            print("You are badass the goton is killed ")
            return "laser_weapon_armory"
        else:
            print("Does not compute")
            return "central_corridor"


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                    You do a dive roll into the Weapon Armory, crouch and scan
                    the room for more Gothons that might be hiding. It's dead
                    quiet, too quiet. You stand up and run to the far side of
                    the room and find the neutron bomb in its container.
                    There's a keypad lock on the box and you need the code to
                    get the bomb out. If you get the code wrong 10 times then
                    the lock closes forever and you can't get the bomb. The
                    code is 3 digits.

                    """))
        code = "123"
        guess = str(input("[keypad]> "))   
        guesess = 0

        while guess != code and guesess < 10:
            print("BUZZZED")
            guesess += 1
            guess = input("[Keypad]> ")


        if guess == code:
            print(dedent("""The container clicks open and the seal breaks, letting
                            gas out. You grab the neutron bomb and run as fast as
                            you can to the bridge where you must place it in the
                            right spot."""))
            return "the_bridge"
        else:
            print(dedent("""
                           The lock buzzes one last time and then you hear a
                        sickening melting sound as the mechanism is fused
                        together. You decide to sit there, and finally the
                        Gothons blow up the ship from their ship and you die. 
                            """))
            return "death"

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
                        You burst onto the Bridge with the netron destruct bomb
                            under your arm and surprise 5 Gothons who are trying to
                            take control of the ship. Each of them has an even uglier
                            clown costume than the last. They haven't pulled their
                            weapons out yet, as they see the active bomb under your
                            arm and don't want to set it off.
                        """))
        
        choice = input("> ")

        if choice == "throw the bomb":
            print(dedent("""In a panic you throw the bomb at the group of Gothons
                            and make a leap for the door. Right as you drop it a
                            Gothon shoots you right in the back killing you. As
                            you die you see another Gothon frantically try to
                            disarm the bomb. You die knowing they will probably
                            blow up when it goes off.
                                    """))
            return 'death'
        
        elif choice == "slowly put the bomb down":
            print(dedent("""You point your blaster at the bomb under your arm and
                            Gothons put their hands up and start to sweat.
                            You inch backward to the door, open it, and then
                            carefully place the bomb on the floor, pointing your
                            blaster at it. You then jump back through the door,
                            punch the close button and blast the lock so the
                            Gothons can't get out. Now that the bomb is placed
                            you run to the escape pod to get off this tin can."""))
            return "EscapePod"
        else:
            print("Does not compute ")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                    You rush through the ship desperately trying to make it to
                    the escape pod before the whole ship explodes. It seems
                    like hardly any Gothons are on the ship, so your run is
                    clear of interference. You get to the chamber with the
                    escape pods, and now need to pick one to take. Some of
                    them could be damaged but you don't have time to look.
                    There's 5 pods, which one do you take?"""))
        
        good_pod = randint(1,5)
        guess_num = input("[pod #]> ")

        if int(guess_num) != good_pod:
            print(dedent("""You jump into pod {guess_num} and hit the eject button.
                            The pod escapes out into the void of space, then
                            implodes as the hull ruptures, crushing your body into
                            jam jelly."""))
            return "death"
        else:
            print(dedent("""
                    You jump into pod {guess_num} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below. As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time. You won!
                    """))
            return "finished"
        

class Finished(Scene):

    
    def enter(self):
        print("you won good job")
        return "finished"



class Map:

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'EscapePod': EscapePod(),
        'death': Death(),
        'finished': Finished(),

    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()


        