"""
BOOT.DEV SKILL CHECK - MODULES 1-7
----------------------------------
Topics Covered:
1. Introduction
2. Variables
3. Functions
4. Scope
5. Testing and Debugging
6. Computing
7. Comparisons

INSTRUCTIONS:
Replace the 'pass' statements with your own code.
Do not change the function names, as I will use them to test your code later.
"""

# ==========================================
# PART 1: VARIABLES & COMPUTING
# ==========================================


def calculate_character_stats(base_strength, base_intelligence, level):
    """
    You are building an RPG character sheet.

    1. Calculate 'total_strength': It should be base_strength + (level * 2).
    2. Calculate 'total_intelligence': It should be base_intelligence + (level * 1.5).
    3. Calculate 'mana': It should be total_intelligence * 10.

    Return total_strength, total_intelligence, and mana (in that order).

    IMPORTANT: 'mana' should be an integer (remove any decimals),
    even if the calculation results in a float.
    """
    # Write your code here
    total_strength = base_strength + (level * 2)
    total_intelligence = base_intelligence + (level * 1.5)
    mana = total_intelligence * 10
    return total_strength, total_intelligence, mana


# ==========================================
# PART 2: FUNCTIONS & SCOPE
# ==========================================

# GLOBAL VARIABLE
xp_multiplier = 1.5


def calculate_xp_gain(base_xp, bonus_event_active):
    """
    Calculate the total XP gained from a quest.

    1. If 'bonus_event_active' is True, use the global 'xp_multiplier'.
    2. If 'bonus_event_active' is False, ignore the multiplier (treat it as 1.0).
    3. The formula is: base_xp * (multiplier used).
    4. Return the final calculated XP.
    """
    # Write your code here
    if bonus_event_active:
        base_xp *= xp_multiplier
        return base_xp
    return base_xp * 1


def update_multiplier(new_val):
    """
    Update the global 'xp_multiplier' variable to 'new_val'.

    Hint: You need to tell Python you are writing to the global variable,
    not creating a new local one.
    """
    # Write your code here
    global xp_multiplier
    xp_multiplier = new_val
    return xp_multiplier


# ==========================================
# PART 3: COMPARISONS & LOGIC
# ==========================================


def can_enter_dungeon(level, has_key, is_banned):
    """
    Determine if a player can enter a dungeon.

    Rules:
    1. Player level must be at least 10.
    2. Player must have the key (has_key must be True).
    3. Player must NOT be banned (is_banned must be False).

    Return True if they can enter, False otherwise.

    Constraint: Try to do this in a single return statement using
    logical operators (and, or, not, >, <, etc).
    """
    # Write your code here
    return (level >= 10) and (has_key == True) and (is_banned == False)


def compare_equipment(item1_power, item2_power):
    """
    Compare two items based on their power level.

    Return a string based on the comparison:
    - If item1 is stronger, return "Item 1 is better"
    - If item2 is stronger, return "Item 2 is better"
    - If they are equal, return "Items are equal"
    """
    # Write your code here
    if item1_power > item2_power:
        return "Item 1 is better"
    elif item2_power > item1_power:
        return "Item 2 is better"
    else:
        return "Items are equal"


# ==========================================
# PART 4: TESTING & DEBUGGING (The tricky part!)
# ==========================================


def damage_calculator(base_damage, weapon_bonus, is_critical):
    """
    There is a SYNTAX BUG in this function!
    It is supposed to calculate damage:
    - Add base_damage and weapon_bonus.
    - If is_critical is True, multiply the result by 2.

    Find the bug, fix it, and ensure the function returns the total.
    """

    # --- BUGGY CODE STARTS HERE ---
    total = base_damage + weapon_bonus
    if is_critical == True:  # <--- Hint: Look closely at this line
        total = total * 2
    # --- BUGGY CODE ENDS HERE ---

    return total


# ==========================================
# PART 5: YOUR OWN TESTS
# ==========================================


def run_tests():
    """
    Write code here to test your own functions.
    Print "PASS" if the function works as expected, and "FAIL" if it doesn't.
    I have done the first one for you.
    """
    print("--- Running Tests ---")

    # Test 1: Character Stats
    str_stat, int_stat, mana = calculate_character_stats(10, 10, 5)
    # Math: Str=10+(5*2)=20, Int=10+(5*1.5)=17.5, Mana=17.5*10=175
    if str_stat == 20 and int_stat == 17.5 and mana == 175:
        print("Test 1 (Stats): PASS")
    else:
        print(f"Test 1 (Stats): FAIL - Got {str_stat}, {int_stat}, {mana}")

    # Test 2: XP Gain
    # TODO: Write a test case for calculate_xp_gain where bonus is True
    # If base is 100 and multiplier is 1.5 (default), result should be 150.
    test_var = calculate_xp_gain(100, True)
    if test_var == 150:
        print("PASS")
    else:
        print("FAIL")

    # Test 3: Dungeon Entry
    # TODO: Write a test case for can_enter_dungeon where they have
    # the level and key, but ARE banned. (Should return False)
    test_var_2 = can_enter_dungeon(11, True, True)

    if test_var_2 == False:
        print("PASS")
    else:
        print("FAIL")

    # Test 4: Damage Calculator Fix
    # TODO: Write a test to ensure your fix for damage_calculator works
    # Try base 10, bonus 5, critical True. Result should be 30.
    test_var_3 = damage_calculator(10, 5, True)
    if test_var_3 == 30:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    run_tests()
