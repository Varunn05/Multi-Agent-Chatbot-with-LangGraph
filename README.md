# Multi-Agent Chatbot with LangGraph

A powerful AI chatbot application built using LangGraph, FastAPI, and Streamlit that provides dynamic model selection and web search capabilities.

## Features

- **Multi-Provider Support**: Choose between Groq and OpenAI language models
- **Dynamic Model Selection**: Switch between different models at runtime
- **Web Search Integration**: Optional web search powered by Tavily Search API
- **Interactive UI**: Clean and intuitive Streamlit interface
- **RESTful API**: FastAPI backend for scalable deployment
- **Flexible Agent Configuration**: Customizable system prompts for different use cases

## Architecture

The application consists of three main components:

1. **Frontend (main.py)**: Streamlit-based user interface
2. **Backend (backend.py)**: FastAPI server handling chat requests
3. **Agent Logic (app.py)**: LangGraph agent implementation with tool integration

## Prerequisites

- Python 3.8 or higher
- pipenv for virtual environment management
- API keys for the following services:
  - Groq API
  - OpenAI API
  - Tavily Search API

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd multi-agent-chatbot
```

2. Install pipenv if you haven't already:
```bash
pip install pipenv
```

3. Create and activate virtual environment:
```bash
pipenv install
pipenv shell
```

4. Install required dependencies:
```bash
pipenv install fastapi uvicorn streamlit langchain-groq langchain-openai langchain-community langgraph requests pydantic
```

## Configuration

Create a `.env` file in the project root directory and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Alternatively, you can set these as environment variables in your system.

## Usage

### Running the Application

1. **Start the FastAPI backend server:**
```bash
python backend.py
```
The API server will start on `http://127.0.0.1:9999`

2. **Launch the Streamlit frontend (in a new terminal):**
```bash
streamlit run main.py
```
The web interface will open in your browser at `http://localhost:8501`

### Using the Interface

1. **Configure Your Agent:**
   - Enter a system prompt to define your AI agent's behavior
   - Select a provider (Groq or OpenAI)
   - Choose a specific model from the available options

2. **Enable Web Search (Optional):**
   - Check the "Allow Web Search" box to enable internet search capabilities
   - This allows the agent to search for current information when needed

3. **Ask Questions:**
   - Enter your query in the text area
   - Click "Ask Agent!" to get a response

## Supported Models

### Groq Models
- llama-3.3-70b-versatile
- mixtral-8x7b-32768

### OpenAI Models
- gpt-4o-mini

## API Documentation

### POST /chat

Process a chat request with the AI agent.

**Request Body:**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as an AI chatbot who is smart and friendly",
  "messages": ["Tell me about the latest AI trends"],
  "allow_search": true
}
```

**Response:**
```json
"The response from the AI agent..."
```

## Project Structure

```
multi-agent-chatbot/
├── main.py           # Streamlit frontend interface
├── backend.py        # FastAPI server implementation
├── app.py           # LangGraph agent logic
├── README.md        # Project documentation
├── Pipfile          # pipenv dependencies
└── .env             # Environment variables (create this)
```

## Dependencies

- **LangGraph**: Agent orchestration framework
- **FastAPI**: Modern web framework for building APIs
- **Streamlit**: Frontend framework for data applications
- **LangChain**: Integration with various language models
- **Pydantic**: Data validation and settings management
- **Requests**: HTTP library for API calls

## Error Handling

The application includes error handling for:
- Invalid model names
- API connection issues
- Missing environment variables
- Server errors from model providers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Troubleshooting

**Common Issues:**

1. **API Key Errors**: Ensure all required API keys are properly set in your environment variables
2. **Port Conflicts**: If port 9999 is already in use, modify the port in `backend.py`
3. **Model Availability**: Some models may be temporarily unavailable due to provider issues
4. **Network Issues**: Ensure you have a stable internet connection for web search functionality

## Future Enhancements

- Add support for more language model providers
- Implement conversation history persistence
- Add user authentication and session management
- Enhance error handling and logging
- Add model performance metrics and monitoring