import random
import math
from bbplayer import *

class Drafter:
    
    def draft_generate(self, num_players):
        player_list = []
        first_names_list = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "I.",
                      "J.", "K.", "L.", "M.", "N.", "O.", "P.", "Q.", "R.",
                      "S.", "T.", "U.", "V.", "W.", "X.", "Y.", "Z."]
        last_names_list = ["James", "Bryant", "Iverson", "Bird", "Baddie",
                           "Vanderbilt", "Notgood", "DaBest", "McGrady",
                           "Bud", "Swag", "Jam", "Rockafella", "Snipes", "Durant",
                           "Jordan", "Dogg", "Carter", "Wayne", "Tang", "Jones",
                           "Jesus", "Hooplife", "Buckets", "Curry", "Splash",
                           "Dunkins", "Jumpson"]
        player_name_set = self.generate_name_set(num_players, first_names_list, last_names_list)

        for name in player_name_set:
            position = math.ceil(random.random() * 5)
            player_list.append(self.generate_player(position, 0, name))
        return player_list

    def generate_name_set(self, size, first_names_list, last_names_list=None):
        player_name_set = set()
        if last_names_list is not None:
            if size > len(first_names_list) * len(last_names_list):
                raise KeyError('Don\'t have enough names')
            while len(player_name_set) < size:
                player_name_set.add(random.choice(first_names_list) + " " + random.choice(last_names_list))
        else:
            if size > len(first_names_list):
                raise KeyError('Don\'t have enough names')
            while len(player_name_set) < size:
                player_name_set.add(random.choice(first_names_list))
        return player_name_set

    def generate_player(self, pref_pos, pr, name="Generic"):
        #default values
        def_rat = 75
        height     = 78 #6'6"
        weight     = 180
        speed      = def_rat
        age        = 25
        int_s      = def_rat
        mid_s      = def_rat
        out_s      = def_rat
        passing    = def_rat
        handling   = def_rat
        steal      = def_rat
        block      = def_rat
        int_d      = def_rat
        out_d      = def_rat
        rebounding = def_rat
        if pref_pos==1: #point guard
            if pr==1: print("\nPOINT GUARD")
            height -= random.randint(3, 6)
            weight -= random.randint(0, 30)
            speed += random.randint(5, 10)
            int_s -= random.randint(8, 16)
            mid_s += random.randint(0, 10) - 5
            out_s += random.randint(0, 10) - 5
            passing += random.randint(5, 15)
            handling += random.randint(0, 10)
            steal += random.randint(0, 10) - 2
            block -= random.randint(20, 40)
            int_d -= random.randint(8, 16)
            out_d += random.randint(0, 10) - 5
            rebounding -= random.randint(10, 30)
        elif pref_pos==2: #shooting guard
            if pr==1: print("\nSHOOTING GUARD")
            height += random.randint(0, 4) - 3
            weight += random.randint(0, 30) - 15
            speed += random.randint(0, 6)
            int_s += random.randint(0, 16) - 8
            mid_s += random.randint(0, 13) - 5
            out_s += random.randint(0, 13) - 5
            passing += random.randint(0, 10)
            handling += random.randint(0, 10) - 2
            steal += random.randint(0, 10) - 5
            block -= random.randint(10, 30)
            int_d -= random.randint(5, 10)
            out_d += random.randint(0, 10) - 5
            rebounding -= random.randint(5, 15)
        elif pref_pos==3: #small forward
            if pr==1: print("\nSMALL FORWARD")
            height += random.randint(0, 6) - 2
            weight += random.randint(0, 40) - 10
            speed += random.randint(0, 16) - 8
            int_s += random.randint(0, 20) - 8
            mid_s += random.randint(0, 20) - 10
            out_s += random.randint(0, 20) - 10
            passing += random.randint(0, 20) - 10
            handling += random.randint(0, 20) - 10
            steal += random.randint(0, 20) - 10
            block += random.randint(0, 15) - 5
            int_d += random.randint(0, 15) - 5
            out_d += random.randint(0, 15) - 5
            rebounding += random.randint(0, 15) - 5
        elif pref_pos==4: #power forward
            if pr==1: print("\nPOWER FORWARD")
            height += random.randint(1, 7)
            weight += random.randint(20, 60)
            speed += random.randint(0, 15) - 15
            int_s += random.randint(0, 20) - 5
            mid_s += random.randint(0, 16) - 8
            out_s += random.randint(0, 12) - 6
            passing += random.randint(0, 20) - 20
            handling += random.randint(0, 20) - 20
            steal += random.randint(0, 20) - 20
            block += random.randint(0, 20) - 5
            int_d += random.randint(0, 20) - 5
            out_d += random.randint(0, 10) - 8
            rebounding += random.randint(0, 20) - 5
        elif pref_pos==5: #center
            if pr==1: print("\nCENTER")
            height += random.randint(2, 12)
            weight += random.randint(40, 80)
            speed += random.randint(0, 20) - 30
            int_s += random.randint(5, 15)
            mid_s += random.randint(0, 20) - 15
            out_s += random.randint(0, 30) - 45
            passing += random.randint(0, 20) - 40
            handling += random.randint(0, 30) - 40
            steal += random.randint(0, 30) - 40
            block += random.randint(5, 15)
            int_d += random.randint(5, 15)
            out_d += random.randint(0, 20) - 20
            rebounding += random.randint(5, 15)
        #choose 5(?) of these "attributes" to make a player. Some are good, some bad, some funny
        list_attributes = ["Passer", "Offensive Weapon", "Blocker", "Tall", "Short", "On-ball Defense", "Rebounder", "Fumbler", "Fatty", "Slow", "No Threes", "Dunker", "Defensive Liability", "Offensive Liability",
                           "Mid-range Specialist", "The Whole Package", "The Wall", "3pt Specialist", "Two-way inside", "Two-way outside"]
        num_att = 0
        tries = 0
        gained_attributes = []
        while num_att<5 or tries>10:
            att = random.randint(0, len(list_attributes)-1)
            gained_attributes.append(list_attributes[att])
            num_att+=1
        for a in gained_attributes:
            if pr==1: print(a)
            if a=="Passer":
                passing += random.randint(15, 20)
            elif a=="Offensive Weapon":
                out_s += random.randint(0, 10)
                mid_s += random.randint(10, 15)
                int_s += random.randint(10, 15)
            elif a=="Blocker":
                block += random.randint(10, 15)
            elif a=="Tall":
                height += random.randint(4,8)
            elif a=="Short":
                height -= random.randint(3,5)
            elif a=="On-ball Defense":
                steal += random.randint(5, 10)
                out_d += random.randint(5, 10)
            elif a=="Rebounder":
                rebounding += random.randint(10, 15)
                height += random.randint(0, 2)
            elif a=="Fumbler":
                passing -= random.randint(5, 10)
                handling -= random.randint(5, 10)
            elif a=="Fatty":
                weight += random.randint(50, 100)
            elif a=="Slow":
                speed -= random.randint(20, 40)
                if speed<10: speed=10
            elif a=="No Threes":
                out_s -= random.randint(20, 30)
                if out_s<10: out_s=10
            elif a=="Dunker":
                int_s += random.randint(15, 20)
            elif a=="Defensive Liability":
                steal -= random.randint(5, 10)
                block -= random.randint(5, 10)
                int_d -= random.randint(5, 10)
                out_d -= random.randint(5, 10)
            elif a=="Offensive Liability":
                int_s -= random.randint(5, 10)
                out_s -= random.randint(5, 10)
                mid_s -= random.randint(5, 10)
                if mid_s<10: mid_s=10
                if int_s<10: int_s=10
                if out_s<10: out_s=10
            elif a=="Mid-range Specialist":
                mid_s += random.randint(12, 17)
            elif a=="The Whole Package":
                steal += random.randint(2, 4)
                block += random.randint(2, 4)
                int_d += random.randint(2, 4)
                out_d += random.randint(2, 4)
                int_s += random.randint(2, 4)
                out_s += random.randint(2, 4)
                mid_s += random.randint(2, 4)
                passing += random.randint(2, 4)
            elif a=="The Wall":
                int_d += random.randint(12, 17)
                block += random.randint(6, 12)
            elif a=="3pt Specialist":
                out_s += random.randint(12, 17)
                mid_s -= random.randint(5, 15)
                int_s -= random.randint(5, 15)
                passing -= random.randint(5, 15)
                if passing<10: passin=10
                if mid_s<10: mid_s=10
                if int_s<10: int_s=10
            elif a=="Two-way inside":
                int_s += random.randint(8, 12)
                int_d += random.randint(8, 12)
            elif a=="Two-way outside":
                out_s += random.randint(8, 12)
                out_d += random.randint(8, 12)
                
        return bbplayer(name, pref_pos, height, weight, speed, age, int_s, mid_s, out_s, passing, handling, steal, block, int_d, out_d, rebounding, gained_attributes)