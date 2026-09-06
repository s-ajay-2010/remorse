from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

MORSE_CODE= {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "---..", "8": "---..", 
    "9": "----."
}

TEXT= {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
   '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4',  ".....": "5", '-....': '6', '--...': '7','---..': '8',
    '----.': '9'
}

#mte: Morse-code To English
#mi: Morse Input
def mte(mi):
    morse_words= tuple(mi.split("/"))
    words= ()

    for word in morse_words:
        morse_letters= tuple(word.split(' '))
        result= ""
        for morse_letter in morse_letters:
            if morse_letter in TEXT:
                result += TEXT[morse_letter]
        words += (result,)

    return ' '.join(words)

#etm: English To Morse-code
#ti: Text Input
def etm(ti):
    text_split= tuple(ti.split(" "))
    morse_words= ()

    for morse in text_split:
        letters= tuple(morse.upper())
        result= ""
        for letter in letters:
            if letter in MORSE_CODE:
                result += MORSE_CODE[letter] + " "
        morse_words += (result.strip(),)

    return '/'.join(morse_words)


@app.get("/", response_class=HTMLResponse)
def backend_alive():
    return """
    <html>
        <body style="text-align: center; margin-top: 50px; background-color: black; color: white;">
            <h1>Morse Code Translator</h1>
            <button onclick="window.location.href='/morse-to-text'">Morse to Text</button>
            <button onclick="window.location.href='/text-to-morse'">Text to Morse</button>
        </body>
    </html>
    """

@app.get("/morse-to-text")
def morse_endpoint(input_morse: str=None):
    if input_morse:
        output_text= mte(input_morse)
        return{
            "morse": input_morse,
            "text": output_text,
        }
    else:
        return{
            "incomplete request": "please add '?input_morse= YOUR_VALUE' at the end of this url to get the converted version:)",
            "format": "seperate the words with a '/' and the letters with a ' '(yea a literal space)",
        }


@app.get("/text-to-morse")
def text_endpoint(input_text: str=None):
    if input_text:
        output_morse= etm(input_text)
        return{
            "text": input_text,
            "morse": output_morse,
        }
    else:
        return{
            "incomplete request": "please add '?input_text= YOUR_VALUE' at the end of this url to get the converted version:)",
        }