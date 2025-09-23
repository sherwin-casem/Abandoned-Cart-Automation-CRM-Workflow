#!/usr/bin/env python3
"""
Cart Abandonment Recovery Demo Startup Script

This script helps you start both the backend API and frontend demo.
"""

import subprocess
import sys
import time
import webbrowser
import os
from pathlib import Path

def check_python():
    """Check if Python is available"""
    try:
        result = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)
        print(f"✅ Python found: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Python not found: {e}")
        return False

def install_requirements():
    """Install backend requirements"""
    backend_dir = Path(__file__).parent / "backend"
    requirements_file = backend_dir / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ Requirements file not found")
        return False
    
    print("📦 Installing backend requirements...")
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ], check=True, cwd=backend_dir)
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def start_backend():
    """Start the Flask backend server"""
    backend_dir = Path(__file__).parent / "backend"
    app_file = backend_dir / "app.py"
    
    if not app_file.exists():
        print("❌ Backend app.py not found")
        return None
    
    print("🚀 Starting backend server...")
    try:
        process = subprocess.Popen([
            sys.executable, "app.py"
        ], cwd=backend_dir)
        
        # Wait a moment for server to start
        time.sleep(3)
        
        print("✅ Backend server started on http://localhost:5000")
        return process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def open_frontend():
    """Open the frontend in browser"""
    frontend_file = Path(__file__).parent / "index.html"
    
    if not frontend_file.exists():
        print("❌ Frontend index.html not found")
        return False
    
    print("🌐 Opening frontend in browser...")
    try:
        webbrowser.open(f"file://{frontend_file.absolute()}")
        print("✅ Frontend opened in browser")
        return True
    except Exception as e:
        print(f"❌ Failed to open frontend: {e}")
        return False

def main():
    """Main startup function"""
    print("=" * 60)
    print("🛒 Cart Abandonment Recovery Demo")
    print("=" * 60)
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("⚠️  Continuing without installing requirements...")
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("⚠️  Backend not started. Frontend will work in demo mode.")
    
    # Open frontend
    if not open_frontend():
        print("❌ Failed to open frontend")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("🎉 Demo is ready!")
    print("=" * 60)
    print("📱 Frontend: index.html (opened in browser)")
    print("🔧 Backend API: http://localhost:5000")
    print("📊 Dashboard: dashboard.html")
    print("\n💡 Tips:")
    print("   - Click 'Try Live Demo' to simulate recovery")
    print("   - Click 'View Dashboard' to see real-time data")
    print("   - Backend provides realistic dummy data")
    print("\n🛑 Press Ctrl+C to stop the backend server")
    
    try:
        if backend_process:
            backend_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down...")
        if backend_process:
            backend_process.terminate()
        print("✅ Demo stopped")

if __name__ == "__main__":
    main()
