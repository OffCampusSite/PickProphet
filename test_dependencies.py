#!/usr/bin/env python3
"""
Test script to verify all dependencies are working correctly.
This helps identify any missing dependencies before deployment.
"""

import sys

def test_imports():
    """Test all required imports."""
    print("Testing imports...")
    
    try:
        import pandas
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import supabase
        print("✅ Supabase imported successfully")
    except ImportError as e:
        print(f"❌ Supabase import failed: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Requests import failed: {e}")
        return False
    
    try:
        import dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    try:
        import gunicorn
        print("✅ Gunicorn imported successfully")
    except ImportError as e:
        print(f"❌ Gunicorn import failed: {e}")
        return False
    
    return True

def test_app_startup():
    """Test if the app can start without errors."""
    print("\nTesting app startup...")
    
    try:
        # Import the main app
        from fantasy_draft_web_enhanced import app, initialize_app
        
        # Test initialization
        init_result = initialize_app()
        if init_result:
            print("✅ App initialization successful")
        else:
            print("⚠️ App initialization had issues but continuing...")
        
        # Test basic Flask app
        with app.test_client() as client:
            response = client.get('/health')
            if response.status_code == 200:
                print("✅ Health check endpoint working")
            else:
                print(f"❌ Health check failed with status {response.status_code}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ App startup failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 PickProphet Dependency Test")
    print("=" * 40)
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test app startup
        app_ok = test_app_startup()
        
        if app_ok:
            print("\n🎉 All tests passed! Your app is ready for deployment.")
            return 0
        else:
            print("\n❌ App startup tests failed.")
            return 1
    else:
        print("\n❌ Import tests failed. Please install missing dependencies.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 