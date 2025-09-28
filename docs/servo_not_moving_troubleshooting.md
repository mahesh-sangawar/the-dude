# 🔧 Servo Not Moving - Troubleshooting Guide

## 🎯 **Code Runs Successfully BUT Servo Doesn't Move**

This is a hardware/power issue, not a software problem. Let's diagnose step by step.

---

## 🔍 **Step 1: Power Verification**

### **Check Servo Power Supply**
```bash
# Use multimeter to measure voltage at servo:
Red probe → Servo RED wire
Black probe → Servo BROWN wire
Expected: 5.0V ± 0.2V

If NO voltage or LOW voltage:
❌ Power supply not connected properly
❌ Power supply not turned ON
❌ Breadboard connections loose
❌ Power supply insufficient capacity
```

### **Quick Power Tests**
```bash
1. Is power supply turned ON?
2. Is power supply LED lit (if it has one)?
3. Does multimeter show 5V at breadboard rails?
4. Does multimeter show 5V at servo red/brown wires?
```

---

## 🔌 **Step 2: Connection Verification**

### **Double-Check All Connections**
```
Servo 0 (Thumb) should be connected:
✅ Brown wire → Breadboard GND rail
✅ Red wire → Breadboard 5V rail
✅ Orange wire → GPIO board Pin 12

Power Bridge:
✅ Breadboard red rail → GPIO board Pin 2 (5V)
✅ Breadboard blue rail → GPIO board Pin 6 (GND)

Power Supply:
✅ Red wire → Breadboard red rail
✅ Black wire → Breadboard blue rail
```

### **Visual Inspection**
```bash
Look for:
❌ Loose jumper wire connections
❌ Wires not fully inserted into breadboard
❌ Wrong GPIO pin (should be Pin 12)
❌ Servo wires in wrong breadboard holes
❌ Power supply wires not connected
```

---

## 🧪 **Step 3: Quick Diagnostic Tests**

### **Test A: Check GPIO Pin Activity**
```bash
# Run this while servo test is running:
gpio readall | grep "12"

# Should show:
# 12 | 1 | ALT0 | 0 | GPIO. 12 | 32 |

# If it shows different values, GPIO 12 might not be working
```

### **Test B: LED Test (if available)**
```bash
# If you have an LED, test GPIO 12:
# Connect LED: Long leg → GPIO 12, Short leg → GND

# Run this simple test:
python3 -c "
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
for i in range(10):
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(12, GPIO.LOW)
    time.sleep(0.5)
GPIO.cleanup()
"

# LED should blink if GPIO 12 works
```

### **Test C: Different GPIO Pin**
```bash
# Try moving servo orange wire to GPIO 13
# Modify test to use GPIO 13:

# Edit the servo driver temporarily
# Or run quick test:
python3 -c "
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
pwm = GPIO.PWM(13, 50)
pwm.start(7.5)
time.sleep(1)
pwm.ChangeDutyCycle(5)
time.sleep(1)
pwm.ChangeDutyCycle(10)
time.sleep(1)
pwm.stop()
GPIO.cleanup()
"
```

---

## ⚡ **Step 4: Power Supply Issues**

### **Common Power Problems**
```
Problem: Insufficient Current
- SG90 servo needs ~250mA when moving
- Weak power supplies can't provide enough current
- Voltage drops under load

Solutions:
✅ Use 5V 2A+ power supply (not 1A)
✅ Check power supply specifications
✅ Try different power supply if available
✅ Use USB power bank (usually 2A+)
```

### **Power Supply Alternatives to Try**
```bash
Option A: USB Power Bank
- Most provide 2A+ current
- Connect USB → 5V converter → breadboard

Option B: Computer USB Port
- Some provide enough power for single servo
- USB → breadboard adapter

Option C: Pi GPIO Power
- ONLY for testing, not recommended
- Use Pi's 5V pin (very limited current)
```

---

## 🔧 **Step 5: Servo Issues**

### **Test Servo Directly**
```bash
# Connect servo directly to known good power:
# Red → 5V power supply positive
# Brown → 5V power supply negative
# Orange → GPIO 12

# If servo still doesn't move with direct power:
❌ Servo may be defective
❌ Servo may be mechanically bound
❌ Wrong servo type (not standard SG90)
```

### **Servo Mechanical Check**
```bash
1. Can you turn servo shaft by hand?
   - Should have slight resistance
   - Should not be completely locked
   - Should not spin freely

2. Is servo horn attached?
   - Remove servo horn for testing
   - Servo should move without load

3. Listen for servo sounds:
   - Working servo makes quiet whirring sound
   - Bound servo makes clicking/grinding sound
   - Dead servo makes no sound
```

---

## 🎯 **Quick Diagnostic Sequence**

### **5-Minute Quick Test**
```bash
1. Measure voltage at servo (should be 5V)
2. Check all wire connections visually
3. Try different servo if available
4. Test GPIO 12 with LED (if available)
5. Try different GPIO pin (13, 16, etc.)
```

### **Most Likely Causes (in order)**
```
1. 🔋 Power supply not providing enough current
2. 🔌 Loose wire connections (especially power)
3. ⚡ Power supply not turned on or connected
4. 🎯 Wrong GPIO pin connection
5. 🤖 Defective servo
6. 📊 GPIO not enabled properly
```

---

## 🚀 **Quick Fixes to Try Now**

### **Fix 1: Power Supply Check**
```bash
# Ensure power supply is:
✅ Plugged in and ON
✅ Connected to breadboard
✅ Showing 5V on multimeter
✅ Rated for 2A+ current
```

### **Fix 2: Re-seat All Connections**
```bash
# Remove and reconnect:
✅ All servo wires to breadboard
✅ Power bridge wires to GPIO board
✅ Power supply to breadboard
✅ Servo orange wire to GPIO pin 12
```

### **Fix 3: Try Sudo**
```bash
# Run test with elevated permissions:
sudo python3 test_servo.py
```

### **Fix 4: Enable Hardware PWM**
```bash
# Add to /boot/config.txt:
sudo nano /boot/config.txt
# Add line: dtoverlay=pwm,pin=12,func=4
# Reboot: sudo reboot
```

---

## 📊 **Expected Results**

### **When Power is Correct:**
- Servo should make quiet whirring sound
- Servo shaft should move to commanded positions
- No error messages in software

### **When Power is Wrong:**
- Complete silence from servo
- No movement at all
- Software runs fine but no physical response

---

## 🎯 **Next Steps**

### **If Still No Movement:**
1. **Verify 5V at servo connections** (most critical)
2. **Try different servo** (rule out defective unit)
3. **Use different GPIO pin** (rule out pin problem)
4. **Check power supply amperage** (needs 2A+)

### **If You Get Movement:**
🎉 **Success!** You can then:
- Add second servo
- Test multi-servo operation
- Proceed with mechanical integration

**Start with checking the power supply - that's the #1 cause of "software works but servo doesn't move" issues!** ⚡🔧