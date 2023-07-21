import yaml
with open('config2.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
