import yaml

with open("config2.yml", "r") as yamlfile:

   data = yaml.load(yamlfile, Loader=yaml.FullLoader)
   print(data)
