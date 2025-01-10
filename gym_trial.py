from mlagents_envs.environment import UnityEnvironment

# Load the Unity environment (pre-built executable)
env = UnityEnvironment(file_name="path_to_your_unity_env")

# Interact with the environment
env.reset()
behavior_name = list(env.behavior_specs.keys())[0]
decision_steps, terminal_steps = env.get_steps(behavior_name)
print("Number of agents:", len(decision_steps))
env.close()
