
################################################################################
# begining of class
################################################################################

class PyData():
    """
    class containg all astro data for plotting
    """

    def __init__(self, scaling):
        self.scaling = scaling

        if self.scaling == 'Accurate':
            self.sun_scaling_factor     = 1
            self.mercury_scaling_factor = 1
            self.venus_scaling_factor   = 1
            self.earth_scaling_factor   = 1
            self.mars_scaling_factor    = 1
            self.jupiter_scaling_factor = 1
            self.saturn_scaling_factor  = 1
            self.uranus_scaling_factor  = 1
            self.neptune_scaling_factor = 1
            self.pluto_scaling_factor   = 1

        if self.scaling != 'Accurate':
        # scalings (first two letters + s)
            gen_scaling_factor = 2000
            self.sun_scaling_factor     = gen_scaling_factor*0.015
            self.mercury_scaling_factor = gen_scaling_factor
            self.venus_scaling_factor   = gen_scaling_factor
            self.earth_scaling_factor   = gen_scaling_factor
            self.mars_scaling_factor    = gen_scaling_factor
            self.jupiter_scaling_factor = gen_scaling_factor
            self.saturn_scaling_factor  = gen_scaling_factor
            self.uranus_scaling_factor  = gen_scaling_factor
            self.neptune_scaling_factor = gen_scaling_factor
            self.pluto_scaling_factor   = gen_scaling_factor

        ########################################################################
        # Moon data
        ########################################################################

        self.earth_moons = [{'moon_name'         : 'Moon',
                    'moon_radius'       : 1737*self.earth_scaling_factor,
                    'moon_orbit_radius' : 384402}]

        self.m_moons = [{'moon_name'         : 'Deimos',
                    'moon_radius'       : 6*self.mars_scaling_factor,
                    'moon_orbit_radius' : 23463},

                   {'moon_name'         : 'Phobos',
                   'moon_radius'       : 11*self.mars_scaling_factor,
                   'moon_orbit_radius' : 9376}]

        self.jupiter_moons = [{'moon_name'         : 'Io',
                    'moon_radius'       : 1821*self.jupiter_scaling_factor,
                    'moon_orbit_radius' : 421700},

                   {'moon_name'         : 'Europa',
                   'moon_radius'       : 1560*self.jupiter_scaling_factor,
                   'moon_orbit_radius' : 670900},

                   {'moon_name'         : 'Gannymede',
                   'moon_radius'       : 2634*self.jupiter_scaling_factor,
                   'moon_orbit_radius' : 1070400},

                   {'moon_name'         : 'Callisto',
                   'moon_radius'       : 2410*self.jupiter_scaling_factor,
                   'moon_orbit_radius' : 1882700}]

        self.saturn_moons = [{'moon_name'         : 'Enceladus',
                    'moon_radius'       : 521*self.saturn_scaling_factor,
                    'moon_orbit_radius' : 237948},

                   {'moon_name'         : 'Titan',
                    'moon_radius'       : 2574*self.saturn_scaling_factor,
                    'moon_orbit_radius' : 1221870}]

        ########################################################################
        # Gas Rings data
        ########################################################################

        self.saturn_rings = {'minimum_ring_radius'  : 7e3*self.saturn_scaling_factor,
                    'maximum_ring_radius' : 8e4*self.saturn_scaling_factor,
                    'ring_inclination'    : 1}

        ########################################################################
        # Host Star data
        ########################################################################

        # planets
        self.sun_info={
                    'name'                : 'Sun',
                    'orbit_colour'        : 'gold',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 0,
                    'body_radius'         : 605000*self.sun_scaling_factor,
                    'orbital_inclination' : 0,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        ########################################################################
        # Planet data
        ########################################################################

        self.mercury_info={
                    'name'                : 'Mercury',
                    'orbit_colour'        : 'peru',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 46e6,
                    'body_radius'         : 2440*self.mercury_scaling_factor,
                    'orbital_inclination' : 7.005,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.venus_info={
                    'name'                : 'Venus',
                    'orbit_colour'        : 'goldenrod',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 107e6,
                    'body_radius'         : 6052*self.venus_scaling_factor,
                    'orbital_inclination' : 3.3947,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.earth_info={
                    'name'                : 'Earth',
                    'orbit_colour'        : 'forestgreen',
                    'rings_info'          : 'no',
                    'moons_info'          : self.earth_moons,
                    'orbit_radius'        : 149e6,
                    'body_radius'         : 6378*self.earth_scaling_factor,
                    'orbital_inclination' : 0,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.mars_info={
                    'name'                : 'Mars',
                    'orbit_colour'        : 'firebrick',
                    'rings_info'          : 'no',
                    'moons_info'          : self.m_moons,
                    'orbit_radius'        : 205e6,
                    'body_radius'         : 3397*self.mars_scaling_factor,
                    'orbital_inclination' : 1.851,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.jupiter_info={
                    'name'                : 'Jupiter',
                    'orbit_colour'        : 'sandybrown',
                    'rings_info'          : 'no',
                    'moons_info'          : self.jupiter_moons,
                    'orbit_radius'        : 741e6,
                    'body_radius'         : 71492*self.jupiter_scaling_factor,
                    'orbital_inclination' : 1.305,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.saturn_info={
                    'name'                : 'Saturn',
                    'orbit_colour'        : 'yellow',
                    'rings_info'          : self.saturn_rings,
                    'moons_info'          : self.saturn_moons,
                    'orbit_radius'        : 1.35e9,
                    'body_radius'         : 60268*self.saturn_scaling_factor,
                    'orbital_inclination' : 2.484,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.uranus_info={
                    'name'                : 'Uranus',
                    'orbit_colour'        : 'powderblue',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 2.75e9,
                    'body_radius'         : 25559*self.uranus_scaling_factor,
                    'orbital_inclination' : 0.77,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }
       
        self.neptune_info={
                    'name'                : 'Neptune',
                    'orbit_colour'        : 'dodgerblue',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 4.45e9,
                    'body_radius'         : 24766*self.neptune_scaling_factor,
                    'orbital_inclination' : 1.769,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

        self.pluto_info={
                    'name'                : 'Pluto',
                    'orbit_colour'        : 'dimgrey',
                    'rings_info'          : 'no',
                    'moons_info'          : 'no',
                    'orbit_radius'        : 4.46e9,
                    'body_radius'         : 1150*self.pluto_scaling_factor,
                    'orbital_inclination' : 17.142,
                    'init_orbit_position' : 0,
                    'orbit_len_earth_yrs' : 1
                    }

################################################################################
# End of class
################################################################################
