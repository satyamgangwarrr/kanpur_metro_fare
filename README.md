# 🚇 Kanpur Metro Fare Data Collector

This project fetches **Kanpur Metro station details and fare information** from the official **UP Metro Rail API** and stores the complete fare matrix in a local **SQLite database**.

It automatically:
- Fetches all metro stations
- Calculates fares between **every source → destination pair**
- Stores weekday & weekend fares along with station count

---

## 📌 Features

- ✅ Fetches all Kanpur Metro stations via public API  
- ✅ Retrieves fare, distance, and station count for every route  
- ✅ Stores structured data in SQLite (`kanpur_metro.db`)  
- ✅ Handles API rate limits with controlled delays  
- ✅ Easy to query and analyze later  

---

## 🛠 Tech Stack

- **Python 3**
- **Requests** – API calls  
- **SQLite3** – Local database  
- **REST APIs** – UP Metro Rail  

