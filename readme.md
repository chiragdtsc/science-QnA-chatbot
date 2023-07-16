
## Requirement
The current project has the blueprint structure of an AI App. 

Our mission is to implement an 💬NLP chatbot **answering questions about science**. 

Adding logic to the `main.py` file inside the `execute` function. 
```python
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        response = '' # <<< -- Logic goes here
        output.append(response)

    return SimpleText(dict(text=output))
```
## Constraints and restrictions
* Free to use any package or library you see:
* Shouldn't call any external service (e.g. chatGPT) 

## Run
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 

