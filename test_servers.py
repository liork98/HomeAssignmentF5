import requests

def test_server(url, expected_status, expected_content=None):
    try:
        response = requests.get(url)
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
        if expected_content:
            assert expected_content in response.text, f"Expected content not found in response from {url}"
        print(f"Test passed for {url}")
    except Exception as e:
        print(f"Test failed for {url}: {e}")
        return False
    return True

def main():
    tests = [
        {"url": "http://nginx:8080", "expected_status": 200, "expected_content": "This is a custom response served by Nginx."},
        {"url": "http://nginx:8081", "expected_status": 503}
    ]
    results = [test_server(**test) for test in tests]
    exit(0 if all(results) else 1)

if __name__ == "__main__":
    main()
