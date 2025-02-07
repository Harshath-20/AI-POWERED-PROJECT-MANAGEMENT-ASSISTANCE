# AI-Powered Project Management Assistant

## Overview
This project is an AI-driven assistant designed to help with project management by providing insights into project viability, success rates, and investment requirements. It uses AI models to analyze user queries and generate responses, specifically tailored for small-scale industrial projects.

## Features
- **AI-Powered Insights**: Uses AI models to process user queries and provide detailed responses.
- **Flask Backend**: A lightweight backend to handle user queries and communicate with the AI API.
- **Interactive UI**: A simple HTML/JavaScript-based front-end for user interaction.
- **Database Integration**: Supports MongoDB or SQLite for storing past queries and responses.
- **Customizable AI Responses**: Enhancements planned to refine AI-generated answers.

## Tech Stack
- **Python, Flask** - Backend API
- **Gemini AI API** - AI-based responses
- **MongoDB / SQLite** - Database
- **HTML, CSS, JavaScript** - Frontend

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-link.git
   cd project-management-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the API key:
   - Replace `your-gemini-api-key-here` in `config.py` with your actual API key.
4. Run the backend server:
   ```bash
   python server.py
   ```
5. Open `index.html` in a browser to interact with the chatbot.

## Future Enhancements
- Improve UI/UX for better interaction.
- Enhance AI model to provide better accuracy.
- Deploy as a cloud-based web service.

