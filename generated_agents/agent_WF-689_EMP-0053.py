
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-689
# Employee: EMP-0053
# Pattern: chrome.exe:APP_SWITCH->chrome.exe:CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-689 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 06:18:39.624000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/dd921652-7095-4b43-8e5c-70a191d4ca71.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "APP_SWITCH",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 06:18:40.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/9a2d7b25-5648-40e6-8730-bcec1fe9448b.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 06:18:51.801000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/a595d9cc-5144-47be-9a70-0dcd79e90b58.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 06:18:53.247143+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/38f34bca-1077-40d7-840e-e04cdf0a9dab.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 06:18:55.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/0324c686-c6bd-4c52-8e09-30f075e88904.webp",
                "app_name": "chrome.exe",
                "window_title": "Metabase - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1qB3-hcpH6OFaPmZ--OIy6qiWXIjnoilsGDyIOEuCB-A/edit?gid=0#gid=0",
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



