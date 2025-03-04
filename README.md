# 🚀 AI-Powered SQL Query Generator  

An **AI-powered** tool that converts **plain English questions** into **SQL queries** and fetches results from a database using **Google Gemini Pro**.

---

# Demo▶️ : [Here](https://huggingface.co/spaces/1Prarthana/AI-Powered-SQL-Query-Generator)
 
---

## 🔥 How It Works  
1️⃣ **Enter** a question in plain English.  
2️⃣ **AI** converts it into an SQL query.  
3️⃣ **App** executes the query and fetches results.  
4️⃣ **Get** your answer instantly! 🎯  

---

## ✨ Features  
✅ Converts natural language queries to SQL.  
✅ Executes queries on an SQLite database.  
✅ Fetches and displays query results.  
✅ Powered by **Google Gemini Pro**.  
✅ Simple **Streamlit UI**.  
✅ **Fast and accurate** query execution.  

---
# 📸Demo Screenshot:
![Screenshot 2025-03-04 135448](https://github.com/user-attachments/assets/0644d2ac-bf25-458e-a850-1d39d78a3d13)
![Screenshot 2025-03-04 135619](https://github.com/user-attachments/assets/6c89b16d-3bec-40d6-b901-074221c3f9d2)


---

## 🛠️ Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Prarthana-Singh/AI-Powered-SQL-Query-Generator.git
cd AI-Powered-SQL-Query-Generator
```
2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```
3️⃣ **Setup the database**
```bash
python sqlite.py
```
4️⃣ **Run the application**
```bash
streamlit run app.py
```
---

# 🖥️ Usage
1️⃣. Open Streamlit App in your browser.\
2️⃣. Enter a natural language question (e.g., "Show all students studying Data Science").\
3️⃣. Click "Get SQL Query & Fetch Data".\
4️⃣. AI converts your question into an SQL query.\
5️⃣. The app executes the query and displays results.

---
# 🤖 Technologies Used
1. Python (Streamlit, SQLite)
2. Google Gemini Pro (AI Model for query generation)
3. Streamlit (User Interface)
4. SQLite (Database)

---
# 📁 AI-Powered-SQL-Query-Generator
│── app.py              # Main Streamlit App\
│── sqlite.py           # SQLite Database Setup\
│── sqlite_copy.py      # Database Backup\
│── sql.py              # Query Execution Script\
│── students.db         # SQLite Database File\
│── requirements.txt    # Dependencies\
│── README.md           # Project Documentation
