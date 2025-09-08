from picarx import Picarx
from time import sleep
from vilib import Vilib

# Initialize PicarX
px = Picarx()

def main():
    # Start camera
    Vilib.camera_start()
    Vilib.display()

    try:
        while True:
            # --- Check GREEN ---
            Vilib.color_detect("green")
            sleep(0.5)  # allow detection
            green_w = Vilib.detect_obj_parameter['color_w']
            green_h = Vilib.detect_obj_parameter['color_h']

            if green_w > 0 and green_h > 0:
                print("GREEN detected → GO")
                px.forward(30)
                continue

            # --- Check RED ---
            Vilib.color_detect("red")
            sleep(0.5)
            red_w = Vilib.detect_obj_parameter['color_w']
            red_h = Vilib.detect_obj_parameter['color_h']

            if red_w > 0 and red_h > 0:
                print("RED detected → STOP")
                px.stop()
                continue

            # --- If no color, stop for safety ---
            px.stop()

    except KeyboardInterrupt:
        print("Game stopped by user.")
        px.stop()

if __name__ == "__main__":
    main()
