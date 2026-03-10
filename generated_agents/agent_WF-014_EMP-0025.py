
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-014
# Employee: EMP-0025
# Pattern: brave.exe:APP_SWITCH->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-014 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:02.706000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/131a7600-d40f-495e-9861-6795cc9d65e2.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/superset/dashboard/33/?native_filters_key=ZMZfegB6UaLOJJ6PMcBuUtklbhqHx9fcDCun11iVZ5F9HM-2HB2-2ajb1HLYQsno",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:05.748105+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/e9eb7d9b-9b5e-4a86-adff-afb11cc2cd9c.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/dashboard/list/?pageIndex=0&sortColumn=changed_on_delta_humanized&sortOrder=desc&viewMode=table",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:10.614241+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/98ef1b03-aefb-4ded-a6fc-122ad1a8049b.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/33/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:25.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/04a89b5c-8225-4ff0-9513-9ddbcfb94c0a.webp",
                "app_name": "brave.exe",
                "window_title": "[ user incentives ] - Brave",
                "event": "CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/33/?native_filters_key=ZMZfegB6UaLOJJ6PMcBuUtklbhqHx9fcDCun11iVZ5F9HM-2HB2-2ajb1HLYQsno",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:26.000929+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d496b558-3914-489e-9943-d530985f1968.webp",
                "app_name": "brave.exe",
                "window_title": "[ user incentives ] - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/33/?native_filters_key=ZMZfegB6UaLOJJ6PMcBuUtklbhqHx9fcDCun11iVZ5F9HM-2HB2-2ajb1HLYQsno",
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



