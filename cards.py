# -*- coding: utf-8 -*-
class Card(object):
	""" Одна игральная карта """
	TYPES = ["weapon", "soldier", "spell"]
	NAME = ["odar", "olyk", "omolot", "osekira", "oyad", "sdrakon", "sdvorf", "sgolem", "siskatel", "skomandir", "slunnaya", "slychnica", "sprovidec", "sshitonosec", "ssluzhitel", "svolk", "svorgen", "svozhak", "szashitnik", "sznahar", "zkasanie", "zlych", "zstrely", "zteni", "ztexnic"]
	PRICE = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
	HEAL = ["1", "2", "3", "4", "5", "6", "7", "8", "10"]
	DAMAGE = ["1", "2", "3", "4", "5", "7", "8"]
	DEFENCE = ["true", "false"]
	def __init__(self, type, name, price, heal, damage, degence):
		self.types = types
		self.name = name
		self.price = price
		self.heal = heal
		self.damage = damage
		self.defence = defence
	def __str__(self):
		rep = "'тип = ' + self.types + 'имя = ' + self.name + 'цена = ' + self.price + 'Жизни = ' + self.heal + 'атака = ' + self.damage + 'защита = ' + self.defence" 
		return rep

class Hand(object):
	""" 'Рука': набор карт на руках у одного игрока. """
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "В руке нет карт."
		return rep
	def clean(self):
		self.cards = []
	def add(self, card):
		if len(self.cards) < 5:
			pack.remove(card)
			self.cards.append(card)
		else:
			rep = "В вашей руке моксимальное ьколичество карт"
			return rep
	def give(self, card, table):
		self.cards.remove(card)
		table.add(card) #Дописать проверку на количество карт на столе (<3)

class Table(object):
	""" 'Игровой стол': разыгранные карты на столе у одного игрока. """
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "На столе нет карт."
		return rep
	def clean(self):
		self.cards = []
	def add(self, card):
		self.cards.append(card)
	def reset(self, card, reset):
		self.cards.remove(card)
		reset.add(card)

class Reset(object):
	""" Стопка сброса """
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "В сбросе нет карт."
		return rep
	def clean(self):
		self.cards = []
	def add(self, card):
		self.cards.add(card)
	def shuffle(self):
		import random
		random.shuffle(self.cards)

class Pack(object):
	""" Колода карт одного игрока """
	def __init__(self):
		self.cards = []
	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "В колоде больше нет карт."
		return rep
	def create(self, types, name, price, heal, damage,defence):
		self.cards = []
		self.add(Card(types, name, price, heal, damage,defence))
	def add(self):
		self.cards = []
		self.cards = reset.shuffle()

if __name__ == "__main__":
	print("Вы запустили этот модуль напрямую, а не импортировали его.")
	input("\n\nНажмите Enter чтобы выйти.")