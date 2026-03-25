import re
from pathlib import Path
from sys import argv
from os import path
from time import sleep
import Convert_webp
# 対象拡張子
EXTENSIONS = (".jpg", ".jpeg", ".png", ".JPG")

# Markdown画像 ![alt](path)
md_pattern = re.compile(r'(!\[[^\]]*\]\()([^)]+)(\))')

# HTML imgタグ <img src="path">
html_pattern = re.compile(r'(<img[^>]*src=["\'])([^"\']+)(["\'])')

def replace_ext(path: str) -> str:
    for ext in EXTENSIONS:
        if path.lower().endswith(ext):
            return path[: -len(ext)] + ".webp"
    return path


def process_file(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    # Markdown画像
    def md_replacer(match):
        prefix, path, suffix = match.groups()
        return prefix + replace_ext(path) + suffix

    text = md_pattern.sub(md_replacer, text)

    # HTML img
    def html_replacer(match):
        prefix, path, suffix = match.groups()
        return prefix + replace_ext(path) + suffix

    text = html_pattern.sub(html_replacer, text)

    file_path.write_text(text, encoding="utf-8")
    print(f"Processed: {file_path}")


def main():
    print("Processing...")
    sleep(1)
    args=argv
    TARGET_DIR=args[1]
    print(TARGET_DIR)
    if not path.isdir(TARGET_DIR):
        print(f"ERROR {TARGET_DIR} can not found!")
    else:
        print("Starting Convert webp...")
        sleep(1)
        Convert_webp.convert_images_to_webp(TARGET_DIR,80,True)
        print("done!")
        print("Starting markdowns filename...")
        sleep(1)
        TARGET_DIR=Path(TARGET_DIR)
        for md_file in TARGET_DIR.rglob("*.md"):
            process_file(md_file)
        print("done!")


if __name__ == "__main__":
    main()