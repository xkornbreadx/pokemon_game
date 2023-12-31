import random
import time

def slow_type(text, delay=0.008):

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def new_line():
    slow_type("------------------------------------")

def get_valid_input(prompt, options=[]):
    while True:
        try:
            user_input = input(prompt)
            if int(user_input) in options:
                return int(user_input)
            slow_type("That's not a valid option. Please try again.")
        except ValueError:
            slow_type("That's not a valid option. Please try again.")

class Move:
    
    def __init__(self, name, mtype, power, accuracy, special=False, status=None, stat=None, stat_change=None, stat_target=None):
        self.name = name
        self.mtype = mtype
        self.power = power
        self.accuracy = accuracy
        self.special = special
        self.status = status
        self.stat = stat
        self.stat_change = stat_change
        self.stat_target = stat_target

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

#Types:
#'water'
#'fire'
#'grass'
#'normal'
#'electric'
#'ground'
#'rock'
#'poison'

# moves
    
#HMs
cut = Move("Cut", 'normal', 5.5, 95)

ember = Move("Ember", 'fire', 4, 90)
water_gun = Move("Water Gun", 'water', 4, 90)
vine_whip = Move("Vine Whip", 'grass', 4, 90)
thunder_shock = Move("Thunder Shock", 'electric', 4, 100)
tackle = Move("Tackle", 'normal', 4, 100)
astonish = Move("Astonish", 'ghost', 3, 100)
poison_sting = Move("Poison Sting", 'poison', 3, 100, special=True, status='poisoned')
yawn = Move("Yawn", 'normal', 0, 50, special=True, status='asleep')
confuse_ray = Move("Confuse Ray", 'ghost', 0, 100, special=True, status='confused')
supersonic = Move("Supersonic", 'normal', 0, 55, special=True, status='confused')
thunder_wave = Move("Thunder Wave", 'electric', 0, 90, special=True, status='paralyzed')
electro_ball = Move("Electro Ball", 'electric', 6, 100)
swift = Move("Swift", 'normal', 6.5, 100)
howl = Move("Howl", 'normal', 0, 100, stat='attack', stat_change=0.9, stat_target='user')
thunderbolt = Move("Thunderbolt", 'electric', 9, 100)
sludge_bomb = Move("Sludge Bomb", 'poison', 9, 100)
thunder = Move("Thunder", 'electric', 11, 70)
gunk_shot = Move("Gunk Shot", 'poison', 11, 80)
splash = Move("Spash", 'normal', 0, 50)
earth_power = Move("Earth Power", 'ground', 8, 100)
wing_attack = Move("Wing Attack", 'flying', 4.5, 90)
drill_peck = Move("Drill Peck", 'flying', 8, 100)
peck = Move("Peck", 'flying', 3.5, 100)
hyper_voice = Move("Hyper Voice", 'normal', 9, 100)
horn_attack = Move("Horn Attack", 'normal', 7, 100)
waterfall = Move("Waterfall", 'water', 8, 100)
megahorn = Move("Megahorn", 'bug', 11, 85)
scratch = Move("Scratch", 'normal', 5, 95)
spark = Move("Spark", 'normal', 5, 100)
mud_slap = Move("Mud Slap", 'ground', 4, 100)
mega_drain = Move("Mega Drain", 'grass', 5, 100)
bulldoze = Move("Bulldoze", 'ground', 6, 85)
rock_blast = Move("Rock Blast", 'rock', 6.5, 90)
rock_slide = Move("Rock Slide", 'rock', 7, 90)
confusion = Move("Confusion", 'psychic', 6.5, 100)
acid = Move("Acid", 'poison', 4.5, 100)
rollout = Move("Rollout", 'rock', 4.5, 90)
dig = Move("Dig", 'ground', 8, 100)
toxic = Move("Toxic", 'poison', 0, 80, special=True, status='poisoned')
paralyze = Move("Paralyze", 'electric', 0, 60, special=True, status='paralyzed')
bug_bite = Move("Bug Bite", 'bug', 5, 85)
psychic = Move("Psychic", 'psychic', 9, 90)
shadow_ball = Move("Shadow Ball", 'ghost', 8, 90)
rock_throw = Move("Rock Throw", 'rock', 6, 85)
stone_edge = Move("Stone Edge", 'rock', 100, 80)
low_kick = Move("Low Kick", 'fighting', 5, 90)
aqua_tail = Move("Aqua Tail", 'water', 7, 90)
flame_wheel = Move("Flame Wheel", 'fire', 6, 90)
razor_leaf = Move("Razor Leaf", 'grass', 7, 95)
smog = Move("Smog", 'poison', 3, 70, special=True, status='poisoned')
earthquake = Move("Earthquake", 'ground', 9, 90)
seismic_toss = Move("Seismic Toss", 'fighting', 6.5, 100)
bug_buzz = Move("Bug Buzz", 'bug', 8, 90)
cross_chop = Move("Cross Chop", 'fighting', 9.5, 80)
close_combat = Move("Close Combat", 'fighting', 11, 80)
swagger = Move("Swagger", 'normal', 0, 85, stat='attack', stat_change=0.9, stat_target='user')
aerial_ace = Move("Aerial Ace", 'flying', 8, 90)
absorb = Move("Absorb", 'grass', 3.5, 100)
rock_polish = Move("Rock Polish", 'rock', 0, 100, stat='attack', stat_change=0.9, stat_target='user')
discharge = Move("Discharge", 'electric', 8, 100)
poison_fang = Move("Poison Fang", 'poison', 5.5, 100)
swords_dance = Move("Swords Dance", 'normal', 0, 100, stat='attack', stat_change=0.85, stat_target='user')
defense_curl = Move("Defense Curl", 'normal', 0, 100, stat='defense', stat_change=0.9, stat_target='user')
screech = Move("Screech", 'normal', 0, 85, stat='defense', stat_change=0.85, stat_target='enemy')
leer = Move("Leer", 'normal', 0, 100, stat='defense', stat_change=0.9, stat_target='enemy')
charge = Move("Charge", 'electric', 0, 100, stat='attack', stat_change=0.9, stat_target='user')
tail_whip = Move("Tail Whip", 'normal', 0, 100, stat='defense', stat_change=0.9, stat_target='enemy')
growth = Move("Growth", 'normal', 0, 100, stat='attack', stat_change=0.9, stat_target='user')
growl = Move("Growl", 'normal', 0, 100, stat='attack', stat_change=0.9, stat_target='enemy')
fire_fang = Move("Fire Fang", 'fire', 7.5, 95)
zap_cannon = Move("Zap Cannon", 'electric', 11, 50)
slash = Move("Slash", 'normal', 7, 100)
hypnosis = Move("Hypnosis", 'psychic', 0, 60, special=True, status='asleep')
ancient_power = Move("Ancient Power", 'rock', 6, 100)
lick = Move("Lick", 'ghost', 3.5, 100)
night_shade = Move("Night Shade", 'ghost', 7, 100)
powder_snow = Move("Powder Snow", 'ice', 4, 100)
freeze_dry = Move("Freeze-Dry", 'ice', 7, 100)
mist = Move("Mist", 'ice', 0, 100, stat='attack', stat_change=0.9, stat_target='user')
spite = Move("Spite", 'ghost', 5, 100)
hex = Move("Hex", 'ghost', 6, 100)
hurricane = Move("Hurricane", 'flying', 11, 70)
ice_shard = Move("Ice Shard", 'ice', 4.5, 100)
fly = Move("Fly", 'flying', 9, 100)
flamethrower = Move("Flamethrower", 'fire', 9, 100)
stun_spore = Move("Stun Spore", 'grass', 0, 75, special=True, status='paralyzed')
flare_blitz = Move("Flare Blitz", 'fire', 11, 60)
nuzzle = Move("Nuzzle", 'electric', 3, 100, special=True, status='paralyzed')
slap = Move("Slap", 'normal', 4, 100)
poison_powder = Move("Poison Powder", 'poison', 0, 75, special=True, status='poisoned')
sleep_powder = Move("Sleep Powder", 'grass', 0, 75, special=True, status='asleep')
seed_bomb = Move("Seed Bomb", 'grass', 8, 100)
power_whip = Move("Power Whip", 'grass', 11, 60)
sing = Move("Sing", 'normal', 0, 55, special=True, status='asleep')
rapid_spin = Move("Rapid Spin", 'normal', 7, 100)
ice_beam = Move("Ice Beam", 'ice', 9, 100)
crab_hammer = Move("Crab Hammer", 'water', 10, 90)
bubble_beam = Move("Bubblebeam", 'water', 5.5, 100)
mud_shot = Move("Mud Shot", 'ground', 5.5, 100)
surf = Move("Surf", 'water', 9, 100)
aurora_beam = Move("Aurora Beam", 'ice', 6.5, 100)
giga_drain = Move("Giga Drain", 'grass', 8, 100)
water_pulse = Move("Water Pulse", 'water', 7.5, 100)
shell_smash = Move("Shell Smash", 'normal', 0, 100, stat='defense', stat_change=0.85, stat_target='enemy')
iron_defense = Move("Iron Defense", 'normal', 0, 100, stat='defense', stat_change=0.85, stat_target='user')
hydro_pump = Move("Hydro Pump", 'water', 11, 60)
psyshock = Move("Psyshock", 'psychic', 7, 100)
psybeam = Move("Psybeam", 'psychic', 8, 100)
hex = Move("Hex", 'ghost', 6.5, 100)
headbutt = Move("Headbutt", 'normal', 7, 100)
psycho_cut = Move("Psycho Cut", 'psychic', 7.5, 100)
covet = Move("Covet", 'normal', 6, 100)
power_gem = Move("Power Gem", 'rock', 8, 100)
zen_headbutt = Move("Zen Headbutt", 'psychic', 8, 90)
harden = Move("Harden", 'normal', 0, 100, stat='defense', stat_change = 0.9, stat_target='user')
venoshock = Move("Venoshock", 'poison', 7, 100)
poison_jab = Move("Poison Jab", 'poison', 8, 100)

# move sets
fire_moves = [ember, tackle, yawn, confuse_ray]
grass_moves = [vine_whip, tackle, toxic, confuse_ray]
water_moves = [water_gun, tackle, yawn, confuse_ray]
god_moves = [growth, ember, leer, toxic]

class Pokemon:
	
    id = 1

    def __init__(self, species, hp, ptype, attack, defense, level, move_set, name="", player_owned=False):
        self.base_hp = hp
        self.base_attack = attack
        self.base_defense = defense
        self.species = species
        self.ptype = ptype        
        self.maxhp = round(self.base_hp*(level/5)*.7)
        self.hp = self.maxhp
        self.attack = round(self.base_attack*(level/5), 2)
        self.defense = round(self.base_defense*(level/5), 2)
        self.level = level
        self.move_set = move_set
        self.name = self.species
        if name != "":
            self.name = name
        self.player_owned = player_owned
        self.xp = 0
        self.asleep_counter = 0
        self.confused_counter = 0
        self.poisoned_counter = 1
        self.paralyzed = False
        self.poisoned = False
        self.asleep = False
        self.confused = False
        self.evolved1 = False
        self.evolved2 = False
        self.learnable_moves = {}
        self.id = Pokemon.id
        Pokemon.id += 1

        # weaknesses
        if ptype == 'fire':
            self.weakness = ['water', 'ground', 'rock']
        if ptype == 'water':
            self.weakness = ['grass', 'electric']
        if ptype == 'grass':
            self.weakness = ['fire', 'flying', 'poison', 'bug', 'ice']
        if ptype == 'normal':
            self.weakness = ['fighting']
        if ptype == 'electric':
            self.weakness = ['ground']
        if ptype == 'ground':
            self.weakness = ['water', 'grass', 'ice']
        if ptype == 'rock':
            self.weakness = ['water', 'grass', 'ground', 'fighting']
        if ptype == 'poison':
            self.weakness = ['ground', 'psychic', 'bug']
        if ptype == 'psychic':
            self.weakness = ['bug']
        if ptype == 'fighting':
            self.weakness = ['flying', 'psychic']
        if ptype == 'flying':
            self.weakness = ['rock', 'electric', 'ice']
        if ptype == 'bug':
            self.weakness = ['flying', 'poison', 'rock', 'fire']
        if ptype == 'ghost':
            self.weakness = ['ghost']
        if ptype == 'ice':
            self.weakness = ['fighting', 'rock', 'fire']

        # resistances
        if ptype == 'fire':
            self.resistance = ['grass', 'fire', 'bug']
        if ptype == 'water':
            self.resistance = ['fire', 'water', 'ice']
        if ptype == 'grass':
            self.resistance = ['water', 'grass', 'ground', 'electric']
        if ptype == 'normal':
            self.resistance = ['ghost']
        if ptype == 'electric':
            self.resistance = ['electric', 'flying']
        if ptype == 'ground':
            self.resistance = ['electric', 'poison', 'rock']
        if ptype == 'rock':
            self.resistance = ['fire', 'normal', 'flying', 'poison']
        if ptype == 'fighting':
            self.resistance = ['rock', 'bug']
        if ptype == 'flying':
            self.resistance = ['fighting', 'ground', 'bug', 'grass']
        if ptype == 'poison':
            self.resistance = ['fighting', 'poison', 'grass']
        if ptype == 'bug':
            self.resistance = ['fighting', 'ground', 'grass']
        if ptype == 'ghost':
            self.resistance = ['normal', 'fighting', 'poison', 'bug']
        if ptype == 'psychic':
            self.resistance = ['fighting', 'ghost', 'psychic']
        if ptype == 'ice':
            self.resistance = ['ice']

    def update_stats(self, level):
        self.maxhp = round(self.base_hp*(level/5)*.7)
        self.attack = round(self.base_attack*(level/5), 2)
        self.defense = round(self.base_defense*(level/5), 2)
    
    def __repr__(self):
        return self.name
    
    def level_up(self):
        new_level = self.level + 1
        slow_type(f"{self} leveled up from LVL {self.level} to LVL {new_level}!")
        self.level = new_level

    def xp_boost(self, xp):
        if self.player_owned:
            new_line()
            self.xp += xp
            slow_type(f"{self.name} gained {xp} XP. {self.xp}/100")
            while self.xp >= 100:
                self.level_up()
                for key, val in self.__class__.learnable_moves.items():
                    if key == self.level:
                        self.learn_move(key, val)
                self.xp -= 100
            time.sleep(0.5)


    def learn_move(self, level=0, moves=[], tm=None):
        approved=False
        if tm is None:
            if self.level == level:
                approved = True
        else:
            if (tm.itype == 'tmhm' and not tm.move == fly) or (self.ptype == 'flying' and tm.move == fly):
                approved = True
        if approved:
            time.sleep(0.5)
            new_line()
            move_name_list = [move2.name for move2 in self.move_set]
            for move in moves:
                if not move.name in move_name_list:
                    if len(self.move_set) < 4:
                        slow_type(f"{self.name} learned {move}!")
                        self.move_set.append(move)
                        time.sleep(1)
                    else:
                        slow_type(f"{self.name} is trying to learn {move}.")
                        time.sleep(0.5)
                        slow_type("Delete a move to make room?\n1. Yes\n2. No")
                        choice = get_valid_input("Enter number: ", [1, 2])
                        if choice == 1:
                            new_line()
                            slow_type(f"\n{move}" + (f" | Power: {move.power}" if not move.special else f" | Status: {move.status.capitalize()}") + (f" | Accuracy: {move.accuracy}\n"))
                            for index, value in enumerate(self.move_set):
                                slow_type(f"{index + 1}. {value}" + (f" | Power: {value.power}" if not value.special else f" | Status: {value.status.capitalize()}") + (f" | Accuracy: {value.accuracy}"))
                            move_index = get_valid_input("Enter number: ", [1, 2, 3, 4])-1
                            slow_type(f"{self.name} forgot {self.move_set[move_index]}...")
                            time.sleep(1)
                            slow_type(f"...and learned {move}!")
                            time.sleep(0.5)
                            self.move_set[move_index] = move
                        elif choice == 2:
                            continue
                else:
                    slow_type(f"{self.name} tried to learn {move} but already knows it...")
                    time.sleep(1)
        else:
            slow_type(f"{self} was unable to learn a move...")
    
    @classmethod
    def generate_moves(cls, level):
        possible_moves = []
        while len(possible_moves) < 2:
            for key, val in cls.learnable_moves.items():
                if level >= key:
                    for move in val:
                        if move not in possible_moves and random.randint(1,101) < 70:
                            possible_moves.append(move)
        if len(possible_moves) > 4:
            while len(possible_moves) > 4:
                possible_moves.pop(0)
        return possible_moves

    def status_heal(self):
        self.asleep = False
        self.confused = False
        self.poisoned = False
        self.paralyzed = False
        self.asleep_counter = 0
        self.poisoned_counter = 1
        self.confused_counter = 0

    def evolve(self):
        if self.evolve_level1 <= self.level and self.evolved1 == False:
            new_line()
            slow_type(f"Your {self.name} is evolving!")
            time.sleep(1)
            slow_type("......", 0.5)
            slow_type("Congratulations!")
            time.sleep(1)
            slow_type(f"Your {self.name} evolved into {self.evolve_pokemon1}!")
            time.sleep(0.5)
            self.species = self.evolve_pokemon1.species
            self.base_attack = self.evolve_pokemon1.base_attack
            self.base_defense = self.evolve_pokemon1.base_defense
            self.base_hp = self.evolve_pokemon1.base_hp
            self.ptype = self.evolve_pokemon1.ptype
            self.update_stats(self.level)
            slow_type(f"{self.evolve_pokemon1} was registered in the Pokedex.")
            time.sleep(1)
            self.evolved1 = True
            return self.evolve_pokemon1, True
        elif self.evolve_level2 <= self.level and self.evolved2 == False:
            new_line()
            slow_type(f"Your {self.name} is evolving!")
            time.sleep(1)
            slow_type("......", 0.5)
            slow_type("Congratulations!")
            time.sleep(1)
            slow_type(f"Your {self.name} evolved into {self.evolve_pokemon2}!")
            time.sleep(0.5)
            self.species = self.evolve_pokemon2.species
            self.base_attack = self.evolve_pokemon2.base_attack
            self.base_defense = self.evolve_pokemon2.base_defense
            self.base_hp = self.evolve_pokemon2.base_hp
            self.ptype = self.evolve_pokemon2.ptype
            self.update_stats(self.level)
            slow_type(f"{self.evolve_pokemon2} was registered in the Pokedex.")
            time.sleep(1)
            self.evolved2 = True
            return self.evolve_pokemon2, True

    @classmethod
    def generate(cls, level, moves=None):
        if moves is None:
            moves = cls.generate_moves(level)
        yield cls(level=level, moves=moves)

# pokemon subclasses
class Charmander(Pokemon):

    learnable_moves = {1: [growl, scratch], 4: [ember], 9: [flame_wheel], 16: [fire_fang], 20: [slash], 24: [flamethrower], 36: [flare_blitz]}
    
    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Charmander', 35, 'fire', 1.95, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 16
        self.evolve_pokemon1 = Charmeleon()
        self.evolve_level2 = 36
        self.evolve_pokemon2 = Charizard()

class Charmeleon(Pokemon):

    learnable_moves = Charmander.learnable_moves
    
    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Charmeleon', 40, 'fire', 2.1, 2, level, moves, name, player_owned)
        self.evolve_level1 = 36
        self.evolve_pokemon1 = Charizard()

class Charizard(Pokemon):

    learnable_moves = Charmander.learnable_moves
    
    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Charizard', 45, 'fire', 2.25, 2, level, moves, name, player_owned)

class Bulbasaur(Pokemon):

    learnable_moves = {1: [growl, tackle], 4: [vine_whip], 7: [confuse_ray], 15: [poison_powder], 15: [sleep_powder], 18: [seed_bomb], 33: [power_whip]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Bulbasaur', 40, 'grass', 1.9, 2.1, level, moves, name, player_owned)
        self.evolve_level1 = 16
        self.evolve_pokemon1 = Ivysaur()
        self.evolve_level2 = 32
        self.evolve_pokemon2 = Venusaur()

class Ivysaur(Pokemon):

    learnable_moves = Bulbasaur.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Ivysaur', 43, 'grass', 2, 2.2, level, moves, name, player_owned)
        self.evolve_level1 = 32
        self.evolve_pokemon1 = Venusaur()

class Venusaur(Pokemon):

    learnable_moves = Bulbasaur.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Venusaur', 44, 'grass', 2.1, 2.4, level, moves, name, player_owned)
    
class Squirtle(Pokemon):

    learnable_moves = {1: [tackle, tail_whip], 4: [water_gun], 9: [rapid_spin], 15: [water_pulse], 24: [aqua_tail], 27: [shell_smash], 30: [iron_defense], 33: [hydro_pump]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Squirtle', 38, 'water', 2, 2, level, moves, name, player_owned)
        self.evolve_level1 = 16
        self.evolve_pokemon1 = Wartortle()
        self.evolve_level2 = 32
        self.evolve_pokemon2 = Blastoise()

class Wartortle(Pokemon):

    learnable_moves = Squirtle.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Wartortle', 42, 'water', 2.1, 2.1, level, moves, name, player_owned)
        self.evolve_level1 = 32
        self.evolve_pokemon1 = Blastoise()

class Blastoise(Pokemon):

    learnable_moves = Squirtle.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Blastoise', 42, 'water', 2.2, 2.2, level, moves, name, player_owned)

class Rattata(Pokemon):

    learnable_moves = {1: [tackle, tail_whip], 8: [scratch], 20: [slash]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Rattata', 40, 'normal', 1.8, 1.9, level, moves, name, player_owned)
        self.evolve_pokemon1 = Raticate()
        self.evolve_level1 = 20

class Raticate(Pokemon):

    learnable_moves = Rattata.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Raticate', 42, 'normal', 2.1, 2.1, level, moves, name, player_owned)

class Staryu(Pokemon):

    learnable_moves = {1: [harden, tackle], 4: [water_gun], 8: [confuse_ray], 12: [rapid_spin], 20: [psybeam], 27: [water_pulse], 36: [power_gem], 50: [hydro_pump]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Staryu', 38, 'water', 2.1, 2, level, moves, name, player_owned)
        self.evolve_pokemon1 = Starmie()
        self.evolve_level1 = 36
        
class Starmie(Pokemon):

    learnable_moves = Staryu.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Starmie', 41, 'water', 2.2, 2.1, level, moves, name, player_owned)
        
class Goldeen(Pokemon):

    learnable_moves = {1: [peck, tail_whip], 5: [supersonic], 10: [water_pulse], 15: [horn_attack], 25: [aqua_tail], 35: [waterfall], 45: [megahorn]}
    
    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Goldeen', 37, 'water', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 33
        self.evolve_pokemon1 = Seaking()
        
class Seaking(Pokemon):

    learnable_moves = Goldeen.learnable_moves
    
    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Seaking', 42, 'water', 2, 2.1, level, moves, name, player_owned)

class Magikarp(Pokemon):

    learnable_moves = {1: [splash, defense_curl], 15: [tackle], 21: [waterfall], 32: [aqua_tail], 40: [hydro_pump]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Magikarp', 38, 'water', 1.5, 1.5, level, moves, name, player_owned)
        self.evolve_level1 = 20
        self.evolve_pokemon1 = Gyarados()
        self.learnable_moves = {20: water_gun, 20: tackle}

class Gyarados(Pokemon):

    learnable_moves = Magikarp.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Gyarados', 42, 'water', 2.3, 2.2, level, moves, name, player_owned)

class Caterpie(Pokemon):

    learnable_moves = {1: [harden, tackle], 4: [supersonic], 9: [bug_bite], 10: [confusion], 12: [sleep_powder, poison_powder], 16: [psybeam], 24: [aerial_ace], 32: [bug_buzz]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Caterpie', 36, 'bug', 1.8, 1.8, level, moves, name, player_owned)
        self.evolve_level1 = 7
        self.evolve_pokemon1 = Metapod()
        self.evolve_level2 = 10
        self.evolve_pokemon2 = Butterfree()

class Metapod(Pokemon):

    learnable_moves = Caterpie.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Metapod', 42, 'bug', 1.8, 2.2, level, moves, name, player_owned)
        self.evolve_level1 = 10
        self.evolve_pokemon1 = Butterfree()

class Butterfree(Pokemon):

    learnable_moves = Caterpie.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Butterfree', 41, 'bug', 2, 2, level, moves, name, player_owned)

class Vulpix(Pokemon):

    learnable_moves = {1: [ember, tail_whip], 10: [flame_wheel], 20: [confuse_ray], 32: [flamethrower], 45: [flare_blitz]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Vulpix', 38, 'fire', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 32
        self.evolve_pokemon1 = Ninetales()

class Ninetales(Pokemon):

    learnable_moves = Vulpix.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Ninetales', 42, 'fire', 2.15, 2.05, level, moves, name, player_owned)

class Pidgey(Pokemon):

    learnable_moves = {1: [growl, tackle], 7: [peck], 20: [wing_attack], 30: [aerial_ace]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Pidgey', 37, 'flying', 2, 1.9, level, moves, name, player_owned)
        self.evolve_pokemon1 = Pidgeotto()
        self.evolve_level1 = 18
        self.evolve_pokemon2 = Pidgeot()
        self.evolve_level2 = 36

class Pidgeotto(Pokemon):

    learnable_moves = Pidgey.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Pidgeotto', 38, 'flying', 2.1, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 36
        self.evolve_pokemon1 = Pidgeot()

class Pidgeot(Pokemon):

    learnable_moves = Pidgey.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Pidgeot', 41, 'flying', 2.3, 2, level, moves, name, player_owned)

class Weedle(Pokemon):

    learnable_moves = {1: [growl, poison_powder], 7: [harden], 11: [bug_bite], 20: [venoshock], 35: [poison_jab]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Weedle', 37, 'bug', 1.8, 1.8, level, moves, name, player_owned)
        self.evolve_level1 = 7
        self.evolve_pokemon1 = Kakuna()
        self.evolve_level2 = 10
        self.evolve_pokemon2 = Beedrill()

class Kakuna(Pokemon):

    learnable_moves = Weedle.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Kakuna', 42, 'bug', 1.8, 2.2, level, moves, name, player_owned)
        self.evolve_level1 = 10
        self.evolve_pokemon1 = Beedrill()

class Beedrill(Pokemon):

    learnable_moves = Weedle.learnable_moves

    def __init__(self, level=12, name='', moves=None, player_owned=False):
        super().__init__('Beedrill', 41, 'bug', 2, 2, level, moves, name, player_owned)

class Pikachu(Pokemon):

    learnable_moves = {1: [growl, nuzzle, tackle, tail_whip], 4: [thunder_wave], 12: [electro_ball], 20: [spark], 32: [thunderbolt], 42: [thunder]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Pikachu', 40, 'electric', 2, 1.9, level, moves, name, player_owned)

class Raichu(Pokemon):

    learnable_moves = Pikachu.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Raichu', 42, 'electric', 2.25, 2, level, moves, name, player_owned)

class Diglett(Pokemon):

    learnable_moves = {1: [scratch], 4: [growl], 8: [astonish],  11: [mud_slap], 15: [bulldoze], 23: [slash], 30: [dig], 36: [earth_power], 40: [earthquake]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Diglett', 40, 'ground', 1.8, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 26
        self.evolve_pokemon1 = Dugtrio()

class Dugtrio(Pokemon):

    learnable_moves = Diglett.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Dugtrio', 43, 'ground', 2.1, 2, level, moves, name, player_owned)

class Cubone(Pokemon):

    learnable_moves = {1: [growl, mud_slap], 4: [tail_whip], 8: [tackle], 12: [headbutt], 20: [bulldoze], 28: [earth_power], 30: [dig], 40: [earthquake]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Cubone', 40, 'ground', 2.05, 1.85, level, moves, name, player_owned)
        self.evolve_level1 = 28
        self.evolve_pokemon1 = Marowak()

class Marowak(Pokemon):

    learnable_moves = Cubone.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Marowak', 42, 'ground', 2.3, 2, level, moves, name, player_owned)

class Magnemite(Pokemon):

    learnable_moves = {1: [tackle, thunder_shock], 4: [supersonic], 8: [thunder_wave], 12: [electro_ball], 20: [spark], 24: [screech], 34: [discharge], 50: [zap_cannon]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Magnemite', 40, 'electric', 2, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 30
        self.evolve_pokemon1 = Magneton()

class Magneton(Pokemon):

    learnable_moves = Magnemite.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Magneton', 41, 'electric', 2.1, 2, level, moves, name, player_owned)

class Geodude(Pokemon):

    learnable_moves = {1: [defense_curl, tackle], 6: [rock_polish], 10: [rollout], 12: [bulldoze], 16: [rock_throw], 28: [rock_blast], 34: [earthquake], 40: [stone_edge]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Geodude', 40, 'rock', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_pokemon1 = Graveler()
        self.evolve_level1 = 25

class Graveler(Pokemon):

    learnable_moves = Geodude.learnable_moves

    def __init__(self, level=8, name='', moves=None, player_owned=False):
        super().__init__('Graveler', 43, 'rock', 2.1, 2.1, level, moves, name, player_owned)
        
class Onix(Pokemon):

    learnable_moves = {1: [harden, rock_throw, tackle], 8: [rock_polish], 18: [rock_slide], 24: [screech], 28: [bulldoze], 36: [headbutt], 44: [dig], 52: [stone_edge]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Onix', 41, 'rock', 2, 2.2, level, moves, name, player_owned)
        
class Bellsprout(Pokemon):

    learnable_moves = {1: [vine_whip, defense_curl], 7: [growth], 13: [sleep_powder], 15: [poison_powder], 17: [stun_spore], 23: [acid], 32: [razor_leaf], 40: [poison_jab], 47: [headbutt]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Bellsprout', 35, 'grass', 1.8, 1.8, level, moves, name, player_owned)
        self.evolve_level1 = 21
        self.evolve_pokemon1 = Weepinbell()
        self.evolve_level2 = 29
        self.evolve_pokemon2 = Victreebel()
        
class Weepinbell(Pokemon):

    learnable_moves = Bellsprout.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Weepinbell', 39, 'grass', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 29
        self.evolve_pokemon1 = Victreebel()

class Victreebel(Pokemon):

    learnable_moves = Bellsprout.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Victreebel', 41, 'grass', 2.1, 2, level, moves, name, player_owned)

class Tangela(Pokemon):
    
    learnable_moves = {1: [sleep_powder, tackle], 7: [vine_whip], 10: [absorb], 20: [growth], 23: [mega_drain], 29: [stun_spore], 38: [ancient_power], 50: [power_whip]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Tangela', 40, 'grass', 2, 2.2, level, moves, name, player_owned)
        
class Oddish(Pokemon):

    learnable_moves = {1: [growth, tackle], 4: [acid], 12: [poison_powder], 16: [razor_leaf], 18: [sleep_powder], 24: [toxic], 30: [poison_jab]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Oddish', 37, 'grass', 1.85, 1.85, level, moves, name, player_owned)
        self.evolve_level1 = 21
        self.evolve_pokemon1 = Gloom()
        self.evolve_level2 = 30
        self.evolve_pokemon2 = Vileplume()
        
class Gloom(Pokemon):

    learnable_moves = Oddish.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Gloom', 39, 'grass', 2.05, 2, level, moves, name, player_owned)

class Vileplume(Pokemon):

    learnable_moves = Oddish.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Gloom', 42, 'grass', 2.15, 2.1, level, moves, name, player_owned)

class Spearow(Pokemon):

    learnable_moves = {1: [growl, peck], 4: [leer], 10: [tackle], 15: [aerial_ace], 18: [wing_attack], 30: [drill_peck]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Spearow', 38, 'flying', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 21
        self.evolve_pokemon1 = Fearow()
        
class Fearow(Pokemon):

    learnable_moves = Spearow.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Fearow', 41, 'flying', 2.1, 2, level, moves, name, player_owned)
        
class Ekans(Pokemon):

    learnable_moves = {1: [growl, tackle], 13: [acid], 17: [screech], 30: [sludge_bomb], 42: [gunk_shot]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Ekans', 38, 'poison', 2, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 22
        self.evolve_pokemon1 = Arbok()
        
class Arbok(Pokemon):

    learnable_moves = Ekans.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Arbok', 39, 'poison', 2.1, 2.1, level, moves, name, player_owned)
        
class Sandshrew(Pokemon):

    learnable_moves = {1: [defense_curl, scratch], 3: [poison_sting], 8: [rollout], 14: [rapid_spin], 18: [bulldoze], 21: [swift], 30: [slash], 33: [dig], 39: [swords_dance], 45: [earthquake]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Sandshrew', 38, 'ground', 2.1, 1.85, level, moves, name, player_owned)
        self.evolve_level1 = 22
        self.evolve_pokemon1 = Sandslash()
        
class Sandslash(Pokemon):

    learnable_moves = Sandshrew.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Sandslash', 39, 'ground', 2.2, 1.95, level, moves, name, player_owned)
        
class Mankey(Pokemon):

    learnable_moves = {1: [leer, scratch], 8: [low_kick], 12: [seismic_toss], 17: [swagger], 22: [cross_chop], 33: [close_combat], 36: [screech]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Mankey', 37, 'fighting', 2.1, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 28
        self.evolve_pokemon1 = Primeape()
        
class Primeape(Pokemon):

    learnable_moves = Mankey.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Primeape', 40, 'fighting', 2.25, 1.95, level, moves, name, player_owned)
        
class Zubat(Pokemon):

    learnable_moves = {1: [absorb, supersonic], 5: [astonish], 15: [poison_fang], 25: [wing_attack], 40: [venoshock], 50: [aerial_ace]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):

        super().__init__('Zubat', 36, 'flying', 1.85, 1.85, level, moves, name, player_owned)
        self.evolve_level1 = 22
        self.evolve_pokemon1 = Golbat()
        
class Golbat(Pokemon):

    learnable_moves = Zubat.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Golbat', 40, 'flying', 2, 2, level, moves, name, player_owned)

class Meowth(Pokemon):

    learnable_moves = {1: [growl, tackle], 8: [scratch], 16: [headbutt], 22: [swift], 30: [screech], 35: [slash]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Meowth', 37, 'normal', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 28
        self.evolve_pokemon1 = Persian()

class Persian(Pokemon):

    learnable_moves = Meowth.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Persian', 41, 'normal', 2, 2, level, moves, name, player_owned)

class Psyduck(Pokemon):

    learnable_moves = {1: [scratch, tail_whip], 3: [water_gun], 6: [confusion], 12: [water_pulse], 18: [zen_headbutt], 21: [screech], 24: [aqua_tail], 30: [psychic]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Psyduck', 38, 'water', 1.9, 2.1, level, moves, name, player_owned)
        self.evolve_level1 = 33
        self.evolve_pokemon1 = Golduck()

class Golduck(Pokemon):

    learnable_moves = Psyduck.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Golduck', 41, 'water', 2.1, 2, level, moves, name, player_owned)

class Abra(Pokemon):

    learnable_moves = {1: [tackle, confusion], 10: [psybeam], 20: [psycho_cut], 30: [psyshock], 35: [psychic]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Abra', 37, 'psychic', 1.9, 2, level, moves, name, player_owned)
        self.evolve_level1 = 16
        self.evolve_pokemon1 = Kadabra()
        self.evolve_level2 = 32
        self.evolve_pokemon2 = Alakazam()

class Kadabra(Pokemon):

    learnable_moves = Abra.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Kadabra', 41, 'psychic', 2.1, 2, level, moves, name, player_owned)
        self.evolve_level1 = 32
        self.evolve_pokemon1 = Alakazam()

class Alakazam(Pokemon):

    learnable_moves = Abra.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Alakazam', 43, 'psychic', 2.25, 2, level, moves, name, player_owned)

class MrMime(Pokemon):

    learnable_moves = {1: [tackle, defense_curl], 12: [confusion], 20: [psybeam], 30: [psychic]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Mr. Mime', 42, 'psychic', 2, 2, level, moves, name, player_owned)

class Venonat(Pokemon):

    learnable_moves = {1: [tackle], 5: [supersonic], 11: [confusion], 13: [poison_powder], 17: [psybeam], 23: [stun_spore], 25: [bug_buzz], 29: [sleep_powder], 37: [zen_headbutt], 40: [poison_fang], 45: [psychic]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Venonat', 39, 'poison', 1.9, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 30
        self.evolve_pokemon1 = Venomoth()

class Venomoth(Pokemon):

    learnable_moves = Venonat.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Venomoth', 41, 'poison', 2.1, 1.9, level, moves, name, player_owned)

class Voltorb(Pokemon):

    learnable_moves = {1: [charge, tackle], 4: [thunder_shock], 9: [spark], 11: [rollout], 16: [electro_ball], 20: [swift], 30: [discharge]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Voltorb', 38, 'electric', 2, 1.9, level, moves, name, player_owned)
        self.evolve_level1 = 30
        self.evolve_pokemon1 = Electrode()

class Electrode(Pokemon):

    learnable_moves = Voltorb.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Electrode', 40, 'electric', 2.15, 1.95, level, moves, name, player_owned)

class Growlithe(Pokemon):

    learnable_moves = {1: [ember, leer], 4: [howl], 12: [flame_wheel], 24: [fire_fang], 32: [headbutt], 40: [flamethrower], 52: [flare_blitz]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Growlithe', 39, 'fire', 2, 2, level, moves, name, player_owned)
        self.evolved_pokemon1 = Arcanine()
        self.evovled_level1 = 32

class Arcanine(Pokemon):

    learnable_moves = Growlithe.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Arcanine', 43, 'fire', 2.25, 2.15, level, moves, name, player_owned)

class Jigglypuff(Pokemon):

    learnable_moves = {1: [sing, slap, defense_curl], 8: [covet], 18: [swift], 24: [headbutt], 38: [hyper_voice]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Jigglypuff', 38, 'normal', 1.8, 2, level, moves, name, player_owned)
        self.evolve_level1 = 25
        self.evolve_pokemon1 = Wigglytuff()

class Wigglytuff(Pokemon):

    learnable_moves = Jigglypuff.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Wigglytuff', 44, 'normal', 1.85, 2.25, level, moves, name, player_owned)
        
class Aerodactyl(Pokemon):

    learnable_moves = {1: [ancient_power, supersonic], 10: [wing_attack], 18: [rock_slide], 25: [howl], 30: [headbutt], 40: [stone_edge], 50: [hyper_voice]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Aerodactyl', 44, 'normal', 2.2, 1.9, level, moves, name, player_owned)

class Poliwag(Pokemon):

    learnable_moves = {1: [water_gun, defense_curl], 6: [tackle], 12: [mud_shot], 18: [bubble_beam], 24: [water_pulse], 30: [headbutt], 36: [earth_power], 42: [hydro_pump]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Poliwag', 38, 'water', 2, 1.9, level, moves, name, player_owned)
        self.evolve_pokemon1 = Poliwhirl()
        self.evolve_level1 = 25
        self.evolve_pokemon2 = Poliwrath()
        self.evolve_level2 = 35

class Poliwhirl(Pokemon):

    learnable_moves = Poliwag.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Poliwhirl', 41, 'water', 2.15, 2, level, moves, name, player_owned)
        self.evolve_pokemon1 = Poliwrath()
        self.evolve_level1 = 35

class Poliwrath(Pokemon):

    learnable_moves = Poliwag.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Poliwrath', 43, 'water', 2.25, 2.15, level, moves, name, player_owned)

class Krabby(Pokemon):

    learnable_moves = {1: [water_gun, leer], 4: [harden], 12: [mud_shot], 20: [bubble_beam], 25: [headbutt], 32: [water_pulse], 40: [swords_dance], 45: [crab_hammer]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Krabby', 39, 'water', 2.05, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 28
        self.evolve_pokemon1 = Kingler()

class Kingler(Pokemon):

    learnable_moves = Krabby.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Kingler', 42, 'water', 2.2, 1.95, level, moves, name, player_owned)

class Tentacool(Pokemon):

    learnable_moves = {1: [water_gun, poison_sting], 4: [acid], 8: [tackle], 12: [supersonic], 16: [water_pulse], 20: [screech], 24: [bubble_beam], 28: [hex], 36: [poison_jab]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Tentacool', 39, 'water', 1.9, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 30
        self.evolve_pokemon1 = Tentacruel()

class Tentacruel(Pokemon):

    learnable_moves = Tentacool.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Tentacruel', 42, 'water', 2.05, 2.05, level, moves, name, player_owned)

class Shellder(Pokemon):

    learnable_moves = {1: [tackle, water_gun], 4: [defense_curl], 8: [ice_shard], 12: [leer], 16: [water_pulse], 20: [supersonic], 24: [aurora_beam], 30: [ice_beam]} 

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Shellder', 39, 'water', 1.9, 1.95, level, moves, name, player_owned)
        self.evolve_level1 = 30
        self.evolve_pokemon1 = Cloyster()

class Cloyster(Pokemon):

    learnable_moves = Shellder.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Tentacruel', 42, 'ice', 2.15, 2.15, level, moves, name, player_owned)

class Ghastly(Pokemon):
    
    learnable_moves = {1: [lick, confuse_ray], 4: [hypnosis], 16: [spite], 20: [hex], 28: [night_shade], 36: [shadow_ball]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Ghastly', 38, 'ghost', 2, 1.95, level, moves, name, player_owned)
        self.evolve_pokemon1 = Haunter()
        self.evolve_level1 = 25
        self.evolve_pokemon2 = Gengar()
        self.evolve_level2 = 35

class Haunter(Pokemon):
    
    learnable_moves = Ghastly.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Haunter', 41, 'ghost', 2.1, 2, level, moves, name, player_owned)
        self.evolve_pokemon1 = Gengar()
        self.evolve_level1 = 35

class Gengar(Pokemon):
    
    learnable_moves = Ghastly.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Haunter', 44, 'ghost', 2.2, 2.05, level, moves, name, player_owned)

class Zapdos(Pokemon):

    learnable_moves = {1: [peck, thunder_shock], 13: [thunder_wave], 20: [electro_ball], 49: [drill_peck], 50: [thunderbolt], 65: [thunder]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Zapdos', 46, 'electric', 2.25, 2.25, level, moves, name, player_owned)

class Articuno(Pokemon):

    learnable_moves = {1: [mist], 15: [ice_shard], 25: [ancient_power], 35: [ancient_power, freeze_dry], 45: [ice_beam], 50: [hurricane]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Articuno', 46, 'ice', 2.25, 2.25, level, moves, name, player_owned)

class Slowpoke(Pokemon):

    learnable_moves = {1: [tackle], 3: [growl], 6: [water_gun], 9: [yawn], 12: [confusion], 18: [water_pulse], 21: [headbutt], 24: [zen_headbutt], 30: [surf], 36: [psychic]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Slowpoke', 40, 'psychic', 2, 2, level, moves, name, player_owned)
        self.evolve_pokemon1 = Slowbro()
        self.evolve_level1 = 25
        
class Slowbro(Pokemon):

    learnable_moves = Slowpoke.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Slowbro', 42, 'psychic', 2.1, 2.05, level, moves, name, player_owned)

class Drowzee(Pokemon):

    learnable_moves = {1: [tackle, hypnosis], 9: [confusion], 13: [headbutt], 17: [poison_powder], 21: [psybeam], 29: [zen_headbutt], 37: [psychic], 45: [psyshock]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Drowzee', 40, 'psychic', 2.05, 2, level, moves, name, player_owned)
        self.evolve_pokemon1 = Hypno()
        self.evolve_level1 = 28

class Hypno(Pokemon):

    learnable_moves = Drowzee.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Hypno', 42, 'psychic', 2.15, 2.05, level, moves, name, player_owned)

class Koffing(Pokemon):

    learnable_moves = {1: [smog, tackle, poison_sting], 20: [toxic], 24: [sludge_bomb], 30: [poison_jab]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Koffing', 39, 'poison', 2.05, 2.05, level, moves, name, player_owned)
        self.evolve_pokemon1 = Weezing()
        self.evolve_level1 = 24

class Weezing(Pokemon):

    learnable_moves = Koffing.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Weezing', 41, 'poison', 2.1, 2.1, level, moves, name, player_owned)

class Rhyhorn(Pokemon):

    learnable_moves = {1: [tackle, tail_whip], 5: [rock_blast], 10: [bulldoze], 15: [horn_attack], 25: [headbutt], 30: [earth_power], 35: [rock_slide], 45: [earthquake]}

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Rhyhorn', 41, 'ground', 2.1, 2.1, level, moves, name, player_owned)
        self.evolve_level1 = 42
        self.evolve_pokemon1 = Rhydon()

class Rhydon(Pokemon):

    learnable_moves = Rhyhorn.learnable_moves

    def __init__(self, level=5, name='', moves=None, player_owned=False):
        super().__init__('Rhyhorn', 45, 'ground', 2.2, 2.25, level, moves, name, player_owned)