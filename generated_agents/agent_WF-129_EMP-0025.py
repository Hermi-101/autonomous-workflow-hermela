
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-129
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:Custom_CLICK->brave.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-129 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:29:57.194589+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/97c136f6-2e81-43ee-902f-eccd5fa2e4ce.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:29:59.684582+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4796e878-bb59-442d-b0cd-2e920151acd0.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:30:00.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/0db37399-cdfb-4421-9148-bf66a288974e.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "TYPE",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0#heading=h.9y6gvut4310c",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:30:02.372187+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/17868fb9-96fd-4049-a8c6-e797735b9f47.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/document/d/1rFTtec0arUCwffpSzHOLAipzsT740VdqVJb-awXoQYg/edit?tab=t.0#heading=h.9y6gvut4310c",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:30:25.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4583eaf8-bd7b-4edf-b4fe-f0fe10087e88.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "CLICK",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
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



