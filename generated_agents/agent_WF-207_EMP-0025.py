
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-207
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_PASTE_ACTION->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-207 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:48:31.713271+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7e058115-6a75-48cf-86be-4d411d09f36b.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=1436656147#gid=1436656147",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:48:38.295685+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7692987f-6733-4740-84ef-faca7fd45cc3.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=1436656147#gid=1436656147",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:48:41.211638+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d6a8c8af-0550-4729-96ea-d427dc1d0076.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=7012948#gid=7012948",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:48:58.236411+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/ddb534e4-1719-40fb-ae0e-5ac1ccb7e35c.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_PASTE_ACTION",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=7012948#gid=7012948",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:48:59.813885+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/6669de13-566d-4c5e-aca0-59308f3ecd72.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=7012948#gid=7012948",
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



