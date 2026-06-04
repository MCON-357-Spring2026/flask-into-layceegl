import requests

BASE_URL = "http://127.0.0.1:5000"

print("--- 1. Testing Welcome Route ---")
response = requests.get(f"{BASE_URL}/")

print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")
print("\n")

print("--- 2. Testing About Route ---")
response_about = requests.get(f"{BASE_URL}/about")

about_data = response_about.json()

print(f"Name: {about_data.get('name')}")
print(f"Course: {about_data.get('course')}")
print(f"Semester: {about_data.get('semester')}")
print("\n")

print("--- 3. Testing Greeting Route ---")
my_name = "LayCee"
response_greet = requests.get(f"{BASE_URL}/greet/{my_name}")

print(f"Response Text: {response_greet.text}")

if my_name in response_greet.text:
    print("Success: The response contains my name!")
else:
    print("Failure: My name was not found in the response.")
print("\n")

print("--- 4. Testing Calculator Route ---")
params_add = {
    'num1': 10,
    'num2': 5,
    'operation': 'add'
}
response_add = requests.get(f"{BASE_URL}/calculate", params=params_add)
print(f"Addition Response: {response_add.json()}")

params_mult = {
    'num1': 6,
    'num2': 7,
    'operation': 'multiply'
}
response_mult = requests.get(f"{BASE_URL}/calculate", params=params_mult)
print(f"Multiplication Response: {response_mult.json()}")
print("\n")

print("--- 5. Testing Echo Route (POST) ---")
payload = {
    "message": "Hello from IntelliJ!",
    "status": "Testing"
}

response_echo = requests.post(f"{BASE_URL}/echo", json=payload)
echo_data = response_echo.json()

print(f"Echo Response: {echo_data}")

if echo_data.get('echoed') is True:
    print("Success: The response includes 'echoed': True!")
else:
    print("Failure: 'echoed' key was missing or false.")
print("\n")

print("--- 6. Testing Different Status Codes ---")
code_1 = 200
response_code1 = requests.get(f"{BASE_URL}/status/{code_1}")
print(f"Requested Code: {code_1} -> Returned Status Code: {response_code1.status_code}")
print(f"Response Text: {response_code1.text}")

code_2 = 404
response_code2 = requests.get(f"{BASE_URL}/status/{code_2}")
print(f"Requested Code: {code_2} -> Returned Status Code: {response_code2.status_code}")
print(f"Response Text: {response_code2.text}")
print("\n")

print("--- 7. Testing Custom Headers ---")
response_header = requests.get(f"{BASE_URL}/")

custom_header = response_header.headers.get('X-Custom-Header')

print(f"Custom Header Found: {custom_header}")

if custom_header == "FlaskRocks":
    print("Success: Custom header 'X-Custom-Header: FlaskRocks' is present!")
else:
    print("Failure: Custom header was missing or incorrect.")
print("\n")

print("--- 8. Testing Error Handling ---")
response_error = requests.get(f"{BASE_URL}/calculate?num1=10&num2=0&operation=divide")

print(f"Status Code: {response_error.status_code}")
print(f"Response JSON: {response_error.json()}")
print("\n")

