import yaml

with open("../configuration.yaml", "r") as yamlfile:

   data = yaml.load(yamlfile, Loader=yaml.FullLoader)
       print("Read successful")
   print(data)
