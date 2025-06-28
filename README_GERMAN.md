# Tag 12 – Zahlenratespiel 🎯

In diesem Projekt wurde ein interaktives Zahlenratespiel (Number Guessing Game) erstellt, bei dem der Benutzer gegen den Computer antritt. Das Spiel bietet zwei Schwierigkeitsgrade und gibt Rückmeldung, ob die geratene Zahl zu hoch oder zu niedrig ist.

## Funktionen

- Konsolenbasiertes Spiel mit klarer Benutzerführung
- Zwei Schwierigkeitsstufen: leicht (10 Versuche), schwer (5 Versuche)
- Zufällige Zahl zwischen 1 und 100 wird generiert
- Rückmeldung bei zu hoher oder zu niedriger Schätzung
- Spiel endet bei korrektem Treffer oder wenn keine Versuche mehr übrig sind

## So funktioniert's

- Das Spiel wählt eine Zufallszahl zwischen 1 und 100.
- Der Spieler entscheidet sich für einen Schwierigkeitsgrad.
- In jedem Versuch gibt der Spieler eine Zahl ein.
- Nach jeder Eingabe wird angezeigt, ob die Schätzung zu hoch, zu niedrig oder korrekt war.
- Bei einem Treffer gewinnt der Spieler, andernfalls verliert er nach Ablauf der Versuche.

## Beispielausgabe
```
 ,----.                                      ,--.  ,--.                                          ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--' `---'  `----'`--'   

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty level. Type 'easy' or 'hard': hard
You have 5 guesses remaining.
What's your guess?: 50
You guessed too high.
You have 4 guesses remaining.
What's your guess?: 25
You guessed too high.
You have 3 guesses remaining.
What's your guess?: 10
You guessed too low.
You have 2 guesses remaining.
What's your guess?: 18
You guessed too low.
You have 1 guesses remaining.
What's your guess?: 23
You guessed too high.
You ran out of guesses. You lose!
```

## Gelernt

- Umgang mit Gültigkeitsbereichen (local vs. global scope)
- Verständnis von **Block Scope** (in Python vs. C++)
- Namensräume (Namespaces) in Python
- Konventionen für Konstantenbenennung (z. B. `MAX_ATTEMPTS`)
