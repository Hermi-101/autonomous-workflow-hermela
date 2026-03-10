
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-141
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:TYPE->brave.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-141 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:34:55.598061+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8e7cf7e6-f9dd-427c-9b28-06ddf8cce76e.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:35:34.578234+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/9b3f36ab-0d49-44be-a543-f42d45401b96.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3be12b1b3f4_0_148#slide=id.g3be12b1b3f4_0_148",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:36:00.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/64e989c7-814b-40af-98c5-9670eaf0fd9c.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "TYPE",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3be12b1b3f4_0_148#slide=id.g3be12b1b3f4_0_148",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:36:05.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/46aef424-c6a3-4ff7-ba44-66882c4c567f.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "TYPE",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3be12b1b3f4_0_148#slide=id.g3be12b1b3f4_0_148",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:36:30.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/53f1c7dd-911c-4c68-a582-de918dc916b7.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "TYPE",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?slide=id.g3be12b1b3f4_0_148#slide=id.g3be12b1b3f4_0_148",
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



