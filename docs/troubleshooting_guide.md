# 🔧 DUDE Hand Troubleshooting Guide

## 🚨 **Quick Emergency Fixes**

### **🔥 IMMEDIATE STOP CONDITIONS**
```bash
STOP EVERYTHING if you see/smell:
❌ Smoke from any component
❌ Burning smell
❌ Sparks or unusual sounds
❌ Servo getting very hot
❌ Power supply getting very hot

Emergency Action:
1. Power OFF 5V supply immediately
2. Disconnect all servo wires
3. Let everything cool down
4. Check all connections before retry
```

---

## ⚡ **Power & Electrical Issues**

### **Problem: No Movement at All**
```bash
Symptoms: Servos don't move, no response

Diagnosis Steps:
1. Check power supply voltage:
   multimeter → should read 5.0V ± 0.2V

2. Check Pi GPIO voltage:
   GPIO Pin 2 → should read 5.0V
   GPIO Pin 6 → should read 0V (ground)

3. Check servo power:
   Servo red wire → should read 5.0V to ground

4. Check signal connections:
   Verify GPIO pin numbers match code

Solutions:
✅ Ensure 5V power supply is ON
✅ Check all wire connections
✅ Verify breadboard power rails are connected
✅ Try different GPIO pins
✅ Test with single servo first
```

### **Problem: Jittery/Erratic Movement**
```bash
Symptoms: Servo shakes, inconsistent positioning

Most Common Cause: Insufficient power

Solutions:
✅ Upgrade to higher capacity power supply (5A vs 3A)
✅ Check for loose connections
✅ Ensure common ground between Pi and servos
✅ Add capacitor across power rails (1000μF, 16V)
✅ Use shorter, thicker wires for power
✅ Test with fewer servos simultaneously

Advanced Solutions:
✅ Add dedicated servo power supply
✅ Use PCA9685 controller for stable timing
✅ Check for WiFi interference (use ethernet)
```

### **Problem: Servo Overheating**
```bash
Symptoms: Servo hot to touch, reduced performance

Causes:
❌ Excessive load (mechanical binding)
❌ Voltage too high (>6V)
❌ Continuous stall condition
❌ Poor ventilation

Solutions:
✅ Check mechanical freedom (no binding)
✅ Verify 5V supply (not 6V or higher)
✅ Add servo cooling (small fan)
✅ Reduce duty cycle (add delays)
✅ Check for cable tension issues
```

---

## 💻 **Software Issues**

### **Problem: "RPi.GPIO not available" Error**
```bash
Error Message: "RPi.GPIO not available - running in simulation mode"

Solutions:
✅ Install GPIO library: pip3 install RPi.GPIO
✅ Enable GPIO in raspi-config
✅ Run with sudo: sudo python3 test_servo.py
✅ Check Pi user permissions: sudo usermod -a -G gpio pi
✅ Reboot Pi after GPIO changes
```

### **Problem: "Permission denied" Errors**
```bash
Error accessing GPIO pins

Solutions:
✅ Run with sudo: sudo python3 test_servo.py
✅ Add user to gpio group: sudo usermod -a -G gpio $USER
✅ Logout and login again
✅ Check GPIO permissions: ls -l /dev/gpiomem
```

### **Problem: Program Crashes or Freezes**
```bash
Symptoms: Python script stops responding

Common Causes & Solutions:
✅ Memory issue: Use lighter OS (Raspberry Pi OS Lite)
✅ GPIO conflict: sudo pkill -f gpio (kill other GPIO programs)
✅ Infinite loop: Add proper error handling
✅ Hardware fault: Check connections, power supply
✅ SD card corruption: Try fresh SD card
```

### **Problem: Gestures Don't Look Right**
```bash
Symptoms: Movements don't match expected gestures

Diagnosis:
1. Test individual servos first
2. Check servo directions (some may be reversed)
3. Verify cable routing and tension
4. Check mechanical constraints

Solutions:
✅ Adjust angles in config/5_servo_config.json
✅ Calibrate each servo individually
✅ Check servo horn orientation
✅ Verify mechanical range of motion
✅ Add software position limits
```

---

## 🔌 **Connection Issues**

### **Problem: Specific Servo Not Working**
```bash
Symptoms: One servo doesn't respond

Diagnosis Steps:
1. Swap servo to working GPIO pin
2. Test servo on different power source
3. Check signal wire continuity
4. Verify servo isn't damaged

Solutions:
✅ Replace faulty servo
✅ Check/replace signal wire
✅ Try different GPIO pin
✅ Verify breadboard connections
✅ Test servo with multimeter (should draw 10-20mA idle)
```

### **Problem: Intermittent Connections**
```bash
Symptoms: Sometimes works, sometimes doesn't

Common Causes:
❌ Loose breadboard connections
❌ Worn jumper wires
❌ Poor solder joints
❌ Vibration loosening connections

Solutions:
✅ Use higher quality jumper wires
✅ Solder connections for permanence
✅ Secure all connections with tape/clips
✅ Check connections after each test
✅ Use breadboard with tight connections
```

---

## 🤖 **Mechanical Issues**

### **Problem: Limited Range of Motion**
```bash
Symptoms: Servo stops before expected angle

Causes & Solutions:
✅ Cable too tight: Adjust tension
✅ Mechanical binding: Check joint freedom
✅ Servo horn hitting obstacle: Reposition
✅ Software limits too conservative: Adjust config
✅ Servo damaged: Replace servo
```

### **Problem: Servo Direction Reversed**
```bash
Symptoms: Servo moves opposite to expected direction

Solutions:
✅ Flip servo horn 180 degrees
✅ Reverse cable routing direction
✅ Adjust software angle mapping
✅ Use opposite signal logic in code
✅ Check mechanical cable path
```

---

## 📊 **Testing & Validation Issues**

### **Problem: Test Scripts Don't Run**
```bash
Error: Module not found, import errors

Solutions:
✅ Check Python path: export PYTHONPATH=/home/pi/the-dude
✅ Install dependencies: pip3 install -r requirements.txt
✅ Run from correct directory: cd /home/pi/the-dude
✅ Check file permissions: chmod +x test_*.py
✅ Use Python 3: python3 (not python)
```

### **Problem: Interactive Mode Not Responding**
```bash
Symptoms: Commands don't work in interactive mode

Solutions:
✅ Check spelling of commands
✅ Use lowercase: gesture (not Gesture)
✅ Verify gesture names: gestures command
✅ Check servo status: status command
✅ Emergency stop may be active: restart program
```

---

## 🔍 **Diagnostic Tools**

### **Hardware Diagnostic Commands**
```bash
# Check GPIO state
gpio readall

# Monitor system resources
htop

# Check USB power
vcgencmd get_throttled

# Test individual pins
gpio mode 12 out
gpio write 12 1
gpio write 12 0
```

### **Software Debug Mode**
```bash
# Run with debug output
python3 -u test_servo.py 2>&1 | tee debug.log

# Check system logs
sudo journalctl -u ssh
dmesg | tail -20

# Monitor power
vcgencmd measure_volts
```

---

## 📋 **Systematic Troubleshooting Process**

### **Step 1: Isolate the Problem**
```bash
1. Does the problem happen with:
   - Single servo? → Hardware issue
   - All servos? → Power/software issue
   - Specific gesture? → Configuration issue
   - Random times? → Connection issue

2. When does it happen:
   - At startup? → Initialization problem
   - After running? → Overheating/power
   - Specific command? → Software bug
   - After time? → Connection degradation
```

### **Step 2: Systematic Testing**
```bash
1. Test with minimal setup:
   - Single servo only
   - Simple test script
   - Known good power supply
   - Direct GPIO connection

2. Add complexity gradually:
   - Add one servo at a time
   - Test each addition
   - Monitor power consumption
   - Check for interference
```

### **Step 3: Document and Fix**
```bash
1. Record what works:
   - Working configurations
   - Stable power levels
   - Good cable routing

2. Document fixes:
   - What was the problem?
   - What solved it?
   - How to prevent it?
```

---

## 🆘 **When to Ask for Help**

### **Hardware Issues Beyond Basic Troubleshooting**
- Repeated component failures
- Unexplained power issues
- Complex electrical problems
- Safety concerns

### **Software Issues Beyond Documentation**
- Complex Python errors
- GPIO driver problems
- Performance optimization
- Advanced feature implementation

---

## 🎯 **Prevention is Better Than Fixing**

### **Best Practices to Avoid Problems**
```bash
✅ Always test single servo first
✅ Use quality power supply with margin
✅ Make solid connections (solder when possible)
✅ Monitor temperatures during testing
✅ Keep spare servos and wires
✅ Document working configurations
✅ Take photos of working setups
✅ Start simple, add complexity gradually
✅ Regular system backups
✅ Use version control for code changes
```

### **Maintenance Schedule**
```bash
Daily (during active development):
- Check connection tightness
- Monitor servo temperatures
- Verify power supply voltage

Weekly:
- Clean dust from components
- Check for wire wear
- Backup code changes

Monthly:
- Full system test
- Replace worn components
- Update documentation
```

Remember: **Most issues are simple connection or power problems!** Start with the basics before diving into complex solutions. 🔧