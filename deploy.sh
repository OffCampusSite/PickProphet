#!/bin/bash

# PickProphet Deployment Script
# This script helps you deploy your PickProphet application

set -e

echo "🚀 PickProphet Deployment Script"
echo "================================"

# Check if we're in the right directory
if [ ! -f "fantasy_draft_web_enhanced.py" ]; then
    echo "❌ Error: Please run this script from the PickProphet directory"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python installation
if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Creating template..."
    cat > .env << EOF
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url_here
SUPABASE_KEY=your_supabase_anon_key_here

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key_here
FLASK_ENV=production
EOF
    echo "📝 Created .env template. Please edit it with your Supabase credentials."
    echo "   Then run this script again."
    exit 1
fi

echo "✅ .env file found"

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Test the application
echo "🧪 Testing the application..."
python3 test_auth.py

# Set up Supabase if credentials are provided
if grep -q "your_supabase_project_url_here" .env; then
    echo "⚠️  Please update your .env file with real Supabase credentials"
    echo "   Then run this script again."
    exit 1
fi

echo "🔧 Setting up Supabase database..."
python3 setup_supabase_tables.py

# Ask user for deployment preference
echo ""
echo "🌐 Choose your deployment platform:"
echo "1. Railway (Recommended - Easiest)"
echo "2. Vercel"
echo "3. Heroku"
echo "4. Manual deployment"
echo "5. Test locally only"
echo ""
read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🚂 Deploying to Railway..."
        
        if ! command_exists railway; then
            echo "📦 Installing Railway CLI..."
            npm install -g @railway/cli
        fi
        
        echo "🔐 Logging into Railway..."
        railway login
        
        echo "🚀 Initializing Railway project..."
        railway init
        
        echo "📝 Setting environment variables..."
        railway variables set SUPABASE_URL=$(grep SUPABASE_URL .env | cut -d '=' -f2)
        railway variables set SUPABASE_KEY=$(grep SUPABASE_KEY .env | cut -d '=' -f2)
        railway variables set FLASK_SECRET_KEY=$(grep FLASK_SECRET_KEY .env | cut -d '=' -f2)
        railway variables set FLASK_ENV=production
        
        echo "🚀 Deploying..."
        railway up
        
        echo "✅ Deployment to Railway completed!"
        echo "   Your app should be live in a few minutes."
        ;;
        
    2)
        echo "⚡ Deploying to Vercel..."
        
        if ! command_exists vercel; then
            echo "📦 Installing Vercel CLI..."
            npm install -g vercel
        fi
        
        echo "🚀 Deploying..."
        vercel --prod
        
        echo "✅ Deployment to Vercel completed!"
        ;;
        
    3)
        echo "🦊 Deploying to Heroku..."
        
        if ! command_exists heroku; then
            echo "📦 Installing Heroku CLI..."
            echo "   Please install Heroku CLI from: https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        echo "🔐 Logging into Heroku..."
        heroku login
        
        echo "🚀 Creating Heroku app..."
        heroku create pickprophet-$(date +%s)
        
        echo "📝 Setting environment variables..."
        heroku config:set SUPABASE_URL=$(grep SUPABASE_URL .env | cut -d '=' -f2)
        heroku config:set SUPABASE_KEY=$(grep SUPABASE_KEY .env | cut -d '=' -f2)
        heroku config:set FLASK_SECRET_KEY=$(grep FLASK_SECRET_KEY .env | cut -d '=' -f2)
        heroku config:set FLASK_ENV=production
        
        echo "🚀 Deploying..."
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        
        echo "✅ Deployment to Heroku completed!"
        ;;
        
    4)
        echo "📋 Manual deployment instructions:"
        echo ""
        echo "1. Choose your deployment platform (Railway, Vercel, Heroku, etc.)"
        echo "2. Connect your GitHub repository"
        echo "3. Set these environment variables:"
        echo "   - SUPABASE_URL: $(grep SUPABASE_URL .env | cut -d '=' -f2)"
        echo "   - SUPABASE_KEY: $(grep SUPABASE_KEY .env | cut -d '=' -f2)"
        echo "   - FLASK_SECRET_KEY: $(grep FLASK_SECRET_KEY .env | cut -d '=' -f2)"
        echo "   - FLASK_ENV: production"
        echo "4. Deploy!"
        echo ""
        echo "See DEPLOYMENT_GUIDE.md for detailed instructions."
        ;;
        
    5)
        echo "🧪 Testing locally..."
        echo "Starting the application on http://localhost:4000"
        echo "Press Ctrl+C to stop"
        python3 fantasy_draft_web_enhanced.py
        ;;
        
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment process completed!"
echo ""
echo "📋 Next steps:"
echo "1. Test your deployed application"
echo "2. Set up monitoring and backups"
echo "3. Share with your league members"
echo ""
echo "📚 For more information, see DEPLOYMENT_GUIDE.md" 
        heroku login
        
        echo "🚀 Creating Heroku app..."
        heroku create pickprophet-$(date +%s)
        
        echo "📝 Setting environment variables..."
        heroku config:set SUPABASE_URL=$(grep SUPABASE_URL .env | cut -d '=' -f2)
        heroku config:set SUPABASE_KEY=$(grep SUPABASE_KEY .env | cut -d '=' -f2)
        heroku config:set FLASK_SECRET_KEY=$(grep FLASK_SECRET_KEY .env | cut -d '=' -f2)
        heroku config:set FLASK_ENV=production
        
        echo "🚀 Deploying..."
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        
        echo "✅ Deployment to Heroku completed!"
        ;;
        
    4)
        echo "📋 Manual deployment instructions:"
        echo ""
        echo "1. Choose your deployment platform (Railway, Vercel, Heroku, etc.)"
        echo "2. Connect your GitHub repository"
        echo "3. Set these environment variables:"
        echo "   - SUPABASE_URL: $(grep SUPABASE_URL .env | cut -d '=' -f2)"
        echo "   - SUPABASE_KEY: $(grep SUPABASE_KEY .env | cut -d '=' -f2)"
        echo "   - FLASK_SECRET_KEY: $(grep FLASK_SECRET_KEY .env | cut -d '=' -f2)"
        echo "   - FLASK_ENV: production"
        echo "4. Deploy!"
        echo ""
        echo "See DEPLOYMENT_GUIDE.md for detailed instructions."
        ;;
        
    5)
        echo "🧪 Testing locally..."
        echo "Starting the application on http://localhost:4000"
        echo "Press Ctrl+C to stop"
        python3 fantasy_draft_web_enhanced.py
        ;;
        
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment process completed!"
echo ""
echo "📋 Next steps:"
echo "1. Test your deployed application"
echo "2. Set up monitoring and backups"
echo "3. Share with your league members"
echo ""
echo "📚 For more information, see DEPLOYMENT_GUIDE.md" 
echo "After deployment, your app will be available at:"
echo "- Railway: https://your-app-name.railway.app"
echo "- Render: https://your-app-name.onrender.com"
echo "- Heroku: https://your-app-name.herokuapp.com"
echo ""
echo "Remember to:"
echo "1. Test your deployed app"
echo "2. Set up monitoring (optional)"
echo "3. Configure custom domain (optional)"
echo ""
echo "Good luck with your fantasy draft assistant! 🏈" 