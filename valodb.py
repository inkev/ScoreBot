import sqlite3

db = sqlite3.connect("/home/inkev/repos/DrinkBot/historydata.db")

class Valodb(object):
    __DB_LOCATION = "/home/inkev/repos/DrinkBot/matches.db"