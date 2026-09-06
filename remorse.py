from fastapi import FastAPI as fahh
from pydantic import BaseModel as bm

app = fahh()

#TI: TextInput
class TI(bm):
    text: str

#MI: MorseInput
class MI(bm):
    morse: str

MORSE_CODE= {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": "....", "6": "-....", "7": "--....", "8": "---..", 
    "9": "----."
}

TEXT= {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
   '..-.': 'F', '--.': 'G', '....': '5', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
    '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '-....': '6', '--....': '7', '---..': '8',
    '----.': '9'
}

#mte: Morse-code To English
def mte(mi):
    morse_split= tuple(mi.split("/"))
    words= ()

    for word in morse_split:
        words= tuple(word.split(' '))
        result= ""
        for morse_letters in words:
            if morse_letters in TEXT:
                result += TEXT[morse_letters]
    words += (result,)

    return ' '.join(words)

#etm: English To Morse-code
def etm(ti):
    text_split= tuple(ti.split(" "))
    morse_words= ()

    for morse in text_split:
        morse_words= tuple(morse.split(' '))
        result= ()
        for letters in MORSE_CODE:
            if letters in MORSE_CODE:
                result += MORSE_CODE[letters] + " "
        morse_words += (result.strip(),)

    return '/'.join(morse_words)


@app.get("/")
def backend_alive():
    return{
        "backend": "alive, yayy"
    }

@app.post("/morse-to-text")
def morse_endpoint(input_morse: MI):
    output_text= mte(input_morse.morse)
    return{
        "morse": input_morse.morse,
        "text": output_text,
    }


@app.post("/text-to-morse")
def text_endpoint(input_text: TI):
    output_morse= etm(input_text.text)
    return{
        "text": input_text.text,
        "morse": output_morse,
    }