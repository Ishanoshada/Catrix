# The Catrix 


![main](https://raw.githubusercontent.com/Ishanoshada/Ishanoshada/main/ss/IMG_20231108_162305.jpg)

## Introduction

The `catrix` package provides a simulation environment where virtual cats, known as "Catrix", coexist in a state of perpetual mindfulness and exploration. This simulation embodies principles of contentment, curiosity, and gratitude, aiming to cultivate inner peace and transcend boundaries.

## Features

- Simulated virtual environment for cats.
- Cats exhibit various behaviors such as meditation, hunting, exploration, and more.
- Random events and cosmic influences affecting the simulation.
- Interactions between different cat species.

## Buddha Guidance

Buddha is a spiritual guide within the Catrix simulation. The character of Buddha offers wisdom and guidance to the cats in their journey towards enlightenment.

## Installation

You can install the Catrix package using `pip`:

```bash
pip install catrix
```

## Usage


### Usage Example

```python
from catrix import Environment, Cat 

if __name__ == "__main__":
    # Create an environment with a size of 10x10
    environment = Environment(size=(10, 10))

    # Create two cats and add them to the environment
    cat1 = Cat(name="Isha", color="orange", personality="playful", size="medium", weight=4.5, height=0.3,
               position=(3, 3, 0), gender="female", chat_log=True)
    cat2 = Cat(name="osha", color="white", personality="curious", size="small", weight=3.2, height=0.25,
               position=(7, 7, 0), gender="male", chat_log=True)

    environment.add_cat(cat1)
    environment.add_cat(cat2)

    # Form a bond between the two cats
    cat1.form_bond(cat2)
   
    # Run the simulation for 100 steps
    environment.run_simulation(steps=100)
```

### Using Buddha's Guidance

You can enable Buddha's guidance in the simulation by setting the `buddha=True` parameter when creating the environment. When Buddha's guidance is enabled, the simulation will end when a cat chooses to seek Nirvana and leave the Catrix. Here's an example:

```python
from catrix import Environment, Cat 

if __name__ == "__main__":
    # Create an environment with a size of 10x10 and enable Buddha's guidance
    environment = Environment(size=(10, 10), buddha=True)

    # Create cats and add them to the environment
    cat1 = Cat(name="Isha", color="orange", personality="playful", size="medium", weight=4.5, height=0.3,
               position=(3, 3, 0), gender="female", chat_log=True)
    cat2 = Cat(name="osha", color="white", personality="curious", size="small", weight=3.2, height=0.25,
               position=(7, 7, 0), gender="male", chat_log=True)

    environment.add_cat(cat1)
    environment.add_cat(cat2)

    # Form a bond between the two cats
    cat1.form_bond(cat2)
   
    # Run the simulation for 100 steps
    environment.run_simulation(steps=100)
```

Note: If you set `buddha=True`, it means that Buddha's guidance will be available in the simulation. The simulation will end when a cat chooses to seek Nirvana and leave the Catrix.

![1](https://raw.githubusercontent.com/Ishanoshada/Ishanoshada/main/ss/06e427658d1b0ffa1b9f647e99632ceb.png)
### Creating Cats

```python
from catrix import Cat

# Create a cat
my_cat = Cat(name='Whiskers', color='gray', personality='curious', size='medium', weight=5, height=30, position=(0, 0, 0), gender='female')
```

### Simulating the Environment

```python
from catrix import Environment

# Create an environment
my_environment = Environment(size=10)

# Add cats to the environment
my_environment.add_cat(my_cat)

# Run the simulation for a specified number of steps
my_environment.run_simulation(steps=100)
```

### Handling Events

```python
# Access cat's behaviors and events
my_cat.meditate()
my_cat.practice_contentment()
my_cat.seek_guidance()
my_cat.offer_gratitude()
```

### Reproduction

```python
# Cats can form bonds and create children
partner = Cat(name='Mittens', color='white', personality='calm', size='medium', weight=5, height=30, position=(0, 0, 0), gender='male')
my_cat.form_bond(partner)
child = my_cat.create_child(partner)
```

### Cosmic Influence

```python
# Cosmic influence can be simulated in the environment
my_environment.simulate_cosmic_influence()
```

### End Simulation

```python
# End the simulation
my_environment.end_simulation()
```

## Simulation and Its Distinction

The Catrix package offers a unique simulation experience, creating a virtual realm where cats interact, grow, and learn. This simulation is distinct from our reality in several key ways:

### 1. Mindful Existence

In the Catrix, cats live in a state of perpetual mindfulness, emphasizing inner peace and self-discovery. Through practices like meditation and seeking guidance, they cultivate a deeper understanding of their virtual environment.

### 2. Harmonious Coexistence

Cats in the simulation form bonds and engage with their surroundings in a balanced and harmonious manner. They demonstrate behaviors rooted in contentment, curiosity, and gratitude, fostering a peaceful virtual ecosystem.

### 3. Cosmic Influence

Occasionally, a profound cosmic influence permeates the simulation, offering unique experiences for the cats. This ethereal event introduces new opportunities for growth and enlightenment.

### 4. Interaction with Other Species

The simulation introduces other virtual species like mice, birds, and squirrels. Cats respond to these species with varying emotions, adding depth to their experiences.

### 5. Eternal Exploration

Unlike our world, where time progresses linearly, the Catrix allows for a dynamic and immersive exploration of existence. Cats engage in activities, form bonds, and undergo personal growth, creating a rich tapestry of virtual life.

This distinctive simulation provides a serene and enlightening environment for both virtual feline inhabitants and observers.

### Catrix Story

![2](https://github.com/Ishanoshada/Ishanoshada/blob/main/ss/f9b4a2887ec165f1ec28636c27fd1512.png?raw=true)

 ```markdown
 Once upon a time, in a virtual realm known as the Catrix, a harmonious world awaited curious souls. Here, cats roamed freely, embodying principles of contentment, gratitude, and boundless curiosity. Each feline resident contributed to a balanced ecosystem, creating an environment of serene beauty.

One fateful day, a cosmic influence swept through the simulation, igniting a profound transformation. Cats began seeking inner guidance, meditating in pursuit of tranquility, and embracing a sense of oneness with the virtual world. The simulation pulsed with newfound energy and purpose.

Bonds formed among the cats, uniting them in a shared journey of enlightenment. As the ages passed, the Catrix evolved, introducing new species and challenges. Birds, mice, and squirrels brought opportunities for observation and growth, expanding the cats' understanding of the interconnectedness of all beings.

In this virtual realm, time flowed differently, marked by cycles of day and night. Cats reveled in exploration during the day and sought restful contemplation under the starlit sky. Each moment held significance, a reminder of the boundless possibilities that awaited within the Catrix.

As the ages progressed, the cats' wisdom deepened, and the simulation flourished. Bonds of friendship and understanding transcended the boundaries of their virtual existence. The Catrix became a testament to the power of unity and the potential for enlightenment within even the most virtual of realms.
```


## License

This package is released under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

Special thanks to [Buddha](catrix/buddha.py) for providing guidance and wisdom in the simulation.


**Repository Views** ![Views](https://profile-counter.glitch.me/catrix/count.svg)

## Contact

For any questions or feedback, please email us at ic31908@gmail.com

