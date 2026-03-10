
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-630
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:MOVE->chrome.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-630 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:47:36.755243+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/a822481b-b711-4b0c-911c-153dddef21ff.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:47:39.320966+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/bebd43bd-a751-487f-a5a6-a80136a462db.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:47:51.948395+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/336cb200-65d7-4911-9265-04633329b26f.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:49:00.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/211e2ac4-f249-4341-b61c-7be61ac90f0c.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "MOVE",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:49:05.007000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/061fb7c8-bd2c-4781-aa1f-1b8ff82fd584.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "MOVE",
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



