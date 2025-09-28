# 🐍 Python Environment Setup - Fix "Externally Managed" Error

## 🚨 **The Problem**
Newer Raspberry Pi OS versions prevent installing packages globally to protect the system Python environment.

**Error Message:**
```
error: externally-managed-environment
This environment is externally managed
```

---

## ✅ **Solution Options (Choose One)**

### **Option A: Use Virtual Environment (Recommended)**
```bash
# 1. Create virtual environment
python3 -m venv dude-env

# 2. Activate virtual environment
source dude-env/bin/activate

# 3. Install packages in virtual environment
pip install RPi.GPIO

# 4. Install project requirements
pip install -r requirements.txt

# 5. Run tests (while virtual environment is active)
python test_servo.py
```

### **Option B: Use --break-system-packages (Quick Fix)**
```bash
# Install GPIO library
pip3 install RPi.GPIO --break-system-packages

# Install requirements
pip3 install -r requirements.txt --break-system-packages
```

### **Option C: Use apt packages (System Method)**
```bash
# Install GPIO through system package manager
sudo apt update
sudo apt install python3-rpi.gpio python3-pip

# Try installing other requirements
pip3 install -r requirements.txt --break-system-packages
```

---

## 🎯 **Recommended: Virtual Environment Method**

### **Complete Setup Steps:**
```bash
# 1. Navigate to project directory
cd /home/pi/the-dude

# 2. Create virtual environment
python3 -m venv dude-env

# 3. Activate virtual environment
source dude-env/bin/activate

# You should see (dude-env) at start of prompt

# 4. Upgrade pip in virtual environment
pip install --upgrade pip

# 5. Install GPIO library
pip install RPi.GPIO

# 6. Install other requirements
pip install -r requirements.txt

# 7. Test GPIO import
python -c "import RPi.GPIO; print('GPIO library working!')"

# 8. Run servo test
python test_servo.py
```

### **Every Time You Want to Use the Project:**
```bash
# Navigate to project
cd /home/pi/the-dude

# Activate virtual environment
source dude-env/bin/activate

# Now you can run tests
python test_servo.py
```

### **To Deactivate Virtual Environment:**
```bash
deactivate
```

---

## 🚀 **Quick Start (If You Want Fast Results)**

### **Option B - Break System Packages:**
```bash
# Quick install (not recommended for production)
sudo apt install python3-rpi.gpio
pip3 install --break-system-packages -r requirements.txt

# Test immediately
cd /home/pi/the-dude
python3 test_servo.py
```

---

## 🔧 **Troubleshooting**

### **If Virtual Environment Doesn't Work:**
```bash
# Install venv if missing
sudo apt install python3-venv

# Try creating virtual environment again
python3 -m venv dude-env
```

### **If GPIO Still Doesn't Work:**
```bash
# Install system GPIO package
sudo apt install python3-rpi.gpio

# Enable GPIO interface
sudo raspi-config
# Interface Options → GPIO → Enable

# Add user to gpio group
sudo usermod -a -G gpio pi

# Reboot
sudo reboot
```

### **If Requirements.txt Fails:**
```bash
# Install packages individually
pip install RPi.GPIO
# Skip other packages for now, focus on GPIO
```

---

## 📋 **Modified requirements.txt (Minimal)**

Create a simplified requirements.txt for testing:

```bash
# Create minimal requirements for testing
cat > requirements-minimal.txt << EOF
RPi.GPIO>=0.7.1
EOF

# Install minimal requirements
pip install -r requirements-minimal.txt
```

---

## 🎯 **Recommended Quick Fix for Testing**

```bash
# Option 1: System GPIO + break system packages
sudo apt install python3-rpi.gpio
pip3 install --break-system-packages psutil

# Option 2: Test GPIO immediately
cd /home/pi/the-dude
python3 -c "
import sys
sys.path.insert(0, '/usr/lib/python3/dist-packages')
import RPi.GPIO
print('GPIO working!')
"

# Run servo test
python3 test_servo.py
```

---

## ✅ **Which Method to Choose?**

### **For Quick Testing (Start Here):**
```bash
sudo apt install python3-rpi.gpio
cd /home/pi/the-dude
python3 test_servo.py
```

### **For Clean Development:**
Use virtual environment method above.

### **For Production:**
Use proper virtual environment with all packages.

---

## 🎯 **Bottom Line**

**For immediate servo testing:**
1. `sudo apt install python3-rpi.gpio`
2. `cd /home/pi/the-dude`
3. `python3 test_servo.py`

**The GPIO library from apt should be enough to get your servo moving!** 🤖