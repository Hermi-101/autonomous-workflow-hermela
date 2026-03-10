
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-640
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-640 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:51:23.657504+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e2c295ce-a313-4be0-b321-95ac96923d43.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:51:28.979106+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/367b3d92-e115-4a20-b2d7-f95013100156.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:51:30.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/4241b7d5-05f7-48ff-a86c-17992266bde1.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:51:40.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/33d3075e-0c3b-4786-a232-796525a7d8db.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:51:42.349655+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/36bdabe3-0d83-41c2-99b7-86a3f359b4d0.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
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



