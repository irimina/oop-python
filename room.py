
# write our own class, which will be a blueprint for the rooms in the game
'''
class a name starts with a capital letter,
this helps us to distinguish between class names and variables.
'''

class Room():
    # need a constructor to tell Python how to create an object for the class
    # this initializes the object
    def __init__(self):
        # let's add attributes for our room
        self.name=None
        self.description=None
        # self means this object
        # None here means they start off with no value

    # sometimes we allow people to set the values of these parameters
    def __init__(self,room_name):
        # set the value of the attribute self.name to room_name
        self.name=room_name
        self.description=None
    # set the description of the room
    def set_description(self,room_description):
        self.description= room_description

    # get the description of the room 
    def get_description(self):
        return self.description
 # CHALLENGE using getter and seetter
    def get_name(self):
        return self.name

    def set_name(self, name):
        slef.name=name

        
  
        

    

        
        
        
        
        
    

