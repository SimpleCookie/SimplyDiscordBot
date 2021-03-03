from replit import db

def saveToDB(prefix, suffix, action):
  db[prefix+suffix] = action

def getFromDB(prefix, suffix):
  return db[prefix+suffix]

def keyExists(key):
  return key in db

def listDBWithPrefix(prefix):
  return db.prefix(prefix)

def removeCommand(prefix, event):
  cmd = event.content.split(" ", 1)
  del db[prefix+cmd]