
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-316
# Employee: EMP-0028
# Pattern: chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-316 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:16.542000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/d00e3b06-e76f-45fb-bf46-d2527f568474.webp",
                "app_name": "chrome.exe",
                "window_title": "Copy of Fuel - Google Sheets - Google Chrome",
                "event": "APP_SWITCH",
                "url": "onspace.ai/pricing",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:19.448472+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/a22177f3-3e79-4886-86be-8858ed055bfd.webp",
                "app_name": "chrome.exe",
                "window_title": "Copy of Fuel - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "onspace.ai/pricing",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:27.086007+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/bd706fb0-fcb6-47cb-a6e1-7aaab1ae7d81.webp",
                "app_name": "chrome.exe",
                "window_title": "OnSpace.AI - Pricing - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1O5t-aEaANKmGLqhLmDyCGRhX6nt6Gva8Ahv8Dfr2Lzo/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:39.391878+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/da8bd359-91b5-448e-8696-c4d9d169e0f5.webp",
                "app_name": "chrome.exe",
                "window_title": "agents - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "onspace.ai/pricing",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:40.020000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/76df1373-f6b6-4033-9321-c5feba313fea.webp",
                "app_name": "chrome.exe",
                "window_title": "Data definition - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1Xf9iorSzYbCHDrsKpJbYqCt6W8fa2f1N3bD1uQ4eSfI/edit?gid=0#gid=0",
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



