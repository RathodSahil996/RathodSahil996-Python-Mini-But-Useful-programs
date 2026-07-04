import os
import shutil
import argparse

# File type mapping
File_type = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Document_Files": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Audio_Files": ['.mp3', '.wav', '.aac', '.flac'],
    "Video_Files": ['.mp4', '.avi', '.mkv', '.mov'],
    "Archive_Files": ['.zip', '.rar', '.tar', '.gz']
}


def organize_folder(folder_path, dry_run=False):
    """Organize files in `folder_path` into typed subfolders.

    If `dry_run` is True, only prints actions without moving files.
    """
    # Normalize path
    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Target folder does not exist: {folder_path}")

    # Create target folders if they don't exist
    for folder in File_type.keys():
        dest = os.path.join(folder_path, folder)
        if not os.path.exists(dest):
            if dry_run:
                print(f"[dry-run] would create folder: {dest}")
            else:
                os.makedirs(dest, exist_ok=True)

    # Organize files
    for name in os.listdir(folder_path):
        src_path = os.path.join(folder_path, name)

        # Skip directories
        if os.path.isdir(src_path):
            continue

        # Skip this script file if it's inside the target folder
        try:
            this_file = os.path.abspath(__file__)
        except NameError:
            this_file = None
        if this_file and os.path.abspath(src_path) == this_file:
            continue

        ext = os.path.splitext(name)[1].lower()
        moved = False
        for folder, extensions in File_type.items():
            if ext in extensions:
                dest_path = os.path.join(folder_path, folder, name)
                if dry_run:
                    print(f"[dry-run] would move: {src_path} -> {dest_path}")
                else:
                    shutil.move(src_path, dest_path)
                moved = True
                break

        if not moved and dry_run:
            print(f"[dry-run] no rule for: {src_path}")

    if dry_run:
        print("Dry run complete.")
    else:
        print("Files organized successfully!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize files in a folder by type. Defaults to your Downloads folder.')
    parser.add_argument('--path', '-p', help='Target folder path (default: Downloads)',
                        default=os.path.join(os.path.expanduser('~'), 'Downloads'))
    parser.add_argument('--dry-run', action='store_true', help='Show actions without moving files')
    args = parser.parse_args()

    try:
        organize_folder(args.path, dry_run=args.dry_run)
    except Exception as e:
        print(f"Error: {e}")