
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-220
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->explorer.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-220 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 12:27:36.448348+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/3784f5fc-fb7d-4781-a845-010a4473025d.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 12:27:46.434154+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d04bcf32-5825-4bbc-b4ed-129bec693cba.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 12:27:48.718088+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/bbe2945a-b986-499b-be98-dfa175d8d73f.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet",
                "event": "Custom_CLICK",
                "url": "meet.google.com/uir-gkxp-rox?hs=186",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 12:27:54.739237+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/156ed6fa-5774-4301-b778-18bf5b8a8f3a.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Pick up plan",
                "event": "Custom_CLICK",
                "url": "meet.google.com/uir-gkxp-rox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 12:28:07.185601+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/886296b8-515d-40e6-8a56-ef669caafffd.webp",
                "app_name": "explorer.exe",
                "window_title": "Taskbar",
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



