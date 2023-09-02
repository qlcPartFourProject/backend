class FirebaseClientManager:
   __instance = None

   @staticmethod 
   def get_instance():
      """ Static access method. """
      if FirebaseClientManager.__instance == None:
         FirebaseClientManager()
      return FirebaseClientManager.__instance
   
   def __init__(self):
      """ Virtually private constructor. """
      if FirebaseClientManager.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         FirebaseClientManager.__instance = self