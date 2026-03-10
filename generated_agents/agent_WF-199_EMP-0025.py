
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-199
# Employee: EMP-0025
# Pattern: explorer.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-199 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:33:43.333506+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/9bc29683-e138-44c9-9c56-75f5b346a114.webp",
                "app_name": "explorer.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1-Xd4t8_5INQWN3KuJS-wlKGJszyjwlFru_Lf3c69Zj4/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:33:49.697726+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/e67c587f-a69a-4833-91a0-768257a10b0d.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1-Xd4t8_5INQWN3KuJS-wlKGJszyjwlFru_Lf3c69Zj4/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:33:59.855335+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4d900e0e-8bc8-4521-931e-68ade447a465.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3939f550a59_5_782#slide=id.g3939f550a59_5_782",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:34:02.536797+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/527c2f06-b486-4e6f-a8ac-6205626ae5ef.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3942b317c9c_1_679#slide=id.g3942b317c9c_1_679",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:34:50.154216+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/0e96571a-13ae-479b-a5d8-484eefc6f21d.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "",
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



