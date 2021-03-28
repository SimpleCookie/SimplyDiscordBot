import dbAccessor
from datetime import datetime

getUserQuery = "SELECT username FROM user WHERE username = (%s)"
insertUserQuery = "INSERT INTO user (name) VALUES (%s)"
addRunkQuery = "INSERT INTO runk (name) VALUES (%s)"
getRunksHighscoreQuery = "SELECT COUNT(created), username FROM runk GROUP BY username"
addCommandQuery = "INSERT INTO command (command, msg) VALUES (%s, %s)"
getCommandQuery = "SELECT msg FROM command WHERE phrase = (%s)"
getAllCommandsQuery = "SELECT phrase FROM command"
delCommandQuery = "DELETE FROM command where phrase = (%s)"

def saveUser(name):
  connection = dbAccessor.db()
  connection.query(insertUserQuery, (name), True)

def getUser(name):
  connection = dbAccessor.db()
  return connection.query(getUserQuery, (name), False, True)

def addRunk(name):
  connection = dbAccessor.db()
  user = connection.query(getUserQuery, (name), False, True)
  if not user:
    connection.query(insertUserQuery, (name), True)
  timestamp = datetime.today().strftime('%Y-%m-%d')
  params = (name, timestamp)
  execution = connection.query(addRunkQuery, params, True)
  print(execution)
  return execution

def getRunkHighscore():
  connection = dbAccessor.db()
  execution = connection.query(getRunksHighscoreQuery)
  print(execution)
  return execution

def addCommand(phrase, msg):
  connection = dbAccessor.db()
  params = (phrase, msg)
  connection.query(addCommandQuery, params, True)

def getCommand(phrase):
  connection = dbAccessor.db()
  return connection.query(getCommandQuery, (phrase), False, True)

def listCommands():
  connection = dbAccessor.db()
  return connection.query(getAllCommandsQuery)

def delCommand(phrase):
  connection = dbAccessor.db()
  return connection.query(delCommandQuery, (phrase), True)
