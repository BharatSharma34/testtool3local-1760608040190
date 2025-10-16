"""
TestTool3Local - Custom Lambda Tool
Description: test

IMPORTANT: Only edit the code in the main() function below.
The Lambda handler will be automatically appended during deployment.
DO NOT add lambda_handler code here - it will be added automatically.
"""

def main(event_body):
    a=10
    b=20
       
    return {
        "success": True,
        "message": a+b,
        "data": event_body
    }

# You can add helper functions below
