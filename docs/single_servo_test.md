# 🧪 Single Servo Test Setup

## 🎯 **Test ONE Servo First - Smart Approach!**

Testing with a single servo first is the best way to verify your setup works before connecting all 5. Much easier to troubleshoot!

---

## 🔌 **Minimal Hardware Setup**

### **What You Need:**
- [ ] Pi Zero W + GPIO board (assembled)
- [ ] 5V power supply
- [ ] **ONE SG90 servo only**
- [ ] 3 jumper wires (for servo connections)

### **Single Servo Connection:**
```
Connect ONLY Servo 0 (Thumb):

Servo Wire → GPIO Board Terminal
├── Brown wire → GND terminal
├── Red wire → 5V terminal
└── Orange wire → GPIO 12 terminal

Power Supply:
├── Red wire → GPIO board 5V terminal
└── Black wire → GPIO board GND terminal
```

---

## 💻 **Software Setup**

### **1. Navigate to Project Directory**
```bash
cd /home/pi/the-dude
```

### **2. Verify Files Exist**
```bash
ls -la

# You should see:
# test_servo.py
# src/servo_control/servo_driver.py
# config/servo_config.json
```

### **3. Test GPIO Library**
```bash
python3 -c "import RPi.GPIO; print('GPIO library working!')"

# Should print: GPIO library working!
# If error, run: pip3 install RPi.GPIO
```

---

## 🧪 **Single Servo Testing**

### **Test 1: Basic Movement**
```bash
python3 test_servo.py

# Expected output:
🤖 DUDE Servo Test - Starting...
📋 This will test Servo 0 (Thumb CMC) on GPIO pin 12
⚠️  Make sure servo is connected to GPIO 12, 5V, and GND
🛑 Press Ctrl+C to stop at any time

🧪 Test 1: Basic Movement Test
   Moving servo to center position (45°)...
   [SERVO SHOULD MOVE HERE]
   Moving to fully opposed position (90°)...
   [SERVO SHOULD MOVE HERE]
   Moving to relaxed position (0°)...
   [SERVO SHOULD MOVE HERE]

✅ All tests completed successfully!
```

### **Test 2: Interactive Control**
```bash
python3 test_servo.py
# When prompted, select: 2

# Try these commands:
🤖 Enter command: 45      # Move to 45 degrees
🤖 Enter command: 0       # Move to 0 degrees
🤖 Enter command: 90      # Move to 90 degrees
🤖 Enter command: status  # Show status
🤖 Enter command: quit    # Exit
```

---

## ✅ **Success Criteria for Single Servo**

### **What Should Happen:**
```
✅ Servo moves smoothly to each position
✅ No jittery or erratic movement
✅ Servo stops precisely at commanded angles
✅ No overheating during test
✅ Interactive commands respond immediately
✅ Emergency stop (Ctrl+C) works
✅ Program exits cleanly
```

### **What Should NOT Happen:**
```
❌ No movement at all
❌ Jittery, shaking movement
❌ Servo gets hot quickly
❌ Program crashes with errors
❌ Smoke or burning smell
❌ Unusual clicking/grinding sounds
```

---

## 🔧 **Single Servo Troubleshooting**

### **Problem: No Movement**
```bash
Diagnosis Steps:
1. Check power supply is ON
2. Measure voltage at servo:
   - Red wire should show 5.0V to brown wire
3. Verify connections:
   - Orange wire on GPIO 12
   - Brown wire on GND
   - Red wire on 5V

Solutions:
✅ Run with sudo: sudo python3 test_servo.py
✅ Enable GPIO: sudo raspi-config → Interface → GPIO → Enable
✅ Check servo by swapping with known good servo
✅ Try different GPIO pin (change code to use GPIO 13)
```

### **Problem: Jittery Movement**
```bash
Causes & Solutions:
✅ Insufficient power supply (upgrade to 3A minimum)
✅ Loose connections (tighten all connections)
✅ Bad jumper wires (try different wires)
✅ WiFi interference (try ethernet connection)
✅ Add capacitor across power rails (100-1000μF)
```

### **Problem: Permission Errors**
```bash
Error: "RuntimeError: No access to /dev/mem"

Solutions:
✅ Run with sudo: sudo python3 test_servo.py
✅ Add user to gpio group: sudo usermod -a -G gpio pi
✅ Reboot after group change: sudo reboot
✅ Check GPIO is enabled in raspi-config
```

---

## 🎯 **Quick Test Commands**

### **Rapid Verification Test:**
```bash
# Single command test (if basic test works):
cd /home/pi/the-dude
python3 -c "
from src.servo_control.servo_driver import ServoDriver
import time
driver = ServoDriver()
driver.start()
driver.set_servo_position(0, 90)
time.sleep(2)
driver.set_servo_position(0, 0)
time.sleep(2)
driver.stop()
print('Single servo test complete!')
"
```

### **GPIO Pin Verification:**
```bash
# Check if GPIO 12 is available:
gpio readall | grep "12"

# Should show GPIO 12 as available
```

---

## 📊 **Once Single Servo Works:**

### **You're Ready For:**
```
✅ Connect second servo (Index finger - GPIO 13)
✅ Test with 2 servos
✅ Gradually add remaining servos (one at a time)
✅ Run full 5-servo tests
✅ Begin mechanical integration planning
```

### **Confidence Gained:**
```
✅ Power supply is adequate
✅ GPIO board connections work
✅ Software setup is correct
✅ Pi GPIO functionality verified
✅ Servo compatibility confirmed
✅ Ready for full system
```

---

## 🚨 **Safety Notes for Single Servo Test**

### **Power Safety:**
```
⚠️ Even with one servo:
- Monitor servo temperature
- Have emergency power disconnect ready
- Don't leave running unattended
- Stop if anything seems wrong
```

### **Mechanical Safety:**
```
⚠️ Keep servo free to move:
- Don't hold servo shaft while testing
- Ensure servo horn isn't hitting anything
- Listen for binding or strain sounds
- Stop if servo seems to struggle
```

---

## 🎯 **Expected Timeline**

### **Single Servo Test Session:**
```
Setup time: 5 minutes
- Connect one servo
- Verify connections
- Power on system

Testing time: 10 minutes
- Run basic movement test
- Try interactive commands
- Verify smooth operation

Troubleshooting: 0-15 minutes
- Fix any issues found
- Verify stable operation
- Document any adjustments

Total: 15-30 minutes for single servo verification
```

**Once this single servo test works perfectly, you'll have confidence that your setup is correct and ready for the full 5-servo system!** 🎉