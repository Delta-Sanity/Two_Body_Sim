# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:58:54 2022

@author: Sam
"""

import numpy as np



class particle():

    def __init__(self, init_mass, init_pos, init_vel):
        self.mass = int(init_mass)
        self.pos = np.array(init_pos, dtype = 'float32')
        self.vel = np.array(init_vel, dtype = 'float32')

    def motion(self, inv_sec):                  #Simulates motion by summing velocity vector with position vector and setting the result as the new position
                                                #variable 'inv_sec' refers to the inverse of a second (s^-1), the length of time the motion is intended to simulate (The number of )
        pos_2 = self.pos + (np.float32(1 / inv_sec)*(self.vel))

        self.pos = pos_2

    def accel(self, acceleration, inv_sec):
        
        vel_2 = self.vel + (np.float32(1 / inv_sec)*(acceleration))

        self.vel = vel_2

def grav_calc(particle1, particle2): #Uses newtons universal law of gravitation to find gravitational force between the two particles
    G_const = np.float32(6.674e-11)
    
    dist = np.sqrt(np.sum(np.square(particle1.pos - particle2.pos)))

    grav_force = G_const * ((particle1.mass * particle2.mass) / (dist ** 2)) #returns value in newtons
    
    p1_grav_unit_vector = ((particle2.pos - particle1.pos) / dist)
    p2_grav_unit_vector = ((particle1.pos - particle2.pos) / dist)
    
    p1_grav_force_vector = ((grav_force / particle1.mass) * p1_grav_unit_vector)
    p2_grav_force_vector = ((grav_force / particle2.mass) * p2_grav_unit_vector)
    
    final_vects = [p1_grav_force_vector, p2_grav_force_vector]
    
    return(final_vects)

def single_particle_sim(particle, time, time_detail, rec_all, acceleration):   #Produces an Array of states that can be used to graph the path of a particle
    #Notes:
    # time_detail refers to the number of times per simulation second motion is simulated. For example: if time_detail = 5, then motion will be simulated 5 times per second
    # or every 0.2 seconds
    # rec_all, if true records both position and velocity data, if false, records only position data
    
    path = []
    total_steps = time * time_detail
    current_step = 0

    while current_step < total_steps:

        if rec_all:
            state = [particle.pos, particle.vel]
        else:
            state = particle.pos
        
        path.append(state)
        
        particle.accel(acceleration, time_detail)
        particle.motion(time_detail)
        
        current_step = current_step + 1

    return(np.array(path))

def two_body_sim(particle1, particle2, time, time_detail, rec_all):
    
    p1_path = []
    p2_path = []
    
    total_steps = time * time_detail
    current_step = 0
    
    while current_step < total_steps:
        
        if rec_all:
            p1_state = [particle1.pos, particle1.vel]
            p2_state = [particle2.pos, particle2.vel]
        else:
            p1_state = particle1.pos
            p2_state = particle2.pos
        
        p1_path.append(p1_state)
        p2_path.append(p2_state)
        
        grav_vects = grav_calc(particle1, particle2)
        
        particle1.accel(grav_vects[0], time_detail)
        particle2.accel(grav_vects[1], time_detail)
        
        particle1.motion(time_detail)
        particle2.motion(time_detail)
        
        current_step = current_step + 1
        
    combined_paths = [np.array(p1_path), np.array(p2_path)]
    return(combined_paths)