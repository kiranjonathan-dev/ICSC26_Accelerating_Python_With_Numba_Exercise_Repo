import numpy as np
import time


def print_greeting():
    print("Hello ICSC26!")
    time.sleep(0.5)
    print("Welcome to the Simutron 5000")
    print("We will now calculate your output")


def estimate_pi(n_samples):
    n_samples_inside = 0
    for i in range(n_samples):
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 <= 1:
            n_samples_inside += 1
    pi = 4 * n_samples_inside / n_samples
    return pi


def calculate_acceleration(theta_slope, g=9.81):
    time.sleep(0.1)
    return g * np.cos(theta_slope)


def time_to_ground(theta_slope, slope_length, v_slope_0, dt=0.01):
    x_slope = 0
    v_slope = v_slope_0

    time = 0
    while x_slope < slope_length:
        accel = calculate_acceleration(theta_slope)
        v_slope = v_slope + accel * dt
        x_slope = x_slope + v_slope * dt
        time += dt

    return time


def print_closing():
    print("Thank you for waiting patiently")
    print("We are hoping to do an optimisation overhaul...")
    time.sleep(1.5)
    print("in the near future")
    print("We hope you'll recommend Simutron 5000 to your friends!")


def main():
    print_greeting()

    pi = estimate_pi(10_000_000)  # No importing/hardcoding pi allowed!
    pi = np.round(pi, decimals=2)  # Required to remove randomness for testing
    print(f"Pi now estimated as {pi}, simulation can commence...")

    slope_angle = pi / 3
    slope_length = 10
    result = time_to_ground(
        theta_slope=slope_angle, slope_length=slope_length, v_slope_0=0
    )
    print(
        f"Time for mass to travel down slop of length {slope_length}m and incline {slope_angle}rad: "
    )
    print(f"{result} s")

    print_closing()

    return result


main()
