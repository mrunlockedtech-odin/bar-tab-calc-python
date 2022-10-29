class Tab:
  menu = {
    'wine': 5,
    'beer': 3,
    'soft_drink': 2,
    'chicken':10,
    'beef':15,
    'veggie':12,
    'dessert':6
  }
  def __init__(self):
    self.total = 0
    self.items = {}
    