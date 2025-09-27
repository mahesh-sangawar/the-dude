#!/usr/bin/env python3
"""
🎯 OBJECTIVE: 5-servo hand testing and demonstration
⚡ PERFORMANCE: Test coordinated finger movements and gestures
⚠️ SAFETY: Progressive testing with emergency stop capability
🔧 HARDWARE: 5 SG90 servos connected to GPIO pins 12,13,16,19,20
"""

import time
import sys
import signal
from src.servo_control.hand_controller import HandController

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print("\n🛑 Interrupted by user")
    if 'hand' in globals():
        hand.stop()
    sys.exit(0)

def test_individual_fingers():
    """Test each finger individually."""
    print("\n🔧 Testing Individual Fingers")
    print("=" * 40)

    hand = HandController()
    hand.start()

    try:
        fingers = ["thumb", "index", "middle", "ring", "pinky"]

        for finger in fingers:
            print(f"\n🖐️  Testing {finger} finger...")

            # Open position
            print(f"   Opening {finger}...")
            hand.set_finger_position(finger, 0)
            time.sleep(1)

            # Closed position
            print(f"   Closing {finger}...")
            hand.set_finger_position(finger, 90)
            time.sleep(1)

            # Return to neutral
            print(f"   Returning {finger} to neutral...")
            hand.set_finger_position(finger, 30)
            time.sleep(1)

        print("\n✅ Individual finger test completed!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
    finally:
        hand.stop()

def test_basic_gestures():
    """Test predefined gesture library."""
    print("\n🎭 Testing Basic Gestures")
    print("=" * 40)

    hand = HandController()
    hand.start()

    try:
        gestures = hand.get_available_gestures()
        print(f"📋 Available gestures: {gestures}")

        for gesture in gestures:
            print(f"\n🎯 Performing: {gesture}")
            hand.perform_gesture(gesture)
            time.sleep(2)  # Pause between gestures

        print("\n✅ Gesture test completed!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
    finally:
        hand.stop()

def test_sequences():
    """Test animated sequences."""
    print("\n🎬 Testing Animated Sequences")
    print("=" * 40)

    hand = HandController()
    hand.start()

    try:
        sequences = hand.get_available_sequences()
        print(f"📋 Available sequences: {sequences}")

        for sequence in sequences:
            print(f"\n🎬 Performing sequence: {sequence}")
            hand.perform_sequence(sequence)
            time.sleep(3)  # Allow sequence to complete

        print("\n✅ Sequence test completed!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
    finally:
        hand.stop()

def interactive_control():
    """Interactive hand control interface."""
    print("\n🎮 Interactive Hand Control")
    print("=" * 40)
    print("Commands:")
    print("  gesture <name>     - Perform gesture")
    print("  sequence <name>    - Perform sequence")
    print("  finger <name> <angle> - Move finger to angle")
    print("  hand <a1> <a2> <a3> <a4> <a5> - Set all fingers")
    print("  status             - Show hand status")
    print("  gestures           - List available gestures")
    print("  sequences          - List available sequences")
    print("  calibrate <finger> - Calibrate finger")
    print("  stop               - Emergency stop")
    print("  quit               - Exit")

    hand = HandController()
    hand.start()

    try:
        while True:
            command = input("\n🤖 Enter command: ").strip().lower().split()

            if not command:
                continue

            cmd = command[0]

            if cmd in ['q', 'quit', 'exit']:
                break

            elif cmd == 'gesture' and len(command) > 1:
                gesture_name = command[1]
                hand.perform_gesture(gesture_name)

            elif cmd == 'sequence' and len(command) > 1:
                sequence_name = command[1]
                hand.perform_sequence(sequence_name)

            elif cmd == 'finger' and len(command) > 2:
                finger_name = command[1]
                try:
                    angle = float(command[2])
                    hand.set_finger_position(finger_name, angle)
                except ValueError:
                    print("❌ Invalid angle. Use number between 0-90.")

            elif cmd == 'hand' and len(command) > 5:
                try:
                    angles = [float(x) for x in command[1:6]]
                    hand.set_hand_position(angles)
                except ValueError:
                    print("❌ Invalid angles. Use 5 numbers between 0-90.")

            elif cmd == 'status':
                status = hand.get_hand_status()
                print(f"📊 Current gesture: {status['current_gesture']}")
                print(f"📊 Moving: {status['is_moving']}")
                print(f"📊 Finger positions: {status['finger_positions']}")

            elif cmd == 'gestures':
                gestures = hand.get_available_gestures()
                print(f"📋 Available gestures: {gestures}")

            elif cmd == 'sequences':
                sequences = hand.get_available_sequences()
                print(f"📋 Available sequences: {sequences}")

            elif cmd == 'calibrate' and len(command) > 1:
                finger_name = command[1]
                hand.calibrate_finger(finger_name)

            elif cmd == 'stop':
                hand.emergency_stop()

            else:
                print("❌ Unknown command. Type 'quit' to exit.")

    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
    finally:
        hand.stop()

def demonstration_mode():
    """Full demonstration of hand capabilities."""
    print("\n🎪 DUDE Hand Demonstration")
    print("=" * 40)
    print("This will demonstrate all hand capabilities...")
    print("Press Ctrl+C to stop at any time")

    hand = HandController()
    hand.start()

    try:
        # 1. Individual finger test
        print("\n🔧 Part 1: Individual Finger Control")
        fingers = ["thumb", "index", "middle", "ring", "pinky"]
        for finger in fingers:
            print(f"   Moving {finger}...")
            hand.set_finger_position(finger, 90)
            time.sleep(0.5)
            hand.set_finger_position(finger, 0)
            time.sleep(0.5)

        # 2. Basic gestures
        print("\n🎭 Part 2: Basic Gestures")
        basic_gestures = ["open_hand", "closed_fist", "pointing", "thumbs_up", "peace_sign"]
        for gesture in basic_gestures:
            print(f"   Gesture: {gesture}")
            hand.perform_gesture(gesture)
            time.sleep(2)

        # 3. Sequences
        print("\n🎬 Part 3: Animated Sequences")
        sequences = hand.get_available_sequences()
        for sequence in sequences:
            print(f"   Sequence: {sequence}")
            hand.perform_sequence(sequence)
            time.sleep(4)

        # 4. Custom movements
        print("\n🎨 Part 4: Custom Movements")
        print("   Finger wave...")
        for i in range(3):
            hand.set_hand_position([15, 0, 30, 60, 90])
            time.sleep(0.3)
            hand.set_hand_position([15, 30, 60, 90, 60])
            time.sleep(0.3)
            hand.set_hand_position([15, 60, 90, 60, 30])
            time.sleep(0.3)
            hand.set_hand_position([15, 90, 60, 30, 0])
            time.sleep(0.3)

        print("\n🎉 Demonstration complete!")
        hand.perform_gesture("open_hand")

    except Exception as e:
        print(f"\n❌ Demonstration failed: {e}")
    finally:
        hand.stop()

def main():
    """Main test selection interface."""
    print("🤖 DUDE 5-Servo Hand Testing Suite")
    print("=" * 50)
    print("Hardware Required:")
    print("  - 5 SG90 servos connected to GPIO pins:")
    print("    • Thumb:   GPIO 12")
    print("    • Index:   GPIO 13")
    print("    • Middle:  GPIO 16")
    print("    • Ring:    GPIO 19")
    print("    • Pinky:   GPIO 20")
    print("  - 5V power supply (3A minimum)")
    print()
    print("Test Options:")
    print("  1. Individual finger test")
    print("  2. Basic gesture test")
    print("  3. Sequence animation test")
    print("  4. Interactive control")
    print("  5. Full demonstration")

    signal.signal(signal.SIGINT, signal_handler)

    try:
        choice = input("\nSelect test (1-5): ").strip()

        if choice == "1":
            test_individual_fingers()
        elif choice == "2":
            test_basic_gestures()
        elif choice == "3":
            test_sequences()
        elif choice == "4":
            interactive_control()
        elif choice == "5":
            demonstration_mode()
        else:
            print("Invalid choice. Running demonstration...")
            demonstration_mode()

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()

"""
📊 EXPECTED RESULTS:
    ✅ Individual fingers move smoothly
    ✅ Gestures look recognizable
    ✅ Sequences play automatically
    ✅ Interactive control responds properly
    ✅ Emergency stops work immediately

🧪 TROUBLESHOOTING:
    - No movement: Check servo connections and power
    - Jittery movement: Verify power supply capacity
    - Wrong direction: Check servo horn orientation
    - Limited range: Adjust cable tension

🚀 NEXT STEPS:
    1. Mechanical integration with skeleton
    2. Cable routing and tension adjustment
    3. Gesture refinement and new additions
    4. PCA9685 upgrade for smoother control
"""