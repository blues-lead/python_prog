import os

def fix_filenames(folder_name):
    os.chdir(folder_name)
    files = os.listdir()
    for line in files:
        if ".gif" in line:
            to_be_renamed = line
            pos = line.index(".gif")
            line = line[0:pos]
            parts = line.split("_")
            if not parts[0].isdigit() or len(parts) <= 2:
                continue
            new_name = parts[0]+".gif"
            #new_name = parts[2] + "-" + parts[1] + ".mp3"
            os.replace(to_be_renamed, new_name)
        else:
            continue

def main():
    folder = input("Enter folder name: ")
    fix_filenames(folder)

main()