# Claude FastAPI LLM API

## Overview

**Claude FastAPI LLM API** is a production-oriented REST API built with **FastAPI** and **Anthropic Claude**, designed to expose Large Language Model (LLM) capabilities through a scalable, asynchronous web service architecture.

The application provides a structured `/chatbot` endpoint for submitting natural-language prompts to Claude and receiving **real-time streamed responses** using **Server-Sent Events (SSE)**.

The project also implements environment-based secret management, request validation with **Pydantic**, API documentation through **OpenAPI/Swagger**, and modular Python application components.

---

## Author

**Sayeed Ahmad**

---

## Key Features

* **FastAPI-based REST API**
* Integration with **Anthropic Claude LLM**
* **Real-time response streaming**
* **Server-Sent Events (SSE)** support
* Pydantic-based request validation
* Environment-variable-based API key management
* Automatic OpenAPI documentation
* Interactive Swagger UI
* HTTP exception handling
* Configurable maximum output tokens
* Modular Python application structure
* GitHub-ready project configuration

---

## System Architecture

```text
                 ┌─────────────────────┐
                 │       Client        │
                 │  Postman / Browser  │
                 └──────────┬──────────┘
                            │
                            │ HTTP POST
                            ▼
                 ┌─────────────────────┐
                 │       FastAPI       │
                 │      REST API       │
                 └──────────┬──────────┘
                            │
                            │ Request Validation
                            ▼
                 ┌─────────────────────┐
                 │      Pydantic       │
                 │   ChatRequest      │
                 └──────────┬──────────┘
                            │
                            │ Anthropic SDK
                            ▼
                 ┌─────────────────────┐
                 │   Claude LLM API    │
                 │      Anthropic      │
                 └──────────┬──────────┘
                            │
                            │ Streaming Tokens
                            ▼
                 ┌─────────────────────┐
                 │ StreamingResponse   │
                 │       SSE           │
                 └──────────┬──────────┘
                            │
                            ▼
                       Client Response
```

---

## Technology Stack

| Technology        | Purpose                               |
| ----------------- | ------------------------------------- |
| **Python**        | Core programming language             |
| **FastAPI**       | High-performance API framework        |
| **Uvicorn**       | ASGI application server               |
| **Anthropic SDK** | Claude LLM integration                |
| **Pydantic**      | Data validation and schema management |
| **python-dotenv** | Environment configuration             |
| **OpenAPI**       | API specification                     |
| **Swagger UI**    | Interactive API testing               |
| **SSE**           | Real-time response streaming          |
| **Git / GitHub**  | Version control and source management |

---

## Project Structure

```text
claude-fastapi-llm-api/
│
├── app.py
├── claude.py
├── main.py
├── patient.json
├── requirements.txt
├── .gitignore
└── README.md
```

### File Responsibilities

**`main.py`**
Application entry point containing the FastAPI application and API routes.

**`claude.py`**
Claude/Anthropic integration and LLM-related functionality.

**`app.py`**
Application-level functionality and supporting API logic.

**`patient.json`**
JSON-based application data used by the project.

**`requirements.txt`**
Defines the Python dependencies required to run the application.

**`.gitignore`**
Prevents sensitive configuration files, virtual environments, caches, and generated files from being committed.

---

## API Endpoints

### Health / Root Endpoint

```http
GET /
```

Example response:

```json
{
  "status": "ok",
  "message": "Welcome to Sayeed Ahmad's Claude API"
}
```

---

### Claude Chat Endpoint

```http
POST /chatbot
```

Request:

```json
{
  "message": "Hello, World!",
  "max_tokens": 200
}
```

The endpoint validates the request, forwards the prompt to Claude, and streams the generated response back to the client.

---

## API Documentation

After starting the application, interactive API documentation is automatically available through Swagger UI.

```text
http://127.0.0.1:8000/docs
```

The OpenAPI specification is available at:

```text
http://127.0.0.1:8000/openapi.json
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sayeedahmad01/claude-fastapi-llm-api.git
cd claude-fastapi-llm-api
```

### 2. Create a Virtual Environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
```

The application loads the API key through environment variables.

### Security

**Never commit `.env` or API credentials to GitHub.**

The `.gitignore` file should contain:

```text
.env
.venv/
venv/
__pycache__/
*.pyc
```

---

## Running the Application

Start the FastAPI development server:

```bash
python -m uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Testing the Chatbot API

Using the Swagger interface, execute:

```http
POST /chatbot
```

with:

```json
{
  "message": "Explain Artificial Intelligence in simple terms",
  "max_tokens": 200
}
```

The API returns the generated Claude response through a streaming response mechanism.

---

## Streaming Architecture

Unlike a conventional request-response implementation where the complete LLM output is returned after generation, this project uses **streaming inference**.

```text
User Request
     │
     ▼
FastAPI
     │
     ▼
Anthropic Claude
     │
     ├── Token 1 ──►
     ├── Token 2 ──►
     ├── Token 3 ──►
     ├── Token 4 ──►
     │
     ▼
Server-Sent Events
     │
     ▼
Client
```

This approach reduces perceived latency and allows clients to display generated content progressively.

---

## Error Handling

The API includes validation for empty messages.

Example:

```json
{
  "message": ""
}
```

The API responds with an HTTP `400` error:

```json
{
  "detail": "Message cannot be empty"
}
```

The application also handles exceptions occurring during the Claude streaming process.

---

## Configuration

The chatbot request supports configurable output length:

```json
{
  "message": "Explain machine learning",
  "max_tokens": 300
}
```

This allows the client to control the maximum number of generated tokens.

---

## Development Workflow

```text
Client
  │
  ▼
FastAPI Endpoint
  │
  ▼
Pydantic Validation
  │
  ▼
Anthropic SDK
  │
  ▼
Claude LLM
  │
  ▼
StreamingResponse
  │
  ▼
Client
```

---

## Security Considerations

The project follows basic API security practices:

* API credentials are stored using environment variables.
* `.env` is excluded from version control.
* Sensitive credentials should never be hard-coded.
* Input validation is handled through Pydantic.
* API errors are handled without exposing configuration files.

For production deployment, additional controls such as authentication, authorization, rate limiting, request logging, HTTPS, structured observability, and centralized secret management should be considered.

---

## Future Enhancements

Potential improvements include:

* JWT/OAuth2 authentication
* API rate limiting
* Conversation history
* Persistent chat storage
* PostgreSQL integration
* Redis-based caching
* Structured logging
* Prometheus metrics
* Docker containerization
* CI/CD with GitHub Actions
* Production deployment
* WebSocket-based communication
* Retrieval-Augmented Generation (RAG)
* Vector database integration
* Multi-model LLM support

---

## Learning Outcomes

This project demonstrates practical implementation of:

* RESTful API development
* FastAPI application architecture
* LLM API integration
* Prompt-to-response pipelines
* Streaming inference
* Server-Sent Events
* Pydantic data validation
* Environment-based configuration
* API documentation with OpenAPI
* Python virtual environments
* Git and GitHub workflow
* Secure credential management

---

## Author

### Sayeed Ahmad

**AI / ML | Generative AI | Python | FastAPI | LLM Engineering**

This project was developed to explore the integration of modern Large Language Models with production-oriented Python API architectures.

---

## License

This project is intended for educational and development purposes.

---

**Built by Sayeed Ahmad**
