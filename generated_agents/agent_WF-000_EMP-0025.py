
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-000
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-000 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:47.603056+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7fa8e6f5-8170-413a-b8fc-939141a2e2af.webp",
                "app_name": "brave.exe",
                "window_title": "Google Calendar - February 2026 - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/messages",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:53.124722+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f75ac111-23de-46d3-ab50-e2d892ee4fbf.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/login",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:54.876378+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/c0ef8052-18ae-4ede-a975-a5d29ec55bf8.webp",
                "app_name": "brave.exe",
                "window_title": "app.afromessage.com is asking you to",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:55.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/a2b082ae-567b-48ed-a16b-3230c2320e58.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube",
                "event": "CLICK",
                "url": "youtube.com/?feature=ytca",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:58.892377+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/236bc1f2-8831-4f22-93af-a83605775724.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/login",
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



