
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-030
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-030 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:56:08.213428+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/c0a345d3-4c8c-47e7-986d-9c979e27168e.webp",
                "app_name": "brave.exe",
                "window_title": "doc-14-6s-sheets.googleusercontent.com wants to save",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:56:14.213976+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/cc7209fc-1e80-4d47-9fae-bad1dba162ff.webp",
                "app_name": "brave.exe",
                "window_title": "Recent download history",
                "event": "Custom_CLICK",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:56:15.823993+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/29712aa6-38f3-4303-9e2d-60d739aa560c.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:56:16.804000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/2fd3e7b1-c0e9-4abc-a40e-3942df92ec5b.webp",
                "app_name": "brave.exe",
                "window_title": "Recent download history",
                "event": "APP_SWITCH",
                "url": "chatgpt.com/c/6971ec05-c49c-8329-bd7c-ccc7a52dad7b",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:56:30.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f29f3121-bbbe-4370-ac57-d9ff98de96bb.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "TYPE",
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



