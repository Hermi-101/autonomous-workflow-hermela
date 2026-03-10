
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-307
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-307 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:59:55.284278+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/7d5d07fe-b074-4c47-804b-255108dd5a81.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 10:00:10.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/fca5cfa4-bebe-40be-9346-79ba8d3080af.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 10:00:35.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/8c8993c7-915b-4971-9bf8-b2990fd9b287.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/warehouse - Brave",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/warehouse",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 10:00:38.944136+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f3058109-2a3f-4352-82de-3b395ec112c4.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/warehouse",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 10:00:40.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/94175c88-8e4c-4689-a675-4dae9b25d7ad.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/warehouse - Brave",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/warehouse",
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



