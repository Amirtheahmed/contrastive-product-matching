import requests
from tqdm import tqdm

DATASETS = [
    'http://data.dws.informatik.uni-mannheim.de/largescaleproductcorpus/data/v2/repo-download/contrastive-data.zip'
]


def download_datasets():
    for link in DATASETS:

        '''iterate through all links in DATASETS 
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        response = requests.get(link, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(f'../../data/{file_name}', 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")

        print("%s downloaded!\n" % file_name)

    print("All files downloaded!")
    return


if __name__ == "__main__":
    # Path('../../data/').mkdir(parents=True, exist_ok=True)
    download_datasets()
