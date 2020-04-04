import yaml
with open('test_steps.yaml') as f:
    data = yaml.load(f)
    print(data)