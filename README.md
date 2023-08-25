
# Project Title

EVTX_Forensics_View is a tool for Incident responders and Security analysts to provide a better way to take a raw windows event viewer file (.evtx) and process it into a sqlite DB, this can then be used to provide a better interface for forensic analysis of the logs themselves.



## Requirements
* Recent version of python 
* Powershell V 5.1+
* Python packages:json, sqlite3, sys, re (pip install -r requirements.txt)
* A way to open and view the sqlite3 .DB file (MSAccess, DB4S, VScode sqlite Viewer Extension)
## Usage
1. Clone the repository:
```
git clone 
```
2. Change Directory into the cloned repository:
```
cd EVTX_Forensics_View
```
3. Install the required Python packages:
```
pip install -r requirements.txt
```
4. Run the conversion using the full file path:
```
evtx_forensic.ps1 -infile <evtx file Path>
```
5. Use the Forensics.db in your software of choice.
## To Do
1. output a basic forensic analysis of the DB 
- When the log was last cleared (Oldest log date)
- Login numbers by user?
- a few basic detection rules as SQL queries 
2. Build a front end? 
- tkinter 
- py basic GUI 
3. automated analysis through machine learning 
- good luck 

