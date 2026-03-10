
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-541
# Employee: EMP-0028
# Pattern: EXCEL.EXE:Custom_CLICK->EXCEL.EXE:APP_SWITCH->EXCEL.EXE:APP_SWITCH->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-541 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:28.294003+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/70c728e9-b0d6-40dc-bdfd-f06a01f4b231.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - 20260224_105451  [Protected View]",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:29.145000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/61d29dd5-1704-4cf6-b024-451cb8c39b18.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_471_20260224T082528",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:30.164000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/dace1e7b-7696-44f6-890f-d71c975d0220.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:34.012934+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/195c4b04-ec57-46e1-8e65-549d57db93ba.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:34.238000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/472012c0-8633-43d2-a33f-d875db23cf9b.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_470_20260223T122310",
                "event": "APP_SWITCH",
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



