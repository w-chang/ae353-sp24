###############################################################################
#CREATE THE CONTROLLER CLASS
###############################################################################
class Controller():
    def __init__(self):
        # Place your code here
        pass

    
    def reset(self):
        # Place your code here
        pass

    
    def run(self, **kwargs):
        # Place your code here
        return [0., 0., 0., 0.]
    
    
    
###############################################################################
#CREATE THE MAKE_CONTROLLER() FUNCTION
###############################################################################
"""
VALID TEAM NAMES:
    the ORB
    Team Kachow
    Team Steam Tunnels
    Team Flying Mambas
    Team Spare Chang-e
    the Flying Illini
"""
def make_controller():
    controller_instance = Controller()
    team_name = "the ORB"
    return (controller_instance, team_name)