class Tower:
  def __init__(self, gem1, gem2, gem3, name):
    self.gem1 = gem1
    self.gem2 = gem2
    self.gem3 = gem3
    self.name = name

class SeatedGem:
  def __init__(self, tower, location, mvp):
    self.tower = tower
    self.location = location
    self.mvp = mvp


silver = Tower("b1","d1","y1","silver")
silverKnight = Tower(silver,"q2","r3","silver knight")

asteriatedRuby = Tower("r2","r1","p1","Asteriated Ruby")
volcano = Tower(asteriatedRuby,"p3","r4","Volcano")

jade = Tower("g3","e3","b2","jade")
greyJade = Tower(jade,"b4","q3","Grey Jade")
MKJ = Tower(jade,"b4","q3","Monkey King Jade")



