
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-024
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:TYPE->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-024 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:55:00.608907+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/289b0b13-b71a-4bb7-843b-b136468ed355.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:55:03.985273+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/ee86de6a-8e77-45b2-9655-5c8a160d0c2d.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:55:10.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/3284beb2-7ffb-4021-8475-1d8b170a9045.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "TYPE",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:55:15.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5c10c6de-76ad-4399-8319-5e198392eea0.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "TYPE",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:55:48.334345+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/92fc085b-9c28-4ff9-9e02-1904f53bf52c.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
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



