import numpy as np
from plot import plot_trajectory

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
      
    def rotate(self, yaw):
        from math import sin, cos
        mat = np.array([[cos(yaw), -sin(yaw)], [sin(yaw), cos(yaw)]])
        return mat
        
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''
        
        vx = navdata.vx
        vy = navdata.vy
      
        v = np.array([[vx], [vy]])
        
        yaw = navdata.rotZ 
        
        # to go from local velocity to global velocity
        mat = self.rotate(yaw)
        v_world = np.dot(mat, v)

        self.position = v_world * dt + self.position
        
        # TODO: update self.position by integrating measurements contained in navdata
        plot_trajectory("odometry", self.position)