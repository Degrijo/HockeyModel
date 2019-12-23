from abc import ABC
from enum import Enum
from time import clock
from random import randint


class Main:
    def main(self, god):
        god.create_game()
        god.create_violation()
        god.create_commands()
        god.create_referees()


class Creator:
    def create_game(self):
        self.game = Game(clock(), 0, 0, 0)
        print('Game created')

    def create_violation(self):
        pass

    def create_commands(self):
        composition1 = [FieldPlayer('FieldPlayer', f'№{i}', i, str(randint(0, 100)/100)) for i in range(1, 16)]
        goalkeeper1 = Goalkeeper('Goalkeeper', f'№{16}', 16, str(randint(0, 100)/100))
        main_trainer1 = MainTrainer("Main", "Trainer 1")
        second_trainer1 = SecondTrainer("Second", "Trainer 1")
        self.team1 = Team(composition1, goalkeeper1, main_trainer1, second_trainer1)
        composition2 = [FieldPlayer('FieldPlayer', f'№{i}', i, str(randint(0, 100) / 100)) for i in range(17, 32)]
        goalkeeper2 = Goalkeeper('Goalkeeper', f'№{32}', 32, str(randint(0, 100) / 100))
        main_trainer2 = MainTrainer("Main", "Trainer 2")
        second_trainer2 = SecondTrainer("Second", "Trainer 2")
        self.team2 = Team(composition2, goalkeeper2, main_trainer2, second_trainer2)

    def create_referees(self):
        self.trainers = [MainReferee("Main", "Referee"), LineReferee("Line", "Referee 1"), LineReferee("Line", "Referee 2")]


class Game:
    def __init__(self, time, period, goals1, goals2):
        self.time, self.period, self.goals1, self.goals2 = time, period, goals1, goals2


class Team:
    def __init__(self, composition, goalkeeper, main_trainer, second_trainer):
        self.composition, self.goalkeeper, self.main_trainer, self.second_trainer = composition, goalkeeper, \
                                                                                    main_trainer, second_trainer
        print("Created team")


class Trainer(ABC):
    def __init__(self, name, soname):
        self.name, self.soname = name, soname
        print(f"Created trainer {self.name} {self.soname}")

    def give_assistance(self, player):
        print(f"{self.name} {self.soname} gave assistance to {player.name} {player.soname}")

    def swap(self, player1, player2):
        print(f"{self.name} {self.soname} swap {player1.name} {player1.soname} with {player2.name} {player2.soname}")


class MainTrainer(Trainer):
    def get_timeout(self):
        print(f"{self.name} {self.soname} get timeout")

    def dismiss_goalkeeper(self, goalkeeper, player):
        print(f"{self.name} {self.soname} dismissed {goalkeeper.name} {goalkeeper.soname}")

    def put_goalkeeper(self, goalkeeper, player):
        print(f"{self.name} {self.soname} put {goalkeeper.name} {goalkeeper.soname}")


class SecondTrainer(Trainer):
    def give_advise(self, player):
        print(f"{self.name} {self.soname} gave advise to {player.name} {player.soname}")


class Player(ABC):
    def __init__(self, name, soname, number, k_usefull):
        self.name, self.soname, self.number, self.k_usefull = name, soname, number, k_usefull
        self.violations = []
        print(f"Created player {self.name} {self.soname}")

    def give_pass(self, player):
        pass

    def upset(self, violation):
        self.violations.append(violation)

    def leave(self):
        print(f'{self.name} {self.soname} leaved this game')

    def come(self):
        print(f'{self.name} {self.soname} came this game')


class Goalkeeper(Player):
    def keep_gate(self):
        return True if float(self.k_usefull)*100 + randint(0, 25) >= 50 else False


class FieldPlayer(Player):
    def attack_gate(self):
        return True if float(self.k_usefull)*100 + randint(0, 25) >= 50 else False


class Violation:
    def __init__(self, violation_time, violation_type):
        self.violation_time, self.violation_type = violation_time, violation_type


class ViolationType(Enum):
    footboard = 'footboard'
    high_hockey_stick = 'high hockey stick'
    shift_rules = 'shift rules'
    broken_hockey_stick = 'broken hockey stick'
    rough_power_reception = 'rough power reception'


class Referee(ABC):
    def __init__(self, name, soname):
        self.name, self.soname = name, soname

    def continue_game(self, game):
        print('Game continue')

    def start_game(self, game):
        print('Game started')

    def finish_game(self, game):
        print('Game finished')

    def commit_violation(self, player, violation):
        print(f'{self.name} {self.soname} commit {violation.violation_type} of {player.name} {player.soname}')

    def throw_ball(self):
        print(f'{self.name} {self.soname} throw ball')

    def send_to_freebox(self, player, time):
        return True


class MainReferee(Referee):
    def count_goal(self, game):
        print(f'Scope of the game {str(game.goals1)} : {str(game.goals2)}')


class LineReferee(Referee):
    def commit_wrong_entrance(self):
        print(f'{self.name} {self.soname} commited wrong entrance')

    def commit_forwarding(self):
        print(f'{self.name} {self.soname} commited forwarding')
