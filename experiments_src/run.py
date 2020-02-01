import sys
import json
import uuid

experiment_params_file =  str(sys.argv[0]) 
experiment_params = json.load(open(experiment_params_file))
experiment_id = uuid.uuid4()
