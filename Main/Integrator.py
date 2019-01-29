from math import *

# defining constants, all units are in SI units
m = 100
z = 30000
g = -9.8
t_exp = sqrt(2 * -z / g)
v_exp = -sqrt(2 * g * -z)
step_size = 100


# defining Euler's method, takes in initial time, t, initial distance, x0, final distance, xf,
# initial velocity, v, and time step, h
def euler(t, x, xf, v, h):
    s = h
    while (x + v * h) > xf:
        t = t + h
        x = x + v * h
        v = v + g * h
    if (x + v * h) != xf:
        h = (xf - x) / v
        t = t + h
        x = x + v * h
        v = v + g * h
    find_step_size(t, x, v, s)


def find_step_size(t, x, v, s):
    if (abs(v - v_exp) <= abs(.01 * v_exp)) and abs(v - v_exp) <= abs(.01 * v_exp):
        print("\nWith step size " + str(s) + ";")
        print("The velocity is within " + str(v - v_exp) + " of the expected value")
        print("The time is within " + str(t - t_exp) + " of the expected value")
        print("The object, by Euler's method, falls " + str(z - x) + "m reaches the ground at time " + str(
            t) + "s with velocity " + str(v) + "m/s")
    else:
        s = .99 * s
        euler(0, z, 0, 0, s)


euler(0, z, 0, 0, step_size)

