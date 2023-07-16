
## Requirement
The current project has the blueprint structure of an AI App. 

Our mission is to implement an 💬NLP chatbot **answering questions about science**. 

The logic begins in the `main.py` file inside the `execute` function. 
```python
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        response = '' 
        output.append(response)

    return SimpleText(dict(text=output))
```

## Run
The application can be executed in two different ways:
* locally by running the `start.sh` 
* or use a docker container using the following commands - `docker build --tag 'science_qna_bot' .` `docker run --detach 'science_qna_bot` 

