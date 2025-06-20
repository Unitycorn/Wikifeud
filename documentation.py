"""
Walkthrough - step-by-step des Spielablaufes

1. Begrüßung
2. Spielerklärung anzeigen

3. Spielernamen abfragen (f. Spieler 1 & 2)
4. (Rundenanzahl festlegen)

5. Start des Spiels via Tasteneingabe
6. Startspieler ermitteln (random)
7. Auswahl Wiki-Artikel:
- Mindestlänge Artikel:___
- (Ggf. Mindestanzahl enth. Links)
- dann random choice
8. Bekanntgabe des Wikipedia-Artikels (Titel)
9. Thema auswählen oder neues generieren (wdh 7.)
10.Wiki-Wortliste im Hintergrund generieren & bereinigen
- (list of dicts/list?)
11. Anzeige (noch leeren) User-Wortliste als score-board
12. Spieler 1: Worteingabe
- Wort in neue User-Wortliste/scoreboard
- Generiere Punktzahl*  nach Häufigkeit in Wiki-Liste
  (wenn nicht drin: Häufigkeit = 0)
- next
13. Spieler 2: Worteingabe
- Wort in neue User-Wortliste/scoreboard
- Generiere Punktzahl*  nach Häufigkeit in Wiki-Liste
  (wenn nicht drin: Häufigkeit = 0)
- next
  (x5)
14. Bekanntgabe Punktestand & Gewinner:in
"""