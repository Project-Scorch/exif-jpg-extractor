from exif import Image
import os
import numpy

# Function to get all files with .jpg or .JPG extension recursively
def get_image_files(root_dir):
    image_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".JPG"):
                image_files.append(os.path.join(root, file))
    return image_files

# Get all image files recursively
dir_image_files = get_image_files('.')

dir_exif_list = []

for image_file_path in dir_image_files:
    with open(image_file_path, 'rb') as image_file:
        my_image = Image(image_file)
        if my_image.has_exif:
            data_list = [image_file_path]

            try:
                load_data = my_image.exposure_time
            except:
                load_data = ""
            data_list.append(load_data)

            try:
                load_data = my_image.f_number
            except:
                load_data = ""
            data_list.append(load_data)

            try:
                load_data = my_image.photographic_sensitivity
            except:
                load_data = ""
            data_list.append(load_data)

            try:
                load_data = my_image.datetime_original
            except:
                load_data = ""
            data_list.append(load_data)
            print(data_list)
            dir_exif_list.append(data_list)
        else:
            print("No exif found in:", image_file_path)

data_array = numpy.array(dir_exif_list)
numpy.savetxt("data.csv", data_array, delimiter=",", fmt="%s")
print("Data saved.")
