# STATS CALCULATOR
stats = input("Enter 'BATSMEN' or 'BOWLER': ").strip().upper()

# BATSMEN SECTION
if stats == "BATSMEN":
    print("\n--- BATSMEN STATS ---")

    # Average Calculator
    no_of_innings = int(input("Enter the number of innings played: "))
    runs_scored = list(map(int, input("Enter runs scored in each innings (space-separated): ").split()))
    not_outs = int(input("Enter the number of not outs: "))

    if len(runs_scored) != no_of_innings:
        print("Error: Number of scores doesn't match number of innings.")
    elif not_outs > no_of_innings:
        print("Error: Not outs can't be more than innings.")
    elif no_of_innings == 0:
        print("Average: NA (No innings played)")
    elif no_of_innings - not_outs == 0:
        print("Average: NA (Never got out)")
    else:
        average = round(sum(runs_scored) / (no_of_innings - not_outs), 2)
        print("Batting Average:", average)

    # Strike Rate Calculator
    runs_total = int(input("\nEnter total runs scored: "))
    balls_faced = int(input("Enter total balls faced: "))

    if balls_faced == 0:
        print("Strike Rate: NA (No balls faced)")
    else:
        strike_rate = round((runs_total / balls_faced) * 100, 2)
        print("Strike Rate:", strike_rate)

# BOWLER SECTION
elif stats == "BOWLER":
    print("\n--- BOWLER STATS ---")

    balls_bowled = int(input("Enter number of balls bowled: "))
    runs_conceded = int(input("Enter runs conceded: "))
    wickets_taken = int(input("Enter number of wickets taken: "))

    if balls_bowled < 0 or runs_conceded < 0 or wickets_taken < 0:
        print("Error: Negative values are not allowed.")
    elif balls_bowled == 0 or wickets_taken == 0:
        print("Average: NA")
        print("Strike Rate: NA")
    else:
        average = round(runs_conceded / wickets_taken, 2)
        strike_rate = round(balls_bowled / wickets_taken, 2)
        print("Bowling Average:", average)
        print("Bowling Strike Rate:", strike_rate)

# INVALID ENTRY
else:
    print("Invalid input. Please enter either 'BATSMEN' or 'BOWLER'.")
