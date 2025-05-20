import ollama
import json
import sys

def load_conversation(filename=""):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("INFO : file not found, loading empty history")
        return []
    
def save_conversation(conversation, filename="conversation.json"):
    with open(filename, "w") as f:
        json.dump(conversation, f, indent=4)

args = sys.argv

try:
    if args[1] == "-h":
        print("""Usage : python ollama_convs.py <model_name> [Optionnal : conversation history file (json)]
              You need to have pulled a model from ollama beforehand.
              """)
    else:
        model_name = args[1]
        if len(args) >= 3:
            conversation_history = load_conversation(args[2])
        else:
            conversation_history = []
        
        while True:
            user_input = input("Prompt : ")
            conversation_history.append({"role": "user", "content": user_input})

            response = ollama.chat(model=model_name, messages=conversation_history)

            conversation_history.append({"role" : "assistant", "content": response["message"]["content"]})

            if len(args) >= 3:
                save_conversation(conversation_history, args[2])
            else:
                save_conversation(conversation_history)
                print("Saved to conversation.json")

            print(response["message"]["content"])

except ollama.RequestError as req:
    print("[ERROR] There was an error in the request : ", req)
except ollama.ResponseError as res:
    print("[ERROR] There was an error in the response : ", res)
except IndexError as ind:
    print("[ERROR] There is likely an error in the provided command. Run python ollama_convs -h for more information.", ind)
except Exception as e:
    print("[ERROR] Some kind of error occured : ", e)