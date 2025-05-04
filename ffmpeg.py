import os
import sys
import platform
import urllib.request
import zipfile
import tarfile
import stat
import shutil
from pathlib import Path

def get_ffmpeg_path():
    base_dir = Path(os.path.dirname(sys.argv[0])).resolve()
    system = platform.system()

    def cleanup_ffmpeg_dirs():
        for item in base_dir.iterdir():
            if item.is_dir() and item.name.startswith("ffmpeg-"):
                try:
                    shutil.rmtree(item)
                except Exception as e:
                    print(f"Failed to remove {item}: {e}")

    if system == "Windows":
        exe_name = "ffmpeg.exe"
        dest = base_dir / exe_name
        if dest.exists():
            return str(dest)

        print("Downloading FFmpeg for Windows...")
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        tmp_zip = base_dir / "ffmpeg_win.zip"
        urllib.request.urlretrieve(url, tmp_zip)

        with zipfile.ZipFile(tmp_zip, 'r') as zip_ref:
            zip_ref.extractall(base_dir)

        tmp_zip.unlink()

        # 探して移動
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.lower() == "ffmpeg.exe":
                    src = Path(root) / file
                    shutil.move(str(src), dest)
                    break

        cleanup_ffmpeg_dirs()
        return str(dest)

    elif system == "Darwin":
        exe_name = "ffmpeg"
        dest = base_dir / exe_name
        if dest.exists():
            return str(dest)

        print("Downloading FFmpeg for macOS...")
        url = "https://evermeet.cx/ffmpeg/getrelease/zip"
        tmp_zip = base_dir / "ffmpeg_mac.zip"
        urllib.request.urlretrieve(url, tmp_zip)

        with zipfile.ZipFile(tmp_zip, 'r') as zip_ref:
            zip_ref.extractall(base_dir)

        tmp_zip.unlink()

        if dest.exists():
            os.chmod(dest, os.stat(dest).st_mode | stat.S_IEXEC)
            return str(dest)

        for ff in base_dir.glob("ffmpeg*"):
            if ff.is_file():
                os.chmod(ff, os.stat(ff).st_mode | stat.S_IEXEC)
                return str(ff)

        raise FileNotFoundError("FFmpeg not found after extraction.")

    elif system == "Linux":
        exe_name = "ffmpeg"
        dest = base_dir / exe_name
        if dest.exists():
            return str(dest)

        print("Downloading FFmpeg for Linux...")
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        tmp_tar = base_dir / "ffmpeg_linux.tar.xz"
        urllib.request.urlretrieve(url, tmp_tar)

        with tarfile.open(tmp_tar, "r:xz") as tar_ref:
            folder_name = None
            for member in tar_ref.getmembers():
                if member.name.endswith("/ffmpeg"):
                    folder_name = member.name.split("/")[0]
                    member.name = os.path.basename(member.name)
                    tar_ref.extract(member, base_dir)
                    ffmpeg_path = base_dir / member.name
                    ffmpeg_path.rename(dest)
                    os.chmod(dest, os.stat(dest).st_mode | stat.S_IEXEC)
                    break

        tmp_tar.unlink()
        cleanup_ffmpeg_dirs()
        return str(dest)

    else:
        raise OSError(f"Unsupported OS: {system}")
