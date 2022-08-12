import json
import os
import glob
import shutil

# orig_files = glob.glob("TuSimple/train_set/*json")
# for file in orig_files:
#     f = json.loads(open(file).readline())
#     print(f.keys())
#     break

synth_dataset_path = "Simulanes/WATO_TuSimple/"
files = glob.glob(synth_dataset_path + "*json")
img_files = glob.glob(synth_dataset_path + "*jpg")

destination = "TuSimple/train_set/clips/wato/"

if not os.isdir(destination + "clips/wato/"):
    os.mkdir(destination + "clips/wato/")

with open('TuSimple/train_set/train_data_16344.json', "w") as write_file:
    for i, (file, img_file) in enumerate(zip(files, img_files)):
        folder_name = os.path.basename(file).split(".json")[0] + "/"
        new_img_file = "clips/wato/" + folder_name + "/20.jpg"

        f = json.load(open(file))
        f["raw_file"] = new_img_file
        del f["classes"]

        json_obj = json.dumps(f)

        os.mkdir(destination + folder_name)

        # for j in range(20):
            # shutil.copy(img_file, destination + folder_name + str(j + 1) + ".jpg")

        shutil.copy(img_file, destination + folder_name + "20.jpg")

        write_file.write(json_obj)
        write_file.write("\n")

        print("Copied {}/{} files".format(i + 1, len(files)))
