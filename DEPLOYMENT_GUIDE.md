# PickProphet - Complete Deployment Guide

## 🚀 Quick Start

### 1. Fix Authentication Issues ✅
The logout functionality has been fixed and improved:

- **Fixed Routes**: Added proper `/logout` route that redirects to login page
- **Improved Auth**: Enhanced Supabase authentication with better error handling
- **User Management**: Added user info and auth check endpoints
- **Session Management**: Proper session clearing on logout

### 2. Set Up Supabase Database

#### Step 1: Create Supabase Project
1. Go to [supabase.com](https://supabase.com)
2. Create a new project
3. Note your project URL and anon key

#### Step 2: Configure Environment Variables
Create a `.env` file in your project root:

```env
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

# Flask Configuration
FLASK_SECRET_KEY=your_flask_secret_key_here
FLASK_ENV=production
```

#### Step 3: Set Up Database Tables
Run the setup script:

```bash
python3 setup_supabase_tables.py
```

This will create all necessary tables and security policies.

### 3. Configure Supabase Authentication

#### Step 1: Enable Email Authentication
1. Go to your Supabase dashboard
2. Navigate to Authentication > Settings
3. Enable "Enable email confirmations"
4. Configure email templates (optional)

#### Step 2: Set Up Email Templates (Optional)
1. Go to Authentication > Email Templates
2. Customize the confirmation and reset password emails
3. Test the email flow

### 4. Deploy to Production

## 🌐 Deployment Options

### Option 1: Railway (Recommended)

#### Step 1: Prepare for Railway
Create a `railway.json` file:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python fantasy_draft_web_enhanced.py",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

#### Step 2: Deploy
1. Install Railway CLI: `npm i -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Set environment variables in Railway dashboard
5. Deploy: `railway up`

### Option 2: Vercel

#### Step 1: Create vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "fantasy_draft_web_enhanced.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "fantasy_draft_web_enhanced.py"
    }
  ]
}
```

#### Step 2: Deploy
1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel --prod`

### Option 3: Heroku

#### Step 1: Create Procfile
```
web: python fantasy_draft_web_enhanced.py
```

#### Step 2: Deploy
1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Set environment variables
4. Deploy: `git push heroku main`

## 🔧 Environment Variables

Set these in your deployment platform:

```env
# Required
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_SECRET_KEY=your_secret_key_here

# Optional
FLASK_ENV=production
PORT=4000
```

## 📋 Pre-Deployment Checklist

- [ ] Supabase project created and configured
- [ ] Database tables set up using `setup_supabase_tables.py`
- [ ] Environment variables configured
- [ ] Email authentication enabled in Supabase
- [ ] Application tested locally
- [ ] All dependencies in `requirements.txt`

## 🧪 Testing Your Deployment

### 1. Test Authentication
1. Visit your deployed site
2. Try to register a new account
3. Check email confirmation (if enabled)
4. Test login functionality
5. Test logout functionality

### 2. Test Core Features
1. Initialize a draft
2. Draft some players
3. Test custom projections
4. Save and load drafts
5. Test recommendations

### 3. Test User Management
1. Create multiple user accounts
2. Verify data isolation between users
3. Test user-specific custom projections
4. Test completed drafts per user

## 🔒 Security Features

- ✅ Row Level Security (RLS) on all tables
- ✅ User authentication required for all data access
- ✅ Session-based authentication
- ✅ Password validation (minimum 6 characters)
- ✅ CSRF protection (Flask built-in)
- ✅ Secure session management
- ✅ Proper logout functionality

## 🐛 Troubleshooting

### Common Issues

#### 1. "Supabase credentials not found"
- Check your `.env` file has correct credentials
- Verify environment variables are set in deployment platform

#### 2. "relation does not exist" errors
- Run `python3 setup_supabase_tables.py` to create tables
- Check Supabase connection

#### 3. Authentication errors
- Verify Supabase Auth is enabled
- Check email confirmation settings
- Test with development mode first

#### 4. Logout not working
- Fixed in latest version
- Ensure you're using the updated templates
- Check browser console for errors

### Debug Mode
For local development, the app runs in debug mode without Supabase:

```bash
python3 fantasy_draft_web_enhanced.py
```

## 📊 Monitoring and Analytics

### Supabase Dashboard
- Monitor user registrations
- Check database usage
- View authentication logs
- Monitor API performance

### Application Logs
- Check deployment platform logs
- Monitor error rates
- Track user engagement

## 🚀 Next Steps After Deployment

1. **Set up monitoring** for your application
2. **Configure backups** for your Supabase database
3. **Set up custom domain** (optional)
4. **Configure SSL certificates** (usually automatic)
5. **Set up CI/CD pipeline** for automated deployments
6. **Create user documentation** for your league members
7. **Monitor performance** and optimize as needed

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review Supabase documentation
3. Check deployment platform logs
4. Test in development mode first

## 🎉 Success!

Your PickProphet application is now ready for production use with:

- ✅ Fixed logout functionality
- ✅ Proper Supabase authentication
- ✅ User management system
- ✅ Secure data isolation
- ✅ Production-ready deployment

Happy drafting! 🏈 
**Steps:**
1. Go to [railway.app](https://railway.app) and sign up
2. Connect your GitHub repository
3. Add environment variables:
   - `SUPABASE_URL` - Your Supabase project URL
   - `SUPABASE_KEY` - Your Supabase anon key
   - `FLASK_ENV` - Set to `production`
4. Deploy! Railway will automatically detect your Python app

### 2. **Render** (Great Alternative)
**Free tier**: 750 hours/month

**Steps:**
1. Go to [render.com](https://render.com) and sign up
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python fantasy_draft_web_enhanced.py`
   - **Environment Variables**: Same as Railway
5. Deploy!

### 3. **Heroku** (Classic Choice)
**Free tier**: Discontinued, but still popular

**Steps:**
1. Install Heroku CLI
2. Run: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set SUPABASE_URL=your_url
   heroku config:set SUPABASE_KEY=your_key
   heroku config:set FLASK_ENV=production
   ```
4. Deploy: `git push heroku main`

## 🔧 Required Setup

### 1. Supabase Database Setup
Your app already uses Supabase for cloud storage. Make sure to:

1. **Create Supabase Project**:
   - Go to [supabase.com](https://supabase.com)
   - Create new project
   - Get your URL and anon key

2. **Set Environment Variables**:
   ```bash
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-anon-key-here
   ```

3. **Database Tables** (Auto-created):
   - `custom_projections` - User custom projections
   - `users` - User accounts (if you add auth)

### 2. Data Migration
Your app currently stores some data locally. For production:

- ✅ **Custom Projections**: Already in Supabase
- ✅ **User Data**: Already in Supabase  
- ⚠️ **CSV Files**: Need to be included in deployment

## 📁 File Structure for Deployment

Your current structure is deployment-ready:
```
├── fantasy_draft_web_enhanced.py  # Main app
├── supabase_manager.py            # Database layer
├── requirements.txt               # Dependencies
├── templates/                     # HTML templates
├── *.csv                         # Player data files
├── railway.json                  # Railway config
├── Procfile                      # Heroku config
└── runtime.txt                   # Python version
```

## 🌐 Domain & SSL

All recommended platforms provide:
- ✅ Automatic HTTPS/SSL
- ✅ Custom domains (optional)
- ✅ CDN for static files

## 📊 Monitoring & Scaling

### Railway
- Built-in monitoring dashboard
- Auto-scaling based on usage
- Logs available in dashboard

### Render
- Health checks
- Auto-restart on failures
- Performance metrics

### Heroku
- Heroku logs: `heroku logs --tail`
- Add-ons for monitoring
- Dyno scaling options

## 🔒 Security Considerations

1. **Environment Variables**: Never commit secrets to Git
2. **Supabase RLS**: Enable Row Level Security in Supabase
3. **HTTPS**: All platforms provide this automatically
4. **Session Security**: Your app uses Flask sessions (good)

## 💰 Cost Estimates

### Railway
- Free tier: $5/month credit
- Small app: ~$10-20/month

### Render
- Free tier: 750 hours/month
- Small app: ~$7/month

### Heroku
- Basic dyno: $7/month
- Add-ons: $5-20/month

## 🚀 Quick Start Commands

### Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### Render
```bash
# Just connect GitHub repo and deploy via web interface
# No CLI required for basic deployment
```

### Heroku
```bash
# Install Heroku CLI
# Create app
heroku create your-fantasy-draft-app

# Set environment variables
heroku config:set SUPABASE_URL=your_url
heroku config:set SUPABASE_KEY=your_key

# Deploy
git push heroku main
```

## 🐛 Troubleshooting

### Common Issues:

1. **Port Issues**: Fixed with `PORT` environment variable
2. **Missing Dependencies**: Check `requirements.txt`
3. **Database Connection**: Verify Supabase credentials
4. **File Paths**: All CSV files must be in root directory

### Debug Commands:
```bash
# Check logs
railway logs
# or
heroku logs --tail

# Check environment variables
railway variables
# or  
heroku config
```

## 📈 Next Steps After Deployment

1. **Set up monitoring** (optional)
2. **Configure custom domain** (optional)
3. **Set up backups** for Supabase data
4. **Add analytics** (Google Analytics, etc.)
5. **Set up CI/CD** for automatic deployments

Your app is well-architected for cloud deployment! The Supabase integration means all user data will be stored in the cloud, not locally. Choose Railway for the easiest deployment experience. 