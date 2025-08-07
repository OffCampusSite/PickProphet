# James Clessuras Drafter
## Fantasy Football Draft Assistant

A complete fantasy football draft assistant application with advanced features including player projections, custom projections, draft simulation, and more.

### 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python3 start.py
   ```
   OR
   ```bash
   python3 fantasy_draft_web_enhanced.py
   ```

3. **Open Your Browser:**
   Go to: http://localhost:6970

### 📁 Files Included

- **`fantasy_draft_web_enhanced.py`** - Main Flask application
- **`fantasy_draft_assistant_v2.py`** - Core draft assistant logic
- **`supabase_manager.py`** - Database management
- **`templates/`** - All HTML templates
- **`*.csv`** - FantasyPros player projections data
- **`*.json`** - Configuration and data files
- **`start.py`** - Easy startup script

### 🎯 Features

- **Pre-Draft Analysis** - View and customize player projections
- **Live Draft Room** - Real-time draft with AI recommendations
- **Position Filtering** - Filter players by position (QB, RB, WR, TE, K, DST)
- **Custom Projections** - Edit individual player stats and projections
- **Draft Simulation** - AI-powered draft recommendations
- **User Profiles** - Save and view completed drafts
- **Minimalist Roster Display** - Clean, organized roster view

### 🔧 Configuration

- **Port:** 6970 (configurable in `fantasy_draft_web_enhanced.py`)
- **Database:** Local JSON files (no external database required)
- **Data Source:** FantasyPros projections

### 📊 Data Files

- **FantasyPros CSV files** - Player projections by position
- **`custom_projections.json`** - User customizations
- **`completed_drafts.json`** - Saved draft data

### 🎮 Usage

1. **Pre-Draft Page** (`/pre-draft`)
   - View all players with projections
   - Filter by position
   - Customize player projections
   - Sort by ADP, PPR, Half-PPR, or Standard scoring

2. **Draft Room** (`/`)
   - Live draft interface
   - AI recommendations
   - Real-time updates
   - Save drafts when complete

3. **User Profile** (`/user`)
   - View saved drafts
   - Expandable roster display
   - Minimalist design

### 🛠️ Troubleshooting

- **Port already in use:** Change port in `fantasy_draft_web_enhanced.py`
- **Missing dependencies:** Run `pip install -r requirements.txt`
- **Data not loading:** Check CSV files are present

### 📝 Notes

- All data is stored locally in JSON files
- No external database setup required
- Application runs on port 6970 by default
- Includes all necessary templates and static files

### 🎉 Ready to Draft!

The application is fully self-contained and ready to run. Just install dependencies and start the server! 