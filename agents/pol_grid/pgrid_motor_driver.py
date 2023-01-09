##########################################################################
#
# Polarizing Grid Motor Control for UCSD
#
# Gavin Roberts
# gsroberts@ucsd.edu
# 20220919
#
# This program was modified from the appmotion_motors_driver.py code used to 
# control the two motors (output polarizer and linear stage) that are used by the FTS.
# This assumes the motor controllers have been configured properly using the 
# ST Configurator Windows application.
#
# NEED TO DOCUMENT HOW THE MOTOR CONTROLLERS SHOULD BE CONFIGURED.
#
# Commands for communicating with the motor controllers can be found here:
# https://appliedmotion.s3.amazonaws.com/Host-Command-Reference_920-0002W_0.pdf
#
##########################################################################

import sys
#from tkinter.ttk import setup_master
from socs.agent.moxaSerial import Serial_TCPServer
from time import sleep
import numpy as np


# Time to wait for the user to power on the controllers and to see the
# power-on signature from the serial port
DEFAULT_WAIT_START_TIME = 15.0  # seconds

# Alarm Codes
POS_ALM = 'AL=0001'         # postition alarm
CCW_LMT_ALM = 'AL=0002'     # counter-clockwise limit alarm
CW_LMT_ALM = 'AL=0004'      # clockwise limit alarm
OVR_TMP_ALM = 'AL=0008'     # over temperature alarm 
INT_VOL_ALM = 'AL=0010'     # internal voltage alarm
OVR_VOL_ALM = 'AL=0020'     # over voltage alarm
UND_VOL_ALM = 'AL=0040'     # under voltage alarm
OVR_CUR_ALM = 'AL=0080'     # over current alarm
BAD_HAL_SNS_ALM = 'AL=0100' # bad hall sensor alarm
BAD_ENC_ALM = 'AL=0200'     # bad encoder alarm
COM_ERR_ALM = 'AL=0400'     # communication error alarm
BAD_FLS_ALM = 'AL=0800'     # bad flash alarm
WZD_FLD_ALM = 'AL=1000'     # wizard failed alarm
MTR_RES_ALM = 'AL=2000'     # motor resistance alarm
BLK_QSG_ALM = 'AL=4000'     # blank Q segment alarm
NO_MV_ALM = 'AL=8000'       # no move alarm

class Motor:
    def __init__(self, ip, port, mot_id=None):
        print(ip)
        print(port)

        self.ip = ip
        self.port = port
        self.mot_id = mot_id

        self.ser = Serial_TCPServer((ip, port))

        self.sock_status = 0

        # Connect to motor over MOXA serial server
        if not (ip and port):
            print("Invalid Motor information. No Motor control.")
            self.ser = None
        else:
            print('establishing serial server with motor!')
            self.ser

        # Verify motor is in ready state and reset if necessary
        if self.ser:
            msg = self.ser.writeread('RS\r')  # RS = Request Status
            self.ser.flushInput()
            print(msg)
            if (msg == 'RS=R'): # R = Ready
                print("%s in ready state." % (self.mot_id))
            elif (msg != 'RS=R'):
                print(
                    "%s not in ready state.  Resetting." %
                    (self.mot_id))
                print("Message was: ", msg)
                self.kill_all_commands()
                # TODO: Reset motor

                #if ('A' in msg[3:]): # A = Alarm
                if (msg == 'RS=AR'):
                    amsg = self.ser.writeread('AL\r')  # AL = Alarm Code
                    self.alarm_handler(amsg)
                    print("Alarm was found. Resetting.")
                    self.reset_alarms()
                else:
                    print('Irregular message received.')
                    sys.exit(1)
    
        msg = self.ser.writeread('EG\r') # EG = Electronic Gearing
        if (len(msg) <= 4): # Need at least EG=A + \r, which is 5 characters
            print(
                "Couldn't get microstep resolution for %s. Disconnect and retry." %
                (self.mot_id))
        else:
            print(msg)
            self.s_p_rev = float(msg[3:])

        if (self.ser is not None):
            # DL3 = inputs are not used as end-of-travel limit inputs 
            #       and can be used as a general purpose inputs.
            msg = self.ser.writeread('DL\r')
            print(f"msg: {msg}")
            if msg != 'DL=3':
                print("Limits not defined as not used. Resetting...")
                self.ser.flushInput()
                self.ser.write('DL3\r')  # DL3 = Define Limits as not used
                sleep(0.1)

            msg = self.ser.writeread('CC\r')  # CC = Change Current
            print(msg)
            current = float(msg[3:])
            if current < 1.5:
                print("Operating current insufficient. Resetting...")
                self.ser.flushInput()
                self.ser.write('CC1.5\r')

    def alarm_handler(self, msg):
        """alarm_handler(msg)

        **Helper Function** - Prints the alarm message and returns 
        true if an alarm is found. Returns false otherwise.

        Parameters:
            msg (str): The message to be parsed for an alarm.
        """
        if (msg == POS_ALM):
            print('Position alarm.')
            return True
        elif (msg == CCW_LMT_ALM):
            print('CCW limit switch hit unexpectedly.')
            return True
        elif (msg == CW_LMT_ALM):
            print('CW limit switch hit unexpectedly.')
            return True
        elif (msg == OVR_TMP_ALM):
            print('Over temperature alarm.')
            return True
        elif (msg == INT_VOL_ALM):
            print('Internal voltage alarm.')
            return True
        elif (msg == OVR_VOL_ALM):
            print('Over voltage alarm.')
            return True
        elif (msg == UND_VOL_ALM):
            print('Under voltage alarm.')
            return True
        elif (msg == OVR_CUR_ALM):
            print('Over current alarm.')
            return True
        elif (msg == BAD_HAL_SNS_ALM):
            print('Bad hall sensor alarm.')
            return True
        elif (msg == BAD_ENC_ALM):
            print('Bad encoder alarm.')
            return True
        elif (msg == COM_ERR_ALM):
            print('Communication error alarm.')
            return True
        elif (msg == BAD_FLS_ALM):
            print('Bad flash alarm.')
            return True
        elif (msg == WZD_FLD_ALM):
            print('Wizard failed alarm.')
            return True
        elif (msg == MTR_RES_ALM):
            print('Motor resistance alarm.')
            return True
        elif (msg == BLK_QSG_ALM):
            print('Blank Q segment alarm.')
            return True
        elif (msg == NO_MV_ALM):
            print('No move alarm.')
            return True
        else:
            return False
        
    def is_moving(self, verbose=True):
        """
        Returns True if motor is moving, False otherwise.
        Also returns True if the motor provides an irregular
        status message, such as any alarm keys.

        Parameters:
            verbose (bool): Prints output from motor requests if True.
                (default False)
        """
        # Get the status of the motor and print if verbose = True
        print(f'*************\n Driver: is_moving for motor: {self.mot_id}\n***********')
        msg = self.ser.writeread('RS\r')  # RS = Request Status
        if verbose:
            print(f'verbose; message: {msg}')
            sys.stdout.flush()
        # If either motor is moving, immediately return True
        if (msg == 'RS=FMR'):
            if verbose:
                print(f'Motor {self.mot_id} is still moving.')
            return True
        elif (msg == 'RS=R'):
            if verbose:
                print(f'Motor {self.mot_id} is not moving.')
            return False
        elif ('A' in msg[3:]):
            if verbose:
                print(f'Motor {self.mot_id} threw an alarm.')
            # Check what the alarm message is
            msg = self.ser.writeread('AL\r')
            return self.alarm_handler(msg)
        else:
            print(f'Irregular error message for motor {self.mot_id}: {msg}')
            return True

    def kill_all_commands(self):
        """
        Stop all active commands on the device.
        """
        # SK = Stop & Kill - Stop/kill all commands, turn off waiting for
        # input
        self.ser.flushInput()
        self.ser.write('SK\r')
        
    def set_motor_enable(self, enable=True):
        """
        Set motor enable to true or false for given axis. Should
        disable motor when stopped for lower noise data acquisition.

        Parameters:
            enable (bool): Enables specified motor if True, disables specified
                motor if False.
        """
        self.ser.flushInput()
        if enable:
            self.ser.write('ME\r')  # ME = Motor Enable
        else:
            self.ser.write('MD\r')  # MD = Motor Disable
        
    def start_rotation(self):
        """
        Starts jogging specifically for the rotation of the output
        polarizer in the FTS.

        Parameters:
            rot_vel (float): The rotation velocity in revolutions per second 
                within range [0.25,50]. (default 12.0)
            rot_accel (float): The acceleration in revolutions per second per
                second within range [1,3000].  (default 1.0)
        """
        # Set the jog parameters
        #self.ser.write('JS%1.3f\r' % (rot_vel))  # JS = Jog Speed
        #self.ser.write('JA%i\r' % (rot_accel))  # JA = Jog Acceleration
        #self.ser.write('JL%i\r' % (rot_accel))  # JL = Jog Decel
        
        # Start rotation
        self.ser.write('CJ\r')  # CJ = Commence Jogging
        self.ser.flushInput()

    def stop_rotation(self):
        """
        Stops jogging for the rotation of the specified motor.
        """
        self.ser.flushInput()
        self.ser.write('SJ\r')  # SJ = Stop Jogging

    def set_rot_vel(self, rot_vel=5.0):
        """
        Set the rotational velocity of the motor while jogging already in progress.

        Parameters:
            rot_vel (float): The rotational velocity in revolutions per second.
        """
        
        #self.ser.write('CS%1.3f\r' % (rot_vel))
        self.ser.write('JS%1.3f\r' % (rot_vel))
        self.ser.flushInput()

    def get_rot_vel(self):
        """
        Returns the rotational velocity of the motor in revolutions per second.
        """
        msg = self.ser.writeread('JS\r')
        velocities = msg[3:]
        return velocities
        
    def set_rot_accel(self,rot_accel=1.0):
        """
        Set the rotational acceleration of the motor

        Parameters:
            acceleration (float): The acceleration in revolutions per second per
                second within range [1,3000].
        """
        self.ser.write('JA%1.3f\r' % (rot_accel))
        self.ser.write('JL%1.3f\r' % (rot_accel))
        self.ser.flushInput()

    def get_rot_accel(self):
        """
        Set the rotational acceleration of the motor

        Returns:
            rot_accel (float): the rotational acceleration of polarizing grid motor 
                in revolutions per second per second
        """
        accel = []
        msg = self.ser.writeread('JA\r')
        accel.append(int(msg[3:]))
        return accel

    def rotate_by_degrees(self,deg):
        """
        Rotate the polarizer grid by a fixed amount relative to its current position

        Parameters:
            deg (float): The number of degrees to rotate the polarizer by.
        """
        # the number of turns of the motor per 1 turn of the grid?? i.e. 1 turn of the motor moves the grid by 60 deg i think
        # deg * rev/deg * steps/rev = steps 

        unit_pos = int(deg*self.s_p_rev/60.) # 60 is the degrees per revolution

        # Move the motor
        self.ser.write('DI%i\r' % (unit_pos))  # DI = Distance/Position
        self.ser.write('FL\r')  # FL = Feed to Length
        self.ser.flushInput()
        print(unit_pos)
    
    def reset_alarms(self):
        """
        Resets alarm codes present. Only advised if you have checked
        what the alarm is first!
        """
        self.ser.flushInput()
        self.ser.write('AR\r')

    def close_connection(self):
        """
        Close the connection to the serial controller for the
        specified motor.
        """
        self.ser.sock.close()
        print("Connection to serial controller disconnected.")

    def reconnect_motor(self):
        """
        Reestablish connection with specified motor.
        """
        print(f"port: {self.port}")
        try:
            self.ser.sock.close()
            sleep(1)
            del self.ser
            self.ser = Serial_TCPServer((self.ip, self.port))
            print("Connection has been established.")
            self.sock_status = 1
        except ConnectionError:
            print("Connection could not be reestablished.")
            self.sock_status = 0

    def get_position(self, pos_type='steps'):
        """
        Get relative pol grid position in counts or radians.
        """
        positions = []
        #s_p_rev (steps per revolution) is equal to 60 degrees. Conversion of steps to radians is below.
        #steps * rev/steps * deg/rev = deg
        steps_to_deg = (1/self.s_p_rev*60)
        msg = self.ser.writeread('IF\r')
        if msg == 'IF=H':
            # Output is coming out in hexadecimal, switching to decimal
            print('Changing output to decimal')
            self.ser.writeread('IFD\r')
            
        i_pos = self.ser.writeread('IP\r')
        sleep(0.1)
        self.ser.flushInput()
        i_pos = int(i_pos.rstrip('\r')[3:])
        if pos_type == 'steps':
            i_pos = i_pos
        elif pos_type == 'deg':
            i_pos = i_pos*steps_to_deg
        elif pos_type == 'wrap_deg':
            i_pos = (i_pos*steps_to_deg) % 360
            
        positions.append(i_pos)
        
        return positions
        
    def set_zero(self):
        """
        Set home position of pol grid.
        """
        
        self.ser.write('SP0\r')  # SP = Set Position
        self.ser.flushInput()