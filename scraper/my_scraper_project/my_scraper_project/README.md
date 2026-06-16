# Scrapy Web Scraper Project

This project is a migration of a BeautifulSoup-based web scraper into a robust, clean, and highly scalable Scrapy project.

## Features Implemented
- **Scrapy Architecture:** Organized codebase using Spiders, Items, and Pipelines.
- **Pipeline Storage:** Cleans and writes incoming scraped data safely into a structured CSV file (`scraped_output.csv`).
- **Pagination Handling:** Automatically crawls through 4 consecutive pages of the target website.
- **Anti-Blocking System:** Custom download delays (2 seconds) and realistic User-Agent headers configured in `settings.py`.
- **Logging:** Leverages Scrapy's built-in logger to keep track of requests, page counts, and storage processes.

## How to Setup and Run This Scraper

### Prerequisites
Make sure you have Python installed on your Windows machine.

### 1. Set Up Virtual Environment & Activate
Navigate to the project directory using Windows PowerShell:
```powershell
# Set script execution policy if restricted
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the virtual environment
.\venv\Scripts\Activate.ps1