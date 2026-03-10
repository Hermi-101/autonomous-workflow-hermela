import json
import os
from templates import AGENT_TEMPLATE

def build_meta_agent():
    
    input_path = os.path.join(os.path.dirname(__file__), "..", "workflow.json")
    with open(input_path, "r") as f:
        workflows = json.load(f)

    print(f"Meta-Agent: Found {len(workflows)} candidate workflows.")

    
    high_value_workflows = [w for w in workflows if w['persistence']['is_2day']]
    
    if not high_value_workflows:
        print("No high-persistence workflows found. Generating samples from all.")
        high_value_workflows = workflows[:2] 

    
    for idx, wf in enumerate(high_value_workflows):
        workflow_id = f"WF-{idx:03d}"
        
        
        rendered_code = AGENT_TEMPLATE.format(
            workflow_id=workflow_id,
            employee_id=wf['employee_id'],
            signature=wf['pattern_signature'],
            steps_list=json.dumps(wf['steps'], indent=8)
        )
        
       
        file_name = f"agent_{workflow_id}_{wf['employee_id']}.py"
        output_path = os.path.join(os.path.dirname(__file__), "..", "generated_agents", file_name)
        
        
        with open(output_path, "w") as f:
            f.write(rendered_code)
            
        print(f"Success: Dynamically built autonomous agent: {file_name}")

if __name__ == "__main__":
    build_meta_agent()