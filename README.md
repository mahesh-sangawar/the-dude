# 🤖 DUDE - Robotic Hand Project

A sophisticated robotic hand system using 12 servo motors controlled by Raspberry Pi Zero W, designed for realistic human-like movements and AI integration.

## 🎯 **Current Status: Phase 1 - Basic Control**

- ✅ Project structure created
- ✅ Basic servo control system implemented
- ✅ Safety systems and emergency stops
- ✅ GPIO-based control for 8 servos
- 🔄 Ready for hardware testing
- 📦 Shopping list prepared for upgrades

## 🛠️ **Hardware Requirements**

### Current Setup (Phase 1)
- Raspberry Pi Zero W
- 8-12x SG90 servo motors
- Medical education hand skeleton model
- 5V power supply (3A minimum)
- Jumper wires and breadboard

### Recommended Upgrades (Phase 2)
- PCA9685 16-channel PWM controller
- 5V 8A power supply
- Servo extension cables
- Current monitoring module

## 🚀 **Quick Start**

### 1. Setup Raspberry Pi
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
pip3 install -r requirements.txt

# Clone/download project
git clone <repository-url>
cd the-dude
```

### 2. Connect Hardware
```
Servo 0 (Thumb CMC) → GPIO 12
Power: 5V and GND to servo
```

### 3. Test Basic Movement
```bash
# Run servo test
python3 test_servo.py

# Select option 1 for automated test
# Select option 2 for interactive control
```

## 📁 **Project Structure**

```
the-dude/
├── src/
│   ├── servo_control/
│   │   ├── servo_driver.py      # Main servo control system
│   │   └── __init__.py
│   ├── safety/                  # Safety systems (future)
│   └── utils/                   # Utilities (future)
├── config/
│   └── servo_config.json        # Servo configuration
├── docs/
│   ├── shopping_list.md         # Hardware to purchase
│   ├── 12_servo_mapping.md      # Advanced servo layout
│   ├── mechanical_guide.md      # Skeleton integration
│   ├── improvements_roadmap.md  # Future enhancements
│   ├── project_context.md       # Hardware specs
│   └── coding_standards.md      # Code guidelines
├── tests/                       # Test files (future)
├── test_servo.py               # Basic servo testing
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎮 **Usage Examples**

### Basic Servo Control
```python
from src.servo_control.servo_driver import ServoDriver

# Initialize system
driver = ServoDriver()
driver.start()

# Move thumb to opposition
driver.set_servo_position(0, 90.0)

# Emergency stop if needed
driver.emergency_stop_all()

# Clean shutdown
driver.stop()
```

### Safety Features
```python
# Set custom limits
driver.set_servo_limits(0, min_angle=0, max_angle=75)

# Check current position
position = driver.get_servo_position(0)

# Get system status
status = driver.get_status()
```

## 🔒 **Safety Features**

- ✅ **Position bounds checking** - Software limits prevent damage
- ✅ **Emergency stop system** - Immediate halt capability
- ✅ **Graceful shutdown** - Proper GPIO cleanup
- ✅ **Error handling** - Comprehensive exception management
- 🔄 **Current monitoring** - Future hardware upgrade
- 🔄 **Thermal protection** - Future sensor integration

## 📊 **Servo Mapping (Current)**

| Servo | GPIO | Function | Range | Joint |
|-------|------|----------|-------|-------|
| 0 | 12 | Thumb CMC Opposition | 0-90° | CMC |
| 1 | 13 | Thumb MCP Flexion | 0-90° | MCP |
| 2 | 16 | Thumb IP Flexion | 0-60° | IP |
| 3 | 19 | Index MCP | 0-90° | MCP |
| 4 | 20 | Index PIP | 0-100° | PIP |
| 5 | 21 | Index DIP | 0-80° | DIP |
| 6 | 26 | Middle MCP | 0-90° | MCP |
| 7 | 18 | Middle PIP+DIP | 0-90° | PIP/DIP |

**Note**: Servos 8-11 require PCA9685 controller (see shopping list)

## 🛒 **Next Steps**

1. **Test current setup** - Run `test_servo.py` with single servo
2. **Order PCA9685 controller** - Enable all 12 servos (see `docs/shopping_list.md`)
3. **Mechanical integration** - Attach servos to skeleton (see `docs/mechanical_guide.md`)
4. **Expand control** - Add remaining servos
5. **Gesture library** - Implement hand movements
6. **AI integration** - Voice control system

## 📚 **Documentation**

- 📋 [Shopping List](docs/shopping_list.md) - Hardware to purchase
- 🔧 [Mechanical Guide](docs/mechanical_guide.md) - Skeleton integration
- 🚀 [Improvements Roadmap](docs/improvements_roadmap.md) - Future features
- 🎯 [12-Servo Mapping](docs/12_servo_mapping.md) - Advanced configuration

## 🤝 **Contributing**

This is a personal learning project, but suggestions and improvements are welcome!

## ⚠️ **Safety Notice**

- Always test with single servo first
- Use appropriate power supply (never exceed servo ratings)
- Implement emergency stops before full integration
- Be careful when drilling skeleton model
- Monitor servo temperatures during extended use

## 📄 **License**

This project is for educational and personal use.

---

**Status**: ✅ Ready for initial testing with single servo
**Next Milestone**: 🎯 PCA9685 integration for full 12-servo control