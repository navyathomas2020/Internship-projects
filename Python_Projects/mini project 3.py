import random
agents = []

def add_agent(name):
    agent = {
        "name": name,
        "missions": []
    }
    agents.append(agent)
    print("Agent added successfully!")


def assign_mission(name, scores):
    for agent in agents:
        if agent["name"] == name:
            for score in scores:
                agent["missions"].append(score)
            print("Mission scores added!")
            return
    print("Agent not found!")

def view_agents():
    if not agents:
        print("No agents available.")
    for agent in agents:
        print(agent["name"], ":", agent["missions"])


def calculate_average(missions):
    if len(missions) == 0:
        return 0
    return sum(missions) / len(missions)


def top_agent():
    best = None
    highest = 0
    for agent in agents:
        avg = calculate_average(agent["missions"])
        if avg > highest:
            highest = avg
            best = agent
    if best:
        print("Top Agent:", best["name"], "with average", highest)
    else:
        print("No agents found.")

def assign_rank(avg):
    if avg >= 90:
        return "Elite Agent"
    elif avg >= 75:
        return "Senior Agent"
    elif avg >= 50:
        return "Junior Agent"
    else:
        return "Failed Agent"

def generate_report():
    if not agents:
        print("No data to show.")
        return

    print("\n--- Mission Report ---")
    for agent in agents:
        avg = calculate_average(agent["missions"])
        rank = assign_rank(avg)
        print("Name:", agent["name"])
        print("Scores:", agent["missions"])
        print("Average:", avg)
        print("Rank:", rank)
        print("--------------------")


def bonus_points(name):
    for agent in agents:
        if agent["name"] == name:
            bonus = random.randint(5, 15)
            agent["missions"].append(bonus)
            print("Bonus points added:", bonus)
            return
    print("Agent not found!")

def menu():
    while True:
        print("\n--- Spy Mission System ---")
        print("1. Add Agent")
        print("2. Assign Mission")
        print("3. View Agents")
        print("4. Show Top Agent")
        print("5. Generate Report")
        print("6. Add Bonus Points")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter agent name: ")
            add_agent(name=name)

        elif choice == "2":
            name = input("Enter agent name: ")
            scores = input("Enter scores separated by space: ").split()
            scores = [int(s) for s in scores]
            assign_mission(name, scores)

        elif choice == "3":
            view_agents()

        elif choice == "4":
            top_agent()

        elif choice == "5":
            generate_report()

        elif choice == "6":
            name = input("Enter agent name: ")
            bonus_points(name)

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")


menu()