
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-234
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_COPY_ACTION


def run_agent():
    print(f"--- Start Generated Agent for WF-234 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:34:08.611008+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/87bf28e6-e27c-4007-b416-31655c7bbd23.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:34:15.686890+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f411eaae-c6e6-4a60-9378-93f766e30300.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:34:17.970193+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/bc33a8d4-ddc0-4770-b106-566ecb01be93.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:34:18.165204+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f34975b4-e307-4129-b896-db901d41ffc7.webp",
                "app_name": "brave.exe",
                "window_title": "Minimum KG - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1uus61dEu-QVFDmDENAqKVPHpKcJq60nEv2ULgCUYET0/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:34:21.804034+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/0344a4d9-988b-4984-b211-5dd6d100f0a9.webp",
                "app_name": "brave.exe",
                "window_title": "Minimum KG - Google Sheets - Brave",
                "event": "Custom_COPY_ACTION",
                "url": "docs.google.com/spreadsheets/d/1uus61dEu-QVFDmDENAqKVPHpKcJq60nEv2ULgCUYET0/edit?gid=0#gid=0",
                "date": "2026-02-23"
        }
]
    
    for i, step in enumerate(steps):
        print(f"Step {i+1}: {step['event']} in {step['app_name']}")
        
        # 1. Navigation Logic
        if step['url'] and str(step['url']) != 'None':
            print(f"  > Opening URL: {step['url']}")
            webbrowser.open(step['url'])
            time.sleep(4) # Wait for page load
            
        # 2. Click Logic
        if 'CLICK' in step['event'].upper():
            # In a production environment, we would use:
            # pos = pyautogui.locateOnScreen(step['image_path'])
            # pyautogui.click(pos)
            print(f"  > [Simulated] Clicking based on image: {step['image_path']}")
            
        # 3. Typing Logic
        if 'TYPE' in step['event'].upper():
            print(f"  > Typing automated sequence...")
            pyautogui.write("Generated Input", interval=0.1)
            
        time.sleep(1)

    print("--- Workflow Execution Complete ---")

if __name__ == "__main__":
    run_agent() 



