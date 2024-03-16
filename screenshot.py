from PIL import ImageGrab
import time
import schedule

def take_screenshot():
    """Take a screenshot and save it with a timestamp."""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = ImageGrab.grab()
    screenshot.save(f"images/screenshot_{timestamp}.png")
    print(f"Screenshot taken at {timestamp}")

def main():
    # Schedule the take_screenshot function to run every 5 minutes
    schedule.every(5).seconds.do(take_screenshot)
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
