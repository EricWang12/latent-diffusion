


import os
import random
import shutil

def get_image_paths(dir_path, image_paths=[]):
    """
    Recursively gets paths of all images in a directory and its subdirectories.
    """
    return_path = []
    for filename in os.listdir(dir_path):
        filepath = os.path.join(dir_path, filename)
        if os.path.isdir(filepath):
            return_path += get_image_paths(filepath, image_paths)
        elif os.path.splitext(filename)[1].lower() in ['.jpg', '.jpeg', '.png', '.gif']:
            return_path.append(filepath)
    return return_path

def copy_and_split_images(image_paths, output_dir):
    """
    Copies images from the original directory to new directories for training and testing with an index label.
    Splits the images into training and testing datasets in the ratio of 9:1.
    """
    random.shuffle(image_paths)
    num_images = len(image_paths)
    num_train_images = int(num_images * 0.9)
    train_image_paths = image_paths[:num_train_images]
    test_image_paths = image_paths[num_train_images:]
    for i, image_path in enumerate(train_image_paths):
        output_path = os.path.join(output_dir, 'train', f"{i+1}.jpg")
        shutil.copy(image_path, output_path)
    for i, image_path in enumerate(test_image_paths):
        output_path = os.path.join(output_dir, 'test', f"{i+1}.jpg")
        shutil.copy(image_path, output_path)

# # Example usage:
image_paths = get_image_paths('data/THuman_random_hori_64')
output_dir = 'data/thuman_hori_64'
os.makedirs(os.path.join(output_dir, 'train'))
os.makedirs(os.path.join(output_dir, 'test'))
copy_and_split_images(image_paths, output_dir)


def save_file_names_to_txt(directory, output_file):
    """
    Reads all files in a directory and saves their names to a text file.
    """
    with open(output_file, 'w') as f:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                f.write(f"{filename}\n")


save_file_names_to_txt(f"{output_dir}/train", f"{output_dir}/train.txt")
save_file_names_to_txt(f"{output_dir}/test",  f"{output_dir}/test.txt")