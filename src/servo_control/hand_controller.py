"""
🎯 OBJECTIVE: 5-servo hand controller with gesture library
⚡ PERFORMANCE: Coordinated multi-servo movements and gesture sequences
⚠️ SAFETY: Synchronized movement with position validation
🔧 HARDWARE: 5 SG90 servos for thumb and 4 fingers
"""

import json
import time
import threading
from typing import Dict, List, Optional, Tuple
from .servo_driver import ServoDriver

class HandController:
    """
    Professional 5-servo hand controller with gesture library.
    Controls thumb + 4 fingers for realistic hand movements.
    """

    def __init__(self, config_file: str = "config/5_servo_config.json"):
        """
        Initialize hand controller.

        Args:
            config_file: Path to servo configuration file
        """
        self.servo_driver = ServoDriver(use_gpio=True)
        self.config = self._load_config(config_file)
        self.current_gesture = "open_hand"
        self.is_moving = False
        self.movement_thread: Optional[threading.Thread] = None

        # Finger mapping for easy reference
        self.fingers = {
            "thumb": 0,
            "index": 1,
            "middle": 2,
            "ring": 3,
            "pinky": 4
        }

        # Setup servos based on config
        self._setup_servos()

    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Config file {config_file} not found, using defaults")
            return self._default_config()

    def _default_config(self) -> Dict:
        """Provide default configuration if file not found."""
        return {
            "servo_mapping": {
                "0": {"min_angle": 0, "max_angle": 90, "default_position": 15},
                "1": {"min_angle": 0, "max_angle": 90, "default_position": 0},
                "2": {"min_angle": 0, "max_angle": 90, "default_position": 0},
                "3": {"min_angle": 0, "max_angle": 90, "default_position": 0},
                "4": {"min_angle": 0, "max_angle": 90, "default_position": 0}
            },
            "gestures": {
                "open_hand": {"positions": [15, 0, 0, 0, 0]},
                "closed_fist": {"positions": [75, 90, 90, 90, 90]}
            }
        }

    def _setup_servos(self) -> None:
        """Configure servo limits based on config."""
        for servo_id_str, servo_config in self.config["servo_mapping"].items():
            servo_id = int(servo_id_str)
            min_angle = servo_config["min_angle"]
            max_angle = servo_config["max_angle"]
            self.servo_driver.set_servo_limits(servo_id, min_angle, max_angle)

    def start(self) -> None:
        """Start the hand control system."""
        self.servo_driver.start()
        # Move to default open position
        self.perform_gesture("open_hand")
        print("🖐️  DUDE Hand Controller Started - Ready for gestures!")

    def stop(self) -> None:
        """Stop the hand control system."""
        self.is_moving = False
        if self.movement_thread and self.movement_thread.is_alive():
            self.movement_thread.join(timeout=2.0)
        self.servo_driver.stop()
        print("🛑 Hand Controller Stopped")

    def emergency_stop(self) -> None:
        """Emergency stop all movement."""
        self.is_moving = False
        self.servo_driver.emergency_stop_all()
        print("🚨 HAND EMERGENCY STOP")

    def set_finger_position(self, finger: str, angle: float) -> bool:
        """
        Set individual finger position.

        Args:
            finger: Finger name ('thumb', 'index', 'middle', 'ring', 'pinky')
            angle: Target angle in degrees

        Returns:
            bool: True if successful
        """
        if finger not in self.fingers:
            print(f"❌ Unknown finger: {finger}")
            return False

        servo_id = self.fingers[finger]
        return self.servo_driver.set_servo_position(servo_id, angle)

    def set_hand_position(self, positions: List[float]) -> bool:
        """
        Set all finger positions simultaneously.

        Args:
            positions: List of 5 angles [thumb, index, middle, ring, pinky]

        Returns:
            bool: True if all positions set successfully
        """
        if len(positions) != 5:
            print("❌ Need exactly 5 positions for all fingers")
            return False

        success = True
        for i, angle in enumerate(positions):
            if not self.servo_driver.set_servo_position(i, angle):
                success = False

        return success

    def perform_gesture(self, gesture_name: str) -> bool:
        """
        Perform a predefined gesture.

        Args:
            gesture_name: Name of gesture from config

        Returns:
            bool: True if gesture started successfully
        """
        if gesture_name not in self.config["gestures"]:
            print(f"❌ Unknown gesture: {gesture_name}")
            print(f"📋 Available gestures: {list(self.config['gestures'].keys())}")
            return False

        gesture = self.config["gestures"][gesture_name]
        positions = gesture["positions"]
        duration = gesture.get("duration_seconds", 1.0)

        print(f"🎭 Performing gesture: {gesture_name}")
        success = self.set_hand_position(positions)

        if success:
            self.current_gesture = gesture_name
            time.sleep(duration)  # Allow movement to complete

        return success

    def perform_sequence(self, sequence_name: str) -> bool:
        """
        Perform a gesture sequence.

        Args:
            sequence_name: Name of sequence from config

        Returns:
            bool: True if sequence started successfully
        """
        if sequence_name not in self.config["sequences"]:
            print(f"❌ Unknown sequence: {sequence_name}")
            print(f"📋 Available sequences: {list(self.config['sequences'].keys())}")
            return False

        sequence = self.config["sequences"][sequence_name]
        print(f"🎬 Starting sequence: {sequence_name}")

        def run_sequence():
            self.is_moving = True
            try:
                for step in sequence["steps"]:
                    if not self.is_moving:  # Check for stop signal
                        break

                    positions = step["positions"]
                    duration = step["duration"]

                    self.set_hand_position(positions)
                    time.sleep(duration)

            except Exception as e:
                print(f"❌ Sequence error: {e}")
            finally:
                self.is_moving = False

        # Run sequence in separate thread
        self.movement_thread = threading.Thread(target=run_sequence, daemon=True)
        self.movement_thread.start()
        return True

    def get_available_gestures(self) -> List[str]:
        """Get list of available gestures."""
        return list(self.config["gestures"].keys())

    def get_available_sequences(self) -> List[str]:
        """Get list of available sequences."""
        return list(self.config["sequences"].keys())

    def get_finger_positions(self) -> Dict[str, float]:
        """Get current positions of all fingers."""
        positions = {}
        for finger, servo_id in self.fingers.items():
            pos = self.servo_driver.get_servo_position(servo_id)
            positions[finger] = pos if pos is not None else 0.0
        return positions

    def get_hand_status(self) -> Dict:
        """Get complete hand status."""
        return {
            "current_gesture": self.current_gesture,
            "is_moving": self.is_moving,
            "finger_positions": self.get_finger_positions(),
            "available_gestures": self.get_available_gestures(),
            "available_sequences": self.get_available_sequences(),
            "servo_status": self.servo_driver.get_status()
        }

    def calibrate_finger(self, finger: str) -> None:
        """
        Interactive calibration for a finger.

        Args:
            finger: Finger to calibrate
        """
        if finger not in self.fingers:
            print(f"❌ Unknown finger: {finger}")
            return

        servo_id = self.fingers[finger]
        print(f"🔧 Calibrating {finger} finger (Servo {servo_id})")
        print("📋 Testing range of motion...")

        # Test minimum position
        print("   Testing minimum position (0°)...")
        self.servo_driver.set_servo_position(servo_id, 0)
        time.sleep(2)

        # Test maximum position
        print("   Testing maximum position (90°)...")
        self.servo_driver.set_servo_position(servo_id, 90)
        time.sleep(2)

        # Return to neutral
        print("   Returning to neutral position...")
        self.servo_driver.set_servo_position(servo_id, 45)
        time.sleep(1)

        print(f"✅ {finger} calibration complete")

"""
📊 USAGE EXAMPLE:
    >>> hand = HandController()
    >>> hand.start()
    >>>
    >>> # Basic gestures
    >>> hand.perform_gesture("thumbs_up")
    >>> hand.perform_gesture("peace_sign")
    >>> hand.perform_gesture("closed_fist")
    >>>
    >>> # Sequences
    >>> hand.perform_sequence("wave")
    >>> hand.perform_sequence("finger_count")
    >>>
    >>> # Individual control
    >>> hand.set_finger_position("thumb", 45)
    >>> hand.set_hand_position([30, 45, 60, 75, 90])
    >>>
    >>> hand.stop()

🧪 TESTING:
    1. Connect 5 servos to GPIO pins 12, 13, 16, 19, 20
    2. Test individual finger control
    3. Verify gesture library
    4. Test sequence animations
    5. Calibrate each finger

🚀 OPTIMIZATION:
    - Smooth interpolation between positions
    - Custom gesture creation interface
    - Voice command integration
    - Gesture learning from demonstration
"""