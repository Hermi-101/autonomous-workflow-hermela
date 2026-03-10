
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-302
# Employee: EMP-0025
# Pattern: brave.exe:APP_SWITCH->brave.exe:CLICK->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-302 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:40.929000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ac7b890a-c824-418e-a491-e97d99e46cae.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "APP_SWITCH",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:50.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/630def70-1c65-4384-8dc2-cabee6a6d1c3.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:55.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/79447c36-03ea-4019-98d6-7b656815a04c.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:55.645672+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/60c73021-eef5-44f3-a841-70ff7360c0ed.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:58.534734+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b950cec2-ce8c-4bc7-8de4-8959545a9356.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/logistic - Brave",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/logistic",
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



