class Unit:
    def __init__(self, name, hp, damage): # 유닛의 이름, 체력, 공격력
        self.name = name
        self.hp = hp
        self.damage = damage

        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"HP: {self.hp}, 공격력: {self.damage}")

    # 유닛의 공격 기능
    def attack(self, unit:object):
        print(f"{self.name}: {unit}을 공격합니다. [공격력: {self.damage}]")
        unit.__damaged(self.damage)
    
    # 유닛의 피해 기능
    def __damaged(self, damage): # 외부에서 접근할 수 없다.
        print(f"{self.name}: {damage}만큼의 데미지를 입었습니다.")
        self.hp -= damage # 해당 유닛의 체력 감소
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0: # 체력이 0 이하라면 die
            print(f"{self.name}: 적의 공격에 의해 사망하였습니다!")
            
    def __str__(self):
        return self.name + "[hp: " + str(self.hp) + ", damage: " + str(self.damage) + "]"
    
# 메모리에 구현 : 틀(설계도)에 맞춰서 유닛(인스턴스 변수)을 찍어낸다.
print("========= 생성! =========")
worrior1 = Unit("전사1", 40, 5)
worrior2 = Unit("전사2", 40, 5)
archer1  = Unit("궁수1", 25, 10)

# 공격 메서드
print("========= 공격! =========")
worrior1.attack(worrior2)
print("")
archer1.attack(worrior1)
print("")

for _ in range(5):
    archer1.attack(worrior1)
    print("")