import numpy as np
import time


def print_greeting():
    print("Hello ICSC26!")
    time.sleep(0.5)
    print("Welcome to the Simutron 5000")
    print("We will now calculate your output, please wait...")


def estimate_pi(n_samples=10_000_000):
    n_samples_inside = 0
    for i in range(n_samples):
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 <= 1:
            n_samples_inside += 1
    pi = 4 * n_samples_inside / n_samples
    return np.round(pi, decimals=2)  # Removes randomness to make testing simpler


def calculate_acceleration(theta_slope, g=9.81):
    return g * np.sin(theta_slope)


def time_to_ground(theta_slope, slope_length, v_slope_0, dt=1e-6):
    x_slope = 0
    v_slope = v_slope_0

    time = 0
    while x_slope < slope_length:
        accel = calculate_acceleration(theta_slope)
        v_slope = v_slope + accel * dt
        x_slope = x_slope + v_slope * dt
        time += dt

    return time


def print_statistics(slope_length, slope_fracs_to_test, times):
    for i in range(len(times)):
        print(
            f"Time for mass to travel down slop of length {slope_length}m and incline {slope_fracs_to_test[i] * estimate_pi()} rad: "
        )
        print(f"{times[i]}s")

    sum = 0
    for i in range(len(times)):
        sum += times[i]
    mean_time = sum / len(times)

    print(f"Mean time to ground across all runs: {mean_time}s")


def print_closing():
    print("Thank you for waiting patiently")
    print("We are hoping to do an optimisation overhaul...")
    time.sleep(5)
    print("in the near future")
    print("We hope you'll recommend Simutron 5000 to your friends!")


def main():
    print_greeting()

    slope_length = 10
    slope_fracs_to_test = [1 / 6, 1 / 3, 1 / 2]

    times = []
    for slope_angle_pi_frac in slope_fracs_to_test:
        slope_angle = estimate_pi() * slope_angle_pi_frac

        print(f"Calculating for slope angle = {slope_angle}rad...")

        time = time_to_ground(
            theta_slope=slope_angle,
            slope_length=slope_length,
            v_slope_0=0,
        )
        times.append(time)

    print("Calculations finished!")

    print_statistics(slope_length, slope_fracs_to_test, times)

    print_closing()

    return times
