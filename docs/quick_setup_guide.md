# 🤖 DUDE Hand - Quick Setup Guide

## 🎯 **Super Simple Summary**

### **🔌 WIRING (Connect everything first):**
1. **Power**: Supply → GPIO board directly
2. **5 Servos**: All to GPIO board (pins 12,13,16,19,20)
3. **Check**: All connections solid, power OFF

### **💻 TESTING (Run programs):**
1. **Power ON**, boot Pi
2. **Test 1**: `python3 test_servo.py` (single servo)
3. **Test 2**: `python3 test_5_servos.py` → option 1 (all servos)
4. **Test 3**: `python3 test_5_servos.py` → option 2 (gestures)

### **🎉 SUCCESS:**
✅ All servos move
✅ Gestures work
✅ Hand responds to commands

**Total time: ~25 minutes from wires to working robotic hand!** 🤖✋

---

## 📦 **Materials Checklist**
- [ ] Pi Zero W + GPIO board
- [ ] 5 SG90 servos
- [ ] Breadboard with 5V power supply
- [ ] Jumper wires (male-to-male, male-to-female)

---

## 🔌 **Part 1: Physical Wiring (15 minutes)**

### **Step 1: Power Setup**
```
1. Connect Pi Zero W to GPIO board
2. Connect power supply (5V) to breadboard:
   - Red wire → Breadboard red rail (+)
   - Black wire → Breadboard blue rail (-)
3. Bridge power from breadboard to GPIO board:
   - Breadboard red rail → GPIO board 5V
   - Breadboard blue rail → GPIO board GND
```

### **Step 2: Connect All 5 Servos**
```
Each servo has 3 wires (Brown/Red/Orange):

Servo 0 (Thumb):
- Brown → GND
- Red → 5V
- Orange → GPIO Pin 12

Servo 1 (Index):
- Brown → GND
- Red → 5V
- Orange → GPIO Pin 13

Servo 2 (Middle):
- Brown → GND
- Red → 5V
- Orange → GPIO Pin 16

Servo 3 (Ring):
- Brown → GND
- Red → 5V
- Orange → GPIO Pin 19

Servo 4 (Pinky):
- Brown → GND
- Red → 5V
- Orange → GPIO Pin 20
```

### **Step 3: Final Check**
```
✅ All 5 servos connected to power (5V + GND)
✅ Signal wires to correct GPIO pins (12,13,16,19,20)
✅ Power supply connected and OFF (for now)
✅ Pi Zero W connected to GPIO board
✅ No loose connections
```

---

## 💻 **Part 2: Software & Testing (10 minutes)**

### **Step 4: Power On & Setup**
```bash
1. Power ON the 5V supply
2. Boot Pi Zero W (should start normally)
3. Open terminal/SSH to Pi
4. Navigate to project:
   cd /home/pi/the-dude
```

### **Step 5: Run Tests**

#### **Test 1: Single Servo (Thumb)**
```bash
python3 test_servo.py

Expected: Thumb servo moves through test sequence
If working: ✅ Continue to next test
If not working: Check troubleshooting below
```

#### **Test 2: All 5 Servos**
```bash
python3 test_5_servos.py

Select: "1" - Individual finger test

Expected: Each finger moves one at a time
Result: All 5 servos working independently
```

#### **Test 3: Hand Gestures**
```bash
python3 test_5_servos.py

Select: "2" - Basic gesture test

Expected: Hand performs recognizable gestures
- Open hand, closed fist, pointing, etc.
```

#### **Test 4: Interactive Control**
```bash
python3 test_5_servos.py

Select: "4" - Interactive control

Try these commands:
>>> gesture pointing
>>> gesture peace_sign
>>> gesture thumbs_up
>>> hand 0 0 0 0 0
>>> quit
```

---

## 🔧 **Part 3: Quick Troubleshooting**

### **If No Movement:**
```bash
1. Check power supply is ON and shows 5V
2. Run with sudo: sudo python3 test_servo.py
3. Enable GPIO: sudo raspi-config → Interface → GPIO → Enable
4. Reboot: sudo reboot
```

### **If Jittery Movement:**
```bash
1. Check power supply capacity (need 3A minimum for 5 servos)
2. Tighten all connections
3. Try with fewer servos first
```

### **If Permission Errors:**
```bash
1. Run with sudo: sudo python3 test_servo.py
2. Add user to GPIO group: sudo usermod -a -G gpio pi
3. Logout and login again
```

---

## ✅ **Part 4: Success Verification**

### **Complete Success Checklist:**
```
✅ All 5 servos move smoothly in individual test
✅ All basic gestures work and look recognizable
✅ Interactive commands respond correctly
✅ No overheating or unusual sounds
✅ Emergency stop (Ctrl+C) works properly
```

---

## 🎯 **Next Steps After Success**

1. **Mechanical Integration** - Attach servos to skeleton hand
2. **Cable System** - Install tendon/cable routing for realistic movement
3. **Gesture Refinement** - Adjust angles for natural-looking gestures
4. **Hardware Upgrades** - Consider PCA9685 controller for smoother operation
5. **AI Integration** - Add voice control and advanced features

---

## 📚 **Reference Documents**

- **Detailed Instructions**: `docs/testing_instructions.md`
- **Troubleshooting Guide**: `docs/troubleshooting_guide.md`
- **Hardware Shopping List**: `docs/shopping_list.md`
- **Skeleton Integration**: `docs/skeleton_joint_modification.md`

---

**🎉 Congratulations!** Once you complete these steps successfully, you'll have a fully functional 5-servo robotic hand ready for mechanical integration and advanced features!