"""
A module to retrieve and display kernel and environment information in Jupyter Notebooks.
"""

import sys
import platform
import subprocess
from importlib.metadata import version, distributions


def show_kernel_info():
    """
    Display basic information about the current Python kernel and environment.
    """
    print("=== Kernel Information ===")
    print(f"Python version: {sys.version}")
    print(f"Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")

    try:
        ipython_version = version("ipython")
        print(f"IPython version: {ipython_version}")
    except ImportError:
        print("IPython version: Not available (not running in IPython)")


def show_installed_packages():
    """
    List all installed Python packages and their versions.
    Uses importlib.metadata (Python 3.8+).
    """
    print("\n=== Installed Packages ===")
    try:
        for package in sorted(
            distributions(), key=lambda x: x.metadata["Name"].lower()
        ):
            print(f"{package.metadata['Name']}: {package.version}")
    except ImportError:
        print("importlib.metadata not available (Python < 3.8).")
    except Exception as e:
        print(f"Could not retrieve installed packages: {e}")


def show_system_info():
    """
    Display system and hardware information.
    """
    print("\n=== System Information ===")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")

    if platform.system() == "Linux":
        try:
            mem_info = subprocess.check_output(["free", "-h"]).decode().strip()
            print("\nMemory Info:\n" + mem_info)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Memory info: Not available")


def show_all_info():
    """
    Combine all kernel, package, and system information into a single output.
    """
    show_kernel_info()
    show_installed_packages()
    show_system_info()


if __name__ == "__main__":
    print("This module is meant to be imported in a Jupyter Notebook or Python script.")
