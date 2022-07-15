import requests

def download(url, directory):
    get_response = requests.get(url,stream=True)
    file_name  = directory+"/"+url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return file_name