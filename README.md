# Stock Analysis Commandline/API Application
POC Application to use OpenAI APIs to extract tokens and summarise the stock data.
Query the polygon with extracted tokens and visualise the response with graph. 
This application uses the simple chat history management to provide context to LLM and get the better answer.

## Libraries used
- OpenAI
- plotext
- matplotlib
- fastapi
- langchain

## Platform Pre-requisites

- [python 3.11](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation.html)
- [FastAPI](https://fastapi.tiangolo.com/)

In addition to these pre-requisites, the following items are recommended:

- Basic understanding of Python
- Basic understanding of Python virtual environments
- Basic understanding of OpenAI APIs
- Understanding of Repository pattern
- Understanding of dependency injection 
- Basic understanding of FastAPI

## Installation
   You can set up the development environment either by using docker or without docker.
1) Clone the repository to the machine:
   ```shell
   git clone https://github.com/atulingale-sdc/stock-analysis.git
   cd stock-analysis
   git checkout main
   git pull origin
   ```
   ---

2) Run application Commandline
   1. Create Virtual Environment
      ```shell
      cd stock-analysis/
      # Install all dependencies and create new virtual environment
      pipenv install
      ```
   2. Crete `.env`
      ```shell
      cd stock-analysis/
      cp env.sample .env
      ```
      Open the .env file and add the API keys for OpenAI and Polygon. And set the value of `RUN_MODE` as `CLI`
   3. Start application
      ```shell
      pipenv shell
      python app
      ```
      - It will ask the user to enter the query to analyse.
      - User can query like 'What is Apple's stock price for last 5 months'
      - It will Show the Graph and Summery of the stock
      - To exit from application user can type `Exit` and hit enter or press `Ctrl + c` from keyboard

   3) Run application Commandline
      1. Create Virtual Environment
         ```shell
         cd stock-analysis/
         # Install all dependencies and create new virtual environment
         pipenv install
         ```
      2. Crete `.env`
         ```shell
         cd stock-analysis/
         cp env.sample .env
         ```
         Open the .env file and add the API keys for OpenAI and Polygon. And set the value of `RUN_MODE` as `API`
      3. Start application
         ```shell
         pipenv shell
         python app
         ```
         - It will start the API server by default on `8084` port
         - You can Access the Swagger UI at http://127.0.0.1:8084/docs
         - Authorize with username = `atul` and password = `atul`
         - To use the API Click on `` and click on "Try"
         - You can put the JSON body as
           ```json
           {
             "query": "What is apple's stock prices in the last 1 year?"
           }
           ```
           It will get response like:
           ```json
            {
              "query": "What is apple's stock prices in the last 1 year?",
              "summery": "Over the period of July 6, 2023 to July 6, 2024, Apple's stock (AAPL) had a fluctuating opening price, opening at 193.78 and reaching a high of 226.45. The stock also experienced a low of 165.67 and closed at 226.34. The volume of trading was consistently high, with a peak of 1.659 billion shares traded on July 6, 2024. Overall, the stock showed a positive trend, increasing from 196.45 to 226.34 over the course of the year.",
              "graphs": [
                "http://127.0.0.1:8084/images/a9e7611c-9490-40bf-aad1-91525d0bae2d.png"
              ]
            }
           ```
           To see the Graph you can put the URL from response in browser http://127.0.0.1:8084/images/a9e7611c-9490-40bf-aad1-91525d0bae2d.png
         