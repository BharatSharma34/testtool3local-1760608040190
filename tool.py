from tapestrysdk import image_to_text
import json

token = "sk-u5bifw7kk-mgt8jc6l"

def main(user_prompt, document,name):
    try:
        result = image_to_text(token, user_prompt, document, name, "describe this image in detail")
        return result
    except Exception as e:
        
        return {"error": str(e)}

