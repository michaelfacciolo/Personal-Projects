import time
import sys
import os
import signal

# Cross-platform beep functionality
def beep():
    """Play a beep sound depending on the OS."""
    try:
        if os.name == "nt":  # Windows
            import winsound
            winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
        elif sys.platform == "darwin":  # macOS
            os.system("afplay /System/Library/Sounds/Ping.aiff")
        else:  # Linux (Requires 'sox' package)
            os.system("play -nq -t alsa synth 0.5 sine 1000")
    except Exception:
        print("\a")  # Fallback ASCII Bell character


def countdown(duration: int):
    """Countdown timer with progress animation and MM:SS format display."""
    try:
        for remaining in range(duration, 0, -1):
            mins, secs = divmod(remaining, 60)
            progress = "#" * (remaining * 20 // duration)  # Visual progress
            print(f"\r⏳ {mins:02d}:{secs:02d} [{progress:<20}]", end="", flush=True)
            time.sleep(1)
        print("\n✅ Time's up!")
        beep()
    except KeyboardInterrupt:
        print("\n⏹️ Countdown interrupted.")
        sys.exit(1)


def get_valid_time():
    """Prompt user for a valid positive integer time in seconds."""
    while True:
        try:
            t = int(input("⏲️ Enter countdown time in seconds: ").strip())
            if t <= 0:
                print("❌ Please enter a **positive** number.")
                continue
            return t
        except ValueError:
            print("❌ Invalid input. Enter a valid **numeric** value.")


def main():
    """Main function to execute the countdown timer."""
    while True:
        duration = get_valid_time()
        countdown(duration)

        # Ask user if they want to restart
        choice = input("🔁 Restart? (y/n): ").strip().lower()
        if choice != "y":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda sig, frame: print("\n⏹️ Interrupted. Exiting...") or sys.exit(0))
    main()
