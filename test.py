import yaml
from yaml.loader import SafeLoader
with open('/home/runner/work/testrepoyml/testrepoyml/config.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
