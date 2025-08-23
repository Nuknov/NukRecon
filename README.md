# NukRecon

A lightweight recon tool to discover **subdomains** and **hidden directories**.  
It checks both the normal pattern (`sub.domain.com`) and a “reversed” pattern (`domain.com.word`) to raise awareness about look-alike / chained domains often used for phishing.

---

## 1) What I found (real-world examples)
During research, I observed these live/registered patterns, these patterns are considered the phishing pages:

- https://instagram.com.blog/  
- https://instagram.com.xyz/  
- https://www.microsoft.com.blog/  
- https://www.google.com.xyz/  
- https://google.com.xyz/  
- https://testfire.net.download/#/page-not-found  
- https://google.com.store/  
- http://youtube.com.blog/  
- http://youtube.com.store/  

Following are the proof of above phishing page, I founf using this tool:
<img width="1280" height="1024" alt="SUS 1" src="https://github.com/user-attachments/assets/1d8d0980-9290-4dfd-b758-735627f86ec8" />
<img width="1280" height="1024" alt="SUS" src="https://github.com/user-attachments/assets/49359c06-e96f-47d6-819f-89d5520b2d2b" />
<img width="1280" height="1024" alt="SUS 2" src="https://github.com/user-attachments/assets/804d01e5-61fb-4cb8-a11e-b943770aaa8e" />


---

## 2) Features
- Normal pace scan for **subdomains** and **directories**
- Tries **normal** (`sub.domain.com`) and **reversed** (`domain.com.word`) patterns
- Shows only **live** results (HTTP status `< 400`)
- Option to **save results** to `.txt`
- Minimal setup (just `requests` + `colorama`)

---

## 3) Requirements
- Python 3.8+  
- `pip` (Python package manager)

---

## 4) Install (step by step)
```bash
# 1) Clone this repository
git clone https://github.com/Nuknov/NukRecon.git

# 2) Go into the project folder
cd NukRecon

# 3) (Optional for linux/macOS but recommended) create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4) Install dependencies
pip install -r requirements.txt

# 5) Run the tool
python redrecon or python3 redrecon

