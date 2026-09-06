# REMORSE
This is an api which translates morse code to text and vice versa powered by FastAPI

# Endpoints
- ```/``` : This endpoint has buttons for redirection to the ```/morse-to-text``` and ```/text-to-morse``` endpoints.

- ```/morse-to-text```: This endpoint when given your value through the url or as a GET request, it gives you the translated text for the morse code value given. Usage: ```/morse-to-text?input_morse= YOUR_VALUE```

- ```/text-to-morse```: This endpoint when hit with a text through the url or as a GET request, it gives you the equivalent morse code value of it.  Usage: ```/text-to-morse?input_text= YOUR_VALUE```

- ```/docs```: This is FastAPI's default documentation endpoint, you can open this and try out all the endpoints in a GUI way if you want too:)

# Setup
```
git clone https://github.com/s-ajay-2010/remorse.git
cd remorse
python -m venv venv
```
activate your venv with respect to whichever shell and OS you use. 
```
pip install -r requirements.txt
uvicorn remorse:app --reload
```
open http://localhost:8000 .


AI Usage: Nil.