# 🚇 Kanpur Metro Fare Database System

A clean, minimal, and practical Python data engineering project that fetches Kanpur Metro station and fare data from official UP Metro Rail APIs and stores it in a structured SQLite database for easy querying and analysis.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ FEATURES

• Automatic station data collection  
• Fare generation for all source → destination pairs  
• Weekday & weekend fare separation  
• Lightweight SQLite database  
• SQL-ready structured data  
• Ideal for college mini / major projects  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PROJECT PURPOSE

Metro fare information is generally scattered across apps and websites.  
This project converts that information into a single local database that can be:

• Queried using SQL  
• Used for fare comparison  
• Used for route analysis  
• Extended into backend services or applications  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🛠 TECH STACK

• Python 3  
• Requests (API communication)  
• SQLite3 (database)  
• REST APIs  
• SQL  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 APIs USED

Station List API  
https://portal.upmetrorail.com/en/api/v2/stations_by_keyword/2/

Fare & Distance API  
https://portal.upmetrorail.com/en/api/v2/travel_distance_time_fare/2/{FROM}/{TO}/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗄 DATABASE DESIGN

Database Name  
kanpur_metro.db

Table Name  
fare

Columns  
• id (Primary Key)  
• from_code  
• from_name  
• to_code  
• to_name  
• stations_between  
• weekday_fare  
• weekend_fare  

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 WORKING FLOW

Fetch station list  
↓  
Create SQLite database & table  
↓  
Generate all valid station pairs  
↓  
Call fare API for each pair  
↓  
Store fare data using bulk insertion  

Delay is added between API calls to avoid rate limiting.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

▶ HOW TO RUN

Install dependency  
pip install requests

Run script  
python kanpur_metro.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SAMPLE SQL QUERIES

DataBase 

![Screenshot](screenshot/Screenshot%202026-01-28%202.14.16%20PM.png)

Fare between two stations  
SELECT from_name, to_name, weekday_fare, weekend_fare, stations_between  
FROM fare  
WHERE from_name='IIT KANPUR' AND to_name='KALYANPUR METRO';

![Screenshot](screenshot/Screenshot%202026-01-28%202.24.58%20PM.png)

List all metro stations  
SELECT DISTINCT from_code, from_name  
FROM fare  
UNION  
SELECT DISTINCT to_code, to_name  
FROM fare  
ORDER BY from_name;

![Screenshot](screenshot/Screenshot%202026-01-28%202.19.12%20PM.png)

Cheapest routes  
SELECT from_name, to_name, weekday_fare  
FROM fare  
ORDER BY weekday_fare ASC;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 OUTPUT

• SQLite database file: kanpur_metro.db  
• fare table containing complete fare matrix  
• Fully queryable metro fare dataset  


⭐ Star the repository if you find this project useful
