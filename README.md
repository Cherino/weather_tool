# Weather API Data Analyser & Reporter

### 📌 Introduction
Developed as a group project for CIS 1702, this CLI and GUI application is a complete data pipeline that fetches raw weather data from public APIs, performs statistical analysis, and generates multi-format reports. Following the successful completion of the university coursework by the group "Git Happens", I have forked this repository to continue development and implement advanced features from the original roadmap.

### 🚀 Key Features
Dual Interface: Features a streamlined CLI and a GUI built with Tkinter.
Multi-API Integration: Fetches complex JSON payloads from Visual Crossing and Open Weather Map.
Reporting Engine: * Simple Report: Summary of conditions and min/max temps.
Detailed Report: Hourly breakdown and rain probability.
Smart Suggestions: A recommendation engine for clothing based on temperature data.
Data Persistence: Export capability for TXT, CSV, and JSON formats.
Comparison Tool: A dedicated function to compare historical data across different CSV reports.

### 👥 The Team: "Git Happens"
The project was a collaborative effort, with contributions ordered by project impact and engagement:

<b> Caileb Cook (Project Lead / DevOps) </b>Designed the core APIHandler class, built the data pipeline, and implemented the primary error-handling/logging framework. Managed repository structure and documentation.
<b>William Ellison (Core Logic & Diplomacy)</b> Developed the initial application drafts, created the date-range reporting modules, and provided essential team delegation and project originality.
<b>Isaac Ritchie (Data Analysis)</b> Developed the CSV comparison modules and implemented logic for managing file-save states and menu override prevention.
<b>Corey Mairs (Feature Development)</b> Designed the clothing recommendation system and contributed to the primary reporting functions with a focus on data quality.
<b>Benjamin Elliot (UI/UX Design)</b> Lead the transition from terminal-only to a Graphical User Interface (GUI) using the Tkinter module.
<b>Daniel Hassett (Documentation & Logging)</b> Contributed to the final reporting documentation and assisted with input sanitation and error logging configurations.

  

### 🛠️ Technical Stack
Language: Python 3.12+
Core Libraries: requests, tkinter, statistics, csv, json, logging.
APIs: Visual Crossing, Open Weather Map.

### 📂 Repository Structure
/main: The stable, integrated version of the application.
/legacy:
&nbsp; /legacy/code_snippets: Early prototypes and staging modules used during the iterative build process.
&nbsp; /legacy/personal_notes: Notes, comments and other odds and ends used for documentation and planning

### ⚙️ Installation & Usage

Clone the repo:
 ```git clone https://github.com/Cherino/Weather_API.git```

Install dependencies:
```pip install requests```

Run the application:
```python main.py```

### 📈 Future Roadmap
[ ] API Key Security: Migration to .env files for secure environment variable management.
[ ] Enhanced Storage: Implementing a UserQuery class to cache session data.
[ ] Visualizations: Adding Matplotlib support for temperature trend graphs.
[ ] SQL Server??
[ ] Map & Plot weather based on Lat/Lon
[ ] Allow User to plot on map and search for weather that way via Lat/Lon
[ ] Reintroduce Backup API (OpenWeatherAPI)
[ ] More Reporting Types
[ ] Clean up code and finish the UI implementation