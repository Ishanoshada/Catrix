# Importing necessary libraries
import random, os, pyfiglet, sys, time

# Importing the Buddha class from the .buddha module
from .buddha import Buddha

# List of available fonts for the pyfiglet module
FONTS = (
    "basic",
    "o8",
    "cosmic",
    "graffiti",
    "chunky",
    "epic",
    "poison",
    "doom",
    "avatar",
    "3-d",
    "alligator2",
    "banner3-D",
    "block",
    "bubble",
    "digital",
    "doh",
    "doom",
    "epic",
    "fuzzy",
    "isometric1",
    "letters",
    "nancyj-fancy",
    "ogre",
    "poison",
    "roman",
    "shadow",
    "starwars",
    "stop",
    "univers",
    "usaflag",
)



# List of ANSI escape codes for different colors
bcolors = [
    '\033[95m', '\033[94m', '\033[96m', '\033[92m',
    '\033[93m', '\033[91m', '\033[1;33m', '\033[1;31m'
]

# Function to display a stylized logo
def logo():
    # Randomly select a font and two colors for the logo
    font = random.choice(FONTS)
    color1 = random.choice(bcolors)
    color2 = random.choice(bcolors)
    while color1 == color2:
        color2 = random.choice(bcolors)
    
    # Print decorative lines, the logo, and version information
    print(color1 + "•" * os.get_terminal_size().columns, end="\n" * 2)
    print(
        color2
        + pyfiglet.figlet_format(
            "The  Catrix",
            width=os.get_terminal_size().columns,
            justify="center",
            font=font,
        ),
        end="",
    )
    print("\t\t\t\t\t\t V1.0.0 \n")

    print(color1 + "•" * os.get_terminal_size().columns, end="\n" * 2)


# Definition of the Environment class
class Environment:
    def __init__(self, size, log=False, chat_log=False, buddha=False):
        # Initialize environment parameters
        self.size = size
        self.cats = []
        self.prey = {"mouse": 5, "bird": 3, "squirrel": 2}
        self.age = 0
        self.log = log
        self.chat_log = chat_log
        self.buddha = buddha

    # Method for logging messages with a timestamp
    def log_message(self, message):
        if self.log:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"\033[91m[LOG][{current_time}][#] :> {message}\033[0m")

    # Method to add a cat to the environment
    def add_cat(self, cat):
        self.cats.append(cat)
        cat.environment = self

    # Method to remove prey from the environment
    def remove_prey(self, prey_type):
        if prey_type in self.prey:
            self.prey[prey_type] -= 1

    # Method to progress to the next simulation age
    def progress_to_next_age(self):
        self.age += 1
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"[{current_time}][#] :> The simulation has entered a new age: {self.age}")

    # Method to create conversations between cats
    def create_conversations(self):
        for cat1 in self.cats:
            for cat2 in self.cats:
                if cat1 != cat2:
                    cat1.chat(cat2)

    # Method to simulate random natural events
    def simulate_natural_events(self):
        natural_event_chance = random.randint(1, 100)
        if natural_event_chance <= 65:
            # List of random event messages
            random_event_messages = [
                "A gentle breeze rustles through the environment.",
                "The distant sound of water flowing soothes the surroundings.",
                "The leaves on the trees sway gracefully in the virtual wind.",
                "A ray of light pierces through the virtual canopy, casting a warm glow on the ground.",
                "The scent of virtual flowers fills the air, creating a serene atmosphere."
            ]
            random_event_message = random.choice(random_event_messages)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"[{current_time}][#] :> {random_event_message}")
            self.handle_random_event()

    # Method to handle a random natural event
    def handle_random_event(self):
        for cat in self.cats:
            if random.randint(1, 100) <= 50:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cat.meditate()
                cat.practice_contentment()
                cat.seek_guidance()
                cat.offer_gratitude()

    # (Other methods...)
    def simulate_cosmic_influence(self):
        time.sleep(1)
        cosmic_influence_chance = random.randint(1,100)
        if cosmic_influence_chance <= 5:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"[{current_time}][#] :> A profound cosmic influence emanates throughout the simulation.")
            time.sleep(0.2)
            if self.buddha == True:
                buddha = Buddha()
                buddha.enter_simulation(self)
                  # This signals that the simulation should end

            #self.handle_cosmic_influence()
            
    def handle_cosmic_influence(self):
        for cat in self.cats:
            if random.randint(1, 100) <= 20:  # 20% chance of being deeply affected by the influence
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cat.practice_contentment()
                cat.seek_guidance()
                cat.offer_gratitude()
                cat.embrace_oneness()
                cat.transcend_boundaries()

    def introduce_other_species(self):
        species_types = list(self.prey.keys())
        species_type = random.choice(species_types)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"[{current_time}][#] :> A group of {species_type}s has appeared!")
        for cat in self.cats:
            cat.handle_other_species(species_type)

    def update_time_of_day(self):
        time_of_day = random.choice(["day", "night"])
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"[{current_time}][#] :> It's now {time_of_day} in the simulation.")
        for cat in self.cats:
            if time_of_day == "day":
                cat.activity_level = "active"
            else:
                cat.activity_level = "resting"
     
    def end_simulation(self):
        print("\n[Simulation End]")
        print("The Catrix dissolves, merging with the boundless cosmos,")
        print("as each soul embarks on a journey towards ultimate liberation.")
        print("Nirvana awaits those who have chosen the path of enlightenment.")
        print("\t\t\t\t\t\t\t\t\t\t V1.0.0\n")
        exit()

    # Method to run the simulation for a specified number of steps
    def run_simulation(self, steps):
        logo()  # Display the logo
        for _ in range(steps):
            # Perform various simulation steps
            self.simulate_natural_events()
            self.introduce_other_species()
            self.update_time_of_day()
            self.create_conversations()
            self.simulate_cosmic_influence()
            self.create_conversations()

            # Attempt reproduction
            for cat in self.cats:
                if random.randint(1, 100) <= 60:
                    partner = random.choice(self.cats)
                    partner2 = random.choice(self.cats)
                    while True:
                        child = cat.create_child(partner)
                        if child:
                            pass
                        child2 = cat.create_child(partner2)
                        if child2:
                            break
                        if child is not None:
                            self.add_cat(child)
                            self.add_cat(child2)
                            child.form_bond(child2)

            if self.age % 5 == 0:
                self.progress_to_next_age()

  