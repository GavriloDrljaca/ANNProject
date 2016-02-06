def return_label(alphabet, tag):
    return alphabet[tag]

def return_list_labels(alphabet, tag_list):
    return_list = []
    for tag in tag_list:
        return_list.append(alphabet[tag])
    return return_list