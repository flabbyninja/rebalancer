class Asset:
  def __init__(self, name, type, sector):
    self.name = name
    self.type = type
    self.sector = sector
  
  def format_asset(self):
    return "Name: {}, Type: {}, Sector: {}".format(self.name, self.type, self.sector)