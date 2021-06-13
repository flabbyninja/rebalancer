from asset import Asset

def analyse_sectors(assets):
  analysed_data = {}
  for asset in assets:
    if asset.sector in analysed_data:
      analysed_data[asset.sector] += 1
    else:
      analysed_data[asset.sector] = 1
  return analysed_data