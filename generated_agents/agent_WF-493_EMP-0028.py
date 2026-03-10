
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-493
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-493 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:32:33.754390+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/940a0807-4016-44dd-8b73-63d6d321b3e6.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "207.154.221.209:9903/question/281-accepted-with-flash-sales-and-supergroup-leader",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:32:34.477000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/b14cb035-6023-468f-ae70-6e55a7ea5f10.webp",
                "app_name": "chrome.exe",
                "window_title": "Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "207.154.221.209:9903/question/281-accepted-with-flash-sales-and-supergroup-leader",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:32:38.563000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/5a45e7eb-dc8d-4182-98e4-0271a111d896.webp",
                "app_name": "chrome.exe",
                "window_title": "Doing science... \u00b7 Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:32:42.840275+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/e886ab77-de8d-40f9-9940-15e9b0691783.webp",
                "app_name": "chrome.exe",
                "window_title": "Doing science... \u00b7 Metabase - Google Chrome",
                "event": "Custom_CLICK",
                "url": "207.154.221.209:9903/question/281-accepted-with-flash-sales-and-supergroup-leader",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:32:47.556219+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/133cfba4-df1e-4548-ab4a-c7e415a1e6be.webp",
                "app_name": "chrome.exe",
                "window_title": "Doing science... \u00b7 Metabase - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
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



