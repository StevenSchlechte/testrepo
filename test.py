import yaml

with open("../config.yml", "r") as yamlfile:

   data = yaml.load(yamlfile, Loader=yaml.FullLoader)
   print(data)
