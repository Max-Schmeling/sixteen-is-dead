import random
import time


class Player(object):
    def __init__(self, name, bot=False, godmode=False):
        self.name = name.strip() # Name des Spielers
        self.bot = bot # menschlich oder bot
        self.score = 0 # Punktzahl
        self.godmode = godmode # Geheimwaffe
        if self.bot: self.name = "BOT " + self.name
        if self.godmode: self.score = 15
        
    def decide(self):
        """ Entscheidet (selbst, wenn <self.bot> == True), ob (nocheinmal) gewuerfelt wird """
        if not self.godmode: # Ehrlicher Modus
            if not self.bot: # menschlicher Spieler
                user_input = input("{0}: Muechtest du wuerfeln? [j|n] ".format(self.name)).strip().lower()
                while not (user_input.startswith("j") or user_input.startswith("n")):
                    user_input = input("{0}: Ungueltige Eingabe! Bitte gib [j]a oder [n]ein an: ".format(self.name)).strip().lower()
                if user_input.startswith("j"):
                    return True # Ja, der menschliche Spieler will wuerfeln
    
            else:
                def emulate_human_decision_process():
                    """ Ein Hauch von Menschlichkeit """
                    time.sleep(1)
                    propability = 0
                    if self.score <= 9:
                        propability = 1
                    elif self.score <= 11:
                        propability = 0.8
                    elif self.score <= 13:
                        propability = 0.2
                    elif self.score <= 14:
                        propability = 0.05
                    return propability
                
                propability = emulate_human_decision_process()
                decision = random.choices([True, False], [propability, 1-propability])
                return decision[0] # Computergesteuerte Entscheidung auf Basis von <emulate_human_decision_process()>
            
        else: # Godmode
            return False # Nein, es soll nicht gewuerfelt werden. Der Spieler hat bereits 15 Punkte :D
        
        return False # Nein, es soll nicht gewuerfelt werden
            

    def roll_dice(self, number=1, faces=6, seed=None):
        """ Wuerfelt mit <number> wuerfeln und gibt die Ergebnise in einer list() zurueck """
        random.seed(seed)
        rands = []
        for i in range(number):
            rand = random.randint(1, faces)
            rands.append(rand)
        return rands


def sixteen_is_dead(players):
    for player in players:
        
        sum_of_player = 0
        print("{0} Ist am Zug.".format(player.name))
        do_dice = player.decide()
        
        while do_dice:
            
            _sum = sum(player.roll_dice())
            player.score += _sum
            print("{0} hat eine {1} gewuerfelt. Insgesamt: {2}".format(player.name, _sum, player.score))
            
            if player.score >= 16:
                print("{0} hat verloren.".format(player.name))
                player.score = 0
                do_dice = False
                
            elif player.score == 9:
                print("{0} darf nicht mehr wuerfeln.".format(player.name))
                do_dice = False
                
            elif player.score == 10:
                print("{0} muss nochmal wuerfeln. (Es wird in 3 Sekunden automatisch fuer dich gewuerfelt)".format(player.name))
                time.sleep(3)
                
            else:
                do_dice = player.decide()
        
        print("{0} hat seine Runde mit {1} Punkten beendet.".format(player.name, player.score))
        print()
        
    sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
    for i, p in enumerate(sorted_players, 1):
        print("Platz #{0} geht an {1} mit {2} Punkten".format(i, p.name, p.score))
            


players = [
    Player("Detlef", False), 
    Player("Karsten", False), 
    Player("Alex", True)
]
sixteen_is_dead(players)
