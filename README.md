# LLM API Wrapper

## Overview
This API acts as a lightweight wrapper around a large language model (LLM), facilitating easy querying and response processing. It leverages FastAPI to handle requests and integrates various components for model configuration, tokenization, and processing.

## Features
- **Easy Querying**: Send questions to the LLM and receive answers quickly and efficiently.
- **Flexible Configuration**: The `LlmConfigurator` class allows for flexible model configuration.
- **Advanced Processing**: Incorporates tokenization and LoRA (Low-Rank Adaptation) for enhanced query processing.

## Installation
To set up the API, you need to have Python installed on your system. Then, clone this repository and install the required dependencies:

```bash
git clone "https://github.com/MyStuBu/llm_api"
cd [your-repo-directory]
pip install -r requirements.txt
```

## Usage
Start the API server:

```bash
uvicorn app:app --reload
```

To ask a question, simply use the `/ask/{question}` endpoint:

```bash
curl http://localhost:8000/ask/YourQuestionHere
```

Replace `YourQuestionHere` with your actual query.

## Example
To understand how the API works, consider this example query:

```
"How can I set up a version control system for our team project to achieve the KPI with the description: 'Manage personal files and the configuration of these files in a software development environment?"
```

Use the following curl command:

```bash
curl http://localhost:8000/ask/How%20can%20I%20set%20up%20a%20version%20control%20system%20for%20our%20team%20project%20to%20achieve%20the%20KPI%20with%20the%20description:%20'Manage%20personal%20files%20and%20the%20configuration%20of%20these%20files%20in%20a%20software%20development%20environment?
```
