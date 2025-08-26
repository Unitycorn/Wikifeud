
## 👨‍👩‍👧‍👦 Team:

https://github.com/Unitycorn/

https://github.com/anna-pohle/

https://github.com/Markus-Huckriede/

https://github.com/alinejanke/

https://github.com/AllineWamsser

https://github.com/Eugen_Ivliev



# 🧠 WikiFeud – The Wikipedia Word Duel
WikiFeud is a fast-paced, competitive multiplayer word game in couch-coop-mode, built during a hackathon. Two players go head-to-head by naming words they think appear frequently in a randomly selected Wikipedia article. The more often a word shows up in the article, the more points it scores!


## 🎮 Gameplay Overview
1. Welcome screen & game explanation
2. Players enter their names
3. Start the game with a key press
4. Randomly select starting player
5. Selection of Wikipedia-Article
    - Randomly selected in the background via the Wikipedia-API
    - Minimum article length required
8. Announce article title to players
9. Option to reroll and get a new article
10. In the background: Generate and clean up a word frequency list from the article using NLP
11. Display an empty scoreboard
12. Players take turns entering words
13. Scores:
    - Score is based on how often each word appears in the article
    - If the word doesn't appear in the generated word List, it scores 0
14. After X rounds (e.g., 5): Show total scores & Announce the winner!


## ⚙️ Tech Stack
Language: Python 3

Wikipedia API – to fetch article content

SpaCy – for natural language processing (tokenization, lemmatization, etc.)

Colorama – for colorful terminal output

CLI-based interface (terminal/console game)

## 📦 How to Run
Make sure you have Python 3 installed.
clone git repo
install requirements.txt

pip install -r requirements.txt
python main.py


## 🧪 Example Round
🎲 Selected article: Albert Einstein

👤 Player 1: “relativity” → 5 points

👤 Player 2: “physics” → 12 points

...

🏆 Winner: Player 2



## 🚧 Project Status
⚠️ Prototype – Built during a hackathon. The core game loop works well, but there are many ideas for further improvements (e.g., UI, multiplayer over network, advanced word validation, difficulty levels).

### 📄 License
MIT License – Feel free to fork, contribute, and build upon WikiFeud!
