"""
🎯 OBJECTIVE: Basic servo control foundation for DUDE robotic hand
⚡ PERFORMANCE: Direct GPIO PWM control with safety limits
⚠️ SAFETY: Position bounds checking and emergency stop capability
🔧 HARDWARE: Raspberry Pi Zero W GPIO pins to SG90 servos
"""

import time
import threading
from typing import Dict, List, Optional, Tuple
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("RPi.GPIO not available - running in simulation mode")
    GPIO = None

class ServoDriver:
    """
    Professional servo control system for DUDE robotic hand.
    Supports both direct GPIO and future PCA9685 controller integration.
    """

    def __init__(self, use_gpio: bool = True):
        """
        Initialize servo control system.

        Args:
            use_gpio: True for direct GPIO control, False for PCA9685
        """
        self.use_gpio = use_gpio
        self.servo_pins: Dict[int, int] = {}
        self.servo_positions: Dict[int, float] = {}
        self.servo_limits: Dict[int, Tuple[float, float]] = {}
        self.emergency_stop = False
        self.update_thread: Optional[threading.Thread] = None
        self.running = False

        # Default GPIO pin mapping for 12 servos
        self.default_gpio_pins = {
            0: 12,  # Thumb CMC Opposition
            1: 13,  # Thumb MCP Flexion
            2: 16,  # Thumb IP Flexion
            3: 19,  # Index MCP
            4: 20,  # Index PIP
            5: 21,  # Index DIP
            6: 26,  # Middle MCP
            7: 18,  # Middle PIP+DIP (hardware PWM)
            # Servos 8-11 will need PCA9685 or I2C expander
        }

        # Safety limits (degrees) - conservative initially
        self.default_limits = {
            0: (0, 90),    # Thumb opposition
            1: (0, 90),    # Thumb MCP
            2: (0, 60),    # Thumb IP
            3: (0, 90),    # Index MCP
            4: (0, 100),   # Index PIP
            5: (0, 80),    # Index DIP
            6: (0, 90),    # Middle MCP
            7: (0, 90),    # Middle PIP+DIP
        }

        if self.use_gpio and GPIO is not None:
            self._setup_gpio()

    def _setup_gpio(self) -> None:
        """Initialize GPIO pins for servo control."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Setup available GPIO pins
        for servo_id, pin in self.default_gpio_pins.items():
            if servo_id < 8:  # Only setup first 8 servos for GPIO
                GPIO.setup(pin, GPIO.OUT)
                self.servo_pins[servo_id] = pin
                self.servo_positions[servo_id] = 90.0  # Start at middle position
                self.servo_limits[servo_id] = self.default_limits[servo_id]

    def start(self) -> None:
        """Start the servo control system."""
        if self.running:
            return

        self.running = True
        self.emergency_stop = False

        if self.use_gpio and GPIO is not None:
            self.update_thread = threading.Thread(target=self._gpio_update_loop, daemon=True)
            self.update_thread.start()

        print("🤖 DUDE Servo Control System Started")
        print(f"📊 Controlling {len(self.servo_pins)} servos")

    def stop(self) -> None:
        """Stop the servo control system and cleanup."""
        self.running = False
        self.emergency_stop = True

        if self.update_thread and self.update_thread.is_alive():
            self.update_thread.join(timeout=1.0)

        if self.use_gpio and GPIO is not None:
            GPIO.cleanup()

        print("🛑 DUDE Servo Control System Stopped")

    def emergency_stop_all(self) -> None:
        """Immediately stop all servo movement."""
        self.emergency_stop = True
        print("🚨 EMERGENCY STOP ACTIVATED")

    def set_servo_position(self, servo_id: int, angle: float, speed: float = 1.0) -> bool:
        """
        Set servo position with safety checks.

        Args:
            servo_id: Servo identifier (0-11)
            angle: Target angle in degrees
            speed: Movement speed multiplier (0.1-2.0)

        Returns:
            bool: True if command accepted, False if rejected
        """
        if self.emergency_stop:
            print(f"❌ Servo {servo_id}: Emergency stop active")
            return False

        if servo_id not in self.servo_limits:
            print(f"❌ Servo {servo_id}: Not configured")
            return False

        # Safety bounds checking
        min_angle, max_angle = self.servo_limits[servo_id]
        if not (min_angle <= angle <= max_angle):
            print(f"❌ Servo {servo_id}: Angle {angle}° outside limits [{min_angle}°, {max_angle}°]")
            return False

        # Speed limiting
        speed = max(0.1, min(2.0, speed))

        self.servo_positions[servo_id] = angle
        print(f"✅ Servo {servo_id}: Moving to {angle}° (speed: {speed:.1f}x)")
        return True

    def get_servo_position(self, servo_id: int) -> Optional[float]:
        """Get current servo position."""
        return self.servo_positions.get(servo_id)

    def set_servo_limits(self, servo_id: int, min_angle: float, max_angle: float) -> None:
        """Set safety limits for a servo."""
        if 0 <= min_angle < max_angle <= 180:
            self.servo_limits[servo_id] = (min_angle, max_angle)
            print(f"🔒 Servo {servo_id}: Limits set to [{min_angle}°, {max_angle}°]")
        else:
            print(f"❌ Invalid limits for servo {servo_id}")

    def _gpio_update_loop(self) -> None:
        """Main GPIO PWM update loop (50Hz)."""
        while self.running and not self.emergency_stop:
            start_time = time.time()

            # Generate PWM signals for all servos
            for servo_id, pin in self.servo_pins.items():
                if servo_id in self.servo_positions:
                    angle = self.servo_positions[servo_id]
                    pulse_width = self._angle_to_pulse_width(angle)

                    # Generate PWM pulse
                    GPIO.output(pin, GPIO.HIGH)
                    time.sleep(pulse_width / 1000000.0)  # Convert microseconds to seconds
                    GPIO.output(pin, GPIO.LOW)

            # Maintain 50Hz update rate (20ms period)
            elapsed = time.time() - start_time
            sleep_time = max(0, 0.02 - elapsed)  # 20ms - elapsed time
            time.sleep(sleep_time)

    def _angle_to_pulse_width(self, angle: float) -> float:
        """
        Convert servo angle to PWM pulse width.

        Args:
            angle: Servo angle in degrees (0-180)

        Returns:
            Pulse width in microseconds (1000-2000)
        """
        # Standard servo: 1000-2000 microseconds for 0-180 degrees
        pulse_width = 1000 + (angle / 180.0) * 1000
        return max(1000, min(2000, pulse_width))

    def get_status(self) -> Dict:
        """Get complete system status."""
        return {
            "running": self.running,
            "emergency_stop": self.emergency_stop,
            "servo_count": len(self.servo_pins),
            "positions": self.servo_positions.copy(),
            "limits": self.servo_limits.copy(),
            "control_method": "GPIO" if self.use_gpio else "PCA9685"
        }

"""
📊 USAGE EXAMPLE:
    >>> driver = ServoDriver()
    >>> driver.start()
    >>>
    >>> # Test single servo
    >>> driver.set_servo_position(0, 45.0)  # Thumb opposition
    >>> time.sleep(2)
    >>> driver.set_servo_position(0, 0.0)   # Back to start
    >>>
    >>> driver.stop()

🧪 TESTING:
    1. Connect single servo to GPIO pin 12
    2. Run basic movement test
    3. Verify safety limits work
    4. Test emergency stop

🚀 OPTIMIZATION:
    - Hardware PWM for smoother control
    - PCA9685 integration for all 12 servos
    - Current monitoring for load detection
    - Position feedback sensors
"""