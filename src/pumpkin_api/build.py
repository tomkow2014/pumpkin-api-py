import argparse
import subprocess
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Build a Pumpkin Python plugin")
    parser.add_argument("app_module", help="The python module containing the plugin (e.g. 'main')")
    parser.add_argument("-o", "--output", default="plugin.wasm", help="Output wasm file name")
    args = parser.parse_args()

    import pumpkin_api
    pkg_dir = os.path.dirname(pumpkin_api.__file__)
    wit_dir = os.path.join(pkg_dir, "wit_files")
    
    # Pass the parent directory of pumpkin_api to componentize-py so it can resolve `pumpkin_api` module
    # in case it's not installed in a standard site-packages (e.g. editable install or no venv)
    pkg_parent_dir = os.path.dirname(pkg_dir)

    cmd = [
        "componentize-py",
        "-d", wit_dir,
        "-w", "plugin",
        "componentize", args.app_module,
        "-o", args.output,
        "-p", ".",
        "-p", pkg_parent_dir
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
