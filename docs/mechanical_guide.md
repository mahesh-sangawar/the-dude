# Mechanical Integration Guide - Skeleton Hand

## 🦴 **Skeleton Preparation**

### Joint Analysis
```
Articulated Joints to Utilize:
├── Wrist: Flexion/Extension + Rotation
├── Thumb: CMC (opposition) + MCP (flexion)
├── Index: MCP + PIP (coupled movement)
├── Middle: MCP flexion
├── Ring: MCP flexion
├── Pinky: MCP flexion
└── Note: DIP joints follow PIP naturally
```

### Cable Attachment Points
```bash
Drilling Locations (1-2mm holes):
- Fingertip attachment (dorsal side)
- Proximal phalanx (for PIP control)
- Metacarpal heads (MCP pivot)
- Wrist attachment points
- Forearm servo mounting area
```

## 🔧 **Cable-Tendon System**

### Materials List
```
Essential Components:
- Fishing line: 15-20lb test, clear
- Small eyelets: 2-3mm inner diameter
- Servo horns: Standard with SG90 servos
- Ball bearings: 3-4mm for pulleys
- Heat shrink tubing: 2-3mm diameter
- Cable tension springs: Light duty
- Epoxy adhesive: Strong, flexible when cured
```

### Installation Steps

#### Step 1: Mark Cable Paths
1. **Flexion path**: Fingertip → palm → forearm
2. **Guide points**: At each joint that changes direction
3. **Avoid interference**: Keep cables separated
4. **Test routing**: Use string first before drilling

#### Step 2: Install Guide Points
```bash
Drilling Technique:
1. Mark locations with pencil
2. Start with 1mm pilot hole
3. Enlarge gradually to 2mm
4. Smooth with fine sandpaper
5. Install eyelets with epoxy
6. Allow 24hr cure time
```

#### Step 3: Servo Mounting Base
```
Forearm Mount Design:
- Plywood base: 15cm x 10cm x 1cm
- Servo spacing: 2.5cm centers
- Secure to skeleton forearm with clamps
- Allow access to servo horns
- Cable routing channels
```

## ⚙️ **Servo-to-Movement Mapping**

### Thumb Control (2 servos)
```python
# Servo 0: Thumb Opposition (CMC joint)
# Range: 0° = thumb parallel to fingers
#        90° = thumb perpendicular (opposition)

# Servo 1: Thumb Flexion (MCP joint)
# Range: 0° = straight
#        90° = fully flexed
```

### Finger Control (4 servos)
```python
# Index Finger (2 servos - most dexterous)
# Servo 2: MCP flexion (0-90°)
# Servo 3: PIP+DIP flexion (0-100°, coupled)

# Other Fingers (1 servo each)
# Servo 4: Middle MCP (0-90°)
# Servo 5: Ring MCP (0-90°)
# Servo 6: Pinky MCP (0-90°)
```

### Wrist Control (1 servo)
```python
# Servo 7: Wrist Flexion/Extension
# Range: -30° extension to +60° flexion
# Mount: Direct attachment to wrist joint
```

## 🔒 **Safety Considerations**

### Mechanical Limits
```
Built-in Protection:
- Cable tension limiters (weak link concept)
- Servo horn slip clutches
- Emergency cable release mechanism
- Bone stress monitoring (visual inspection)
```

### Installation Safety
```bash
Best Practices:
- Always drill away from joint surfaces
- Use cutting fluid (water) when drilling
- Wear safety glasses
- Secure skeleton during work
- Keep cables under light tension only
```

## 🎯 **Testing Protocol**

### Phase 1: Individual Joint Testing
1. **Single servo connection**
2. **Manual range verification**
3. **Cable tension adjustment**
4. **Smooth movement check**

### Phase 2: Multi-Joint Coordination
1. **Adjacent finger interference check**
2. **Full hand open/close test**
3. **Gesture library validation**
4. **Long-term reliability test**

## 📏 **Measurement & Calibration**

### Critical Measurements
```
Record for Software:
- Cable length from servo to fingertip
- Pulley diameters at each guide point
- Joint angle limits (mechanical stops)
- Servo horn attachment points
- Baseline "relaxed" position
```

### Calibration Procedure
```python
# For each servo, record:
servo_config = {
    "min_pulse": 1000,  # microseconds
    "max_pulse": 2000,  # microseconds
    "min_angle": 0,     # degrees (hand open)
    "max_angle": 90,    # degrees (hand closed)
    "cable_length": 150 # mm from servo to fingertip
}
```

## 🎨 **Future Silicone Application**

### Preparation for Skin
```
Design Considerations:
- Cable access points for maintenance
- Servo accessibility for calibration
- Removable sections for repairs
- Realistic joint appearance
- Proper cable routing to avoid tears
```

### Silicone-Friendly Design
- **Smooth cable routing** (no sharp bends)
- **Flush mounting** of all hardware
- **Flexible joint areas** for natural movement
- **Maintenance access** without skin removal