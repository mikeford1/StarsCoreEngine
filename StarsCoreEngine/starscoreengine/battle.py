"""
    This file is part of Stars Core Engine, which provides an interface and 
    processing of Stars data. 

    Copyright (C) 2014  <Joshua Urlaub + Contributors>

    Stars Core Engine is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Stars Core Engine is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with Stars Core Engine.  If not, see <http://www.gnu.org/licenses/>.

    Contributors to this project agree to abide by the interpretation expressed 
    in the COPYING.Interpretation document.

"""


def getBoardGrid(numPlayers):
    """Returns a diagram of the battle board, copied from 
    http://wiki.starsautohost.org/wiki/%22Battleboard_Starting_Positions_%28BSP%29%22_by_Overworked_-_04_February_2003
    """

    if numPlayers == 2:
        return ["..........",
                "..........",
                "..........",
                "..........",
                ".1........",
                "........2.",
                "..........",
                "..........",
                "..........",
                ".........."]

    elif numPlayers == 3:
        return ["..........",
                "....1.....",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                ".3......2.",
                ".........."]
        
    elif numPlayers == 4:
        return ["..........",
                ".1......4.",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                ".3......2.",
                ".........."]
        
    elif numPlayers == 5:
        return ["..........",
                "....1.....",
                "..........",
                "..........",
                ".3......4.",
                "..........",
                "..........",
                "..........",
                "..5...2...",
                ".........."]
        
    elif numPlayers == 6:
        return ["..........",
                "...6...4..",
                "..........",
                "..........",
                ".1........",
                "........2.",
                "..........",
                "..........",
                "..3...5...",
                ".........."]
        
    elif numPlayers == 7:
        return ["..........",
                ".1...7....",
                "........6.",
                "..........",
                "..........",
                ".2........",
                "........5.",
                "..........",
                "..3...4...",
                ".........."]
        
    elif numPlayers == 8:
        return ["..........",
                "...8..7...",
                "..........",
                ".1......6.",
                "..........",
                "..........",
                ".2......5.",
                "..........",
                "...3..4...",
                ".........."]
        
    elif numPlayers == 9:
        return ["..........",
                "...8..4...",
                "..........",
                ".1......6.",
                "....9.....",
                "..........",
                ".5......2.",
                "..........",
                "...3..7...",
                ".........."]
        
    elif numPlayers == 10:
        return ["..........",
                "..1..2..3.",
                "..........",
                "..........",
                ".4......5.",
                "....6.....",
                "..........",
                ".7......8.",
                "...9..A...",
                ".........."]
        
    elif numPlayers == 11:
        return ["..........",
                "...8..4...",
                "..........",
                ".1....A.6.",
                "...9......",
                "..........",
                ".5....B.2.",
                "..........",
                "...3..7...",
                ".........."]
        
    elif numPlayers == 12:
        return ["..........",
                "...6.B.4..",
                ".9........",
                "........8.",
                ".1........",
                "........2.",
                ".7........",
                "........C.",
                "..3.A.5...",
                ".........."]
        
    elif numPlayers == 13:
        return ["..........",
                ".1.5.6.7..",
                "..........",
                ".2......8.",
                "....D.....",
                ".3......9.",
                "..........",
                ".4........",
                "...A.B.C..",
                ".........."]
        
    elif numPlayers == 14:
        return ["..........",
                ".1.E.D.C..",
                "........B.",
                ".2........",
                "........A.",
                ".3........",
                "........9.",
                ".4........",
                "..5.6.7.8.",
                ".........."]
        
    elif numPlayers == 15:
        return ["..........",
                ".1.E.D.C..",
                "........B.",
                ".2........",
                "....F...A.",
                ".3........",
                "........9.",
                ".4........",
                "..5.6.7.8.",
                ".........."]
        
    elif numPlayers == 16:
        return ["..........",
                ".1.E.D.C..",
                "........B.",
                ".2.F......",
                "........A.",
                ".3........",
                "......G.9.",
                ".4........",
                "..5.6.7.8.",
                ".........."]

def extractCoords(grid, numPlayers):
    """Extracts player starting positions from the grid diagram supplied, returns a list of tuples
    containing the (x, y) coords (top left = (0, 0))"""
    results = []
    codes = "123456789ABCDEF" #what the players are in the grid
    for c in codes[:numPlayers]:
        for yidx, y in enumerate(grid):
            for xidx, x in enumerate(y):
                if x == c:
                    results.append((xidx, yidx))
                    break
    return results
            

def calcAccuracy(computing_power, base_accuracy, jamming):
    return (100 - (100 - base_accuracy) * computing_power * 0.01) * (100 - jamming) * 0.01
    
def calcAttraction(firing_ship, weapon, target, tgt_range):
    """Calculates the attractiveness of a target for weapson according to
    http://wiki.starsautohost.org/wiki/%22Targeting_Order_of_Battle%22_by_Art_Lathrop_1999-04-14_v2.6/7i.

    Assumes that the same weapon components will fire together, but different ones can have different targets.

    """

    #attractiveness = cost / attack power needed
    tgt_class = target["class"]
    tgt_shields = target["shields"]
    tgt_armor = target["armor"]
    cost = (tgt_class.bor + tgt_class.resources) * target["number"]
    if weapon.sapper:
        apn = tgt_shields / (0.9 ** (tgt_class.deflector_effectiveness * 10) * (1 - 0.1 * tgt_range / weapon["range"]))
        return cost / apn
    elif weapon.beampower:
        apn = (tgt_armor + tgt_shields) / (0.9 ** (tgt_class.deflector_effectiveness * 10) * (1 - 0.1 * tgt_range / weapon["range"]))
        return cost / apn
    else:
        coeff = 2 if weapon.doubleDamageUnshielded else 1
        accuracy = calcAccuracy(tgt_class.computing_power, weapon.accuracy, tgt_class.jamming_effectiveness)
        if tgt_shields > tgt_armor:
            apn = tgt_armor * 2 / accuracy
            return cost / apn
        else:
            apn = tgt_shields * 2 / accuracy + (tgt_armor - tgt_shield) / (accuracy * coeff)            
            return cost / apn
