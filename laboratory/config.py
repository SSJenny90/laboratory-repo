"""
This is a configuration file for setting up the laboratory. It contains settings to set the name of the the experiment, sample dimensions, instrument addresses and physical constants. Experiment name and sample dimensions should be modified with each new experiment. Everything else can remain as is unless the physical setup of the lab has changed.
"""
import os
from datetime import datetime

#if you wish to receive email updates when the program completes each step
EMAIL = 'samuel.jennings@adelaide.edu.au'

#-------------------Experiment settings-------------------
PROJECT_NAME = 'Test3'
SAMPLE_THICKNESS = 2.6 #in mm
SAMPLE_DIAMETER = 12.7 #in mm
SAMPLE_AREA = 97.686 #in mm^2 - ONLY SET IF SAMPLE IS NOT A COMPLETE DISK AND AREA MUST BE CALCULATED MANUALLY

MINIMUM_FREQ = 20       #in Hz
MAXIMUM_FREQ = 2000000  #in Hz (2MHz)
FREQ_LOG_SCALE = False
FREQUENCY_LIST = []

DEBUG = False

START_TIME = None
"""Starts the experiment at the given date and time. Can be any datetime object in the future

START_TIME = datetime(  year=2019,
                        day=3,
                        month=10,
                        hour=18,
                        minute=17)
"""


#-------------------Folder defaults-------------------
ROOT = os.getcwd()
DATA_DIR = os.path.join(ROOT,'data')
LOG_DIR = os.path.join(ROOT,'log')
CALIBRATION_DIR = os.path.join(ROOT,'laboratory','calibration')


GLOBAL_MAXTRY = 5
#-------------------DAQ settings-------------------
DAQ_ADDRESS = 'USB0::0x0957::0x2007::MY49021284::INSTR'
REFERENCE_TEMPERATURE = '101'
ELECTRODE_1 = '104'
ELECTRODE_2 = '105'
VOLTAGE = '103'
SWITCH = '205,206'
THERMISTOR_OHMS = 10000
TEMPERATURE_INTEGRATION_TIME = 10   #in cycles
VOLTAGE_INTEGRATION_TIME = 1   #in cycles

#-------------------LCR settings-------------------
LCR_ADDRESS = 'USB0::0x0957::0x0909::MY46312484::INSTR'

#-------------------Furnace settings-------------------
FURNACE_ADDRESS = 'COM8'
RESET_TEMPERATURE = 40       #temperature the furnace resets to

#-------------------Stage settings-------------------
MOTOR_ADDRESS = 'COM5'
SUBDIVISION = 2  #from back of motion controller
STEP_ANGLE = 0.9  #from the side of the stage
PITCH = 4        #in mm - from the optics focus website
MAXIMUM_STAGE_POSITION = 10000
EQUILIBRIUM_POSITION = 'furnace_profile.pkl'

#-------------------Gas settings-------------------
MFC_ADDRESS = 'COM6'    #for windows
# MFC_ADDRESS = '/dev/tty.SLAB_USBtoUART'   #for mac

CO2 = { 'address':'A',
        'upper_limit': 200,
        'precision':2}

CO_A = {'address':'B',
        'upper_limit': 50,
        'precision':2}

CO_B = {'address':'C',
        'upper_limit': 2,
        'precision':3}

H2 = {  'address':'D',
        'upper_limit': 50,
        'precision':2}




