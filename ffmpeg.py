import os
import platform
import urllib.request
import zipfile
import tarfile
import stat
import shutil
from pathlib import Path

def get_ffmpeg_path():
    system = platform.system()
    arch = platform.machine().lower()
    base_dir = Path(__file__).parent.resolve()

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
            for file in zip_ref.namelist():
                if file.endswith("ffmpeg.exe"):
                    zip_ref.extract(file, base_dir)
                    src = base_dir / file
                    shutil.move(src, dest)
                    break
        tmp_zip.unlink()
        return str(dest)

    elif system == "Darwin":
        exe_name = "ffmpeg"
        cache_dir = Path.home() / ".cache" / "ffmpeg"
        cache_dir.mkdir(parents=True, exist_ok=True)
        dest = cache_dir / exe_name
        if dest.exists():
            return str(dest)
        print("Downloading FFmpeg for macOS...")
        url = "https://evermeet.cx/ffmpeg/getrelease/zip"
        tmp_zip = cache_dir / "ffmpeg_mac.zip"
        urllib.request.urlretrieve(url, tmp_zip)
        with zipfile.ZipFile(tmp_zip, 'r') as zip_ref:
            zip_ref.extractall(cache_dir)
        os.chmod(dest, os.stat(dest).st_mode | stat.S_IEXEC)
        tmp_zip.unlink()
        return str(dest)

    elif system == "Linux":
        exe_name = "ffmpeg"
        cache_dir = Path.home() / ".cache" / "ffmpeg"
        cache_dir.mkdir(parents=True, exist_ok=True)
        dest = cache_dir / exe_name
        if dest.exists():
            return str(dest)
        print("Downloading FFmpeg for Linux...")
        url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
        tmp_tar = cache_dir / "ffmpeg_linux.tar.xz"
        urllib.request.urlretrieve(url, tmp_tar)
        with tarfile.open(tmp_tar, "r:xz") as tar_ref:
            for member in tar_ref.getmembers():
                if member.name.endswith("/ffmpeg"):
                    member.name = os.path.basename(member.name)
                    tar_ref.extract(member, cache_dir)
                    break
        os.chmod(dest, os.stat(dest).st_mode | stat.S_IEXEC)
        tmp_tar.unlink()
        return str(dest)

    else:
        raise OSError("Unsupported OS")

# 使用例:
if __name__ == "__main__":
    ffmpeg_path = get_ffmpeg_path()
    print("Using FFmpeg at:", ffmpeg_path)
