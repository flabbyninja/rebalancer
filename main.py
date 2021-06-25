from asset import Asset

def main():
  my_asset = Asset("Acme Ltd", "Equity", "Healthcare")
  print(my_asset.format_asset())

if __name__ == "__main__":
  main()
  
  