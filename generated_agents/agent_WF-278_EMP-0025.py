
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-278
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-278 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:26:00.684577+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f133da61-4b42-45a5-acff-9fad2a3a0ae8.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:26:01.794000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/44aaef47-b64d-46b9-af57-0637a1ce0158.webp",
                "app_name": "brave.exe",
                "window_title": "New Tab - Brave",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:26:05.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/5ec54c4e-37ce-40ce-af97-078be0fbdb4d.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:26:06.475766+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/5d680abd-2be2-4b23-b269-eeb170db5f15.webp",
                "app_name": "brave.exe",
                "window_title": "New Tab - Brave",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:26:09.603582+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/0802e19f-8a67-4010-bd05-011dd941c8d6.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
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



