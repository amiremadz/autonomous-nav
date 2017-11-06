import numpy as np

class State:
    def __init__(self):
        self.position = np.zeros((3,1))
        self.velocity = np.zeros((3,1))

class UserCode:
    def __init__(self):
        # TODO: tune gains
    
        # xy control gains
        Kp_xy = 0.5 # xy proportional
        Kd_xy = 0.0 # xy differential
        
        # height control gains
        Kp_z  = 0.5 # z proportional
        Kd_z  = 0.0 # z differential
        
        self.Kp = np.array([[Kp_xy, Kp_xy, Kp_z]]).T
        self.Kd = np.array([[Kd_xy, Kd_xy, Kd_z]]).T
    
    def compute_control_command(self, t, dt, state, state_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param state: State - current quadrotor position and velocity computed from noisy measurements
        :param state_desired: State - desired quadrotor position and velocity
        :return - xyz velocity control signal represented as 3x1 numpy array
        '''
        # plot current state and desired setpoint
        self.plot(state.position, state_desired.position)
        
        # TODO: implement PID controller computing u from state and state_desired
        e    = state_desired.position - state.position
        edot = state_desired.velocity - state.velocity 
        
        e_x = e[0]
        e_y = e[1]
        e_z = e[2]
        
        edot_x = edot[0]
        edot_y = edot[1]
        edot_z = edot[2]
        
        ux = self.Kp[0] * e_x + self.Kd[0] * edot_x
        uy = self.Kp[1] * e_y + self.Kd[1] * edot_y
        uz = self.Kp[2] * e_z + self.Kd[2] * edot_z
        
        u = np.array([[ux, uy, uz]]).T
        
        return u
        
    def plot(self, position, position_desired):
        from plot import plot
        plot("x", position[0])
        plot("x_des", position_desired[0])
        plot("y", position[1])
        plot("y_des", position_desired[1])
        plot("z", position[2])
        plot("z_des", position_desired[2])
        
