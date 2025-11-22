# AnimeFinder 🐾

A semantic search application for finding animals based on text descriptions, powered by Google Gemini embeddings.

## 🎯 Project Overview

AnimeFinder allows you to search for animals using natural language descriptions. The app uses semantic search powered by Google's Gemini embedding model to find the most relevant matches.

## 🏗️ Architecture

- **Frontend**: Next.js 14+ with TypeScript, Tailwind CSS v4, ShadCN
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL 16 + PgVector extension
- **Object Storage**: MinIO (S3-compatible)
- **AI**: Google Gemini Embeddings (`gemini-embedding-001`)

## 📁 Project Structure

```
AnimeFinder/
├── backend/          # FastAPI application
├── frontend/         # Next.js application
├── notebooks/        # Jupyter notebooks for prototyping
├── docs/             # Documentation
└── docker-compose.yml
```

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- pnpm

### Installation

1. Clone the repository
2. Set up environment variables (copy `.env.example` to `.env`)
3. Run `docker-compose up` to start services
4. Install backend dependencies: `pip install -r backend/requirements.txt`
5. Install frontend dependencies: `cd frontend && pnpm install`

## 📝 License

MIT

## 👨‍💻 Author

Built with ❤️ for learning embeddings and semantic search
