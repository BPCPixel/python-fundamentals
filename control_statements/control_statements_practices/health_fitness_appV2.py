# Health and Fitness Tracking System - Version 2

# Constants
DAILY_STEPS_GOAL = 10000
CALORIES_PER_STEP = 0.04

print(f'{"=" * 20} Health and Fitness App V2 {"=" * 20}\n')

name = input('Type your name: ').strip().title()
steps = int(input("Today's steps: "))

# Calculations
burned_calories = steps * CALORIES_PER_STEP
goal_achieved = steps >= DAILY_STEPS_GOAL
goal_achieved_txt = 'Yes' if goal_achieved else 'No'

# Output
print(f'''
User: {name}
Today's steps: {steps}
Burned calories: {burned_calories:.2f} kcal
Daily steps goal achieved: {goal_achieved_txt}
Daily steps goal: {DAILY_STEPS_GOAL}
''')

print(f'{"=" * 50}')

