
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-631
# Employee: EMP-0053
# Pattern: chrome.exe:MOVE->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-631 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:49:45.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/802e0de1-c47c-4848-8ad7-857e829d6f85.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "MOVE",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:50:01.536453+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ff515d5d-21dc-4290-bd08-72fbe85d5284.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:50:25.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1bca6b40-b84f-4dc4-bec4-205c8389aecd.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=129142762#gid=129142762",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:50:25.313513+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e95ba744-14d3-4003-8a60-f3de6fdd79be.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=129142762#gid=129142762",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:51:16.557941+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7b7fcba3-ed67-4a7e-bfe7-97a38325a7e1.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating (Responses) - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=129142762#gid=129142762",
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



