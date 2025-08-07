#!/usr/bin/env python3
"""
James Clessuras Drafter - Fantasy Football Draft Assistant
Startup Script

This script runs the fantasy draft assistant application.
"""

import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("Starting James Clessuras Drafter...")
    print("Fantasy Football Draft Assistant")
    print("=" * 40)
    
    try:
        from fantasy_draft_web_enhanced import app
        print("Application loaded successfully!")
        print("Starting server on port 6970...")
        print("Open your browser and go to: http://localhost:6970")
        print("Press Ctrl+C to stop the server")
        print("=" * 40)
        
        app.run(debug=True, host='0.0.0.0', port=6970)
    except ImportError as e:
        print(f"Error importing application: {e}")
        print("Make sure all required files are present in this directory.")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1) 