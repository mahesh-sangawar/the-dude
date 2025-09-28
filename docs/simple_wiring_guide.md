# 🔌 Simple 5-Servo Wiring Guide

## **Materials Checklist**
- [ ] Pi Zero W + GPIO board
- [ ] 5 SG90 servos
- [ ] Breadboard with 5V power supply
- [ ] Jumper wires (male-to-male, male-to-female)

## **Physical Wiring (15 minutes)**

### **Power Connections**
```
1. Power Supply → Breadboard:
   Red wire → Breadboard red rail (+)
   Black wire → Breadboard blue rail (-)

2. Breadboard → GPIO Board:
   Breadboard red rail → GPIO board 5V pin
   Breadboard blue rail → GPIO board GND pin

3. Pi Zero W → GPIO Board:
   Insert Pi into GPIO board (all pins aligned)
```

### **Servo Connections (All 5 at once)**
```
Each servo has 3 wires: Brown(GND), Red(5V), Orange(Signal)

Connect to GPIO board:
                Brown   Red   Orange
Servo 0 (Thumb)  → GND → 5V → Pin 12
Servo 1 (Index)  → GND → 5V → Pin 13
Servo 2 (Middle) → GND → 5V → Pin 16
Servo 3 (Ring)   → GND → 5V → Pin 19
Servo 4 (Pinky)  → GND → 5V → Pin 20
```

### **Final Check Before Power On**
- [ ] All servos have power (red/brown wires)
- [ ] All servos have signal (orange wires to correct pins)
- [ ] No loose connections
- [ ] Power supply is OFF

## **Testing Sequence (10 minutes)**

### **1. Power On**
```bash
Turn ON 5V power supply
Pi should boot normally
Servos should not move initially
```

### **2. Basic Test**
```bash
cd /home/pi/the-dude
python3 test_servo.py

Should see thumb servo moving through test sequence
```

### **3. All Servos Test**
```bash
python3 test_5_servos.py
Select: 1 (Individual finger test)

Should see each finger move one at a time
```

### **4. Gesture Test**
```bash
python3 test_5_servos.py
Select: 2 (Basic gesture test)

Should see recognizable hand gestures
```

### **5. Interactive Test**
```bash
python3 test_5_servos.py
Select: 4 (Interactive control)

Try: gesture pointing
Try: gesture peace_sign
Try: quit
```

## **Success Criteria**
✅ All 5 servos move smoothly
✅ Gestures look recognizable
✅ Interactive commands work
✅ No overheating or errors

## **Common Quick Fixes**
- No movement → Run with `sudo python3 test_servo.py`
- Permission error → `sudo raspi-config` → Enable GPIO → Reboot
- Jittery movement → Check power supply capacity (need 3A+)
- Hot servos → Check for mechanical binding

**Total time: ~25 minutes from start to working hand gestures!** 🎉