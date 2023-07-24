#Extraction of titles and abstracts.
import os

folder_path = r'C:\Games\KSP\1.12.5 Stock\GameData\PhotonCorp\Parts\SpaceShuttleSRB'
field_name_1 = 'title'
field_name_2 = 'description'
field_name_3 = 'name'
output_file = 'en-us.cfg'

with open(output_file, 'w') as out:
    for dirpath, dirnames, filenames in os.walk(folder_path):
        folder_name = os.path.basename(dirpath)
        for filename in filenames:
            if filename.endswith('.cfg'):
                with open(os.path.join(dirpath, filename), 'r') as file:
                    found_field_1 = False
                    found_field_2 = False
                    found_field_3 = False
                    field_value_3 = ''
                    for line in file:
                        if field_name_1 in line:
                            field_value = line.split('=')[1].strip()
                            out.write(f'\t\t#LOC_{field_value_3}_title = {field_value}\n')
                            found_field_1 = True
                        if field_name_2 in line:
                            field_value = line.split('=')[1].strip()
                            out.write(f'\t\t#LOC_{field_value_3}_description = {field_value}\n\n')
                            found_field_2 = True
                        if field_name_3 in line:
                            field_value_3 = line.split('=')[1].strip()
                            found_field_3 = True
                        if found_field_1 and found_field_2 and found_field_3:
                            break


