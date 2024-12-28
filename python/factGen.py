import streamlit as st
import random

categories = [
    "Science",
    "History",
    "Nature",
    "Technology",
    "Geography",
    "Food",
    "Sports",
    "Arts and Literature",
    "Health and Medicine",
    "Random"
]

facts = {
    "Science": [
        "The speed of light in a vacuum is approximately 299,792 kilometers per second, making it the fastest known phenomenon in the universe.",
        "Water expands by about 9% when it freezes, which is why ice floats on liquid water.",
        "DNA, or deoxyribonucleic acid, carries the genetic instructions for the development and functioning of all known living organisms.",
        "The Earth's core is as hot as the surface of the Sun, with temperatures reaching up to 6,000°C (10,800°F).",
        "Antimatter is the opposite of normal matter. When matter and antimatter collide, they annihilate each other, releasing immense energy.",
        "The human brain contains about 86 billion neurons, each capable of forming thousands of connections, enabling complex thought and memory.",
        "Stars shine because of nuclear fusion, where hydrogen atoms combine to form helium, releasing vast amounts of energy.",
        "Photosynthesis in plants converts carbon dioxide and sunlight into oxygen and glucose, sustaining life on Earth.",
        "The Large Hadron Collider (LHC) is the world’s most powerful particle accelerator, located at CERN in Switzerland.",
        "Saturn's moon Titan is the only moon in the solar system with a dense atmosphere, primarily composed of nitrogen."
    ],
    "History": [
        "The Great Wall of China, built over centuries, is the longest wall in the world, stretching over 21,000 kilometers.",
        "The Roman Empire lasted over 1,000 years, influencing modern law, government, architecture, and language.",
        "The American Civil War (1861–1865) was primarily fought over the issues of slavery and states' rights.",
        "The printing press, invented by Johannes Gutenberg in the 15th century, revolutionized information dissemination.",
        "World War I (1914–1918) introduced trench warfare, tanks, and chemical weapons on a massive scale.",
        "The Renaissance, spanning the 14th to 17th centuries, marked a rebirth of art, culture, and science in Europe.",
        "The pyramids of Giza in Egypt were constructed as tombs for pharaohs and remain some of the oldest monuments in the world.",
        "The fall of the Berlin Wall in 1989 symbolized the end of the Cold War and the reunification of Germany.",
        "The Black Death, a pandemic in the 14th century, wiped out nearly a third of Europe's population.",
        "The first humans are believed to have migrated out of Africa around 60,000–70,000 years ago."
    ],
    "Nature": [
        "The Amazon rainforest produces 20% of the world’s oxygen and is home to 10% of all known species.",
        "Blue whales, the largest animals on Earth, can weigh as much as 200 tons and grow up to 100 feet long.",
        "Mount Everest, the highest peak in the world, stands at 8,848 meters (29,029 feet) above sea level.",
        "Coral reefs are known as the 'rainforests of the sea' due to their incredible biodiversity.",
        "The Arctic and Antarctic regions are the coldest places on Earth, with temperatures dropping to -89°C (-128°F).",
        "Elephants are the largest land animals and can communicate over long distances using low-frequency rumbles.",
        "Volcanoes form when molten rock (magma) erupts through the Earth's crust, creating cones or calderas.",
        "The Sahara Desert is the largest hot desert in the world, covering over 9 million square kilometers.",
        "Ocean currents, like the Gulf Stream, play a critical role in regulating Earth's climate by transporting heat.",
        "Trees can live for thousands of years; the oldest known tree, Methuselah, is over 4,800 years old."
    ],
    "Technology": [
        "The first computer, ENIAC, was built in 1945 and occupied a space the size of a room.",
        "The Internet, originally developed as ARPANET in the 1960s, connects billions of devices worldwide.",
        "Smartphones contain more computing power than the computers used for the Apollo 11 moon landing.",
        "Blockchain technology underpins cryptocurrencies like Bitcoin, ensuring secure and decentralized transactions.",
        "Artificial Intelligence (AI) is revolutionizing industries by enabling machines to learn and adapt to tasks.",
        "3D printing, or additive manufacturing, allows the creation of objects layer by layer using various materials.",
        "The Global Positioning System (GPS) relies on satellites to provide precise location information.",
        "Quantum computing, still in its infancy, promises to solve complex problems beyond classical computers' capabilities.",
        "The first email was sent in 1971 by Ray Tomlinson, marking the beginning of digital communication.",
        "Electric vehicles (EVs) are becoming increasingly popular as sustainable alternatives to gasoline-powered cars."
    ],
    "Geography": [
        "Africa is the second-largest continent, covering 30.3 million square kilometers and home to 1.4 billion people.",
        "The Pacific Ocean is the largest and deepest ocean, covering over 63 million square miles.",
        "Mount Everest is located in the Himalayan range, on the border between Nepal and China (Tibet).",
        "The Amazon River is the second-longest river in the world, flowing through South America for 6,575 kilometers.",
        "Russia is the largest country by area, spanning 11 time zones and covering over 17 million square kilometers.",
        "Greenland is the largest island in the world that is not a continent, with a population of around 56,000.",
        "The Andes, in South America, is the longest mountain range, stretching over 7,000 kilometers.",
        "Lake Baikal in Siberia is the world’s deepest freshwater lake, reaching depths of 1,642 meters.",
        "The Great Barrier Reef, off Australia’s coast, is the largest coral reef system, visible from space.",
        "Antarctica is the driest, coldest, and windiest continent, covered by 98% ice."
    ],
    "Food": [
        "Chocolate comes from cacao beans, which grow on the cacao tree native to tropical regions.",
        "Sushi originated in Japan and traditionally consists of vinegared rice, raw fish, and seaweed.",
        "Cheese is made by curdling milk using an enzyme called rennet, producing a wide variety of flavors.",
        "Honey never spoils and has been found in ancient Egyptian tombs still fit for consumption.",
        "Bread is one of the oldest prepared foods, with evidence of baking dating back over 30,000 years.",
        "Chili peppers contain capsaicin, which gives them their heat and is used in pain-relief creams.",
        "Avocados are fruits, and their high-fat content makes them a unique dietary staple.",
        "Pizza, one of the world’s most popular foods, originated in Naples, Italy, in the 18th century.",
        "Pasta comes in over 300 shapes, each designed to pair well with specific types of sauces.",
        "Coffee is the second most traded commodity globally, after crude oil."
    ],
    "Sports": [
        "The Olympic Games originated in ancient Greece over 2,700 years ago.",
        "Soccer, or football, is the most popular sport globally, with over 4 billion fans.",
        "Cricket is the second most popular sport, particularly in countries like India, Pakistan, and England.",
        "The first Super Bowl was played in 1967 between the Green Bay Packers and Kansas City Chiefs.",
        "Tennis matches are scored using 'love,' '15,' '30,' and '40,' with 'love' meaning zero points.",
        "Michael Phelps holds the record for the most Olympic gold medals won by an individual, with 23.",
        "The FIFA World Cup is the most-watched sporting event, drawing billions of viewers worldwide.",
        "Basketball was invented by James Naismith in 1891 as an indoor game for students.",
        "The Tour de France, first held in 1903, is the most prestigious cycling race in the world.",
        "Golf was first played in Scotland, with the earliest courses dating back to the 15th century."
    ],
    "Arts and Literature": [
        "Leonardo da Vinci's 'Mona Lisa' is one of the most famous paintings, housed in the Louvre Museum in Paris.",
        "William Shakespeare, often called the Bard of Avon, wrote 39 plays and 154 sonnets.",
        "The novel 'Don Quixote' by Miguel de Cervantes is considered one of the first modern novels.",
        "Vincent van Gogh created over 2,000 artworks, including 'Starry Night,' despite battling mental illness.",
        "The Great Gatsby by F. Scott Fitzgerald is a classic American novel set in the 1920s.",
        "The Sistine Chapel ceiling, painted by Michelangelo, depicts scenes from the Book of Genesis.",
        "The Harry Potter series by J.K. Rowling has sold over 500 million copies worldwide.",
        "Pablo Picasso co-founded the Cubist movement, revolutionizing modern art.",
        "The poem 'The Raven' by Edgar Allan Poe is known for its dark, gothic themes.",
        "Jane Austen’s novels, like 'Pride and Prejudice,' explore themes of love, class, and society."
    ],
    "Health and Medicine": [
        "The human heart beats around 100,000 times a day, pumping 5.7 liters of blood per minute.",
        "Vaccines work by stimulating the immune system to recognize and fight specific pathogens.",
        "The discovery of penicillin by Alexander Fleming in 1928 revolutionized modern medicine.",
        "Regular exercise can reduce the risk of chronic diseases like diabetes, heart disease, and stroke.",
        "The liver is the largest internal organ and is capable of regenerating itself after damage.",
        "Sleep is essential for health, with adults recommended to get 7–9 hours of rest each night.",
        "The brain uses about 20% of the body's total energy, despite only making up 2% of its weight.",
        "The stethoscope, invented in 1816, remains a vital tool for diagnosing heart and lung conditions.",
        "Mental health disorders like depression affect over 280 million people worldwide.",
        "Blood pressure is measured in millimeters of mercury (mmHg) and includes systolic and diastolic readings."
    ],
    "Random": [
        "Octopuses have three hearts, and their blood is blue due to the presence of copper-based hemocyanin.",
        "Bananas are berries, but strawberries are not, according to botanical definitions.",
        "A group of flamingos is called a 'flamboyance,' reflecting their vibrant pink color.",
        "Wombat poop is cube-shaped, a unique adaptation for marking territory.",
        "There are more stars in the universe than grains of sand on all the beaches on Earth.",
        "The Eiffel Tower grows about 6 inches in summer due to thermal expansion of its iron.",
        "Sharks existed before trees, with their earliest ancestors appearing over 400 million years ago.",
        "The dot over the lowercase letters 'i' and 'j' is called a 'tittle.'",
        "Cats have five toes on their front paws but only four on their back paws.",
        "Bees can recognize human faces using a combination of pattern recognition and memory."
    ]
}

st.sidebar.radio("Select a category", categories)

st.markdown("Random Fact Generator")
st.write("Discover fascinating facts from various categories. Select a category from the sidebar and click the button to uncover a new fact")