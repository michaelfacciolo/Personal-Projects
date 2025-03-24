import time
import sys

# For Windows
try:
    import winsound
    def beep():
        winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
except ImportError:
    # For macOS/Linux
    def beep():
        print("\a")  # ASCII Bell character, may not work on all systems

def countdown(t):
    """Countdown timer that displays time in MM:SS format."""
    while t > 0:
        mins, secs = divmod(t, 60)
        print(f"\r{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        t -= 1
    print("\nThe timer is up!")
    beep()  # Play sound when the timer is up

def main():
    while True:
        try:
            t = int(input("Enter the time in seconds: "))
            if t <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    countdown(t)

if __name__ == "__main__":
    main()
