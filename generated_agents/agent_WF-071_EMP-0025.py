
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-071
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:Custom_COPY_ACTION->brave.exe:TYPE->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-071 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:08:44.571614+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/539dacbf-4ec2-4600-8e8e-a0bd23f9fdd0.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:08:45.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/fd172977-d86c-4e07-b6b4-052d1a405fa7.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:08:47.494185+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/136c947a-0ff8-4907-823b-72e3ea15ff46.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_COPY_ACTION",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:08:50.023000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5ff4bcef-f95a-44cc-b2da-7b15403c1ff1.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:08:50.836519+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/2a252e6d-7ca1-4391-8baa-1fefcbd24728.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=0#gid=0",
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



