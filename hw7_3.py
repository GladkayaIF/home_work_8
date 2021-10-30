
import os
path_read = "C:/Users/axata/PycharmProjects/pythonProject/3"
path_write = "C:/Users/axata/PycharmProjects/pythonProject/res"
file_list = []
for root, dirs, files in os.walk(path_read):
    for file in files:
        file_list.append(os.path.join(root, file))


data = {}
for name in file_list:
    count = 0
    temp_data = ()
    data_file = ''

    with open(name, encoding="utf8") as f:
        for line in f:
            count += 1
            data_file += line

    temp_data = (count, data_file)
    path_dir, name_dir = name.split('\\')
    data[name_dir] = temp_data


sorted_values = sorted(data.values())
sorted_dict = {}

for i in sorted_values:
    for k in data.keys():
        if data[k] == i:
            sorted_dict[k] = data[k]
            break


name_write = path_write + '/new.txt'
with open(name_write, mode='w', encoding="utf8") as f:
    for k in sorted_dict:
        f.writelines(k + '\n')
        for v in sorted_dict[k]:
            f.writelines(str(v) + '\n')
    f.close()