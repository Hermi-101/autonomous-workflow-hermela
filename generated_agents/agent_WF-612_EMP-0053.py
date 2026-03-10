
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-612
# Employee: EMP-0053
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-612 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:53:47.338000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/145296dc-4373-4bda-b1d6-2f781c4b64be.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMiss Sun @ \u200eChip Chip Social (5527)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:53:51.905849+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/5ea6c751-c2f6-4d45-801e-9dd9ccc2b01e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMiss Sun @ \u200eChip Chip Social (5527)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:54:06.288754+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/00b212ae-b347-4dac-920a-3beb732c10f0.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:54:38.442073+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7f2cd65a-9d5c-4791-852e-5fa016a8a251.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:54:40.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/784f756f-cb9a-4c91-b5b2-b730e6df18c2.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/redelivery",
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



