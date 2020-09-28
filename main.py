from Solar_System import PySpace
ss = PySpace()

POV = {'azim'     : -45,
        'elev'    : 0,
        'max_lim' : 2e7}

ss.solar_system(POV=POV,scaling='notoscale',grid='grid')