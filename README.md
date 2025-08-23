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

Following are the proof of above phishing page, I found using this tool:
<img width="1045" height="277" alt="SUS 1" src="https://github.com/user-attachments/assets/813e1028-4975-43a0-977e-781aef1ac9b5" />
<img width="1037" height="619" alt="SUS" src="https://github.com/user-attachments/assets/068494dc-91c5-4a67-bc76-6e38364bd167" />
<img width="1077" height="589" alt="SUS 2" src="https://github.com/user-attachments/assets/c4cdc89e-cdcc-4fa8-a925-57cab077e106" />
<img width="1167" height="504" alt="SUS 3" src="https://github.com/user-attachments/assets/a58d2194-9280-4c3b-99a2-6dd5e2e3c1d0" />



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
```
```
# 2) Go into the project folder
cd NukRecon
```
```
# 3) (Optional for linux/macOS but recommended) create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```
```
# 4) Install dependencies
pip install -r requirements.txt
```
```
# 5) Run the tool
python redrecon or python3 redrecon
```

---
## 5) **Proof of concept**: You can see the tool in action below.
<img width="473" height="795" alt="SUBDOMAIN" src="https://github.com/user-attachments/assets/1ae8ba37-e966-429c-bcfd-a96a0e883367" />
<img width="519" height="795" alt="PATHSCANNER" src="https://github.com/user-attachments/assets/a903ff27-f73f-48a6-a6ac-e697864987cc" />


## ⚠️ Disclaimer

NukRecon is intended **solely for educational purposes, security research, and authorized testing**.  

The tool is designed to help researchers, students, and security professionals **understand subdomain structures, directory paths, and potential phishing patterns**.  

By using NukRecon, you agree to the following:  
1. You will **only scan domains you own** or have **explicit permission** to test.  
2. You will **not use this tool for illegal or malicious activities**.  
3. The author is **not responsible for any misuse or damage** resulting from unauthorized usage.  

Always act ethically, responsibly, and within the boundaries of the law.









