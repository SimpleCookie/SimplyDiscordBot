from database import dbAccessor
from datetime import datetime

__getUserQuery = "SELECT username FROM user WHERE username = %s"
__insertUserQuery = "INSERT INTO user (username) VALUES (%s)"
__addRunkQuery = "INSERT INTO runk (username, created) VALUES (%s, %s)"
__getRunksHighscoreQuery = "SELECT COUNT(created), username FROM runk GROUP BY username"
__getRunksHighscoreByUserQuery = "SELECT COUNT(created) FROM runk WHERE username = %s"
__addCommandQuery = "INSERT INTO command (phrase, msg) VALUES (%s, %s)"
__getCommandQuery = "SELECT msg FROM command WHERE phrase = %s"
__getAllCommandsQuery = "SELECT phrase FROM command"
__delCommandQuery = "DELETE FROM command where phrase = %s"


def saveUser(name):
    connection = dbAccessor.db()
    connection.query(__insertUserQuery, (name,), True)


def getUser(name):
    connection = dbAccessor.db()
    return connection.query(__getUserQuery, (name,), False, True)


def addRunk(name):
    connection = dbAccessor.db()
    user = connection.query(__getUserQuery, (name,), False, True)
    if not user:
        connection.query(__insertUserQuery, (name,), True)
    timestamp = datetime.today().isoformat()
    params = (name, timestamp)
    execution = connection.query(__addRunkQuery, params, True)
    return execution


def getRunkHighscoreByUsername(name):
    connection = dbAccessor.db()
    return connection.query(__getRunksHighscoreByUserQuery, (name,))


def getRunkHighscore():
    connection = dbAccessor.db()
    return connection.query(__getRunksHighscoreQuery)


def addCommand(phrase, msg):
    connection = dbAccessor.db()
    params = (phrase, msg)
    connection.query(__addCommandQuery, params, True)


def getCommand(phrase):
    connection = dbAccessor.db()
    return connection.query(__getCommandQuery, (phrase,), False, True)


def listCommands():
    connection = dbAccessor.db()
    return connection.query(__getAllCommandsQuery)


def delCommand(phrase):
    connection = dbAccessor.db()
    return connection.query(__delCommandQuery, (phrase,), True)


__all__ = [
    "saveUser",
    "getUser",
    "addRunk",
    "getRunkHighscoreByUsername",
    "getRunkHighscore",
    "addCommand",
    "getCommand",
    "listCommands",
    "delCommand",
]
