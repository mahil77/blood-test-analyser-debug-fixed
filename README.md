# Blood Test Analyser (Debugged & Fixed)

## This project is a Blood Test Report Analysis System built using FastAPI and CrewAI.
It was provided as a debug challenge with multiple issues in the codebase.
I identified and fixed all bugs, ensuring the system now runs smoothly.

### Bugs Found & Fixes Applied
1. Environment & Dependencies

Bug: requirements.txt had missing/incorrect libraries.

Fix: Cleaned dependencies, pinned correct versions (e.g., fastapi, uvicorn, crewai, crewai-tools).

2. Uvicorn Not Recognized

Bug: uvicorn command not available.

Fix: Installed uvicorn inside the virtual environment and ran as:uvicorn main: app --reload
3. Missing FastAPI Module

Bug: ModuleNotFoundError: No module named 'fastapi'.

Fix: Installed FastAPI and ensured it was listed in requirements.txt.


4. Incorrect Tool Definitions

Bug: BloodTestReportTool.read_data_tool was used incorrectly.

Fix: Adjusted method definitions and imports for proper usage.

5. CrewAI Agent Misconfigurations

Bug: The llm variable is undefined, and the tools are not attached properly.

Fix: Defined placeholder LLM integration and corrected tool usage in agents.

6. Git Issues (Author/Push)

Bug: Commits were showing under another username.

Fix: Reconfigured Git user, amended commit author, and force-pushed.

Setup Instructions
1. Clone the Repository
git clone https://github.com/mahil77/blood-test-analyser-debug-fixed.git
cd blood-test-analyser-debug-fixed

2. Create Virtual Environment
python -m venv venv


Activate it:

Windows (PowerShell):

.\venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3. Install Requirements
pip install -r requirements.txt

4. Run the API
uvicorn main: app --reload


The API will run at: http://127.0.0.1:8000

API Documentation
GET /

Health check endpoint.

Response:

{ "message": "Blood Test Report Analyser API is running" }

POST /analyze

Upload a blood test report (PDF) and receive analysis.

Request (Form Data):

File: PDF file of the blood test report

Query: Custom query (optional, default: "Summarise my Blood Test Report")

Response:

{
  "status": "success",
  "query": "Summarise my Blood Test Report",
  "analysis": "Detailed AI-generated health insights",
  "file_processed": "blood_report.pdf"
}
