def list_to_dict(list_data):
    dict_data = dict()
    for item in list_data:
        dict_data.update(item.copy())
    return dict_data

