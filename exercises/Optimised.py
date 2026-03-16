import numpy as np
import numba
import time


def print_greeting():
    print("Hello ICSC26!")
    print("Welcome to the Simutron 5000")
    print("We will now calculate your output, please wait...")


@numba.jit(parallel=True)  # Parallel JIT this
def estimate_pi(n_samples=10_000_000):
    n_samples_inside = 0
    for i in numba.prange(n_samples):  # Don't forget prange!
        x = np.random.random()
        y = np.random.random()
        if x**2 + y**2 <= 1:
            n_samples_inside += 1
    pi = 4 * n_samples_inside / n_samples
    return np.round(pi, decimals=2)  # Removes randomness to make testing simpler


@numba.jit  # Simple JIT this
def time_to_ground(theta_slope, slope_length, v_slope_0, dt=1e-6):
    x_slope = 0
    v_slope = v_slope_0
    accel = 9.81 * np.cos(theta_slope)  # Inline this and remove from loop (invariant)
    # Wouldn't have to inline but simplifies typing issue

    time = 0
    while x_slope < slope_length:
        v_slope = v_slope + accel * dt
        x_slope = x_slope + v_slope * dt
        time += dt

    return time


def print_statistics(slope_length, slope_angles, times):
    for i in range(len(times)):
        print(
            f"Time for mass to travel down slop of length {slope_length}m and incline {slope_angles[i]} rad: "  # Remove call to estimate_pi()
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
    print("in the near future")
    print("We hope you'll recommend Simutron 5000 to your friends!")


def main():
    print_greeting()  # Remove sleep function

    PI = estimate_pi()  # Calculate only once!

    slope_length = 10
    slope_fracs_to_test = [1 / 6, 1 / 3, 1 / 2]

    times = []
    slope_angles = []
    for slope_angle_pi_frac in slope_fracs_to_test:
        slope_angle = PI * slope_angle_pi_frac  # Reuse PI value calculated
        slope_angles.append(slope_angle)  # Store for reuse in print_statistics()

        print(f"Calculating for slope angle = {slope_angle}rad...")

        time = time_to_ground(
            theta_slope=slope_angle,
            slope_length=slope_length,
            v_slope_0=0,
        )
        times.append(time)

    print("Calculations finished!")

    print_statistics(slope_length, slope_angles, times)

    print_closing()  # Remove sleep function

    return times
