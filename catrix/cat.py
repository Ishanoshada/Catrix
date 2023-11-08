import time, random, sys
from .chatdata import chat_options, reply_options  # Importing chat data from a module

# Function for simulating slow typing effect
def slow_type(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Class definition for a Cat
class Cat:
    # Constructor method to initialize a Cat object
    def __init__(self, name, color, personality, size, weight, height, position, gender, log=False, chat_log=True):
        # Initializing attributes
        self.name = name
        self.color = color
        self.personality = personality
        self.size = size
        self.weight = weight
        self.height = height
        self.position = position
        self.gender = gender
        self.activity_level = "active"
        self.emotional_state = "neutral"
        self.energy = 100
        self.vitality = 100
        self.health = 100
        self.bonded_to = None
        self.environment = None
        self.log = log
        self.chat_log = chat_log

    # Method for logging messages
    def log_message(self, message):
        if self.log:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"\033[91m[LOG][{current_time}][{self.name}] :> {message}\033[0m")

    # Method for forming a bond with another cat
    def form_bond(self, other_cat):
        self.bonded_to = other_cat
        other_cat.bonded_to = self
        self.log_message(f"{self.name} forms a bond with {other_cat.name}.")
        if self.chat_log:
            self.log_message(f"{self.name} and {other_cat.name} start chatting.")

    # Method for initiating a chat with another cat
    def chat(self, other_cat):
        if self.bonded_to == other_cat:
            # Choosing a random chat type and message
            chat_type = random.choice(list(chat_options.keys()))
            chat_message = random.choice(chat_options[chat_type])
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if self.chat_log:
                print(f"\033[92m[CHAT][{current_time}][{self.name}] :> ", end=""); slow_type(f"{chat_message}\033[0m")
            other_cat.respond_to_chat(chat_type)

    # Method for responding to a chat initiated by another cat
    def respond_to_chat(self, chat_type):
        reply_message = random.choice(reply_options[chat_type])
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if self.chat_log:
            print(f"\033[92m[CHAT][{current_time}][{self.name}] :> ", end=""); slow_type(f" {reply_message}\033[0m")

    # Methods for various actions and behaviors of the cat
    # (meditate, practice_contentment, seek_guidance, offer_gratitude, embrace_oneness, transcend_boundaries, hunt, sleep, explore, interact_with_environment, groom, handle_other_species, perform_actions_in_harmony)
    # These methods simulate the cat's interactions with its environment and other species.
    def meditate(self):
        if random.randint(1, 100) <= 10:  # 10% chance of meditating
            self.log_message(f"{self.name} enters a state of deep contemplation.")
            self.emotional_state = "tranquility"
            self.energy += random.randint(5, 10)
            self.vitality += random.randint(5, 10)

    def practice_contentment(self):
        if random.randint(1, 100) <= 15:  # 15% chance of practicing contentment
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} finds contentment in the present moment.\033[0m")
            self.emotional_state = "contentment"
            self.energy += random.randint(5, 10)

    def seek_guidance(self):
        if random.randint(1, 100) <= 8:  # 8% chance of seeking guidance
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} seeks inner guidance and reflection.\033[0m")
            self.emotional_state = "reflection"
            self.vitality += random.randint(5, 10)
            self.health += random.randint(1, 5)

    def offer_gratitude(self):
        if random.randint(1, 100) <= 12:  # 12% chance of offering gratitude
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} expresses gratitude for the simulation.\033[0m")
            self.emotional_state = "gratitude"
            self.vitality += random.randint(5, 10)

    def embrace_oneness(self):
        if random.randint(1, 100) <= 10:  # 10% chance of embracing oneness
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} experiences a profound sense of oneness with the simulation.\033[0m")
            self.emotional_state = "oneness"
            self.energy += random.randint(5, 10)
            self.vitality += random.randint(5, 10)

    def transcend_boundaries(self):
        if random.randint(1, 100) <= 8:  # 8% chance of transcending boundaries
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} transcends the boundaries of the simulated reality.\033[0m")
            self.emotional_state = "transcendence"
            self.energy += random.randint(5, 10)
            self.vitality += random.randint(5, 10)
            self.health += random.randint(1, 5)

    def hunt(self):
        prey_types = list(self.environment.prey.keys())
        if len(prey_types) > 0:
            prey_type = random.choice(prey_types)
            if self.environment.prey[prey_type] > 0:
                self.environment.remove_prey(prey_type)
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} successfully hunted a {prey_type}.\033[0m")
                self.energy += random.randint(10, 20)
                self.vitality += random.randint(5, 10)
                self.health += random.randint(5, 10)
            else:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} couldn't find any {prey_type} to hunt.\033[0m")
        else:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} couldn't find any prey in the environment.\033[0m")

    def sleep(self):
        sleep_duration = random.randint(6, 10)  # Simulate 6-10 hours of sleep
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} sleeps for {sleep_duration} hours.\033[0m")
        self.energy += random.randint(20, 30) * (sleep_duration / 8)
        self.vitality += random.randint(5, 10) * (sleep_duration / 8)
        self.health += random.randint(5, 10) * (sleep_duration / 8)

    def explore(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} explores the environment.\033[0m")
        self.energy -= random.randint(10, 20)
        self.vitality += random.randint(5, 10)

    def interact_with_environment(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} interacts with the environment.\033[0m")
        self.energy -= random.randint(5, 10)
        self.vitality += random.randint(5, 10)

    def groom(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} grooms itself.\033[0m")
        self.energy -= random.randint(5, 10)
        self.vitality += random.randint(5, 10)
        self.health += random.randint(5, 10)
        
    def handle_other_species(self, species_type):
        if species_type == "birds":
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} is observing the group of birds.\033[0m")
            if random.randint(1, 100) <= 50:  # 50% chance of getting interested in birds
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} finds the birds fascinating!\033[0m")
                self.emotional_state = "interest"
        elif species_type == "mice":
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} is cautiously watching the mice.\033[0m")
            if random.randint(1, 100) <= 30:  # 30% chance of getting scared of mice
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} is scared of the mice!\033[0m")
                self.emotional_state = "fear"
        elif species_type == "squirrels":
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} is curious about the squirrels.\033[0m")
            if random.randint(1, 100) <= 40:  # 40% chance of getting curious about squirrels
                        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());self.log_message(f"\033[92m[{current_time}][{self.name}] :> {self.name} wants to explore the area with squirrels!\033[0m")
        self.emotional_state = "curiosity"
      
    def perform_actions_in_harmony(self):
        self.hunt()
        self.sleep()
        self.explore()
        self.interact_with_environment()
        self.groom()
        self.handle_other_species("birds")
        self.handle_other_species("mice")
        self.handle_other_species("squirrels")
        
                                                  

    # Method for creating a child with a partner
    def create_child(self, partner):
        if self.gender != partner.gender:  # Ensure different genders for reproduction
            child_name = random.choice(["Whiskers Jr.", "Mittens Jr.", "Fluffy", "Luna", "leo", "neo"])
            child_color = random.choice([self.color, partner.color])
            child_personality = random.choice([self.personality, partner.personality])
            child_size = random.choice([self.size, partner.size])
            child_weight = (self.weight + partner.weight) / 2
            child_height = (self.height + partner.height) / 2
            child_position = (self.position[0], self.position[1], 0)  # Assuming same position as parent
            child_gender = random.choice(["male", "female"])

            child = Cat(
                name=child_name,
                color=child_color,
                personality=child_personality,
                size=child_size,
                weight=child_weight,
                height=child_height,
                position=child_position,
                gender=child_gender
            )

            return child

        return None

    # Method for receiving Buddha's guidance and experiencing a spiritual transformation
    def receive_buddha_guidance(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{current_time}][{self.name}] :> {self.name} receives Buddha's guidance.")
        self.embrace_oneness()
        self.transcend_boundaries()
