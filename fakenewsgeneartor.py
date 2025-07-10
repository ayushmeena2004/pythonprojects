import random
#Subjects
names = [
    "Ayush", "Riya", "Ananya", "Kabir", "Aman", "Priya", "Neha", "Rohan", "Simran", "Vikas",
    "Aisha", "Rahul", "Pooja", "Sahil", "Aniket", "Divya", "Kunal", "Sneha", "Aarav", "Ishita",
    "Rajat", "Tanvi", "Varun", "Sanya", "Yash", "Komal", "Arnav", "Bhavya", "Dev", "Nisha",
    "Lakshya", "Megha", "Parth", "Muskan", "Manav", "Preeti", "Vedant", "Diya", "Sameer", "Naina",
    "Hardik", "Shreya", "Siddharth", "Anvi", "Vivaan", "Esha", "Harsh", "Jhanvi", "Gaurav", "Tanya"
]
#Actions
funny_actions = [
    "eats a shoe", "sings to a plant", "dances with a broom", "talks to a wall", "laughs at nothing",
    "fights a pillow", "runs from a butterfly", "paints their face green", "jumps into a dustbin",
    "makes weird noises", "wears socks on hands", "hugs a tree", "pretends to be a cat", "chases their own shadow",
    "builds a house of cards", "starts a staring contest with a mirror", "plays chess with an imaginary friend",
    "tries to fly", "argues with a mosquito", "tickles themselves", "catches invisible fish",
    "makes faces at the moon", "sleeps under the table", "plays hide and seek with a shoe",
    "dances in the rain wearing sunglasses", "laughs like a donkey", "mimics a robot", "talks like a pirate",
    "eats ice cream with a fork", "tries to hypnotize people", "wears a t-shirt as pants",
    "counts stars during the day", "draws faces on potatoes", "sings opera in the bathroom",
    "jumps like a frog", "rides an invisible bicycle", "acts like a superhero", "makes animal sounds in class",
    "throws paper planes at the fan", "stares at ceiling fans", "names every ant they see",
    "writes love letters to pizza", "uses banana as a phone", "scares people with a mask",
    "plays guitar on a broomstick", "argues with their shoes", "orders food for their pet rock",
    "does yoga with a dog", "makes prank calls to their own number"
]
#Objects
funny_objects = [
    "a flying potato", "a dancing cactus", "a rubber chicken", "a talking pen", "an invisible car",
    "a rainbow-colored wig", "a magic spoon", "a one-eyed teddy bear", "a pizza slice with a crown",
    "a plastic lizard", "a glowing watermelon", "a superhero cape", "a fart cushion", "a glitter bomb",
    "a pair of bunny slippers", "a singing lamp", "a fish-shaped pillow", "a wobbly chair", "a broken umbrella",
    "a crying emoji pillow", "a funky hat", "a detective magnifying glass", "a box of expired chocolates",
    "a fridge magnet", "a banana peel", "a mini drum", "a unicorn toy", "a skateboard with wings",
    "a mirror with lipstick marks", "a toy dinosaur", "a half-eaten donut", "a giant rubber duck",
    "a weird selfie stick", "a dancing robot toy", "a book of bad jokes", "a tiny guitar", "a whistle",
    "a sleeping mask", "a star-shaped balloon", "a chocolate fountain", "a bag of fake spiders",
    "a disco light", "a moon-shaped pillow", "a ghost costume", "a TV remote with no batteries",
    "a half-broken headphone", "a glow stick", "a pirate eye-patch", "a potato wearing glasses",
    "a glittery scarf"
]

while True:
    input1 = input("You want to generate some funny sentences? (yes/no): ").strip().lower()
    
    if input1 == 'yes':
        try:
            count = int(input("How many funny sentences do you want to generate? "))
            print("\nHere you go:\n")
            for _ in range(count):
                name = random.choice(names)
                funny_action = random.choice(funny_actions)
                funny_object = random.choice(funny_objects)
                print(f"{name} {funny_action} using {funny_object}.")
            print()
        except ValueError:
            print("Please enter a valid number.\n")
    else:
        print("\nThank you for using the Funny Sentence Generator! 😄")
        break
    




