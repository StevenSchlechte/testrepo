import yaml

with open("../config.yml", "r") as yamlfile:

   data = yaml.load(yamlfile, Loader=yaml.FullLoader)
       print("Read successful")
   print(data)
