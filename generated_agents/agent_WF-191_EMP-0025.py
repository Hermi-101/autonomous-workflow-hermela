
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-191
# Employee: EMP-0025
# Pattern: explorer.exe:Custom_CLICK->explorer.exe:TYPE->explorer.exe:Custom_CLICK->explorer.exe:Custom_CLICK->explorer.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-191 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:58:00.420117+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d2b0056d-ba6b-478f-a375-abff24cfd466.webp",
                "app_name": "explorer.exe",
                "window_title": "com.mate - File Explorer",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:58:35.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8ad802fb-b9fb-473f-b4c6-3190bc31ff81.webp",
                "app_name": "explorer.exe",
                "window_title": "com.mate - File Explorer",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:58:37.688869+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7482b758-0021-4533-98ba-f32be007dd91.webp",
                "app_name": "explorer.exe",
                "window_title": "com.mate - File Explorer",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:59:09.901434+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/fb2cfb95-646f-4977-a2f8-343c41664fa3.webp",
                "app_name": "explorer.exe",
                "window_title": "com.mate - File Explorer",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:59:10.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/45969afb-ad9e-43d1-97a0-25796d80b625.webp",
                "app_name": "explorer.exe",
                "window_title": "Canceling...",
                "event": "CLICK",
                "url": "",
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



