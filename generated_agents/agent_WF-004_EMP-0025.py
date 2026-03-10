
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-004
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-004 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:50:58.892377+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/236bc1f2-8831-4f22-93af-a83605775724.webp",
                "app_name": "brave.exe",
                "window_title": "Afro Message | The Enterprise Grade SMS Service Provider In Ethiopia! - Brave",
                "event": "Custom_CLICK",
                "url": "app.afromessage.com/login",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:01.391354+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d92f3f19-666b-4a9d-94cf-ab54fcdbd876.webp",
                "app_name": "brave.exe",
                "window_title": "Sign in - Google Accounts - Brave",
                "event": "Custom_CLICK",
                "url": "accounts.google.com/v3/signin/accountchooser?client_id=163171907328-e5p792gfab1pndm9l1i0g73jlpl1o0td.apps.googleusercontent.com&fetch_basic_profile=true&gsiwebsdk=2&include_granted_scopes=true&redirect_uri=storagerelay%3A%2F%2Fhttps%2Fapp.afromessage.com%3Fid%3Dauth76258&response_type=permission+id_token&scope=email+profile+openid&ss_domain=https%3A%2F%2Fapp.afromessage.com&dsh=S-1405410832%3A1771829450791967&o2v=1&service=lso&flowName=GeneralOAuthFlow&opparams=%253Fopenid.realm%2526ss_domain%253Dhttps%25253A%25252F%25252Fapp.afromessage.com&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAMehJ6A0bRkCe-sVYgXBJOehav93rQe23AKJZF2fwYuIJg_XmM_V3o-2RJNH8mAbte0GI0LD1JWxzucSBeeR-7Xw1-Edo4FSo5MQj8V7X956A2ZrfFiBPPzym7hVZ7LaOoy96mmcUPMnISvcAv46eIC4s1_1FBSKWSZNojlJ2WBobO3VV1FCWd7D-eSMlNpSRTvvXkJIhDY0KQZ9XEXOINoswkjMuauno9U7Of0pQrGpD1CIlauO1XzIroNu3mY_PGhi18PMr9elhfiyvbycVcCAO4joX9XoMn50bBP-1HP9CSh7mENuVE_VqJuzRL7A8oeIIvj0aWc7fh4G5voACAaGD0zzuw-fUbGZS3l863vGNDDSg7QQ9C9VW75-ytOMPSh4Z52a-eJ8MHoviB2bj6lrwPzpptdlWxXIcSK3ujmKPqSGAmd4FPyQKu04_1qDrMt0Y7-CfORXWQGiBeYdsR9EnpdM31PPOCDxK0Opia03SQsWO4%26flowName%3DGeneralOAuthFlow%26as%3DS-1405410832%253A1771829450791967%26client_id%3D163171907328-e5p792gfab1pndm9l1i0g73jlpl1o0td.apps.googleusercontent.com%26requestPath%3D%252Fsignin%252Foauth%252Fconsent%23&app_domain=https%3A%2F%2Fapp.afromessage.com",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:02.789132+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b78d18c9-fa41-4ec9-8560-5afe9e64719c.webp",
                "app_name": "brave.exe",
                "window_title": "Sign in - Google Accounts - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:03.573000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d88504af-121b-42f5-ad36-c291ac35a79e.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube",
                "event": "APP_SWITCH",
                "url": "youtube.com",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:51:05.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/1d625beb-87b5-4aa0-b971-a8e2dad79991.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) YouTube",
                "event": "MOVE",
                "url": "youtube.com",
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



