import time
import random
import signal
import atexit
from dotenv import load_dotenv

from utils.api.get_pending_requests import get_pending_requests
from utils.mail_sender.email_sender import send_email

from utils.util import get_undetected_driver
from utils.automation import (
    capture_jwt_token, login,
    navigate_to_Instructors_listings
)

load_dotenv()

# Global reference so cleanup handlers can access it
_driver = None


def cleanup_driver():
    """Ensure the browser is closed on exit."""
    global _driver
    if _driver:
        try:
            _driver.quit()
            print("Browser closed successfully.")
        except Exception:
            pass
        _driver = None


def signal_handler(sig, frame):
    """Handle termination signals (Ctrl+C, stop debugging, etc.)."""
    print(f"\nReceived signal {sig}. Closing browser...")
    cleanup_driver()
    raise SystemExit(0)


# Register cleanup for normal exit and signals
atexit.register(cleanup_driver)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
try:
    signal.signal(signal.SIGBREAK, signal_handler)  # Windows: Ctrl+Break
except AttributeError:
    pass  # SIGBREAK only available on Windows


def main():
    global _driver
    _driver = get_undetected_driver(headless=False)
    try:
        login(_driver)
        navigate_to_Instructors_listings(_driver)
        jwt_token = capture_jwt_token(_driver)
        if _driver:
            print("JWT token captured successfully.")
            _driver.quit()
            _driver = None
        pending_requests = get_pending_requests(jwt_token)
        if pending_requests:
            for request in pending_requests:
                instructor_email = request.get("email")
                instructor_name = request.get("name")
                send_email(instructor_email, instructor_name)
                time.sleep(random.uniform(1, 3))  # Sleep to avoid spamming
        else:
            print("No pending requests found.")

    except Exception as e:
        print(f"An error occurred in main: {e}")
    finally:
        cleanup_driver()


if __name__ == "__main__":
    main()
