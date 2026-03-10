
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-614
# Employee: EMP-0053
# Pattern: ShellExperienceHost.exe:Custom_CLICK->ShellExperienceHost.exe:Custom_CLICK->ShellExperienceHost.exe:Custom_CLICK->ShellExperienceHost.exe:Custom_CLICK->ShellExperienceHost.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-614 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:57:37.677536+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/83060740-bc31-4919-ba35-6a7638a1a2e7.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:57:39.154413+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1dbbea08-5fdd-44b6-a1ee-b8836a56aca9.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:57:56.008115+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/b790bfb3-43d9-4f5e-a7fa-390617a6be0c.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:57:57.826325+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/bbe4706b-be6c-48f0-b9a0-6161f0a96506.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:58:03.749469+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7264b0d9-1ef5-4dcc-bf53-7646dd40a9aa.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "Custom_CLICK",
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



