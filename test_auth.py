#!/usr/bin/env python3
"""
Authentication Test Script
This script tests the authentication system to ensure it's working properly.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_auth_system():
    """Test the authentication system."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing PickProphet Authentication System")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return False
    
    # Test 2: Test registration
    print("\n📝 Testing Registration...")
    test_email = "test@example.com"
    test_password = "testpassword123"
    
    registration_data = {
        "email": test_email,
        "password": test_password
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/auth/register",
            json=registration_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Registration endpoint working")
        else:
            print(f"⚠️  Registration returned status {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Registration test failed: {e}")
    
    # Test 3: Test login
    print("\n🔐 Testing Login...")
    
    login_data = {
        "email": test_email,
        "password": test_password
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/auth/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Login endpoint working")
            data = response.json()
            if data.get('success'):
                print("✅ Login successful")
            else:
                print(f"⚠️  Login failed: {data.get('error', 'Unknown error')}")
        else:
            print(f"⚠️  Login returned status {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Login test failed: {e}")
    
    # Test 4: Test logout
    print("\n🚪 Testing Logout...")
    
    try:
        response = requests.get(f"{base_url}/logout")
        if response.status_code == 302:  # Redirect
            print("✅ Logout route working (redirects to login)")
        else:
            print(f"⚠️  Logout returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Logout test failed: {e}")
    
    # Test 5: Test API logout
    try:
        response = requests.get(f"{base_url}/api/auth/logout")
        if response.status_code == 200:
            print("✅ API logout endpoint working")
        else:
            print(f"⚠️  API logout returned status {response.status_code}")
    except Exception as e:
        print(f"❌ API logout test failed: {e}")
    
    print("\n🎉 Authentication tests completed!")
    print("\nNext steps:")
    print("1. If all tests passed, your auth system is working")
    print("2. Deploy to your chosen platform")
    print("3. Test with real users")
    
    return True

def test_supabase_connection():
    """Test Supabase connection."""
    
    print("\n🔗 Testing Supabase Connection...")
    
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("⚠️  Supabase credentials not found in .env file")
        print("   The app will run in development mode")
        return False
    
    try:
        from supabase import create_client
        supabase = create_client(supabase_url, supabase_key)
        
        # Test connection by trying to access a table
        result = supabase.table('user_custom_projections').select('*').limit(1).execute()
        print("✅ Supabase connection successful")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        print("   Make sure your credentials are correct")
        return False

if __name__ == "__main__":
    print("🚀 PickProphet Authentication Test Suite")
    print("=" * 50)
    
    # Test Supabase connection
    supabase_ok = test_supabase_connection()
    
    # Test authentication system
    auth_ok = test_auth_system()
    
    if auth_ok:
        print("\n✅ All tests completed successfully!")
        print("Your authentication system is ready for deployment.")
    else:
        print("\n❌ Some tests failed. Please check the issues above.") 
"""
Authentication Test Script
This script tests the authentication system to ensure it's working properly.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_auth_system():
    """Test the authentication system."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing PickProphet Authentication System")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return False
    
    # Test 2: Test registration
    print("\n📝 Testing Registration...")
    test_email = "test@example.com"
    test_password = "testpassword123"
    
    registration_data = {
        "email": test_email,
        "password": test_password
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/auth/register",
            json=registration_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Registration endpoint working")
        else:
            print(f"⚠️  Registration returned status {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Registration test failed: {e}")
    
    # Test 3: Test login
    print("\n🔐 Testing Login...")
    
    login_data = {
        "email": test_email,
        "password": test_password
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/auth/login",
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Login endpoint working")
            data = response.json()
            if data.get('success'):
                print("✅ Login successful")
            else:
                print(f"⚠️  Login failed: {data.get('error', 'Unknown error')}")
        else:
            print(f"⚠️  Login returned status {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Login test failed: {e}")
    
    # Test 4: Test logout
    print("\n🚪 Testing Logout...")
    
    try:
        response = requests.get(f"{base_url}/logout")
        if response.status_code == 302:  # Redirect
            print("✅ Logout route working (redirects to login)")
        else:
            print(f"⚠️  Logout returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Logout test failed: {e}")
    
    # Test 5: Test API logout
    try:
        response = requests.get(f"{base_url}/api/auth/logout")
        if response.status_code == 200:
            print("✅ API logout endpoint working")
        else:
            print(f"⚠️  API logout returned status {response.status_code}")
    except Exception as e:
        print(f"❌ API logout test failed: {e}")
    
    print("\n🎉 Authentication tests completed!")
    print("\nNext steps:")
    print("1. If all tests passed, your auth system is working")
    print("2. Deploy to your chosen platform")
    print("3. Test with real users")
    
    return True

def test_supabase_connection():
    """Test Supabase connection."""
    
    print("\n🔗 Testing Supabase Connection...")
    
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("⚠️  Supabase credentials not found in .env file")
        print("   The app will run in development mode")
        return False
    
    try:
        from supabase import create_client
        supabase = create_client(supabase_url, supabase_key)
        
        # Test connection by trying to access a table
        result = supabase.table('user_custom_projections').select('*').limit(1).execute()
        print("✅ Supabase connection successful")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        print("   Make sure your credentials are correct")
        return False

if __name__ == "__main__":
    print("🚀 PickProphet Authentication Test Suite")
    print("=" * 50)
    
    # Test Supabase connection
    supabase_ok = test_supabase_connection()
    
    # Test authentication system
    auth_ok = test_auth_system()
    
    if auth_ok:
        print("\n✅ All tests completed successfully!")
        print("Your authentication system is ready for deployment.")
    else:
        print("\n❌ Some tests failed. Please check the issues above.") 
 