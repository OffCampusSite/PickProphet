# 🚀 PickProphet Deployment Guide

## GitHub Upload Instructions

### 1. Initialize Git Repository
```bash
cd /Users/gclessuras/Desktop/PickProphetFolder
git init
git remote add origin https://github.com/egclessuras-svg/PickProphet.git
```

### 2. Add All Files
```bash
git add .
git commit -m "Initial commit: PickProphet Fantasy Draft Assistant"
```

### 3. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## Railway Deployment Instructions

### 1. Connect Railway to GitHub
1. Go to [Railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `egclessuras-svg/PickProphet`

### 2. Configure Environment Variables (Optional)
In Railway dashboard, go to Variables tab and add:
```
FLASK_SECRET_KEY=your-secret-key-here
SUPABASE_URL=your-supabase-url (if using database)
SUPABASE_KEY=your-supabase-key (if using database)
```

### 3. Deploy
- Railway will automatically detect the Python app
- It will use the `Procfile` and `railway.json` for configuration
- The app will be available at your Railway domain

## Files Included in Repository

### Core Application Files
- ✅ `fantasy_draft_web_enhanced.py` - Main Flask app
- ✅ `fantasy_draft_assistant_v2_clean.py` - Draft logic
- ✅ `supabase_manager.py` - Database management
- ✅ `rankings.csv` - Player data (392 players)

### Templates
- ✅ `templates/` - All HTML templates
- ✅ `templates/index.html`
- ✅ `templates/login.html`
- ✅ `templates/register.html`
- ✅ `templates/pre_draft.html`
- ✅ `templates/draft.html`
- ✅ `templates/user.html`

### Configuration Files
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Railway deployment
- ✅ `railway.json` - Railway configuration
- ✅ `.gitignore` - Git ignore rules
- ✅ `README.md` - Project documentation

### Excluded Files (via .gitignore)
- ❌ `__pycache__/` - Python cache
- ❌ `*.log` - Log files
- ❌ `player_projections_cache.json` - Runtime cache
- ❌ `completed_drafts.json` - User data
- ❌ `.env` - Environment variables

## Verification Checklist

Before pushing to GitHub, verify:

- [ ] App runs locally with `python3 run_port_5201.py`
- [ ] All 392 players load from `rankings.csv`
- [ ] Web interface accessible at http://localhost:5201
- [ ] No sensitive data in repository
- [ ] All dependencies in `requirements.txt`
- [ ] Railway configuration files present

## Post-Deployment

After Railway deployment:

1. **Test the live app** - Verify all features work
2. **Check logs** - Monitor for any errors
3. **Update domain** - Configure custom domain if needed
4. **Monitor performance** - Check Railway metrics

## Troubleshooting

### GitHub Issues
- Ensure repository is public
- Check file permissions
- Verify .gitignore is working

### Railway Issues
- Check build logs for errors
- Verify environment variables
- Ensure PORT variable is set
- Check health check endpoint

## Support

For deployment issues:
1. Check Railway logs
2. Verify GitHub repository
3. Test locally first
4. Contact support if needed

---

**Ready to deploy!** 🚀