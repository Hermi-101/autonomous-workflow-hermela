
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-442
# Employee: EMP-0028
# Pattern: EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:CLICK->EXCEL.EXE:Custom_CLICK->EXCEL.EXE:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-442 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:25:58.390293+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/6ed28110-a4a9-4ecc-9476-b0c1b9709cc6.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:26:01.948335+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/c9f345bd-923d-479c-bd63-c84d99f0c486.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Format Cells",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:26:05.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/7d214b3f-657a-4693-95f0-724dc18535c2.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_471_20260224T082528",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:26:05.064734+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/1e3f7aa1-f84f-4deb-907d-ed18260c754a.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Format Cells",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:26:07.501423+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/c29a4eae-d891-422e-8ef1-b7494f3a6876.webp",
                "app_name": "EXCEL.EXE",
                "window_title": "Microsoft Excel (Product Activation Failed) - sqllab_untitled_query_471_20260224T082116",
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



