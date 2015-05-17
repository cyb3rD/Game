# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app

# Карта 
class Card():

	def __init__(self):
		self.damage = 0
		self.health = 0
	# вывод значения
	def getDamage(self):
		return self.damage
	# изменение значения Damage
	def changeDamage(self, damage):
		return self.damage + damage
# Игрок
class Player():
	pass

# Стол
class Table():
	pass

# Колода
class Deck():
	pass


@app.route('/')
@app.route('/index')
def index():
	# Инициализация карт
	# ToDo:
	#  Рандомная раздача карт на руку
	PlayerCard = Card()

	# Вывод основных параметров/свойств игрока
	# Рабочий вариант без разделения шаблонов
	return render_template("game.html", damage = PlayerCard.getDamage())

	# Использование разделдения шаблонов
	return render_template("Field.html", damage = PlayerCard.getDamage())