# This code simulates a health and fitness tracking system

# Constants
DAILY_STEPS_GOAL = 10000
CALORIES_PER_STEP = 0.04

print(f'{"=" * 20} Health and Fitness App {"=" * 20}\n')

# User input
name = input('Type your name: ').strip().title()
steps = int(input("Today's steps: "))

# Calculations
burned_calories = steps * CALORIES_PER_STEP
goal_achieved = steps >= DAILY_STEPS_GOAL

# Output
if goal_achieved:
    print(f'''Hello, {name}
Congratulations, you achieved your daily goal!
Steps: {steps} / {DAILY_STEPS_GOAL}

You burned {burned_calories:.2f} calories today.

Nice work!
''')
else:
    print(f'''Hello, {name}
You didn't reach your daily goal.
You were {DAILY_STEPS_GOAL - steps} steps away.

You burned {burned_calories:.2f} calories today.

Try again tomorrow, you can do it!
''')

print(f'\n{"=" * 50}')
