
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-194
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-194 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:26:14.343514+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/71914d6e-0b2a-4ef0-b321-7e38cab89ccc.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3939f550a59_5_814#slide=id.g3939f550a59_5_814",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:27:45.416941+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b6be7cce-b452-4cc1-a2e9-c1d9541049bc.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:28:32.056231+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/035ba349-6eab-41ca-b4e2-6934724aefe0.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3939f550a59_5_814#slide=id.g3939f550a59_5_814",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:29:59.458036+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/22c7c012-adce-4de3-b2f0-8a369011bb86.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:30:09.379249+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d82a17f5-9278-4efd-ab09-a1666ab54109.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSocial backend @ \u200eNA (6824)",
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



