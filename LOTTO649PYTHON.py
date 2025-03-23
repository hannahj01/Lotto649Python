import random

def generate_ticket():
    return set(random.sample(range(1, 50), 6))

# Generate the winning ticket
winning_numbers = generate_ticket()
print("Winning Numbers:", sorted(winning_numbers))

ticket_count = 0

while True:
    player_numbers = generate_ticket()
    ticket_count += 1

    if player_numbers == winning_numbers:
        print("\nJackpot! You won!")
        print("Abel sucks!")
        print("Player's Winning Ticket:", sorted(player_numbers))
        print(f"Tickets Needed to Win: {ticket_count}")
        break
