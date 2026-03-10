
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-537
# Employee: EMP-0028
# Pattern: EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-537 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:53.482464+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/e4bf73ac-9a86-401b-9af8-94c9220f7014.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:54.604436+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/d8c63acd-312f-4807-98ba-75bf72342687.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_472_20260224T131149",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:58:55.847742+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/e1625913-3178-4b80-9fa7-810b2e8ecbb2.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
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



