print('hello mason, this is a terraria checklist for progression!!')
n = input('press enter to continue')
list = ['get 1 full bar of hearts / make arena for eye of cuthulu ask me if you need help on this', 'fight eye of cuthulu', 'make yoyo, bow, and war axe', 'go to corruption and mine two orbs using bombs to get to orbs, get musket and other item, then build housing for arm dealer' , 'make arena in corruption to fight eater of worlds and keep getting more and more hearts', 'make jester arrows with arrows and falling stars because they pierce and hit all the parts of eater of worlds', 'fight eater of worlds', 'make shadow scale armor and nightmare pickaxe', 'make hellavator down to hell and put ropes in it to make it easy to traverse' , 'build arena at dungeon and once you get within 4 or 5 hearts of max, fight skeltron', 'make bucket with iron and fill it with water, pour it on lava and mine the obsidian', 'get waterleaf which grows on sand, and firblossom which grows on ash in the underworld, make obsidian skin potions', 'go to hell(haha) and take obsidian skin potions go in lava and mine as much hellstone as humanly possible, get a hellforge from one of the houses, and mine more obsidian to make the hellstone bars', 'make molten armor, hellfire bow, firey great sword if you dont have enough get more hellstone', 'you have reached this point ask me for further guidance and I \nwill update program and add more instructions!']
f = open('save.txt', 'r')
point = f.readline()
f.close()
x = 1
while x == 1:
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  print(list[int(point)])
  h = input('press enter for next step or type exit exactly as seen to leave\n--->')
  if h == 'exit':
    x = 2
  else:
    point1 = int(point) + 1
    point = point1
f = open('save.txt', 'w')
try:
  f.write(str(point))
except:
  f.close()
f.close()