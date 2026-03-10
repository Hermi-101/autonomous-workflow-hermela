
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-575
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:APP_SWITCH->chrome.exe:CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-575 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:19:54.752007+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/055e2cd7-0637-4c3e-84ce-5adb3e4277d7.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/groups/groupDetails?id=462aa677-53e4-4f33-b4e2-cfc957718283 - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:19:54.853000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/856d1cd5-78b0-49b2-847c-a7460cce2369.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "APP_SWITCH",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:19:56.902000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/47001f45-6382-44fc-aef1-de234b588fe7.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "APP_SWITCH",
                "url": "chipchipadmindec.chipchip.social/dashboard/users",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:20:00.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f82f4893-728b-448d-8546-16c5b9747617.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/users - Google Chrome",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:20:04.964248+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ea0107aa-5143-4c81-a96e-d4c46e668714.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/groups/groupDetails?id=462aa677-53e4-4f33-b4e2-cfc957718283",
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



