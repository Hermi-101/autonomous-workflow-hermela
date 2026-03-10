
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-540
# Employee: EMP-0028
# Pattern: EXCEL.EXE:APP_SWITCH->EXCEL.EXE:APP_SWITCH->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-540 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:10.758000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/5ab7e939-ef30-48ea-8790-b61677a695c0.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_472_20260224T121412",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:11.772000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/173b8c34-a30c-4eb9-bff0-50a8ddc7592b.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:23.370958+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/82ce302b-6dde-4601-a08a-6a5ba690e1cf.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_472_20260224T115829",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:24.766022+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/36b1272a-18b0-4fbc-930a-cd4429a308b1.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:59:25.920326+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/b080419c-2b66-4ec6-8de0-57ab7f901166.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_472_20260224T115510",
                "event": "Custom_CLICK",
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



