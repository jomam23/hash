from flask import Flask, request
import string

app = Flask(__name__)

char = string.ascii_letters + string.digits + string.punctuation

@app.route("/", methods=["GET", "POST"])
def index():
    encoded_output = ""
    decoded_output = ""

    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        dinput_text = request.form.get("dinput_text", "")

        # Load key
        with open("key.txt", "r") as file:
            key = file.read()

        # Encode
        text3 = ""
        text = ""
        for letter in input_text:
            if letter in char:
                index = char.index(letter)
                text3 += key[index]
            else:
                text3 += letter
        for letter in text3:
            if letter in char:
                index = char.index(letter)
                text += key[index]
            else:
                text += letter
        encoded_output = text

        # Decode
        text32 = ""
        text2 = ""
        for letter in dinput_text:
            if letter in key:
                index = key.index(letter)
                text32 += char[index]
            else:
                text32 += letter
        for letter in text32:
            if letter in key:
                index = key.index(letter)
                text2 += char[index]
            else:
                text2 += letter
        decoded_output = text2

        # Save encoded output
        with open("ciphertext.txt", "w") as file:
            file.write(encoded_output)

    return f'''
        <form method="post">
            <label>Write your encode input:</label><br>
            <input type="text" name="input_text" /><br><br>
            <label>Write your decode input:</label><br>
            <input type="text" name="dinput_text" /><br><br>
            <input type="submit" value="Submit" />
        </form>

        <h2>Encoded Output:</h2>
        <p>{encoded_output}</p>
        <h2>Decoded Output:</h2>
        <p>{decoded_output}</p>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
    print("🔥 Flask app running...")
