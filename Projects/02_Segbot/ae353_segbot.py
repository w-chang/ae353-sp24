"""
This modules provides a backend for the ae353 segbot example
"""

###############################################################################
#DEPENDENCIES
###############################################################################
from condynsate.simulator import Simulator
from pathlib import Path
import numpy as np


###############################################################################
#SIMULATION CLASS
###############################################################################
class Segbot_sim():
    def __init__(self,
                 use_keyboard=True,
                 visualization=True,
                 visualization_fr=20.,
                 animation=True,
                 animation_fr=10.):
        """
        Initializes an instance of the simulation class.

        Parameters
        ----------
        keyboard : bool, optional
            A boolean flag that indicates whether the simulation will allow
            the use of keyboard interactivity. The default is True.
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
        # Set the visualization and animation options
        self.visualization = visualization
        self.animation = animation

        # Initialize and instance of the simulator
        self.sim = Simulator(keyboard=use_keyboard,
                             visualization=visualization,
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
        
        # If there is no animation, do not add subplots
        if not animation:
            return
        
        # Make plot for state and input
        self.p1, self.a1 = self.sim.add_subplot(n_artists=2,
                                                subplot_type='line',
                                                title="Angles vs. Time",
                                                x_label="Time [Seconds]",
                                                y_label="Angles [Rad]",
                                                colors=["m", "c"],
                                                line_widths=[2.5, 2.5],
                                                line_styles=["-", "-"],
                                                labels=["Pitch", "Yaw"])
        self.p2, self.a2 = self.sim.add_subplot(n_artists=2,
                                                subplot_type='line',
                                                title="Position vs. Time",
                                                x_label="Time [Seconds]",
                                                y_label="Positions [Meters]",
                                                colors=["r", "b"],
                                                line_widths=[2.5, 2.5],
                                                line_styles=["-", "-"],
                                                labels=["Lat", "Long"])
        
        # Open the animator GUI
        self.sim.open_animator_gui()


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
        # Set the initial values
        self.sim.set_joint_velocity(urdf_obj=self.station_obj,
                                joint_name='space_to_ring',
                                velocity=station_velocity,
                                initial_cond=True,
                                physics=False)
        
        
        # Reset the controller
        controller.reset()
        
        # # Create a lists to hold the simulation data
        # time_history = []
        # pendulum_angle_history =[]
        # pendulum_velocity_history = []
        # wheel_angle_history =[]
        # wheel_velocity_history = []
        # torque_history = []

        # Await run command
        self.sim.await_keypress(key='enter')
            
        # Run the simulation loop
        while(not self.sim.is_done):
            ##################################################################
            # SENSOR
            # Use a sensor to collect the pendulum angle and rate
            body_state = self.sim.get_base_state(urdf_obj=self.segbot_obj,
                                                 body_coords=True)
            world_state = self.sim.get_base_state(urdf_obj=self.segbot_obj,
                                                  body_coords=False)
            pitch = body_state['pitch']
            pitch_vel = body_state['angular velocity'][1]
            yaw = body_state['yaw']
            yaw_vel = body_state['angular velocity'][2]
            long_pos = world_state['position'][0]
            long_vel = world_state['velocity'][0]
            lat_pos = world_state['position'][1]
            lat_vel = world_state['velocity'][1]
            
            ###################################################################
            # CONTROLLER
            # Get the torque as calculated by the controller
            sw = self.sim.is_pressed("shift+w")
            w = self.sim.is_pressed("w")
            ss = self.sim.is_pressed("shift+s")
            s = self.sim.is_pressed("s")
            sd = self.sim.is_pressed("shift+d")
            d = self.sim.is_pressed("d")
            sa = self.sim.is_pressed("shift+a")
            a = self.sim.is_pressed("a")
            inputs = controller.run(pitch=pitch,
                                    pitch_velocity=pitch_vel,
                                    yaw=yaw,
                                    yaw_vel=yaw_vel,
                                    lateral_position=lat_pos,
                                    lateral_velocity=lat_vel,
                                    longitudinal_position=long_pos,
                                    longitudinal_velocity=long_vel,
                                    time=self.sim.time,
                                    sw=sw,
                                    w=w,
                                    ss=ss,
                                    s=s,
                                    sd=sd,
                                    d=d,
                                    sa=sa,
                                    a=a)
            left_torque = -inputs[0]
            right_torque = -inputs[1]
            
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
                                      torque=left_torque,
                                      show_arrow=True,
                                      arrow_scale=0.25,
                                      arrow_offset=0.051)
            self.sim.set_joint_torque(urdf_obj=self.segbot_obj,
                                      joint_name="chassis_to_right_wheel",
                                      torque=right_torque,
                                      show_arrow=True,
                                      arrow_scale=0.25,
                                      arrow_offset=-0.051)
           
            ###################################################################
            # UPDATE THE PLOTS
            # This is how we add data points to the animator
            self.sim.add_subplot_point(subplot_index=self.p1,
                                       artist_index=self.a1[0],
                                       x=self.sim.time,
                                       y=pitch)
            self.sim.add_subplot_point(subplot_index=self.p1,
                                       artist_index=self.a1[1],
                                       x=self.sim.time,
                                       y=yaw)
            self.sim.add_subplot_point(subplot_index=self.p2,
                                       artist_index=self.a2[0],
                                       x=self.sim.time,
                                       y=lat_pos)
            self.sim.add_subplot_point(subplot_index=self.p2,
                                       artist_index=self.a2[1],
                                       x=self.sim.time,
                                       y=long_pos)
            
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
        return val
            