
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-594
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:MOVE->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-594 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:35:42.051664+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e2e98c67-2d7b-4899-9f9a-5dc809c74011.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:36:00.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ac1c487a-5fb8-435e-8a29-d9fbd9ba6510.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:36:00.516138+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1d63f762-a61a-431e-bc48-44e7fab03dd6.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:36:20.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/65f1802a-cfce-46f6-af1d-a3e7e94abd4d.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "MOVE",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:36:25.151156+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/0d664ff4-546c-4a41-a98c-ef2dd83a1979.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
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



