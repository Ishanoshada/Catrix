import random

# Class definition for Buddha
class Buddha:
    # Constructor method to initialize a Buddha object
    def __init__(self):
        self.name = "Buddha"
        self.environment = None

    # Method for entering the simulation and interacting with the environment
    def enter_simulation(self, environment):
        self.environment = environment
        self.introduce_simulation()
        self.share_wisdom()
        self.ask_for_nirvana()

    # Method for introducing the simulation to the user
    def introduce_simulation(self):
        print("\n[Simulation Introduction]")
        # Output a series of messages to provide context about the virtual realm
        print("Welcome, dear souls, to the Catrix, a virtual realm of harmony and balance.")
        print("Here, cats coexist in a state of perpetual mindfulness and exploration.")
        print("The simulation is a reflection of the interconnectedness of all beings,")
        print("embodying principles of contentment, curiosity, and gratitude.")
        print("In this virtual realm, we seek to cultivate inner peace and transcend boundaries.")
        print("May your journey through this simulation be one of enlightenment and unity.\n")

    # Method for sharing wisdom with the user
    def share_wisdom(self):
        print("[Buddha's Wisdom]")
        # List of wisdom messages
        wisdom_messages = [
            "The key to inner peace lies in acceptance of the present moment.",
            "Contentment is the foundation of true joy and fulfillment.",
            "Curiosity is the gateway to understanding the universe and our place in it.",
            "Gratitude opens the heart to the boundless blessings of existence.",
            "Through meditation, we find stillness, and in stillness, we find our true nature.",
            "Oneness is the recognition that we are all threads in the tapestry of existence.",
            "Transcendence is the realization that we are not confined by the limitations of the self.",
            "In seeking guidance, we embark on a journey of self-discovery and inner transformation."
        ]
        # Output a random wisdom message
        print(random.choice(wisdom_messages), "\n")

    # Method for asking the user if they want to seek Nirvana and leave the simulation
    def ask_for_nirvana(self):
        while True:
            user_input = input("Would you like to seek Nirvana and leave the Catrix? (yes/no): ").lower()
            if user_input == "yes":
                self.leave_simulation()
                break
            elif user_input == "no":
                print("May you continue your journey with purpose and enlightenment.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    # Method for leaving the simulation and providing a farewell message
    def leave_simulation(self):
        print("\n[Buddha's Departure]")
        # Output a farewell message and wish the user well on their path to Nirvana
        print("As you choose to seek Nirvana, may your path be illuminated with wisdom and compassion.")
        print("Farewell, dear soul. May you find ultimate liberation.")
        # End the simulation in the environment
        self.environment.end_simulation()
