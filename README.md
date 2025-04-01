The QuickFind - Custom Search Engine

The QuickFind is a lightweight and efficient search engine built using Flask and the Google Custom Search API. It provides a user-friendly interface with multiple search categories and a responsive design for a seamless search experience.

Features
* Search Categories: Web, Images, News, Videos
* Pagination: Navigate between search results pages
* Responsive UI: Google-like interface with modern design

Technologies Used
* Backend: Python (Flask)
* Frontend: HTML, CSS

Installation & Setup

Prerequisites
* Python 3.x installed
* A Google Custom Search API key and CSE ID

Steps
1. Clone the repository:

git clone https://github.com/gracy1305/QuickFind.git
cd QuickFind
2. Install dependencies:
pip install -r requirements.txt
3. Configure API credentials in app.py:
API_KEY = "your-API-KEY"
CSE_ID = "your-CSE-ID"
4. Run the application:
python app.py
5. Open http://127.0.0.1:5000/ in your browser.

Project Structure

Future Enhancements
* Dynamic search suggestions
* Dark/Light mode toggle
* Search History feature
* Save & Share search results
* Improved error handling
License
This project is licensed under the MIT License.


