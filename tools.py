## tools.py (fixed)

# Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

# PDFLoader for reading PDF files
try:
    from langchain_community.document_loaders import PDFLoader
except Exception:
    # If langchain_community isn't available, raise a helpful error at runtime.
    # The import is placed in try/except to avoid failing at module import time on machines
    # where the package isn't installed yet.
    PDFLoader = None

from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class BloodTestReportTool:
    @staticmethod
    def read_data_tool(path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path (synchronous).

        Args:
            path (str): Path of the pdf file.

        Returns:
            str: Full Blood Test report file text
        """
        if PDFLoader is None:
            raise ImportError(
                "Missing dependency: langchain_community.document_loaders.PDFLoader is not available. "
                "Install `langchain-community` or the package that provides PDFLoader."
            )

        if not os.path.exists(path):
            raise FileNotFoundError(f"PDF file not found: {path}")

        docs = PDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content or ""
            # Remove duplicate blank lines
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report.strip()

## Creating Nutrition Analysis Tool
class NutritionTool:
    @staticmethod
    def analyze_nutrition_tool(blood_report_data: str) -> str:
        # Process and analyze the blood report data (placeholder)
        processed_data = blood_report_data

        # Clean up double spaces
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

## Creating Exercise Planning Tool
class ExerciseTool:
    @staticmethod
    def create_exercise_plan_tool(blood_report_data: str) -> str:
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"
