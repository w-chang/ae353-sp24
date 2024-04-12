###############################################################################
#IMPORTS
###############################################################################
from __future__ import print_function
import sys
import threading
try:
    import thread
except ImportError:
    import _thread as thread
import importlib
import numpy as np
try:
    range, _print = xrange, print
    def print(*args, **kwargs): 
        flush = kwargs.pop('flush', False)
        _print(*args, **kwargs)
        if flush:
            kwargs.get('file', sys.stdout).flush()            
except NameError:
    pass


###############################################################################
#TIMEOUT TOOLS
###############################################################################
def quit_function(fn_name):
    thread.interrupt_main() # raises KeyboardInterrupt
    
    
def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer


###############################################################################
#TIME TESTS
###############################################################################
class EmptyKeyError(Exception):
    pass


@exit_after(5.5)
def attempt_import(racer_name):
    module = importlib.import_module(racer_name)
    return module
    
    
@exit_after(5.5)
def test_make(module):
    (controller, team_name) = module.make_controller()
    if team_name not in ["the ORB",
                         "Team Kachow",
                         "Team Steam Tunnels",
                         "Team Flying Mambas",
                         "Team Spare Chang-e",
                         "the Flying Illini"]:
        raise EmptyKeyError("InvalidTeamName")
    if not isinstance(controller, module.Controller):
        raise EmptyKeyError("DidNotMakeController")
    return (controller, team_name)
    

@exit_after(1.5)
def test_init(module):
    _ = module.Controller()
    

@exit_after(1.5)
def test_reset(controller):
    output = controller.reset()
    if not (output is None):
        raise EmptyKeyError("ResetReturnInvalid")


@exit_after(0.006)
def test_run(controller):
    yaw = -np.pi/2.
    c = np.cos(yaw)
    s = np.sin(yaw)
    Rz = np.array([[c, -s, 0.],
                   [s,  c, 0.],
                   [0., 0., 1.]])
    base = np.array([0., 1., 0.])
    dirn = Rz @ base
    inputs = controller.run(dt = 0.01,
                            mocap_1 = np.array([0.25, 0., 0.046875]),
                            mocap_2 = np.array([0., 0.25, 0.046875]),
                            mocap_3 = np.array([-0.25, 0., 0.046875]),
                            mocap_4 = np.array([0., -0.25, 0.046875]),
                            next_gate =  0.6*np.array([20., 0., 0.]),
                            dir_gate = dirn,
                            is_last_gate = False,
                            pos_others = [np.array([1., 1.25, 1.5])])
    if not ((type(inputs) is list) or 
            (type(inputs) is tuple) or 
            (type(inputs) is np.ndarray)):
        raise EmptyKeyError("InputsNotList")
    if len(inputs) != 4:
        raise EmptyKeyError("InvalidNumberOfInputs")
    for inp in inputs:
        if not isinstance(inp, float):
            raise EmptyKeyError("InvalidInputType")


###########################################################################
#FUNCTION FOR RUNNING ALL UNIT TESTS
###########################################################################
def run_tests(racer_names,
              return_valid=False):
    # Racer names
    modules = []
    invalid = []
    
    # Import racers here
    for i in range(len(racer_names)):
        name = racer_names[i]
        try:
            module = attempt_import(name)
        except KeyboardInterrupt:
            print("{} import took too long. DQ.".format(name))
            modules.append(None)
            invalid.append(i)
        except:
            print("Could not import {}. DQ.".format(name))
            modules.append(None)
            invalid.append(i)
        else:
            modules.append(module)

    # controllers and teams
    controllers = []
    team_names = []
    
    # Make controller test
    for i in range(len(racer_names)):
        name = racer_names[i]
        mod = modules[i]
        if i in invalid:
            controllers.append(None)
            team_names.append(None)
            continue
            
        try:
            (controller, team_name) = test_make(mod)
        except KeyboardInterrupt:
            print("{} make_controller() took too long. DQ.".format(name))
            controllers.append(None)
            team_names.append(None)
            invalid.append(i)
        except EmptyKeyError as exc:
            print("{} {}. DQ.".format(name, exc))
            controllers.append(None)
            team_names.append(None)
            invalid.append(i)
        except:
            print("{} make_controller() raised exception. DQ.".format(name))
            controllers.append(None)
            team_names.append(None)
            invalid.append(i)
        else:
            controllers.append(controller)
            team_names.append(team_name)

    # Controller.__init__() test
    for i in range(len(racer_names)):
        name = racer_names[i]
        mod = modules[i]
        if i in invalid:
            continue
        
        try:
            test_init(mod)
        except KeyboardInterrupt:
            print("{} __init__() took too long. DQ.".format(name))
            invalid.append(i)
        except EmptyKeyError as exc:
            print("{} {}. DQ.".format(name, exc))
            invalid.append(i)
        except:
            print("{} __init__() raised exception. DQ.".format(name))
            invalid.append(i)

    # Controller.reset() test
    for i in range(len(racer_names)):
        name = racer_names[i]
        con = controllers[i]
        if i in invalid:
            continue
        
        try:
            test_reset(con)
        except KeyboardInterrupt:
            print("{} reset() took too long. DQ.".format(name))
            invalid.append(i)
        except EmptyKeyError as exc:
            print("{} {}. DQ.".format(name, exc))
            invalid.append(i)
        except:
            print("{} reset() raised exception. DQ.".format(name))
            invalid.append(i)

    # Controller.run() test
    for i in range(len(racer_names)):
        name = racer_names[i]
        con = controllers[i]
        if i in invalid:
            continue
        
        try:
            test_run(con)
        except KeyboardInterrupt:
            print("{} run() took too long. DQ.".format(name))
            invalid.append(i)
        except EmptyKeyError as exc:
            print("{} {}. DQ.".format(name, exc))
            invalid.append(i)
        except:
            print("{} run() raised exception. DQ.".format(name))
            invalid.append(i)

    a = len(racer_names)
    b = len(modules)
    c = len(controllers)
    d = len(team_names)
    n_racers = [a, b, c, d]
    if not all(i == n_racers[0] for i in n_racers):
        print(racer_names)
        print(modules)
        print(controllers)
        print(team_names)
        raise Exception("If you get this error, see the course staff.")
    n_racers = n_racers[0]
    
    print("\nVALID RACERS:")
    for i in range(len(racer_names)):
        if not i in invalid:
            print(racer_names[i])
    print("")
    
    if return_valid:
        valid_racer_names = []
        valid_modules = []
        valid_controllers = []
        valid_team_names = []
        for i in range(len(racer_names)):
            if not (i in invalid):
                valid_racer_names.append(racer_names[i])
                valid_modules.append(modules[i])
                valid_controllers.append(controllers[i])
                valid_team_names.append(team_names[i])
        
        results = (valid_racer_names,
                   valid_modules,
                   valid_controllers,
                   valid_team_names)
        return results