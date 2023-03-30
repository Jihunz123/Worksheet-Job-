class Job:
    def __init__(self, name, strength, intelligence, endurance):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.endurance = endurance


class Warrior(Job):
    def __init__(self):
        super().__init__("전사", 10, 5, 7)
        self.special_skill = "파워스트라이크"


class Archer(Job):
    def __init__(self):
        super().__init__("궁수", 7, 10, 5)
        self.special_skill = "홀리애로우"


class Wizard(Job):
    def __init__(self):
        super().__init__("마법사", 5, 10, 7)
        self.special_skill = "썬더볼트"


class Rogue(Job):
    def __init__(self):
        super().__init__("도적", 7, 7, 10)
        self.special_skill = "쿼드스로우"


class Player:
    def __init__(self, name, job):
        self.name = name
        self.level = 1
        self.exp = 0
        self.current_hp = 100
        self.max_hp = 100
        self.job = job

        # 캐릭터마다 다른 스탯
        if job.name == "전사":
            self.strength = job.strength + 3
            self.intelligence = job.intelligence - 2
            self.endurance = job.endurance + 2
        elif job.name == "궁수":
            self.strength = job.strength - 2
            self.intelligence = job.intelligence + 3
            self.endurance = job.endurance + 2
        elif job.name == "마법사":
            self.strength = job.strength - 2
            self.intelligence = job.intelligence + 3
            self.endurance = job.endurance + 2
        elif job.name == "도적":
            self.strength = job.strength + 1
            self.intelligence = job.intelligence + 1
            self.endurance = job.endurance + 3

    def use_special_skill(self):
        print(f"{self.name}님의 특수 스킬 '{self.job.special_skill}'을(를) 사용합니다!")
