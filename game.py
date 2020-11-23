"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random
import math


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level):
		self.__name__ = str(name)
		self.power = power
		self.min_level = min_level

	def make_unarmed(self):
		return Weapon("Unarmed", 20, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level, weapon=None):
		self.__name__ = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		if not weapon:
			self.weapon = Weapon.make_unarmed(weapon)
		else:
			self.weapon = weapon
		self.hp = max_hp

	def take_damage(self, attacker, defender):
		chance_crit = random.randint(0, 1000)/1000
		if chance_crit <= 6.25:
			crit = 2
		else:
			crit = 1
		modifier = crit*(random.randint(85, 100)/100)
		dmg = ((((2*attacker.level/5)+2)*attacker.weapon.power*(attacker.attack/defender.defense)/50) + 2)*modifier
		self.hp += -1*math.floor(dmg)
		if self.hp < 0:
			self.hp = 0


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	defender.take_damage(attacker, defender)
	print(f"{attacker.__name__} used {attacker.weapon.__name__}")
	print(f"{defender.__name__} took {defender.max_hp-defender.hp} damage")


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	turns = 0
	while attacker.hp > 0 or defender.hp > 0:
		turns += 1
		deal_damage(attacker, defender)
		if defender.hp < 0:
			deal_damage(defender, attacker)
		else:
			break
	return turns
