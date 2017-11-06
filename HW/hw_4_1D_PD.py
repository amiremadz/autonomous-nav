class UserCode:
    def __init__(self):
        # TODO: tune gains
        self.Kp = 1.25
        self.Kd = 2.25
        self.x_prev = 0
            
    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to compute_control_command
        :param x_measured: measured position (scalar)
        :param x_desired: desired position (scalar)
        :return - control command u
        '''
        # TODO: implement PD controller
        e = x_desired - x_measured 
        edot = 0 - (x_measured - self.x_prev)/dt
        u = self.Kp * e + self.Kd * edot
        self.x_prev = x_measured

        return u

