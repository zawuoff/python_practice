"""
BOOT.DEV SKILL CHECK - MODULES 1-8 (LOOPS EDITION)
--------------------------------------------------
Topics Covered:
- Variables, Functions, Scope, Logic
- NEW: For Loops (using range)
- NEW: While Loops
- NEW: Accumulator Pattern (Running totals)

INSTRUCTIONS:
Replace 'pass' with your code.
Do NOT use Lists (we haven't learned them yet).
"""

# ==========================================
# PART 1: FOR LOOPS (The Basics)
# ==========================================


def calculate_total_xp(battles_fought, xp_per_battle):
    """
    The player has fought a certain number of battles.
    Each battle gives a fixed amount of XP.

    1. Create a variable 'total_xp' starting at 0.
    2. Use a FOR loop that runs 'battles_fought' times.
    3. Inside the loop, add 'xp_per_battle' to 'total_xp'.
    4. Return the final total_xp.
    """
    # Write your code here
    total_xp = 0
    for i in range(0, battles_fought):
        total_xp += xp_per_battle
    return total_xp


def count_countdown_timer(start_number):
    """
    We need a countdown for a spell cast.

    1. Use a loop (for or while) to print numbers from 'start_number' down to 1.
    2. AFTER the loop finishes, return the string "Cast!"

    Example: If start_number is 3, it should print 3, 2, 1, then return "Cast!"
    """
    # Write your code here
    for i in range(start_number, 0, 1):
        print(i)
    return "Cast!"


# ==========================================
# PART 2: WHILE LOOPS (Logic)
# ==========================================


def regenerate_mana(current_mana, max_mana, regen_rate):
    """
    A potion regenerates mana over time.

    1. Use a WHILE loop.
    2. The loop should run as long as 'current_mana' is LESS than 'max_mana'.
    3. Inside the loop:
       - Add 'regen_rate' to 'current_mana'.
       - Print "Regenerating..." (optional, but helps debug)
    4. Be careful! If adding mana goes OVER max_mana, set it equal to max_mana.
       (You might need an 'if' check inside or after the loop).
    5. Return the final 'current_mana'.
    """
    # Write your code here
    while current_mana < max_mana:
        current_mana += regen_rate
        print("Regenerating...")
    if current_mana > max_mana:
        current_mana = max_mana
    return current_mana


# ==========================================
# PART 3: ADVANCED LOOPS (The "FizzBuzz" Test)
# ==========================================


def calculate_critical_hits(total_attacks):
    """
    In this game, every 3rd attack is a CRITICAL HIT (double damage).
    Every 5th attack is a MISS (zero damage).
    Normal attacks do 10 damage.

    Calculate the total damage after 'total_attacks'.

    Rules:
    - Loop from 1 to total_attacks (inclusive).
    - If the attack number is divisible by 3, add 20 damage.
    - If the attack number is divisible by 5, add 0 damage.
    - Otherwise, add 10 damage.
    - Important: If a number is divisible by both 3 and 5 (like 15),
      treat it as a MISS (priority to the miss).

    Return the total damage.
    """
    # Write your code here
    total_damage = 0
    normal_dmg = 10
    critical_dmg = normal_dmg * 2
    miss = 0

    for i in range(1, total_attacks + 1):
        if i % 3 == 0:
            total_damage += critical_dmg
        elif i % 5 == 0:
            total_damage += miss
        elif (i % 3 == 0) and (i % 5 == 0):
            total_damage += miss
        else:
            total_damage += normal_dmg
    return total_damage


# ==========================================
# PART 4: DEBUGGING (Find the Infinite Loop)
# ==========================================


def climb_tower(floors_to_climb):
    """
    BUG ALERT! This function is supposed to count how many steps it takes
    to climb the tower.

    1. There is a bug that causes an INFINITE LOOP.
    2. There is a logic bug where it returns the wrong value.

    Fix the loop and ensure it returns the correct number of steps.
    (Assume 1 floor = 10 steps).
    """
    steps_taken = 0
    current_floor = 0

    # --- BUGGY CODE STARTS HERE ---
    while current_floor < floors_to_climb:
        current_floor += 1
        steps_taken += 10
        # Hint: Is current_floor ever changing?
    # --- BUGGY CODE ENDS HERE ---

    return steps_taken


# ==========================================
# PART 5: YOUR TESTS
# ==========================================


def run_tests():
    print("--- Running Tests ---")

    # Test 1: Total XP
    if calculate_total_xp(5, 100) == 500:
        print("Test 1 (XP Loop): PASS")
    else:
        print("Test 1 (XP Loop): FAIL")

    # Test 2: Countdown
    if count_countdown_timer(3) == "Cast!":
        print("Test 2 (Countdown): PASS")
    else:
        print(
            f"Test 2 (Countdown): FAIL - Expected 'Cast!', got {count_countdown_timer(3)}"
        )

    # Test 3: Mana Regen
    if regenerate_mana(50, 100, 20) == 100:
        print("Test 3 (Mana Normal): PASS")
    elif regenerate_mana(99, 100, 5) == 100:
        print("Test 3 (Mana Cap): PASS")
    else:
        print("Test 3 (Mana): FAIL")

    # Test 4: Critical Hits
    # 1(10) + 2(10) + 3(20) + 4(10) + 5(0) = 50
    dmg = calculate_critical_hits(5)
    if dmg == 50:
        print("Test 4 (Crit Logic): PASS")
    else:
        print(f"Test 4 (Crit Logic): FAIL - Expected 50, got {dmg}")

    # Test 5: Infinite Loop Fix
    if climb_tower(3) == 30:
        print("Test 5 (Tower Fix): PASS")
    else:
        print("Test 5 (Tower Fix): FAIL")


if __name__ == "__main__":
    run_tests()
