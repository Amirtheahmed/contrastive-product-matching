from zipfile import ZipFile

DATASETS = [
    'http://data.dws.informatik.uni-mannheim.de/largescaleproductcorpus/data/v2/repo-download/contrastive-data.zip'
]


def unzip_files():
    for link in DATASETS:
        file_name = link.split('/')[-1]
        # opening the zip file in READ mode
        with ZipFile(f'../../data/{file_name}', 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()

            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall(path='../../')
            print('Done!')


if __name__ == "__main__":
    # Path('../../data/').mkdir(parents=True, exist_ok=True)
    unzip_files()
