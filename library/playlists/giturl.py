import json

def modify_json_data(json_data):
    modified_data = json_data.copy()

    for key in modified_data:
        value = modified_data[key]
        album = value['album']
        id_name = value['id']
        modified_data[key]['url'] = f"https://github.com/kendreaditya/BlackHole-playlist/raw/main/library/playlists/{album}/{id_name}.m4a"
    
    return modified_data

# Example usage
json_data = json.load(open('Carana Sevane.json', 'r'))
modified_json_data = modify_json_data(json_data)
json.dump(modified_json_data, open('Carana Sevane Github.json', 'w'), indent=2)
