import os
import sys
import subprocess
import glob
import argparse

def convert_images_to_webp(target_dir, quality=70, remove_original=False):
    # 対象の拡張子
    extensions = (".png", ".jpg", ".jpeg")

    # 再帰的に検索
    for ext in extensions:
        for input_path in glob.glob(os.path.join(target_dir, "**", f"*{ext}"), recursive=True):
            output_path = os.path.splitext(input_path)[0] + ".webp"

            # 既に .webp が存在する場合はスキップ
            if os.path.exists(output_path):
                print(f"⚠ {output_path} は既に存在します。スキップします。")
                continue

            cmd = [
                "cwebp",
                "-resize", "2000", "0",
                "-q", str(quality),
                "-m", "6",
                "-af",
                "-metadata", "none",
                input_path,
                "-o", output_path
            ]

            print(f"Converting: {input_path} -> {output_path}")
            subprocess.run(cmd, check=True)

            # 変換成功後に元ファイルを削除
            if remove_original:
                os.remove(input_path)
                print(f"🗑 元ファイルを削除しました: {input_path}")

    print("✅ 変換完了！")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="指定フォルダ内の画像を WebP に変換するスクリプト"
    )
    parser.add_argument("path", help="対象フォルダ")
    parser.add_argument("-q", "--quality", type=int, default=70, help="画質 (0-100, デフォルト: 70)")
    parser.add_argument("-r", "--remove", action="store_true", help="変換後に元ファイルを削除する")

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"エラー: {args.path} は存在しません。")
        sys.exit(1)

    convert_images_to_webp(args.path, args.quality, args.remove)
