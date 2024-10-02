import zipfile
import os

def unzip_data(file):
    # Open the zip file
    output_dir = f'./data/raw/{file}'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    zip_file_path = f'./data/landing/{file}.zip'

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(output_dir)
        

if __name__ == "__main__":
    # filename = "HHP_release"
    # for i in range(1,4):
    #     unzip_data(filename + str(i))
    filename = "HHP_release3"
    unzip_data(filename)