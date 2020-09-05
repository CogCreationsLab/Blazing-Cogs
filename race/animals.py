import random

racers = (
    ("<:BanditCard:751676116280016927>", "fast"),
    ("<:MegaKnightCard:751676158554144908>", "fast"),
    ("<:BattleRamCard:751676202284089384>", "fast"),
    ("<:IceSpiritCard:751678916196040734>", "fast"),
    ("<:FireSpiritsCard:751678981379457054>", "fast"),
    ("<:GoblinGiantCard:751679093141143583>", "abberant"),
    ("<:LavaHoundCard:751679989161918464>", "abberant"),
    ("<:GolemCard:751680015577382935>", "slow"),
    ("<:GiantCard:751726707014238300>", "slow"),
    ("<:HogRiderCard:751726794578722817>", "fast"),
    ("<:PEKKACard:751727813924487178>", "predator"),
    ("<:GoblinsCard:751727887765471344>", "fast"),
    ("<:SpearGoblinsCard:751727928785764422>", "abberant"),
    ("<:PrincessCard:751920096368132226>", "abberant"),
    ("<:WizardCard:751920188684894278>", "fast"),
    ("<:IceWizardCard:751920217793364038>", "abberant"),
    ("<:ElectroWizardCard:751920259379888273>", "fast"),
    ("<:SparkyCard:751920285053354105>", "slow"),
    ("<:MinerCard:751920320201490562>", "abberant"),
    ("<:ValkyrieCard:751920352711409795>", "fast"),
    ("<:GoblinGangCard:751920382679711815>", "fast"),
    ("<:RoyalGhostCard:751920430251507823>", "fast"),
    ("<:MagicArcherCard:751920459276353576>", "fast"),
    ("<:NightWitchCard:751920481325809742>", "slow"),
    ("<:InfernoDragonCard:751920505069502485>", "slow"),
    ("<:BabyDragonCard:751920539743813783>", "slow"),
    ("<:LumberjackCard:751920563454214174> ", "fast"),
    ("<:SkeletonArmyCard:751920600192254085>", "fast"),
    ("<:SkeletonsCard:751920615652458606> ", "fast"),
    ("<:GuardsCard:751920639191023677>", "fast"),
    ("<:HunterCard:751920672942325901>", "slow"),
    ("<:DarkPrinceCard:751920710892388402>", "predator"),
    ("<:PrinceCard:751920740479270952>", "predator"),
    ("<:BowlerCard:751920761253527562>", "slow"),
    ("<:BalloonCard:751920787396624475>", "slow"),
    ("<:WitchCard:751920815687204894>", "abberant"),
    ("<:CannonCartCard:751920868560601118>", "abberant"),
    ("<:ExecutionerCard:751920897019084831>", "slow"),
    ("<:GiantSkeletonCard:751920922155286528>", "slow"),
    ("<:IceGolemCard:751920959417745438>", "slow"),
    ("<:MegaMinionCard:751920982687613082>", "slow"),
    ("<:DartGoblinCard:751921010768347196>", "fast"),
    ("<:MusketeerCard:751921053621551196>", "fast"),
    ("<:ZappiesCard:751921077197996089>", "fast"),
    ("<:FlyingMachineCard:751921101902184469>", "slow"),
    ("<:MiniPEKKACard:751921124077469889>", "abberant"),
    ("<:ThreeMusketeersCard:751921145791512717>", "fast"),
    ("<:RoyalHogsCard:751921167039725649>", "fast"),
    ("<:BatsCard:751921202393645076>", "fast"),
    ("<:SkeletonBarrelCard:751921234916278312>", "slow"),
    ("<:BomberCard:751922275489677412> ", "fast"),
    ("<:MinionsCard:751922322943770685>", "fast"),
    ("<:MinionHordeCard:751922352471670785>", "fast"),
    ("<:ArchersCard:751922376949760101>", "fast"),
    ("<:KnightCard:751922593094959174>", "fast"),
    ("<:BarbariansCard:751922643913146388>", "slow"),
    ("<:EliteBarbariansCard:751922674401542324>", "fast"),
    ("<:RoyalGiantCard:751922710510305311>", "fast"),
    ("<:RascalsCard:751922733637566535>", "slow"),
    ("<:RoyalRecruitsCard:751922766428504065>", "abberant"),
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
