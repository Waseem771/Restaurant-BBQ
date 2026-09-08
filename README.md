# ?? Restaurant BBQ Analytics & AI Dashboard

A full-stack Business Intelligence (BI) platform tailored for a BBQ Restaurant. This application features real-time analytics, anomaly detection, sales forecasting, and an embedded **AI Assistant** capable of translating natural language questions into data-driven insights.

![Dashboard Preview](https://via.placeholder.com/1000x500.png?text=BBQ+Analytics+Dashboard)

## ? Features
- **Interactive KPI Dashboards**: Real-time visualizations of sales, orders, and product performance using Recharts.
- **AI-Powered Assistant**: Ask questions like *"What was our best selling item last month?"* and the AI will analyze your SQLite database and respond with insights.
- **Anomaly Detection**: Automated detection of unusual sales patterns.
- **Forecasting**: Predict future trends based on historical data using `scikit-learn`.
- **Fully Dockerized**: Ready to be deployed anywhere with a single command.

## ??? Tech Stack
- **Frontend**: React 18, Vite, Recharts, Lucide Icons
- **Backend**: Python 3.11, FastAPI, SQLite, Pandas, Scikit-Learn
- **AI Integration**: Groq (Llama/Mixtral) and Anthropic (Claude) APIs
- **Deployment**: Docker, Modal, Vercel, AWS EC2

---

## ?? Quickstart (Local Development)

The easiest way to run the entire application locally is using **Docker**.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Waseem771/Restaurant-BBQ.git
   cd Restaurant-BBQ
   ```

2. **Set up Environment Variables:**
   Copy `.env.example` to `.env` (if applicable) or create a `.env` file in the root directory:
   ```env
   JWT_SECRET_KEY=your_super_secret_key_here
   GROQ_API_KEY=your_groq_api_key
   LLM_PROVIDER=groq
   ```

3. **Run with Docker Compose:**
   ```bash
   docker-compose up -d --build
   ```

4. **Access the App:**
   - **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
   - **Backend API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

**Default Login:**
- Username: `admin`
- Password: `iba@12345678`

---

## ?? Deployment Guides

This project is structured to be easily deployed to modern cloud providers. 

### 1. Vercel & Modal (Serverless)
- **Backend (Modal)**: We use `modal_app.py` in the `backend/` directory to deploy the FastAPI app and mount the SQLite database to a persistent cloud volume.
- **Frontend (Vercel)**: Connect your GitHub repo to Vercel, set the root directory to `frontend/`, and set the `VITE_API_URL` environment variable to your live Modal backend URL.

### 2. AWS EC2 (Docker)
Since the app includes a `docker-compose.yml` and an Nginx proxy configuration, deploying to a VPS like AWS EC2 is as simple as:
1. Launching an Ubuntu instance and opening ports 80 and 3000.
2. Installing Docker.
3. Cloning the repository and running `sudo docker-compose up -d --build`.

*(Detailed deployment guides can be found in the repository docs).*

---

## ??? Project Structure
```text
Restaurant-BBQ/
+-- backend/                # FastAPI application
¦   +-- app/                # API routes, AI logic, DB models
¦   +-- data/               # SQLite database storage
¦   +-- modal_app.py        # Serverless deployment script
¦   +-- requirements.txt    # Python dependencies
+-- frontend/               # React / Vite application
¦   +-- src/                # Components, Pages, Hooks, API services
¦   +-- nginx.conf          # Production web server config
¦   +-- package.json        # Node dependencies
+-- docker-compose.yml      # Master Docker orchestration
```

## ?? Security Note
**Never commit your `.env` file or hardcode API keys (like Groq or Anthropic keys) into your code.** The repository uses GitHub Push Protection to prevent accidental secret leaks.

## ?? License
This project is licensed under the MIT License.
