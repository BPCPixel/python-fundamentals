# This code simulates a Hotel Reservation to practice control statements
print(f'{"=" * 20} Hotel Reservations {"=" * 20}\n')

# CONSTANTS
ROOM_WITHOUT_SEA_VIEW = 150.50
ROOM_SEA_VIEW = 190.50

# User input
print(f'{"-" * 15} Data Client {"-" * 15}')
name_client = input('Type your name: ').strip().title()
days_of_stay = int(input('Insert days of stay: '))
sea_view = input('Would you like a room with sea view (yes/no)? ').strip().upper()

# Total cost of the stay
total_cost_stay = (days_of_stay * ROOM_SEA_VIEW) if sea_view == 'YES' else (days_of_stay * ROOM_WITHOUT_SEA_VIEW)

# Output
print(f'\n{"-" * 15} Reservation Details {"-" * 15}')
print(f'Client: {name_client}')
print(f'Days of stay: {days_of_stay}')
print(f'Total cost: ${total_cost_stay:.2f}')
print(f'Room with sea view: {sea_view.title()}')

print(f'\n{"=" * 60}')