import json
import os

class GameStartManager(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)
        #self.saveMemoryVersionOfDatabaseToFile()

    # These methods deal with Get/Set data into the memory
    # These methods are intermediary methods between the application and the methods that really "talk" to the file database
    
    def load(self , location):
        if os.path.exists(location):
            self.loadMemoryVersionOfDatabaseFromFile()
        else:
            #self.initialiseDatabase() #new
            self.loadMemoryVersionOfDatabaseFromFile()  #why do this when we just set memoryVersionOfDatabase?  
        return True

    def initialiseDatabase(self): #new
        try:
            self.resetdb()        
            self.memoryVersionOfDatabase={"Enemies":[]}
            self.saveMemoryVersionOfDatabaseToFile()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def appendZombie(self, ZombieID):
        self.memoryVersionOfDatabase["Enemies"].append({"name": ZombieID,"lives": "3"})
        self.saveMemoryVersionOfDatabaseToFile()

    def updateZombie(self, ZombieID, lives):
        self.loadMemoryVersionOfDatabaseFromFile()

        #First we unpack the data
        zombies=self.memoryVersionOfDatabase["Enemies"]  #This is a list
        zombie = list(filter(lambda i: i['name'] == ZombieID, zombies))[0]  

        #Then we make the change 
        zombie["lives"]=lives  #Take a look at memoryVersionOfDatabase How is that possible?

        #Then we save the changes
        self.saveMemoryVersionOfDatabaseToFile()


    def set(self , key , value):
        try:
            self.memoryVersionOfDatabase[str(key)] = value
            self.saveMemoryVersionOfDatabaseToFile()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , object_key, level_key):
        try:
            self.loadMemoryVersionOfDatabaseFromFile()
            Levels = self.memoryVersionOfDatabase["Levels"]
            level = Levels[level_key]
            #level = Levels["1"]
            return level[object_key]
        except KeyError:
            print("No Value Can Be Found for " + str(level_key))
            return False

    def get_level(self, level_key):
        try:
            self.loadMemoryVersionOfDatabaseFromFile()
            Levels = self.memoryVersionOfDatabase["Levels"]
            return Levels[level_key]
        except KeyError:
            print("No Value Can Be Found for " + str(level_key))
            return False

    def delete(self , key):
        if not key in self.memoryVersionOfDatabase:
            return False
        del self.memoryVersionOfDatabase[key]
        self.saveMemoryVersionOfDatabaseToFile()
        return True
    
    def resetdb(self):
        self.memoryVersionOfDatabase={}
        self.saveMemoryVersionOfDatabaseToFile()
        return True



    # These methods deal with the real database file
    def loadMemoryVersionOfDatabaseFromFile(self):
        self.memoryVersionOfDatabase = json.load(open(self.location , "r")) 

    def saveMemoryVersionOfDatabaseToFile(self):
        try:
            json.dump(self.memoryVersionOfDatabase , open(self.location, "w+"))
            return True
        except:
            return False
