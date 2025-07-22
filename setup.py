#!/usr/bin/env python3
"""
Setup script for Marriage Vendors Test Automation
This script helps users set up the testing environment quickly.
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Print setup banner"""
    print("=" * 60)
    print("  Marriage Vendors - Test Automation Setup")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print("📋 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    print()

def create_virtual_environment():
    """Create virtual environment"""
    print("🔧 Creating virtual environment...")
    try:
        if not os.path.exists("env"):
            subprocess.run([sys.executable, "-m", "venv", "env"], check=True)
            print("✅ Virtual environment created successfully")
        else:
            print("✅ Virtual environment already exists")
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    print()

def get_activation_command():
    """Get the virtual environment activation command based on OS"""
    system = platform.system().lower()
    if system == "windows":
        return ".\\env\\Scripts\\Activate.ps1"
    else:
        return "source env/bin/activate"

def install_dependencies():
    """Install project dependencies"""
    print("📦 Installing dependencies...")
    try:
        # Determine pip path based on OS
        system = platform.system().lower()
        if system == "windows":
            pip_path = os.path.join("env", "Scripts", "pip.exe")
        else:
            pip_path = os.path.join("env", "bin", "pip")
        
        # Install requirements
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)
    print()

def verify_installation():
    """Verify that Selenium is properly installed"""
    print("🔍 Verifying installation...")
    try:
        # Determine python path based on OS
        system = platform.system().lower()
        if system == "windows":
            python_path = os.path.join("env", "Scripts", "python.exe")
        else:
            python_path = os.path.join("env", "bin", "python")
        
        # Check Selenium installation
        result = subprocess.run([
            python_path, "-c", 
            "import selenium; print('Selenium version:', selenium.__version__)"
        ], capture_output=True, text=True, check=True)
        
        print("✅", result.stdout.strip())
    except subprocess.CalledProcessError:
        print("❌ Failed to verify Selenium installation")
        sys.exit(1)
    print()

def print_usage_instructions():
    """Print usage instructions"""
    activation_cmd = get_activation_command()
    
    print("🎉 Setup completed successfully!")
    print()
    print("📖 Next Steps:")
    print("=" * 40)
    print(f"1. Activate virtual environment:")
    print(f"   {activation_cmd}")
    print()
    print("2. Run all tests:")
    print("   python -m unittest discover -s . -p \"test_*.py\" -v")
    print()
    print("3. Run individual test file:")
    print("   python test_1_user_authencation.py")
    print()
    print("4. Run specific test method:")
    print("   python -m unittest test_1_user_authencation.TestUserAuthentication.test_2_valid_login -v")
    print()
    print("📚 For more information, check the README.md file")
    print("=" * 60)

def main():
    """Main setup function"""
    print_banner()
    check_python_version()
    create_virtual_environment()
    install_dependencies()
    verify_installation()
    print_usage_instructions()

if __name__ == "__main__":
    main()
