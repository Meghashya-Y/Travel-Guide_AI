## 🌍 Travel Guide AI

Intelligent AI-Powered Travel Itinerary Generator

---

## 📌 Overview

Travel Guide AI is a web-based intelligent travel planning application built using Streamlit and Google Gemini AI (LLM API).

The system allows users to:

* Select Indian states and destinations

* Generate structured day-wise itineraries

* Receive AI-generated travel insights

* Plan trips interactively through a clean UI

This project demonstrates the practical integration of Generative AI in the tourism domain.

---

## 🚀 Live Demo

(Add Streamlit Cloud / deployed link here if available)

🧠 Key Features

✔ State-wise destination selection
✔ Dynamic day-wise itinerary generation
✔ Integration with Google Gemini AI
✔ Clean and responsive Streamlit UI
✔ Secure API key management using .env
✔ Modular Python architecture

---

## 🏗️ System Architecture

```bash

User Input (Streamlit UI)
        ↓
Input Processing
        ↓
Itinerary Generator (Rule-based)
        ↓
Gemini AI API (LLM-based Response)
        ↓
Formatted Travel Plan Display

```

---

## 🛠️ Tech Stack

| Layer           | Technology                  |
| --------------- | --------------------------- |
| Frontend        | Streamlit                   |
| Backend         | Python                      |
| AI Model        | Google Gemini Pro (LLM API) |
| Environment     | dotenv                      |
| Version Control | Git & GitHub                |

---

## 📂 Project Structure

``` plain text
Travel-Guide-AI/
│
├── app.py                  # Main Streamlit Application
├── itinerary_generator.py  # Rule-based itinerary logic
├── text_gemini.py          # Gemini API integration
├── background.jpg          # UI background asset
├── .env                    # API key storage
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

```
---

## 🔍 How It Works

1️⃣ User Selection

* The user selects:

* State

* Destination

* Number of travel days

2️⃣ Itinerary Generation

The system:

* Uses structured looping logic

* Creates a day-wise travel schedule

3️⃣ AI Enhancement

Google Gemini AI:

* Generates intelligent descriptions

* Provides contextual travel suggestions

4️⃣ Output Display

Streamlit renders:

* Clean formatted itinerary

* AI-generated travel insights

---

## ⚙️ Installation & Setup

Step 1: Clone the Repository

``` bash
git clone https://github.com/Kranthipolanki/Travel-Guide-Ai.git
cd Travel-Guide-Ai
```

Step 2: Create Virtual Environment (Recommended)

``` bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Step 3: Install Dependencies

``` bash
pip install -r requirements.txt
```

Step 4: Add Gemini API Key

Create a .env file:

``` bash

GOOGLE_API_KEY=your_api_key_here

```

Step 5: Run the Application

```bash
streamlit run app.py
```
---

## 🧪 Testing

The project has been tested for:

* Correct itinerary generation

* API connectivity validation

* UI responsiveness

Error handling for missing API keys

---

## 📊 Current Limitations

* No personalized recommendation engine

* Static destination data (dictionary-based)

* No database integration

* No collaborative filtering

* No travel API integration (future scope)

---

## 🔮 Future Enhancements

* Add content-based recommendation system

* Integrate real-time travel APIs

* Add hotel & transport suggestions

* Implement user login & preference storage

* Convert to full-stack production deployment

* Deploy on Streamlit Cloud / AWS

---

## 📚 Academic Relevance

This project demonstrates:

* Generative AI integration in web applications

* Prompt-based LLM usage

* Modular software design

* Agile development methodology

* AI-assisted decision support systems

---

## 👥 Team Details

Team ID: LTVIP2026TMIDS88672
Team Size: 5

Team Leader : Kranthi Polanki

Team Member : Bodanapu Venkata Keerthana

Team Member : Meghashya Yarasani

Team Member : Harshitha Raghava

Team Member : Sulaiman Shaik

---

## 📜 License

This project is developed for academic and learning purposes.

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to fork and improve!

---
