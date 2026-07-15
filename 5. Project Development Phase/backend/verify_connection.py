"""
Quick verification script to test if the backend is running and connected properly.
Run this script from the backend directory after starting the server.

Usage: python verify_connection.py
"""

import requests
import sys
from pathlib import Path

# Configuration
BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def print_header(text):
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}")

def print_success(text):
    print(f"[PASS] {text}")

def print_error(text):
    print(f"[FAIL] {text}")

def test_health_check():
    """Test if the backend is running."""
    print_header("Testing Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Backend is running: {data}")
            return True
        else:
            print_error(f"Unexpected status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error(f"Cannot connect to {BASE_URL}")
        print("  -> Is the backend server running?")
        print("  -> Run: python main.py")
        return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_api_endpoints():
    """Test each API endpoint."""
    print_header("Testing API Endpoints")
    
    endpoints = [
        {
            "name": "Explain",
            "endpoint": "/explain",
            "payload": {"topic": "Photosynthesis", "level": "beginner"}
        },
        {
            "name": "Q&A",
            "endpoint": "/qa",
            "payload": {"question": "What is the capital of France?"}
        },
        {
            "name": "Quiz",
            "endpoint": "/quiz",
            "payload": {"topic": "Math", "num_questions": 3}
        },
        {
            "name": "Summarize",
            "endpoint": "/summarize",
            "payload": {"text": "Photosynthesis is the process by which plants convert light energy into chemical energy."}
        },
        {
            "name": "Learning Path",
            "endpoint": "/learn/recommendations",
            "payload": {"topic": "Python"}
        }
    ]
    
    all_passed = True
    for test in endpoints:
        try:
            print(f"\nTesting {test['name']} ({test['endpoint']})...")
            response = requests.post(
                f"{BASE_URL}{test['endpoint']}",
                json=test['payload'],
                timeout=TIMEOUT
            )
            if response.status_code == 200:
                data = response.json()
                if "result" in data:
                    result = data["result"][:100] + "..." if len(data["result"]) > 100 else data["result"]
                    print_success(f"{test['name']} returned: {result}")
                else:
                    print_error(f"{test['name']} response missing 'result' field")
                    all_passed = False
            else:
                print_error(f"{test['name']} returned status {response.status_code}")
                print(f"  Response: {response.text[:200]}")
                all_passed = False
        except requests.exceptions.Timeout:
            print_error(f"{test['name']} timed out (took longer than {TIMEOUT}s)")
            print("  -> Check if API is processing slowly or if GOOGLE_API_KEY is valid")
            all_passed = False
        except Exception as e:
            print_error(f"{test['name']} error: {e}")
            all_passed = False
    return all_passed

def test_frontend():
    """Test if frontend is served."""
    print_header("Testing Frontend")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=TIMEOUT)
        if response.status_code == 200:
            if "EduGenie" in response.text:
                print_success("Frontend is being served correctly")
                return True
            else:
                print_error("Frontend loaded but EduGenie not found in HTML")
                return False
        else:
            print_error(f"Frontend returned status {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Frontend test error: {e}")
        return False

def test_cors():
    """Test if CORS is properly configured."""
    print_header("Testing CORS Configuration")
    try:
        headers = {
            "Origin": "http://example.com",
            "Access-Control-Request-Method": "POST"
        }
        response = requests.options(
            f"{BASE_URL}/explain",
            headers=headers,
            timeout=TIMEOUT
        )
        if "access-control-allow-origin" in response.headers:
            print_success(f"CORS enabled: {response.headers.get('access-control-allow-origin')}")
            return True
        else:
            print_error("CORS headers not found in response")
            return False
    except Exception as e:
        print_error(f"CORS test error: {e}")
        return False

def main():
    print("\n" + "="*50)
    print("  EduGenie Connection Verification")
    print("="*50)
    print(f"Testing backend at: {BASE_URL}")
    
    results = []
    
    # Run all tests
    results.append(("Health Check", test_health_check()))
    if results[0][1]:  # Only test other things if backend is running
        results.append(("Frontend", test_frontend()))
        results.append(("CORS", test_cors()))
        results.append(("API Endpoints", test_api_endpoints()))
    
    # Summary
    print_header("Verification Summary")
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "[PASS]" if passed else "[FAIL]"
        print(f"{symbol} {test_name}: {status}")
    
    # Final message
    print()
    if results[0][1]:
        print("[PASS] Backend and frontend are properly connected!")
        print("[PASS] You can now use the application at http://localhost:8000")
        return 0
    else:
        print("[FAIL] Connection verification failed.")
        print("[FAIL] Please check the backend server and configuration.")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nVerification interrupted by user.")
        sys.exit(130)
