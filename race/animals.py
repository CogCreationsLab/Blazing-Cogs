import random

racers = (
    (self.emoji('Bandit'), 'predator'),
    (self.emoji('MegaKnight'), 'predator'),
    (self.emoji('BattleRam'), 'predator'),
    (self.emoji('IceSpirit'), 'fast'),
    (self.emoji('FireSpirits'), 'fast'),
    (self.emoji('GoblinGiant'), 'abberant'),
    (self.emoji('LavaHound'), 'abberant'),
    (self.emoji('Golem'), 'slow'),
    (self.emoji('Giant'), 'slow'),
    (self.emoji('HogRider'), 'fast'),
    (self.emoji('PEKKA'), 'predator'),
    (self.emoji('Goblins'), 'fast'),
    (self.emoji('SpearGoblins'), 'abberant'),
    (self.emoji('Princess'), 'abberant'),
    (self.emoji('Wizard'), 'fast'),
    (self.emoji('IceWizard'), 'fast'),
    (self.emoji('ElectroWizard'), 'fast'),
    (self.emoji('Sparky'), 'slow'),
    (self.emoji('Miner'), 'abberant'),
    (self.emoji('Valkyrie'), 'fast'),
    (self.emoji('GoblinGang'), 'fast'),
    (self.emoji('RoyalGhost'), 'fast'),
    (self.emoji('MagicArcher'), 'fast'),
    (self.emoji('NightWitch'), 'slow'),
    (self.emoji('InfernoDragon'), 'slow'),
    (self.emoji('BabyDragon'), 'slow'),
    (self.emoji('Lumberjack'), 'fast'),
    (self.emoji('SkeletonArmy'), 'fast'),
    (self.emoji('Skeletons'), 'fast'),
    (self.emoji('Guards'), 'fast'),
    (self.emoji('Hunter'), 'slow'),
    (self.emoji('DarkPrince'), 'predator'),
    (self.emoji('Prince'), 'predator'),
    (self.emoji('Bowler'), 'slow'),
    (self.emoji('Balloon'), 'slow'),
    (self.emoji('Witch'), 'abberant'),
    (self.emoji('CannonCart'), 'abberant'),
    (self.emoji('Executioner'), 'slow'),
    (self.emoji('GiantSkeleton'), 'slow'),
    (self.emoji('IceGolem'), 'slow'),
    (self.emoji('MegaMinion'), 'slow'),
    (self.emoji('DartGoblin'), 'fast'),
    (self.emoji('Musketeer'), 'fast'),
    (self.emoji('Zappies'), 'fast'),
    (self.emoji('FlyingMachine'), 'slow'),
    (self.emoji('MiniPEKKA'), 'abberant'),
    (self.emoji('ThreeMusketeers'), 'fast'),
    (self.emoji('RoyalHogs'), 'fast'),
    (self.emoji('Bats'), 'fast'),
    (self.emoji('SkeletonBarrel'), 'slow'),
    (self.emoji('Bomber'), 'fast'),
    (self.emoji('Minions'), 'fast'),
    (self.emoji('MinionHorde'), 'fast'),
    (self.emoji('Archers'), 'fast'),
    (self.emoji('Knight'), 'slow'),
    (self.emoji('Barbarians'), 'fast'),
    (self.emoji('EliteBarbarians'), 'fast'),
    (self.emoji('RoyalGiant'), 'slow'),
    (self.emoji('Rascals'), 'abberant'),
    (self.emoji('RoyalRecruits'), 'steady')
)


class Animal:
    def __init__(self, emoji, _type):
        self.emoji = emoji
        self._type = _type
        self.track = "•   " * 20
        self.position = 80
        self.turn = 0
        self.current = self.track + self.emoji

    def move(self):
        self._update_postion()
        self.turn += 1
        return self.current

    def _update_postion(self):
        distance = self._calculate_movement()
        self.current = "".join(
            (
                self.track[: max(0, self.position - distance)],
                self.emoji,
                self.track[max(0, self.position - distance) :],
            )
        )
        self.position = self._get_position()

    def _get_position(self):
        return self.current.find(self.emoji)

    def _calculate_movement(self):
        if self._type == "slow":
            return random.randint(1, 3) * 3
        elif self._type == "fast":
            return random.randint(0, 4) * 3

        elif self._type == "steady":
            return 2 * 3

        elif self._type == "abberant":
            if random.randint(1, 100) >= 90:
                return 5 * 3
            else:
                return random.randint(0, 2) * 3

        elif self._type == "predator":
            if self.turn % 2 == 0:
                return 0
            else:
                return random.randint(2, 5) * 3

        elif self._type == ":unicorn:":
            if self.turn % 3:
                return random.choice([len("blue"), len("red"), len("green")]) * 3
            else:
                return 0
        else:
            if self.turn == 1:
                return 14 * 3
            elif self.turn == 2:
                return 0
            else:
                return random.randint(0, 2) * 3
