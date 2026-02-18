"""
BOOT.DEV SKILL CHECK - SPACE STATION EDITION
--------------------------------------------
Topics: Loops, Logic, Accumulators, Math
Theme: You are the AI controlling a failing space station.
"""

# ==========================================
# PART 1: FOR LOOPS (The Fuel Calculator)
# ==========================================


def calculate_fuel_cost(distance, base_fuel):
    """
    GOAL: Calculate fuel needed for a trip.

    The further you go, the more fuel it costs per lightyear due to engine heat.
    - For the 1st lightyear, cost is 'base_fuel'.
    - For the 2nd lightyear, cost is 'base_fuel' + 1.
    - For the 3rd lightyear, cost is 'base_fuel' + 2.
    - And so on...

    Example: Distance 3, Base 10
    - Year 1: 10
    - Year 2: 11
    - Year 3: 12
    - Total: 33

    Task: Use a FOR loop to calculate the total.
    """
    # Write your code here
    total = 0
    for i in range(0, distance):
        total += base_fuel + i
        # print(total)
    return total


# ==========================================
# PART 2: WHILE LOOPS (The Airlock)
# ==========================================


def pressurize_airlock(current_pressure, target_pressure):
    """
    GOAL: Safely pressurize the airlock.

    Rules:
    1. Use a WHILE loop to increase 'current_pressure' by 10 until it meets OR exceeds 'target_pressure'.
    2. CRITICAL SAFETY: If the pressure goes OVER the target, the airlock explodes.
       You must check for this *inside* the loop.
    3. If adding 10 would go over, you must add only the remaining difference.

    Return the final pressure (which must equal target_pressure).
    """
    # Write your code here
    while current_pressure < target_pressure:
        if target_pressure - current_pressure < 10:
            current_pressure += target_pressure - current_pressure
        else:
            current_pressure += 10
    return current_pressure


print(pressurize_airlock(10, 10))  # debugging the result beofre test cases ran

# ==========================================
# PART 3: LOGIC & MATH (The Alien Signal)
# ==========================================


def decode_signal(signal_strength):
    """
    GOAL: Calculate the "Meaning Value" of a signal stream.

    We analyze every integer from 1 up to 'signal_strength'.

    Rules:
    - Loop from 1 to 'signal_strength' (inclusive).
    - If number is divisible by 3: It's "Static" -> Add 1 to total.
    - If number is divisible by 4: It's "Data" -> Add 5 to total.
    - If number is divisible by BOTH 3 and 4 (e.g., 12): It's "Interference" -> SUBTRACT 10 from total.
    - (Priority: 'Interference' rule overrides the others).

    Return the final total.
    """
    # Write your code here
    final_total = 0
    for i in range(1, signal_strength + 1):
        if i % 3 == 0 and i % 4 == 0:
            print("its interference")
            final_total -= 10
        elif i % 4 == 0:
            print("Its data")
            final_total += 5
        elif i % 3 == 0:
            print("its static")
            final_total += 1
    return final_total


# ==========================================
# PART 4: DEBUGGING (The Oxygen Leak)
# ==========================================


def monitor_oxygen(current_o2):
    """
    BUG ALERT!
    This function tracks oxygen loss.
    - O2 drops by 5 every minute.
    - When it hits 20 or lower, the emergency generator kicks in and adds 50 O2 ONCE.
    - The loop should stop when O2 reaches 0.

    The Bug: The generator adds 50 every single time it's low, creating an INFINITE LOOP.

    Task: Fix the logic so the generator only runs ONCE.
    (Hint: You might need a boolean flag variable like 'generator_used = False')
    """

    minutes_survived = 0
    generator_used = False  # <--- Hint hint

    # --- BUGGY CODE STARTS HERE ---
    while current_o2 > 0:
        current_o2 = current_o2 - 5
        minutes_survived = minutes_survived + 1

        if current_o2 <= 20 and not generator_used:
            current_o2 += 50
            generator_used = True

    # --- BUGGY CODE ENDS HERE ---

    return minutes_survived


# ==========================================
# PART 5: TESTS
# ==========================================


def run_tests():
    print("--- Running Space Station Tests ---")

    # Test 1: Fuel
    # Dist 3, Base 10 -> 10 + 11 + 12 = 33
    if calculate_fuel_cost(3, 10) == 33:
        print("Test 1 (Fuel): PASS")
    else:
        print(f"Test 1 (Fuel): FAIL - Expected 33, Got {calculate_fuel_cost(3, 10)}")

    # Test 2: Airlock
    # Start 0, Target 25. Steps: 10, 20, then needs 5 (not 10!) -> 25
    if pressurize_airlock(0, 25) == 25:
        print("Test 2 (Airlock): PASS")
    else:
        print(f"Test 2 (Airlock): FAIL - Got {pressurize_airlock(0, 25)}")

    # Test 3: Signal Decoding
    # Range 1 to 12.
    # 3 (Static +1), 4 (Data +5), 6 (Static +1), 8 (Data +5), 9 (Static +1), 12 (Interference -10)
    # Total = 1 + 5 + 1 + 5 + 1 - 10 = 3
    if decode_signal(12) == 3:
        print("Test 3 (Signal): PASS")
    else:
        print(f"Test 3 (Signal): FAIL - Expected 3, Got {decode_signal(12)}")

    # Test 4: Oxygen (Infinite Loop Fix)
    # Start 40.
    # 40->35->30->25->20 (Gen kicks in! +50) -> 70.
    # Then drains 70...65... until 0. Total minutes should be roughly 18.
    try:
        result = monitor_oxygen(40)
        if result == 18:
            print("Test 4 (Oxygen): PASS")
        else:
            print(f"Test 4 (Oxygen): FAIL - Expected 18, Got {result}")
    except KeyboardInterrupt:
        print("Test 4 (Oxygen): FAIL - Infinite Loop!")


if __name__ == "__main__":
    run_tests()
