from database import dbAccessor
from datetime import datetime

__getUserQuery = "SELECT username FROM user WHERE username = (%s)"
__insertUserQuery = "INSERT INTO user (name) VALUES (%s)"
__addRunkQuery = "INSERT INTO runk (name) VALUES (%s)"
__getRunksHighscoreQuery = "SELECT COUNT(created), username FROM runk GROUP BY username"
__addCommandQuery = "INSERT INTO command (command, msg) VALUES (%s, %s)"
__getCommandQuery = "SELECT msg FROM command WHERE phrase = (%s)"
__getAllCommandsQuery = "SELECT phrase FROM command"
__delCommandQuery = "DELETE FROM command where phrase = (%s)"

def saveUser(name):
  connection = dbAccessor.db()
  connection.query(__insertUserQuery, (name), True)

def getUser(name):
  connection = dbAccessor.db()
  return connection.query(__getUserQuery, (name), False, True)

def addRunk(name):
  connection = dbAccessor.db()
  user = connection.query(__getUserQuery, (name), False, True)
  if not user:
    connection.query(__insertUserQuery, (name), True)
  timestamp = datetime.today().strftime('%Y-%m-%d')
  params = (name, timestamp)
  execution = connection.query(__addRunkQuery, params, True)
  print(execution)
  return execution

def getRunkHighscore():
  connection = dbAccessor.db()
  execution = connection.query(__getRunksHighscoreQuery)
  print(execution)
  return execution

def addCommand(phrase, msg):
  connection = dbAccessor.db()
  params = (phrase, msg)
  connection.query(__addCommandQuery, params, True)

def getCommand(phrase):
  connection = dbAccessor.db()
  return connection.query(__getCommandQuery, (phrase), False, True)

def listCommands():
  connection = dbAccessor.db()
  return connection.query(__getAllCommandsQuery)

def delCommand(phrase):
  connection = dbAccessor.db()
  return connection.query(__delCommandQuery, (phrase), True)
