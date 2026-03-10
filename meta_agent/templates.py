AGENT_TEMPLATE = """
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: {workflow_id}
# Employee: {employee_id}
# Pattern: {signature}


def run_agent():
    print(f"--- Start Generated Agent for {workflow_id} ---")
    pyautogui.PAUSE = 1.0

    steps = {steps_list}
    
    for i, step in enumerate(steps):
        print(f"Step {{i+1}}: {{step['event']}} in {{step['app_name']}}")
        
        # 1. Navigation Logic
        if step['url'] and str(step['url']) != 'None':
            print(f"  > Opening URL: {{step['url']}}")
            webbrowser.open(step['url'])
            time.sleep(4) # Wait for page load
            
        # 2. Click Logic
        if 'CLICK' in step['event'].upper():
            # In a production environment, we would use:
            # pos = pyautogui.locateOnScreen(step['image_path'])
            # pyautogui.click(pos)
            print(f"  > [Simulated] Clicking based on image: {{step['image_path']}}")
            
        # 3. Typing Logic
        if 'TYPE' in step['event'].upper():
            print(f"  > Typing automated sequence...")
            pyautogui.write("Generated Input", interval=0.1)
            
        time.sleep(1)

    print("--- Workflow Execution Complete ---")

if __name__ == "__main__":
    run_agent() 



"""