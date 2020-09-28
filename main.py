from Solar_System import PySpace
ss = PySpace()

POV={
	'azim'	  : -60,
	'elev'	  : 30,
	'max_lim' : 2.5e9
	}

ss.solar_system(POV=POV,scaling='notoscale',grid='grid')