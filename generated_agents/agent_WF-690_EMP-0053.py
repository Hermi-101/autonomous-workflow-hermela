
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-690
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->ShellExperienceHost.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-690 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 07:38:42.351982+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/fc2a15d3-f95e-44b5-bc30-3b144f02a64d.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 07:38:44.671985+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/4c67a9ec-3d04-4532-9020-17489c99ee55.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 07:38:45.457546+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/920e31b4-1301-4b4c-87c8-2fa3132fb476.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 07:38:54.305543+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/640eb4ed-aa4c-4663-9d8f-3543c4894cf7.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 07:38:57.246149+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/f9fbac50-8a01-4a62-99c6-2451929bdca9.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
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



