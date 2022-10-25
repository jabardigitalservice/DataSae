import yaml

'''
read yaml config dan parse into file and class

'''


def get_config(filepath):
    result = None
    with open(filepath, "r") as stream:
        try:
            result = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return result
