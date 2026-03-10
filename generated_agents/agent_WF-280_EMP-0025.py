
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-280
# Employee: EMP-0025
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-280 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:11:17.562000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/af924c0b-2290-4403-b11a-af07b872bb7b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNA (6928)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:11:20.651000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/1f266663-5f57-43e5-82e6-5018a4e4ccc0.webp",
                "app_name": "Telegram.exe",
                "window_title": "(369) \u200eShower Thoughts \ud83d\udebf @ \u200eNA (6927)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:11:20.895872+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/2f0dc96d-9362-4d97-96bf-393025355463.webp",
                "app_name": "Telegram.exe",
                "window_title": "(369) \u200eShower Thoughts \ud83d\udebf @ \u200eNA (6927)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:11:21.687000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/9fa40067-3c76-4ada-b461-5fa008f8a365.webp",
                "app_name": "Telegram.exe",
                "window_title": "(8) \u200eYazz - ChipChip Operation Team @ \u200eNA (6922)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:11:23.737000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/10045052-b015-44d7-9a25-08a92689dfef.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNA (6914)",
                "event": "APP_SWITCH",
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



