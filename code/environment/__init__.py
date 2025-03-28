'''
This module contains classes that are used for simulating palletization.
'''
HEIGHT_TOLERANCE_MM = 5  # mm

SIZE_ROLLCONTAINER = (800, 700)  # mm
'''The base area of the target "rollcontainer" in millimeters.'''
SIZE_EURO_PALLET = (1200, 800)  # mm
'''The base area of the target "euro-pallet" in millimeters.'''
MAXHEIGHT_TARGET = 2000  # mm
'''The maximum height of the observation space/target in millimeters.'''

MAXHEIGHT_OBSERVATION_SPACE = 2000  # mm
'''The maximum height of the observation space/target in millimeters.'''

from environment.HeightMap import HeightMap
from environment.PalletizingEnvironment import PalletizingEnvironment
from environment.LC import LC

from environment.Space3D import Space3D
from environment.Item3D import Item3D

from environment.SimPalEnv import SimPalEnv

