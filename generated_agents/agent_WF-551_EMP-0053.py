
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-551
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-551 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:08:20.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f2f08f00-8889-4443-b078-83f8fcb0a3eb.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/refund",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:08:23.874017+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ef0b3125-3ea6-4ce8-9fd9-b4dd32c72c80.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/refund",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:08:25.625462+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/92254eea-6850-4bed-8667-bdeeeda221e1.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/refund",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:08:27.445751+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e369fc62-2621-4398-b6a7-5e6a0a0cdfb6.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/refund",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:09:05.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3e32e2a7-a0b8-42a2-bdc7-e06de4734d4e.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/refund - Google Chrome",
                "event": "MOVE",
                "url": "chipchipadmindec.chipchip.social/dashboard/refund",
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



