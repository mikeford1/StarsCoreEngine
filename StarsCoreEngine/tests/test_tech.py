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

from ..starscoreengine import *
from ..starscoreengine.template_tech import *
import unittest
from math import fabs

class TestTech(unittest.TestCase):
    def test_order(self):
        tech = order_tech()
        self.assertEqual(tech["shields"]["Croby Sharmor"], {"energy" : 7, "weapons" : 0, "propulsion" : 0, "construction" : 4, 
                                                            "electronics" : 0, "biotechnology" : 0, "mass" : 10, "resources" : 15, 
                                                            "iron" : 7, "bor" : 0, "germ" : 4, "shieldDP" : 60, "hasPRT" : ["IS"], "hasLRT" : [], "notLRT" : []})
        self.assertNotEqual(tech["shields"]["Croby Sharmor"], {"energy" : 7, "weapons" : 0, "propulsion" : 0, "construction" : 4, 
                                                            "electronics" : 0, "biotechnology" : 0, "mass" : 10, "resources" : 15, 
                                                            "iron" : 7, "bor" : 0, "germ" : 4, "shieldDP" : 60, "hasPRT" : ["SS"], "hasLRT" : [], "notLRT" : []})

    def test_hulls(self):
            tmp =  {"Battleship" : {"Armor" : [6],
                            "Armor Scanner Elect/Mech" : [],
                            "Bomb" : [],
                            "Elect" : [3, 3],
                            "Engine" : [4],
                            "General Purpose" : [],
                            "Mech" : [],
                            "Mine" : [],
                            "Mine Elect Mech" : [],
                            "Mining" : [],
                            "Scanner" : [],
                            "Scanner Elect Mech" : [1],
                            "Shield" : [8],
                            "Shield Elect Mech": [],
                            "Shield or Armor" : [],
                            "Weapon" : [2, 2, 6, 6, 4]}
            }
            hullDicts = hull_slots(tmp)
            expectedDict = {'A': {'slotsAvalable': 4, 'objectType': 'Engine'}, 
                            'B': {'slotsAvalable': 6, 'objectType': 'Armor'}, 
                            'C': {'slotsAvalable': 2, 'objectType': 'Weapon'}, 
                            'D': {'slotsAvalable': 2, 'objectType': 'Weapon'},              
                            'E': {'slotsAvalable': 6, 'objectType': 'Weapon'}, 
                            'F': {'slotsAvalable': 6, 'objectType': 'Weapon'}, 
                            'G': {'slotsAvalable': 4, 'objectType': 'Weapon'}, 
                            'H': {'slotsAvalable': 8, 'objectType': 'Shield'}, 
                            'I': {'slotsAvalable': 3, 'objectType': 'Elect'}, 
                            'J': {'slotsAvalable': 3, 'objectType': 'Elect'},
                            'K': {'slotsAvalable': 1, 'objectType': 'Scanner Elect Mech'}
                        }

            self.assertEqual(hullDicts["Battleship"], expectedDict)



