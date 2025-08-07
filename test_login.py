#!/usr/bin/env python3
"""
Test Login with User Credentials
This script tests the login functionality with the user's credentials.
"""

import requests
import json

def test_login():
    """Test login with user credentials."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing Login with User Credentials")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Try login with user credentials
    print("\n🔐 Testing login with egclessuras@gmail.com...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = requests.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Login successful!")
        print(f"   User ID: {result.get('user', {}).get('id', 'Unknown')}")
        print(f"   Email: {result.get('user', {}).get('email', 'Unknown')}")
        print(f"   Message: {result.get('message', 'Unknown')}")
    else:
        print(f"❌ Login failed: {response.text}")
        return
    
    # Test 3: Check authentication status
    print("\n🔍 Checking authentication status...")
    response = requests.get(f"{base_url}/api/auth/check")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Authentication check successful!")
        print(f"   Authenticated: {result.get('authenticated', False)}")
        print(f"   User ID: {result.get('user_id', 'Unknown')}")
    else:
        print(f"❌ Authentication check failed: {response.text}")
    
    print("\n🎉 Login Test Complete!")
    print("=" * 50)
    print("✅ If login was successful, you can now use the application!")

if __name__ == "__main__":
    test_login() 
"""
Test Login with User Credentials
This script tests the login functionality with the user's credentials.
"""

import requests
import json

def test_login():
    """Test login with user credentials."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing Login with User Credentials")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Try login with user credentials
    print("\n🔐 Testing login with egclessuras@gmail.com...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = requests.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Login successful!")
        print(f"   User ID: {result.get('user', {}).get('id', 'Unknown')}")
        print(f"   Email: {result.get('user', {}).get('email', 'Unknown')}")
        print(f"   Message: {result.get('message', 'Unknown')}")
    else:
        print(f"❌ Login failed: {response.text}")
        return
    
    # Test 3: Check authentication status
    print("\n🔍 Checking authentication status...")
    response = requests.get(f"{base_url}/api/auth/check")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Authentication check successful!")
        print(f"   Authenticated: {result.get('authenticated', False)}")
        print(f"   User ID: {result.get('user_id', 'Unknown')}")
    else:
        print(f"❌ Authentication check failed: {response.text}")
    
    print("\n🎉 Login Test Complete!")
    print("=" * 50)
    print("✅ If login was successful, you can now use the application!")

if __name__ == "__main__":
    test_login() 
 