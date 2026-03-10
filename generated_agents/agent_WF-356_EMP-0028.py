
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-356
# Employee: EMP-0028
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-356 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:53:55.032000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/d029e482-4119-41f3-b1b9-15e14fe95a8c.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "207.154.221.209:9903/question#eyJkYXRhc2V0X3F1ZXJ5Ijp7InR5cGUiOiJuYXRpdmUiLCJkYXRhYmFzZSI6MiwibmF0aXZlIjp7InF1ZXJ5IjoiXHJcbi0tIHNlbGVjdCBcclxuLS0gZGlzdGluY3QgXHJcbi0tIHUubmFtZSBhcyBuYW1lICwgdS5waG9uZSBhcyBwaG9uZSAgLS0sIGNvdW50KCBkaXN0aW5jdCBvLmlkICkgYXMgZ3JvdXBzIFxyXG4tLSAtLSBmcm9tIHVzZXJzIHUgXHJcblxyXG4tLSBGUk9NIGdyb3VwX2RlYWxzIGdkIFxyXG4tLSAgICAgSk9JTiBncm91cHMgZyBPTiBnLmdyb3VwX2RlYWxzX2lkID0gZ2QuaWRcclxuLS0gICAgIEpPSU4gZ3JvdXBzX2NhcnRzIGdjIE9OIGdjLmdyb3VwX2lkID0gZy5pZCBhbmQgIGcuY3JlYXRlZF9ieSA9IGdjLnVzZXJfaWRcclxuLS0gICAgIEpPSU4gb3JkZXJzIG8gT04gby5ncm91cHNfY2FydHNfaWQgPSBnYy5pZCBcclxuLS0gICAgIEpPSU4gdXNlcnMgdSBPTiB1LmlkID0gZ2MudXNlcl9pZFxyXG4tLSAgICAgSk9JTiBwcm9kdWN0cyBwIE9OIGdkLnByb2R1Y3RfaWQgPSBwLmlkXHJcbi0tICAgICBKT0lOIHByb2R1Y3RfbmFtZXMgcG4gT04gcC5uYW1lX2lkID0gcG4uaWRcclxuLS0gICAgIEpPSU4gZGVsaXZlcnlfdHJhY2tzIGQgT04gZ2MuaWQgPSBkLmdyb3VwX2NhcnRfaWRcclxuLS0gICAgICAgICB3aGVyZSAgZ2Muc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbi0tICAgICAgICAgQU5EIG8uc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbi0tICAgICAgICAgQU5EIGcuc3RhdHVzID0gJ0NPTVBMRVRFRCdcclxuLS0gICAgICAgICBBTkQgby5kZWxldGVkX2F0IElTIE5VTExcclxuLS0gICAgIC0tICAgYW5kICBEQVRFKG8uY3JlYXRlZF9hdCkgIEJFVFdFRU4gJzIwMjYtMDEtMTYnIEFORCAnMjAyNi0wMi0xNidcclxuLS0gICAgICAgYW5kICBEQVRFKG8uY3JlYXRlZF9hdCkgICBCRVRXRUVOICcyMDI1LTA5LTIwJyBBTkQgJzIwMjYtMDItMjAnXHJcblxyXG5cclxuXHJcblxyXG5TRUxFQ1RcclxuZGlzdGluY3QgXHJcbi0tIGRhdGVfdHJ1bmMoJ3dlZWsnLCBvLmNyZWF0ZWRfYXQpLFxyXG4gICAgdS5uYW1lIEFTIG5hbWUsIFxyXG4gICAgdS5waG9uZSBBUyBwaG9uZVxyXG4gICAgXHJcbkZST00gXHJcbiAgICBncm91cF9kZWFscyBnZCBcclxuSk9JTiBcclxuICAgIGdyb3VwcyBnIE9OIGcuZ3JvdXBfZGVhbHNfaWQgPSBnZC5pZFxyXG5KT0lOIFxyXG4gICAgZ3JvdXBzX2NhcnRzIGdjIE9OIGdjLmdyb3VwX2lkID0gZy5pZCBBTkQgZy5jcmVhdGVkX2J5ID0gZ2MudXNlcl9pZFxyXG5KT0lOIFxyXG4gICAgb3JkZXJzIG8gT04gby5ncm91cHNfY2FydHNfaWQgPSBnYy5pZCBcclxuSk9JTiBcclxuICAgIHVzZXJzIHUgT04gdS5pZCA9IGdjLnVzZXJfaWRcclxuSk9JTiBcclxuICAgIHByb2R1Y3RzIHAgT04gZ2QucHJvZHVjdF9pZCA9IHAuaWRcclxuSk9JTiBcclxuICAgIHByb2R1Y3RfbmFtZXMgcG4gT04gcC5uYW1lX2lkID0gcG4uaWRcclxuSk9JTiBcclxuICAgIGRlbGl2ZXJ5X3RyYWNrcyBkIE9OIGdjLmlkID0gZC5ncm91cF9jYXJ0X2lkXHJcbldIRVJFICBcclxuICAgIGdjLnN0YXR1cyA9ICdDT01QTEVURUQnIFxyXG4gICAgQU5EIG8uc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbiAgICBBTkQgZy5zdGF0dXMgPSAnQ09NUExFVEVEJ1xyXG4gICAgQU5EIG8uZGVsZXRlZF9hdCBJUyBOVUxMXHJcbiAgICBBTkQgby5jcmVhdGVkX2F0IEJFVFdFRU4gJzIwMjUtMDktMjAnIEFORCAnMjAyNi0wMi0yMCcgXHJcbkdST1VQIEJZIFxyXG4gICAgdS5pZCwgdS5uYW1lLCB1LnBob25lLCBkYXRlX3RydW5jKCd3ZWVrJywgby5jcmVhdGVkX2F0KVxyXG5IQVZJTkcgXHJcbiAgICBDT1VOVChESVNUSU5DVCBvLmlkKSA-PSAyXHJcbk9SREVSIEJZIFxyXG4gICAgdS5uYW1lIiwidGVtcGxhdGUtdGFncyI6e319fSwiZGlzcGxheSI6InRhYmxlIiwiZGlzcGxheUlzTG9ja2VkIjp0cnVlLCJwYXJhbWV0ZXJzIjpbXSwidmlzdWFsaXphdGlvbl9zZXR0aW5ncyI6e319",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:53:56.779908+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/2f6dd4d4-7408-4abd-8250-bed8f6bb043b.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:54:06.326506+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ab4adb54-1911-41e2-bc17-e8e29ad5f84f.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "207.154.221.209:9903/question#eyJkYXRhc2V0X3F1ZXJ5Ijp7InR5cGUiOiJuYXRpdmUiLCJkYXRhYmFzZSI6MiwibmF0aXZlIjp7InF1ZXJ5IjoiXHJcbi0tIHNlbGVjdCBcclxuLS0gZGlzdGluY3QgXHJcbi0tIHUubmFtZSBhcyBuYW1lICwgdS5waG9uZSBhcyBwaG9uZSAgLS0sIGNvdW50KCBkaXN0aW5jdCBvLmlkICkgYXMgZ3JvdXBzIFxyXG4tLSAtLSBmcm9tIHVzZXJzIHUgXHJcblxyXG4tLSBGUk9NIGdyb3VwX2RlYWxzIGdkIFxyXG4tLSAgICAgSk9JTiBncm91cHMgZyBPTiBnLmdyb3VwX2RlYWxzX2lkID0gZ2QuaWRcclxuLS0gICAgIEpPSU4gZ3JvdXBzX2NhcnRzIGdjIE9OIGdjLmdyb3VwX2lkID0gZy5pZCBhbmQgIGcuY3JlYXRlZF9ieSA9IGdjLnVzZXJfaWRcclxuLS0gICAgIEpPSU4gb3JkZXJzIG8gT04gby5ncm91cHNfY2FydHNfaWQgPSBnYy5pZCBcclxuLS0gICAgIEpPSU4gdXNlcnMgdSBPTiB1LmlkID0gZ2MudXNlcl9pZFxyXG4tLSAgICAgSk9JTiBwcm9kdWN0cyBwIE9OIGdkLnByb2R1Y3RfaWQgPSBwLmlkXHJcbi0tICAgICBKT0lOIHByb2R1Y3RfbmFtZXMgcG4gT04gcC5uYW1lX2lkID0gcG4uaWRcclxuLS0gICAgIEpPSU4gZGVsaXZlcnlfdHJhY2tzIGQgT04gZ2MuaWQgPSBkLmdyb3VwX2NhcnRfaWRcclxuLS0gICAgICAgICB3aGVyZSAgZ2Muc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbi0tICAgICAgICAgQU5EIG8uc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbi0tICAgICAgICAgQU5EIGcuc3RhdHVzID0gJ0NPTVBMRVRFRCdcclxuLS0gICAgICAgICBBTkQgby5kZWxldGVkX2F0IElTIE5VTExcclxuLS0gICAgIC0tICAgYW5kICBEQVRFKG8uY3JlYXRlZF9hdCkgIEJFVFdFRU4gJzIwMjYtMDEtMTYnIEFORCAnMjAyNi0wMi0xNidcclxuLS0gICAgICAgYW5kICBEQVRFKG8uY3JlYXRlZF9hdCkgICBCRVRXRUVOICcyMDI1LTA5LTIwJyBBTkQgJzIwMjYtMDItMjAnXHJcblxyXG5cclxuXHJcblxyXG5TRUxFQ1RcclxuZGlzdGluY3QgXHJcbi0tIGRhdGVfdHJ1bmMoJ3dlZWsnLCBvLmNyZWF0ZWRfYXQpLFxyXG4gICAgdS5uYW1lIEFTIG5hbWUsIFxyXG4gICAgdS5waG9uZSBBUyBwaG9uZVxyXG4gICAgXHJcbkZST00gXHJcbiAgICBncm91cF9kZWFscyBnZCBcclxuSk9JTiBcclxuICAgIGdyb3VwcyBnIE9OIGcuZ3JvdXBfZGVhbHNfaWQgPSBnZC5pZFxyXG5KT0lOIFxyXG4gICAgZ3JvdXBzX2NhcnRzIGdjIE9OIGdjLmdyb3VwX2lkID0gZy5pZCBBTkQgZy5jcmVhdGVkX2J5ID0gZ2MudXNlcl9pZFxyXG5KT0lOIFxyXG4gICAgb3JkZXJzIG8gT04gby5ncm91cHNfY2FydHNfaWQgPSBnYy5pZCBcclxuSk9JTiBcclxuICAgIHVzZXJzIHUgT04gdS5pZCA9IGdjLnVzZXJfaWRcclxuSk9JTiBcclxuICAgIHByb2R1Y3RzIHAgT04gZ2QucHJvZHVjdF9pZCA9IHAuaWRcclxuSk9JTiBcclxuICAgIHByb2R1Y3RfbmFtZXMgcG4gT04gcC5uYW1lX2lkID0gcG4uaWRcclxuSk9JTiBcclxuICAgIGRlbGl2ZXJ5X3RyYWNrcyBkIE9OIGdjLmlkID0gZC5ncm91cF9jYXJ0X2lkXHJcbldIRVJFICBcclxuICAgIGdjLnN0YXR1cyA9ICdDT01QTEVURUQnIFxyXG4gICAgQU5EIG8uc3RhdHVzID0gJ0NPTVBMRVRFRCcgXHJcbiAgICBBTkQgZy5zdGF0dXMgPSAnQ09NUExFVEVEJ1xyXG4gICAgQU5EIG8uZGVsZXRlZF9hdCBJUyBOVUxMXHJcbiAgICBBTkQgby5jcmVhdGVkX2F0IEJFVFdFRU4gJzIwMjUtMDktMjAnIEFORCAnMjAyNi0wMi0yMCcgXHJcbkdST1VQIEJZIFxyXG4gICAgdS5pZCwgdS5uYW1lLCB1LnBob25lLCBkYXRlX3RydW5jKCd3ZWVrJywgby5jcmVhdGVkX2F0KVxyXG5IQVZJTkcgXHJcbiAgICBDT1VOVChESVNUSU5DVCBvLmlkKSA-PSAyXHJcbk9SREVSIEJZIFxyXG4gICAgdS5uYW1lIiwidGVtcGxhdGUtdGFncyI6e319fSwiZGlzcGxheSI6InRhYmxlIiwiZGlzcGxheUlzTG9ja2VkIjp0cnVlLCJwYXJhbWV0ZXJzIjpbXSwidmlzdWFsaXphdGlvbl9zZXR0aW5ncyI6e319",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:54:07.203000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/d816c7fd-f1e1-40d1-aa73-57d8309482d6.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:54:13.250780+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/7e168012-610e-4ae3-8d20-02d592b1e6e4.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/66/?native_filters_key=Y0a9RQKKdwtUQLVl2jmR1Z5lzml2_A7ROuAhZc7wKmFn2Inokd43s4BJzs2DlGjO",
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



