import os
import argparse

def change_file_extensions(root_folder, old_extension, new_extension):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(old_extension):
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, filename.rsplit('.', 1)[0] + new_extension)
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Change file extensions in a directory and its subdirectories.')
    parser.add_argument('root_folder', help='The root folder path; Be sure to use quotes if using a single backslash Windows path (e.g., C:\\My\\Folder)')
    parser.add_argument('old_extension', help='The old file extension (e.g., .txt)')
    parser.add_argument('new_extension', help='The new file extension (e.g., .md)')

    args = parser.parse_args()

    # Normalize the root folder path
    root_folder = os.path.normpath(args.root_folder)

    print(f'Checking in root_folder: {root_folder}')
    
    change_file_extensions(root_folder, args.old_extension, args.new_extension)

# e.g., python change_extension.py C:\Audiobooks .m4b .mp4