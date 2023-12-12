from flask import Flask, render_template, request, send_file
import random
from pprint import pformat
import base64
import webbrowser
import threading
from waitress import serve

app = Flask(__name__)

alphabets = ["\U0001f600", "\U0001f601", "\U0001f602", "\U0001f603", "\U0001f604", "\U0001f605", "\U0001f606", "\U0001f607", "\U0001f608", "\U0001f609", "\U0001f60a", "\U0001f60b", "\U0001f60c", "\U0001f60d", "\U0001f60e", "\U0001f60f", "\U0001f610", "\U0001f611", "\U0001f612", "\U0001f613", "\U0001f614", "\U0001f615", "\U0001f616", "\U0001f617", "\U0001f618", "\U0001f619", "\U0001f61a", "\U0001f61b", "\U0001f61c", "\U0001f61d", "\U0001f61e", "\U0001f61f", "\U0001f620", "\U0001f621", "\U0001f622", "\U0001f623", "\U0001f624", "\U0001f625", "\U0001f626", "\U0001f627", "\U0001f628", "\U0001f629", "\U0001f62a", "\U0001f62b", "\U0001f62c", "\U0001f62d", "\U0001f62e", "\U0001f62f", "\U0001f630", "\U0001f631", "\U0001f632", "\U0001f633", "\U0001f634", "\U0001f635", "\U0001f636", "\U0001f637", "\U0001f638", "\U0001f639", "\U0001f63a", "\U0001f63b", "\U0001f63c", "\U0001f63d", "\U0001f63e", "\U0001f63f", "\U0001f640", "\U0001f641", "\U0001f642", "\U0001f643", "\U0001f644", "\U0001f645", "\U0001f646", "\U0001f647", "\U0001f648", "\U0001f649", "\U0001f64a", "\U0001f64b", "\U0001f64c", "\U0001f64d", "\U0001f64e", "\U0001f64f", "\U0001f680", "\U0001f681", "\U0001f682", "\U0001f683", "\U0001f684", "\U0001f685", "\U0001f686", "\U0001f687", "\U0001f688", "\U0001f689", "\U0001f68a", "\U0001f68b", "\U0001f68c", "\U0001f68d", "\U0001f68e", "\U0001f68f", "\U0001f690", "\U0001f691", "\U0001f692", "\U0001f693", "\U0001f694", "\U0001f695", "\U0001f696", "\U0001f697", "\U0001f698", "\U0001f699", "\U0001f69a", "\U0001f69b", "\U0001f69c", "\U0001f69d", "\U0001f69e", "\U0001f69f", "\U0001f6a0", "\U0001f6a1", "\U0001f6a2", "\U0001f6a3", "\U0001f6a4", "\U0001f6a5", "\U0001f6a6", "\U0001f6a7", "\U0001f6a8", "\U0001f6a9", "\U0001f6aa", "\U0001f6ab", "\U0001f6ac", "\U0001f6ad", "\U0001f6ae", "\U0001f6af", "\U0001f6b0", "\U0001f6b1", "\U0001f6b2", "\U0001f6b3", "\U0001f6b4", "\U0001f6b5", "\U0001f6b6", "\U0001f6b7", "\U0001f6b8", "\U0001f6b9", "\U0001f6ba", "\U0001f6bb", "\U0001f6bc", "\U0001f6bd", "\U0001f6be", "\U0001f6bf", "\U0001f6c0", "\U0001f6c1", "\U0001f6c2", "\U0001f6c3", "\U0001f6c4", "\U0001f6c5", "\U0001f6cb", "\U0001f6cc", "\U0001f6cd", "\U0001f6ce", "\U0001f6cf", "\U0001f6d0", "\U0001f6d1", "\U0001f6d2", "\U0001f6d3", "\U0001f6d4", "\U0001f6d5", "\U0001f6e0", "\U0001f6e1", "\U0001f6e2", "\U0001f6e3", "\U0001f6e4", "\U0001f6e5", "\U0001f6e9", "\U0001f6eb", "\U0001f6ec", "\U0001f6f0", "\U0001f6f3", "\U0001f910", "\U0001f911", "\U0001f912", "\U0001f913", "\U0001f914", "\U0001f915", "\U0001f916", "\U0001f917", "\U0001f918", "\U0001f919", "\U0001f91a", "\U0001f91b", "\U0001f91c", "\U0001f91d", "\U0001f91e", "\U0001f920", "\U0001f921", "\U0001f922", "\U0001f923", "\U0001f924", "\U0001f925", "\U0001f926", "\U0001f927", "\U0001f928", "\U0001f929", "\U0001f92a", "\U0001f92b", "\U0001f92c", "\U0001f92d", "\U0001f92e", "\U0001f92f", "\U0001f930", "\U0001f931", "\U0001f932", "\U0001f933", "\U0001f934", "\U0001f935", "\U0001f936", "\U0001f937", "\U0001f938", "\U0001f939", "\U0001f93a", "\U0001f93c", "\U0001f93d", "\U0001f93e", "\U0001f940", "\U0001f941", "\U0001f942", "\U0001f943", "\U0001f944", "\U0001f945", "\U0001f947", "\U0001f948", "\U0001f949", "\U0001f94a", "\U0001f94b", "\U0001f950", "\U0001f951", "\U0001f952", "\U0001f953", "\U0001f954", "\U0001f955", "\U0001f956", "\U0001f957", "\U0001f958", "\U0001f959", "\U0001f95a", "\U0001f95b", "\U0001f95c", "\U0001f95d", "\U0001f95e", "\U0001f95f", "\U0001f960", "\U0001f961", "\U0001f962", "\U0001f963", "\U0001f964", "\U0001f965", "\U0001f966", "\U0001f967", "\U0001f968", "\U0001f969", "\U0001f96a", "\U0001f96b", "\U0001f980", "\U0001f981", "\U0001f982", "\U0001f983", "\U0001f984", "\U0001f985", "\U0001f986", "\U0001f987", "\U0001f988", "\U0001f989", "\U0001f98a", "\U0001f98b", "\U0001f98c", "\U0001f98d", "\U0001f98e", "\U0001f98f", "\U0001f990", "\U0001f991", "\U0001f992", "\U0001f993", "\U0001f994", "\U0001f995", "\U0001f996", "\U0001f997", "\U0001f998", "\U0001f999", "\U0001f99a", "\U0001f99b", "\U0001f99c", "\U0001f99d", "\U0001f99e", "\U0001f99f", "\U0001f9a0", "\U0001f9a1", "\U0001f9a2", "\U0001f9b0", "\U0001f9b1", "\U0001f9b2", "\U0001f9b3", "\U0001f9b4", "\U0001f9b5", "\U0001f9b6", "\U0001f9b7", "\U0001f9b8", "\U0001f9b9", "\U0001f9c0", "\U0001f9c1", "\U0001f9c2", "\U0001f9d0", "\U0001f9d1", "\U0001f9d2", "\U0001f9d3", "\U0001f9d4", "\U0001f9d5", "\U0001f9d6", "\U0001f9d7", "\U0001f9d8", "\U0001f9d9", "\U0001f9da", "\U0001f9db", "\U0001f9dc", "\U0001f9dd", "\U0001f9de", "\U0001f9df", "\U0001fae5", "\U0001f405", "\U0001f4A1", "\U0001f9bb", "\U0001F4B0", "\U0001F48E", "\U0001F440"]

MAX_STR_LEN = 70

def wrt_emoji(code, n):
    return "\n".join("{}\\".format(code[i: i + n]) for i in range(0, len(code), n)).rstrip("\\")

def emoji_write(code, alphabets):
    alphabet = random.sample(alphabets, 10)
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (f'exec("".join(map(chr,[int("".join(str({pformat(d2)}[i]) for i in x.split())) for x in\n' + f'"{wrt_emoji("  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in code), MAX_STR_LEN)}"\n.split("  ")])))\n')

def base64_wrt(code):
    encode_message = code.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    encrypt_txt = base64_bytes.decode('ascii')
    encrypt = f'import base64; exec(base64.b64decode("{encrypt_txt}".encode("ascii")).decode("ascii"))'
    return encrypt


@app.route('/', methods=['GET', 'POST'])
def index():
    encoded_code = ""
    original_code = ""
    if request.method == 'POST':
        uploaded_file = request.files.get('fileInput')
        if uploaded_file and uploaded_file.filename != '':
            input_code = uploaded_file.read().decode('utf-8')
        else:
            input_code = request.form.get('input_code')

        original_code = input_code

        # Determine encoding method
        encoding_method = request.form.get('encoding_method')
        if encoding_method == 'emoji':
            encoded_code = emoji_write(input_code, alphabets)
        elif encoding_method == 'base64':
            encoded_code = base64_wrt(input_code)
        
    return render_template('index.html', encoded_code=encoded_code, original_code=original_code)


@app.route('/download')
def download():
    with open('encoded_code.txt', 'w') as f:
        f.write(request.args.get('encoded_code'))
    return send_file('encoded_code.txt', as_attachment=True)



# For Development Server
def start_server():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    url = "http://127.0.0.1:8080"
    webbrowser.open(url)




# # For Production Server
# if __name__ == '__main__':
#     serve(app, host='0.0.0.0', port=8080)