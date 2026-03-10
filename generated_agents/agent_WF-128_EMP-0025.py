
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-128
# Employee: EMP-0025
# Pattern: brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-128 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:27:45.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/cc0c4e18-3f01-4066-b0b7-b14c86b8787d.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:27:47.140929+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/2d07ed55-8636-49f1-913d-c9e419879633.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:27:50.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5a70957e-987e-461f-ad63-fa9f56935435.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "TYPE",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:27:54.524488+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4947d492-d735-4d47-ade5-23c8c65a253e.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:28:12.362865+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/fe735a7e-f221-4f9c-82bd-737e10c5b260.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
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



