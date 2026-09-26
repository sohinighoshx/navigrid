import math


def route_cost(distance, slope, slope_weight=8.0):
    return distance + slope_weight * slope


def select_route():
    # Candidate routes based on the NaviGrid arena.
    flat_distance = 24.0
    flat_slope = 0.0

    ramp_distance = 17.0
    ramp_slope = 0.20

    flat_cost = route_cost(flat_distance, flat_slope)
    ramp_cost = route_cost(ramp_distance, ramp_slope)

    if ramp_cost < flat_cost:
        selected = "RAMP_A_TO_B"
    else:
        selected = "FLAT_ZIGZAG"

    return {
        "flat_cost": flat_cost,
        "ramp_cost": ramp_cost,
        "selected": selected,
    }


if __name__ == "__main__":
    result = select_route()

    print("NaviGrid Adaptive Route Selection")
    print(f"Flat route cost : {result['flat_cost']:.2f}")
    print(f"Ramp route cost : {result['ramp_cost']:.2f}")
    print(f"Selected route  : {result['selected']}")
