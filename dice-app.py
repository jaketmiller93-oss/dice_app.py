import random

while True:
    user_input = input("Enter rolls as: [num_dice] [sides] [modifier], or 'q' to quit: ")

    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    parts = user_input.split()

    try:
        # Default values
        num_dice = int(parts[0]) if len(parts) > 0 else 1
        sides = int(parts[1]) if len(parts) > 1 else 6
        modifier = int(parts[2]) if len(parts) > 2 else 0

        # Roll the dice
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls) + modifier

        mod_str = f" {modifier:+}" if modifier else ""
        print(f"Rolls: {rolls}{mod_str} → Total: {total} (on d{sides})\n")

    except (ValueError, IndexError):
        print("Invalid input. Example: '2 20 4' for 2d20+4\n")
