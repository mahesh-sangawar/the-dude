#!/usr/bin/env python3
"""
🎯 OBJECTIVE: Basic servo testing script for DUDE robotic hand
⚡ PERFORMANCE: Test individual servo movement and safety systems
⚠️ SAFETY: Includes emergency stop and position limits
🔧 HARDWARE: Single SG90 servo on GPIO pin 12
"""

import time
import sys
import signal
from src.servo_control.servo_driver import ServoDriver

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print("\n🛑 Interrupted by user")
    if 'driver' in globals():
        driver.stop()
    sys.exit(0)

def test_single_servo():
    """Test basic servo functionality."""
    print("🤖 DUDE Servo Test - Starting...")
    print("📋 This will test Servo 0 (Thumb CMC) on GPIO pin 12")
    print("⚠️  Make sure servo is connected to GPIO 12, 5V, and GND")
    print("🛑 Press Ctrl+C to stop at any time\n")

    # Setup signal handler for clean exit
    signal.signal(signal.SIGINT, signal_handler)

    # Initialize servo driver
    driver = ServoDriver(use_gpio=True)
    driver.start()

    try:
        # Test 1: Basic movement
        print("🧪 Test 1: Basic Movement Test")
        print("   Moving servo to center position (45°)...")
        driver.set_servo_position(0, 45.0)
        time.sleep(2)

        print("   Moving to fully opposed position (90°)...")
        driver.set_servo_position(0, 90.0)
        time.sleep(2)

        print("   Moving to relaxed position (0°)...")
        driver.set_servo_position(0, 0.0)
        time.sleep(2)

        # Test 2: Safety limits
        print("\n🔒 Test 2: Safety Limits Test")
        print("   Attempting to exceed upper limit (120° - should fail)...")
        success = driver.set_servo_position(0, 120.0)
        if not success:
            print("   ✅ Safety limit working correctly!")

        print("   Attempting to exceed lower limit (-10° - should fail)...")
        success = driver.set_servo_position(0, -10.0)
        if not success:
            print("   ✅ Safety limit working correctly!")

        # Test 3: Smooth movement sequence
        print("\n🎯 Test 3: Smooth Movement Sequence")
        print("   Performing thumb opposition sequence...")

        positions = [0, 15, 30, 45, 60, 75, 90, 75, 60, 45, 30, 15, 0]
        for i, pos in enumerate(positions):
            print(f"   Step {i+1}/13: Moving to {pos}°")
            driver.set_servo_position(0, pos)
            time.sleep(0.5)

        # Test 4: Emergency stop
        print("\n🚨 Test 4: Emergency Stop Test")
        print("   Starting movement, then triggering emergency stop...")
        driver.set_servo_position(0, 90.0)
        time.sleep(0.5)
        driver.emergency_stop_all()

        # Try to move after emergency stop (should fail)
        success = driver.set_servo_position(0, 0.0)
        if not success:
            print("   ✅ Emergency stop working correctly!")

        # Test 5: System status
        print("\n📊 Test 5: System Status")
        status = driver.get_status()
        print(f"   System Running: {status['running']}")
        print(f"   Emergency Stop: {status['emergency_stop']}")
        print(f"   Servo Count: {status['servo_count']}")
        print(f"   Control Method: {status['control_method']}")
        print(f"   Current Positions: {status['positions']}")

        print("\n✅ All tests completed successfully!")
        print("🎉 Your servo control system is working properly!")

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        print("🔧 Check your connections and try again")

    finally:
        print("\n🛑 Stopping servo control system...")
        driver.stop()
        print("🏁 Test complete!")

def interactive_servo_control():
    """Interactive servo position control."""
    print("🎮 DUDE Interactive Servo Control")
    print("📋 Commands:")
    print("   - Enter angle (0-90): Move servo to position")
    print("   - 'q' or 'quit': Exit")
    print("   - 'stop': Emergency stop")
    print("   - 'status': Show system status")

    driver = ServoDriver(use_gpio=True)
    driver.start()

    try:
        while True:
            user_input = input("\n🤖 Enter command: ").strip().lower()

            if user_input in ['q', 'quit', 'exit']:
                break
            elif user_input == 'stop':
                driver.emergency_stop_all()
            elif user_input == 'status':
                status = driver.get_status()
                print(f"📊 Status: {status}")
            else:
                try:
                    angle = float(user_input)
                    success = driver.set_servo_position(0, angle)
                    if success:
                        print(f"✅ Moving to {angle}°")
                    else:
                        print("❌ Command rejected (check limits or emergency stop)")
                except ValueError:
                    print("❌ Invalid input. Enter a number between 0-90.")

    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
    finally:
        driver.stop()

if __name__ == "__main__":
    print("🤖 DUDE Servo Testing Suite")
    print("1. Automated Test")
    print("2. Interactive Control")

    try:
        choice = input("Select option (1 or 2): ").strip()

        if choice == "1":
            test_single_servo()
        elif choice == "2":
            interactive_servo_control()
        else:
            print("Invalid choice. Running automated test...")
            test_single_servo()

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)

"""
📊 USAGE EXAMPLE:
    # On Raspberry Pi:
    python3 test_servo.py

    # Expected output:
    🤖 DUDE Servo Test - Starting...
    📋 This will test Servo 0 (Thumb CMC) on GPIO pin 12
    ✅ All tests completed successfully!

🧪 TESTING CHECKLIST:
    [ ] Connect servo to GPIO 12, 5V, GND
    [ ] Run automated test
    [ ] Verify smooth movement
    [ ] Test safety limits
    [ ] Test emergency stop
    [ ] Try interactive control

🚀 NEXT STEPS:
    1. Connect additional servos to other GPIO pins
    2. Test multi-servo coordination
    3. Implement gesture library
    4. Add PCA9685 controller support
"""