# -*- coding: utf-8 -*-
import cards
def create_pack():
	""" Создание новой колоды из 25 карт """
	pack_player = cards.Pack()
	#СУЩЕСТВА
	#Оружейный дворф
	pack_player.create(types = "soldier", name = "sdvorf", price = "6", heal = "4", damage = "4", defence = "false")
	#Огненный дракон
	pack_player.create(types = "soldier", name = "sdrakon", price = "8", heal = "10", damage = "8", defence = "false")
	#Кменный голем
	pack_player.create(types = "soldier", name = "sgolem", price = "7", heal = "7", damage = "7", defence = "false")
	#Искатель клада
	pack_player.create(types = "soldier", name = "siskatel", price = "3", heal = "3", damage = "1", defence = "false")
	#Командир гвардии
	pack_player.create(types = "soldier", name = "skomandir", price = "6", heal = "5", damage = "5", defence = "false")
	#Лунная целительница
	pack_player.create(types = "soldier", name = "slunnaya", price = "5", heal = "4", damage = "3", defence = "false")
	#Эльфийская лучница
	pack_player.create(types = "soldier", name = "slychnica", price = "2", heal = "2", damage = "1", defence = "false")
	#Старый провидец
	pack_player.create(types = "soldier", name = "sprovidec", price = "3", heal = "3", damage = "2", defence = "false")
	#Щитоносец
	pack_player.create(types = "soldier", name = "sshitonosec", price = "5", heal = "6", damage = "3", defence = "true")
	#Служитель культа
	pack_player.create(types = "soldier", name = "ssluzhitel", price = "4", heal = "3", damage = "4", defence = "false")
	#Волк разведчик
	pack_player.create(types = "soldier", name = "svolk", price = "1", heal = "1", damage = "2", defence = "false")
	#Раненый ворген
	pack_player.create(types = "soldier", name = "svorgen", price = "4", heal = "8", damage = "4", defence = "false")
	#Вожак стаи
	pack_player.create(types = "soldier", name = "svozhak", price = "2", heal = "2", damage = "2", defence = "false")
	#Защитник средиземья
	pack_player.create(types = "soldier", name = "szashitnik", price = "1", heal = "2", damage = "1", defence = "true")
	#Знахарь средиземья
	pack_player.create(types = "soldier", name = "sznahar", price = "1", heal = "2", damage = "1", defence = "false")
	#Знахарь средиземья
	pack_player.create(types = "soldier", name = "sznahar", price = "1", heal = "2", damage = "1", defence = "false")
	#ЗАКЛИНАНИЯ
	#Целебное касание
	pack_player.create(types = "spell", name = "zkasanie", price = "3", heal = "0", damage = "0", defence = "false")
	#Небесный луч
	pack_player.create(types = "spell", name = "zlych", price = "0", heal = "0", damage = "0", defence = "false")
	#Чародейские стрелы
	pack_player.create(types = "spell", name = "zstrely", price = "2", heal = "0", damage = "0", defence = "false")
	#Атака теней
	pack_player.create(types = "spell", name = "zteni", price = "3", heal = "0", damage = "0", defence = "false")
	#Ментальный техник
	pack_player.create(types = "spell", name = "ztexnic", price = "5", heal = "0", damage = "0", defence = "false")
	#ОРУЖИЕ
	#Дар древних
	pack_player.create(types = "weapon", name = "odar", price = "2", heal = "0", damage = "0", defence = "false")
	#Эльфийский лук
	pack_player.create(types = "weapon", name = "olyk", price = "4", heal = "0", damage = "0", defence = "false")
	#Молот правосудия
	pack_player.create(types = "weapon", name = "omolot", price = "5", heal = "0", damage = "0", defence = "false")
	#Зааленная секира
	pack_player.create(types = "weapon", name = "osekira", price = "3", heal = "0", damage = "0", defence = "false")
	#Паучий яд
	pack_player.create(types = "weapon", name = "oyad", price = "5", heal = "0", damage = "0", defence = "false")
	return pack_player


pack_player1 = create_pack()
n = 0
for card in pack_player1.cards:
	print ("Name: " + pack_player1.cards[n].name + "Damage: " + pack_player1.cards[n].damage )
	n += 1

