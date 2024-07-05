# Stock Analysis Commandline Application
POC Application to use OpenAI APIs to extract tokens and summarise the stock data.
Query the polygon with extracted tokens and visualise the response with graph. Exercise the 

## Libraries used
- OpenAI
- plotext

## Platform Pre-requisites

- [python 3.11](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation/)

In addition to these pre-requisites, the following items are recommended:

- Basic understanding of Python
- Basic understanding of Python virtual environments
- Basic understanding of OpenAI APIs
- Understanding of Repository pattern
- Understanding of dependency injection

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

2) Run application
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
      Open the .env file and add the API keys for OpenAI and Polygon
   3. Start application
      ```shell
      pipenv shell
      python app
      ```
      - It will ask the user to enter the query to analyse.
      - User can query like 'What is Apple's stock price for last 5 months'
      - It will Show the Graph and Summery of the stock
      - To exit from application user can type `Exit` and hit enter or press `Ctrl + c` from keyboard
