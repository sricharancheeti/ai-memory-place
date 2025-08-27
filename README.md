# AI Memory Palace 🏰 (Neuro-AR Lite)

Transform any PDF or technical manual into an interactive 3D knowledge palace you can walk through. This project turns passive reading into an active, spatial experience.

_**Status:** Currently in the 1-week MVP development phase._

> **Note:** A live demo and video will be available at the end of the 7-day build.

---

### ## The Core Concept

The ancient "Method of Loci," or memory palace, is a mnemonic device that uses spatial visualization to recall information. This project is a modern, AI-powered implementation of that technique.

You upload a boring document, and the application:
1.  **Analyzes** the content, breaking it down into logical sections.
2.  **Builds** a virtual 3D world where each section becomes a unique "room."
3.  **Populates** each room with interactive objects representing key concepts.
4.  **Narrates** a summary when you interact with an object, bringing the information to life.

Suddenly, you're not just reading a manual—you're exploring it.

### ## 🎯 MVP Goal (1-Week Sprint)

The goal for this initial sprint is to create a functional proof-of-concept:
* **Upload** a PDF document.
* **Backend** parses the document into sections/chapters.
* **Frontend** dynamically generates a basic 3D world with one cube "room" per section.
* Each room contains clickable objects that trigger a short, AI-generated narration of that section's content.

### ## 🛠️ Tech Stack

* **Frontend:** Angular + Three.js
* **Backend:** FastAPI (Python)
* **PDF Parsing:** `PyPDF2` or `pdfplumber`
* **LLM Narration:** Hugging Face `distilbart-cnn` (or a simple stub for the MVP)
* **Deployment:** Docker, GitHub Pages (Frontend), Render/Heroku (Backend)

---

### ## 📅 Project Roadmap & Build Log

This project is being built in a public 7-day sprint.

* **[x] Day 1: Project Setup & CI/CD**
    * Scaffold Angular and FastAPI apps.
    * Set up Docker Compose for local development.
    * Create a basic CI pipeline with GitHub Actions.

* **[ ] Day 2: PDF Parsing Backend**
    * Create an endpoint to upload a PDF.
    * Implement logic to extract text and split it into sections.
    * Return a JSON structure of the document's layout.

* **[ ] Day 3: LLM Narration Service**
    * Integrate a small, free LLM to summarize text sections.
    * Update the API to include a "narration" field for each section.

* **[ ] Day 4: 3D World Scaffolding**
    * Set up a basic Three.js scene in Angular.
    * Add movement controls (WASD/Orbit).
    * Create placeholder geometry for rooms and objects.

* **[ ] Day 5: Backend ↔ Frontend Integration**
    * Connect the frontend to the backend API.
    * Dynamically generate the 3D world based on the JSON received after a PDF upload.

* **[ ] Day 6: Narration & Interaction**
    * Implement click/hover events on 3D objects.
    * Display narrations in a UI element (tooltip or sidebar).
    * *Bonus:* Use the browser's Text-to-Speech API to speak the narration.

* **[ ] Day 7: Polish, Deploy & Demo**
    * Clean up the UI and add basic instructions.
    * Deploy the frontend to GitHub Pages and the backend to Render.
    * Record a short video demo for this README.

### ## 🚀 How to Run Locally

This project is fully containerized, so you only need Docker installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-memory-palace.git](https://github.com/your-username/ai-memory-palace.git)
    cd ai-memory-palace
    ```

2.  **Build and run the services:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the application:**
    * Frontend will be running at `http://localhost:4200`
    * Backend API will be running at `http://localhost:8000`

### ## 🌟 Stretch Goals (Post-MVP)

* More realistic 3D environments (walls, textures, lighting).
* A minimap to navigate the knowledge palace.
* LLM-powered "quiz mode" where objects ask you questions.
* Multiplayer mode to walk through a document with others.