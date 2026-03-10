
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-137
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-137 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:33:53.753290+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d3cff650-233e-4250-b3d3-cfe214d63f27.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=802127652#gid=802127652",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:34:50.139431+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7dc57497-30fa-406b-81e8-46f5430543e8.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBstKKKGrxMnNHlTwdTqzXLSB",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:34:50.282000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f6e95be8-fb19-4f2b-8a89-630bc6588f48.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project ... - @amir@chipchip.social , @natiassefa5@... - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:34:53.491415+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d3c60b9c-91aa-43da-8f40-003464cfb319.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project ... - @amir@chipchip.social , @natiassefa5@... - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/presentation/d/1W9WyQLl8IuMMhkfkDVCNXvjhjuQCFB3XEysWAz-33hw/edit?disco=AAAB0p8kvMw&usp=comment_email_document&ts=699bfc1d&usp_dm=true",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:34:54.395000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/7834c12e-9401-47b0-a0b8-ae23bec9ea76.webp",
                "app_name": "brave.exe",
                "window_title": "Untitled - Brave",
                "event": "APP_SWITCH",
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



