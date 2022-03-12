import random

facts = ["The worlds oldest wooden wheel has been around for more than 5,000 years",
         "Dead skin cells are a main ingredient in household dust",
         "Sudan has more pyramids than any country in the world",
         "The cornea is one of only two parts of the human body without blood vessels",
         "The worlds first animated feature film was made in Argentina",
         "German chocolate cake was invented in Texas",
         "There is enough gold inside Earth to coat the planet",
         "Human beings can use only a small fraction of Earths water",
         "It takes a drop of water 90 days to travel the entire Mississippi River",
         "The first person processed at Ellis Island was a 15-year-old girl from Ireland",
         "Japan has one vending machine for every 40 people",
         "Lemons float, but limes sink",
         "McDonalds once made bubblegum-flavored broccoli",
         "Theres only one letter that doesnt appear in any U.S. state name",
         "A cow-bison hybrid is called a beefalo",
         "Scotland has 421 words for snow",
         "Armadillo shells are bulletproof",
         "The longest English word is 189,819 letters long",
         "Some octopus species lay 56,000 eggs at a time",
         "Cats have fewer toes on their back paws",
         "Blue whales eat half a million calories in one mouthful",
         "Most Disney characters wear gloves to keep animation simple",
         "The man with the worlds deepest voice can make sounds humans cant hear",
         "The current American flag was designed by a high school student",
         "Cows dont have upper front teeth",
         "Thanks to 3D printing, NASA can basically email tools to astronauts",
         "Bananas grow upside down",
         "There were active volcanoes on the moon when dinosaurs were alive",
         "Dogs sniff good smells with their left nostril",
         "Human noses and ears get bigger as we age",
         "Movie trailers originally played after the movie",
         "Mercedes invented a car controlled by a joystick",
         "The CIA headquarters has its own Starbucks, but baristas dont write names on the cups",
         "Giraffe tongues can be 20 inches long",
         "Theres only one U.S. state capital without a McDonalds",
         "Humans arent the only animals that dream",
         "The inventor of the microwave appliance received only $2 for his discovery",
         "The Eiffel Tower can grow more than six inches during the summer",
         "Bees can fly higher than Mount Everest",
         "Ancient Egyptians used dead mice to ease toothaches",
         ]


def factGenerator():
    fact = random.choices(facts)
    return fact


# print(factGenerator())
