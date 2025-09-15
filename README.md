\# Sales Chat - Web Prototype



Minimal FastAPI and static-frontend prototype:

\- Text input to GPT; text reply + gTTS audio returned and auto-played.



Setup (local)

1\. Copy .env.example to .env and populate OPENAI\_API\_KEY.

2\. Create virtual environment and install dependencies:

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate   (on Windows)

&nbsp;  pip install -r requirements.txt

3\. Run server:

&nbsp;  uvicorn server:app --reload --port 8000

4\. Open in browser:

&nbsp;  http://127.0.0.1:8000



Deploy

\- Use Render (Web Service) or similar.

\- In Render environment variables, set:

&nbsp;  OPENAI\_API\_KEY = <your key>

\- Build command:

&nbsp;  pip install -r requirements.txt

\- Start command:

&nbsp;  uvicorn server:app --host 0.0.0.0 --port $PORT



Security

\- Do NOT commit your .env. Keep API keys only in your local .env and in the host environment variables.



