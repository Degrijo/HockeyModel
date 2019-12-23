from abc import ABC
from enum import Enum
from time import clock


class Main:
    def main(self):
        god = Creator()
        god.create_game()
        god.create_violation()
        god.create_commands()
        god.create_referees()


class Creator:
    def create_game(self):
        self.game = Game(clock(), 0, 0, 0)

    def create_violation(self):
        pass

    def create_commands(self):
        pass

    def create_referees(self):
        pass


class Game:
    def __init__(self, time, period, goals1, goals2):
        self.time, self.period, self.goals1, self.goals2 = time, period, goals1, goals2


class Team:
    def __init__(self, composition, goalkeeper, main_trainer, second_trainer):
        self.composition, self.goalkeeper, self.main_trainer, self.second_trainer = composition, goalkeeper, \
                                                                                    main_trainer, second_trainer


class Trainer(ABC):
    def __init__(self, name, soname):
        self.name, self.soname = name, soname

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


class Player(ABC):
    def __init__(self, name, soname, number, k_usefull):
        self.name, self.soname, self.number, self.k_usefull = name, soname, number, k_usefull
        self.violations = []

    def give_pass(self, player):
        pass

    def upset(self, violation):
        self.violations.append(violation)

    def leave(self):
        pass

    def come(self):
        pass


class Goalkeeper(Player):
    def keep_gate(self):
        pass


class FieldPlayer(Player):
    def attack_gate(self):
        pass


class Violation:
    def __init__(self, violation_time, violation_type):
        self.violation_time, self.violation_type = violation_time, violation_type


class ViolationType(Enum):
    footboard = 1
    high_hockey_stick = 2
    shift_rules = 3
    broken_hockey_stick = 4
    rough_power_reception = 5


class Referee(ABC):
    def __init__(self, name, soname):
        self.name, self.soname = name, soname

    def continue_game(self, game):
        pass

    def start_game(self, game):
        pass

    def finish_game(self, game):
        pass

    def commit_violation(self, player, violation):
        pass

    def throw_ball(self):
        pass

    def send_to_freebox(self, player, time):
        pass


class MainReferee(Referee):
    def count_goal(self, game):
        pass


class LineReferee(Referee):
    def commit_wrong_entrance(self):
        pass

    def commit_forwarding(self):
        pass
