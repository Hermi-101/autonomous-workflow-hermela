
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-321
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-321 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:32:58.780912+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/315cffb7-3d49-4a75-9c34-bc559c738d78.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/66/?native_filters_key=Y0a9RQKKdwtUQLVl2jmR1Z5lzml2_A7ROuAhZc7wKmFn2Inokd43s4BJzs2DlGjO",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:09.499157+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/0a5942f7-df39-46c1-be66-8a83e22b37ef.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:10.047000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/337ab0ff-1cb3-4199-a7ad-566aa45008b6.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:27.634399+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/27d95c78-5c80-4c93-8aef-7b3952aeaff0.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:53.725875+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/3b87657d-85ed-4143-8c09-7807a9b82808.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
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



