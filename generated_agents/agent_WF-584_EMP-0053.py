
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-584
# Employee: EMP-0053
# Pattern: msedge.exe:Custom_CLICK->msedge.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-584 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:24:40.114928+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2f7bd8f3-e107-4b62-a0a3-42597c301781.webp",
                "app_name": "msedge.exe",
                "window_title": "telebirr_Buy Goods_purchase_goods_0.5n150 (1) (18).pdf and 3 more pages - Personal - Microsoft\u200b Edge",
                "event": "Custom_CLICK",
                "url": "https://admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:24:43.191620+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/8ddabe4a-746e-4cce-960c-4c4a8bafe7b2.webp",
                "app_name": "msedge.exe",
                "window_title": "Reports and 3 more pages - Personal - Microsoft\u200b Edge",
                "event": "Custom_CLICK",
                "url": "https://admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:24:43.878000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/cac2f493-5799-41e8-b743-381b61ef5f87.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "APP_SWITCH",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:24:47.197391+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ae0bd05c-d00c-4aa9-bedd-c227e0320ae0.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:24:50.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2fcd6e63-84e0-4a72-9fd4-43ed3965b0ff.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/users - Google Chrome",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users",
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



