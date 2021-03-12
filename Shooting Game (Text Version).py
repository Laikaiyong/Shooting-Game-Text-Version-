class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)

class MaBaoguo(Enemy):
    def __init__(self):
        super().__init__('马保国', 1)


m = Monster()
a = Alien()
mbg = MaBaoguo()

print("""
********** Welcome to the Shooting Game **********
         Code contributed by: Vandyck Lai

Note that the game will end automatically when all 
enemies are eliminated. You can type in <exit> to 
end the game too, have fun! :D

Please choose your weapon to attack specific Enemy

laser --> Alien
gun   --> Monster
闪电鞭 --> 马保国
""")

def player():
    while True:
        x = input("Attack! Select your weapon: ")
        if x == 'exit':
            break
        elif x == 'laser':
            a.hit()
        elif x == 'gun':
            m.hit()
        elif x == '闪电鞭':
            mbg.hit()
        while m.lives == 0 and a.lives == 0 and mbg.lives == 0:
            return(print("\nEnemy eliminated, GOOD JOB!"))

player()