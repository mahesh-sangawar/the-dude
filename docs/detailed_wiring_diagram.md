# 🔌 Detailed GPIO Board Wiring Diagram

## 🎯 **Complete Pin-by-Pin Connection Guide**

### **GPIO Board Physical Layout Reference**
```
Pi Zero W GPIO Pins (40-pin layout):
     3V3  (1) (2)  5V
   GPIO2  (3) (4)  5V
   GPIO3  (5) (6)  GND
   GPIO4  (7) (8)  GPIO14
     GND  (9) (10) GPIO15
  GPIO17 (11) (12) GPIO18
  GPIO27 (13) (14) GND
  GPIO22 (15) (16) GPIO23
     3V3 (17) (18) GPIO24
  GPIO10 (19) (20) GND
   GPIO9 (21) (22) GPIO25
  GPIO11 (23) (24) GPIO8
     GND (25) (26) GPIO7
   GPIO0 (27) (28) GPIO1
   GPIO5 (29) (30) GND
   GPIO6 (31) (32) GPIO12  ← Servo 0 (Thumb)
  GPIO13 (33) (34) GND     ← Servo 1 (Index)
  GPIO19 (35) (36) GPIO16  ← Servo 2 (Middle)
  GPIO26 (37) (38) GPIO20  ← Servo 4 (Pinky)
     GND (39) (40) GPIO21
```

---

## ⚡ **Power Supply Connections**

### **Power Input to GPIO Board**
```
5V Power Supply → GPIO Board:

Connection Method A: Screw Terminals (if available)
- Power supply RED wire → 5V screw terminal
- Power supply BLACK wire → GND screw terminal
- Tighten screws securely

Connection Method B: Pin Headers with Jumpers
- Power supply RED wire → Male jumper → Pin 2 (5V)
- Power supply BLACK wire → Male jumper → Pin 6 (GND)

Connection Method C: Direct Wire Insertion (spring terminals)
- Insert RED wire directly into 5V terminal
- Insert BLACK wire directly into GND terminal
```

### **Power Distribution Strategy**
```
Use Multiple Power Pins for Better Distribution:

5V Pins Available: Pin 2, Pin 4
GND Pins Available: Pin 6, Pin 9, Pin 14, Pin 20, Pin 25, Pin 30, Pin 34, Pin 39

Recommended Distribution:
- Servos 0,1,2 → Pin 2 (5V), Pin 6 (GND)
- Servos 3,4 → Pin 4 (5V), Pin 14 (GND)
- Power supply → Pin 2 (5V), Pin 6 (GND)
```

---

## 🤖 **Detailed Servo Connections**

### **Servo 0 - Thumb (GPIO 12)**
```
SG90 Servo Wire Colors → GPIO Board Pins:

Brown/Black wire → GND Pin 6 (Physical pin 6)
Red wire → 5V Pin 2 (Physical pin 2)
Orange/Yellow wire → GPIO 12 Pin 32 (Physical pin 32)

Connection Details:
- Use female-to-male jumper if servo has male pins
- Use female-to-female jumper if GPIO board has male pins
- Ensure solid connection - wiggle test each wire
- Route orange wire away from power wires to avoid interference
```

### **Servo 1 - Index Finger (GPIO 13)**
```
SG90 Servo Wire Colors → GPIO Board Pins:

Brown/Black wire → GND Pin 6 (Physical pin 6) [SHARED]
Red wire → 5V Pin 2 (Physical pin 2) [SHARED]
Orange/Yellow wire → GPIO 13 Pin 33 (Physical pin 33)

Connection Notes:
- Share power rails with Servo 0
- Keep signal wire (orange) separate
- Label wire if possible: "Index"
```

### **Servo 2 - Middle Finger (GPIO 16)**
```
SG90 Servo Wire Colors → GPIO Board Pins:

Brown/Black wire → GND Pin 6 (Physical pin 6) [SHARED]
Red wire → 5V Pin 2 (Physical pin 2) [SHARED]
Orange/Yellow wire → GPIO 16 Pin 36 (Physical pin 36)

Connection Notes:
- Share power with Servos 0,1
- Route signal wire cleanly
- Test connection before securing
```

### **Servo 3 - Ring Finger (GPIO 19)**
```
SG90 Servo Wire Colors → GPIO Board Pins:

Brown/Black wire → GND Pin 14 (Physical pin 14) [NEW GND]
Red wire → 5V Pin 4 (Physical pin 4) [NEW 5V]
Orange/Yellow wire → GPIO 19 Pin 35 (Physical pin 35)

Connection Notes:
- Use different power pins for load distribution
- Helps prevent voltage drops
- Keep signal wire routing clean
```

### **Servo 4 - Pinky Finger (GPIO 20)**
```
SG9 Servo Wire Colors → GPIO Board Pins:

Brown/Black wire → GND Pin 14 (Physical pin 14) [SHARED with Servo 3]
Red wire → 5V Pin 4 (Physical pin 4) [SHARED with Servo 3]
Orange/Yellow wire → GPIO 20 Pin 38 (Physical pin 38)

Connection Notes:
- Share power with Servo 3
- Final servo connection
- Double-check all connections before power-on
```

---

## 📊 **Complete Connection Summary Table**

| Servo | Finger | GPIO Pin | Physical Pin | Brown (GND) | Red (5V) | Orange (Signal) |
|-------|--------|----------|--------------|-------------|----------|-----------------|
| 0 | Thumb | 12 | 32 | Pin 6 (GND) | Pin 2 (5V) | Pin 32 (GPIO12) |
| 1 | Index | 13 | 33 | Pin 6 (GND) | Pin 2 (5V) | Pin 33 (GPIO13) |
| 2 | Middle | 16 | 36 | Pin 6 (GND) | Pin 2 (5V) | Pin 36 (GPIO16) |
| 3 | Ring | 19 | 35 | Pin 14 (GND) | Pin 4 (5V) | Pin 35 (GPIO19) |
| 4 | Pinky | 20 | 38 | Pin 14 (GND) | Pin 4 (5V) | Pin 38 (GPIO20) |

---

## 🔧 **Wire Management & Organization**

### **Wire Routing Best Practices**
```
Signal Wires (Orange):
- Route away from power wires
- Keep as short as practical
- Avoid tight bends or loops
- Separate from each other when possible

Power Wires (Red/Brown):
- Twist red and brown together for each servo
- Use thicker gauge wire if available (18-20 AWG)
- Keep power runs short and direct
- Secure at connection points

Organization Tips:
- Label each servo wire set (Thumb, Index, etc.)
- Use different colored jumpers for easy identification
- Cable tie wire bundles together
- Leave some slack for movement/adjustment
```

### **Connection Order (Recommended)**
```
Step-by-Step Connection Sequence:

1. Insert Pi Zero W into GPIO board
2. Connect power supply to GPIO board (5V, GND)
3. Test voltage with multimeter (should read 5.0V)
4. Connect Servo 0 (Thumb) - test immediately
5. Connect Servo 1 (Index) - test both servos
6. Connect Servo 2 (Middle) - test first 3 servos
7. Connect Servo 3 (Ring) - test first 4 servos
8. Connect Servo 4 (Pinky) - test all 5 servos
9. Secure all connections
10. Final system test
```

---

## 🔍 **Connection Verification Checklist**

### **Before Power-On**
- [ ] Pi Zero W properly seated in GPIO board
- [ ] Power supply connected to correct pins (5V, GND)
- [ ] All servo brown wires to GND pins
- [ ] All servo red wires to 5V pins
- [ ] All servo orange wires to correct GPIO pins
- [ ] No loose connections
- [ ] No short circuits between power rails
- [ ] Wire routing clean and organized

### **Pin Assignment Verification**
```
Use this command to verify GPIO pin mapping:
gpio readall

Should show pins 12,13,16,19,20 as OUT mode when program runs
```

### **Power Distribution Check**
```
Measure voltage at each servo connection:
- Each red wire should read 5.0V ± 0.1V to its corresponding brown wire
- If voltage varies significantly, check power distribution
- Consider using thicker power wires if voltage drops
```

---

## ⚡ **Advanced Wiring Options**

### **Option A: Dedicated Power Distribution**
```
For best power stability:

Create power bus:
- Use heavier gauge wire (16-18 AWG)
- Connect all servo red wires to single 5V bus
- Connect all servo brown wires to single GND bus
- Connect bus to GPIO board with thick wires

Benefits:
- Better voltage stability
- Easier troubleshooting
- Professional appearance
- Easier servo replacement
```

### **Option B: Servo Extension Cables**
```
If servos will be mounted away from GPIO board:

Use servo extension cables:
- 3-wire servo extensions (various lengths)
- Male-female format typically
- Allows servos to be positioned for mechanical integration
- Keeps GPIO board area clean

Purchase Options:
- 15cm extensions for close mounting
- 30cm extensions for flexible positioning
- Assorted pack for different finger lengths
```

### **Option C: Terminal Block Distribution**
```
Professional power distribution:

Use screw terminal blocks:
- 5V distribution block
- GND distribution block
- Single feed from GPIO board
- Multiple outputs to servos

Benefits:
- Very secure connections
- Easy to modify
- Professional appearance
- Good for permanent installation
```

---

## 🚨 **Safety & Troubleshooting**

### **Connection Safety**
```
⚠️ CRITICAL SAFETY CHECKS:

Before Every Power-On:
1. Verify 5V and GND are not shorted
2. Check all connections are secure
3. Ensure no bare wires touching
4. Verify correct GPIO pin assignments
5. Have emergency power disconnect ready

During Operation:
1. Monitor servo temperatures
2. Watch for voltage drops
3. Listen for unusual sounds
4. Check for loose connections
5. Verify smooth servo movement
```

### **Common Wiring Problems**
```
Problem: Servo doesn't move
Causes:
- Signal wire on wrong GPIO pin
- Power connection loose
- Servo defective
- GPIO pin damaged

Problem: Erratic movement
Causes:
- Insufficient power supply
- Loose connections
- Interference on signal wires
- Multiple ground loops

Problem: Servo gets hot
Causes:
- Voltage too high (>5.5V)
- Mechanical binding
- Continuous stall condition
- Poor heat dissipation
```

---

## 📐 **Physical Layout Considerations**

### **GPIO Board Mounting**
```
Secure mounting options:
- Standoffs to keep board elevated
- Mounting to project base/chassis
- Protection from accidental contact
- Access for maintenance/adjustment

Ventilation:
- Ensure airflow around Pi and GPIO board
- Keep heat-generating components apart
- Consider small cooling fan for extended operation
```

### **Servo Positioning Planning**
```
For eventual mechanical integration:

Consider cable length requirements:
- Thumb: Shortest run (servo close to thumb)
- Index: Medium run (precision control needed)
- Middle: Medium run (primary grip finger)
- Ring: Longer run (couples with middle)
- Pinky: Longest run (outer edge of hand)

Plan servo mounting locations:
- Forearm area for main servo cluster
- Individual mounting for specific servos
- Access for maintenance and adjustment
- Protection from mechanical damage
```

This detailed guide should give you everything needed for professional-quality servo connections! 🔌🤖