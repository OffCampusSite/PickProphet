# PickProphet - Fantasy Football Draft Assistant

A comprehensive fantasy football draft assistant with pre-draft analysis and player customization features.

## Features

- **Pre-Draft Analysis**: Analyze and customize player projections before the draft
- **Player Customization**: Edit individual player stats and see recalculated projections
- **Multiple Scoring Formats**: PPR, Half-PPR, and Standard scoring calculations
- **FantasyPros Integration**: Uses FantasyPros CSV data for accurate projections
- **Real-time Calculations**: Points recalculate immediately when stats are modified
- **Reset Functionality**: Reset all players to FantasyPros default data

## Files Included

### Core Application Files
- `fantasy_draft_web_enhanced.py` - Main Flask application
- `fantasy_draft_assistant_v2.py` - Core draft assistant logic
- `requirements.txt` - Python dependencies

### Data Files
- `WeeklyFantasyFootballCheatingSheet.csv` - Primary player data with ADP
- `FantasyPros_Fantasy_Football_Projections_QB.csv` - QB projections
- `FantasyPros_Fantasy_Football_Projections_RB.csv` - RB projections
- `FantasyPros_Fantasy_Football_Projections_WR.csv` - WR projections
- `FantasyPros_Fantasy_Football_Projections_TE.csv` - TE projections
- `FantasyPros_Fantasy_Football_Projections_K.csv` - Kicker projections
- `FantasyPros_Fantasy_Football_Projections_DST.csv` - Defense projections

### Templates
- `templates/` - HTML templates for the web interface

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python3 fantasy_draft_web_enhanced.py
   ```

3. **Access the Application**:
   - Open your browser and go to: `http://localhost:6971`
   - Navigate to `/pre-draft` for the pre-draft analysis page

## Usage

### Pre-Draft Analysis
1. Click "Load Players" to load all player data
2. Use filters to search by position, sort by ADP/points
3. Click the edit icon next to any player to customize their stats
4. Save changes to see recalculated projections
5. Use "Reset All Player Data" to return to FantasyPros defaults

### Player Customization
- Edit individual stats (passing yards, receptions, etc.)
- See real-time point calculations for PPR, Half-PPR, and Standard
- Customized players show a green "Customized" badge
- All changes are saved and persist across sessions

## Scoring Formats

- **PPR**: Full point per reception
- **Half-PPR**: Half point per reception  
- **Standard**: No reception points

## Data Sources

- **Primary**: WeeklyFantasyFootballCheatingSheet.csv (ADP, basic info)
- **Projections**: FantasyPros CSV files (detailed stats for calculations)

## Troubleshooting

- If you get "Address already in use" errors, the app is already running
- Make sure all CSV files are in the same directory as the Python files
- Check that all dependencies are installed via `pip install -r requirements.txt` 