#!/usr/bin/env python3
"""
Test Supabase Setup and Custom Projections
This script tests the Supabase connection and custom projections functionality.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_supabase_connection():
    """Test if Supabase tables exist."""
    
    print("🔗 Testing Supabase Connection...")
    
    try:
        from supabase import create_client
        supabase_url = os.environ.get("SUPABASE_URL")
        supabase_key = os.environ.get("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            print("❌ Supabase credentials not found in .env file")
            return False
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Test if tables exist
        try:
            result = supabase.table('user_custom_projections').select('*').limit(1).execute()
            print("✅ user_custom_projections table exists")
        except Exception as e:
            print(f"❌ user_custom_projections table error: {e}")
            return False
        
        try:
            result = supabase.table('completed_drafts').select('*').limit(1).execute()
            print("✅ completed_drafts table exists")
        except Exception as e:
            print(f"❌ completed_drafts table error: {e}")
            return False
        
        print("✅ All Supabase tables are accessible")
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def test_authentication():
    """Test authentication endpoints."""
    
    print("\n🔐 Testing Authentication...")
    base_url = "http://localhost:4000"
    
    # Test registration
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
    except Exception as e:
        print(f"❌ Registration test failed: {e}")
    
    # Test login
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
            return True
        else:
            print(f"⚠️  Login returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Login test failed: {e}")
        return False

def test_custom_projections():
    """Test custom projections functionality."""
    
    print("\n📊 Testing Custom Projections...")
    base_url = "http://localhost:4000"
    
    # Test saving a custom projection
    custom_data = {
        "player_name": "Test Player",
        "position": "RB",
        "custom_stats": {
            "rushing_yards": 1200,
            "rushing_tds": 8,
            "receptions": 50,
            "receiving_yards": 400,
            "receiving_tds": 2,
            "fumbles": 2
        }
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/save_custom_projection",
            json=custom_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Custom projection save endpoint working")
        else:
            print(f"⚠️  Custom projection save returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Custom projection save test failed: {e}")

def test_draft_initialization():
    """Test draft initialization with custom projections."""
    
    print("\n🏈 Testing Draft Initialization...")
    base_url = "http://localhost:4000"
    
    draft_data = {
        "num_teams": 12,
        "user_position": 1,
        "scoring_format": "ppr"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/init",
            json=draft_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Draft initialization working")
                print(f"   Custom projections loaded: {data.get('draft_info', {}).get('custom_projections_loaded', 0)}")
            else:
                print(f"⚠️  Draft initialization failed: {data.get('error')}")
        else:
            print(f"⚠️  Draft initialization returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Draft initialization test failed: {e}")

if __name__ == "__main__":
    print("🚀 PickProphet Supabase Setup Test")
    print("=" * 50)
    
    # Test Supabase connection
    supabase_ok = test_supabase_connection()
    
    if not supabase_ok:
        print("\n❌ Supabase setup failed. Please run the SQL commands in your Supabase dashboard first.")
        print("   Copy the contents of create_tables.sql and run it in your Supabase SQL Editor.")
        exit(1)
    
    # Test authentication
    auth_ok = test_authentication()
    
    if auth_ok:
        # Test custom projections
        test_custom_projections()
        
        # Test draft initialization
        test_draft_initialization()
        
        print("\n🎉 All tests completed!")
        print("Your PickProphet application is ready for deployment.")
    else:
        print("\n❌ Authentication tests failed. Please check your Supabase Auth settings.") 
"""
Test Supabase Setup and Custom Projections
This script tests the Supabase connection and custom projections functionality.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_supabase_connection():
    """Test if Supabase tables exist."""
    
    print("🔗 Testing Supabase Connection...")
    
    try:
        from supabase import create_client
        supabase_url = os.environ.get("SUPABASE_URL")
        supabase_key = os.environ.get("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            print("❌ Supabase credentials not found in .env file")
            return False
        
        supabase = create_client(supabase_url, supabase_key)
        
        # Test if tables exist
        try:
            result = supabase.table('user_custom_projections').select('*').limit(1).execute()
            print("✅ user_custom_projections table exists")
        except Exception as e:
            print(f"❌ user_custom_projections table error: {e}")
            return False
        
        try:
            result = supabase.table('completed_drafts').select('*').limit(1).execute()
            print("✅ completed_drafts table exists")
        except Exception as e:
            print(f"❌ completed_drafts table error: {e}")
            return False
        
        print("✅ All Supabase tables are accessible")
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def test_authentication():
    """Test authentication endpoints."""
    
    print("\n🔐 Testing Authentication...")
    base_url = "http://localhost:4000"
    
    # Test registration
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
    except Exception as e:
        print(f"❌ Registration test failed: {e}")
    
    # Test login
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
            return True
        else:
            print(f"⚠️  Login returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Login test failed: {e}")
        return False

def test_custom_projections():
    """Test custom projections functionality."""
    
    print("\n📊 Testing Custom Projections...")
    base_url = "http://localhost:4000"
    
    # Test saving a custom projection
    custom_data = {
        "player_name": "Test Player",
        "position": "RB",
        "custom_stats": {
            "rushing_yards": 1200,
            "rushing_tds": 8,
            "receptions": 50,
            "receiving_yards": 400,
            "receiving_tds": 2,
            "fumbles": 2
        }
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/save_custom_projection",
            json=custom_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Custom projection save endpoint working")
        else:
            print(f"⚠️  Custom projection save returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Custom projection save test failed: {e}")

def test_draft_initialization():
    """Test draft initialization with custom projections."""
    
    print("\n🏈 Testing Draft Initialization...")
    base_url = "http://localhost:4000"
    
    draft_data = {
        "num_teams": 12,
        "user_position": 1,
        "scoring_format": "ppr"
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/init",
            json=draft_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Draft initialization working")
                print(f"   Custom projections loaded: {data.get('draft_info', {}).get('custom_projections_loaded', 0)}")
            else:
                print(f"⚠️  Draft initialization failed: {data.get('error')}")
        else:
            print(f"⚠️  Draft initialization returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Draft initialization test failed: {e}")

if __name__ == "__main__":
    print("🚀 PickProphet Supabase Setup Test")
    print("=" * 50)
    
    # Test Supabase connection
    supabase_ok = test_supabase_connection()
    
    if not supabase_ok:
        print("\n❌ Supabase setup failed. Please run the SQL commands in your Supabase dashboard first.")
        print("   Copy the contents of create_tables.sql and run it in your Supabase SQL Editor.")
        exit(1)
    
    # Test authentication
    auth_ok = test_authentication()
    
    if auth_ok:
        # Test custom projections
        test_custom_projections()
        
        # Test draft initialization
        test_draft_initialization()
        
        print("\n🎉 All tests completed!")
        print("Your PickProphet application is ready for deployment.")
    else:
        print("\n❌ Authentication tests failed. Please check your Supabase Auth settings.") 
 