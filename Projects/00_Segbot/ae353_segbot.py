"""
This modules provides a backend for the ae353 segbot example
"""

###############################################################################
#DEPENDENCIES
###############################################################################
from condynsate.simulator import Simulator
from pathlib import Path
import numpy as np
import sys
import time


###############################################################################
#SIMULATION CLASS
###############################################################################
class Segbot_sim():
    def __init__(self,
                 force_keyboard=False,
                 visualization=True,
                 visualization_fr=20.,
                 animation=True,
                 animation_fr=10.):
        """
        Initializes an instance of the simulation class.

        Parameters
        ----------
        force_keyboard : bool, optional
            A boolean flag that indicates whether the simulation will force
            the keyboard to be used, regardless of OS
        visualization : bool, optional
            A boolean flag that indicates whether the simulation will be 
            visualized in meshcat. The default is True.
        visualization_fr : float, optional
            The frame rate (frames per second) at which the visualizer is
            updated. The default is 20..
        animation : bool, optional
            A boolean flag that indicates whether animated plots are created
            in real time. The default is True.
        animation_fr : float, optional
            The frame rate (frames per second) at which the animated plots are
            updated. The default is 10..

        Returns
        -------
        None.

        """
        # Disable keyboard use for Mac users =(
        if sys.platform == 'win32':
            self.use_keyboard = True
        elif sys.platform == 'linux':
            self.use_keyboard = True
        else:
            self.use_keyboard = False or force_keyboard
            
        # Set the visualization and animation options
        self.visualization = visualization
        self.animation = animation

        # Initialize and instance of the simulator
        self.sim = Simulator(visualization=visualization,
                             visualization_fr=visualization_fr,
                             animation=animation,
                             animation_fr=animation_fr)
        
        # Load urdf objects
        if visualization:
            # Get the path to the current directory
            path = (Path(__file__).parents[0]).absolute().as_posix()
            
            # Load the station
            station = path + "/segbot_vis/station.urdf"
            self.station_obj = self.sim.load_urdf(urdf_path=station,
                                            position=[0, 2.5, 15],
                                            roll=np.pi/2.,
                                            pitch=np.pi/2.,
                                            fixed=True,
                                            update_vis=True)
        
            # Load the segbot
            segbot = path + "/segbot_vis/segbot.urdf"
            self.segbot_obj = self.sim.load_urdf(urdf_path=segbot,
                                            position=[0, 0, 0.527],
                                            fixed=False,
                                            update_vis=True)
        
        # # If there is no animation, do not add subplots
        # if not animation:
        #     return
        
        # # Make plot for state and input
        # self.p1, self.a1 = self.sim.add_subplot(n_artists=2,
        #                                         subplot_type='line',
        #                                         title="Angles vs Time",
        #                                         x_label="Time [Seconds]",
        #                                         y_label="Angles [Deg / Rad]",
        #                                         colors=["m", "c"],
        #                                         line_widths=[2.5, 2.5],
        #                                         line_styles=["-", "-"],
        #                                         labels=["Pendulum [Deg]",
        #                                                 "Wheel [Rad]"],
        #                                         h_zero_line=True)
        # self.p2, self.a2 = self.sim.add_subplot(n_artists=1,
        #                                         subplot_type='line',
        #                                         title="Torque vs Time",
        #                                         x_label="Time [Seconds]",
        #                                         y_label="Torque [Nm]",
        #                                         y_lim=[-5.,5.],
        #                                         colors=["k"],
        #                                         line_widths=[2.5],
        #                                         line_styles=["-"],
        #                                         h_zero_line=True)
        
        # # Open the animator GUI
        # self.sim.open_animator_gui()


    def run(self,
            controller,
            max_time = None,
            station_velocity = 0.0333,
            initial_pitch_angle = 0.0,
            initial_pitch_velocity = 0.0,):
        """
        Runs a complete simulation

        Parameters
        ----------
        controller : class
            A custom class that, at a minimum, must provide the functions
            controller.run() and controller.reset()
        max_time : Float, optional
            The total amount of time the simulation is allowed to run. When
            set to None, the simulator will run until the terminal command is 
            called. If the keyboard is disabled, users are not allowed to 
            set max time as None. The default value is None. 
        station_velocity : Float, optional
            The angular velocity of the station in radians per second.
            Remains constant throughout simulation. The default value is 
            0.0333.
        initial_pitch_angle : Float, optional
            The initial pitch angle of the segbot in radians. This is set
            when the simulation starts and when the simulation is
            reset. The default value is 0.0.
        initial_pitch_velocity : Float, optional
            The initial pitch angular rate of the wheels in radians / second.
            This is set when the simulation starts and when the simulation is
            reset. The default value is 0.0.

        Returns
        -------
        data : Dictionary of Lists
            data["pitch_angle"] : List of Floats
                A list of the pitch angle in radians at each time stamp
                during the simulation.
            data["pitch_velocity"] : List of Floats
                A list of the pitch rate in radians/second at each time stamp
                during the simulation.
            data["lateral_position"] : List of Floats
                A list of the lateral position in meters each time
                stamp during the simulation.
            data["lateral_velocity"] : List of Floats
                A list of the lateral velocity in meters/second at each time
                stamp during the simulation.
            data["torque"] : List of Floats
                A list of the applied torque in Newton-meters at each time
                stamp during the simulation.
            data["time"] : List of Floats
                A list of the time stamps in seconds.

        """
        # Check max_time is valid
        if not self.use_keyboard and max_time == None:
            max_time = 10.0
            
        # Set the initial values
        self.sim.set_joint_velocity(urdf_obj=self.station_obj,
                                joint_name='space_to_ring',
                                velocity=station_velocity,
                                initial_cond=True,
                                physics=False)
        
        
        # # Reset the controller
        # controller.reset()
        
        # # Create a lists to hold the simulation data
        # time_history = []
        # pendulum_angle_history =[]
        # pendulum_velocity_history = []
        # wheel_angle_history =[]
        # wheel_velocity_history = []
        # torque_history = []

        # Await run command
        if self.use_keyboard:
            self.sim.await_keypress(key='enter')
        else:
            time.sleep(1)
            
        # Run the simulation loop
        while(not self.sim.is_done):
            # ##################################################################
            # # SENSOR
            # # Use a sensor to collect the pendulum angle and rate
            # pendulum_state = self.sim.get_joint_state(urdf_obj=self.cart_obj,
            #                                       joint_name='chassis_to_arm')
            # pendulum_angle = pendulum_state['position']
            # pendulum_rate = pendulum_state['velocity']
            
            # # Use a sensor to collect the angles and rates of each wheel
            # wheel1_state = self.sim.get_joint_state(urdf_obj=self.cart_obj,
            #                                    joint_name='chassis_to_wheel_1')
            # wheel2_state = self.sim.get_joint_state(urdf_obj=self.cart_obj,
            #                                    joint_name='chassis_to_wheel_2')
            # wheel3_state = self.sim.get_joint_state(urdf_obj=self.cart_obj,
            #                                    joint_name='chassis_to_wheel_3')
            # wheel4_state = self.sim.get_joint_state(urdf_obj=self.cart_obj,
            #                                    joint_name='chassis_to_wheel_4')
            
            # # Calculate the average wheel angle and velocity
            # wheel_angle = 0.25*(wheel1_state['position']+
            #                     wheel2_state['position']+
            #                     wheel3_state['position']+
            #                     wheel4_state['position'])
            # wheel_rate = 0.25*(wheel1_state['velocity']+
            #                    wheel2_state['velocity']+
            #                    wheel3_state['velocity']+
            #                    wheel4_state['velocity'])
            
            # ###################################################################
            # # CONTROLLER
            # # Get the torque as calculated by the controller
            # inputs = controller.run(pendulum_angle=pendulum_angle,
            #                         wheel_angle=wheel_angle,
            #                         pendulum_velocity=pendulum_rate,
            #                         wheel_velocity=wheel_rate,
            #                         time=self.sim.time)
            # torque = inputs[0]
            
            # ###################################################################
            # # SIMULATION DATA
            # # Append data to history lists
            # time_history.append(self.sim.time)
            # pendulum_angle_history.append(pendulum_angle)
            # pendulum_velocity_history.append(pendulum_rate)
            # wheel_angle_history.append(wheel_angle)
            # wheel_velocity_history.append(wheel_rate)
            # torque_history.append(torque)
            
            # ###################################################################
            # # ACTUATOR
            # # Apply one quater of the controller calculated torque to
            # # each of the four the wheels.
            self.sim.set_joint_torque(urdf_obj=self.segbot_obj,
                                      joint_name="chassis_to_left_wheel",
                                      torque=-2.,
                                      show_arrow=True,
                                      arrow_scale=0.25,
                                      arrow_offset=0.051)
            self.sim.set_joint_torque(urdf_obj=self.segbot_obj,
                                      joint_name="chassis_to_right_wheel",
                                      torque=-2.,
                                      show_arrow=True,
                                      arrow_scale=0.25,
                                      arrow_offset=-0.051)
           
            # ###################################################################
            # # UPDATE THE PLOTS
            # # This is how we add data points to the animator
            # # Plot the pendulum angle, wheel angle, and torque
            # self.sim.add_subplot_point(subplot_index=self.p1,
            #                            artist_index=self.a1[0],
            #                            x=self.sim.time,
            #                            y=180.*pendulum_angle/np.pi)
            # self.sim.add_subplot_point(subplot_index=self.p1,
            #                            artist_index=self.a1[1],
            #                            x=self.sim.time,
            #                            y=wheel_angle)
            # self.sim.add_subplot_point(subplot_index=self.p2,
            #                            artist_index=self.a2[0],
            #                            x=self.sim.time,
            #                            y=torque)
            
            ###################################################################
            # STEP THE SIMULATION
            # Step the sim
            val = self.sim.step(real_time=True,
                                update_vis=self.visualization,
                                update_ani=self.animation,
                                max_time=max_time)
            
            # # Handle resetting the controller and simulation data
            # if val == 3:
            #     # Reset the controller
            #     controller.reset()
                
            #     # Reset the history
            #     time_history = []
            #     pendulum_angle_history =[]
            #     pendulum_velocity_history = []
            #     wheel_angle_history =[]
            #     wheel_velocity_history = []
            #     torque_history = []
                
                
        # # When the simulation is done running, gather all simulation data 
        # # into a dictionary and return it
        # data = {'time' : time_history,
        #         'pendulum_angle' : pendulum_angle_history,
        #         'wheel_angle' : wheel_angle_history,
        #         'pendulum_velocity' : pendulum_velocity_history,
        #         'wheel_velocity' : wheel_velocity_history,
        #         'torque' : torque_history}
        # return data
            