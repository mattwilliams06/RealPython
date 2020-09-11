def save_dict(dict_to_save, path):
    import pickle
    import os
    name = 'test_dict.pickle'
    if not isinstance(dict_to_save, dict):
        print('Function takes dictionaries only.')
    else:
        with open(os.path.join(path,name), 'wb') as f:
            pickle.dump(dict_to_save,f)
            print(f'Pickle completed at {path}')

def load_dict(filepath):
    import pickle
    with open(filepath, 'rb') as f:
        return pickle.load(f)
