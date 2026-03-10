
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-538
# Employee: EMP-0028
# Pattern: EXCEL.EXE:Custom_CLICK->EXCEL.EXE:APP_SWITCH->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:APP_SWITCH->EXCEL.EXE:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-538 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:57.027160+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/4fcae52b-2969-43e4-8604-3a65c08e9339.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_475_20260224T134903",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:57.482000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/51bf7850-1175-4fe3-81e7-4df52064a87c.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:58.203231+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/50cdaeb9-f3f1-4bf9-8eef-a647d2ed0a59.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:58.502000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/0d7d76ee-75cb-4ba1-84c9-7ae8f3ba0747.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_475_20260224T133327",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:05.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/0f3a5e4c-40dc-4a83-befb-8a638ac1f40d.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "CLICK",
                "url": "",
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



