
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-006
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-006 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:27.973948+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b3232445-30a3-4747-a057-3ea43cd4aeeb.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Josh Johnson | Charity Accidentally Gives People Meth - YouTube",
                "event": "Custom_CLICK",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:29.751667+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/bc440974-dd0d-477e-a975-2f08be14deea.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "Custom_CLICK",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:30.328000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f9edf8a4-fda0-4de7-98c0-49d55ba5d13d.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "APP_SWITCH",
                "url": "app.afromessage.com/lists",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:31.965065+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8d43f193-772b-4aa1-aeac-7892137a81f5.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/dashboard",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:39.050123+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/cd35f8f6-304c-4c71-bb07-cea28972f986.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/lists",
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



