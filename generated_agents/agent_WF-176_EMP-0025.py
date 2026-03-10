
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-176
# Employee: EMP-0025
# Pattern: brave.exe:CLICK->brave.exe:TYPE->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-176 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:17:55.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/cbda0855-302b-4191-bae2-b0d51b2a1e53.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=174774035#gid=174774035",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:18:15.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/eb0ea2ca-2c02-4af3-b2c3-cc49848b746b.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=174774035#gid=174774035",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:18:19.416841+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/ed8b49c7-424e-4215-aba6-99cbb1e48d0a.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=174774035#gid=174774035",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:18:20.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b000b860-7f99-4cc8-998b-54248d7cb592.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=174774035#gid=174774035",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:18:20.298511+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8ffa1369-93a9-45a0-9730-3218df850c03.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=174774035#gid=174774035",
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



